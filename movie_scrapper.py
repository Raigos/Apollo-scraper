import requests
from bs4 import BeautifulSoup
import argparse
from datetime import datetime, timedelta

def get_available_dates(soup):
    date_inputs = soup.find_all('input', {'class': 'day-picker__input'})
    return [input_tag.get('value') for input_tag in date_inputs if input_tag.get('value')]

def scrape_movies(url, date):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    params = {'dt': date, 'lang': 'eng'}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage for date {date}. Error: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('div', class_='schedule-card__info-container')

    movie_dict = {}

    for movie in movies:
        title = movie.find('p', class_='schedule-card__title').text.strip()
        genres = [genre.strip() for genre in movie.find('span', class_='schedule-card__genre').text.split(',') if genre.strip()]
        
        options = movie.find_all('p', class_='schedule-card__option-title')
        language = subtitles = format_type = 'N/A'

        for option in options:
            option_text = option.text.strip()
            if 'Language' in option_text:
                language = option_text.replace('Language:', '').strip()
            elif 'Subtitles' in option_text:
                subtitles = option_text.replace('Subtitles:', '').strip()
            elif any(format in option_text for format in ['2D', '3D', 'IMAX']):
                format_type = option_text

        time_container = movie.find_previous('div', class_='schedule-card__time-container')
        start_time = time_container.find('time', class_='schedule-card__time').text.strip()
        cinema = time_container.find('p', class_='schedule-card__cinema').text.strip()
        screen = time_container.find('p', class_='schedule-card__hall').text.strip()

        if title not in movie_dict:
            movie_dict[title] = {
                'genres': genres,
                'language': language,
                'subtitles': subtitles,
                'format': format_type,
                'showings': []
            }

        movie_dict[title]['showings'].append({
            'date': date, 
            'start_time': start_time,
            'cinema': cinema,
            'screen': screen
        })

    return movie_dict

def print_movies(date, movies):
    print(f"Movies for date: {date}")
    print("=" * 50)

    if movies:
        for title, info in movies.items():
            print(f"Movie: {title}")
            print(f"Genres: {', '.join(info['genres'])}")
            print(f"Language: {info['language']}")
            print(f"Subtitles: {info['subtitles']}")
            print(f"Format: {info['format']}")
            print("Showings:")
            for showing in info['showings']:
                print(f"  - {showing['date']} {showing['start_time']} at {showing['cinema']}, {showing['screen']}")
            print("-" * 50)
    else:
        print("No movies were scraped.")

def main():
    parser = argparse.ArgumentParser(description="Scrape movie schedules from Apollo Kino.")
    parser.add_argument('-d', '--days', type=int, default=1, help="Number of days to scrape (default: 1)")
    args = parser.parse_args()

    url = 'https://www.apollokino.ee/eng/schedule'

    # Get available dates
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    available_dates = get_available_dates(soup)

    # Scrape for the specified number of days
    for i in range(min(args.days, len(available_dates))):
        date = available_dates[i]
        movies = scrape_movies(url, date)
        if movies:
            print_movies(date, movies)
        else:
            print(f"No data available for {date}")
        print("\n")

if __name__ == "__main__":
    main()  