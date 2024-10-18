# Apollo Kino Movie Scraper

This Python script scrapes movie schedules for the Apollo Kino website (https://www.apollokino.ee/eng/schedule). It allows you to retrieve movie information, including titles, genres, languages, subtitles, formats, and showtimes for multiple days.

## Prerequisites

Before running this script, make sure you have Python installed

Run the script using the following command:
```bash
python movie_srapper.py
```
 By default, this will scrape movie information for the current day.

To scrape movie information for multiple days, use the `-d` or `--days` argument followed by the number of days you want to scrape. For example:
```bash
python apollo_kino_scraper.py -d 3
```
This will scrape movie information for the next 3 available days.

## Output

The script will print the movie information to the console, including:
- Movie title
- Genres
- Language
- Subtitles
- Format (e.g., 2D, 3D, IMAX)
- Showtimes (date, start time, cinema, and screen)

## Notes

- The script uses a user agent to mimic a web browser.