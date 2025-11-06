#!/usr/bin/env python3
"""LinkedIn Profile Scraper CLI"""

import asyncio
import sys
import questionary
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.cli.display import console, show_header, display_summary
from src.cli.menu import show_main_menu, select_data_options, select_export_format, load_usernames
from src.scraper.scraper import ProfileScraper
from src.utils.export import CSVExporter
from src.utils.config import Config


def scrape_profiles(scraper: ProfileScraper, usernames: list, config, profiles_count: int) -> bool:
    """Scrape profiles"""
    if not usernames:
        return False

    # Skip duplicates
    already_scraped = scraper.get_scraped_usernames()
    usernames = [u for u in usernames if u.lower() not in already_scraped]

    if not usernames:
        console.print("[yellow]All usernames already scraped[/]")
        input("\nPress Enter...")
        return False

    console.print(f"[green]→ Loaded {len(usernames)} username(s)[/]")

    # Select data to scrape
    data_options = select_data_options(config, profiles_count)

    # Confirm
    if not questionary.confirm(f"Scrape {len(usernames)} profiles?").ask():
        return False

    # Scrape
    scraper.clear_failed_profiles()
    asyncio.run(scraper.scrape_profiles(usernames, data_options))
    return True


def main():
    """Main entry point"""
    config = Config()
    scraper = ProfileScraper(
        api_key=config.api_key,
        max_concurrent=config.max_concurrent,
        max_retries=config.max_retries,
        retry_delay=config.retry_delay
    )
    exporter = CSVExporter(output_dir=config.output_dir)
    has_unsaved_data = False  # Track if data needs saving

    try:
        while True:
            profiles = scraper.get_profiles_data()
            choice = show_main_menu(config, len(profiles))

            if choice == "Scrape from usernames.txt":
                usernames = load_usernames("usernames.txt")
                if scrape_profiles(scraper, usernames, config, len(profiles)):
                    profiles = scraper.get_profiles_data()
                    has_unsaved_data = True  # Mark as unsaved
                    show_header("Done", config, len(profiles))
                    display_summary(profiles)
                    input("\nPress Enter...")

            elif choice == "Scrape from custom file":
                file_path = questionary.text("Enter file path:").ask()
                if file_path:
                    usernames = load_usernames(file_path)
                    if scrape_profiles(scraper, usernames, config, len(profiles)):
                        profiles = scraper.get_profiles_data()
                        has_unsaved_data = True  # Mark as unsaved
                        show_header("Done", config, len(profiles))
                        display_summary(profiles)
                        input("\nPress Enter...")

            elif choice == "Enter usernames manually":
                input_str = questionary.text("Enter usernames (comma-separated):").ask()
                if input_str:
                    usernames = [u.strip() for u in input_str.split(",") if u.strip()]
                    if scrape_profiles(scraper, usernames, config, len(profiles)):
                        profiles = scraper.get_profiles_data()
                        has_unsaved_data = True  # Mark as unsaved
                        show_header("Done", config, len(profiles))
                        display_summary(profiles)
                        input("\nPress Enter...")

            elif choice == "View scraped profiles":
                if profiles:
                    show_header("Scraped Profiles", config, len(profiles))
                    display_summary(profiles)
                else:
                    show_header("Scraped Profiles", config, 0)
                    console.print("[yellow]No profiles scraped yet[/]")
                input("\nPress Enter...")

            elif choice == "Export data":
                if not profiles:
                    console.print("[yellow]No data to export[/]")
                    input("\nPress Enter...")
                    continue

                fmt = select_export_format(config, len(profiles))
                if fmt == "csv":
                    filename = questionary.text("Filename (or Enter for auto):").ask()
                    if filename is not None:  # User didn't cancel
                        exporter.export_to_csv(profiles, filename or None)
                        has_unsaved_data = False  # Mark as saved
                        input("\nPress Enter...")
                elif fmt == "json":
                    filename = questionary.text("Filename (or Enter for auto):").ask()
                    if filename is not None:  # User didn't cancel
                        exporter.export_to_json(profiles, filename or None)
                        has_unsaved_data = False  # Mark as saved
                        input("\nPress Enter...")

            elif choice == "Exit":
                # Check for unsaved data
                if has_unsaved_data and profiles:
                    console.print("\n[yellow]⚠️  You have unsaved data![/]")
                    save_choice = questionary.confirm("Would you like to save before exiting?", default=True).ask()

                    if save_choice:
                        # Prompt for export
                        fmt = select_export_format(config, len(profiles))
                        if fmt == "csv":
                            filename = questionary.text("Filename (or Enter for auto):").ask()
                            if filename is not None:
                                exporter.export_to_csv(profiles, filename or None)
                        elif fmt == "json":
                            filename = questionary.text("Filename (or Enter for auto):").ask()
                            if filename is not None:
                                exporter.export_to_json(profiles, filename or None)
                        # Continue to exit regardless

                console.print("\n[cyan]Goodbye![/]")
                sys.exit(0)

    except KeyboardInterrupt:
        profiles = scraper.get_profiles_data()
        if has_unsaved_data and profiles:
            console.print("\n\n[yellow]⚠️  You have unsaved data![/]")
            save_choice = questionary.confirm("Would you like to save before exiting?", default=True).ask()
            if save_choice:
                fmt = select_export_format(config, len(profiles))
                if fmt == "csv":
                    filename = questionary.text("Filename (or Enter for auto):").ask()
                    if filename is not None:
                        exporter.export_to_csv(profiles, filename or None)
                elif fmt == "json":
                    filename = questionary.text("Filename (or Enter for auto):").ask()
                    if filename is not None:
                        exporter.export_to_json(profiles, filename or None)

        console.print("\n[cyan]Goodbye![/]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
