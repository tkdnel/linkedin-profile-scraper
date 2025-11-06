"""Display utilities for the CLI"""

import os
from typing import List, Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()


def clear_terminal():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_header(title: str, config=None, profiles_count: int = 0):
    """Show header with config and branding"""
    clear_terminal()

    header = Text()

    # Title section
    header.append("LinkedIn Profile Scraper", style="bold cyan")
    header.append(f"  •  {title}", style="bold white")

    if profiles_count > 0:
        header.append(f"  •  ", style="dim")
        header.append(f"{profiles_count} profiles scraped", style="bold green")

    # Config section
    if config:
        api_key = config.api_key
        masked = f"{api_key[:8]}...{api_key[-6:]}" if len(api_key) > 14 else "***...***"

        header.append("\n\n", style="dim")
        header.append("⚙️  Configuration\n", style="bold white")
        header.append(f"   API Key: ", style="dim")
        header.append(f"{masked}", style="cyan")
        header.append(f"  •  ", style="dim")
        header.append(f"Concurrent: ", style="dim")
        header.append(f"{config.max_concurrent}", style="cyan")
        header.append(f"  •  ", style="dim")
        header.append(f"Retries: ", style="dim")
        header.append(f"{config.max_retries}", style="cyan")

    # Branding section
    header.append("\n\n", style="dim")
    header.append("💙 Made with love by ", style="dim")
    header.append("LinkdAPI Team", style="bold cyan")
    header.append("\n", style="dim")
    header.append("   📧 support@linkdapi.com  •  ", style="dim")
    header.append("🌐 linkdapi.com  •  ", style="dim")
    header.append("⭐ github.com/linkdapi", style="dim")

    console.print(Panel(header, box=box.DOUBLE, border_style="cyan", padding=(1, 2)))
    console.print()


def display_summary(profiles_data: List[Dict]):
    """Display summary table of profiles"""
    if not profiles_data:
        return

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("Username", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Headline", style="yellow", max_width=50)
    table.add_column("Location", style="blue", max_width=25)

    for profile in profiles_data[:15]:  # Show top 15
        location = profile.get('location', '')
        if isinstance(location, dict):
            location = location.get('fullLocation', '')

        table.add_row(
            profile.get('publicIdentifier', 'N/A'),
            profile.get('fullName', 'N/A'),
            (profile.get('headline') or 'N/A')[:50],
            str(location)[:25] if location else 'N/A'
        )

    console.print(table)

    if len(profiles_data) > 15:
        console.print(f"\n[dim]Showing 15 of {len(profiles_data)} profiles[/]")
