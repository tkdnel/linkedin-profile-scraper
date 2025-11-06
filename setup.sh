#!/bin/bash
# Setup script for LinkedIn Profile Scraper

echo "======================================"
echo "LinkedIn Profile Scraper - Setup"
echo "======================================"
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "======================================"
echo "✓ Setup completed successfully!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Edit config.ini and add your LinkdAPI key"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python main.py"
echo ""
echo "Get your API key at: https://linkdapi.com"
echo ""
