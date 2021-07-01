import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

mean= (np.mean(data))
dev= (np.std(data))
low=(mean - dev)
high =(mean + dev)
count= len([i for i in data if low < i and high > i])
print((count/data.size)*100)
