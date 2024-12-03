# Movie Schedule Data Extraction Project

A Python-based project developed to learn web data extraction and processing. Through this project, I gained hands-on experience with HTTP protocols, data parsing, and Python's ecosystem while creating a tool that collects and organizes movie schedule information.

## Technical Overview
The project works with several Python libraries and concepts:
- HTTP request handling with proper headers and error management
- HTML parsing and data extraction using BeautifulSoup4
- Command-line interface with argument parsing
- Structured data organization
- Date and time operations

## Prerequisites
- Python 3.x
- Required packages:
    - requests
    - beautifulsoup4
    - argparse
    - datetime

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
The script supports both single-day and multi-day data extraction.

Basic usage for current day:
```bash
python data_extractor.py
```

Extract data for multiple days:
```bash
python data_extractor.py -d 3
```

The `-d` argument accepts any positive integer to specify the number of days to process.

## Output Structure
The script generates structured output including:
- Movie title
- Genre categorization
- Language and subtitle information
- Format specifications (2D, 3D, IMAX)
- Schedule details:
    - Date and time
    - Location information
    - Screen assignment

Example output:
```
Movies for date: 2024-03-12
==================================================
Movie: Example Movie Title
Genres: Action, Adventure
Language: English
Subtitles: Estonian
Format: 2D
Showings:
  - 2024-03-12 19:30 at Cinema Location, Screen 1
--------------------------------------------------
```

## Error Handling
The script includes robust error handling for:
- Failed HTTP requests
- Invalid date inputs
- Parsing errors
- Network connectivity issues

## Notes
- The script uses a user agent to ensure proper request handling
- Rate limiting is implemented to avoid overloading servers
- All times are displayed in local timezone