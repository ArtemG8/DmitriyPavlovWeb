from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import requests

def tester():
    pass


def main(request):
    API_KEY = 'AIzaSyB94roF0VaB4CO9uFLN_xXNtPGhD7N0trg'
    CHANNEL_ID = 'UCpeIpEAkt9rn-gmEi0h8-SA'

    url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id={CHANNEL_ID}&key={API_KEY}'

    response = requests.get(url)
    data = response.json()

    # Проверка на наличие данных
    if 'items' in data and len(data['items']) > 0:
        channel_data = data['items'][0]
        statistics = channel_data['statistics']
    else:
        statistics = {}

    return render(request, 'main_page/main.html', {'statistics': statistics})

