# Extracting number of uploaded videos and extracting the titles of them
from googleapiclient.discovery import build

api_key = 'AIzaSyCTH8yqSkChtMmnEmKdBsVm4n3BxSNrsLg'
youtube = build('youtube','V3',developerKey=api_key)
tempplaylistId = 'UCHQWqXihFpz7rsSfAowMERw'

res = youtube.channels().list(id = 'UCHQWqXihFpz7rsSfAowMERw',part = 'contentDetails').execute()
res = youtube.playlistItems().list(playlistId = 'UUHQWqXihFpz7rsSfAowMERw',part = 'snippet',maxResults = 50).execute()

#print(res)
#channel_Id = 'UCHQWqXihFpz7rsSfAowMERw'
def get_channel_videos(channel_id):
    res = youtube.channels().list(id = channel_id,part = 'contentDetails').execute()
    playlist_id =  res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None
    while 1:
        res =  youtube.playlistItems().list(playlistId=playlist_id,part='snippet',maxResults=50,pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        if next_page_token is None:
            break
    return videos
videos = get_channel_videos('UCHQWqXihFpz7rsSfAowMERw')
# 'number of uploaded videos'
print(len(videos)),
# printing titles of all videos
for video in videos:
    print(video['snippet']['title']) 

