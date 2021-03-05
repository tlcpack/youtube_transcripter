from youtube_transcript_api import YouTubeTranscriptApi
from wordcloud import WordCloud
import matplotlib.pyplot as plt

final = []
finalstr = ''
video = input('Give me a youtube id: ')
trans = YouTubeTranscriptApi.get_transcript(video)
for dic in trans:
  for key in dic:
    if key == 'text':
      final.append(dic[key])

finalstr = ' '.join(final)
with open('text2.txt', mode='w') as file:
    file.write(finalstr)
    print("ready!")

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(finalstr)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()