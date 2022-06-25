

from django.conf import settings


class SearchParam():
    def search(self, request):
        search_params = {
            'part': 'snippet',
            'q': request,
            'key':  settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 9,
            'type': 'video'
        }
        return search_params
