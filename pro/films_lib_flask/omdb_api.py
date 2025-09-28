import requests
from flask import current_app

def search_media(title, media_type):
    api_key = current_app.config['OMDB_API_KEY']
    url = f"http://www.omdbapi.com/?t={title}&type={media_type}&apikey={api_key}"
    try:
        response = requests.get(url)
        # print(f"OMDB API URL: {url}")
        # print(f"OMDB API Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            # print(f"OMDB API Response: {data}")
            if data.get('Response') == 'True':
                return {
                    'title': data.get('Title', title),
                    'description': data.get('Plot', ''),
                    'poster_url': data.get('Poster', None) if data.get('Poster') != 'N/A' else None
                }
    except Exception as e:
        print(f"OMDB API Exception: {str(e)}")
    return None