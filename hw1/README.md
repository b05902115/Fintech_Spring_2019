# 金融科技  Hw1 第十四組

### ETF爬蟲解說


### 1. 你選擇用甚麼樣的套件來做網路爬蟲？為什麼要用這個套件

- 套件：fix-yahoo-finance
  * 首先從pypi上下載fix_yahoo_fincance
  * 在command line輸入pip3 install fix-yahoo-finance-0.0.21.tar.gz
  * 在command lind輸入 pip3 install pandas_datareader

- 原因：fix-yahoo-finance可以直接從Yahoo finance找到數據
- 參考網站：[別人從Yahoo上抓取資料的代碼]

（http://tn00343140a.pixnet.net/blog/post/166418964-python%E7%94%A8fix-yahoo-finance%E4%B8%8B%E8%BC%89yahoo%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99?fbclid=IwAR1Mb0X9iBjqaw7g3bJbuFc8w2YHHCr-x51Lc4i2EcaOT3m4XfekuBl9jEQ）


### 2. 流程圖

![流程圖](https://github.com/b05902115/Fintech_Spring_2019/blob/master/hw1/%20%E6%B5%81%E7%A8%8B%E5%9C%96.png)



### 3. 5 種當別人使用你的程式最有可能會遇到的錯誤情況，並提供解決辦法

- 沒有事先安裝好需要的套件（pandas、fix-yahoo-finance）
```diff
  * *+ 解決：在command line使用pip3 install*
```  
- csv檔沒有放在正確路徑，或路徑名稱錯誤
```diff
  * *+解決：直接修改程式內路徑名稱，或更改檔案名稱*
```  
- for 迴圈會寫不出來。
```diff
  * *+解決：可以參考code的邏輯。*
```  
- 開啟csv檔出現亂碼
  * *解決：利用 "UTF-8" 編碼開啟檔案*
  
- 過程中39個ETF資料可以不用先下載下來，通過程式調整一下excel的格式後再存成一個檔案。避免文件太多帶來困擾。

- 安裝套件時可能會出現安裝失敗的問題
  * *解決：注意python版本，如果超過3的話使用pip時要改為pip3，其餘則用pip*



### 4. 補充

- 有試過從etfdb.com連接到homepage再找每日收盤價，但幾乎所有homepage都只能找到NAV而無法找到收盤價，且每個ETF的homepage格式皆不盡相通，使用統一的爬蟲程式來爬不同的homepage難度很高，故決定直接從yahoo上爬收盤價。

- 檔案路徑名：

  * python檔："ETF_crawler.py"

  * 原始csv檔："Real Estate ETF List (48).csv"

  * 結果csv檔："ETF.csv"

    

### 5. 執行結果




