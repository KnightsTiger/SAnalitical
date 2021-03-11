from googleapiclient.discovery import build
api_key = 'AIzaSyCTH8yqSkChtMmnEmKdBsVm4n3BxSNrsLg'
youtube = build('youtube','V3',developerKey=api_key)
print(type(youtube))