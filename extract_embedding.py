import faiss
import numpy as np

EMB_DIM = 256


embeds = np.load('embed.npy')
labels = np.load('label.npy')

index = faiss.IndexFlatIP(EMB_DIM)
index.add(embeds)

D, I = index.search(embeds, k=3)

print(D.shape)
print(I.shape)