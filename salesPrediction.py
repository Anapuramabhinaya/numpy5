!cp -r "/content/drive/My Drive/Global Superstore.csv" /content
     

from google.colab import drive
drive.mount("/content/drive")
     
Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).

cd /content
     
/content

import pandas as pd
#df = pd.read_csv('Global Superstore.csv')
     

# import csv
# with open('Global Superstore.csv' , errors = 'ignore') as kq:
#   csv_reader = csv.reader(kq)
#   with open ('kq.csv' , 'w') as tw1:
#     write1 = csv.writer(tw1)
#     for row in csv_reader :
#         write1.writerows(row)
    
     

df12 = pd.read_csv('Global Superstore.csv' , encoding = "ISO-8859-1")
     

df = pd.read_csv('Global Superstore.csv' , encoding = "ISO-8859-1")
     

df.head()
     
Row ID	Order ID	Order Date	Ship Date	Ship Mode	Customer ID	Customer Name	Segment	City	State	...	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear
Order Date																					
2012-07-31	32298	CA-2012-124891	2012-07-31	31-07-2012	Same Day	RH-19495	Rick Hansen	Consumer	New York City	New York	...	2309.650	7	0.0	762.1845	933.57	Critical	2012	7	31	31
2013-05-02	26341	IN-2013-77878	2013-05-02	07-02-2013	Second Class	JR-16210	Justin Ritter	Corporate	Wollongong	New South Wales	...	3709.395	9	0.1	-288.7650	923.63	Critical	2013	5	2	18
2013-10-17	25330	IN-2013-71249	2013-10-17	18-10-2013	First Class	CR-12730	Craig Reiter	Consumer	Brisbane	Queensland	...	5175.171	9	0.1	919.9710	915.49	Medium	2013	10	17	42
2013-01-28	13524	ES-2013-1579342	2013-01-28	30-01-2013	First Class	KM-16375	Katherine Murray	Home Office	Berlin	Berlin	...	2892.510	5	0.1	-96.5400	910.16	Medium	2013	1	28	5
2013-05-11	47221	SG-2013-4320	2013-05-11	06-11-2013	Same Day	RH-9495	Rick Hansen	Consumer	Dakar	Dakar	...	2832.960	8	0.0	311.5200	903.04	Critical	2013	5	11	19
5 rows × 28 columns


df.count()
     
Row ID            51290
Order ID          51290
Order Date        51290
Ship Date         51290
Ship Mode         51290
Customer ID       51290
Customer Name     51290
Segment           51290
City              51290
State             51290
Country           51290
Postal Code        9994
Market            51290
Region            51290
Product ID        51290
Category          51290
Sub-Category      51290
Product Name      51290
Sales             51290
Quantity          51290
Discount          51290
Profit            51290
Shipping Cost     51290
Order Priority    51290
dtype: int64

df.head()
     
Row ID	Order ID	Order Date	Ship Date	Ship Mode	Customer ID	Customer Name	Segment	City	State	...	Product ID	Category	Sub-Category	Product Name	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority
0	32298	CA-2012-124891	31-07-2012	31-07-2012	Same Day	RH-19495	Rick Hansen	Consumer	New York City	New York	...	TEC-AC-10003033	Technology	Accessories	Plantronics CS510 - Over-the-Head monaural Wir...	2309.650	7	0.0	762.1845	933.57	Critical
1	26341	IN-2013-77878	05-02-2013	07-02-2013	Second Class	JR-16210	Justin Ritter	Corporate	Wollongong	New South Wales	...	FUR-CH-10003950	Furniture	Chairs	Novimex Executive Leather Armchair, Black	3709.395	9	0.1	-288.7650	923.63	Critical
2	25330	IN-2013-71249	17-10-2013	18-10-2013	First Class	CR-12730	Craig Reiter	Consumer	Brisbane	Queensland	...	TEC-PH-10004664	Technology	Phones	Nokia Smart Phone, with Caller ID	5175.171	9	0.1	919.9710	915.49	Medium
3	13524	ES-2013-1579342	28-01-2013	30-01-2013	First Class	KM-16375	Katherine Murray	Home Office	Berlin	Berlin	...	TEC-PH-10004583	Technology	Phones	Motorola Smart Phone, Cordless	2892.510	5	0.1	-96.5400	910.16	Medium
4	47221	SG-2013-4320	05-11-2013	06-11-2013	Same Day	RH-9495	Rick Hansen	Consumer	Dakar	Dakar	...	TEC-SHA-10000501	Technology	Copiers	Sharp Wireless Fax, High-Speed	2832.960	8	0.0	311.5200	903.04	Critical
5 rows × 24 columns


import seaborn as sns
corr1 = df.corr()                             #importing seaborn model for plotting graph
sns.heatmap(corr1)
     
<matplotlib.axes._subplots.AxesSubplot at 0x7f954f7d2cf8>


sales1 = df['Sales']
     

sales1.resample('W').sum()
     
Order Date
2011-01-02      3264.23300
2011-01-09     44493.75150
2011-01-16     45704.56598
2011-01-23     21799.13634
2011-01-30     15337.02860
2011-02-06     50531.70840
2011-02-13     36810.51030
2011-02-20     27372.64350
2011-02-27     25479.34666
2011-03-06     34256.35370
2011-03-13     48432.34008
2011-03-20     45315.85720
2011-03-27     25148.89650
2011-04-03     26639.18848
2011-04-10     38946.48730
2011-04-17     34339.83120
2011-04-24     25605.47060
2011-05-01     27685.26600
2011-05-08     24894.90320
2011-05-15     39030.35564
2011-05-22     29526.25760
2011-05-29     33984.82750
2011-06-05     28445.56876
2011-06-12     56605.98002
2011-06-19     41714.26192
2011-06-26     52137.21294
2011-07-03     40269.04830
2011-07-10     44692.38120
2011-07-17     33369.66950
2011-07-24     31321.39602
                  ...     
2014-06-15     80668.23230
2014-06-22    102155.83432
2014-06-29    106010.71186
2014-07-06     71747.57154
2014-07-13     78609.76796
2014-07-20     52551.23732
2014-07-27     53963.24866
2014-08-03     60127.99216
2014-08-10     93451.14760
2014-08-17    106887.90068
2014-08-24    118144.35654
2014-08-31     95327.16012
2014-09-07     76858.02770
2014-09-14     63347.94334
2014-09-21    123273.13948
2014-09-28    110573.45770
2014-10-05     69573.57162
2014-10-12     93994.69404
2014-10-19    102970.47142
2014-10-26     93373.00084
2014-11-02     94950.85870
2014-11-09     90607.53338
2014-11-16    101755.52272
2014-11-23    162917.65730
2014-11-30    136854.97416
2014-12-07     51829.39626
2014-12-14     98005.72702
2014-12-21     99450.13210
2014-12-28    123273.28474
2015-01-04     55198.85788
Freq: W-SUN, Name: Sales, Length: 210, dtype: float64

import matplotlib.pyplot as plt
f, (ax1) = plt.subplots(1, figsize = (10, 5))                                                       #plot of weekly sales data
sales1.resample('W').sum().plot(color = 'blue' , ax = ax1)
     
<matplotlib.axes._subplots.AxesSubplot at 0x7f954f295780>


df.columns
     
Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
       'Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount',
       'Profit', 'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day',
       'WeekOfYear'],
      dtype='object')

df.head()
     
Row ID	Order ID	Order Date	Ship Date	Ship Mode	Customer ID	Customer Name	Segment	City	State	...	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear
Order Date																					
2012-07-31	32298	CA-2012-124891	2012-07-31	31-07-2012	Same Day	RH-19495	Rick Hansen	Consumer	New York City	New York	...	2309.650	7	0.0	762.1845	933.57	Critical	2012	7	31	31
2013-05-02	26341	IN-2013-77878	2013-05-02	07-02-2013	Second Class	JR-16210	Justin Ritter	Corporate	Wollongong	New South Wales	...	3709.395	9	0.1	-288.7650	923.63	Critical	2013	5	2	18
2013-10-17	25330	IN-2013-71249	2013-10-17	18-10-2013	First Class	CR-12730	Craig Reiter	Consumer	Brisbane	Queensland	...	5175.171	9	0.1	919.9710	915.49	Medium	2013	10	17	42
2013-01-28	13524	ES-2013-1579342	2013-01-28	30-01-2013	First Class	KM-16375	Katherine Murray	Home Office	Berlin	Berlin	...	2892.510	5	0.1	-96.5400	910.16	Medium	2013	1	28	5
2013-05-11	47221	SG-2013-4320	2013-05-11	06-11-2013	Same Day	RH-9495	Rick Hansen	Consumer	Dakar	Dakar	...	2832.960	8	0.0	311.5200	903.04	Critical	2013	5	11	19
5 rows × 28 columns


import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
predictors = [x for x in df.columns if x  in ['Quantity' , 'Discount' , 'Profit' , 'Shipping Cost' , 'Year' , 'Month' , 'Day' , 'WeekOfYear']]
y = np.log (df.Sales)
X = df

     

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.3, # 30% for the evaluation set
                                                    random_state = 42)
     

params = {
    'booster': 'gbtree', 
    'objective': 'reg:linear',
    'subsample': 0.8, 
    'colsample_bytree': 0.85, 
    'eta': 0.01, 
    'max_depth': 16, 
    'seed': 42} 
     

import xgboost as xgb
from xgboost.sklearn import XGBRegressor
     

X_train.columns = X_train.columns.str.replace(' ' , '')
X_test.columns =  X_test.columns.str.replace(' ' , '')
     

predictors = [x.replace(' ' , '') for x in predictors]
     

dtrain = xgb.DMatrix(X_train[predictors], y_train)
dtest = xgb.DMatrix(X_test[predictors], y_test)

watchlist = [(dtrain, 'train'), (dtest, 'test')]

xgb_model = xgb.train(params, dtrain, 1000, evals = watchlist,
                      early_stopping_rounds = 50, verbose_eval = True)
     
[0]	train-rmse:4.19473	test-rmse:4.21299
Multiple eval metrics have been passed: 'test-rmse' will be used for early stopping.

Will train until test-rmse hasn't improved in 50 rounds.
[1]	train-rmse:4.1534	test-rmse:4.17148
[2]	train-rmse:4.11309	test-rmse:4.13107
[3]	train-rmse:4.07316	test-rmse:4.09101
[4]	train-rmse:4.03307	test-rmse:4.05077
[5]	train-rmse:3.99335	test-rmse:4.01093
[6]	train-rmse:3.95404	test-rmse:3.97148
[7]	train-rmse:3.91606	test-rmse:3.93347
[8]	train-rmse:3.87753	test-rmse:3.89483
[9]	train-rmse:3.83962	test-rmse:3.85675
[10]	train-rmse:3.80209	test-rmse:3.81907
[11]	train-rmse:3.76475	test-rmse:3.78157
[12]	train-rmse:3.72777	test-rmse:3.74447
[13]	train-rmse:3.69118	test-rmse:3.70773
[14]	train-rmse:3.65494	test-rmse:3.67134
[15]	train-rmse:3.61906	test-rmse:3.63534
[16]	train-rmse:3.58438	test-rmse:3.60064
[17]	train-rmse:3.54939	test-rmse:3.56551
[18]	train-rmse:3.5148	test-rmse:3.53078
[19]	train-rmse:3.48086	test-rmse:3.49676
[20]	train-rmse:3.44676	test-rmse:3.46255
[21]	train-rmse:3.41299	test-rmse:3.42865
[22]	train-rmse:3.3801	test-rmse:3.3957
[23]	train-rmse:3.34701	test-rmse:3.36248
[24]	train-rmse:3.31443	test-rmse:3.32975
[25]	train-rmse:3.282	test-rmse:3.29719
[26]	train-rmse:3.24988	test-rmse:3.26496
[27]	train-rmse:3.21856	test-rmse:3.23356
[28]	train-rmse:3.18787	test-rmse:3.20284
[29]	train-rmse:3.15673	test-rmse:3.1716
[30]	train-rmse:3.12593	test-rmse:3.14068
[31]	train-rmse:3.09586	test-rmse:3.11055
[32]	train-rmse:3.06563	test-rmse:3.08022
[33]	train-rmse:3.03574	test-rmse:3.05022
[34]	train-rmse:3.00629	test-rmse:3.02066
[35]	train-rmse:2.9792	test-rmse:2.99353
[36]	train-rmse:2.95015	test-rmse:2.96437
[37]	train-rmse:2.92365	test-rmse:2.93784
[38]	train-rmse:2.89518	test-rmse:2.90929
[39]	train-rmse:2.86698	test-rmse:2.88098
[40]	train-rmse:2.84125	test-rmse:2.85521
[41]	train-rmse:2.81361	test-rmse:2.82749
[42]	train-rmse:2.78666	test-rmse:2.80047
[43]	train-rmse:2.75958	test-rmse:2.77331
[44]	train-rmse:2.73316	test-rmse:2.74681
[45]	train-rmse:2.7068	test-rmse:2.72036
[46]	train-rmse:2.68053	test-rmse:2.69401
[47]	train-rmse:2.65495	test-rmse:2.66839
[48]	train-rmse:2.62937	test-rmse:2.6427
[49]	train-rmse:2.60391	test-rmse:2.61716
[50]	train-rmse:2.5807	test-rmse:2.59391
[51]	train-rmse:2.55616	test-rmse:2.56934
[52]	train-rmse:2.53161	test-rmse:2.54471
[53]	train-rmse:2.50714	test-rmse:2.52017
[54]	train-rmse:2.48289	test-rmse:2.49587
[55]	train-rmse:2.45892	test-rmse:2.47182
[56]	train-rmse:2.43559	test-rmse:2.44844
[57]	train-rmse:2.41222	test-rmse:2.42499
[58]	train-rmse:2.38896	test-rmse:2.40164
[59]	train-rmse:2.36595	test-rmse:2.37856
[60]	train-rmse:2.34316	test-rmse:2.35571
[61]	train-rmse:2.32123	test-rmse:2.33379
[62]	train-rmse:2.29894	test-rmse:2.31145
[63]	train-rmse:2.27698	test-rmse:2.28943
[64]	train-rmse:2.25545	test-rmse:2.2679
[65]	train-rmse:2.23378	test-rmse:2.2462
[66]	train-rmse:2.21235	test-rmse:2.22471
[67]	train-rmse:2.19114	test-rmse:2.20345
[68]	train-rmse:2.17016	test-rmse:2.18241
[69]	train-rmse:2.1494	test-rmse:2.16162
[70]	train-rmse:2.12883	test-rmse:2.141
[71]	train-rmse:2.10904	test-rmse:2.12125
[72]	train-rmse:2.08889	test-rmse:2.10105
[73]	train-rmse:2.06909	test-rmse:2.0812
[74]	train-rmse:2.04935	test-rmse:2.06142
[75]	train-rmse:2.02996	test-rmse:2.042
[76]	train-rmse:2.01076	test-rmse:2.02275
[77]	train-rmse:1.99179	test-rmse:2.00374
[78]	train-rmse:1.97314	test-rmse:1.9851
[79]	train-rmse:1.95443	test-rmse:1.96636
[80]	train-rmse:1.93743	test-rmse:1.94938
[81]	train-rmse:1.91904	test-rmse:1.93096
[82]	train-rmse:1.90116	test-rmse:1.91305
[83]	train-rmse:1.88332	test-rmse:1.89518
[84]	train-rmse:1.86565	test-rmse:1.87747
[85]	train-rmse:1.84806	test-rmse:1.85988
[86]	train-rmse:1.83063	test-rmse:1.84241
[87]	train-rmse:1.81367	test-rmse:1.82547
[88]	train-rmse:1.79692	test-rmse:1.80874
[89]	train-rmse:1.7803	test-rmse:1.79213
[90]	train-rmse:1.76356	test-rmse:1.77537
[91]	train-rmse:1.74702	test-rmse:1.75881
[92]	train-rmse:1.73063	test-rmse:1.74241
[93]	train-rmse:1.71443	test-rmse:1.72621
[94]	train-rmse:1.69838	test-rmse:1.71016
[95]	train-rmse:1.68276	test-rmse:1.69456
[96]	train-rmse:1.66705	test-rmse:1.67884
[97]	train-rmse:1.65149	test-rmse:1.66328
[98]	train-rmse:1.63611	test-rmse:1.64791
[99]	train-rmse:1.62113	test-rmse:1.63295
[100]	train-rmse:1.60629	test-rmse:1.61818
[101]	train-rmse:1.5914	test-rmse:1.60329
[102]	train-rmse:1.57661	test-rmse:1.58852
[103]	train-rmse:1.56212	test-rmse:1.57404
[104]	train-rmse:1.54893	test-rmse:1.5609
[105]	train-rmse:1.53463	test-rmse:1.54665
[106]	train-rmse:1.52059	test-rmse:1.53262
[107]	train-rmse:1.50669	test-rmse:1.51873
[108]	train-rmse:1.49295	test-rmse:1.50502
[109]	train-rmse:1.47936	test-rmse:1.49146
[110]	train-rmse:1.46579	test-rmse:1.47792
[111]	train-rmse:1.45249	test-rmse:1.46466
[112]	train-rmse:1.4392	test-rmse:1.45142
[113]	train-rmse:1.42644	test-rmse:1.43877
[114]	train-rmse:1.41383	test-rmse:1.42627
[115]	train-rmse:1.40098	test-rmse:1.41346
[116]	train-rmse:1.38821	test-rmse:1.40075
[117]	train-rmse:1.37563	test-rmse:1.38823
[118]	train-rmse:1.36334	test-rmse:1.37601
[119]	train-rmse:1.35112	test-rmse:1.36385
[120]	train-rmse:1.3391	test-rmse:1.35194
[121]	train-rmse:1.32714	test-rmse:1.34004
[122]	train-rmse:1.31517	test-rmse:1.32815
[123]	train-rmse:1.30334	test-rmse:1.31639
[124]	train-rmse:1.29187	test-rmse:1.30501
[125]	train-rmse:1.2804	test-rmse:1.29364
[126]	train-rmse:1.26908	test-rmse:1.28236
[127]	train-rmse:1.25793	test-rmse:1.27129
[128]	train-rmse:1.24673	test-rmse:1.26017
[129]	train-rmse:1.23584	test-rmse:1.24937
[130]	train-rmse:1.22485	test-rmse:1.23848
[131]	train-rmse:1.21399	test-rmse:1.22773
[132]	train-rmse:1.20324	test-rmse:1.2171
[133]	train-rmse:1.19264	test-rmse:1.20661
[134]	train-rmse:1.18232	test-rmse:1.19642
[135]	train-rmse:1.17188	test-rmse:1.18612
[136]	train-rmse:1.16178	test-rmse:1.17615
[137]	train-rmse:1.15172	test-rmse:1.16624
[138]	train-rmse:1.14164	test-rmse:1.15626
[139]	train-rmse:1.13167	test-rmse:1.14646
[140]	train-rmse:1.12182	test-rmse:1.13672
[141]	train-rmse:1.11225	test-rmse:1.1273
[142]	train-rmse:1.10269	test-rmse:1.1179
[143]	train-rmse:1.09318	test-rmse:1.10857
[144]	train-rmse:1.08373	test-rmse:1.09929
[145]	train-rmse:1.07439	test-rmse:1.09012
[146]	train-rmse:1.06525	test-rmse:1.08117
[147]	train-rmse:1.05629	test-rmse:1.07238
[148]	train-rmse:1.04724	test-rmse:1.06352
[149]	train-rmse:1.03829	test-rmse:1.05474
[150]	train-rmse:1.02959	test-rmse:1.04622
[151]	train-rmse:1.021	test-rmse:1.03782
[152]	train-rmse:1.01246	test-rmse:1.02948
[153]	train-rmse:1.0039	test-rmse:1.02111
[154]	train-rmse:0.995467	test-rmse:1.01289
[155]	train-rmse:0.987241	test-rmse:1.00487
[156]	train-rmse:0.978953	test-rmse:0.996801
[157]	train-rmse:0.970857	test-rmse:0.988962
[158]	train-rmse:0.962903	test-rmse:0.981228
[159]	train-rmse:0.954998	test-rmse:0.973577
[160]	train-rmse:0.947046	test-rmse:0.965851
[161]	train-rmse:0.939204	test-rmse:0.958212
[162]	train-rmse:0.931446	test-rmse:0.950713
[163]	train-rmse:0.923902	test-rmse:0.943427
[164]	train-rmse:0.916322	test-rmse:0.93613
[165]	train-rmse:0.9088	test-rmse:0.928886
[166]	train-rmse:0.901471	test-rmse:0.921863
[167]	train-rmse:0.894126	test-rmse:0.914838
[168]	train-rmse:0.886843	test-rmse:0.90788
[169]	train-rmse:0.879775	test-rmse:0.901113
[170]	train-rmse:0.872845	test-rmse:0.894469
[171]	train-rmse:0.865813	test-rmse:0.887723
[172]	train-rmse:0.858863	test-rmse:0.881088
[173]	train-rmse:0.851978	test-rmse:0.874541
[174]	train-rmse:0.845437	test-rmse:0.868338
[175]	train-rmse:0.838832	test-rmse:0.862052
[176]	train-rmse:0.832158	test-rmse:0.855684
[177]	train-rmse:0.82623	test-rmse:0.850055
[178]	train-rmse:0.819714	test-rmse:0.84388
[179]	train-rmse:0.813275	test-rmse:0.8378
[180]	train-rmse:0.806992	test-rmse:0.831911
[181]	train-rmse:0.800697	test-rmse:0.825974
[182]	train-rmse:0.794586	test-rmse:0.820224
[183]	train-rmse:0.78857	test-rmse:0.814544
[184]	train-rmse:0.782602	test-rmse:0.808942
[185]	train-rmse:0.776662	test-rmse:0.803405
[186]	train-rmse:0.770696	test-rmse:0.797813
[187]	train-rmse:0.764942	test-rmse:0.792469
[188]	train-rmse:0.759125	test-rmse:0.787065
[189]	train-rmse:0.753339	test-rmse:0.781739
[190]	train-rmse:0.747664	test-rmse:0.77647
[191]	train-rmse:0.742095	test-rmse:0.771368
[192]	train-rmse:0.73653	test-rmse:0.766229
[193]	train-rmse:0.731077	test-rmse:0.761274
[194]	train-rmse:0.7257	test-rmse:0.756389
[195]	train-rmse:0.720298	test-rmse:0.751396
[196]	train-rmse:0.714977	test-rmse:0.746517
[197]	train-rmse:0.709758	test-rmse:0.741829
[198]	train-rmse:0.704518	test-rmse:0.737062
[199]	train-rmse:0.699906	test-rmse:0.732855
[200]	train-rmse:0.695348	test-rmse:0.728676
[201]	train-rmse:0.690263	test-rmse:0.72409
[202]	train-rmse:0.685794	test-rmse:0.720055
[203]	train-rmse:0.680828	test-rmse:0.715602
[204]	train-rmse:0.675945	test-rmse:0.711238
[205]	train-rmse:0.671186	test-rmse:0.707002
[206]	train-rmse:0.66636	test-rmse:0.702684
[207]	train-rmse:0.661719	test-rmse:0.698525
[208]	train-rmse:0.65704	test-rmse:0.694517
[209]	train-rmse:0.652501	test-rmse:0.690464
[210]	train-rmse:0.648025	test-rmse:0.686505
[211]	train-rmse:0.64347	test-rmse:0.682467
[212]	train-rmse:0.639063	test-rmse:0.67861
[213]	train-rmse:0.634741	test-rmse:0.674785
[214]	train-rmse:0.630481	test-rmse:0.671025
[215]	train-rmse:0.626179	test-rmse:0.667374
[216]	train-rmse:0.621883	test-rmse:0.663618
[217]	train-rmse:0.617678	test-rmse:0.66006
[218]	train-rmse:0.613482	test-rmse:0.65637
[219]	train-rmse:0.609351	test-rmse:0.652927
[220]	train-rmse:0.605279	test-rmse:0.649514
[221]	train-rmse:0.601194	test-rmse:0.645995
[222]	train-rmse:0.597155	test-rmse:0.642544
[223]	train-rmse:0.593224	test-rmse:0.639131
[224]	train-rmse:0.589304	test-rmse:0.635735
[225]	train-rmse:0.585411	test-rmse:0.632384
[226]	train-rmse:0.581584	test-rmse:0.629239
[227]	train-rmse:0.577745	test-rmse:0.625992
[228]	train-rmse:0.574005	test-rmse:0.62297
[229]	train-rmse:0.570338	test-rmse:0.619962
[230]	train-rmse:0.566637	test-rmse:0.61689
[231]	train-rmse:0.563111	test-rmse:0.613938
[232]	train-rmse:0.559513	test-rmse:0.610914
[233]	train-rmse:0.555906	test-rmse:0.608032
[234]	train-rmse:0.552391	test-rmse:0.60515
[235]	train-rmse:0.548866	test-rmse:0.602268
[236]	train-rmse:0.545442	test-rmse:0.599489
[237]	train-rmse:0.54204	test-rmse:0.596693
[238]	train-rmse:0.538649	test-rmse:0.593933
[239]	train-rmse:0.535292	test-rmse:0.591229
[240]	train-rmse:0.531957	test-rmse:0.588605
[241]	train-rmse:0.528825	test-rmse:0.586012
[242]	train-rmse:0.525697	test-rmse:0.583479
[243]	train-rmse:0.522439	test-rmse:0.581075
[244]	train-rmse:0.519413	test-rmse:0.578729
[245]	train-rmse:0.516428	test-rmse:0.57633
[246]	train-rmse:0.513335	test-rmse:0.573979
[247]	train-rmse:0.510257	test-rmse:0.571562
[248]	train-rmse:0.507334	test-rmse:0.569249
[249]	train-rmse:0.504302	test-rmse:0.56687
[250]	train-rmse:0.501283	test-rmse:0.564567
[251]	train-rmse:0.498334	test-rmse:0.562305
[252]	train-rmse:0.49545	test-rmse:0.560053
[253]	train-rmse:0.492515	test-rmse:0.558011
[254]	train-rmse:0.489708	test-rmse:0.555958
[255]	train-rmse:0.486892	test-rmse:0.553933
[256]	train-rmse:0.484149	test-rmse:0.551891
[257]	train-rmse:0.481427	test-rmse:0.549812
[258]	train-rmse:0.4787	test-rmse:0.547781
[259]	train-rmse:0.476143	test-rmse:0.545884
[260]	train-rmse:0.473451	test-rmse:0.543891
[261]	train-rmse:0.470759	test-rmse:0.541963
[262]	train-rmse:0.468173	test-rmse:0.540148
[263]	train-rmse:0.465551	test-rmse:0.538287
[264]	train-rmse:0.463012	test-rmse:0.536396
[265]	train-rmse:0.460509	test-rmse:0.534548
[266]	train-rmse:0.457977	test-rmse:0.53272
[267]	train-rmse:0.455571	test-rmse:0.531011
[268]	train-rmse:0.453216	test-rmse:0.529281
[269]	train-rmse:0.450939	test-rmse:0.527696
[270]	train-rmse:0.448829	test-rmse:0.526218
[271]	train-rmse:0.446531	test-rmse:0.524584
[272]	train-rmse:0.44427	test-rmse:0.522978
[273]	train-rmse:0.441867	test-rmse:0.521472
[274]	train-rmse:0.439589	test-rmse:0.51989
[275]	train-rmse:0.437331	test-rmse:0.51825
[276]	train-rmse:0.435193	test-rmse:0.516744
[277]	train-rmse:0.433061	test-rmse:0.515276
[278]	train-rmse:0.430867	test-rmse:0.513793
[279]	train-rmse:0.428713	test-rmse:0.512355
[280]	train-rmse:0.426625	test-rmse:0.510887
[281]	train-rmse:0.424457	test-rmse:0.509485
[282]	train-rmse:0.422381	test-rmse:0.508148
[283]	train-rmse:0.420263	test-rmse:0.506744
[284]	train-rmse:0.41846	test-rmse:0.505562
[285]	train-rmse:0.416334	test-rmse:0.504296
[286]	train-rmse:0.414338	test-rmse:0.50303
[287]	train-rmse:0.412287	test-rmse:0.501695
[288]	train-rmse:0.410329	test-rmse:0.50036
[289]	train-rmse:0.408333	test-rmse:0.499087
[290]	train-rmse:0.406366	test-rmse:0.497901
[291]	train-rmse:0.404434	test-rmse:0.496718
[292]	train-rmse:0.402518	test-rmse:0.495554
[293]	train-rmse:0.400705	test-rmse:0.494419
[294]	train-rmse:0.398773	test-rmse:0.493265
[295]	train-rmse:0.396897	test-rmse:0.492173
[296]	train-rmse:0.395029	test-rmse:0.491025
[297]	train-rmse:0.393073	test-rmse:0.489986
[298]	train-rmse:0.391254	test-rmse:0.48891
[299]	train-rmse:0.389505	test-rmse:0.48783
[300]	train-rmse:0.387761	test-rmse:0.486818
[301]	train-rmse:0.386072	test-rmse:0.485798
[302]	train-rmse:0.384379	test-rmse:0.48473
[303]	train-rmse:0.382694	test-rmse:0.483676
[304]	train-rmse:0.381051	test-rmse:0.482667
[305]	train-rmse:0.379472	test-rmse:0.481721
[306]	train-rmse:0.377764	test-rmse:0.480743
[307]	train-rmse:0.376129	test-rmse:0.479852
[308]	train-rmse:0.374534	test-rmse:0.47888
[309]	train-rmse:0.373029	test-rmse:0.478031
[310]	train-rmse:0.371508	test-rmse:0.477178
[311]	train-rmse:0.370074	test-rmse:0.476303
[312]	train-rmse:0.368607	test-rmse:0.475457
[313]	train-rmse:0.367087	test-rmse:0.47462
[314]	train-rmse:0.365565	test-rmse:0.473765
[315]	train-rmse:0.364016	test-rmse:0.472898
[316]	train-rmse:0.362503	test-rmse:0.472139
[317]	train-rmse:0.360993	test-rmse:0.471332
[318]	train-rmse:0.359566	test-rmse:0.470589
[319]	train-rmse:0.358142	test-rmse:0.469846
[320]	train-rmse:0.35668	test-rmse:0.469068
[321]	train-rmse:0.355296	test-rmse:0.468308
[322]	train-rmse:0.353886	test-rmse:0.467559
[323]	train-rmse:0.352556	test-rmse:0.466849
[324]	train-rmse:0.351166	test-rmse:0.466091
[325]	train-rmse:0.349799	test-rmse:0.465429
[326]	train-rmse:0.3484	test-rmse:0.464705
[327]	train-rmse:0.347017	test-rmse:0.464093
[328]	train-rmse:0.345692	test-rmse:0.463423
[329]	train-rmse:0.344552	test-rmse:0.462838
[330]	train-rmse:0.343256	test-rmse:0.462142
[331]	train-rmse:0.341998	test-rmse:0.461492
[332]	train-rmse:0.340662	test-rmse:0.460864
[333]	train-rmse:0.339358	test-rmse:0.460258
[334]	train-rmse:0.338141	test-rmse:0.459618
[335]	train-rmse:0.336831	test-rmse:0.458985
[336]	train-rmse:0.335667	test-rmse:0.458412
[337]	train-rmse:0.334443	test-rmse:0.457832
[338]	train-rmse:0.333218	test-rmse:0.45732
[339]	train-rmse:0.331993	test-rmse:0.456805
[340]	train-rmse:0.330945	test-rmse:0.45631
[341]	train-rmse:0.329753	test-rmse:0.455744
[342]	train-rmse:0.328564	test-rmse:0.455255
[343]	train-rmse:0.327416	test-rmse:0.454778
[344]	train-rmse:0.326207	test-rmse:0.454263
[345]	train-rmse:0.325032	test-rmse:0.453818
[346]	train-rmse:0.323935	test-rmse:0.453326
[347]	train-rmse:0.32283	test-rmse:0.452865
[348]	train-rmse:0.321829	test-rmse:0.452403
[349]	train-rmse:0.320705	test-rmse:0.451926
[350]	train-rmse:0.319754	test-rmse:0.451461
[351]	train-rmse:0.318632	test-rmse:0.450988
[352]	train-rmse:0.317557	test-rmse:0.450569
[353]	train-rmse:0.316466	test-rmse:0.450175
[354]	train-rmse:0.3154	test-rmse:0.449781
[355]	train-rmse:0.314423	test-rmse:0.449309
[356]	train-rmse:0.313322	test-rmse:0.44887
[357]	train-rmse:0.312296	test-rmse:0.4485
[358]	train-rmse:0.311274	test-rmse:0.448102
[359]	train-rmse:0.310375	test-rmse:0.447715
[360]	train-rmse:0.309417	test-rmse:0.447323
[361]	train-rmse:0.308419	test-rmse:0.446911
[362]	train-rmse:0.307488	test-rmse:0.446522
[363]	train-rmse:0.306537	test-rmse:0.446196
[364]	train-rmse:0.305617	test-rmse:0.445808
[365]	train-rmse:0.304656	test-rmse:0.445422
[366]	train-rmse:0.303898	test-rmse:0.4451
[367]	train-rmse:0.302898	test-rmse:0.444749
[368]	train-rmse:0.30199	test-rmse:0.444384
[369]	train-rmse:0.301036	test-rmse:0.444075
[370]	train-rmse:0.300166	test-rmse:0.443742
[371]	train-rmse:0.299328	test-rmse:0.443425
[372]	train-rmse:0.298469	test-rmse:0.443095
[373]	train-rmse:0.297654	test-rmse:0.442766
[374]	train-rmse:0.296799	test-rmse:0.44249
[375]	train-rmse:0.295887	test-rmse:0.442198
[376]	train-rmse:0.294933	test-rmse:0.441872
[377]	train-rmse:0.294187	test-rmse:0.441599
[378]	train-rmse:0.2933	test-rmse:0.441282
[379]	train-rmse:0.292461	test-rmse:0.44097
[380]	train-rmse:0.291584	test-rmse:0.440678
[381]	train-rmse:0.29085	test-rmse:0.440411
[382]	train-rmse:0.290135	test-rmse:0.440155
[383]	train-rmse:0.289326	test-rmse:0.43993
[384]	train-rmse:0.288546	test-rmse:0.439626
[385]	train-rmse:0.287715	test-rmse:0.439369
[386]	train-rmse:0.287055	test-rmse:0.439118
[387]	train-rmse:0.286393	test-rmse:0.438896
[388]	train-rmse:0.285657	test-rmse:0.438628
[389]	train-rmse:0.284833	test-rmse:0.438373
[390]	train-rmse:0.284153	test-rmse:0.438131
[391]	train-rmse:0.283423	test-rmse:0.437897
[392]	train-rmse:0.282623	test-rmse:0.437674
[393]	train-rmse:0.281943	test-rmse:0.43747
[394]	train-rmse:0.281251	test-rmse:0.437197
[395]	train-rmse:0.280586	test-rmse:0.43698
[396]	train-rmse:0.279875	test-rmse:0.436758
[397]	train-rmse:0.279181	test-rmse:0.436534
[398]	train-rmse:0.278465	test-rmse:0.436321
[399]	train-rmse:0.277707	test-rmse:0.436116
[400]	train-rmse:0.277016	test-rmse:0.435897
[401]	train-rmse:0.276333	test-rmse:0.435709
[402]	train-rmse:0.275645	test-rmse:0.435527
[403]	train-rmse:0.274946	test-rmse:0.435353
[404]	train-rmse:0.274329	test-rmse:0.435125
[405]	train-rmse:0.273711	test-rmse:0.434922
[406]	train-rmse:0.273032	test-rmse:0.434749
[407]	train-rmse:0.272441	test-rmse:0.434565
[408]	train-rmse:0.271767	test-rmse:0.434366
[409]	train-rmse:0.270988	test-rmse:0.434204
[410]	train-rmse:0.270324	test-rmse:0.434025
[411]	train-rmse:0.269664	test-rmse:0.433899
[412]	train-rmse:0.268934	test-rmse:0.433726
[413]	train-rmse:0.268354	test-rmse:0.433543
[414]	train-rmse:0.267817	test-rmse:0.433351
[415]	train-rmse:0.267246	test-rmse:0.433202
[416]	train-rmse:0.266699	test-rmse:0.433025
[417]	train-rmse:0.266115	test-rmse:0.432839
[418]	train-rmse:0.265496	test-rmse:0.432688
[419]	train-rmse:0.264949	test-rmse:0.432514
[420]	train-rmse:0.264346	test-rmse:0.432362
[421]	train-rmse:0.263791	test-rmse:0.432188
[422]	train-rmse:0.26325	test-rmse:0.43206
[423]	train-rmse:0.262658	test-rmse:0.431917
[424]	train-rmse:0.262079	test-rmse:0.431748
[425]	train-rmse:0.261498	test-rmse:0.431628
[426]	train-rmse:0.260899	test-rmse:0.431508
[427]	train-rmse:0.260483	test-rmse:0.431366
[428]	train-rmse:0.259932	test-rmse:0.431243
[429]	train-rmse:0.259405	test-rmse:0.431094
[430]	train-rmse:0.258857	test-rmse:0.430971
[431]	train-rmse:0.258391	test-rmse:0.430843
[432]	train-rmse:0.257869	test-rmse:0.430731
[433]	train-rmse:0.257297	test-rmse:0.43061
[434]	train-rmse:0.256693	test-rmse:0.430504
[435]	train-rmse:0.256254	test-rmse:0.430393
[436]	train-rmse:0.255678	test-rmse:0.430271
[437]	train-rmse:0.255213	test-rmse:0.430174
[438]	train-rmse:0.254561	test-rmse:0.430041
[439]	train-rmse:0.254069	test-rmse:0.429932
[440]	train-rmse:0.253564	test-rmse:0.429802
[441]	train-rmse:0.253107	test-rmse:0.429691
[442]	train-rmse:0.252686	test-rmse:0.429601
[443]	train-rmse:0.25215	test-rmse:0.429503
[444]	train-rmse:0.251655	test-rmse:0.42939
[445]	train-rmse:0.251157	test-rmse:0.429312
[446]	train-rmse:0.250702	test-rmse:0.42921
[447]	train-rmse:0.250338	test-rmse:0.429121
[448]	train-rmse:0.249857	test-rmse:0.429027
[449]	train-rmse:0.249421	test-rmse:0.428947
[450]	train-rmse:0.248999	test-rmse:0.428855
[451]	train-rmse:0.248575	test-rmse:0.42878
[452]	train-rmse:0.248146	test-rmse:0.428688
[453]	train-rmse:0.247713	test-rmse:0.428576
[454]	train-rmse:0.247178	test-rmse:0.428521
[455]	train-rmse:0.246733	test-rmse:0.42842
[456]	train-rmse:0.246364	test-rmse:0.428348
[457]	train-rmse:0.24594	test-rmse:0.428261
[458]	train-rmse:0.245581	test-rmse:0.428166
[459]	train-rmse:0.245166	test-rmse:0.428083
[460]	train-rmse:0.244696	test-rmse:0.427996
[461]	train-rmse:0.244339	test-rmse:0.427921
[462]	train-rmse:0.243889	test-rmse:0.427851
[463]	train-rmse:0.243528	test-rmse:0.427776
[464]	train-rmse:0.243134	test-rmse:0.427705
[465]	train-rmse:0.242788	test-rmse:0.427642
[466]	train-rmse:0.242501	test-rmse:0.427574
[467]	train-rmse:0.242119	test-rmse:0.427513
[468]	train-rmse:0.241665	test-rmse:0.427445
[469]	train-rmse:0.241202	test-rmse:0.427364
[470]	train-rmse:0.240875	test-rmse:0.427308
[471]	train-rmse:0.240479	test-rmse:0.42723
[472]	train-rmse:0.240111	test-rmse:0.427151
[473]	train-rmse:0.239735	test-rmse:0.427112
[474]	train-rmse:0.239356	test-rmse:0.427031
[475]	train-rmse:0.23898	test-rmse:0.426966
[476]	train-rmse:0.238585	test-rmse:0.426908
[477]	train-rmse:0.238229	test-rmse:0.426858
[478]	train-rmse:0.237815	test-rmse:0.426786
[479]	train-rmse:0.237461	test-rmse:0.426726
[480]	train-rmse:0.237154	test-rmse:0.426682
[481]	train-rmse:0.236786	test-rmse:0.426638
[482]	train-rmse:0.236442	test-rmse:0.426575
[483]	train-rmse:0.236015	test-rmse:0.426542
[484]	train-rmse:0.235713	test-rmse:0.426499
[485]	train-rmse:0.235288	test-rmse:0.426442
[486]	train-rmse:0.234907	test-rmse:0.426387
[487]	train-rmse:0.234534	test-rmse:0.426349
[488]	train-rmse:0.234216	test-rmse:0.426319
[489]	train-rmse:0.233864	test-rmse:0.426293
[490]	train-rmse:0.233529	test-rmse:0.426236
[491]	train-rmse:0.233232	test-rmse:0.426192
[492]	train-rmse:0.232909	test-rmse:0.426157
[493]	train-rmse:0.232598	test-rmse:0.426117
[494]	train-rmse:0.232247	test-rmse:0.426079
[495]	train-rmse:0.231976	test-rmse:0.426025
[496]	train-rmse:0.231604	test-rmse:0.425976
[497]	train-rmse:0.231284	test-rmse:0.425943
[498]	train-rmse:0.230965	test-rmse:0.42591
[499]	train-rmse:0.230615	test-rmse:0.425868
[500]	train-rmse:0.230383	test-rmse:0.425825
[501]	train-rmse:0.230078	test-rmse:0.425783
[502]	train-rmse:0.229703	test-rmse:0.42574
[503]	train-rmse:0.229442	test-rmse:0.425699
[504]	train-rmse:0.22902	test-rmse:0.425646
[505]	train-rmse:0.228779	test-rmse:0.425614
[506]	train-rmse:0.22838	test-rmse:0.425573
[507]	train-rmse:0.228103	test-rmse:0.425542
[508]	train-rmse:0.227754	test-rmse:0.42552
[509]	train-rmse:0.227407	test-rmse:0.425494
[510]	train-rmse:0.227115	test-rmse:0.42546
[511]	train-rmse:0.226852	test-rmse:0.425423
[512]	train-rmse:0.226536	test-rmse:0.425375
[513]	train-rmse:0.226302	test-rmse:0.42533
[514]	train-rmse:0.226008	test-rmse:0.425287
[515]	train-rmse:0.225681	test-rmse:0.425251
[516]	train-rmse:0.225417	test-rmse:0.425221
[517]	train-rmse:0.225134	test-rmse:0.425207
[518]	train-rmse:0.224801	test-rmse:0.42518
[519]	train-rmse:0.224544	test-rmse:0.425133
[520]	train-rmse:0.224332	test-rmse:0.4251
[521]	train-rmse:0.224018	test-rmse:0.425075
[522]	train-rmse:0.223847	test-rmse:0.425043
[523]	train-rmse:0.223556	test-rmse:0.425006
[524]	train-rmse:0.223256	test-rmse:0.424985
[525]	train-rmse:0.223019	test-rmse:0.424957
[526]	train-rmse:0.22275	test-rmse:0.424924
[527]	train-rmse:0.222513	test-rmse:0.424891
[528]	train-rmse:0.222248	test-rmse:0.424868
[529]	train-rmse:0.221952	test-rmse:0.42486
[530]	train-rmse:0.221614	test-rmse:0.42485
[531]	train-rmse:0.221316	test-rmse:0.424813
[532]	train-rmse:0.221067	test-rmse:0.424792
[533]	train-rmse:0.220793	test-rmse:0.424772
[534]	train-rmse:0.220553	test-rmse:0.424762
[535]	train-rmse:0.220276	test-rmse:0.424739
[536]	train-rmse:0.219962	test-rmse:0.424723
[537]	train-rmse:0.219692	test-rmse:0.424705
[538]	train-rmse:0.219497	test-rmse:0.424673
[539]	train-rmse:0.219235	test-rmse:0.424646
[540]	train-rmse:0.218999	test-rmse:0.424613
[541]	train-rmse:0.218696	test-rmse:0.424577
[542]	train-rmse:0.218444	test-rmse:0.424568
[543]	train-rmse:0.218261	test-rmse:0.424544
[544]	train-rmse:0.218057	test-rmse:0.424523
[545]	train-rmse:0.217889	test-rmse:0.424496
[546]	train-rmse:0.217659	test-rmse:0.424481
[547]	train-rmse:0.217404	test-rmse:0.424443
[548]	train-rmse:0.217194	test-rmse:0.424422
[549]	train-rmse:0.216927	test-rmse:0.424395
[550]	train-rmse:0.216723	test-rmse:0.424366
[551]	train-rmse:0.216465	test-rmse:0.424352
[552]	train-rmse:0.216266	test-rmse:0.424331
[553]	train-rmse:0.21595	test-rmse:0.424323
[554]	train-rmse:0.215707	test-rmse:0.424311
[555]	train-rmse:0.215557	test-rmse:0.424295
[556]	train-rmse:0.215372	test-rmse:0.424294
[557]	train-rmse:0.215142	test-rmse:0.424269
[558]	train-rmse:0.214882	test-rmse:0.424257
[559]	train-rmse:0.214617	test-rmse:0.424241
[560]	train-rmse:0.214401	test-rmse:0.424228
[561]	train-rmse:0.214181	test-rmse:0.424208
[562]	train-rmse:0.213965	test-rmse:0.424186
[563]	train-rmse:0.213789	test-rmse:0.424168
[564]	train-rmse:0.213599	test-rmse:0.424152
[565]	train-rmse:0.213468	test-rmse:0.424131
[566]	train-rmse:0.213223	test-rmse:0.42411
[567]	train-rmse:0.213057	test-rmse:0.424096
[568]	train-rmse:0.212912	test-rmse:0.424081
[569]	train-rmse:0.212669	test-rmse:0.424063
[570]	train-rmse:0.212462	test-rmse:0.42406
[571]	train-rmse:0.212221	test-rmse:0.424048
[572]	train-rmse:0.212076	test-rmse:0.42403
[573]	train-rmse:0.211888	test-rmse:0.424014
[574]	train-rmse:0.211642	test-rmse:0.423996
[575]	train-rmse:0.211435	test-rmse:0.423993
[576]	train-rmse:0.211255	test-rmse:0.423992
[577]	train-rmse:0.21114	test-rmse:0.42398
[578]	train-rmse:0.210851	test-rmse:0.423949
[579]	train-rmse:0.210654	test-rmse:0.423943
[580]	train-rmse:0.210456	test-rmse:0.423922
[581]	train-rmse:0.210294	test-rmse:0.423913
[582]	train-rmse:0.210087	test-rmse:0.423894
[583]	train-rmse:0.209858	test-rmse:0.423887
[584]	train-rmse:0.209737	test-rmse:0.423882
[585]	train-rmse:0.209558	test-rmse:0.423848
[586]	train-rmse:0.209378	test-rmse:0.423847
[587]	train-rmse:0.209169	test-rmse:0.423826
[588]	train-rmse:0.208964	test-rmse:0.42381
[589]	train-rmse:0.208782	test-rmse:0.423799
[590]	train-rmse:0.208604	test-rmse:0.423794
[591]	train-rmse:0.208453	test-rmse:0.423789
[592]	train-rmse:0.208212	test-rmse:0.423773
[593]	train-rmse:0.207988	test-rmse:0.423768
[594]	train-rmse:0.207808	test-rmse:0.423761
[595]	train-rmse:0.207618	test-rmse:0.423746
[596]	train-rmse:0.207448	test-rmse:0.423736
[597]	train-rmse:0.207255	test-rmse:0.423731
[598]	train-rmse:0.207142	test-rmse:0.423715
[599]	train-rmse:0.207041	test-rmse:0.423701
[600]	train-rmse:0.20694	test-rmse:0.423692
[601]	train-rmse:0.206729	test-rmse:0.423688
[602]	train-rmse:0.206557	test-rmse:0.423676
[603]	train-rmse:0.206463	test-rmse:0.42367
[604]	train-rmse:0.206255	test-rmse:0.423654
[605]	train-rmse:0.206085	test-rmse:0.423654
[606]	train-rmse:0.205945	test-rmse:0.423645
[607]	train-rmse:0.205772	test-rmse:0.423636
[608]	train-rmse:0.205627	test-rmse:0.423629
[609]	train-rmse:0.20549	test-rmse:0.423623
[610]	train-rmse:0.205219	test-rmse:0.423622
[611]	train-rmse:0.205026	test-rmse:0.423633
[612]	train-rmse:0.204879	test-rmse:0.423614
[613]	train-rmse:0.204611	test-rmse:0.423611
[614]	train-rmse:0.204436	test-rmse:0.423607
[615]	train-rmse:0.20429	test-rmse:0.423592
[616]	train-rmse:0.204145	test-rmse:0.423583
[617]	train-rmse:0.204019	test-rmse:0.423576
[618]	train-rmse:0.203858	test-rmse:0.423569
[619]	train-rmse:0.20376	test-rmse:0.423576
[620]	train-rmse:0.203535	test-rmse:0.42357
[621]	train-rmse:0.203419	test-rmse:0.423565
[622]	train-rmse:0.203282	test-rmse:0.42356
[623]	train-rmse:0.203125	test-rmse:0.423545
[624]	train-rmse:0.203043	test-rmse:0.423541
[625]	train-rmse:0.20287	test-rmse:0.423527
[626]	train-rmse:0.202704	test-rmse:0.423527
[627]	train-rmse:0.202589	test-rmse:0.423524
[628]	train-rmse:0.202514	test-rmse:0.423521
[629]	train-rmse:0.202385	test-rmse:0.423506
[630]	train-rmse:0.202256	test-rmse:0.423502
[631]	train-rmse:0.202133	test-rmse:0.423503
[632]	train-rmse:0.202015	test-rmse:0.423489
[633]	train-rmse:0.201879	test-rmse:0.42348
[634]	train-rmse:0.201719	test-rmse:0.423484
[635]	train-rmse:0.201628	test-rmse:0.423481
[636]	train-rmse:0.201499	test-rmse:0.423482
[637]	train-rmse:0.201329	test-rmse:0.423474
[638]	train-rmse:0.20125	test-rmse:0.423466
[639]	train-rmse:0.201034	test-rmse:0.423447
[640]	train-rmse:0.200796	test-rmse:0.423447
[641]	train-rmse:0.200587	test-rmse:0.423423
[642]	train-rmse:0.200419	test-rmse:0.423418
[643]	train-rmse:0.200309	test-rmse:0.423411
[644]	train-rmse:0.200159	test-rmse:0.423395
[645]	train-rmse:0.200039	test-rmse:0.423393
[646]	train-rmse:0.199948	test-rmse:0.423389
[647]	train-rmse:0.199796	test-rmse:0.423376
[648]	train-rmse:0.199589	test-rmse:0.423371
[649]	train-rmse:0.199425	test-rmse:0.423364
[650]	train-rmse:0.199288	test-rmse:0.423349
[651]	train-rmse:0.199118	test-rmse:0.423357
[652]	train-rmse:0.198886	test-rmse:0.423364
[653]	train-rmse:0.1987	test-rmse:0.423365
[654]	train-rmse:0.198472	test-rmse:0.423362
[655]	train-rmse:0.198333	test-rmse:0.42335
[656]	train-rmse:0.198167	test-rmse:0.423351
[657]	train-rmse:0.198024	test-rmse:0.423348
[658]	train-rmse:0.197955	test-rmse:0.423346
[659]	train-rmse:0.197797	test-rmse:0.423341
[660]	train-rmse:0.197667	test-rmse:0.423338
[661]	train-rmse:0.197518	test-rmse:0.42333
[662]	train-rmse:0.197451	test-rmse:0.423322
[663]	train-rmse:0.197304	test-rmse:0.42331
[664]	train-rmse:0.197024	test-rmse:0.42332
[665]	train-rmse:0.196918	test-rmse:0.423317
[666]	train-rmse:0.196624	test-rmse:0.42332
[667]	train-rmse:0.196489	test-rmse:0.423319
[668]	train-rmse:0.196373	test-rmse:0.423307
[669]	train-rmse:0.19624	test-rmse:0.423305
[670]	train-rmse:0.196077	test-rmse:0.423298
[671]	train-rmse:0.195931	test-rmse:0.423284
[672]	train-rmse:0.195772	test-rmse:0.423276
[673]	train-rmse:0.19558	test-rmse:0.42327
[674]	train-rmse:0.195491	test-rmse:0.423267
[675]	train-rmse:0.195377	test-rmse:0.423275
[676]	train-rmse:0.195267	test-rmse:0.423269
[677]	train-rmse:0.195125	test-rmse:0.423276
[678]	train-rmse:0.194963	test-rmse:0.423277
[679]	train-rmse:0.194847	test-rmse:0.423263
[680]	train-rmse:0.194643	test-rmse:0.423257
[681]	train-rmse:0.194353	test-rmse:0.423264
[682]	train-rmse:0.194245	test-rmse:0.423256
[683]	train-rmse:0.19413	test-rmse:0.423251
[684]	train-rmse:0.194007	test-rmse:0.423249
[685]	train-rmse:0.193878	test-rmse:0.423256
[686]	train-rmse:0.193737	test-rmse:0.42325
[687]	train-rmse:0.193527	test-rmse:0.423246
[688]	train-rmse:0.193325	test-rmse:0.423243
[689]	train-rmse:0.193202	test-rmse:0.423238
[690]	train-rmse:0.192968	test-rmse:0.42324
[691]	train-rmse:0.192806	test-rmse:0.423232
[692]	train-rmse:0.192655	test-rmse:0.42324
[693]	train-rmse:0.192555	test-rmse:0.423234
[694]	train-rmse:0.192428	test-rmse:0.423232
[695]	train-rmse:0.192278	test-rmse:0.423238
[696]	train-rmse:0.192174	test-rmse:0.423232
[697]	train-rmse:0.19201	test-rmse:0.423231
[698]	train-rmse:0.191952	test-rmse:0.423229
[699]	train-rmse:0.191725	test-rmse:0.423226
[700]	train-rmse:0.191612	test-rmse:0.423227
[701]	train-rmse:0.191463	test-rmse:0.423224
[702]	train-rmse:0.191321	test-rmse:0.423229
[703]	train-rmse:0.191104	test-rmse:0.423226
[704]	train-rmse:0.190972	test-rmse:0.423221
[705]	train-rmse:0.190815	test-rmse:0.423222
[706]	train-rmse:0.190671	test-rmse:0.42322
[707]	train-rmse:0.190532	test-rmse:0.423224
[708]	train-rmse:0.190427	test-rmse:0.423228
[709]	train-rmse:0.190317	test-rmse:0.423223
[710]	train-rmse:0.190284	test-rmse:0.42322
[711]	train-rmse:0.1902	test-rmse:0.423221
[712]	train-rmse:0.189998	test-rmse:0.423226
[713]	train-rmse:0.189869	test-rmse:0.423229
[714]	train-rmse:0.189627	test-rmse:0.423245
[715]	train-rmse:0.189475	test-rmse:0.423239
[716]	train-rmse:0.189392	test-rmse:0.423239
[717]	train-rmse:0.189268	test-rmse:0.42324
[718]	train-rmse:0.189152	test-rmse:0.423241
[719]	train-rmse:0.188989	test-rmse:0.42323
[720]	train-rmse:0.188896	test-rmse:0.423226
[721]	train-rmse:0.188633	test-rmse:0.423221
[722]	train-rmse:0.188518	test-rmse:0.42323
[723]	train-rmse:0.188374	test-rmse:0.423225
[724]	train-rmse:0.188104	test-rmse:0.423234
[725]	train-rmse:0.187984	test-rmse:0.423238
[726]	train-rmse:0.187883	test-rmse:0.423236
[727]	train-rmse:0.187742	test-rmse:0.42324
[728]	train-rmse:0.187625	test-rmse:0.423243
[729]	train-rmse:0.187411	test-rmse:0.423249
[730]	train-rmse:0.187341	test-rmse:0.423247
[731]	train-rmse:0.187289	test-rmse:0.423237
[732]	train-rmse:0.187218	test-rmse:0.423233
[733]	train-rmse:0.187025	test-rmse:0.423223
[734]	train-rmse:0.18677	test-rmse:0.423203
[735]	train-rmse:0.186691	test-rmse:0.423197
[736]	train-rmse:0.186609	test-rmse:0.423198
[737]	train-rmse:0.186548	test-rmse:0.423195
[738]	train-rmse:0.186372	test-rmse:0.423194
[739]	train-rmse:0.186251	test-rmse:0.423198
[740]	train-rmse:0.186103	test-rmse:0.423198
[741]	train-rmse:0.186053	test-rmse:0.423194
[742]	train-rmse:0.185743	test-rmse:0.42318
[743]	train-rmse:0.185623	test-rmse:0.423182
[744]	train-rmse:0.185471	test-rmse:0.423173
[745]	train-rmse:0.185393	test-rmse:0.423173
[746]	train-rmse:0.185277	test-rmse:0.423173
[747]	train-rmse:0.185139	test-rmse:0.423173
[748]	train-rmse:0.184979	test-rmse:0.423167
[749]	train-rmse:0.184915	test-rmse:0.42317
[750]	train-rmse:0.184837	test-rmse:0.423171
[751]	train-rmse:0.184671	test-rmse:0.423168
[752]	train-rmse:0.184586	test-rmse:0.423164
[753]	train-rmse:0.18448	test-rmse:0.423166
[754]	train-rmse:0.184317	test-rmse:0.423173
[755]	train-rmse:0.184203	test-rmse:0.423178
[756]	train-rmse:0.184076	test-rmse:0.423181
[757]	train-rmse:0.183958	test-rmse:0.423171
[758]	train-rmse:0.18382	test-rmse:0.423174
[759]	train-rmse:0.183771	test-rmse:0.423171
[760]	train-rmse:0.183632	test-rmse:0.423172
[761]	train-rmse:0.183512	test-rmse:0.423175
[762]	train-rmse:0.183452	test-rmse:0.423173
[763]	train-rmse:0.183315	test-rmse:0.423172
[764]	train-rmse:0.183186	test-rmse:0.423185
[765]	train-rmse:0.182899	test-rmse:0.4232
[766]	train-rmse:0.182728	test-rmse:0.423199
[767]	train-rmse:0.182627	test-rmse:0.423197
[768]	train-rmse:0.182407	test-rmse:0.423199
[769]	train-rmse:0.182277	test-rmse:0.423194
[770]	train-rmse:0.182169	test-rmse:0.423191
[771]	train-rmse:0.182057	test-rmse:0.423189
[772]	train-rmse:0.181732	test-rmse:0.423188
[773]	train-rmse:0.181662	test-rmse:0.423181
[774]	train-rmse:0.181589	test-rmse:0.423171
[775]	train-rmse:0.181524	test-rmse:0.423169
[776]	train-rmse:0.181355	test-rmse:0.423165
[777]	train-rmse:0.181272	test-rmse:0.423172
[778]	train-rmse:0.181163	test-rmse:0.423178
[779]	train-rmse:0.18102	test-rmse:0.423181
[780]	train-rmse:0.180968	test-rmse:0.42318
[781]	train-rmse:0.180867	test-rmse:0.423181
[782]	train-rmse:0.180681	test-rmse:0.423174
[783]	train-rmse:0.180481	test-rmse:0.423183
[784]	train-rmse:0.180376	test-rmse:0.423185
[785]	train-rmse:0.180306	test-rmse:0.423184
[786]	train-rmse:0.180222	test-rmse:0.423185
[787]	train-rmse:0.180162	test-rmse:0.423191
[788]	train-rmse:0.180052	test-rmse:0.423189
[789]	train-rmse:0.17986	test-rmse:0.4232
[790]	train-rmse:0.179769	test-rmse:0.423198
[791]	train-rmse:0.17968	test-rmse:0.423199
[792]	train-rmse:0.179495	test-rmse:0.423202
[793]	train-rmse:0.179246	test-rmse:0.423199
[794]	train-rmse:0.179176	test-rmse:0.423196
[795]	train-rmse:0.179083	test-rmse:0.423196
[796]	train-rmse:0.178917	test-rmse:0.423196
[797]	train-rmse:0.178669	test-rmse:0.423193
[798]	train-rmse:0.178516	test-rmse:0.423202
[799]	train-rmse:0.17843	test-rmse:0.4232
[800]	train-rmse:0.178308	test-rmse:0.423201
[801]	train-rmse:0.178081	test-rmse:0.423214
[802]	train-rmse:0.177881	test-rmse:0.423212
Stopping. Best iteration:
[752]	train-rmse:0.184586	test-rmse:0.423164


yhat = xgb_model.predict(xgb.DMatrix(X_test[predictors]))
#error = rmspe(X_test.Sales.values, np.exp(yhat))

#print('First validation yelds RMSPE: {:.6f}'.format(error))
     

from xgboost import plot_tree
import matplotlib.pyplot as plt
plot_tree(xgb_model)
fig = plt.gcf()
fig.set_size_inches(100, 90)
     


X_test['predicted sales'] = xgb_model.predict(xgb.DMatrix(X_test[predictors]))
X_test['actual sales'] = np.log(X_test.Sales.values)
X_test.head(20)
     
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  """Entry point for launching an IPython kernel.
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  
Row ID	Order ID	Order Date	Ship Date	Ship Mode	Customer ID	Customer Name	Segment	City	State	...	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear	predicted sales	actual sales
Order Date																					
2012-12-11	6598	US-2012-158330	2012-12-11	18-11-2012	Standard Class	SC-20725	Steven Cartwright	Consumer	Tegucigalpa	Francisco Morazán	...	0.4	-1.2720	0.41	Medium	2012	12	11	50	2.347157	1.769514
2014-12-12	35654	CA-2014-162565	2014-12-12	12-12-2014	Same Day	RR-19315	Ralph Ritter	Consumer	Aurora	Illinois	...	0.2	3.6288	1.14	High	2014	12	12	50	2.344082	2.338724
2013-06-24	15893	ES-2013-3667448	2013-06-24	01-07-2013	Standard Class	TH-21235	Tiffany House	Corporate	Lucerne	Lucerne	...	0.0	126.4800	18.52	Medium	2013	6	24	26	5.837378	5.595529
2011-01-11	32102	CA-2011-134313	2011-01-11	07-11-2011	Standard Class	RA-19915	Russell Applegate	Consumer	Denver	Colorado	...	0.2	4.3176	2.12	Medium	2011	1	11	2	3.391082	3.765285
2014-02-04	6232	US-2014-146556	2014-02-04	07-04-2014	Standard Class	FH-14365	Fred Hopkins	Corporate	Panama City	Panama	...	0.4	-0.7680	0.48	Medium	2014	2	4	6	1.891789	1.742569
2013-08-28	19565	IT-2013-5108540	2013-08-28	30-08-2013	First Class	BE-11455	Brad Eason	Home Office	Aschaffenburg	Bavaria	...	0.0	26.1000	13.70	High	2013	8	28	35	4.813080	4.611649
2014-12-18	7986	MX-2014-101406	2014-12-18	21-12-2014	First Class	DA-13450	Dianna Arnett	Home Office	León	León	...	0.0	38.0800	21.20	High	2014	12	18	51	5.157887	4.508219
2012-12-12	23650	IN-2012-55618	2012-12-12	18-12-2012	Standard Class	MG-17695	Maureen Gnade	Consumer	Belgaum	Karnataka	...	0.0	16.5600	4.72	Medium	2012	12	12	50	3.996287	5.471598
2012-03-05	40847	CA-2012-160864	2012-03-05	06-05-2012	First Class	NF-18595	Nicole Fjeld	Home Office	San Jose	California	...	0.2	5.1930	1.95	High	2012	3	5	10	3.039426	2.628141
2011-06-04	48368	NI-2011-900	2011-06-04	10-04-2011	Standard Class	AS-90	Adam Shillingsburg	Consumer	Lagos	Lagos	...	0.7	-56.2560	2.95	High	2011	6	4	22	3.808092	3.499050
2013-06-13	51190	TU-2013-1610	2013-06-13	17-06-2013	Second Class	JS-5940	Joni Sundaresam	Home Office	Kars	Kars	...	0.6	-29.7900	4.37	High	2013	6	13	24	3.423486	4.374246
2013-05-24	37725	CA-2013-143714	2013-05-24	28-05-2013	Standard Class	CC-12370	Christopher Conant	Consumer	Philadelphia	Pennsylvania	...	0.4	-24.4764	7.54	Medium	2013	5	24	21	4.348927	4.807147
2012-12-13	46656	CM-2012-6440	2012-12-13	15-12-2012	First Class	BP-1230	Benjamin Patterson	Consumer	Yaounde	Centre	...	0.0	61.6200	94.38	Critical	2012	12	13	50	6.240782	5.507768
2014-09-16	13402	ES-2014-3240614	2014-09-16	20-09-2014	Second Class	BB-10990	Barry Blumstein	Corporate	Piacenza	Emilia-Romagna	...	0.0	8.5800	20.02	High	2014	9	16	38	5.016868	4.676560
2014-05-20	34922	CA-2014-113530	2014-05-20	22-05-2014	Second Class	BC-11125	Becky Castell	Home Office	San Francisco	California	...	0.0	1.0208	0.19	Medium	2014	5	20	21	1.625235	1.258461
2013-12-21	35017	CA-2013-151155	2013-12-21	25-12-2013	Standard Class	AB-10255	Alejandro Ballentine	Home Office	Jackson	Mississippi	...	0.0	7.3788	1.45	High	2013	12	21	51	3.236444	2.940220
2014-08-28	12657	ES-2014-2959093	2014-08-28	02-09-2014	Standard Class	CM-11935	Carlos Meador	Consumer	Hamm	North Rhine-Westphalia	...	0.0	10.5000	4.40	High	2014	8	28	35	3.736063	3.386084
2014-09-08	19435	ES-2014-5886915	2014-09-08	10-08-2014	First Class	BE-11410	Bobby Elias	Consumer	Madrid	Madrid	...	0.1	187.6080	28.33	Medium	2014	9	8	37	6.261138	6.268505
2014-11-30	28391	IN-2014-10020	2014-11-30	04-12-2014	Standard Class	AH-10075	Adam Hart	Corporate	Darbhanga	Bihar	...	0.0	179.7000	59.03	Medium	2014	11	30	48	6.328618	6.464588
2014-10-06	17541	ES-2014-3691479	2014-10-06	12-06-2014	First Class	FH-14365	Fred Hopkins	Corporate	Palma de Mallorca	Balearic Islands	...	0.0	148.3200	54.15	Medium	2014	10	6	41	6.240071	5.968145
20 rows × 30 columns


from xgboost import plot_importance
plot_importance(xgb_model , importance_type = "gain")                      #feature importance values for xgboost
     


     

df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
df['WeekOfYear'] = df.index.weekofyear

     

df.index = df['Order Date']
     

df.index
     
DatetimeIndex(['2012-07-31', '2013-05-02', '2013-10-17', '2013-01-28',
               '2013-05-11', '2013-06-28', '2011-07-11', '2012-04-14',
               '2014-10-14', '2012-01-28',
               ...
               '2014-11-29', '2014-09-06', '2012-12-28', '2014-05-30',
               '2014-05-08', '2014-06-19', '2014-06-20', '2013-02-12',
               '2012-02-18', '2012-05-22'],
              dtype='datetime64[ns]', name='Order Date', length=51290, freq=None)

import pandas as pd
df = pd.read_csv('Global Superstore.csv' , encoding = "ISO-8859-1" , parse_dates = ['Order Date'])
     

df.head()
     

import keras
from sklearn.preprocessing import MinMaxScaler                #importing min max scaler library for min max scaling of the dataset
     

df = df.drop(["Customer Name"] , axis = 1)                         
     

df = df.drop(["Customer ID"] , axis = 1)
     

df = df.drop(["Order ID"] , axis = 1)
     

df = df.drop(["Row ID"] , axis = 1)
     

df = df.drop(["Ship Date"] , axis = 1)
     

cat_col = ['Ship Mode' , 'Segment' , 'City' , 'State' , 'Country' , 'Market' , 'Region' , 'Product ID' , 'Category' , 'Sub-Category' , 'Product Name' , 'Order Priority']
     


     

import sklearn.preprocessing as preprocessing
for col in cat_col:
    lbl = preprocessing.LabelEncoder()                                          #doing label encoding for categorical attriutes for creating input for LSTM model 
    lbl.fit(df[col].values.astype('str'))
    df[col] = lbl.transform(df[col].values.astype('str'))                       
     

for kq1 in df.columns:
  if kq1 != 'Order Date':                                                       #replacing null values in the columns with the mean value of the columns
    df[kq1] = df[kq1].fillna(df[kq1].mean())
     

df.head()
     
Order Date	Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	Product ID	Category	Sub-Category	Product Name	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority
0	2012-07-31	1	0	2290	703	139	10024.000000	6	6	8246	2	0	2750	2309.650	7	0.0	762.1845	933.57	0
1	2013-05-02	2	1	3518	702	6	55190.379428	0	9	907	0	5	2525	3709.395	9	0.1	-288.7650	923.63	0
2	2013-10-17	0	0	497	820	6	55190.379428	0	9	10157	2	13	2502	5175.171	9	0.1	919.9710	915.49	3
3	2013-01-28	0	2	375	145	47	55190.379428	4	3	10146	2	13	2414	2892.510	5	0.1	-96.5400	910.16	3
4	2013-05-11	1	0	857	270	110	55190.379428	1	0	10249	2	6	3158	2832.960	8	0.0	311.5200	903.04	0

df.isnull().any(axis=1)
     

df.columns
     
Index(['Order Date', 'Ship Mode', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount',
       'Profit', 'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day',
       'WeekOfYear'],
      dtype='object')

df = df[['Order Date', 'Ship Mode', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name' , 'Quantity', 'Discount',
       'Profit', 'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day',
       'WeekOfYear','Sales']]
     

print(df['Order Date'].min(), df['Order Date'].max())                           #minimum order date and maximum order date
     
2011-01-01 00:00:00 2014-12-31 00:00:00

df = df.dropna(axis = 0)
     

df.columns
     
Index(['Order Date', 'Ship Mode', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit',
       'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day', 'WeekOfYear',
       'Sales'],
      dtype='object')

split_date = pd.datetime(2014,1,24)
train_set = df.loc[df['Order Date'] <= split_date]                    #splitting data set into train , test and validation
dev_set = df.loc[df['Order Date'] > split_date]
     

len(train_set)/(len(dev_set)+len(train_set))
     
0.67490738935465

split_date_dev = pd.datetime(2014,2,15)
val_set = dev_set.loc[dev_set['Order Date'] <= split_date_dev]
test_set = dev_set.loc[dev_set['Order Date'] > split_date_dev]
     

train_set = train_set.set_index('Order Date')
val_set = val_set.set_index('Order Date')
test_set = test_set.set_index('Order Date')
     

test_set.columns
     
Index(['Ship Mode', 'Segment', 'City', 'State', 'Country', 'Postal Code',
       'Market', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit',
       'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day',
       'WeekOfYear'],
      dtype='object')


     

train_set_array = train_set.iloc[:,:].values
val_set_array = val_set.iloc[:,:].values                                        #creating arrays from dataframe for input to LSTM
test_set_array = test_set.iloc[:,:].values

print("Shape of train, val and test array:\n",train_set_array.shape,"\n",val_set_array.shape,"\n",test_set_array.shape)
     
Shape of train, val and test array:
 (34616, 22) 
 (859, 22) 
 (15815, 22)

train_set_array[:,13]
     
array([7., 9., 9., ..., 3., 2., 3.])

sc = MinMaxScaler(feature_range=(0,1))
train_set_scaled = sc.fit_transform(train_set_array[:,:])                           #Min max scaling of the columns for input to the LSTM Model
val_set_scaled = sc.fit_transform(val_set_array[:,:])
test_set_scaled = sc.fit_transform(test_set_array[:,:])

print(train_set_scaled.shape, val_set_scaled.shape, test_set_scaled.shape)

     
(34616, 22) (859, 22) (15815, 22)

pd.DataFrame(sc.inverse_transform(train_set_scaled))
     

X_train = []
y_train = []
X_val = []
y_val = []
X_test = []
y_test = []

X_train, y_train = train_set_scaled[:,:-1], train_set_scaled[:,-1]
X_val, y_val = val_set_scaled[:,:-1], val_set_scaled[:,-1]                      #creating the validation , training and testing input arrays for the lstm model
X_test, y_test = test_set_scaled[:,:-1], test_set_scaled[:,-1]

print(X_train.shape, y_train.shape, X_val.shape, y_val.shape, X_test.shape, y_test.shape)
     
(34616, 21) (34616,) (859, 21) (859,) (15815, 21) (15815,)

X1_train , y1_train = train_set_scaled[]
     

def moving_test_window_preds(n_future_preds):

    preds_moving = []                                    # Use this to store the prediction made on each test window
    moving_test_window = [X_test[0,:].tolist()]          # Creating the first test window
    moving_test_window = np.array(moving_test_window)    # Making it an numpy array
    print(moving_test_window.shape)
    for i in range(n_future_preds):
        preds_one_step = regressor.predict(moving_test_window) # Note that this is already a scaled prediction so no need to rescale this
        preds_moving.append(preds_one_step[0,0]) # get the value from the numpy 2D array and append to predictions
        preds_one_step = preds_one_step.reshape(1,1,1) # Reshaping the prediction to 3D array for concatenation with moving test window
        moving_test_window = np.concatenate((moving_test_window[:,1:,:], preds_one_step), axis=1) # This is the new moving test window, where the first element from the window has been removed and the prediction  has been appended to the end
        
    
    
    return preds_moving

     

preds_moving = moving_test_window_preds(500)
     

from keras.preprocessing.sequence import TimeSeriesGenerator
train_data_gen = TimeSeriesGenerator(train_set)
     

X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_val = X_val.reshape((X_val.shape[0], 1, X_val.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))
     

print(X_train.shape, X_val.shape, X_test.shape)
     
(34616, 1, 17) (859, 1, 17) (15815, 1, 17)

X1_train = train_set_scaled[:,:-1]
X2_train = X1_train
Y1_train = train_set_scaled[: , :-1]
X1_train = X1_train.reshape((X1_train.shape[0] , 1 , X1_train.shape[1]))             
#Y1_train = Y1_train.reshape((Y1_train.shape[0] , 1 , Y1_train.shape[1]))
     

pd.DataFrame(train_set_scaled[:,:-1])
     

newmodel1 = Sequential()      #Sequential LSTM model initialized for predicting feature values for the future time steps 
newmodel1.add(LSTM(units = 10, return_sequences = True,  activation = 'relu', input_shape = (X1_train.shape[1] , 21)))
newmodel1.add(Dropout(0.5))
     

newmodel1.add(LSTM(units = 10, return_sequences = True,  activation = 'relu'))   #adding hidden layers to the LSTM model
newmodel1.add(Dropout(0.5))
     

newmodel1.add(LSTM(units = 21, return_sequences = False,   activation = 'relu'))   #output layer with 21 outputs for the feature values
     

newmodel1.compile(optimizer= 'adam', 
                  loss='mean_squared_error',               #compiling the model
                  metrics=['accuracy'])
     

history = newmodel1.fit(X1_train, 
              Y1_train, 
              epochs = 40, 
              batch_size = 512,                               #compiling the model and fitting the data
              validation_data = (X1_train, Y1_train),
              verbose = 1)
     
Train on 30594 samples, validate on 30594 samples
Epoch 1/40
30594/30594 [==============================] - 4s 125us/step - loss: 0.2963 - acc: 0.0435 - val_loss: 0.2725 - val_acc: 5.5566e-04
Epoch 2/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.2071 - acc: 0.0784 - val_loss: 0.1432 - val_acc: 0.0831
Epoch 3/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.1499 - acc: 0.2145 - val_loss: 0.1009 - val_acc: 0.5974
Epoch 4/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.1247 - acc: 0.2909 - val_loss: 0.0836 - val_acc: 0.6035
Epoch 5/40
30594/30594 [==============================] - 1s 46us/step - loss: 0.1118 - acc: 0.3473 - val_loss: 0.0785 - val_acc: 0.6035
Epoch 6/40
30594/30594 [==============================] - 1s 46us/step - loss: 0.1031 - acc: 0.3851 - val_loss: 0.0763 - val_acc: 0.6035
Epoch 7/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0959 - acc: 0.4218 - val_loss: 0.0748 - val_acc: 0.6035
Epoch 8/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0903 - acc: 0.4682 - val_loss: 0.0747 - val_acc: 0.6035
Epoch 9/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0867 - acc: 0.5048 - val_loss: 0.0754 - val_acc: 0.6035
Epoch 10/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0848 - acc: 0.5163 - val_loss: 0.0762 - val_acc: 0.6035
Epoch 11/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0834 - acc: 0.5344 - val_loss: 0.0769 - val_acc: 0.6035
Epoch 12/40
30594/30594 [==============================] - 1s 46us/step - loss: 0.0828 - acc: 0.5387 - val_loss: 0.0770 - val_acc: 0.6035
Epoch 13/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0824 - acc: 0.5470 - val_loss: 0.0771 - val_acc: 0.6035
Epoch 14/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0819 - acc: 0.5603 - val_loss: 0.0770 - val_acc: 0.6035
Epoch 15/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0816 - acc: 0.5579 - val_loss: 0.0768 - val_acc: 0.6035
Epoch 16/40
30594/30594 [==============================] - 1s 46us/step - loss: 0.0815 - acc: 0.5711 - val_loss: 0.0766 - val_acc: 0.6035
Epoch 17/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0812 - acc: 0.5678 - val_loss: 0.0764 - val_acc: 0.6035
Epoch 18/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0809 - acc: 0.5701 - val_loss: 0.0762 - val_acc: 0.6035
Epoch 19/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0807 - acc: 0.5748 - val_loss: 0.0756 - val_acc: 0.6035
Epoch 20/40
30594/30594 [==============================] - 1s 46us/step - loss: 0.0801 - acc: 0.5736 - val_loss: 0.0747 - val_acc: 0.6035
Epoch 21/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0797 - acc: 0.5685 - val_loss: 0.0743 - val_acc: 0.6035
Epoch 22/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0796 - acc: 0.5684 - val_loss: 0.0739 - val_acc: 0.6035
Epoch 23/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0794 - acc: 0.5681 - val_loss: 0.0739 - val_acc: 0.6035
Epoch 24/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0792 - acc: 0.5682 - val_loss: 0.0737 - val_acc: 0.6035
Epoch 25/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0790 - acc: 0.5683 - val_loss: 0.0735 - val_acc: 0.6035
Epoch 26/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0788 - acc: 0.5705 - val_loss: 0.0734 - val_acc: 0.6035
Epoch 27/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0786 - acc: 0.5708 - val_loss: 0.0732 - val_acc: 0.6035
Epoch 28/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0783 - acc: 0.5722 - val_loss: 0.0729 - val_acc: 0.6035
Epoch 29/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0783 - acc: 0.5687 - val_loss: 0.0727 - val_acc: 0.6035
Epoch 30/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0780 - acc: 0.5701 - val_loss: 0.0723 - val_acc: 0.6035
Epoch 31/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0779 - acc: 0.5650 - val_loss: 0.0722 - val_acc: 0.6035
Epoch 32/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0775 - acc: 0.5699 - val_loss: 0.0719 - val_acc: 0.6035
Epoch 33/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0774 - acc: 0.5695 - val_loss: 0.0716 - val_acc: 0.6035
Epoch 34/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0772 - acc: 0.5704 - val_loss: 0.0714 - val_acc: 0.6035
Epoch 35/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0769 - acc: 0.5633 - val_loss: 0.0714 - val_acc: 0.6035
Epoch 36/40
30594/30594 [==============================] - 1s 44us/step - loss: 0.0767 - acc: 0.5607 - val_loss: 0.0710 - val_acc: 0.6035
Epoch 37/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0765 - acc: 0.5602 - val_loss: 0.0708 - val_acc: 0.6035
Epoch 38/40
30594/30594 [==============================] - 1s 46us/step - loss: 0.0763 - acc: 0.5657 - val_loss: 0.0705 - val_acc: 0.6037
Epoch 39/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0760 - acc: 0.5565 - val_loss: 0.0703 - val_acc: 0.6038
Epoch 40/40
30594/30594 [==============================] - 1s 45us/step - loss: 0.0758 - acc: 0.5523 - val_loss: 0.0703 - val_acc: 0.6040

X_test.shape
     
(16973, 1, 21)

X1_train.shape
     
(30594, 1, 21)

tkq2 = pd.DataFrame(X_test.reshape(X_test.shape[0] , 21))
kq2
     
0	1	2	3	4	5	6	7	8	9	...	11	12	13	14	15	16	17	18	19	20
0	1.000000	0.5	0.762115	0.175824	0.952055	0.964314	1.000000	1.000000	0.371756	0.5	...	0.377344	0.363121	0.307692	0.2500	0.544175	1.000000	0.666667	0.0	0.818182	0.433333
1	0.666667	0.5	0.672357	0.398352	0.301370	0.547398	0.666667	0.250000	0.232093	0.5	...	0.192237	0.133515	0.230769	0.1250	0.381340	0.923901	0.000000	0.0	0.545455	1.000000
2	0.666667	0.5	0.372522	0.461538	0.952055	0.416366	1.000000	0.833333	0.813685	1.0	...	0.605228	0.160682	0.615385	0.0000	0.412640	0.899744	0.000000	0.0	0.181818	0.333333
3	1.000000	0.5	0.712830	0.918498	0.431507	0.547398	0.666667	0.833333	0.267470	0.5	...	0.508582	0.568458	1.000000	0.0000	0.740444	0.897001	0.666667	0.0	0.636364	0.266667
4	0.000000	0.5	0.898128	0.750916	0.041096	0.547398	0.000000	0.750000	0.839926	1.0	...	0.196990	0.183231	0.615385	0.1250	0.366326	0.883874	0.000000	0.0	0.000000	1.000000
5	0.666667	0.0	0.917676	0.476190	0.876712	0.547398	0.166667	0.000000	0.529012	0.5	...	0.558490	0.243530	0.384615	0.0000	0.441125	0.879783	0.333333	0.0	0.363636	0.366667
6	0.000000	0.0	0.431993	0.210623	0.554795	0.547398	0.833333	0.583333	0.981242	1.0	...	0.637708	0.122390	0.230769	0.0000	0.405826	0.840125	0.000000	0.0	0.545455	1.000000
7	0.000000	0.0	0.838106	0.793956	0.260274	0.547398	0.833333	0.250000	0.199922	0.0	...	0.482176	0.150437	0.538462	0.2500	0.413494	0.839457	0.000000	0.0	0.363636	0.266667
8	0.333333	0.5	0.145374	0.657509	0.952055	0.260373	1.000000	0.833333	0.917776	1.0	...	0.266174	0.571415	0.230769	0.6250	0.000000	0.777718	0.333333	0.0	0.363636	0.333333
9	1.000000	1.0	0.332048	0.363553	0.390411	0.547398	0.000000	0.333333	0.977257	1.0	...	0.637972	0.322749	0.461538	0.0000	0.423534	0.759128	0.333333	0.0	0.909091	0.333333
10	0.666667	0.5	0.882709	0.462454	0.390411	0.547398	0.000000	0.333333	0.046457	0.0	...	0.818062	0.404830	0.923077	0.0000	0.562219	0.758736	1.000000	0.0	0.727273	0.833333
11	0.000000	0.0	0.819383	0.819597	0.178082	0.547398	0.000000	0.666667	0.055205	0.0	...	0.667019	0.197204	0.384615	0.0000	0.374085	0.743062	0.333333	0.0	0.636364	0.900000
12	0.666667	0.0	0.678139	0.709707	0.958904	0.547398	0.833333	0.833333	0.058509	0.0	...	0.452865	0.248058	0.769231	0.0000	0.445845	0.731283	0.333333	0.0	1.000000	0.566667
13	0.000000	0.0	0.091685	0.582418	0.404110	0.547398	0.500000	0.416667	0.830693	1.0	...	0.220491	0.150591	0.538462	0.0000	0.413546	0.727181	0.000000	0.0	0.727273	0.566667
14	0.333333	0.5	0.390419	0.175824	0.952055	0.931716	1.000000	1.000000	0.844786	1.0	...	0.467124	0.171400	0.307692	0.2500	0.443181	0.726120	0.333333	0.0	0.545455	0.800000
15	0.000000	0.0	0.323513	0.967033	0.041096	0.547398	0.000000	0.750000	0.248323	0.5	...	0.192765	0.299372	0.615385	0.1250	0.473889	0.708014	0.333333	0.0	0.363636	0.233333
16	0.666667	0.0	0.863711	0.304029	0.952055	0.312559	1.000000	0.833333	0.949947	1.0	...	0.783206	0.311972	0.923077	0.2500	0.394659	0.702367	1.000000	0.0	0.636364	0.766667
17	0.666667	0.0	0.250275	0.253663	0.068493	0.547398	0.000000	0.333333	0.012829	0.0	...	0.774228	0.218781	0.461538	0.0000	0.418742	0.702137	0.333333	0.0	0.909091	0.066667
18	0.666667	0.5	0.609031	0.532051	0.321918	0.547398	0.666667	0.250000	0.956556	1.0	...	0.789015	0.319479	0.461538	0.0000	0.393287	0.696559	1.000000	0.0	0.909091	0.233333
19	1.000000	0.0	0.971641	0.423993	0.178082	0.547398	0.000000	0.666667	0.050345	0.0	...	0.766570	0.360624	0.769231	0.0000	0.425793	0.686301	0.333333	0.0	0.000000	0.566667
20	0.000000	0.0	0.811674	0.042125	0.815068	0.547398	0.666667	0.833333	0.047526	0.0	...	0.774228	0.156263	0.307692	0.0000	0.463083	0.684469	0.333333	0.0	0.545455	0.366667
21	0.000000	0.5	0.729075	0.932234	0.390411	0.547398	0.000000	0.333333	0.190786	0.0	...	0.247161	0.137142	0.230769	0.0000	0.425466	0.683155	0.000000	0.0	1.000000	0.500000
22	0.333333	1.0	0.355176	0.272894	0.554795	0.547398	0.833333	0.583333	0.981534	1.0	...	0.789015	0.121687	0.230769	0.0000	0.374932	0.683109	0.000000	0.0	0.909091	0.633333
23	0.000000	0.5	0.664648	0.869963	0.397260	0.547398	0.000000	0.916667	0.188259	0.0	...	0.160285	0.244773	0.461538	0.5875	0.320757	0.676010	0.333333	0.0	0.636364	0.833333
24	0.666667	0.0	0.572412	0.945971	0.041096	0.547398	0.000000	0.750000	0.964914	1.0	...	0.081595	0.204500	0.307692	0.1250	0.444972	0.670604	0.000000	0.0	0.363636	0.500000
25	1.000000	0.0	0.509912	0.654762	0.301370	0.547398	0.666667	0.250000	0.077850	0.0	...	0.485081	0.409221	1.000000	0.1250	0.369654	0.660313	0.333333	0.0	0.909091	0.600000
26	0.666667	0.5	0.572137	0.586996	0.582192	0.547398	0.166667	0.000000	0.829721	1.0	...	0.228413	0.378641	1.000000	0.0000	0.609592	0.655126	1.000000	0.0	0.818182	0.900000
27	0.666667	0.0	0.413271	0.591575	0.952055	0.485943	1.000000	0.250000	0.389542	0.5	...	0.394243	0.388836	0.230769	0.0000	0.600779	0.654550	0.333333	0.0	0.000000	0.533333
28	0.666667	0.0	0.687225	0.711538	0.952055	0.177437	1.000000	0.500000	0.068811	0.0	...	0.433853	0.315420	0.615385	0.3750	0.303894	0.653052	1.000000	0.0	0.636364	0.566667
29	0.666667	0.5	0.599945	0.750000	0.150685	0.547398	0.333333	0.083333	0.926329	1.0	...	0.637708	0.275969	0.384615	0.0000	0.473392	0.629898	0.000000	0.0	1.000000	0.733333
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
16943	1.000000	0.0	0.687225	0.711538	0.952055	0.177529	1.000000	0.500000	0.379337	0.5	...	0.537101	0.000105	0.076923	0.8750	0.363492	0.000058	1.000000	0.0	0.727273	0.700000
16944	0.666667	0.0	0.526982	0.461538	0.952055	0.393731	1.000000	0.833333	0.358441	0.5	...	0.399789	0.000863	0.000000	0.0000	0.364194	0.000058	1.000000	0.0	1.000000	0.966667
16945	1.000000	0.0	0.160242	0.045788	0.910959	0.547398	0.500000	0.416667	0.712897	0.5	...	0.862688	0.000255	0.000000	0.7500	0.363531	0.000058	1.000000	0.0	1.000000	0.400000
16946	1.000000	0.5	0.482930	0.501832	0.643836	0.547398	0.166667	0.000000	0.216639	0.5	...	0.021389	0.000143	0.000000	0.8750	0.363456	0.000058	1.000000	0.0	1.000000	0.366667
16947	1.000000	0.0	0.364537	0.361722	1.000000	0.547398	0.166667	0.000000	0.765575	0.5	...	0.935041	0.000054	0.000000	0.8750	0.363412	0.000058	1.000000	0.0	0.909091	0.766667
16948	1.000000	0.0	0.147026	0.167582	0.801370	0.547398	0.000000	0.666667	0.736223	0.5	...	0.337206	0.000461	0.000000	0.6250	0.363557	0.000046	1.000000	0.0	1.000000	0.333333
16949	0.000000	1.0	0.525055	0.175824	0.952055	0.905028	1.000000	1.000000	0.955681	1.0	...	0.998680	0.019966	0.307692	0.2500	0.365293	0.000046	0.333333	0.0	0.909091	0.166667
16950	1.000000	0.0	0.384637	0.900183	0.952055	0.771896	1.000000	0.250000	0.113616	0.0	...	0.857407	0.000253	0.076923	0.7500	0.363382	0.000046	1.000000	0.0	0.818182	0.033333
16951	1.000000	0.0	0.384637	0.900183	0.952055	0.772153	1.000000	0.250000	0.353387	0.5	...	0.885926	0.000053	0.000000	1.0000	0.363451	0.000046	1.000000	0.0	0.363636	0.766667
16952	1.000000	0.5	0.482930	0.501832	0.643836	0.547398	0.166667	0.000000	0.523569	0.5	...	0.523105	0.000159	0.000000	0.8750	0.363196	0.000046	1.000000	0.0	1.000000	0.366667
16953	1.000000	0.0	0.952093	0.251832	0.643836	0.547398	0.166667	0.000000	0.519681	0.5	...	0.495643	0.000167	0.000000	0.8750	0.363329	0.000046	1.000000	0.0	1.000000	0.566667
16954	0.000000	0.5	0.393447	0.595238	0.116438	0.547398	0.833333	0.833333	0.472641	0.5	...	0.884077	0.002588	0.461538	0.0000	0.365227	0.000035	0.333333	0.0	1.000000	0.700000
16955	0.000000	0.0	0.837280	0.284799	0.945205	0.547398	0.666667	0.583333	0.348819	0.5	...	0.518088	0.001918	0.076923	0.0000	0.363994	0.000035	1.000000	0.0	0.363636	0.733333
16956	1.000000	0.5	0.483756	0.740842	0.657534	0.547398	0.000000	0.333333	0.605404	0.5	...	0.428835	0.001280	0.076923	0.6250	0.362381	0.000035	1.000000	0.0	0.636364	0.200000
16957	1.000000	0.0	0.384637	0.900183	0.952055	0.772153	1.000000	0.250000	0.343279	0.5	...	0.404014	0.000175	0.000000	1.0000	0.363184	0.000035	1.000000	0.0	0.272727	0.533333
16958	0.000000	0.0	0.069934	0.175824	0.952055	0.938518	1.000000	1.000000	0.480416	0.5	...	0.057301	0.002468	0.461538	0.0000	0.365227	0.000035	1.000000	0.0	0.727273	0.966667
16959	0.666667	0.0	0.436399	0.442308	0.732877	0.547398	0.500000	0.416667	0.763048	0.5	...	0.904938	0.003806	0.000000	0.0000	0.364244	0.000035	1.000000	0.0	1.000000	0.533333
16960	0.333333	0.0	0.966134	0.555861	0.150685	0.547398	0.333333	0.083333	0.326368	0.5	...	0.118035	0.000446	0.000000	0.0000	0.363798	0.000035	1.000000	0.0	1.000000	0.733333
16961	1.000000	0.0	0.183095	0.197802	0.301370	0.547398	0.666667	0.250000	0.562251	0.5	...	0.112490	0.001245	0.076923	0.0000	0.364193	0.000023	1.000000	0.0	0.363636	0.233333
16962	1.000000	0.5	0.683095	0.967033	0.041096	0.547398	0.000000	0.750000	0.456993	0.5	...	0.422498	0.003336	0.076923	0.1250	0.364476	0.000023	1.000000	0.0	0.909091	0.800000
16963	1.000000	0.0	0.747247	0.057692	0.746575	0.547398	0.500000	0.416667	0.402274	0.5	...	0.235543	0.000350	0.000000	0.0000	0.363841	0.000023	1.000000	0.0	0.727273	0.100000
16964	0.666667	0.0	0.783866	0.580586	0.205479	0.547398	0.833333	0.166667	0.301584	0.5	...	0.185371	0.001348	0.076923	0.0000	0.363689	0.000023	1.000000	0.0	0.272727	0.533333
16965	0.000000	1.0	0.931443	0.595238	0.116438	0.547398	0.833333	0.833333	0.563903	0.5	...	0.673092	0.000391	0.000000	0.0000	0.363640	0.000012	0.333333	0.0	0.909091	0.266667
16966	1.000000	0.5	0.673733	0.900183	0.952055	0.776370	1.000000	0.250000	0.247643	0.5	...	0.361236	0.000084	0.076923	1.0000	0.363214	0.000012	1.000000	0.0	0.727273	0.166667
16967	0.000000	1.0	0.581498	0.563187	0.910959	0.547398	0.500000	0.416667	0.394305	0.5	...	0.185107	0.002406	0.384615	0.7500	0.358942	0.000012	1.000000	0.0	0.909091	0.933333
16968	0.000000	0.0	0.130507	0.874542	0.116438	0.547398	0.833333	0.833333	0.616289	0.5	...	0.429892	0.005968	0.307692	0.0000	0.364508	0.000012	0.333333	0.0	0.727273	0.166667
16969	0.333333	0.5	0.531388	0.931319	0.390411	0.547398	0.000000	0.333333	0.586646	0.5	...	0.306311	0.001893	0.076923	0.0000	0.363813	0.000000	0.333333	0.0	0.363636	0.966667
16970	1.000000	1.0	0.898128	0.750916	0.041096	0.547398	0.000000	0.750000	0.358538	0.5	...	0.107209	0.004115	0.307692	0.1250	0.365526	0.000000	1.000000	0.0	0.363636	0.233333
16971	0.333333	0.5	0.474394	0.375458	0.445205	0.547398	0.000000	0.666667	0.467490	0.5	...	0.063111	0.004618	0.307692	0.0000	0.364063	0.000000	1.000000	0.0	0.454545	0.600000
16972	1.000000	0.0	0.384637	0.900183	0.952055	0.772153	1.000000	0.250000	0.254835	0.5	...	0.507526	0.000000	0.000000	1.0000	0.363531	0.000000	1.000000	0.0	0.454545	0.633333
16973 rows × 21 columns


X_train.shape[0]-16000
     
14594

cols2
     

# for i in range(xForecast.shape[1]):
#     newSteps.append(newModel.predict(xForecast[:,i:i+1,:]))
# forecastFromInput = np.asarray(newSteps).reshape(1,xForecast.shape[1],2)
#newmodel1.set_weights(regressor.get_weights())
import numpy as np
newSteps = []
for i in range(100):
  newSteps.append(newmodel1.predict(X_test[i:i+1,:,:]))
forecastFromInput = np.asarray(newSteps)
forecastFromInput.shape
#forecastfromInput1 = sc.inverse_transform(forecastFromInput.reshape(13794,21))
kq1 = pd.DataFrame(forecastFromInput.reshape(100,21) )
kq1

     
0	1	2	3	4	5	6	7	8	9	...	11	12	13	14	15	16	17	18	19	20
0	0.776427	0.337928	0.536129	0.540248	0.596604	0.579665	0.631970	0.535768	0.438142	0.443525	...	0.495186	0.010187	0.206132	0.186848	0.342770	0.026366	0.715196	0.524162	0.557522	0.511222
1	0.437349	0.250007	0.371452	0.384670	0.383459	0.411411	0.383180	0.388671	0.325231	0.335564	...	0.419543	0.011230	0.162311	0.146787	0.275963	0.038522	0.408707	0.366050	0.410863	0.434598
2	0.561277	0.292208	0.448658	0.466290	0.459282	0.500758	0.469744	0.449998	0.409583	0.418533	...	0.466324	0.011136	0.182047	0.160969	0.311707	0.035827	0.519725	0.451444	0.481418	0.486227
3	0.653983	0.314572	0.487862	0.499763	0.519576	0.538094	0.542004	0.488240	0.420162	0.428514	...	0.478120	0.010761	0.192936	0.172913	0.326151	0.031898	0.602999	0.485558	0.516282	0.497662
4	0.500006	0.280410	0.435141	0.465133	0.411496	0.496626	0.410062	0.430108	0.452583	0.460138	...	0.470497	0.011602	0.177099	0.151191	0.310489	0.040120	0.463059	0.453740	0.472004	0.484666
5	0.458865	0.259094	0.390338	0.406994	0.396472	0.435668	0.397260	0.402061	0.354708	0.364734	...	0.443402	0.011295	0.166888	0.148856	0.285916	0.038585	0.428079	0.389302	0.428832	0.460754
6	0.479486	0.271827	0.417128	0.442121	0.406255	0.472767	0.406647	0.418809	0.409725	0.418976	...	0.459144	0.011493	0.173357	0.150413	0.301247	0.039550	0.445576	0.426474	0.454837	0.478546
7	0.422298	0.244489	0.361286	0.373869	0.373225	0.399561	0.371200	0.380653	0.314802	0.325225	...	0.405888	0.011229	0.159657	0.144878	0.271179	0.038811	0.395162	0.355122	0.401573	0.421912
8	0.646137	0.317930	0.493407	0.513948	0.499525	0.551013	0.514105	0.486169	0.466265	0.473205	...	0.487910	0.010990	0.193145	0.168729	0.331334	0.033623	0.594596	0.505271	0.521782	0.500619
9	0.695031	0.342828	0.520733	0.563980	0.457991	0.593220	0.450874	0.492297	0.629337	0.630259	...	0.523720	0.011496	0.194543	0.159993	0.346219	0.036728	0.636166	0.587171	0.543437	0.509130
10	0.481521	0.264148	0.397059	0.410579	0.411498	0.440402	0.415947	0.409918	0.348912	0.358930	...	0.443842	0.011171	0.168898	0.152052	0.287409	0.037405	0.448298	0.393572	0.434224	0.469202
11	0.422187	0.244591	0.361727	0.374567	0.373125	0.400293	0.371015	0.380857	0.316134	0.326541	...	0.406556	0.011236	0.159750	0.144821	0.271503	0.038859	0.395072	0.355818	0.402038	0.422520
12	0.660244	0.312756	0.484978	0.490958	0.535012	0.529946	0.563228	0.490753	0.388161	0.397213	...	0.471401	0.010609	0.193133	0.176686	0.322702	0.030684	0.608870	0.472364	0.513861	0.496181
13	0.455340	0.262571	0.401142	0.424702	0.391847	0.453849	0.390230	0.406467	0.391166	0.400630	...	0.452303	0.011498	0.169198	0.147447	0.293716	0.039990	0.424412	0.408199	0.440153	0.473284
14	0.569065	0.295670	0.455389	0.474694	0.462717	0.509535	0.473550	0.454853	0.420971	0.429602	...	0.470056	0.011154	0.183758	0.161854	0.315238	0.035804	0.525936	0.460433	0.488077	0.488887
15	0.427699	0.249412	0.374695	0.392480	0.376142	0.419289	0.373296	0.388385	0.345897	0.355953	...	0.426261	0.011372	0.162736	0.144765	0.279608	0.039626	0.400115	0.374092	0.414966	0.440410
16	0.849650	0.355929	0.552481	0.561310	0.594563	0.594192	0.625352	0.543663	0.519030	0.520889	...	0.517087	0.010132	0.207402	0.182488	0.348566	0.024808	0.790163	0.570325	0.564137	0.513184
17	0.430012	0.247747	0.367829	0.381395	0.378561	0.407765	0.377397	0.385500	0.323413	0.333795	...	0.414898	0.011247	0.161341	0.145834	0.274564	0.038768	0.402054	0.362698	0.407768	0.430214
18	0.779906	0.356557	0.537702	0.570531	0.504245	0.598527	0.507782	0.514195	0.613901	0.614136	...	0.528334	0.010992	0.199637	0.167331	0.348782	0.031531	0.719096	0.597478	0.553001	0.511223
19	0.447732	0.253244	0.376799	0.389737	0.390207	0.417313	0.391136	0.393359	0.328671	0.339144	...	0.426682	0.011203	0.163731	0.148101	0.278258	0.038202	0.417967	0.371636	0.415724	0.441315
20	0.488435	0.265320	0.396995	0.408180	0.418382	0.438645	0.425228	0.411970	0.336518	0.347259	...	0.441548	0.011081	0.169289	0.154026	0.286503	0.036676	0.454169	0.390633	0.434448	0.467819
21	0.430136	0.248384	0.370524	0.385509	0.378134	0.412180	0.376524	0.386878	0.331463	0.341719	...	0.419200	0.011283	0.161895	0.145547	0.276466	0.039020	0.402135	0.367084	0.410638	0.434250
22	0.594128	0.308678	0.478423	0.506978	0.460845	0.542104	0.465833	0.467227	0.488142	0.495051	...	0.487325	0.011316	0.188162	0.161109	0.327927	0.036848	0.546820	0.500670	0.509817	0.497224
23	0.457972	0.256741	0.384304	0.398148	0.396499	0.426480	0.398544	0.399140	0.338748	0.348872	...	0.437797	0.011210	0.165605	0.149255	0.281961	0.038062	0.427016	0.380346	0.422829	0.451940
24	0.612332	0.319204	0.494390	0.533536	0.446548	0.566429	0.442981	0.473417	0.560146	0.564038	...	0.503901	0.011582	0.190161	0.158433	0.336730	0.038597	0.560621	0.538485	0.524509	0.503211
25	0.561904	0.287361	0.436684	0.446692	0.467201	0.481448	0.482726	0.446277	0.364920	0.375198	...	0.455547	0.010924	0.179857	0.163415	0.303451	0.034395	0.520296	0.429873	0.470316	0.481440
26	0.675193	0.331137	0.511281	0.542605	0.484094	0.577248	0.488470	0.492829	0.547572	0.551635	...	0.506884	0.011181	0.195206	0.165117	0.340939	0.034821	0.619480	0.548619	0.537089	0.506619
27	0.633226	0.307993	0.475745	0.485698	0.512139	0.523740	0.534712	0.479444	0.398320	0.407447	...	0.470975	0.010766	0.190179	0.171896	0.320433	0.032187	0.584382	0.469152	0.505591	0.493800
28	0.872303	0.343150	0.561414	0.552278	0.670873	0.588740	0.722544	0.569345	0.416959	0.419390	...	0.500602	0.009549	0.214070	0.198057	0.347487	0.020913	0.808923	0.527891	0.575474	0.515946
29	0.598617	0.314461	0.487554	0.524441	0.446225	0.558062	0.444352	0.468948	0.540801	0.545768	...	0.498623	0.011538	0.188938	0.158207	0.333758	0.038507	0.549110	0.526037	0.518569	0.500975
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
70	0.486557	0.268656	0.407807	0.425438	0.413904	0.455955	0.417812	0.416139	0.372873	0.382558	...	0.450539	0.011274	0.171505	0.152281	0.294039	0.037951	0.452524	0.408541	0.444823	0.473894
71	0.928768	0.350674	0.569800	0.556282	0.696069	0.589000	0.756665	0.577830	0.438266	0.439554	...	0.509318	0.009335	0.215526	0.198172	0.348715	0.018721	0.872313	0.543709	0.575527	0.515087
72	0.563684	0.288017	0.438277	0.448361	0.469175	0.483332	0.485285	0.447710	0.365334	0.375550	...	0.455976	0.010918	0.180371	0.163980	0.304255	0.034293	0.521652	0.431032	0.472012	0.482160
73	0.704716	0.333796	0.517950	0.540583	0.517299	0.576951	0.530848	0.505137	0.510040	0.514882	...	0.502532	0.010838	0.198361	0.171722	0.341088	0.032011	0.646983	0.539899	0.542354	0.507383
74	0.571208	0.297815	0.459622	0.481143	0.461247	0.516107	0.470939	0.456886	0.434284	0.442611	...	0.473547	0.011208	0.184687	0.161484	0.317918	0.036143	0.527444	0.468042	0.492157	0.490721
75	0.519855	0.275070	0.414619	0.425467	0.439769	0.457973	0.450600	0.427134	0.349037	0.359633	...	0.447672	0.011018	0.174024	0.158256	0.294186	0.035706	0.482278	0.408074	0.450570	0.474895
76	0.561462	0.288168	0.439682	0.451948	0.463967	0.486386	0.478122	0.446990	0.378734	0.388278	...	0.458782	0.010986	0.180299	0.162430	0.305561	0.034820	0.519867	0.436002	0.472953	0.482535
77	0.775212	0.357400	0.536017	0.574292	0.487897	0.599978	0.486488	0.509784	0.639173	0.638583	...	0.532383	0.011152	0.198289	0.164321	0.349125	0.032671	0.714004	0.605720	0.551022	0.511204
78	0.442096	0.251357	0.373896	0.387007	0.386427	0.414094	0.386724	0.390817	0.327102	0.337388	...	0.422845	0.011218	0.162942	0.147366	0.276996	0.038375	0.412923	0.368611	0.413097	0.437817
79	0.676016	0.324597	0.504440	0.523147	0.516180	0.560655	0.533264	0.496627	0.472277	0.478798	...	0.491843	0.010843	0.195916	0.171715	0.335006	0.032332	0.621910	0.515765	0.530895	0.503158
80	0.713416	0.327769	0.512808	0.521903	0.554975	0.561509	0.582932	0.511301	0.435628	0.442851	...	0.487528	0.010516	0.199503	0.179193	0.335432	0.029492	0.657479	0.508497	0.537709	0.504689
81	0.530833	0.287932	0.444036	0.469307	0.434234	0.502505	0.438285	0.441038	0.436829	0.445390	...	0.470099	0.011395	0.180133	0.155919	0.312729	0.038134	0.491138	0.456644	0.478942	0.486607
82	0.585203	0.310127	0.481590	0.517791	0.442301	0.551454	0.440628	0.464491	0.529959	0.535298	...	0.495164	0.011558	0.187622	0.157439	0.331315	0.038784	0.537334	0.517377	0.513635	0.499344
83	0.422298	0.244489	0.361286	0.373869	0.373225	0.399561	0.371200	0.380653	0.314802	0.325225	...	0.405888	0.011229	0.159657	0.144878	0.271179	0.038811	0.395162	0.355122	0.401573	0.421912
84	0.437430	0.251439	0.375749	0.391105	0.383496	0.418213	0.382864	0.390936	0.336294	0.346582	...	0.426466	0.011288	0.163320	0.146618	0.278928	0.038882	0.408689	0.372501	0.415372	0.440744
85	0.442764	0.251314	0.373787	0.386695	0.386690	0.413836	0.387072	0.390885	0.326536	0.336802	...	0.422639	0.011210	0.162905	0.147427	0.276855	0.038323	0.413495	0.368440	0.412987	0.437746
86	0.430955	0.249737	0.373789	0.390101	0.378824	0.416916	0.376978	0.388642	0.338840	0.349044	...	0.424226	0.011324	0.162678	0.145528	0.278519	0.039245	0.402963	0.371521	0.413806	0.438608
87	0.563536	0.297625	0.460221	0.485494	0.450936	0.520102	0.456746	0.454408	0.453954	0.461938	...	0.476940	0.011322	0.184128	0.159101	0.319502	0.037180	0.520405	0.474974	0.493274	0.491406
88	0.939498	0.364017	0.570361	0.564334	0.669093	0.594749	0.723434	0.568707	0.497367	0.498528	...	0.521020	0.009636	0.213056	0.191120	0.350905	0.020149	0.888473	0.574532	0.571280	0.514437
89	0.770263	0.353681	0.535630	0.567869	0.503369	0.597183	0.507283	0.512382	0.606331	0.607087	...	0.525751	0.010966	0.199468	0.167240	0.348241	0.031717	0.709715	0.592294	0.552200	0.511114
90	0.773005	0.352610	0.536837	0.564722	0.517532	0.595603	0.525764	0.516529	0.582847	0.584116	...	0.522193	0.010852	0.200610	0.170169	0.347821	0.030797	0.712322	0.584276	0.553951	0.511156
91	0.464786	0.260063	0.390260	0.404993	0.401490	0.433907	0.404235	0.403517	0.345834	0.356081	...	0.441855	0.011230	0.167183	0.150218	0.285039	0.038026	0.433109	0.387109	0.428467	0.459833
92	0.512054	0.276886	0.422297	0.440419	0.428556	0.472533	0.434559	0.428037	0.388127	0.397591	...	0.456532	0.011244	0.175124	0.155053	0.300515	0.037351	0.475234	0.425119	0.458189	0.478441
93	0.838616	0.367380	0.547220	0.576414	0.526465	0.600552	0.535798	0.524648	0.628760	0.627971	...	0.535882	0.010809	0.201500	0.169160	0.350384	0.028913	0.780820	0.613369	0.555150	0.511582
94	0.745884	0.335262	0.527482	0.537691	0.567365	0.576250	0.595519	0.523575	0.456376	0.461752	...	0.496002	0.010419	0.202993	0.181613	0.341215	0.028334	0.686030	0.525965	0.550525	0.509366
95	0.757323	0.338759	0.531621	0.543076	0.566458	0.581105	0.593123	0.525492	0.472381	0.477216	...	0.500263	0.010418	0.203556	0.180931	0.343056	0.028171	0.697035	0.535355	0.553437	0.510345
96	0.640164	0.320938	0.497477	0.526460	0.478215	0.562283	0.484444	0.483197	0.513889	0.519598	...	0.497093	0.011199	0.192671	0.164338	0.335494	0.035439	0.587693	0.525383	0.526101	0.502934
97	0.437223	0.249502	0.370440	0.383272	0.383274	0.410127	0.383301	0.388272	0.322902	0.333286	...	0.418200	0.011211	0.162083	0.146888	0.275382	0.038431	0.408355	0.364906	0.410102	0.433546
98	0.598748	0.308749	0.478306	0.505206	0.464747	0.540573	0.470698	0.468044	0.482622	0.489655	...	0.486275	0.011274	0.188160	0.161609	0.327294	0.036462	0.551816	0.498773	0.509274	0.496710
99	0.506811	0.279858	0.431032	0.456175	0.420321	0.488316	0.422411	0.430322	0.425269	0.434083	...	0.464934	0.011434	0.176687	0.153104	0.307166	0.038826	0.469765	0.442827	0.467477	0.482599
100 rows × 21 columns


regressor.predict(forecastFromInput)
     
array([[0.5314704 ],
       [0.39313424],
       [0.45735168],
       [0.49087316],
       [0.44787303],
       [0.40918922],
       [0.43232912],
       [0.38583964],
       [0.4953358 ],
       [0.512759  ],
       [0.41426662],
       [0.38612795],
       [0.48926568],
       [0.41900265],
       [0.4636553 ],
       [0.39664876],
       [0.5353898 ],
       [0.39039642],
       [0.52174854],
       [0.39742848],
       [0.41438726],
       [0.3928929 ],
       [0.4834423 ],
       [0.4038328 ],
       [0.4963384 ],
       [0.4476125 ],
       [0.50849724],
       [0.48100865],
       [0.5511632 ],
       [0.49095023],
       [0.5165312 ],
       [0.5428799 ],
       [0.4728846 ],
       [0.46403646],
       [0.44991782],
       [0.43193698],
       [0.4732233 ],
       [0.45209083],
       [0.4978721 ],
       [0.38734654],
       [0.5200686 ],
       [0.48327404],
       [0.40792447],
       [0.5260299 ],
       [0.43805307],
       [0.43924546],
       [0.51411414],
       [0.4980624 ],
       [0.42824653],
       [0.4153533 ],
       [0.422633  ],
       [0.5209394 ],
       [0.41294026],
       [0.5239126 ],
       [0.44099885],
       [0.44339508],
       [0.40397766],
       [0.50411534],
       [0.5478094 ],
       [0.4017713 ],
       [0.53186196],
       [0.4435888 ],
       [0.38946372],
       [0.52332604],
       [0.45742583],
       [0.5157812 ],
       [0.5155367 ],
       [0.4038899 ],
       [0.5344359 ],
       [0.54225475],
       [0.42342037],
       [0.54971445],
       [0.44929594],
       [0.51427746],
       [0.46735483],
       [0.42919803],
       [0.4498134 ],
       [0.5192584 ],
       [0.39512694],
       [0.5039493 ],
       [0.5111963 ],
       [0.45461357],
       [0.48643658],
       [0.38583964],
       [0.39704868],
       [0.39504826],
       [0.39563993],
       [0.4680732 ],
       [0.5422673 ],
       [0.5212641 ],
       [0.523556  ],
       [0.40887126],
       [0.43567097],
       [0.5228309 ],
       [0.5234195 ],
       [0.5260489 ],
       [0.49863708],
       [0.3924916 ],
       [0.48295787],
       [0.44391775]], dtype=float32)

forecastFromInput
     
(16973, 1, 21)

Y1_train.shape
     
(30593, 1, 22)

history = newmodel1.fit(X1_train, 
              Y1_train, 
              epochs = 40, 
              batch_size = 512, 
              validation_data = (X1_train, Y1_train),
              verbose = 1)
     

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Flatten
     

regressor = Sequential()
     

print(X_train.shape[1])
     
1

regressor.add(LSTM(units = 10, return_sequences = True, activation = 'relu', input_shape = (X_train.shape[1], 21)))
regressor.add(Dropout(0.5))

     
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.

regressor.add(LSTM(units = 10, return_sequences = True, activation = 'relu'))
regressor.add(Dropout(0.5))
     

regressor.add(LSTM(units = 10, return_sequences = False, activation = 'relu'))
regressor.add(Dropout(0.5))
     

regressor.add(Dense(units=1))
     

my_adam_optimizer = keras.optimizers.Adam(lr=0.01, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
     

regressor.compile(optimizer= 'adam', 
                  loss='mean_squared_error', 
                  metrics=['accuracy'])
     

history = regressor.fit(X_train, 
              y_train, 
              epochs = 40, 
              batch_size = 512, 
              validation_data = (X_val, y_val),
              verbose = 1)
     
Train on 30594 samples, validate on 3723 samples
Epoch 1/40
30594/30594 [==============================] - 1s 36us/step - loss: 0.0413 - acc: 0.0354 - val_loss: 0.0612 - val_acc: 0.1362
Epoch 2/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0406 - acc: 0.0361 - val_loss: 0.0613 - val_acc: 0.1362
Epoch 3/40
30594/30594 [==============================] - 1s 41us/step - loss: 0.0407 - acc: 0.0360 - val_loss: 0.0598 - val_acc: 0.1362
Epoch 4/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0408 - acc: 0.0359 - val_loss: 0.0608 - val_acc: 0.1362
Epoch 5/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0408 - acc: 0.0356 - val_loss: 0.0598 - val_acc: 0.1362
Epoch 6/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0403 - acc: 0.0361 - val_loss: 0.0586 - val_acc: 0.1362
Epoch 7/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0405 - acc: 0.0359 - val_loss: 0.0609 - val_acc: 0.1362
Epoch 8/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0406 - acc: 0.0362 - val_loss: 0.0602 - val_acc: 0.1362
Epoch 9/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0403 - acc: 0.0360 - val_loss: 0.0589 - val_acc: 0.1362
Epoch 10/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0400 - acc: 0.0355 - val_loss: 0.0582 - val_acc: 0.1362
Epoch 11/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0402 - acc: 0.0360 - val_loss: 0.0597 - val_acc: 0.1362
Epoch 12/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0401 - acc: 0.0361 - val_loss: 0.0589 - val_acc: 0.1362
Epoch 13/40
30594/30594 [==============================] - 1s 40us/step - loss: 0.0399 - acc: 0.0357 - val_loss: 0.0605 - val_acc: 0.1362
Epoch 14/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0400 - acc: 0.0363 - val_loss: 0.0592 - val_acc: 0.1362
Epoch 15/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0395 - acc: 0.0359 - val_loss: 0.0608 - val_acc: 0.1362
Epoch 16/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0399 - acc: 0.0357 - val_loss: 0.0605 - val_acc: 0.1362
Epoch 17/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0400 - acc: 0.0359 - val_loss: 0.0609 - val_acc: 0.1362
Epoch 18/40
30594/30594 [==============================] - 1s 37us/step - loss: 0.0397 - acc: 0.0359 - val_loss: 0.0598 - val_acc: 0.1362
Epoch 19/40
30594/30594 [==============================] - 1s 37us/step - loss: 0.0398 - acc: 0.0361 - val_loss: 0.0592 - val_acc: 0.1362
Epoch 20/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0398 - acc: 0.0360 - val_loss: 0.0619 - val_acc: 0.1362
Epoch 21/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0394 - acc: 0.0360 - val_loss: 0.0602 - val_acc: 0.1362
Epoch 22/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0394 - acc: 0.0362 - val_loss: 0.0590 - val_acc: 0.1362
Epoch 23/40
30594/30594 [==============================] - 1s 40us/step - loss: 0.0395 - acc: 0.0360 - val_loss: 0.0600 - val_acc: 0.1362
Epoch 24/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0398 - acc: 0.0361 - val_loss: 0.0611 - val_acc: 0.1362
Epoch 25/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0395 - acc: 0.0361 - val_loss: 0.0597 - val_acc: 0.1362
Epoch 26/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0390 - acc: 0.0363 - val_loss: 0.0606 - val_acc: 0.1362
Epoch 27/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0399 - acc: 0.0362 - val_loss: 0.0605 - val_acc: 0.1362
Epoch 28/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0397 - acc: 0.0356 - val_loss: 0.0605 - val_acc: 0.1362
Epoch 29/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0393 - acc: 0.0362 - val_loss: 0.0605 - val_acc: 0.1362
Epoch 30/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0393 - acc: 0.0359 - val_loss: 0.0596 - val_acc: 0.1362
Epoch 31/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0393 - acc: 0.0361 - val_loss: 0.0598 - val_acc: 0.1362
Epoch 32/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0395 - acc: 0.0360 - val_loss: 0.0604 - val_acc: 0.1362
Epoch 33/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0396 - acc: 0.0359 - val_loss: 0.0603 - val_acc: 0.1362
Epoch 34/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0396 - acc: 0.0364 - val_loss: 0.0595 - val_acc: 0.1362
Epoch 35/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0392 - acc: 0.0362 - val_loss: 0.0617 - val_acc: 0.1362
Epoch 36/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0392 - acc: 0.0360 - val_loss: 0.0606 - val_acc: 0.1362
Epoch 37/40
30594/30594 [==============================] - 1s 38us/step - loss: 0.0394 - acc: 0.0362 - val_loss: 0.0613 - val_acc: 0.1362
Epoch 38/40
30594/30594 [==============================] - 1s 40us/step - loss: 0.0394 - acc: 0.0363 - val_loss: 0.0606 - val_acc: 0.1362
Epoch 39/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0393 - acc: 0.0357 - val_loss: 0.0604 - val_acc: 0.1362
Epoch 40/40
30594/30594 [==============================] - 1s 39us/step - loss: 0.0391 - acc: 0.0359 - val_loss: 0.0607 - val_acc: 0.1362

history = regressor.fit(X_train, 
              y_train, 
              epochs = 100, 
              batch_size = 512, 
              validation_data = (X_val, y_val),
              verbose = 1)
     
Train on 30594 samples, validate on 3723 samples
Epoch 1/100
30594/30594 [==============================] - 1s 38us/step - loss: 0.0394 - acc: 0.0362 - val_loss: 0.0607 - val_acc: 0.1362
Epoch 2/100
30594/30594 [==============================] - 1s 40us/step - loss: 0.0388 - acc: 0.0364 - val_loss: 0.0609 - val_acc: 0.1362
Epoch 3/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0393 - acc: 0.0357 - val_loss: 0.0598 - val_acc: 0.1362
Epoch 4/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0391 - acc: 0.0363 - val_loss: 0.0614 - val_acc: 0.1362
Epoch 5/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0386 - acc: 0.0364 - val_loss: 0.0596 - val_acc: 0.1362
Epoch 6/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0385 - acc: 0.0362 - val_loss: 0.0603 - val_acc: 0.1362
Epoch 7/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0389 - acc: 0.0360 - val_loss: 0.0609 - val_acc: 0.1362
Epoch 8/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0390 - acc: 0.0361 - val_loss: 0.0603 - val_acc: 0.1362
Epoch 9/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0388 - acc: 0.0360 - val_loss: 0.0625 - val_acc: 0.1362
Epoch 10/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0394 - acc: 0.0357 - val_loss: 0.0604 - val_acc: 0.1362
Epoch 11/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0393 - acc: 0.0362 - val_loss: 0.0593 - val_acc: 0.1362
Epoch 12/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0389 - acc: 0.0367 - val_loss: 0.0590 - val_acc: 0.1362
Epoch 13/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0390 - acc: 0.0359 - val_loss: 0.0597 - val_acc: 0.1362
Epoch 14/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0387 - acc: 0.0364 - val_loss: 0.0590 - val_acc: 0.1362
Epoch 15/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0387 - acc: 0.0364 - val_loss: 0.0581 - val_acc: 0.1362
Epoch 16/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0386 - acc: 0.0360 - val_loss: 0.0581 - val_acc: 0.1362
Epoch 17/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0390 - acc: 0.0364 - val_loss: 0.0587 - val_acc: 0.1362
Epoch 18/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0385 - acc: 0.0362 - val_loss: 0.0611 - val_acc: 0.1362
Epoch 19/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0390 - acc: 0.0365 - val_loss: 0.0582 - val_acc: 0.1362
Epoch 20/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0388 - acc: 0.0359 - val_loss: 0.0583 - val_acc: 0.1362
Epoch 21/100
30594/30594 [==============================] - 1s 38us/step - loss: 0.0388 - acc: 0.0360 - val_loss: 0.0581 - val_acc: 0.1362
Epoch 22/100
30594/30594 [==============================] - 1s 38us/step - loss: 0.0378 - acc: 0.0363 - val_loss: 0.0580 - val_acc: 0.1362
Epoch 23/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0384 - acc: 0.0361 - val_loss: 0.0579 - val_acc: 0.1362
Epoch 24/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0391 - acc: 0.0363 - val_loss: 0.0580 - val_acc: 0.1362
Epoch 25/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0390 - acc: 0.0361 - val_loss: 0.0601 - val_acc: 0.1362
Epoch 26/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0390 - acc: 0.0361 - val_loss: 0.0573 - val_acc: 0.1362
Epoch 27/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0384 - acc: 0.0365 - val_loss: 0.0578 - val_acc: 0.1362
Epoch 28/100
30594/30594 [==============================] - 1s 38us/step - loss: 0.0386 - acc: 0.0361 - val_loss: 0.0591 - val_acc: 0.1362
Epoch 29/100
30594/30594 [==============================] - 1s 36us/step - loss: 0.0391 - acc: 0.0360 - val_loss: 0.0581 - val_acc: 0.1362
Epoch 30/100
30594/30594 [==============================] - 1s 37us/step - loss: 0.0386 - acc: 0.0359 - val_loss: 0.0580 - val_acc: 0.1362
Epoch 31/100
30594/30594 [==============================] - 1s 39us/step - loss: 0.0382 - acc: 0.0362 - val_loss: 0.0574 - val_acc: 0.1362
Epoch 32/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0388 - acc: 0.0363 - val_loss: 0.0562 - val_acc: 0.1362
Epoch 33/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0386 - acc: 0.0363 - val_loss: 0.0573 - val_acc: 0.1362
Epoch 34/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0384 - acc: 0.0363 - val_loss: 0.0594 - val_acc: 0.1362
Epoch 35/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0359 - val_loss: 0.0593 - val_acc: 0.1362
Epoch 36/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0394 - acc: 0.0361 - val_loss: 0.0584 - val_acc: 0.1362
Epoch 37/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0390 - acc: 0.0359 - val_loss: 0.0583 - val_acc: 0.1362
Epoch 38/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0387 - acc: 0.0362 - val_loss: 0.0577 - val_acc: 0.1362
Epoch 39/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0384 - acc: 0.0365 - val_loss: 0.0591 - val_acc: 0.1362
Epoch 40/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0389 - acc: 0.0361 - val_loss: 0.0582 - val_acc: 0.1362
Epoch 41/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0365 - val_loss: 0.0579 - val_acc: 0.1362
Epoch 42/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0388 - acc: 0.0362 - val_loss: 0.0569 - val_acc: 0.1362
Epoch 43/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0362 - val_loss: 0.0564 - val_acc: 0.1362
Epoch 44/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0362 - val_loss: 0.0580 - val_acc: 0.1362
Epoch 45/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0389 - acc: 0.0362 - val_loss: 0.0551 - val_acc: 0.1362
Epoch 46/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0384 - acc: 0.0365 - val_loss: 0.0571 - val_acc: 0.1362
Epoch 47/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0364 - val_loss: 0.0575 - val_acc: 0.1362
Epoch 48/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0361 - val_loss: 0.0590 - val_acc: 0.1362
Epoch 49/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0385 - acc: 0.0360 - val_loss: 0.0586 - val_acc: 0.1362
Epoch 50/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0385 - acc: 0.0357 - val_loss: 0.0574 - val_acc: 0.1362
Epoch 51/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0385 - acc: 0.0361 - val_loss: 0.0576 - val_acc: 0.1362
Epoch 52/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0383 - acc: 0.0366 - val_loss: 0.0567 - val_acc: 0.1362
Epoch 53/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0386 - acc: 0.0361 - val_loss: 0.0567 - val_acc: 0.1362
Epoch 54/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0383 - acc: 0.0363 - val_loss: 0.0578 - val_acc: 0.1362
Epoch 55/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0387 - acc: 0.0364 - val_loss: 0.0560 - val_acc: 0.1362
Epoch 56/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0387 - acc: 0.0361 - val_loss: 0.0577 - val_acc: 0.1362
Epoch 57/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0388 - acc: 0.0366 - val_loss: 0.0570 - val_acc: 0.1362
Epoch 58/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0381 - acc: 0.0363 - val_loss: 0.0558 - val_acc: 0.1362
Epoch 59/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0389 - acc: 0.0357 - val_loss: 0.0575 - val_acc: 0.1362
Epoch 60/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0387 - acc: 0.0360 - val_loss: 0.0549 - val_acc: 0.1362
Epoch 61/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0364 - val_loss: 0.0569 - val_acc: 0.1362
Epoch 62/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0358 - val_loss: 0.0568 - val_acc: 0.1362
Epoch 63/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0383 - acc: 0.0363 - val_loss: 0.0559 - val_acc: 0.1362
Epoch 64/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0389 - acc: 0.0361 - val_loss: 0.0550 - val_acc: 0.1362
Epoch 65/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0361 - val_loss: 0.0560 - val_acc: 0.1362
Epoch 66/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0384 - acc: 0.0364 - val_loss: 0.0577 - val_acc: 0.1362
Epoch 67/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0384 - acc: 0.0361 - val_loss: 0.0576 - val_acc: 0.1362
Epoch 68/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0388 - acc: 0.0360 - val_loss: 0.0550 - val_acc: 0.1362
Epoch 69/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0359 - val_loss: 0.0560 - val_acc: 0.1362
Epoch 70/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0384 - acc: 0.0363 - val_loss: 0.0562 - val_acc: 0.1362
Epoch 71/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0383 - acc: 0.0361 - val_loss: 0.0564 - val_acc: 0.1362
Epoch 72/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0381 - acc: 0.0364 - val_loss: 0.0552 - val_acc: 0.1362
Epoch 73/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0386 - acc: 0.0360 - val_loss: 0.0566 - val_acc: 0.1362
Epoch 74/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0362 - val_loss: 0.0573 - val_acc: 0.1362
Epoch 75/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0360 - val_loss: 0.0573 - val_acc: 0.1362
Epoch 76/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0388 - acc: 0.0359 - val_loss: 0.0562 - val_acc: 0.1362
Epoch 77/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0364 - val_loss: 0.0571 - val_acc: 0.1362
Epoch 78/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0388 - acc: 0.0361 - val_loss: 0.0561 - val_acc: 0.1362
Epoch 79/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0385 - acc: 0.0365 - val_loss: 0.0557 - val_acc: 0.1362
Epoch 80/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0385 - acc: 0.0359 - val_loss: 0.0579 - val_acc: 0.1362
Epoch 81/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0384 - acc: 0.0362 - val_loss: 0.0559 - val_acc: 0.1362
Epoch 82/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0383 - acc: 0.0363 - val_loss: 0.0572 - val_acc: 0.1362
Epoch 83/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0361 - val_loss: 0.0571 - val_acc: 0.1362
Epoch 84/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0387 - acc: 0.0362 - val_loss: 0.0568 - val_acc: 0.1362
Epoch 85/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0389 - acc: 0.0364 - val_loss: 0.0557 - val_acc: 0.1362
Epoch 86/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0363 - val_loss: 0.0565 - val_acc: 0.1362
Epoch 87/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0360 - val_loss: 0.0569 - val_acc: 0.1362
Epoch 88/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0388 - acc: 0.0358 - val_loss: 0.0573 - val_acc: 0.1362
Epoch 89/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0385 - acc: 0.0362 - val_loss: 0.0545 - val_acc: 0.1362
Epoch 90/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0387 - acc: 0.0358 - val_loss: 0.0568 - val_acc: 0.1362
Epoch 91/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0381 - acc: 0.0366 - val_loss: 0.0559 - val_acc: 0.1362
Epoch 92/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0389 - acc: 0.0361 - val_loss: 0.0583 - val_acc: 0.1362
Epoch 93/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0383 - acc: 0.0361 - val_loss: 0.0568 - val_acc: 0.1362
Epoch 94/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0385 - acc: 0.0361 - val_loss: 0.0564 - val_acc: 0.1362
Epoch 95/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0387 - acc: 0.0359 - val_loss: 0.0565 - val_acc: 0.1362
Epoch 96/100
30594/30594 [==============================] - 1s 43us/step - loss: 0.0385 - acc: 0.0361 - val_loss: 0.0578 - val_acc: 0.1362
Epoch 97/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0392 - acc: 0.0361 - val_loss: 0.0568 - val_acc: 0.1362
Epoch 98/100
30594/30594 [==============================] - 1s 42us/step - loss: 0.0386 - acc: 0.0361 - val_loss: 0.0553 - val_acc: 0.1362
Epoch 99/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0382 - acc: 0.0359 - val_loss: 0.0549 - val_acc: 0.1362
Epoch 100/100
30594/30594 [==============================] - 1s 41us/step - loss: 0.0382 - acc: 0.0366 - val_loss: 0.0559 - val_acc: 0.1362

regressor = Sequential()
regressor.add(LSTM(units = 100, return_sequences = True, activation = 'relu', input_shape = (X_train.shape[1], 21)))
regressor.add(Dropout(0.5))
regressor.add(LSTM(units = 100, return_sequences = True, activation = 'relu'))
regressor.add(Dropout(0.5))
regressor.add(LSTM(units = 100, return_sequences = False, activation = 'relu'))
regressor.add(Dropout(0.5))
regressor.add(Dense(units=1))
regressor.compile(optimizer= my_adam_optimizer, 
                  loss='mean_squared_error', 
                  metrics=['accuracy'])
history = regressor.fit(X_train, 
              y_train, 
              epochs = 100, 
              batch_size = 512, 
              validation_data = (X_val, y_val),
              verbose = 1)

     
Train on 34616 samples, validate on 859 samples
Epoch 1/100
34616/34616 [==============================] - 10s 275us/step - loss: 0.1874 - acc: 0.0281 - val_loss: 0.0892 - val_acc: 0.3166
Epoch 2/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0777 - acc: 0.0355 - val_loss: 0.0590 - val_acc: 0.3527
Epoch 3/100
34616/34616 [==============================] - 2s 46us/step - loss: 0.0684 - acc: 0.0377 - val_loss: 0.0590 - val_acc: 0.3527
Epoch 4/100
34616/34616 [==============================] - 2s 45us/step - loss: 0.0677 - acc: 0.0376 - val_loss: 0.0589 - val_acc: 0.3527
Epoch 5/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0674 - acc: 0.0384 - val_loss: 0.0589 - val_acc: 0.3527
Epoch 6/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0678 - acc: 0.0380 - val_loss: 0.0595 - val_acc: 0.3527
Epoch 7/100
34616/34616 [==============================] - 2s 43us/step - loss: 0.0671 - acc: 0.0379 - val_loss: 0.0604 - val_acc: 0.3527
Epoch 8/100
34616/34616 [==============================] - 2s 43us/step - loss: 0.0676 - acc: 0.0382 - val_loss: 0.0579 - val_acc: 0.3527
Epoch 9/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0678 - acc: 0.0374 - val_loss: 0.0587 - val_acc: 0.3527
Epoch 10/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0674 - acc: 0.0378 - val_loss: 0.0586 - val_acc: 0.3527
Epoch 11/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0672 - acc: 0.0378 - val_loss: 0.0577 - val_acc: 0.3527
Epoch 12/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0673 - acc: 0.0377 - val_loss: 0.0589 - val_acc: 0.3527
Epoch 13/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0375 - val_loss: 0.0603 - val_acc: 0.3527
Epoch 14/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0674 - acc: 0.0379 - val_loss: 0.0601 - val_acc: 0.3527
Epoch 15/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0673 - acc: 0.0375 - val_loss: 0.0605 - val_acc: 0.3527
Epoch 16/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0677 - acc: 0.0369 - val_loss: 0.0595 - val_acc: 0.3527
Epoch 17/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0375 - val_loss: 0.0608 - val_acc: 0.3527
Epoch 18/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0679 - acc: 0.0374 - val_loss: 0.0588 - val_acc: 0.3527
Epoch 19/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0672 - acc: 0.0378 - val_loss: 0.0592 - val_acc: 0.3527
Epoch 20/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0380 - val_loss: 0.0580 - val_acc: 0.3527
Epoch 21/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0677 - acc: 0.0380 - val_loss: 0.0596 - val_acc: 0.3527
Epoch 22/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0677 - acc: 0.0377 - val_loss: 0.0601 - val_acc: 0.3527
Epoch 23/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0676 - acc: 0.0377 - val_loss: 0.0586 - val_acc: 0.3527
Epoch 24/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0674 - acc: 0.0380 - val_loss: 0.0603 - val_acc: 0.3527
Epoch 25/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0674 - acc: 0.0378 - val_loss: 0.0603 - val_acc: 0.3527
Epoch 26/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0680 - acc: 0.0369 - val_loss: 0.0610 - val_acc: 0.3527
Epoch 27/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0677 - acc: 0.0378 - val_loss: 0.0574 - val_acc: 0.3527
Epoch 28/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0668 - acc: 0.0372 - val_loss: 0.0588 - val_acc: 0.3527
Epoch 29/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0677 - acc: 0.0374 - val_loss: 0.0581 - val_acc: 0.3527
Epoch 30/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0677 - acc: 0.0374 - val_loss: 0.0596 - val_acc: 0.3527
Epoch 31/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0675 - acc: 0.0380 - val_loss: 0.0594 - val_acc: 0.3527
Epoch 32/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0680 - acc: 0.0370 - val_loss: 0.0598 - val_acc: 0.3527
Epoch 33/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0674 - acc: 0.0382 - val_loss: 0.0600 - val_acc: 0.3527
Epoch 34/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0674 - acc: 0.0377 - val_loss: 0.0598 - val_acc: 0.3527
Epoch 35/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0677 - acc: 0.0380 - val_loss: 0.0579 - val_acc: 0.3527
Epoch 36/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0675 - acc: 0.0374 - val_loss: 0.0620 - val_acc: 0.3527
Epoch 37/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0672 - acc: 0.0380 - val_loss: 0.0595 - val_acc: 0.3527
Epoch 38/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0674 - acc: 0.0378 - val_loss: 0.0596 - val_acc: 0.3527
Epoch 39/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0675 - acc: 0.0376 - val_loss: 0.0610 - val_acc: 0.3527
Epoch 40/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0380 - val_loss: 0.0605 - val_acc: 0.3527
Epoch 41/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0676 - acc: 0.0381 - val_loss: 0.0597 - val_acc: 0.3527
Epoch 42/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0678 - acc: 0.0378 - val_loss: 0.0613 - val_acc: 0.3527
Epoch 43/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0677 - acc: 0.0372 - val_loss: 0.0596 - val_acc: 0.3527
Epoch 44/100
34616/34616 [==============================] - 2s 45us/step - loss: 0.0664 - acc: 0.0390 - val_loss: 0.0591 - val_acc: 0.3527
Epoch 45/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0673 - acc: 0.0375 - val_loss: 0.0611 - val_acc: 0.3527
Epoch 46/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0677 - acc: 0.0374 - val_loss: 0.0581 - val_acc: 0.3527
Epoch 47/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0672 - acc: 0.0383 - val_loss: 0.0623 - val_acc: 0.3527
Epoch 48/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0670 - acc: 0.0377 - val_loss: 0.0593 - val_acc: 0.3527
Epoch 49/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0672 - acc: 0.0375 - val_loss: 0.0585 - val_acc: 0.3527
Epoch 50/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0675 - acc: 0.0376 - val_loss: 0.0607 - val_acc: 0.3527
Epoch 51/100
34616/34616 [==============================] - 2s 43us/step - loss: 0.0676 - acc: 0.0374 - val_loss: 0.0601 - val_acc: 0.3527
Epoch 52/100
34616/34616 [==============================] - 2s 43us/step - loss: 0.0677 - acc: 0.0377 - val_loss: 0.0618 - val_acc: 0.3527
Epoch 53/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0678 - acc: 0.0369 - val_loss: 0.0644 - val_acc: 0.3527
Epoch 54/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0670 - acc: 0.0379 - val_loss: 0.0612 - val_acc: 0.3527
Epoch 55/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0671 - acc: 0.0383 - val_loss: 0.0609 - val_acc: 0.3527
Epoch 56/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0670 - acc: 0.0378 - val_loss: 0.0594 - val_acc: 0.3527
Epoch 57/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0681 - acc: 0.0378 - val_loss: 0.0618 - val_acc: 0.3527
Epoch 58/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0673 - acc: 0.0380 - val_loss: 0.0610 - val_acc: 0.3527
Epoch 59/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0673 - acc: 0.0375 - val_loss: 0.0582 - val_acc: 0.3527
Epoch 60/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0672 - acc: 0.0380 - val_loss: 0.0575 - val_acc: 0.3527
Epoch 61/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0678 - acc: 0.0376 - val_loss: 0.0588 - val_acc: 0.3527
Epoch 62/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0375 - val_loss: 0.0620 - val_acc: 0.3527
Epoch 63/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0671 - acc: 0.0378 - val_loss: 0.0609 - val_acc: 0.3527
Epoch 64/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0675 - acc: 0.0380 - val_loss: 0.0583 - val_acc: 0.3527
Epoch 65/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0677 - acc: 0.0377 - val_loss: 0.0590 - val_acc: 0.3527
Epoch 66/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0669 - acc: 0.0380 - val_loss: 0.0603 - val_acc: 0.3527
Epoch 67/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0679 - acc: 0.0380 - val_loss: 0.0625 - val_acc: 0.3527
Epoch 68/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0677 - acc: 0.0374 - val_loss: 0.0615 - val_acc: 0.3527
Epoch 69/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0667 - acc: 0.0377 - val_loss: 0.0595 - val_acc: 0.3527
Epoch 70/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0668 - acc: 0.0380 - val_loss: 0.0605 - val_acc: 0.3527
Epoch 71/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0673 - acc: 0.0374 - val_loss: 0.0605 - val_acc: 0.3527
Epoch 72/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0678 - acc: 0.0369 - val_loss: 0.0600 - val_acc: 0.3527
Epoch 73/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0672 - acc: 0.0376 - val_loss: 0.0584 - val_acc: 0.3527
Epoch 74/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0678 - acc: 0.0373 - val_loss: 0.0617 - val_acc: 0.3527
Epoch 75/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0676 - acc: 0.0372 - val_loss: 0.0584 - val_acc: 0.3527
Epoch 76/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0384 - val_loss: 0.0603 - val_acc: 0.3527
Epoch 77/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0674 - acc: 0.0378 - val_loss: 0.0619 - val_acc: 0.3527
Epoch 78/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0671 - acc: 0.0378 - val_loss: 0.0584 - val_acc: 0.3527
Epoch 79/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0668 - acc: 0.0378 - val_loss: 0.0606 - val_acc: 0.3527
Epoch 80/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0674 - acc: 0.0376 - val_loss: 0.0604 - val_acc: 0.3527
Epoch 81/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0677 - acc: 0.0376 - val_loss: 0.0606 - val_acc: 0.3527
Epoch 82/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0675 - acc: 0.0389 - val_loss: 0.0654 - val_acc: 0.3527
Epoch 83/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0676 - acc: 0.0372 - val_loss: 0.0607 - val_acc: 0.3527
Epoch 84/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0675 - acc: 0.0380 - val_loss: 0.0594 - val_acc: 0.3527
Epoch 85/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0680 - acc: 0.0374 - val_loss: 0.0619 - val_acc: 0.3527
Epoch 86/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0682 - acc: 0.0367 - val_loss: 0.0553 - val_acc: 0.3527
Epoch 87/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0676 - acc: 0.0379 - val_loss: 0.0632 - val_acc: 0.3527
Epoch 88/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0678 - acc: 0.0377 - val_loss: 0.0624 - val_acc: 0.3527
Epoch 89/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0677 - acc: 0.0376 - val_loss: 0.0616 - val_acc: 0.3527
Epoch 90/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0679 - acc: 0.0375 - val_loss: 0.0633 - val_acc: 0.3527
Epoch 91/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0668 - acc: 0.0382 - val_loss: 0.0593 - val_acc: 0.3527
Epoch 92/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0673 - acc: 0.0380 - val_loss: 0.0636 - val_acc: 0.3527
Epoch 93/100
34616/34616 [==============================] - 1s 42us/step - loss: 0.0671 - acc: 0.0380 - val_loss: 0.0615 - val_acc: 0.3527
Epoch 94/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0674 - acc: 0.0374 - val_loss: 0.0630 - val_acc: 0.3527
Epoch 95/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0674 - acc: 0.0380 - val_loss: 0.0627 - val_acc: 0.3527
Epoch 96/100
34616/34616 [==============================] - 2s 44us/step - loss: 0.0670 - acc: 0.0374 - val_loss: 0.0625 - val_acc: 0.3527
Epoch 97/100
34616/34616 [==============================] - 1s 43us/step - loss: 0.0677 - acc: 0.0376 - val_loss: 0.0601 - val_acc: 0.3527
Epoch 98/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0674 - acc: 0.0376 - val_loss: 0.0590 - val_acc: 0.3527
Epoch 99/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0675 - acc: 0.0375 - val_loss: 0.0608 - val_acc: 0.3527
Epoch 100/100
34616/34616 [==============================] - 1s 41us/step - loss: 0.0676 - acc: 0.0379 - val_loss: 0.0594 - val_acc: 0.3527

regressor = Sequential()
regressor.add(LSTM(units = 100, return_sequences = True, activation = 'relu', input_shape = (X_train.shape[1], 21)))
regressor.add(Dropout(0.5))
regressor.add(LSTM(units = 100, return_sequences = True, activation = 'relu'))
regressor.add(Dropout(0.5))
regressor.add(LSTM(units = 100, return_sequences = False, activation = 'relu'))
regressor.add(Dropout(0.5))
regressor.add(Dense(units=1))
regressor.compile(optimizer= 'adam', 
                  loss='mean_squared_error', 
                  metrics=['accuracy'])
history = regressor.fit(X_train, 
              y_train, 
              epochs = 100, 
              batch_size = 512, 
              validation_data = (X_val, y_val),
              verbose = 1)
     
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-112-fd54d690074a> in <module>()
     15               batch_size = 512,
     16               validation_data = (X_val, y_val),
---> 17               verbose = 1)

/usr/local/lib/python3.6/dist-packages/keras/engine/training.py in fit(self, x, y, batch_size, epochs, verbose, callbacks, validation_split, validation_data, shuffle, class_weight, sample_weight, initial_epoch, steps_per_epoch, validation_steps, **kwargs)
    950             sample_weight=sample_weight,
    951             class_weight=class_weight,
--> 952             batch_size=batch_size)
    953         # Prepare validation data.
    954         do_validation = False

/usr/local/lib/python3.6/dist-packages/keras/engine/training.py in _standardize_user_data(self, x, y, sample_weight, class_weight, check_array_lengths, batch_size)
    749             feed_input_shapes,
    750             check_batch_axis=False,  # Don't enforce the batch size.
--> 751             exception_prefix='input')
    752 
    753         if y is not None:

/usr/local/lib/python3.6/dist-packages/keras/engine/training_utils.py in standardize_input_data(data, names, shapes, check_batch_axis, exception_prefix)
    136                             ': expected ' + names[i] + ' to have shape ' +
    137                             str(shape) + ' but got array with shape ' +
--> 138                             str(data_shape))
    139     return data
    140 

ValueError: Error when checking input: expected lstm_32_input to have shape (1, 21) but got array with shape (1, 17)

df1 = regressor.predict(X_test)
     

len(X_train)/len(X_val)
     
2.9205986518907805

test_set['Predicted Values'] = df1
     

test_set1 = pd.DataFrame(test_set_scaled)
     

test_set.columns
     
Index(['Ship Mode', 'Segment', 'City', 'State', 'Country', 'Postal Code',
       'Market', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Quantity', 'Discount', 'Profit', 'Shipping Cost',
       'Order Priority', 'Year', 'Month', 'Day', 'WeekOfYear', 'Sales',
       'Predicted Values'],
      dtype='object')

test_set.drop('Sales')
     

test_set2.columns
     
Index(['Ship Mode', 'Segment', 'City', 'State', 'Country', 'Postal Code',
       'Market', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit',
       'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day', 'WeekOfYear',
       'Predicted Values', 'Actual Sales'],
      dtype='object')

col2 = ['Ship Mode' , 'Segment' , 'City' , 'State'  , 'Country' ,  'Postal Code',
       'Market', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit',
       'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day', 'WeekOfYear']
     

test_set2 = pd.DataFrame(test_set_scaled , columns = col2)
     

test_set2['Predicted Values'] = df1 
     

test_set2
     
Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	Product ID	Category	...	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear	Predicted Values
0	1.000000	0.5	0.762115	0.175824	0.952055	0.964314	1.000000	1.000000	0.371756	0.5	...	0.307692	0.2500	0.544175	1.000000	0.666667	0.0	0.818182	0.433333	0.803922	0.659934
1	0.666667	0.5	0.672357	0.398352	0.301370	0.547398	0.666667	0.250000	0.232093	0.5	...	0.230769	0.1250	0.381340	0.923901	0.000000	0.0	0.545455	1.000000	0.588235	0.518060
2	0.666667	0.5	0.372522	0.461538	0.952055	0.416366	1.000000	0.833333	0.813685	1.0	...	0.615385	0.0000	0.412640	0.899744	0.000000	0.0	0.181818	0.333333	0.196078	0.369788
3	1.000000	0.5	0.712830	0.918498	0.431507	0.547398	0.666667	0.833333	0.267470	0.5	...	1.000000	0.0000	0.740444	0.897001	0.666667	0.0	0.636364	0.266667	0.607843	0.454222
4	0.000000	0.5	0.898128	0.750916	0.041096	0.547398	0.000000	0.750000	0.839926	1.0	...	0.615385	0.1250	0.366326	0.883874	0.000000	0.0	0.000000	1.000000	0.078431	0.369788
5	0.666667	0.0	0.917676	0.476190	0.876712	0.547398	0.166667	0.000000	0.529012	0.5	...	0.384615	0.0000	0.441125	0.879783	0.333333	0.0	0.363636	0.366667	0.372549	0.369788
6	0.000000	0.0	0.431993	0.210623	0.554795	0.547398	0.833333	0.583333	0.981242	1.0	...	0.230769	0.0000	0.405826	0.840125	0.000000	0.0	0.545455	1.000000	0.588235	0.505364
7	0.000000	0.0	0.838106	0.793956	0.260274	0.547398	0.833333	0.250000	0.199922	0.0	...	0.538462	0.2500	0.413494	0.839457	0.000000	0.0	0.363636	0.266667	0.352941	0.369788
8	0.333333	0.5	0.145374	0.657509	0.952055	0.260373	1.000000	0.833333	0.917776	1.0	...	0.230769	0.6250	0.000000	0.777718	0.333333	0.0	0.363636	0.333333	0.352941	0.416113
9	1.000000	1.0	0.332048	0.363553	0.390411	0.547398	0.000000	0.333333	0.977257	1.0	...	0.461538	0.0000	0.423534	0.759128	0.333333	0.0	0.909091	0.333333	0.882353	0.737965
10	0.666667	0.5	0.882709	0.462454	0.390411	0.547398	0.000000	0.333333	0.046457	0.0	...	0.923077	0.0000	0.562219	0.758736	1.000000	0.0	0.727273	0.833333	0.745098	0.642918
11	0.000000	0.0	0.819383	0.819597	0.178082	0.547398	0.000000	0.666667	0.055205	0.0	...	0.384615	0.0000	0.374085	0.743062	0.333333	0.0	0.636364	0.900000	0.666667	0.596696
12	0.666667	0.0	0.678139	0.709707	0.958904	0.547398	0.833333	0.833333	0.058509	0.0	...	0.769231	0.0000	0.445845	0.731283	0.333333	0.0	1.000000	0.566667	0.980392	0.775520
13	0.000000	0.0	0.091685	0.582418	0.404110	0.547398	0.500000	0.416667	0.830693	1.0	...	0.538462	0.0000	0.413546	0.727181	0.000000	0.0	0.727273	0.566667	0.725490	0.643159
14	0.333333	0.5	0.390419	0.175824	0.952055	0.931716	1.000000	1.000000	0.844786	1.0	...	0.307692	0.2500	0.443181	0.726120	0.333333	0.0	0.545455	0.800000	0.568627	0.455210
15	0.000000	0.0	0.323513	0.967033	0.041096	0.547398	0.000000	0.750000	0.248323	0.5	...	0.615385	0.1250	0.473889	0.708014	0.333333	0.0	0.363636	0.233333	0.352941	0.369788
16	0.666667	0.0	0.863711	0.304029	0.952055	0.312559	1.000000	0.833333	0.949947	1.0	...	0.923077	0.2500	0.394659	0.702367	1.000000	0.0	0.636364	0.766667	0.647059	0.568677
17	0.666667	0.0	0.250275	0.253663	0.068493	0.547398	0.000000	0.333333	0.012829	0.0	...	0.461538	0.0000	0.418742	0.702137	0.333333	0.0	0.909091	0.066667	0.862745	0.711251
18	0.666667	0.5	0.609031	0.532051	0.321918	0.547398	0.666667	0.250000	0.956556	1.0	...	0.461538	0.0000	0.393287	0.696559	1.000000	0.0	0.909091	0.233333	0.862745	0.737131
19	1.000000	0.0	0.971641	0.423993	0.178082	0.547398	0.000000	0.666667	0.050345	0.0	...	0.769231	0.0000	0.425793	0.686301	0.333333	0.0	0.000000	0.566667	0.039216	0.369788
20	0.000000	0.0	0.811674	0.042125	0.815068	0.547398	0.666667	0.833333	0.047526	0.0	...	0.307692	0.0000	0.463083	0.684469	0.333333	0.0	0.545455	0.366667	0.529412	0.454037
21	0.000000	0.5	0.729075	0.932234	0.390411	0.547398	0.000000	0.333333	0.190786	0.0	...	0.230769	0.0000	0.425466	0.683155	0.000000	0.0	1.000000	0.500000	0.980392	0.759301
22	0.333333	1.0	0.355176	0.272894	0.554795	0.547398	0.833333	0.583333	0.981534	1.0	...	0.230769	0.0000	0.374932	0.683109	0.000000	0.0	0.909091	0.633333	0.901961	0.750046
23	0.000000	0.5	0.664648	0.869963	0.397260	0.547398	0.000000	0.916667	0.188259	0.0	...	0.461538	0.5875	0.320757	0.676010	0.333333	0.0	0.636364	0.833333	0.666667	0.606364
24	0.666667	0.0	0.572412	0.945971	0.041096	0.547398	0.000000	0.750000	0.964914	1.0	...	0.307692	0.1250	0.444972	0.670604	0.000000	0.0	0.363636	0.500000	0.372549	0.369788
25	1.000000	0.0	0.509912	0.654762	0.301370	0.547398	0.666667	0.250000	0.077850	0.0	...	1.000000	0.1250	0.369654	0.660313	0.333333	0.0	0.909091	0.600000	0.901961	0.756294
26	0.666667	0.5	0.572137	0.586996	0.582192	0.547398	0.166667	0.000000	0.829721	1.0	...	1.000000	0.0000	0.609592	0.655126	1.000000	0.0	0.818182	0.900000	0.843137	0.703540
27	0.666667	0.0	0.413271	0.591575	0.952055	0.485943	1.000000	0.250000	0.389542	0.5	...	0.230769	0.0000	0.600779	0.654550	0.333333	0.0	0.000000	0.533333	0.039216	0.369788
28	0.666667	0.0	0.687225	0.711538	0.952055	0.177437	1.000000	0.500000	0.068811	0.0	...	0.615385	0.3750	0.303894	0.653052	1.000000	0.0	0.636364	0.566667	0.647059	0.614002
29	0.666667	0.5	0.599945	0.750000	0.150685	0.547398	0.333333	0.083333	0.926329	1.0	...	0.384615	0.0000	0.473392	0.629898	0.000000	0.0	1.000000	0.733333	1.000000	0.774449
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
16943	1.000000	0.0	0.687225	0.711538	0.952055	0.177529	1.000000	0.500000	0.379337	0.5	...	0.076923	0.8750	0.363492	0.000058	1.000000	0.0	0.727273	0.700000	0.745098	0.684734
16944	0.666667	0.0	0.526982	0.461538	0.952055	0.393731	1.000000	0.833333	0.358441	0.5	...	0.000000	0.0000	0.364194	0.000058	1.000000	0.0	1.000000	0.966667	0.000000	0.789655
16945	1.000000	0.0	0.160242	0.045788	0.910959	0.547398	0.500000	0.416667	0.712897	0.5	...	0.000000	0.7500	0.363531	0.000058	1.000000	0.0	1.000000	0.400000	0.960784	0.780898
16946	1.000000	0.5	0.482930	0.501832	0.643836	0.547398	0.166667	0.000000	0.216639	0.5	...	0.000000	0.8750	0.363456	0.000058	1.000000	0.0	1.000000	0.366667	0.960784	0.776508
16947	1.000000	0.0	0.364537	0.361722	1.000000	0.547398	0.166667	0.000000	0.765575	0.5	...	0.000000	0.8750	0.363412	0.000058	1.000000	0.0	0.909091	0.766667	0.921569	0.763084
16948	1.000000	0.0	0.147026	0.167582	0.801370	0.547398	0.000000	0.666667	0.736223	0.5	...	0.000000	0.6250	0.363557	0.000046	1.000000	0.0	1.000000	0.333333	0.960784	0.777447
16949	0.000000	1.0	0.525055	0.175824	0.952055	0.905028	1.000000	1.000000	0.955681	1.0	...	0.307692	0.2500	0.365293	0.000046	0.333333	0.0	0.909091	0.166667	0.862745	0.733118
16950	1.000000	0.0	0.384637	0.900183	0.952055	0.771896	1.000000	0.250000	0.113616	0.0	...	0.076923	0.7500	0.363382	0.000046	1.000000	0.0	0.818182	0.033333	0.764706	0.680356
16951	1.000000	0.0	0.384637	0.900183	0.952055	0.772153	1.000000	0.250000	0.353387	0.5	...	0.000000	1.0000	0.363451	0.000046	1.000000	0.0	0.363636	0.766667	0.392157	0.369788
16952	1.000000	0.5	0.482930	0.501832	0.643836	0.547398	0.166667	0.000000	0.523569	0.5	...	0.000000	0.8750	0.363196	0.000046	1.000000	0.0	1.000000	0.366667	0.960784	0.777690
16953	1.000000	0.0	0.952093	0.251832	0.643836	0.547398	0.166667	0.000000	0.519681	0.5	...	0.000000	0.8750	0.363329	0.000046	1.000000	0.0	1.000000	0.566667	0.980392	0.780027
16954	0.000000	0.5	0.393447	0.595238	0.116438	0.547398	0.833333	0.833333	0.472641	0.5	...	0.461538	0.0000	0.365227	0.000035	0.333333	0.0	1.000000	0.700000	1.000000	0.780733
16955	0.000000	0.0	0.837280	0.284799	0.945205	0.547398	0.666667	0.583333	0.348819	0.5	...	0.076923	0.0000	0.363994	0.000035	1.000000	0.0	0.363636	0.733333	0.392157	0.369788
16956	1.000000	0.5	0.483756	0.740842	0.657534	0.547398	0.000000	0.333333	0.605404	0.5	...	0.076923	0.6250	0.362381	0.000035	1.000000	0.0	0.636364	0.200000	0.607843	0.552392
16957	1.000000	0.0	0.384637	0.900183	0.952055	0.772153	1.000000	0.250000	0.343279	0.5	...	0.000000	1.0000	0.363184	0.000035	1.000000	0.0	0.272727	0.533333	0.294118	0.369788
16958	0.000000	0.0	0.069934	0.175824	0.952055	0.938518	1.000000	1.000000	0.480416	0.5	...	0.461538	0.0000	0.365227	0.000035	1.000000	0.0	0.727273	0.966667	0.764706	0.686008
16959	0.666667	0.0	0.436399	0.442308	0.732877	0.547398	0.500000	0.416667	0.763048	0.5	...	0.000000	0.0000	0.364244	0.000035	1.000000	0.0	1.000000	0.533333	0.980392	0.779924
16960	0.333333	0.0	0.966134	0.555861	0.150685	0.547398	0.333333	0.083333	0.326368	0.5	...	0.000000	0.0000	0.363798	0.000035	1.000000	0.0	1.000000	0.733333	1.000000	0.777721
16961	1.000000	0.0	0.183095	0.197802	0.301370	0.547398	0.666667	0.250000	0.562251	0.5	...	0.076923	0.0000	0.364193	0.000023	1.000000	0.0	0.363636	0.233333	0.352941	0.369788
16962	1.000000	0.5	0.683095	0.967033	0.041096	0.547398	0.000000	0.750000	0.456993	0.5	...	0.076923	0.1250	0.364476	0.000023	1.000000	0.0	0.909091	0.800000	0.921569	0.761649
16963	1.000000	0.0	0.747247	0.057692	0.746575	0.547398	0.500000	0.416667	0.402274	0.5	...	0.000000	0.0000	0.363841	0.000023	1.000000	0.0	0.727273	0.100000	0.686275	0.641788
16964	0.666667	0.0	0.783866	0.580586	0.205479	0.547398	0.833333	0.166667	0.301584	0.5	...	0.076923	0.0000	0.363689	0.000023	1.000000	0.0	0.272727	0.533333	0.294118	0.369788
16965	0.000000	1.0	0.931443	0.595238	0.116438	0.547398	0.833333	0.833333	0.563903	0.5	...	0.000000	0.0000	0.363640	0.000012	0.333333	0.0	0.909091	0.266667	0.862745	0.746665
16966	1.000000	0.5	0.673733	0.900183	0.952055	0.776370	1.000000	0.250000	0.247643	0.5	...	0.076923	1.0000	0.363214	0.000012	1.000000	0.0	0.727273	0.166667	0.686275	0.617304
16967	0.000000	1.0	0.581498	0.563187	0.910959	0.547398	0.500000	0.416667	0.394305	0.5	...	0.384615	0.7500	0.358942	0.000012	1.000000	0.0	0.909091	0.933333	0.921569	0.770642
16968	0.000000	0.0	0.130507	0.874542	0.116438	0.547398	0.833333	0.833333	0.616289	0.5	...	0.307692	0.0000	0.364508	0.000012	0.333333	0.0	0.727273	0.166667	0.686275	0.640349
16969	0.333333	0.5	0.531388	0.931319	0.390411	0.547398	0.000000	0.333333	0.586646	0.5	...	0.076923	0.0000	0.363813	0.000000	0.333333	0.0	0.363636	0.966667	0.411765	0.369788
16970	1.000000	1.0	0.898128	0.750916	0.041096	0.547398	0.000000	0.750000	0.358538	0.5	...	0.307692	0.1250	0.365526	0.000000	1.000000	0.0	0.363636	0.233333	0.352941	0.369788
16971	0.333333	0.5	0.474394	0.375458	0.445205	0.547398	0.000000	0.666667	0.467490	0.5	...	0.307692	0.0000	0.364063	0.000000	1.000000	0.0	0.454545	0.600000	0.470588	0.417173
16972	1.000000	0.0	0.384637	0.900183	0.952055	0.772153	1.000000	0.250000	0.254835	0.5	...	0.000000	1.0000	0.363531	0.000000	1.000000	0.0	0.454545	0.633333	0.470588	0.372165
16973 rows × 23 columns


test_set
     

df5 = regressor.predict(X_val)
     

test_set
     
Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	Product ID	Category	...	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear	Predicted Values
Order Date																					
2014-10-14	3	1	2771	192	139	95823.000000	6	12	3825	1	...	5	0.20	1906.4850	867.69	2	2014	10	14	42	0.010876
2014-07-31	2	1	2445	435	44	55190.379428	4	3	2388	1	...	4	0.10	186.9480	801.66	0	2014	7	31	31	0.010876
2014-03-11	2	1	1356	504	139	42420.000000	6	10	8372	2	...	9	0.00	517.4793	780.70	0	2014	3	11	11	0.010876
2014-08-09	3	1	2592	1003	63	55190.379428	4	10	2752	1	...	14	0.00	3979.0800	778.32	2	2014	8	9	32	0.010876
2014-01-31	0	1	3265	820	6	55190.379428	0	9	8642	2	...	9	0.10	28.4040	766.93	0	2014	1	31	5	0.010876
2014-05-12	2	0	3336	520	128	55190.379428	1	0	5443	1	...	6	0.00	818.2800	763.38	1	2014	5	12	20	0.010876
2014-07-31	0	0	1572	230	81	55190.379428	5	7	10096	2	...	4	0.00	445.5200	728.97	0	2014	7	31	31	0.010876
2014-05-09	0	0	3047	867	38	55190.379428	5	3	2057	0	...	8	0.20	526.4960	728.39	0	2014	5	9	19	0.010876
2014-05-11	1	1	531	718	139	27217.000000	6	10	9443	2	...	4	0.50	-3839.9904	674.82	1	2014	5	11	19	0.010876
2014-11-11	3	2	1209	397	57	55190.379428	0	4	10055	2	...	7	0.00	632.5200	658.69	1	2014	11	11	46	0.010876
2014-09-26	2	1	3209	505	57	55190.379428	0	4	478	0	...	13	0.00	2097.0300	658.35	3	2014	9	26	39	0.010876
2014-08-28	0	0	2979	895	26	55190.379428	0	8	568	0	...	6	0.00	110.3400	644.75	1	2014	8	28	35	0.010876
2014-12-18	2	0	2466	775	140	55190.379428	5	10	602	0	...	11	0.00	868.1200	634.53	1	2014	12	18	51	0.010876
2014-09-18	0	0	336	636	59	55190.379428	3	5	8547	2	...	8	0.00	527.0400	630.97	0	2014	9	18	38	0.010876
2014-07-25	1	1	1421	192	139	92646.000000	6	12	8692	2	...	5	0.20	839.9860	630.05	1	2014	7	25	30	0.010876
2014-05-08	0	0	1178	1056	6	55190.379428	0	9	2555	1	...	9	0.10	1164.2670	614.34	1	2014	5	8	19	0.010876
2014-08-24	2	0	3140	332	139	32303.000000	6	10	9774	2	...	13	0.20	327.5922	609.44	3	2014	8	24	34	0.010876
2014-11-03	2	0	912	277	10	55190.379428	0	4	132	0	...	7	0.00	581.9100	609.24	1	2014	11	3	45	0.010876
2014-11-08	2	1	2215	581	47	55190.379428	4	3	9842	2	...	7	0.00	313.1100	604.40	3	2014	11	8	45	0.010876
2014-01-18	3	0	3532	463	26	55190.379428	0	8	518	0	...	11	0.00	656.3700	595.50	1	2014	1	18	3	0.010876
2014-07-12	0	0	2951	46	119	55190.379428	4	10	489	0	...	5	0.00	1050.1500	593.91	1	2014	7	12	28	0.010876
2014-12-16	0	1	2651	1018	57	55190.379428	0	4	1963	0	...	4	0.00	652.9200	592.77	0	2014	12	16	51	0.010876
2014-11-20	1	2	1293	298	81	55190.379428	5	7	10099	2	...	4	0.00	119.2800	592.73	0	2014	11	20	47	0.010876
2014-08-26	0	1	2417	950	58	55190.379428	0	11	1937	0	...	7	0.47	-452.8104	586.57	1	2014	8	26	35	0.010876
2014-05-16	2	0	2082	1033	6	55190.379428	0	9	9928	2	...	5	0.10	858.9000	581.88	0	2014	5	16	20	0.010876
2014-11-19	3	0	1855	715	44	55190.379428	4	3	801	0	...	14	0.10	63.5460	572.95	1	2014	11	19	47	0.010876
2014-10-28	2	1	2081	641	85	55190.379428	1	0	8537	2	...	14	0.00	2597.2800	568.45	3	2014	10	28	44	0.010876
2014-01-17	2	0	1504	646	139	49201.000000	6	3	4008	1	...	4	0.00	2504.2216	567.95	1	2014	1	17	3	0.010876
2014-08-18	2	0	2499	777	139	19134.000000	6	6	708	0	...	9	0.30	-630.8820	566.65	3	2014	8	18	34	0.010876
2014-12-23	2	1	2182	819	22	55190.379428	2	1	9531	2	...	6	0.00	1159.0200	546.56	0	2014	12	23	52	0.010876
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
2014-09-22	3	0	2499	777	139	19143.000000	6	6	3903	1	...	2	0.70	-1.5264	0.06	3	2014	9	22	39	0.010876
2014-12-30	2	0	1917	504	139	40214.000000	6	10	3688	1	...	1	0.00	5.8891	0.06	3	2014	12	30	1	0.010876
2014-12-13	3	0	585	50	133	55190.379428	3	5	7335	1	...	1	0.60	-1.1100	0.06	3	2014	12	13	50	0.010876
2014-12-12	3	1	1757	548	94	55190.379428	1	0	2229	1	...	1	0.70	-1.9020	0.06	3	2014	12	12	50	0.010876
2014-11-24	3	0	1327	395	146	55190.379428	1	0	7877	1	...	1	0.70	-2.3730	0.06	3	2014	11	24	48	0.010876
2014-12-11	3	0	537	183	117	55190.379428	0	8	7575	1	...	1	0.50	-0.8400	0.05	3	2014	12	11	50	0.010876
2014-11-06	0	2	1910	192	139	90045.000000	6	12	9833	2	...	5	0.20	17.4975	0.05	1	2014	11	6	45	0.010876
2014-10-02	3	0	1400	983	139	77070.000000	6	3	1169	0	...	2	0.60	-2.6892	0.05	3	2014	10	2	40	0.010876
2014-05-24	3	0	1400	983	139	77095.000000	6	3	3636	1	...	1	0.80	-1.9602	0.05	3	2014	5	24	21	0.010876
2014-12-12	3	1	1757	548	94	55190.379428	1	0	5387	1	...	1	0.70	-4.6470	0.05	3	2014	12	12	50	0.010876
2014-12-18	3	0	3461	275	94	55190.379428	1	0	5347	1	...	1	0.70	-3.2490	0.05	3	2014	12	18	51	0.010876
2014-12-22	0	1	1432	650	17	55190.379428	5	10	4863	1	...	7	0.00	16.8000	0.04	1	2014	12	22	52	0.010876
2014-05-23	0	0	3044	311	138	55190.379428	4	7	3589	1	...	2	0.00	3.7800	0.04	3	2014	5	23	21	0.010876
2014-08-07	3	1	1760	809	96	55190.379428	0	4	6229	1	...	2	0.50	-13.2600	0.04	3	2014	8	7	32	0.010876
2014-04-17	3	0	1400	983	139	77095.000000	6	3	3532	1	...	1	0.80	-4.7784	0.04	3	2014	4	17	16	0.010876
2014-09-30	0	0	257	192	139	93309.000000	6	12	4943	1	...	7	0.00	16.8000	0.04	3	2014	9	30	40	0.010876
2014-12-17	2	0	1588	483	107	55190.379428	3	5	7851	1	...	1	0.00	6.4200	0.04	3	2014	12	17	51	0.010876
2014-12-23	1	0	3512	607	22	55190.379428	2	1	3358	1	...	1	0.00	1.7100	0.04	3	2014	12	23	52	0.010876
2014-05-08	3	0	668	216	44	55190.379428	4	3	5785	1	...	2	0.00	5.8800	0.03	3	2014	5	8	19	0.010876
2014-11-25	3	1	2484	1056	6	55190.379428	0	9	4702	1	...	2	0.10	8.8620	0.03	3	2014	11	25	48	0.010876
2014-09-04	3	0	2717	63	109	55190.379428	3	5	4139	1	...	1	0.00	2.1600	0.03	3	2014	9	4	36	0.010876
2014-04-17	2	0	2850	634	30	55190.379428	5	2	3103	1	...	2	0.00	0.5600	0.03	3	2014	4	17	16	0.010876
2014-11-09	0	2	3386	650	17	55190.379428	5	10	5802	1	...	1	0.00	0.0400	0.02	1	2014	11	9	45	0.010876
2014-09-06	3	1	2450	983	139	77506.000000	6	3	2548	1	...	2	0.80	-4.4660	0.02	3	2014	9	6	36	0.010876
2014-11-29	0	2	2115	615	133	55190.379428	3	5	4057	1	...	6	0.60	-49.5720	0.02	3	2014	11	29	48	0.010876
2014-09-06	0	0	477	955	17	55190.379428	5	10	6341	1	...	5	0.00	9.2000	0.02	1	2014	9	6	36	0.010876
2014-05-30	1	1	1933	1017	57	55190.379428	0	4	6036	1	...	2	0.00	1.8600	0.01	1	2014	5	30	22	0.010876
2014-05-08	3	2	3265	820	6	55190.379428	0	9	3689	1	...	5	0.10	19.9500	0.01	3	2014	5	8	19	0.010876
2014-06-19	1	1	1726	410	65	55190.379428	0	8	4810	1	...	5	0.00	4.5000	0.01	3	2014	6	19	25	0.010876
2014-06-20	3	0	1400	983	139	77095.000000	6	3	2622	1	...	1	0.80	-1.1100	0.01	3	2014	6	20	25	0.010876
16973 rows × 22 columns


val_set2 =  pd.DataFrame(val_set_scaled , columns = col2)
     

val_set2['Predicted Values'] = df5
     

val_set2
     

val_set2['Actual Values'] = val_set2['Sales']
     

test_set2['Actual Sales'] = test_set2['Sales']
     

test_set_scaled.columns
     

scaler = preprocessing.MinMaxScaler(feature_range = (0,1))
scaled_data = scaler.fit_transform(test_set['Sales'].reshape(-1,1))
     
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:2: FutureWarning: reshape is deprecated and will raise in a subsequent release. Please use .values.reshape(...) instead
  

df4['Actual Sales'] = pd.DataFrame(scaled_data)
     

test_set['Actual Sales'] = pd.DataFrame(scaled_data)
     

test_set['Actual Sales'] = df4['Actual Sales']
     

df4['Actual Sales']
     
1        0.133515
2        0.160682
3        0.568458
4        0.183231
5        0.243530
6        0.122390
7        0.150437
8        0.571415
9        0.322749
10       0.404830
11       0.197204
12       0.248058
13       0.150591
14       0.171400
15       0.299372
16       0.311972
17       0.218781
18       0.319479
19       0.360624
20       0.156263
21       0.137142
22       0.121687
23       0.244773
24       0.204500
25       0.409221
26       0.378641
27       0.388836
28       0.315420
29       0.275969
30       0.251725
           ...   
16943    0.000105
16944    0.000863
16945    0.000255
16946    0.000143
16947    0.000054
16948    0.000461
16949    0.019966
16950    0.000253
16951    0.000053
16952    0.000159
16953    0.000167
16954    0.002588
16955    0.001918
16956    0.001280
16957    0.000175
16958    0.002468
16959    0.003806
16960    0.000446
16961    0.001245
16962    0.003336
16963    0.000350
16964    0.001348
16965    0.000391
16966    0.000084
16967    0.002406
16968    0.005968
16969    0.001893
16970    0.004115
16971    0.004618
16972    0.000000
Name: Actual Sales, Length: 16972, dtype: float64

test_set['Predicted Values']
     

print(X_train.shape)
     
(27918, 1, 21)

df.head()
     
Row ID	Order ID	Order Date	Ship Date	Ship Mode	Customer ID	Customer Name	Segment	City	State	...	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear
Order Date																					
2012-07-31	32298	CA-2012-124891	2012-07-31	31-07-2012	Same Day	RH-19495	Rick Hansen	Consumer	New York City	New York	...	2309.650	7	0.0	762.1845	933.57	Critical	2012	7	31	31
2013-05-02	26341	IN-2013-77878	2013-05-02	07-02-2013	Second Class	JR-16210	Justin Ritter	Corporate	Wollongong	New South Wales	...	3709.395	9	0.1	-288.7650	923.63	Critical	2013	5	2	18
2013-10-17	25330	IN-2013-71249	2013-10-17	18-10-2013	First Class	CR-12730	Craig Reiter	Consumer	Brisbane	Queensland	...	5175.171	9	0.1	919.9710	915.49	Medium	2013	10	17	42
2013-01-28	13524	ES-2013-1579342	2013-01-28	30-01-2013	First Class	KM-16375	Katherine Murray	Home Office	Berlin	Berlin	...	2892.510	5	0.1	-96.5400	910.16	Medium	2013	1	28	5
2013-05-11	47221	SG-2013-4320	2013-05-11	06-11-2013	Same Day	RH-9495	Rick Hansen	Consumer	Dakar	Dakar	...	2832.960	8	0.0	311.5200	903.04	Critical	2013	5	11	19
5 rows × 28 columns


df.head()
     
Row ID	Order Date	Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	...	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear
Order Date																					
2012-07-31	32298	2012-07-31	Same Day	Consumer	New York City	New York	United States	10024.0	US	East	...	2309.650	7	0.0	762.1845	933.57	Critical	2012	7	31	31
2013-05-02	26341	2013-05-02	Second Class	Corporate	Wollongong	New South Wales	Australia	NaN	APAC	Oceania	...	3709.395	9	0.1	-288.7650	923.63	Critical	2013	5	2	18
2013-10-17	25330	2013-10-17	First Class	Consumer	Brisbane	Queensland	Australia	NaN	APAC	Oceania	...	5175.171	9	0.1	919.9710	915.49	Medium	2013	10	17	42
2013-01-28	13524	2013-01-28	First Class	Home Office	Berlin	Berlin	Germany	NaN	EU	Central	...	2892.510	5	0.1	-96.5400	910.16	Medium	2013	1	28	5
2013-05-11	47221	2013-05-11	Same Day	Consumer	Dakar	Dakar	Senegal	NaN	Africa	Africa	...	2832.960	8	0.0	311.5200	903.04	Critical	2013	5	11	19
5 rows × 24 columns


print(df.dtypes)
     
Order Date        datetime64[ns]
Ship Mode                 object
Segment                   object
City                      object
State                     object
Country                   object
Postal Code              float64
Market                    object
Region                    object
Product ID                object
Category                  object
Sub-Category              object
Product Name              object
Sales                    float64
Quantity                   int64
Discount                 float64
Profit                   float64
Shipping Cost            float64
Order Priority            object
Year                       int64
Month                      int64
Day                        int64
WeekOfYear                 int64
dtype: object

df.head()
     
Order Date	Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	Product ID	Category	Sub-Category	Product Name	Sales	Quantity	Discount	Profit	Shipping Cost	Order Priority
0	2012-07-31	1	0	2290	703	139	10024.0	6	6	8246	2	0	2750	2309.650	7	0.0	762.1845	933.57	0
1	2013-05-02	2	1	3518	702	6	NaN	0	9	907	0	5	2525	3709.395	9	0.1	-288.7650	923.63	0
2	2013-10-17	0	0	497	820	6	NaN	0	9	10157	2	13	2502	5175.171	9	0.1	919.9710	915.49	3
3	2013-01-28	0	2	375	145	47	NaN	4	3	10146	2	13	2414	2892.510	5	0.1	-96.5400	910.16	3
4	2013-05-11	1	0	857	270	110	NaN	1	0	10249	2	6	3158	2832.960	8	0.0	311.5200	903.04	0

df.columns
     
Index(['Order Date', 'Ship Mode', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount',
       'Profit', 'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day',
       'WeekOfYear'],
      dtype='object')

y = df['Sales']
     

df.index.min()
     
Timestamp('2011-01-01 00:00:00')

import matplotlib.pyplot as plt
import statsmodels.api as sm
from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive' , freq=12)
fig = decomposition.plot()
plt.show()
     


results.plot_diagnostics(figsize=(16, 8))
plt.show()
     

df['Order Date']
     
Order Date
2012-07-31   2012-07-31
2013-05-02   2013-05-02
2013-10-17   2013-10-17
2013-01-28   2013-01-28
2013-05-11   2013-05-11
2013-06-28   2013-06-28
2011-07-11   2011-07-11
2012-04-14   2012-04-14
2014-10-14   2014-10-14
2012-01-28   2012-01-28
2011-05-04   2011-05-04
2012-04-19   2012-04-19
2011-12-27   2011-12-27
2012-11-13   2012-11-13
2013-06-06   2013-06-06
2014-07-31   2014-07-31
2014-03-11   2014-03-11
2014-08-09   2014-08-09
2014-01-31   2014-01-31
2014-05-12   2014-05-12
2012-08-08   2012-08-08
2011-10-29   2011-10-29
2011-02-05   2011-02-05
2013-02-27   2013-02-27
2014-07-31   2014-07-31
2014-05-09   2014-05-09
2011-12-17   2011-12-17
2011-03-14   2011-03-14
2013-11-03   2013-11-03
2012-02-25   2012-02-25
                ...    
2013-09-16   2013-09-16
2014-12-17   2014-12-17
2014-12-23   2014-12-23
2011-12-22   2011-12-22
2014-05-08   2014-05-08
2011-10-05   2011-10-05
2014-11-25   2014-11-25
2012-10-08   2012-10-08
2012-04-06   2012-04-06
2013-07-06   2013-07-06
2011-10-18   2011-10-18
2014-09-04   2014-09-04
2014-04-17   2014-04-17
2013-09-30   2013-09-30
2014-11-09   2014-11-09
2011-03-12   2011-03-12
2014-09-06   2014-09-06
2012-12-25   2012-12-25
2011-08-09   2011-08-09
2011-03-21   2011-03-21
2014-11-29   2014-11-29
2014-09-06   2014-09-06
2012-12-28   2012-12-28
2014-05-30   2014-05-30
2014-05-08   2014-05-08
2014-06-19   2014-06-19
2014-06-20   2014-06-20
2013-02-12   2013-02-12
2012-02-18   2012-02-18
2012-05-22   2012-05-22
Name: Order Date, Length: 51290, dtype: datetime64[ns]


     

from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

model = ARIMA(np.asarray(df),order=(1,1,2))
 
     

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#read the data
df 
#check the dtypes
df.dtypes
     
Order Date        datetime64[ns]
Ship Mode                  int64
Segment                    int64
City                       int64
State                      int64
Country                    int64
Postal Code              float64
Market                     int64
Region                     int64
Product ID                 int64
Category                   int64
Sub-Category               int64
Product Name               int64
Sales                    float64
Quantity                   int64
Discount                 float64
Profit                   float64
Shipping Cost            float64
Order Priority             int64
Year                       int64
Month                      int64
Day                        int64
WeekOfYear                 int64
dtype: object

df['Order_Date1'] = pd.to_datetime(df['Order Date'] , format = '%d/%m/%Y %H.%M.%S')
df = df.drop(['Order Date'], axis=1)
df.index = df.Order_Date1
     

df19 = pd.read_csv('Global Superstore.csv' , encoding = "ISO-8859-1" , parse_dates = ['Order Date'])
     

from sklearn import preprocessing

x = df19.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
normalized_df= pd.DataFrame(min_max_scaler.fit_transform(df19.T), columns=df19.columns, index=df19.index)
     

df.columns
# df = df[['Order_Date1','Ship Mode', 'Segment', 'City', 'State', 'Country', 'Postal Code',
#        'Market', 'Region', 'Product ID', 'Category', 'Sub-Category',
#        'Product Name' , 'Quantity', 'Discount', 'Profit',
#        'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day', 'WeekOfYear',
#        'Sales']]
     
Index(['Order_Date1', 'Ship Mode', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit',
       'Shipping Cost', 'Order Priority', 'Year', 'Month', 'Day', 'WeekOfYear',
       'Sales'],
      dtype='object')

df = df.drop('Order_Date1' , axis=1)
train = df[:int(0.8*(len(df)))]
valid = df[int(0.8*(len(df))):]

#fit the model
from statsmodels.tsa.vector_ar.var_model import VAR

model = VAR(endog=np.asarray(train))
model_fit = model.fit()

# make prediction on validation
prediction = model_fit.forecast(model_fit.y, steps=len(valid))
    
     
/usr/local/lib/python3.6/dist-packages/statsmodels/compat/pandas.py:56: FutureWarning: The pandas.core.datetools module is deprecated and will be removed in a future version. Please use the pandas.tseries module instead.
  from pandas.core import datetools
/usr/local/lib/python3.6/dist-packages/statsmodels/tsa/vector_ar/var_model.py:461: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
  params = np.linalg.lstsq(z, y_sample)[0]

col2
     
['Ship Mode',
 'Segment',
 'City',
 'State',
 'Country',
 'Postal Code',
 'Market',
 'Region',
 'Product ID',
 'Category',
 'Sub-Category',
 'Product Name',
 'Sales',
 'Quantity',
 'Discount',
 'Profit',
 'Shipping Cost',
 'Order Priority',
 'Year',
 'Month',
 'Day',
 'WeekOfYear']

pred = pd.DataFrame(index=range(0,len(prediction)),columns=['Ship Mode',
 'Segment',
 'City',
 'State',
 'Country',
 'Postal Code',
 'Market',
 'Region',
 'Product ID',
 'Category',
 'Sub-Category',
 'Product Name',
 
 'Quantity',
 'Discount',
 'Profit',
 'Shipping Cost',
 'Order Priority',
 'Year',
 'Month',
 'Day',
 'WeekOfYear','Sales'])
#pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for j in range(0,22):
    for i in range(0, len(prediction)):
       pred.iloc[i][j] = prediction[i][j]
pred
     
Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	Product ID	Category	...	Quantity	Discount	Profit	Shipping Cost	Order Priority	Year	Month	Day	WeekOfYear	Sales
0	2.26484	0.656158	1808.22	555.281	82.1434	55282.1	3.20762	5.5839	5179.93	1.01188	...	80.9418	3.15071	0.132222	-3.69085	2.08026	2.12799	2012.8	7.07681	15.9034	28.7063
1	2.27127	0.664908	1837.09	557.097	76.8403	55262.8	3.26586	5.92957	5159.98	1.00634	...	101.338	3.42696	0.130403	2.12768	2.13035	2.12126	2012.78	7.1206	16.0957	28.9607
2	2.27267	0.663829	1844.24	560.673	76.2364	55238.4	3.28513	6.02188	5148.06	1.00469	...	105.404	3.47065	0.129686	2.64893	2.18447	2.12021	2012.78	7.12813	16.1043	28.9963
3	2.27275	0.663603	1845.71	561.383	76.2173	55233.7	3.29115	6.04287	5146.15	1.00444	...	106.458	3.4798	0.129507	2.81158	2.23918	2.11987	2012.78	7.1292	16.1043	29.0014
4	2.27261	0.663561	1846.01	561.51	76.2326	55232.8	3.29305	6.04697	5145.88	1.00442	...	106.937	3.48197	0.129458	2.89126	2.29389	2.11966	2012.78	7.1294	16.1042	29.0023
5	2.27247	0.663555	1846.07	561.53	76.2385	55232.6	3.29363	6.04769	5145.86	1.00443	...	107.31	3.48278	0.129439	2.95426	2.34849	2.11948	2012.78	7.12945	16.1041	29.0026
6	2.27234	0.663555	1846.09	561.536	76.2396	55232.5	3.29377	6.04785	5145.88	1.00445	...	107.664	3.48334	0.129428	3.01383	2.40295	2.11931	2012.78	7.12948	16.1041	29.0027
7	2.27221	0.663556	1846.09	561.539	76.2392	55232.4	3.29378	6.04794	5145.91	1.00446	...	108.014	3.48385	0.129418	3.07258	2.45727	2.11915	2012.78	7.12949	16.1042	29.0028
8	2.27208	0.663557	1846.09	561.543	76.2385	55232.2	3.29373	6.04804	5145.93	1.00448	...	108.363	3.48435	0.129409	3.13103	2.51146	2.11898	2012.78	7.12951	16.1042	29.0028
9	2.27194	0.663558	1846.09	561.547	76.2378	55232.1	3.29367	6.04813	5145.96	1.0045	...	108.71	3.48484	0.129401	3.1893	2.56551	2.11882	2012.78	7.12952	16.1043	29.0029
10	2.27181	0.663559	1846.1	561.551	76.237	55232	3.29361	6.04824	5145.99	1.00451	...	109.057	3.48533	0.129392	3.24742	2.61941	2.11866	2012.78	7.12953	16.1044	29.003
11	2.27168	0.66356	1846.1	561.555	76.2362	55231.8	3.29354	6.04834	5146.02	1.00453	...	109.403	3.48582	0.129384	3.30538	2.67319	2.1185	2012.78	7.12954	16.1044	29.003
12	2.27155	0.663561	1846.1	561.559	76.2355	55231.7	3.29347	6.04844	5146.04	1.00455	...	109.749	3.48631	0.129375	3.36319	2.72682	2.11834	2012.78	7.12956	16.1045	29.0031
13	2.27142	0.663562	1846.1	561.563	76.2347	55231.6	3.2934	6.04854	5146.07	1.00456	...	110.093	3.4868	0.129367	3.42086	2.78032	2.11818	2012.78	7.12957	16.1045	29.0031
14	2.27129	0.663563	1846.1	561.567	76.2339	55231.4	3.29333	6.04864	5146.1	1.00458	...	110.436	3.48729	0.129358	3.47838	2.83369	2.11802	2012.78	7.12958	16.1046	29.0032
15	2.27116	0.663564	1846.1	561.571	76.2332	55231.3	3.29326	6.04874	5146.13	1.00459	...	110.779	3.48777	0.12935	3.53576	2.88691	2.11786	2012.78	7.12959	16.1047	29.0033
16	2.27103	0.663565	1846.1	561.575	76.2324	55231.2	3.29319	6.04884	5146.16	1.00461	...	111.121	3.48826	0.129342	3.59298	2.94001	2.1177	2012.78	7.12961	16.1047	29.0033
17	2.2709	0.663566	1846.11	561.579	76.2317	55231	3.29313	6.04894	5146.19	1.00463	...	111.462	3.48874	0.129333	3.65007	2.99297	2.11754	2012.78	7.12962	16.1048	29.0034
18	2.27077	0.663567	1846.11	561.583	76.2309	55230.9	3.29306	6.04905	5146.21	1.00464	...	111.802	3.48922	0.129325	3.707	3.04579	2.11738	2012.78	7.12963	16.1048	29.0035
19	2.27065	0.663567	1846.11	561.587	76.2301	55230.8	3.29299	6.04915	5146.24	1.00466	...	112.141	3.4897	0.129317	3.7638	3.09848	2.11723	2012.78	7.12964	16.1049	29.0035
20	2.27052	0.663568	1846.11	561.591	76.2294	55230.7	3.29292	6.04925	5146.27	1.00467	...	112.479	3.49018	0.129308	3.82045	3.15103	2.11707	2012.78	7.12965	16.1049	29.0036
21	2.27039	0.663569	1846.11	561.595	76.2286	55230.5	3.29285	6.04934	5146.3	1.00469	...	112.816	3.49066	0.1293	3.87695	3.20346	2.11691	2012.78	7.12966	16.105	29.0036
22	2.27026	0.66357	1846.11	561.599	76.2279	55230.4	3.29279	6.04944	5146.32	1.0047	...	113.153	3.49114	0.129292	3.93331	3.25574	2.11675	2012.78	7.12968	16.1051	29.0037
23	2.27014	0.663571	1846.11	561.603	76.2271	55230.3	3.29272	6.04954	5146.35	1.00472	...	113.489	3.49161	0.129283	3.98953	3.3079	2.1166	2012.78	7.12969	16.1051	29.0038
24	2.27001	0.663572	1846.11	561.607	76.2264	55230.1	3.29265	6.04964	5146.38	1.00474	...	113.823	3.49209	0.129275	4.0456	3.35992	2.11644	2012.78	7.1297	16.1052	29.0038
25	2.26988	0.663573	1846.12	561.611	76.2257	55230	3.29258	6.04974	5146.41	1.00475	...	114.157	3.49256	0.129267	4.10154	3.41181	2.11629	2012.78	7.12971	16.1052	29.0039
26	2.26976	0.663574	1846.12	561.615	76.2249	55229.9	3.29252	6.04984	5146.43	1.00477	...	114.49	3.49303	0.129259	4.15733	3.46357	2.11613	2012.78	7.12972	16.1053	29.0039
27	2.26963	0.663575	1846.12	561.619	76.2242	55229.7	3.29245	6.04994	5146.46	1.00478	...	114.823	3.49351	0.129251	4.21298	3.5152	2.11598	2012.78	7.12974	16.1053	29.004
28	2.26951	0.663576	1846.12	561.623	76.2234	55229.6	3.29238	6.05004	5146.49	1.0048	...	115.154	3.49397	0.129243	4.26848	3.5667	2.11582	2012.78	7.12975	16.1054	29.0041
29	2.26938	0.663577	1846.12	561.627	76.2227	55229.5	3.29232	6.05013	5146.51	1.00481	...	115.485	3.49444	0.129234	4.32385	3.61806	2.11567	2012.78	7.12976	16.1055	29.0041
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
10228	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10229	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10230	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10231	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10232	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10233	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10234	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10235	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10236	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10237	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10238	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10239	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10240	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10241	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10242	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10243	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10244	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10245	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10246	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10247	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10248	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10249	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10250	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10251	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10252	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10253	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10254	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10255	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10256	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10257	2.2203	0.663928	1846.6	563.156	75.9339	55179.4	3.26624	6.08846	5157.15	1.01087	...	245.254	3.67836	0.126049	26.0567	23.7805	2.05526	2012.78	7.13433	16.1275	29.0278
10258 rows × 22 columns


from sklearn.metrics import mean_squared_error
for i in pred.columns:
    print('rmse value for', i, 'is : ', np.sqrt(mean_squared_error(pred[i], valid[i])))
     
rmse value for Ship Mode is :  0.9734336053390827
rmse value for Segment is :  0.7687590981148649
rmse value for City is :  997.3987175915491
rmse value for State is :  310.97443097278034
rmse value for Country is :  37.54479229587181
rmse value for Postal Code is :  17286.485021286364
rmse value for Market is :  2.233477219931442
rmse value for Region is :  3.46668300485791
rmse value for Product ID is :  2175.4628991883455
rmse value for Category is :  0.32528519471189266
rmse value for Sub-Category is :  4.579229555347856
rmse value for Product Name is :  1112.6168280136305
rmse value for Quantity is :  2.0566515584335225
rmse value for Discount is :  0.28111243606008945
rmse value for Profit is :  31.73989422739384
rmse value for Shipping Cost is :  22.130367025424512
rmse value for Order Priority is :  0.9896212191747569
rmse value for Year is :  1.1033939802677668
rmse value for Month is :  3.422493165712028
rmse value for Day is :  8.309013945099684
rmse value for WeekOfYear is :  15.172470417901378
rmse value for Sales is :  223.68762976442062

from sklearn.metrics import mean_squared_error
for i in pred.columns:
    print('rmse value for', i, 'is : ', np.sqrt(mean_squared_error(np.log(pred[i]), np.log(valid[i]))))
     

model = VAR(endog=np.asarray(df))
model_fit = model.fit()
pred = model_fit.forecast(model_fit.y, steps=10)
pred = pd.DataFrame(index=range(0,len(prediction)),columns=['Ship Mode',
 'Segment',
 'City',
 'State',
 'Country',
 'Postal Code',
 'Market',
 'Region',
 'Product ID',
 'Category',
 'Sub-Category',
 'Product Name',
 
 'Quantity',
 'Discount',
 'Profit',
 'Shipping Cost',
 'Order Priority',
 'Year',
 'Month',
 'Day',
 'WeekOfYear','Sales'])
#pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for j in range(0,22):
    for i in range(0, len(prediction)):
       pred.iloc[i][j] = prediction[i][j]
pred = pred.drop(['Year' , 'Month' , 'Day'], axis = 1)
pred
     
/usr/local/lib/python3.6/dist-packages/statsmodels/tsa/vector_ar/var_model.py:461: FutureWarning:

`rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.

Ship Mode	Segment	City	State	Country	Postal Code	Market	Region	Product ID	Category	Sub-Category	Product Name	Quantity	Discount	Profit	Shipping Cost	Order Priority	WeekOfYear	Sales
0	2.27019	0.684044	1806.39	565.68	71.6676	55052.6	3.01918	5.92421	5119.49	1.02238	8.15963	1885.2	3.22722	0.133052	-5.02241	2.07723	2.15783	28.595	78.2692
1	2.27451	0.664095	1811.15	553.566	75.1633	55229	3.194	6.01389	5187.83	1.0062	8.15909	1892.89	3.44212	0.130858	2.21524	2.12726	2.12431	28.9763	101.757
2	2.27305	0.663573	1814.48	554.204	75.2436	55231.1	3.2589	6.01652	5197.86	1.0046	8.16282	1890.2	3.47372	0.129899	2.65896	2.18157	2.12073	28.9938	105.615
3	2.27274	0.663548	1814.75	554.2	75.2189	55232	3.28179	6.00976	5198.76	1.00445	8.16262	1890.34	3.48003	0.129589	2.80646	2.23638	2.11996	28.9991	106.512
4	2.2726	0.66355	1814.79	554.188	75.2089	55232.4	3.28972	6.00649	5198.68	1.00443	8.1626	1890.49	3.48183	0.129489	2.88594	2.29112	2.11968	29.0014	106.938
5	2.27247	0.663551	1814.79	554.183	75.2056	55232.5	3.29244	6.00532	5198.69	1.00444	8.16254	1890.56	3.48268	0.129451	2.9502	2.34573	2.11949	29.0022	107.297
6	2.27235	0.663553	1814.79	554.18	75.2045	55232.5	3.29334	6.00498	5198.8	1.00445	8.16244	1890.58	3.48329	0.129432	3.01054	2.4002	2.11932	29.0026	107.647
7	2.27222	0.663554	1814.78	554.178	75.2041	55232.4	3.29361	6.00495	5198.94	1.00446	8.16233	1890.58	3.48382	0.12942	3.06963	2.45453	2.11916	29.0027	107.996
8	2.27209	0.663555	1814.77	554.177	75.2039	55232.2	3.29366	6.00502	5199.1	1.00448	8.16221	1890.58	3.48433	0.12941	3.12822	2.50872	2.119	29.0028	108.345
9	2.27195	0.663556	1814.77	554.175	75.2037	55232.1	3.29363	6.00513	5199.27	1.00449	8.16209	1890.58	3.48483	0.129401	3.18654	2.56277	2.11883	29.0029	108.692
10	2.27182	0.663557	1814.76	554.174	75.2037	55232	3.29358	6.00525	5199.43	1.00451	8.16196	1890.57	3.48532	0.129393	3.24468	2.61669	2.11867	29.003	109.039
11	2.27169	0.663558	1814.75	554.173	75.2036	55231.8	3.29351	6.00538	5199.6	1.00453	8.16184	1890.56	3.48581	0.129384	3.30265	2.67047	2.11851	29.003	109.386
12	2.27156	0.663559	1814.74	554.171	75.2035	55231.7	3.29344	6.00551	5199.77	1.00454	8.16172	1890.56	3.4863	0.129376	3.36048	2.72411	2.11835	29.0031	109.731
13	2.27143	0.66356	1814.74	554.17	75.2034	55231.6	3.29338	6.00564	5199.94	1.00456	8.1616	1890.55	3.48679	0.129367	3.41815	2.77762	2.11819	29.0032	110.075
14	2.2713	0.66356	1814.73	554.169	75.2033	55231.4	3.29331	6.00577	5200.1	1.00458	8.16148	1890.55	3.48728	0.129359	3.47568	2.83099	2.11803	29.0032	110.419
15	2.27117	0.663561	1814.72	554.167	75.2033	55231.3	3.29324	6.0059	5200.27	1.00459	8.16136	1890.54	3.48776	0.12935	3.53306	2.88422	2.11787	29.0033	110.761
16	2.27104	0.663562	1814.71	554.166	75.2032	55231.2	3.29317	6.00602	5200.44	1.00461	8.16124	1890.54	3.48825	0.129342	3.59029	2.93732	2.11771	29.0033	111.103
17	2.27091	0.663563	1814.71	554.165	75.2031	55231	3.2931	6.00615	5200.6	1.00462	8.16112	1890.53	3.48873	0.129334	3.64738	2.99028	2.11755	29.0034	111.444
18	2.27079	0.663564	1814.7	554.163	75.203	55230.9	3.29303	6.00628	5200.77	1.00464	8.161	1890.53	3.48921	0.129325	3.70432	3.04311	2.11739	29.0035	111.784
19	2.27066	0.663565	1814.69	554.162	75.203	55230.8	3.29297	6.00641	5200.93	1.00465	8.16088	1890.52	3.48969	0.129317	3.76112	3.09581	2.11724	29.0035	112.123
20	2.27053	0.663566	1814.68	554.161	75.2029	55230.6	3.2929	6.00653	5201.1	1.00467	8.16076	1890.52	3.49017	0.129309	3.81777	3.14837	2.11708	29.0036	112.461
21	2.2704	0.663567	1814.68	554.159	75.2028	55230.5	3.29283	6.00666	5201.26	1.00469	8.16064	1890.51	3.49065	0.1293	3.87428	3.2008	2.11692	29.0037	112.799
22	2.27027	0.663568	1814.67	554.158	75.2027	55230.4	3.29276	6.00679	5201.42	1.0047	8.16052	1890.5	3.49113	0.129292	3.93065	3.25309	2.11677	29.0037	113.135
23	2.27015	0.663569	1814.66	554.157	75.2027	55230.3	3.29269	6.00691	5201.59	1.00472	8.1604	1890.5	3.4916	0.129284	3.98688	3.30525	2.11661	29.0038	113.471
24	2.27002	0.66357	1814.66	554.155	75.2026	55230.1	3.29263	6.00704	5201.75	1.00473	8.16028	1890.49	3.49208	0.129276	4.04296	3.35728	2.11645	29.0038	113.806
25	2.26989	0.663571	1814.65	554.154	75.2025	55230	3.29256	6.00717	5201.91	1.00475	8.16016	1890.49	3.49255	0.129267	4.09889	3.40918	2.1163	29.0039	114.14
26	2.26977	0.663572	1814.64	554.153	75.2024	55229.9	3.29249	6.00729	5202.07	1.00476	8.16005	1890.48	3.49302	0.129259	4.15469	3.46094	2.11614	29.004	114.473
27	2.26964	0.663572	1814.63	554.151	75.2024	55229.7	3.29243	6.00742	5202.23	1.00478	8.15993	1890.48	3.49349	0.129251	4.21035	3.51258	2.11599	29.004	114.805
28	2.26952	0.663573	1814.63	554.15	75.2023	55229.6	3.29236	6.00754	5202.39	1.0048	8.15981	1890.47	3.49396	0.129243	4.26586	3.56408	2.11583	29.0041	115.137
29	2.26939	0.663574	1814.62	554.149	75.2022	55229.5	3.29229	6.00766	5202.56	1.00481	8.15969	1890.47	3.49443	0.129235	4.32123	3.61545	2.11568	29.0041	115.468
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
10228	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10229	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10230	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10231	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10232	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10233	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10234	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10235	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10236	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10237	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10238	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10239	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10240	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10241	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10242	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10243	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10244	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10245	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10246	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10247	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10248	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10249	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10250	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10251	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10252	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10253	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10254	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10255	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10256	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10257	2.2203	0.663928	1811.79	553.637	75.173	55179.4	3.26623	6.05643	5265.61	1.01087	8.11387	1888.39	3.67836	0.126049	26.0566	23.7804	2.05526	29.0278	245.253
10258 rows × 19 columns


from fbprophet import Prophet
import numpy as np
import pandas as pd
     

df15 = pd.read_csv('Global Superstore.csv' , encoding = "ISO-8859-1" , parse_dates = ['Order Date'])
     

df15['ds'] = df15['Order Date']
     

df15.columns
     
Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
       'Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country',
       'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
       'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount',
       'Profit', 'Shipping Cost', 'Order Priority', 'ds'],
      dtype='object')

df15['y_orig'] = df15['Sales'] # to save a copy of the original data..you'll see why shortly. 
# log-transform y
df15['Sales'] = np.log(df15['Sales'])
     

df15['y'] = df15['Sales']
     

model = Prophet() #instantiate Prophet
model.fit(df15);
     
INFO:fbprophet:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.

future_data = model.make_future_dataframe(periods=100, freq = 'w')

     

forecast_data = model.predict(future_data)
     

forecast_data
     
ds	trend	trend_lower	trend_upper	yhat_lower	yhat_upper	additive_terms	additive_terms_lower	additive_terms_upper	multiplicative_terms	multiplicative_terms_lower	multiplicative_terms_upper	weekly	weekly_lower	weekly_upper	yearly	yearly_lower	yearly_upper	yhat
0	2011-01-01	4.462862	4.462862	4.462862	2.534471	6.429547	0.008843	0.008843	0.008843	0.0	0.0	0.0	0.001428	0.001428	0.001428	0.007415	0.007415	0.007415	4.471705
1	2011-01-01	4.462862	4.462862	4.462862	2.623705	6.393486	0.008843	0.008843	0.008843	0.0	0.0	0.0	0.001428	0.001428	0.001428	0.007415	0.007415	0.007415	4.471705
2	2011-01-01	4.462862	4.462862	4.462862	2.554291	6.184890	0.008843	0.008843	0.008843	0.0	0.0	0.0	0.001428	0.001428	0.001428	0.007415	0.007415	0.007415	4.471705
3	2011-01-01	4.462862	4.462862	4.462862	2.437851	6.295689	0.008843	0.008843	0.008843	0.0	0.0	0.0	0.001428	0.001428	0.001428	0.007415	0.007415	0.007415	4.471705
4	2011-01-01	4.462862	4.462862	4.462862	2.617956	6.319301	0.008843	0.008843	0.008843	0.0	0.0	0.0	0.001428	0.001428	0.001428	0.007415	0.007415	0.007415	4.471705
5	2011-01-01	4.462862	4.462862	4.462862	2.559928	6.339700	0.008843	0.008843	0.008843	0.0	0.0	0.0	0.001428	0.001428	0.001428	0.007415	0.007415	0.007415	4.471705
6	2011-01-02	4.462936	4.462936	4.462936	2.566951	6.245496	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
7	2011-01-02	4.462936	4.462936	4.462936	2.478336	6.370242	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
8	2011-01-02	4.462936	4.462936	4.462936	2.567578	6.303721	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
9	2011-01-02	4.462936	4.462936	4.462936	2.594986	6.251945	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
10	2011-01-02	4.462936	4.462936	4.462936	2.751963	6.356107	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
11	2011-01-02	4.462936	4.462936	4.462936	2.669154	6.306517	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
12	2011-01-02	4.462936	4.462936	4.462936	2.550285	6.270995	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
13	2011-01-02	4.462936	4.462936	4.462936	2.523276	6.255999	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
14	2011-01-02	4.462936	4.462936	4.462936	2.675182	6.285286	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
15	2011-01-02	4.462936	4.462936	4.462936	2.618800	6.486577	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
16	2011-01-02	4.462936	4.462936	4.462936	2.543373	6.301916	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
17	2011-01-02	4.462936	4.462936	4.462936	2.530701	6.347127	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
18	2011-01-02	4.462936	4.462936	4.462936	2.630030	6.322510	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
19	2011-01-02	4.462936	4.462936	4.462936	2.564603	6.396538	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
20	2011-01-02	4.462936	4.462936	4.462936	2.600522	6.391564	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
21	2011-01-02	4.462936	4.462936	4.462936	2.632014	6.218496	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
22	2011-01-02	4.462936	4.462936	4.462936	2.635722	6.297315	-0.011684	-0.011684	-0.011684	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005150	0.005150	0.005150	4.451252
23	2011-01-03	4.463010	4.463010	4.463010	2.533247	6.452655	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
24	2011-01-03	4.463010	4.463010	4.463010	2.526715	6.354058	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
25	2011-01-03	4.463010	4.463010	4.463010	2.462943	6.358382	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
26	2011-01-03	4.463010	4.463010	4.463010	2.624116	6.279354	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
27	2011-01-03	4.463010	4.463010	4.463010	2.449957	6.300294	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
28	2011-01-03	4.463010	4.463010	4.463010	2.599580	6.266485	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
29	2011-01-03	4.463010	4.463010	4.463010	2.583589	6.393934	-0.007490	-0.007490	-0.007490	0.0	0.0	0.0	-0.010450	-0.010450	-0.010450	0.002960	0.002960	0.002960	4.455520
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
51360	2016-05-08	4.468893	4.463034	4.474378	2.515739	6.268506	-0.083849	-0.083849	-0.083849	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.067015	-0.067015	-0.067015	4.385044
51361	2016-05-15	4.468795	4.462803	4.474367	2.569937	6.417732	-0.023842	-0.023842	-0.023842	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.007008	-0.007008	-0.007008	4.444954
51362	2016-05-22	4.468698	4.462572	4.474415	2.520855	6.433989	0.020060	0.020060	0.020060	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.036894	0.036894	0.036894	4.488758
51363	2016-05-29	4.468601	4.462329	4.474478	2.729389	6.264457	0.016880	0.016880	0.016880	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.033715	0.033715	0.033715	4.485481
51364	2016-06-05	4.468503	4.462071	4.474517	2.512690	6.326348	-0.013946	-0.013946	-0.013946	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.002888	0.002888	0.002888	4.454557
51365	2016-06-12	4.468406	4.461925	4.474567	2.600158	6.211329	-0.030250	-0.030250	-0.030250	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.013416	-0.013416	-0.013416	4.438156
51366	2016-06-19	4.468309	4.461720	4.474602	2.540155	6.315505	-0.017486	-0.017486	-0.017486	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.000652	-0.000652	-0.000652	4.450823
51367	2016-06-26	4.468211	4.461453	4.474693	2.628779	6.289179	-0.001676	-0.001676	-0.001676	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.015158	0.015158	0.015158	4.466535
51368	2016-07-03	4.468114	4.461146	4.474764	2.635254	6.301705	-0.011747	-0.011747	-0.011747	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.005087	0.005087	0.005087	4.456367
51369	2016-07-10	4.468017	4.460961	4.474844	2.599823	6.277964	-0.039622	-0.039622	-0.039622	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.022788	-0.022788	-0.022788	4.428395
51370	2016-07-17	4.467920	4.460705	4.474922	2.587662	6.191092	-0.047744	-0.047744	-0.047744	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.030910	-0.030910	-0.030910	4.420176
51371	2016-07-24	4.467822	4.460448	4.474992	2.676133	6.275206	-0.014643	-0.014643	-0.014643	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.002192	0.002192	0.002192	4.453180
51372	2016-07-31	4.467725	4.460188	4.475075	2.626763	6.428539	0.037085	0.037085	0.037085	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.053920	0.053920	0.053920	4.504810
51373	2016-08-07	4.467628	4.459993	4.475108	2.750359	6.504100	0.063795	0.063795	0.063795	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.080629	0.080629	0.080629	4.531422
51374	2016-08-14	4.467530	4.459728	4.475167	2.476400	6.418734	0.046746	0.046746	0.046746	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.063580	0.063580	0.063580	4.514276
51375	2016-08-21	4.467433	4.459448	4.475240	2.527001	6.167348	0.007618	0.007618	0.007618	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.024452	0.024452	0.024452	4.475051
51376	2016-08-28	4.467336	4.459158	4.475291	2.541999	6.279306	-0.020610	-0.020610	-0.020610	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.003776	-0.003776	-0.003776	4.446726
51377	2016-09-04	4.467238	4.458861	4.475290	2.596788	6.168049	-0.028892	-0.028892	-0.028892	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.012058	-0.012058	-0.012058	4.438346
51378	2016-09-11	4.467141	4.458611	4.475313	2.457110	6.250737	-0.032595	-0.032595	-0.032595	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.015761	-0.015761	-0.015761	4.434546
51379	2016-09-18	4.467044	4.458338	4.475415	2.606636	6.341718	-0.042882	-0.042882	-0.042882	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.026047	-0.026047	-0.026047	4.424162
51380	2016-09-25	4.466946	4.458122	4.475518	2.533894	6.361734	-0.049248	-0.049248	-0.049248	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.032414	-0.032414	-0.032414	4.417698
51381	2016-10-02	4.466849	4.457887	4.475540	2.600977	6.427803	-0.034857	-0.034857	-0.034857	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.018023	-0.018023	-0.018023	4.431992
51382	2016-10-09	4.466752	4.457608	4.475665	2.566689	6.264563	-0.002255	-0.002255	-0.002255	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.014579	0.014579	0.014579	4.464496
51383	2016-10-16	4.466654	4.457352	4.475729	2.609836	6.357790	0.025091	0.025091	0.025091	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.041925	0.041925	0.041925	4.491746
51384	2016-10-23	4.466557	4.457142	4.475780	2.515946	6.371379	0.027294	0.027294	0.027294	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.044129	0.044129	0.044129	4.493852
51385	2016-10-30	4.466460	4.456914	4.475788	2.559334	6.423270	0.007533	0.007533	0.007533	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.024368	0.024368	0.024368	4.473993
51386	2016-11-06	4.466363	4.456642	4.475836	2.682061	6.352488	-0.015844	-0.015844	-0.015844	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	0.000990	0.000990	0.000990	4.450518
51387	2016-11-13	4.466265	4.456355	4.475869	2.714386	6.239860	-0.031039	-0.031039	-0.031039	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.014204	-0.014204	-0.014204	4.435227
51388	2016-11-20	4.466168	4.456068	4.475892	2.534253	6.200241	-0.039875	-0.039875	-0.039875	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.023041	-0.023041	-0.023041	4.426293
51389	2016-11-27	4.466071	4.455802	4.475967	2.584400	6.161771	-0.045331	-0.045331	-0.045331	0.0	0.0	0.0	-0.016834	-0.016834	-0.016834	-0.028497	-0.028497	-0.028497	4.420740
51390 rows × 19 columns


model.plot(forecast_data)
     



model.plot_components(forecast_data)
     



forecast_data_orig = forecast_data # make sure we save the original forecast data

forecast_data_orig['yhat'] = np.exp(forecast_data_orig['yhat'])
forecast_data_orig['yhat_lower'] = np.exp(forecast_data_orig['yhat_lower'])
forecast_data_orig['yhat_upper'] = np.exp(forecast_data_orig['yhat_upper'])
     

df16 = forecast_data
df16['end1'] = np.exp(forecast_data['yhat'])
     

df16
     

model.plot(forecast_data_orig)
     

from fbprophet.diagnostics import cross_validation
df_cv = cross_validation(model, initial='730 days', period='180 days', horizon = '365 days')
df_cv.head()
     
INFO:fbprophet:Making 3 forecasts with cutoffs between 2013-01-05 00:00:00 and 2013-12-31 00:00:00
ds	yhat	yhat_lower	yhat_upper	y	cutoff
0	2013-01-06	4.484491	2.619825	6.299039	2.917554	2013-01-05
1	2013-01-06	4.484491	2.667634	6.195070	3.432696	2013-01-05
2	2013-01-06	4.484491	2.644376	6.310192	3.995629	2013-01-05
3	2013-01-06	4.484491	2.662958	6.424545	3.118304	2013-01-05
4	2013-01-06	4.484491	2.632457	6.154654	4.837931	2013-01-05

from fbprophet.diagnostics import performance_metrics
df_p = performance_metrics(df_cv)
df_p.head()
     
horizon	mse	rmse	mae	mape	coverage
15546	48 days	2.136207	1.461577	1.195176	0.357298	0.779129
15547	48 days	2.136067	1.461529	1.195128	0.357233	0.779129
15549	48 days	2.134961	1.461151	1.194725	0.357183	0.779343
15550	48 days	2.135120	1.461205	1.194845	0.357204	0.779343
15543	48 days	2.135135	1.461210	1.194862	0.357208	0.779343


     