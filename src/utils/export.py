"""CSV and JSON export utilities"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from rich.console import Console

console = Console()


class CSVExporter:
    """Handles CSV export functionality"""

    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

    def flatten_profile_data(self, profile: Dict) -> Dict:
        """Flatten nested profile data for CSV export - dynamically handles all fields"""
        flat_data = {}

        # Basic profile information
        flat_data['username'] = profile.get('publicIdentifier', '')
        flat_data['profile_url'] = f"https://linkedin.com/in/{profile.get('publicIdentifier', '')}" if profile.get('publicIdentifier') else ''

        # Simple fields (strings, numbers, booleans)
        simple_fields = [
            'firstName', 'lastName', 'fullName', 'headline', 'urn',
            'followerCount', 'connectionsCount', 'profileID',
            'creator', 'qualityProfile', 'isTopVoice', 'premium', 'influencer',
            'joined', 'about', 'backgroundImageURL', 'profilePictureURL'
        ]

        for field in simple_fields:
            if field in profile:
                flat_data[field] = profile[field]

        # Handle location (nested object)
        location = profile.get('location')
        if location and isinstance(location, dict):
            flat_data['location_city'] = location.get('city', '')
            flat_data['location_region'] = location.get('region', '')
            flat_data['location_country'] = location.get('countryName', '')
            flat_data['location_full'] = location.get('fullLocation', '')
            flat_data['location_countryCode'] = location.get('countryCode', '')
        elif location:
            flat_data['location_full'] = str(location)

        # Handle CurrentPositions (array)
        current_positions = profile.get('CurrentPositions', [])
        if current_positions and isinstance(current_positions, list):
            flat_data['current_companies'] = " | ".join([
                pos.get('name', '') for pos in current_positions if isinstance(pos, dict) and pos.get('name')
            ])

        # Handle experience array
        experiences = profile.get('experience', [])
        if experiences and isinstance(experiences, list):
            exp_list = []
            for i, exp in enumerate(experiences[:5]):  # Top 5 experiences
                if not isinstance(exp, dict):
                    continue

                company = exp.get('companyName', '')
                title = exp.get('title', '')
                duration = exp.get('duration', '')

                # If this experience has nested positions, use those
                positions = exp.get('positions', [])
                if positions and isinstance(positions, list):
                    for pos in positions[:1]:  # Get first position
                        if isinstance(pos, dict):
                            title = pos.get('title', title)
                            duration = pos.get('duration', duration)
                            break

                if title and company:
                    exp_entry = f"{title} at {company}"
                    if duration:
                        exp_entry += f" ({duration})"
                    exp_list.append(exp_entry)

            flat_data['top_5_experiences'] = " | ".join(exp_list)
            flat_data['total_experience_count'] = len(experiences)

        # Handle positions array (alternative format)
        positions = profile.get('positions')
        if positions and isinstance(positions, list) and not experiences:
            pos_list = []
            for pos in positions[:5]:
                if isinstance(pos, dict):
                    title = pos.get('jobTitle', '')
                    company = pos.get('company', '')
                    if title:
                        pos_list.append(f"{title}" + (f" at {company}" if company else ""))
            if pos_list:
                flat_data['top_5_positions'] = " | ".join(pos_list)
                flat_data['total_positions_count'] = len(positions)

        # Handle education array
        educations = profile.get('education')
        if educations and isinstance(educations, list):
            edu_list = []
            for edu in educations[:3]:  # Top 3 educations
                if not isinstance(edu, dict):
                    continue

                school = edu.get('schoolName', '') or edu.get('university', '')
                degree = edu.get('degreeName', '') or edu.get('degree', '')
                duration = edu.get('duration', '')

                if school:
                    edu_entry = degree if degree else school
                    if degree and school:
                        edu_entry = f"{degree} - {school}"
                    if duration:
                        edu_entry += f" ({duration})"
                    edu_list.append(edu_entry)

            if edu_list:
                flat_data['top_3_education'] = " | ".join(edu_list)
                flat_data['total_education_count'] = len(educations)

        # Handle skills array
        skills = profile.get('skills', [])
        if skills and isinstance(skills, list):
            # Top 10 skills
            skill_names = []
            skill_endorsements = []

            for skill in skills[:10]:
                if isinstance(skill, dict):
                    skill_name = skill.get('skillName', '')
                    if skill_name:
                        skill_names.append(skill_name)
                        endorsement_count = skill.get('endorsementsCount', 0)
                        skill_endorsements.append(f"{skill_name} ({endorsement_count})")

            if skill_names:
                flat_data['top_10_skills'] = ", ".join(skill_names)
                flat_data['top_10_skills_with_endorsements'] = " | ".join(skill_endorsements)
                flat_data['total_skills_count'] = len(skills)

        # Handle certifications array
        certifications = profile.get('certifications', [])
        if certifications and isinstance(certifications, list):
            cert_names = []
            for cert in certifications[:5]:  # Top 5 certifications
                if isinstance(cert, dict):
                    cert_name = cert.get('certificationName', '') or cert.get('name', '')
                    if cert_name:
                        cert_names.append(cert_name)

            if cert_names:
                flat_data['top_5_certifications'] = " | ".join(cert_names)
                flat_data['total_certifications_count'] = len(certifications)

        # Handle supported locales
        locales = profile.get('supportedLocales', [])
        if locales and isinstance(locales, list):
            locale_strs = []
            for locale in locales:
                if isinstance(locale, dict):
                    lang = locale.get('language', '')
                    country = locale.get('country', '')
                    if lang and country:
                        locale_strs.append(f"{lang}_{country}")
            if locale_strs:
                flat_data['supported_locales'] = ", ".join(locale_strs)

        # Handle contact info
        contact_info = profile.get('contactInfo')
        if contact_info and isinstance(contact_info, dict):
            # Email address - can be string, list, or null
            email = contact_info.get('emailAddress')
            if email:
                if isinstance(email, list):
                    flat_data['email'] = ", ".join([str(e) for e in email if e])
                else:
                    flat_data['email'] = str(email)

            # Phone number - can be string, list, or null
            phone = contact_info.get('phoneNumber')
            if phone:
                if isinstance(phone, list):
                    flat_data['phone'] = ", ".join([str(p) for p in phone if p])
                else:
                    flat_data['phone'] = str(phone)

            # Websites - array of objects
            websites = contact_info.get('websites', [])
            if websites and isinstance(websites, list):
                website_urls = []
                website_details = []
                for site in websites:
                    if isinstance(site, dict):
                        url = site.get('url', '')
                        category = site.get('category', '')
                        if url:
                            website_urls.append(url)
                            if category:
                                website_details.append(f"{url} ({category})")
                            else:
                                website_details.append(url)

                if website_urls:
                    flat_data['websites'] = " | ".join(website_urls)
                    flat_data['websites_detailed'] = " | ".join(website_details)
                    flat_data['websites_count'] = len(websites)

        return flat_data

    def export_to_csv(self, profiles_data: List[Dict], filename: Optional[str] = None) -> str:
        """Export scraped profiles to CSV with dynamic columns based on available data"""
        if not profiles_data:
            console.print("[yellow]No data to export![/]")
            return ""

        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"linkedin_profiles_{timestamp}.csv"
        else:
            if not filename.endswith(".csv"):
                filename += ".csv"
            filename = filename.replace(" ", "_")

        output_path = Path(self.output_dir) / filename

        try:
            # Flatten all profile data
            flattened_data = [self.flatten_profile_data(profile) for profile in profiles_data]

            # Get all unique keys and check if they have non-empty values
            all_fields = set()
            field_has_data = {}

            for data in flattened_data:
                for key, value in data.items():
                    all_fields.add(key)
                    # Check if this field has any non-empty data
                    if key not in field_has_data:
                        field_has_data[key] = False
                    # Consider a field as having data if it's not empty/None/0/False (but keep 0 for counts)
                    if value and (value != '' or isinstance(value, (int, float, bool))):
                        if not (isinstance(value, bool) and not value):  # Exclude False booleans
                            field_has_data[key] = True

            # Only include fields that have data in at least one profile
            fieldnames = [field for field in sorted(all_fields) if field_has_data.get(field, False)]

            # Ensure username and profile_url are always first if they exist
            priority_fields = ['username', 'profile_url', 'firstName', 'lastName', 'fullName', 'headline']
            ordered_fieldnames = []

            for pf in priority_fields:
                if pf in fieldnames:
                    ordered_fieldnames.append(pf)
                    fieldnames.remove(pf)

            ordered_fieldnames.extend(fieldnames)

            # Write to CSV with only non-empty columns
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=ordered_fieldnames, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(flattened_data)

            console.print(f"\n[bold green]✓[/] Data exported to: [cyan]{output_path}[/]")
            console.print(f"[dim]Total profiles exported: {len(flattened_data)}[/]")
            console.print(f"[dim]Columns in CSV: {len(ordered_fieldnames)}[/]")
            return str(output_path)

        except Exception as e:
            console.print(f"[bold red]Error exporting to CSV:[/] {str(e)}")
            import traceback
            traceback.print_exc()
            return ""

    def export_to_json(self, profiles_data: List[Dict], filename: Optional[str] = None) -> str:
        """Export scraped profiles to JSON"""
        if not profiles_data:
            console.print("[yellow]No data to export![/]")
            return ""

        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"linkedin_profiles_{timestamp}.json"
        else:
            if not filename.endswith(".json"):
                filename += ".json"
            filename = filename.replace(" ", "_")

        output_path = Path(self.output_dir) / filename

        try:
            # Write to JSON with pretty printing
            with open(output_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(profiles_data, jsonfile, indent=2, ensure_ascii=False)

            console.print(f"\n[bold green]✓[/] Data exported to: [cyan]{output_path}[/]")
            console.print(f"[dim]Total profiles exported: {len(profiles_data)}[/]")
            return str(output_path)

        except Exception as e:
            console.print(f"[bold red]Error exporting to JSON:[/] {str(e)}")
            import traceback
            traceback.print_exc()
            return ""
