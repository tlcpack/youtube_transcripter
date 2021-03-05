from youtube_transcript_api import YouTubeTranscriptApi

final = []
finalstr = ''
video = input('Give me a youtube id: ')
trans = YouTubeTranscriptApi.get_transcript(video)
for dic in trans:
  for key in dic:
    if key == 'text':
      final.append(dic[key])

finalstr = ' '.join(final)
print(finalstr)
