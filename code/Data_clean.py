import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns
from datetime import datetime
from collections import Counter
user=pd.read_csv('user_logs_v2.csv')
train=pd.read_csv('train_v2.csv')
training = pd.merge(left = train,right = user,how = 'left',on=['msno'])
print(training.head())
training['num_25'] = training.num_25.apply(lambda x: int(x) if pd.notnull(x) else 0)
training['num_50'] = training.num_50.apply(lambda x: int(x) if pd.notnull(x) else 0)
training['num_75'] = training.num_75.apply(lambda x: int(x) if pd.notnull(x) else 0)
training['num_100'] = training.num_100.apply(lambda x: int(x) if pd.notnull(x) else 0)
training['total_secs'] = training.total_secs.apply(lambda x: int(x) if pd.notnull(x) else 0)
training['num_unq'] = training.num_unq.apply(lambda x: int(x) if pd.notnull(x) else 0)

dic = Counter(training.msno)
a=[]
for key in dic:
	a.append(dic[key])

training_churn = training[training['is_churn'] == 1]

dic2= Counter(training_churn.msno)
b=[]
for key in dic2:
	b.append(dic2[key])


plt.figure(1)
plt.subplot(421)

p1=sns.distplot(training['num_25'],hist = False, kde = True, kde_kws = {'shade':True,'linewidth':5})
s1=sns.distplot(training_churn['num_25'],hist = False,color='red', kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlim([1,60])
plt.xlabel('Num of Songs')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for num_25", fontsize=12)


plt.subplot(422)
p2=sns.distplot(training['num_50'],hist = False, kde = True, kde_kws = {'shade':True,'linewidth':5})
s2=sns.distplot(training_churn['num_50'],hist = False,color='red', kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlim([1,15])
plt.xlabel('Num of Songs')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for num_50", fontsize=12)


plt.subplot(423)
p3=sns.distplot(training['num_75'],hist = False,kde = True, kde_kws = {'shade':True,'linewidth':5})
s3=sns.distplot(training['num_75'],hist = False,color='red',kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlim([1,15])
plt.xlabel('Num of Songs')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for num_75", fontsize=12)

plt.subplot(424)
p4=sns.distplot(training['num_100'],hist = False, kde = True, kde_kws = {'shade':True,'linewidth':5})
s5=sns.distplot(training_churn['num_100'],hist = False,color='red', kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlim([1,150])
plt.xlabel('Num of Songs')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for num_100", fontsize=12)


plt.subplot(425)
p5=sns.distplot(training['num_unq'],hist = False, kde = True, kde_kws = {'shade':True,'linewidth':5})
s5=sns.distplot(training_churn['num_unq'],hist = False,color='red', kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlim([1,100])
plt.xlabel('Num of Songs')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for unique number of songs", fontsize=12)
plt.legend(loc='best')

plt.subplot(426)
p6=sns.distplot(training['total_secs'],hist = False,kde = True, kde_kws = {'shade':True,'linewidth':5})
s6=sns.distplot(training_churn['total_secs'],hist = False,color='red', kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlabel('total seconds')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for total seconds", fontsize=12)
plt.legend(loc='best')




plt.subplot(414)
p7=sns.distplot(a,hist = False, kde = True, kde_kws = {'shade':True,'linewidth':5})
s7=sns.distplot(b,hist = False,color='red', kde = True, kde_kws = {'shade':True,'linewidth':1})
plt.xlabel('entries per user')
plt.ylabel('Density', fontsize=12)
plt.title("Uesr_log for entries per user", fontsize=12)
plt.legend(loc='best')


plt.tight_layout()
plt.show()





