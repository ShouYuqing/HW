#!/usr/bin/env python
'''
For Python 2.7
'''
import scipy.stats as ss
import numpy as np
import csv
import codecs
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt

"""
Encoding
"""
file11 = codecs.open('/classes/ece2720/pe3/unicode1.dat','r','utf-8')
for i in file11.readlines():
	print(i)
file22 = codecs.open('/classes/ece2720/pe3/unicode2.dat','r','utf-16-le')
for i in file22.readlines():
	print(i)
file33 = codecs.open('/classes/ece2720/pe3/unicode3.dat','r','utf-8')
for i in file33.readlines():
	print(i)
file44 = codecs.open('/classes/ece2720/pe3/unicode4.dat','rb','utf-16')
for i in file44.readlines():
	print(i)
file55 = codecs.open('/classes/ece2720/pe3/unicode5.dat', 'r', 'utf-16-be')
for i in file55.readlines():
    print(i)




"""
Synthetic data processing
"""

# array to store the data
arr = np.zeros(shape=(1,3000))

# open csv file and read it into array
i=0
file = csv.reader(open('/classes/ece2720/pe3/synthetic.csv','r'))
for num in file:
    arr[i] = num

# plot histogram of data
plt.hist(arr[0,:])
plt.title("histogram")
plt.savefig('figure1.pdf')

# plot the probability plot of data
plt.figure()
ss.probplot(arr[0,:], plot = plt)
plt.savefig('figure2.pdf')

#calculate ML mean
m_sum = 0
for m_i in range(0,3000):
    m_sum = m_sum + arr[0,m_i]
meann = m_sum/(m_i+1)

# calculate ML variance
v_sum=0
for v_i in range(0,3000):
    v_sum = v_sum + (arr[0,v_i]-meann)**2
variancee = v_sum/(v_i+1)
#print(variancee)


"""
Real data processing
"""
# read age6
age = np.zeros(shape = [1,1000])
fare = np.zeros(shape = [1,1000])
file2 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt2 = 0
for k in file2.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[6] =='':
            cnt = cnt + 1
        else:
            cnt = cnt + 1
            if k.split(',')[6] == '':
                cnt = cnt + 1
            else:
                age[0, cnt2] = float(k.split(',')[6])
                cnt = cnt + 1
                cnt2 = cnt2 + 1

# plot the histogram of age
real_age = np.zeros(shape=[1,1])
for i in range(0, 1000):
    if age[0,i]==0:
        continue
    else:
        real_age = np.append(real_age, age[0,i])

#print(real_age.shape)
plt.figure()
plt.hist(real_age[:])
plt.title("age histogram")
plt.savefig('figure3.pdf')

# mean and variance of age
a_sum = 0
for a_i in real_age:
    a_sum = a_sum + a_i
meann = a_sum/(real_age.size)
#print(meann)

a_sum=0
for a_i in real_age:
    a_sum = a_sum + (a_i-meann)**2
variancee = a_sum/(real_age.size)
#print(variancee)




# read fare10
file3 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt2 = 0
for k in file3.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[6] =='':
            cnt = cnt + 1
        else:
            fare[0, cnt2] = float(k.split(',')[10])
            cnt = cnt + 1
            cnt2 = cnt2 + 1

# plot the histogram of fare
real_fare = np.zeros(shape=[1,1])
for i in range(0, 1000):
    if fare[0,i]==0:
        continue
    else:
        real_fare = np.append(real_fare, fare[0,i])

#print(real_fare.shape)
plt.figure()
plt.hist(real_fare[:])
plt.title("fare histogram")
plt.savefig('figure4.pdf')

# count the number of passengers
# mean of fare
m_sum = 0
for f_i in real_fare:
    m_sum = m_sum + f_i
meann = m_sum/(real_fare.size)
#print(meann)

# variance of fare
f_sum=0
for f_i in real_fare:
    f_sum = f_sum + (f_i-meann)**2
variancee = f_sum/(real_fare.size)
#print(variancee)

# plot probability plot
plt.figure()
ss.probplot(real_age, plot = plt)
plt.savefig('figure5.pdf')

plt.figure()
ss.probplot(real_fare, plot = plt)
plt.savefig('figure6.pdf')

# calculate overall survival rate
file4 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt2 = 0
cnt_sv = 0
cnt_dd = 0
for k in file4.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if int(k.split(',')[1]) == 0:
            cnt_dd = cnt_dd + 1
            cnt = cnt + 1
        else:
            cnt_sv =cnt_sv + 1
            cnt = cnt + 1

sv_rate = cnt_sv/ float(cnt_dd + cnt_sv)
print('overall survival rate: '+str(sv_rate))

# 1
file5 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file5.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[5] == 'female':
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('female survival rate: '+str(sv_rate))

# 2
file6 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file6.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[5] == 'male':
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('male survival rate: '+str(sv_rate))


# 3
file7 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file7.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[2] == '1':
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('first class survival rate: '+str(sv_rate))

# 4
file8 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file8.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[2] == '3':
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('third class survival rate: '+str(sv_rate))

# 5
file9 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file9.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[2] == '1' and k.split(',')[5] == 'male':
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('men in first class survival rate: '+str(sv_rate))


# 6
file10 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file10.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if k.split(',')[2] == '3' and k.split(',')[5] == 'female':
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('weman in third class survival rate: '+str(sv_rate))


# 7
file11 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file11.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if float(k.split(',')[10]) > 100 :
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('Those whose fare exceeded 100 survival rate: '+str(sv_rate))

# 8
file12 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file12.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if float(k.split(',')[10]) < 50 :
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv =cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('Those whose fare was less than 50 survival rate: '+str(sv_rate))

# 9
file13 = open('/classes/ece2720/pe3/passengers.csv')
cnt = 0
cnt_sv = 0
cnt_dd = 0
for k in file13.readlines():
    if cnt == 0:
        cnt = cnt + 1
    else:
        if int(k.split(',')[7]) != 0:
            if int(k.split(',')[1]) == 0:
                cnt_dd = cnt_dd + 1
                cnt = cnt + 1
            else:
                cnt_sv = cnt_sv + 1
                cnt = cnt + 1
        else:
            continue
sv_rate = cnt_sv / float(cnt_dd + cnt_sv)
print('People traveling as part of a family survival rate: ' + str(sv_rate))

