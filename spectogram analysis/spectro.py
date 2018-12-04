
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from PIL import Image
from scipy.spatial.distance import pdist, squareform

a=Image.open('spec.jpeg')
a.load()
a=a.convert('L')
ar = np.asarray(a, dtype="int32" )
c=ar-np.average(ar)
# c=np.arctan(c)

plt.imshow(a)

intensity=c
intensity=np.transpose(c)
intensity=np.asarray([np.abs(np.subtract(intensity[i],intensity[i-1])) for i in np.arange(1,intensity.shape[0])] )
# intensity=np.asarray([np.abs(np.subtract(intensity[i],intensity[i-1])) for i in np.arange(1,intensity.shape[0])] )
intensity=np.transpose(intensity)
print(intensity)
intensity=2*(np.average(intensity,weights=np.arange(ar.shape[0]),axis=0))

print(intensity.shape)
indexes=find_peaks(intensity,threshold=18)[0]
# plt.plot(indexes,[ intensity[i] for i in indexes])
plt.plot(intensity)




print(indexes.shape)

# print("================================")
# N=100
# print(pixels)
# data = [ [intensity[x],x] for x in pixels]
# data=np.array(data, dtype='int64')



# # generate 3 clusters of each around 100 points and one orphan point
# N=100
# # data = np.random.randn(3*N,2)
# # data[:N] += 5
# # data[-N:] += 10
# # data[-1:] -= 20
# print(data[:90])

# # clustering
# thresh = 30
# clusters = hcluster.fclusterdata(data, thresh, criterion="distance")
# print(clusters)
# # plotting
# plt.scatter(*np.transpose(data), c=clusters,s=9)
# plt.axis("equal")
# title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))


indexes=[np.abs((indexes[i]+indexes[i-1])/2) for i in np.arange(indexes.shape[0])]
print(indexes)
plt.bar(indexes,100,color='r')
# plt.title(title)
plt.show()