# 위키피디아에서 워드 클라우드 만들기
# pip install wikipedia,wordcloud,matplotlib
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wiki = wikipedia.page('KOREA')
text = wiki.content

wordcloud = WordCloud(width = 2000, height = 1500).generate(text)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.show()
