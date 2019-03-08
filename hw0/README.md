# HW0

####從助教的程式碼中，挑出一段功能修改後並寫上修改說明，放置Github

- Reference：https://github.com/MiccWan/Political-News-Analysis/tree/master/final_demo



### My work - Wordcloud Generator

- **Motivation**

  I have no interest in those political analysis so I pick the wordcloud which is very impressive when I first read TA's project. Also, I think that this wordcloud generator might be useful in other place.

- **Result**

  ![kobe_wordcloud](/Users/Ingram/Desktop/CSIE/3-2/CSX/hw0/kobe_wordcloud.png)

- **Implementation**

  From TA's source code, I learned that there's a package for python to generate wordcloud.

  The package is called **wordcloud** and I use **pip3 install** to download it.

  We can just import it and use **matplotlib** package as well to export the result image.

  The implementation steps are as follow.

  1. Choose a *Kobe Bryant's logo* image as a mask image **kobe.png**

     ![kobe](/Users/Ingram/Desktop/CSIE/3-2/CSX/hw0/kobe.png)

  2. Randomly picked sentences about *Kobe Bryant* from wikipedia and write into **kobe.txt**

  3. Write a python code to generate the wordcloud photo **kobe_wordcloud.png**

     *(Reference: https://github.com/amueller/word_cloud)*

  ```python
  # Generate the wordcloud
  wc = WordCloud(background_color="white", max_words=2000, mask=kobe_mask, stopwords=stopwords)
  ```

- **Difficulty**

  At first, I tried some Kobe Bryant's photos but they all failed. Because that the mask image needed for the wordcloud generator must have a strong contrast in color. Otherwise, the mask you want to present will not be obvious. Therefore, I used some photo editor app to make the mask image stronger in color. And I succeeded to generate a wordcloud with a Kobe Bryant's shape. That said, since every NBA players all looks the same in that shape, it is hard to tell who's that from the wordcloud. I finally decided to choose a simple logo of Kobe Bryant and it worked.