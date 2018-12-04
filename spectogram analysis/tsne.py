from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


thres=250


a=Image.open('spec.jpeg')
a.load()
a=a.convert('L')
ar = np.asarray(a, dtype="int32" )
print(np.average(ar))
b=np.tanh(ar-np.average(ar))
c=b-np.min(b)
intensity=np.sum(np.exp(b),axis=0)
pixels=np.arange(ar.shape[1])
print(pixels)
print(pixels.shape,intensity.shape)

plt.scatter(pixels,intensity)
plt.show()

print(ar.shape)
print("================================")

data = [ [x,intensity[x] ] for x in pixels]
data=np.array(data, dtype='int64')
plt.bar(*np.transpose(data))


l={0}
co=0
coi=0
act=1
for a in data:
    if a[1]<300:
        if act!=0:
            act=0
            co=0
        co+=1
        coi+=a[0]
    else:
        act=1
        if co>5:   
            l.add(coi/co)
        co=0          
print(l)




dat=[[400,x] for x in l]



plt.bar(*np.transpose(dat),width=3)


plt.show()