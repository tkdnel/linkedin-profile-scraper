"""Interactive menu with arrow key navigation"""

import questionary
from typing import Optional, List

from .display import console, show_header

# Simple questionary style
STYLE = questionary.Style([
    ('pointer', 'fg:#00bcd4 bold'),
    ('highlighted', 'fg:#00bcd4 bold'),
    ('answer', 'fg:#4caf50 bold'),
])


def show_main_menu(config, profiles_count: int) -> str:
    """Show main menu"""
    show_header("Main Menu", config, profiles_count)

    choices = [
        "Scrape from usernames.txt",
        "Scrape from custom file",
        "Enter usernames manually",
        "View scraped profiles",
        "Export data",
        "Exit"
    ]

    choice = questionary.select(
        "Choose action:",
        choices=choices,
        style=STYLE,
        use_arrow_keys=True
    ).ask()

    return choice or "Exit"


def select_data_options(config, profiles_count: int) -> set:
    """Select which data to scrape"""
    show_header("Select Data", config, profiles_count)

    console.print("[dim]Use Space to select, Enter to confirm[/]\n")

    options = questionary.checkbox(
        "What to scrape? (Overview always included):",
        choices=[
            {"name": "Details & About", "value": "details"},
            {"name": "Experience", "value": "experience"},
            {"name": "Education", "value": "education"},
            {"name": "Skills", "value": "skills"},
            {"name": "Certifications", "value": "certifications"},
            {"name": "Contact Info", "value": "contact"},
        ],
        style=STYLE
    ).ask()

    selected = {'overview'}
    if options:
        selected.update(options)
    return selected


def select_export_format(config, profiles_count: int) -> str:
    """Select export format"""
    show_header("Export", config, profiles_count)

    choice = questionary.select(
        "Choose format:",
        choices=["CSV", "JSON", "Cancel"],
        style=STYLE,
        use_arrow_keys=True
    ).ask()

    return (choice or "Cancel").lower()


def load_usernames(file_path: str) -> List[str]:
    """Load usernames from file"""
    try:
        with open(file_path, 'r') as f:
            usernames = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        if not usernames:
            console.print(f"[yellow]File is empty: {file_path}[/]")

        return usernames
    except FileNotFoundError:
        console.print(f"[red]File not found: {file_path}[/]")
        return []
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")
        return []
