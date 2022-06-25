from django.conf import settings
from django.shortcuts import render
from serpapi import GoogleSearch

from video.video import SearchVideo
from search_param.search_param import SearchParam


def index(request):
    videos = []
    images = []
    if 'submitV' in request.POST:

        search_param = SearchParam()
        search = search_param.search(request.POST['search'])
        video_params = SearchVideo()
        video_ids = []
        video_params.get_search_url(search)

        for result in video_params.get_search_url(search):
            video_ids.append(result['id']['videoId'])
        video_params.search(video_ids)
        video_params.get_video_url(video_params.search(video_ids))
        for result in video_params.get_video_url(video_params.search(video_ids)):
            video_data = video_params.videos_data(result)
            videos.append(video_data)

    if 'submitI' in request.POST:
        ImageParams = {
            "api_key": settings.SERPAPI_API_KEY,
            "engine": "google",
            "q": request.POST['search'],
            "location": "Austin, Texas, United States",
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en",
            "num": "9",
            "tbm": "isch",
        }

        search = GoogleSearch(ImageParams)

        for image_result in search.get_dict()['images_results']:
            image_data = {
                'title': image_result['title'],
                'thumbnail': image_result['thumbnail']
            }
            images.append(image_data)

    context = {
        'videos': videos,
        'images': images
    }

    return render(request, 'search/index.html', context)
