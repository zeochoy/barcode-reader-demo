from pyzbar.pyzbar import decode
from PIL import Image
from apiclient.discovery import build
import random

YOUTUBE_DATA_API_KEY = 'AIzaSyAKYKdL_NiIXwkIVNLmlTgGJykLY6n8MhM'
youtube = build('youtube','v3', developerKey = YOUTUBE_DATA_API_KEY)


def read_barcode(img_url):
    img = Image.open(img_url)
    result = decode(img)
    return str(result[0].data)[2:-1]


def search_youtube(product_name):
    request = youtube.search().list(q='金寶'+product_name, part='snippet', type='video', maxResults=50)
    res = request.execute()
    video_ids = [res['items'][i]['id']['videoId'] for i in range(len(res['items']))]
    return 'https://www.youtube.com/embed/' + random.choice(video_ids)
