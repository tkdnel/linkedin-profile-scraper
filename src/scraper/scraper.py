"""Core scraping logic"""

from typing import List, Dict, Set
import asyncio

from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.console import Console, Group
from linkdapi import AsyncLinkdAPI
from collections import deque
from rich.panel import Panel
from rich.live import Live

from ..api.client import LinkedInAPIClient, ScrapeStatus

console = Console()


class ProfileScraper:
    """Handles the profile scraping operations"""

    def __init__(self, api_key: str, max_concurrent: int = 10, max_retries: int = 3, retry_delay: int = 5):
        self.api_client = LinkedInAPIClient(api_key, max_retries=max_retries, retry_delay=retry_delay)
        self.max_concurrent = max_concurrent
        self.profiles_data: List[Dict] = []
        self.failed_profiles: List[Dict] = []  # Track failed profiles
        self.log_buffer = deque(maxlen=30)  # Keep only last 30 log lines
        self.live_display = None  # Will be set during scraping
        self.progress = None  # Will be set during scraping

    def _add_log(self, message: str):
        """Add a log message to the buffer"""
        self.log_buffer.append(message)
        if self.live_display and self.progress:
            try:
                self.live_display.update(Group(self.progress, self._get_log_panel()))
            except:
                pass

    def _get_log_panel(self):
        """Create a panel with the last 20 log lines"""
        if not self.log_buffer:
            return Panel("", title="[dim]Activity Log[/]", border_style="dim")

        log_text = "\n".join(list(self.log_buffer))
        panel_height = min(len(self.log_buffer) + 2, 22)
        return Panel(log_text, title="[dim]Activity Log[/]", height=panel_height, border_style="dim")

    async def scrape_profiles(self, usernames: List[str], data_options: Set[str] = None):
        """
        Scrape multiple profiles asynchronously

        Args:
            usernames: List of LinkedIn usernames to scrape
            data_options: Set of data types to fetch (overview, details, experience, education, skills, certifications)
        """
        if data_options is None:
            data_options = {'overview', 'details', 'experience', 'education', 'skills', 'certifications'}

        self.log_buffer.clear()
        data_list = [opt.title() for opt in sorted(data_options) if opt != 'overview']
        if data_list:
            self._add_log(f"[cyan]→ Fetching: Overview + {', '.join(data_list)}[/]")

        self._add_log(f"[cyan]→ Starting scrape of {len(usernames)} profile{'s' if len(usernames) != 1 else ''}...[/]")
        self.api_client.log_callback = self._add_log

        async with AsyncLinkdAPI(self.api_client.api_key) as api:
            progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn()
            )
            task = progress.add_task(
                "[cyan]Scraping profiles...",
                total=len(usernames)
            )
            with Live(Group(progress, self._get_log_panel()), console=console, refresh_per_second=50) as live:
                self.live_display = live
                self.progress = progress
                batch_size = self.max_concurrent

                for i in range(0, len(usernames), batch_size):
                    batch = usernames[i:i + batch_size]
                    results = await asyncio.gather(
                        *[self.api_client.fetch_profile_data(api, username, data_options) for username in batch],
                        return_exceptions=True
                    )
                    for username, result in zip(batch, results):
                        if isinstance(result, Exception):
                            error_msg = str(result)
                            # Check if this is a rate limit exception that slipped through
                            if "429" in error_msg or "too many requests" in error_msg.lower():
                                self._add_log(f"[red]✗ ({username}) Rate limit exceeded (exhausted all retries)[/]")
                                self.failed_profiles.append({'username': username, 'error': 'Rate limit exceeded'})
                            else:
                                clean_error = error_msg.replace("Request failed: ", "").replace("API Error: ", "").replace("Client error", "").strip()
                                self._add_log(f"[red]✗ ({username}) {clean_error[:70]}[/]")
                                self.failed_profiles.append({'username': username, 'error': error_msg})
                        else:
                            status, data_or_error = result
                            if status == ScrapeStatus.SUCCESS:
                                self.profiles_data.append(data_or_error)
                                self._add_log(f"[green]✓ ({username}) Profile scraped successfully[/]")

                            elif status == ScrapeStatus.NOT_FOUND:
                                self._add_log(f"[red]✗ ({username}) Profile not found[/]")
                                self.failed_profiles.append({'username': username, 'error': f'Not found: {data_or_error}'})

                            elif status == ScrapeStatus.RATE_LIMITED:
                                self._add_log(f"[red]✗ ({username}) Rate limit exceeded (exhausted all retries)[/]")
                                self.failed_profiles.append({'username': username, 'error': 'Rate limit exceeded'})

                            elif status == ScrapeStatus.ERROR:
                                clean_error = data_or_error.replace("Request failed: ", "").replace("API Error: ", "").replace("Client error", "").strip()
                                self._add_log(f"[red]✗ ({username}) {clean_error[:70]}[/]")
                                self.failed_profiles.append({'username': username, 'error': data_or_error})

                        progress.update(task, advance=1)
                        live.update(Group(progress, self._get_log_panel()))

                    if i + batch_size < len(usernames):
                        await asyncio.sleep(0.5)

                self.live_display = None
                self.progress = None

        console.print(f"\n[bold cyan]{'='*60}[/]")
        console.print(f"[bold green]✓ Scraping completed![/]")
        console.print(f"[green]  • Successfully scraped: {len(self.profiles_data)} profile{'s' if len(self.profiles_data) != 1 else ''}[/]")

        if self.failed_profiles:
            console.print(f"[red]  • Failed: {len(self.failed_profiles)} profile{'s' if len(self.failed_profiles) != 1 else ''}[/]")
            console.print(f"\n[yellow]Failed profiles:[/]")
            for failed in self.failed_profiles[:5]:
                console.print(f"  [red]✗[/] [dim]{failed['username']}:[/] {failed['error'][:80]}")
            if len(self.failed_profiles) > 5:
                console.print(f"  [dim]... and {len(self.failed_profiles) - 5} more[/]")

        console.print(f"[bold cyan]{'='*60}[/]\n")

    def get_profiles_data(self) -> List[Dict]:
        """Get the scraped profiles data"""
        return self.profiles_data

    def get_scraped_usernames(self) -> Set[str]:
        """Get set of already scraped usernames"""
        usernames = set()
        for profile in self.profiles_data:
            username = profile.get('publicIdentifier')
            if username:
                usernames.add(username.lower())
        return usernames

    def get_failed_profiles(self) -> List[Dict]:
        """Get list of failed profiles"""
        return self.failed_profiles

    def clear_failed_profiles(self):
        """Clear the failed profiles list"""
        self.failed_profiles = []

    def clear_data(self):
        """Clear the profiles data"""
        self.profiles_data = []
        self.failed_profiles = []
