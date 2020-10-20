from youtube_transcript_api import YouTubeTranscriptApi

final = []
finalstr = ''
trans = YouTubeTranscriptApi.get_transcript('8iei3HtdBbQ')
for dic in trans:
  for key in dic:
    if key == 'text':
      final.append(dic[key])

finalstr = ' '.join(final)
print(finalstr)
