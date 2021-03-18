from googleapiclient.discovery import build
from datetime import datetime
api_key = 'AIzaSyCTH8yqSkChtMmnEmKdBsVm4n3BxSNrsLg'
youtube = build('youtube','V3',developerKey=api_key)
#print(type(youtube))
# following is the data extraction URL
#https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCFbNIlppjAuEX4znoulh0Cw&key=AIzaSyCTH8yqSkChtMmnEmKdBsVm4n3BxSNrsLg
# Extracting data from a spcific time range
start_time = datetime(year=2000,month=1,day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2021,month=3,day=31).strftime('%Y-%m-%dT%H:%M:%SZ')
res = youtube.search().list(part='snippet',q='පකයා',maxResults = 1,type='video',publishedAfter=start_time,publishedBefore=end_time).execute();
#print(res)
for item in res['items']:
    print(item['snippet']['title'],item['id']['videoId'])
#----------------------------------------------------------------------------------------------------------------------------------
