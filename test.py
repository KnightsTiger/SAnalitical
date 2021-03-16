from googleapiclient.discovery import build
api_key = 'AIzaSyCTH8yqSkChtMmnEmKdBsVm4n3BxSNrsLg'
youtube = build('youtube','V3',developerKey=api_key)
print(type(youtube))
# following is the data extraction URL
#https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCFbNIlppjAuEX4znoulh0Cw&key=AIzaSyCTH8yqSkChtMmnEmKdBsVm4n3BxSNrsLg