import requests
from django.conf import settings
from isodate import parse_duration
from interface.search import ISearch


class SearchVideo(ISearch):

    def search(self, video_ids):
        video_params = {
            'key':  settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet,contentDetails',
            'id': video_ids,
            'maxResults': 9,
        }
        return video_params

    def get_search_url(self, search):
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        r = requests.get(search_url, params=search)
        return r.json()['items']

    def get_video_url(self, video):
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        r = requests.get(video_url, params=video)
        return r.json()['items']

    def add_video_ids_list(self, video_ids, func):
        for result in func:
            video_ids.append(result['id']['videoId'])

    def get_videos_id(self, requests, url, params):
        video_ids = []
        r = requests.get(url, params=params)
        results = r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])

    def videos_data(self, result):
        video_data = {
            'title': result['snippet']['title'],
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={result["id"]}',
            'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail': result['snippet']['thumbnails']['high']['url']
        }
        return video_data
