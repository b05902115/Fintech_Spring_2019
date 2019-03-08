import numpy as np
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image


# Read the keyword text
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'kobe.txt')).read()
	
# Read the mask image
kobe_mask = np.array(Image.open(path.join(d, "kobe.png")))

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2000, mask=kobe_mask,
stopwords=stopwords)


wc.generate(text)
wc.to_file(path.join(d, "kobe_wordcloud.png"))
