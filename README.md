# LinkedIn Profile Scraper - Easy & Fast LinkedIn Data Extraction Tool

A powerful, user-friendly **LinkedIn profile scraper** and **LinkedIn data scraper** that extracts comprehensive profile information using the [LinkdAPI](https://linkdapi.com). Perfect for recruiters, marketers, researchers, and anyone needing to collect LinkedIn profile data at scale.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## 🎬 See It In Action

Watch the scraper extract **320 LinkedIn profiles in seconds** with async processing!

<video className="center" src="https://github-production-user-asset-6210df.s3.amazonaws.com/193476718/510903259-81bcc6ce-7cf8-445c-b150-f7f106f92a4d.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251106%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251106T172116Z&X-Amz-Expires=300&X-Amz-Signature=5b4bff1d64f1b95778a21d103d47973b5c8137727fb5831bbd2fb5b206d559c9&X-Amz-SignedHeaders=host"></video>


*🚀 The demo shows real-time scraping with live progress tracking, intelligent error handling, and batch processing at scale. Experience the speed of parallel API requests handling 10+ profiles simultaneously!*

**What you'll see in the demo:**
- ⚡ Blazing-fast async batch processing
- 📊 Real-time progress bars and activity logs
- 🎯 Smart retry logic for rate limits
- ✅ Successful scraping of 320 profiles
- 💾 Automatic data export to CSV

---

## 🌟 Why This LinkedIn Scraper?

- ✅ **No Coding Required** - Beautiful interactive menu with arrow-key navigation
- ⚡ **Blazing Fast** - Async processing handles multiple profiles simultaneously (10x-40x faster) - *See the [demo](#-see-it-in-action) scraping 320 profiles!*
- 🎯 **Comprehensive Data** - Scrapes profiles, experience, education, skills, certifications, and contact info
- 💾 **Smart Export** - Export to CSV or JSON with automatic data flattening
- 🛡️ **Safe & Reliable** - Built-in retry logic, error handling, and duplicate prevention
- 🎨 **Beautiful UI** - Rich terminal interface with real-time progress tracking
- 💙 **Made with love by LinkdAPI Team**

---

## 📋 Table of Contents

- [See It In Action](#-see-it-in-action)
- [What You Can Scrape](#what-you-can-scrape)
- [Quick Start (Non-Developers)](#quick-start-non-developers)
- [Installation Guide](#installation-guide)
  - [Windows](#for-windows-users)
  - [macOS/Linux](#for-macos--linux-users)
- [How to Use](#how-to-use)
- [Configuration Options](#configuration-options)
- [Features in Detail](#features-in-detail)
- [CSV Output Format](#csv-output-format)
- [Tips & Best Practices](#tips--best-practices)
- [Troubleshooting](#troubleshooting)
- [Common Use Cases](#common-use-cases)
- [Support & Links](#support--links)

---

## 🎯 What You Can Scrape

This **LinkedIn profile scraper** extracts:

| Data Type | What's Included |
|-----------|----------------|
| **👤 Basic Info** | Full name, headline, location, profile URL |
| **📝 About** | Summary/bio section |
| **💼 Experience** | Job titles, companies, durations, descriptions |
| **🎓 Education** | Schools, degrees, fields of study, dates |
| **⚡ Skills** | All skills with endorsement counts |
| **🏆 Certifications** | Certificates and professional licenses |
| **📊 Stats** | Follower count, connection count |
| **📞 Contact** | Email, phone numbers, websites (when available) |

---

## 🚀 Quick Start (Non-Developers)

**Never coded before? No problem!** Watch our [demo video](#-see-it-in-action) to see it in action, then follow these simple steps:

### Step 1: Get Your API Key
1. Visit [linkdapi.com](https://linkdapi.com)
2. Sign up for a free account
3. Copy your API key from the dashboard

### Step 2: Download & Setup
```bash
# Download the project (or download ZIP from GitHub)
git clone https://github.com/linkdapi/linkedin-profile-scraper.git
cd linkedin-profile-scraper

# Run the automatic setup (installs everything for you)
chmod +x setup.sh
./setup.sh
```

### Step 3: Add Your API Key
1. Open `config.ini` file in any text editor (Notepad, TextEdit, etc.)
2. Replace `YOUR_API_KEY_HERE` with your actual API key
3. Save the file

### Step 4: Add LinkedIn Usernames
1. Open `usernames.txt` in a text editor
2. Add LinkedIn usernames (one per line)
   - **How to find username**: From `linkedin.com/in/billgates` → use `billgates`
3. Save the file

### Step 5: Run the Scraper
```bash
# Activate the environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Start the scraper
python3 main.py
```

### Step 6: Use the Menu
- Use **↑↓ arrow keys** to navigate
- Press **Enter** to select
- Choose "Scrape from usernames.txt"
- Select what data you want (use **Space** to check/uncheck)
- Press **Enter** to confirm and start scraping
- When done, choose "Export data" to save as CSV or JSON

**That's it! Your data will be in the `output/` folder** 🎉

---

## 📦 Installation Guide

### Prerequisites

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **LinkdAPI Account** ([Sign up free](https://linkdapi.com))
- Internet connection

### For Windows Users

1. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation

2. **Open Command Prompt** (cmd)
   ```bash
   # Navigate to project folder
   cd path\to\linkedin-profile-scraper

   # Create virtual environment
   python -m venv venv

   # Activate it
   venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Open `config.ini` in Notepad
   - Replace `YOUR_API_KEY_HERE` with your LinkdAPI key
   - Save

4. **Run the scraper**
   ```bash
   python main.py
   ```

### For macOS / Linux Users

1. **Open Terminal**

2. **Run the automated setup**
   ```bash
   cd linkedin-profile-scraper
   chmod +x setup.sh
   ./setup.sh
   ```

   **OR manually install:**
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate it
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   ```bash
   # Edit config file
   nano config.ini
   # OR
   open config.ini  # Opens in default editor on macOS

   # Replace YOUR_API_KEY_HERE with your key, then save
   ```

4. **Run the scraper**
   ```bash
   python3 main.py
   ```

---

## 🎮 How to Use

### Main Menu Options

When you run `python3 main.py`, you'll see:

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  LinkedIn Profile Scraper  •  Main Menu                  ║
║                                                           ║
║  ⚙️  Configuration                                        ║
║     API Key: enterpr...Egag-Q  •  Concurrent: 10  •  Retries: 3 ║
║                                                           ║
║  💙 Made with love by LinkdAPI Team                       ║
║     📧 support@linkdapi.com  •  🌐 linkdapi.com  •  ⭐ github.com/linkdapi ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

Choose action:
❯ Scrape from usernames.txt
  Scrape from custom file
  Enter usernames manually
  View scraped profiles
  Export data
  Exit
```

### Option 1: Scrape from usernames.txt

1. **Prepare your file**: Edit `usernames.txt`, add usernames (one per line)
   ```
   billgates
   satyanadella
   jeffweiner08
   ```

2. **Select this option** from the menu

3. **Choose what to scrape**: Check/uncheck with Space, confirm with Enter
   - ✅ Details & About
   - ✅ Experience
   - ✅ Education
   - ✅ Skills
   - ✅ Certifications
   - ✅ Contact Info

4. **Confirm** and watch the magic happen!

### Option 2: Scrape from Custom File

Same as Option 1, but you can specify any file path:
```
Enter file path: /path/to/my-linkedin-list.txt
```

### Option 3: Enter Usernames Manually

Type usernames separated by commas:
```
Enter usernames (comma-separated): billgates, elonmusk, reidhoffman
```

### Option 4: View Scraped Profiles

See a summary table of all profiles you've scraped in the current session.

### Option 5: Export Data

Choose format:
- **CSV** - Perfect for Excel, Google Sheets, data analysis
- **JSON** - Complete raw data with full structure

Enter custom filename or press Enter for auto-generated name (e.g., `linkedin_profiles_20250106_143022.csv`)

### Option 6: Exit

- If you have **unsaved data**, you'll be prompted:
  ```
  ⚠️  You have unsaved data!
  Would you like to save before exiting? (Y/n)
  ```
- Choose **Yes** to export before exiting
- Choose **No** to exit without saving

---

## ⚙️ Configuration Options

Edit `config.ini` to customize:

```ini
[LINKDAPI]
# Your API key from https://linkdapi.com
api_key = YOUR_API_KEY_HERE

[SETTINGS]
# Number of profiles to scrape simultaneously (1-50)
# Higher = faster but uses more API credits
# Recommended: 10 for free plans, 20-30 for paid plans
max_concurrent_requests = 10

# Where to save exported files
output_directory = output

# How many times to retry failed requests (1-10)
max_retries = 3

# Delay between retries in seconds
# Note: Rate limit errors (429) use exponential backoff automatically
# All other errors use fixed 1-second wait
retry_delay = 2
```

### Performance Tuning

| Plan Type | Recommended `max_concurrent_requests` |
|-----------|--------------------------------------|
| Free Trial | 5-10 |
| Starter | 10-15 |
| Professional | 20-30 |
| Enterprise | 30-50 |

---

## 🔥 Features in Detail

### 1. **Async Batch Processing**
- Processes multiple profiles simultaneously
- Up to **40x faster** than sequential scraping
- Configurable concurrency to match your API plan
- **[Watch it in action](#-see-it-in-action)** - See 320 profiles scraped in seconds!

### 2. **Smart Retry Logic**
- **Rate Limits (429)**: Exponential backoff (2s, 4s, 6s...)
- **Other Errors**: Fixed 1-second wait between retries
- **Non-Retryable Errors**: Skips profiles that don't exist

### 3. **Duplicate Prevention**
- Automatically detects already-scraped usernames
- Prevents wasting API credits on duplicates
- Shows warning with list of duplicates

### 4. **Selective Data Scraping**
- Choose exactly what data you need
- Save API credits by skipping unnecessary fields
- Overview (basic info) is always included

### 5. **Real-Time Progress**
- Live activity log showing each profile as it's scraped
- Success/failure indicators
- Error messages with retry information

### 6. **Beautiful Terminal UI**
- Config always visible in header
- Color-coded messages (green=success, yellow=warning, red=error)
- Progress bars and spinners
- Professional data tables

### 7. **Unsaved Data Protection**
- Tracks whether scraped data has been exported
- Warns you before exiting if data is unsaved
- Works for both Exit button and Ctrl+C

---

## 📊 CSV Output Format

The CSV export includes these columns (only non-empty columns are included):

### Basic Information
- `username` - LinkedIn username
- `profile_url` - Full LinkedIn profile URL
- `firstName`, `lastName`, `fullName` - Name fields
- `headline` - Professional headline
- `profilePictureURL` - Profile photo URL

### Location & Stats
- `location_city`, `location_region`, `location_country`, `location_full`
- `followerCount` - Number of followers
- `connectionsCount` - Number of connections

### Professional Info
- `about` - About/summary section
- `current_companies` - Current employer(s)
- `top_5_experiences` - Recent work positions with durations
- `total_experience_count` - Total jobs listed

### Education
- `top_3_education` - Recent education with degrees
- `total_education_count` - Total education entries

### Skills & Certifications
- `top_10_skills` - Key skills (comma-separated)
- `top_10_skills_with_endorsements` - Skills with endorsement counts
- `total_skills_count` - Total skills listed
- `top_5_certifications` - Recent certifications
- `total_certifications_count` - Total certifications

### Contact Information
- `email` - Email address(es) when available
- `phone` - Phone number(s) when available
- `websites` - Personal/company websites
- `websites_detailed` - Websites with categories

### Other
- `premium` - Premium account status
- `creator` - Creator mode status
- `influencer` - Influencer status
- `joined` - LinkedIn join date

**Note**: Only columns with actual data are included. Empty fields across all profiles are automatically removed.

---

## 💡 Tips & Best Practices

### Finding LinkedIn Usernames

The username is the part after `linkedin.com/in/`:

✅ **Correct Examples:**
- URL: `https://linkedin.com/in/billgates` → Username: `billgates`
- URL: `https://linkedin.com/in/satya-nadella-3145136` → Username: `satya-nadella-3145136`
- URL: `https://linkedin.com/in/jeff-weiner-08` → Username: `jeff-weiner-08`

❌ **Wrong:**
- Don't use the full URL
- Don't include `in/` or any slashes
- Don't use profile IDs from company pages

### Optimizing Scraping Speed

1. **Start Small**: Test with 5-10 profiles first
2. **Monitor Credits**: Check your LinkdAPI dashboard regularly
3. **Adjust Concurrency**: Increase `max_concurrent_requests` if you have a paid plan
4. **Batch Your Work**: Process 50-100 profiles at a time, export, then continue

### Avoiding Rate Limits

1. Don't set `max_concurrent_requests` too high (respect your plan limits)
2. The scraper automatically handles rate limits with exponential backoff
3. If you hit frequent rate limits, reduce concurrency

### Managing Large Lists

For scraping 500+ profiles:

1. **Split into batches**: Create multiple input files with 100 profiles each
2. **Export after each batch**: Don't scrape 1000 profiles without exporting
3. **Use JSON for full data**: CSV flattening may lose some nested details

### Data Accuracy

- **Public profiles only**: Private profiles or profiles with strict privacy settings won't return full data
- **Contact info**: Email/phone are only available if the profile owner made them public
- **Real-time data**: Data is fetched live from LinkedIn via LinkdAPI

---

## 🔧 Troubleshooting

### "Config file not found"
**Solution**: Make sure `config.ini` exists in the same directory as `main.py`

### "Please set your LinkdAPI key"
**Solution**:
1. Open `config.ini`
2. Replace `YOUR_API_KEY_HERE` with your actual API key from [linkdapi.com](https://linkdapi.com)
3. Save the file

### "File not found: usernames.txt"
**Solution**: Create a `usernames.txt` file in the project directory and add LinkedIn usernames (one per line)

### "No module named 'questionary'" or similar
**Solution**:
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### "No data returned" for a username
**Possible causes**:
- Username is incorrect (check spelling)
- Profile doesn't exist or was deleted
- Profile is set to private
- Username format is wrong (should be the part after `linkedin.com/in/`)

### Rate limit errors (429)
**Solution**:
- The scraper automatically handles this with exponential backoff
- If it happens frequently, reduce `max_concurrent_requests` in `config.ini`
- Check your API plan limits at [linkdapi.com/dashboard](https://linkdapi.com/dashboard)

### Scraper is slow
**Solutions**:
1. Increase `max_concurrent_requests` in `config.ini` (if your plan allows)
2. Uncheck data types you don't need (less API calls = faster)
3. Check your internet connection

### Export creates empty CSV
**Cause**: No profiles were successfully scraped
**Solution**:
- Check the scraping logs for errors
- Verify usernames are correct
- Ensure your API key is valid and has credits

### "ModuleNotFoundError: No module named 'linkdapi'"
**Solution**:
```bash
pip install linkdapi --upgrade
```

---

## 📈 Common Use Cases

### 🎯 Recruitment & Talent Sourcing
Scrape candidate profiles from LinkedIn searches:
1. Find candidates on LinkedIn manually
2. Copy their usernames to `usernames.txt`
3. Scrape all profiles at once
4. Export to CSV for your ATS or spreadsheet

### 📊 Market Research & Analysis
Analyze professionals in specific industries:
- Identify skill trends in your industry
- Research competitor employee backgrounds
- Build industry expertise databases

### 💼 Sales & Lead Generation
Build targeted prospect lists:
- Scrape decision-maker profiles
- Collect contact information (when available)
- Build outreach lists with job titles and companies

### 🔬 Academic Research
Study career paths and professional networks:
- Analyze career progression patterns
- Study education-to-career pipelines
- Research professional skills distribution

### 📢 Influencer Marketing
Identify and research LinkedIn influencers:
- Find creators by follower count
- Analyze top voices in your niche
- Build influencer outreach lists

---

## 🔗 Support & Links

### Official Links
- **Website**: [linkdapi.com](https://linkdapi.com)
- **GitHub**: [github.com/linkdapi](https://github.com/linkdapi)
- **Documentation**: [linkdapi.com/docs](https://linkdapi.com/docs)
- **API Dashboard**: [linkdapi.com/dashboard](https://linkdapi.com/dashboard)

### Get Help
- **Email**: support@linkdapi.com
- **Issues**: Create an issue on GitHub
- **API Questions**: Check [LinkdAPI Documentation](https://linkdapi.com/docs)

### Related Tools
- **LinkdAPI Python SDK**: [github.com/linkdapi/linkdapi-sdk](https://github.com/linkdapi/linkdapi-sdk)
- **API Playground**: Test API calls at [linkdapi.com/playground](https://linkdapi.com/playground)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This LinkedIn scraper tool is for **educational and research purposes only**. Users are responsible for:

- Complying with LinkedIn's Terms of Service
- Respecting data privacy laws (GDPR, CCPA, etc.)
- Obtaining necessary permissions for data collection
- Using scraped data ethically and legally

**The LinkdAPI Team is not responsible for misuse of this tool.** Always respect people's privacy and use scraped data responsibly.

---

## 🌟 Star This Repo!

If this LinkedIn profile scraper helped you, please ⭐ star this repository on GitHub!

**Keywords**: linkedin scraper, linkedin profile scraper, linkedin data scraper, linkedin scraping tool, linkedin automation, linkedin api, profile extractor, linkedin data extraction, linkedin bulk scraper, linkedin recruiter tool, linkedin lead generation

---

**💙 Made with love by [LinkdAPI Team](https://linkdapi.com)**

*Questions? Email us at support@linkdapi.com*
