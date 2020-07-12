"""
author: Allyson Vasquez
date: July.3.2020

Collect UNCC student statistics & visualize data onto horizontal bar plot
"""
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
header = []
data = []

# Retrieve page & data
url = 'https://admissions.uncc.edu/about-unc-charlotte/university-profile'
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

for index in soup.find_all("tbody"):
    data = index.text

# Parse data
data = data.split('\n')
data[:] = [x for x in data if x != '']
for index, element in enumerate(data):
    if index % 2 == 0:
        header.append(element)
data = data[1::2]
data = [i.split('+')[0] for i in data]
data = [i.replace(',', "") for i in data]
data = np.array(data)

# Create series
uncc_series = pd.Series(data, index=header)
uncc_series = uncc_series.drop(index=['Gender ratio:', 'Student/Faculty ratio:'])
uncc_series = uncc_series.astype(int)
print(uncc_series)

# Plot data
uncc_series.plot(kind='barh', fontsize=10, color='#6E4BBF')
plt.title('UNCC Statistics', fontsize=35)
plt.xlabel('Values', fontsize=15)
plt.ylabel('Categories', fontsize=15)

fig = plt.gcf()
fig.set_size_inches(40, 20, forward=True)
plt.savefig('uncc_data.png', dpi=100)
# uncc_series.show()