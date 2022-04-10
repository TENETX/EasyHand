#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch 
from model import Model
import pandas as pd 
import numpy as np
from torch.utils.data import Dataset,DataLoader


# In[ ]:


#from google.colab import drive
#drive.mount('/content/drive')


# In[8]:


dev = torch.device('cuda:0' if torch.cuda.is_available() else "cpu")


# In[9]:


class data(Dataset):

    def __init__(self,path):
        self.dataset = np.array(pd.read_csv(path))
        self.map = {'old': 0, 'young': 1, 'man': 2, 'woman': 3, 'smile': 4, 'sad': 5, 'cartoon': 6, 'todo': 7, 'clear': 8, 'selfie': 9}

    def __getitem__(self,index):
        yvals = torch.tensor(self.map[self.dataset[index][0]], dtype=torch.long)
        xvals = torch.from_numpy(self.dataset[index][1:].astype(np.float32))
        return xvals,yvals

    def __len__(self):
        return self.dataset.shape[0]


# In[10]:


batch_size = 10
dataset = data('./dataset/dataset321.csv')
loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)
model = Model().to(dev)
loss_list = []
print(dev)


# In[12]:


epochs = 1000
lr = 0.000001
crit = torch.nn.CrossEntropyLoss()
opt = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.8)

for epoch in range(epochs):

    total_loss = 0
    
    for x,y in loader : 
        x = x.to(dev)
        y = y.to(dev)

        opt.zero_grad()
        yhat = model.forward(x)
        loss = crit(yhat,y)
        total_loss += loss
        loss.backward()
        opt.step()

    if epoch % 10 == 0 : 
        print('EPOCH : ', epoch)
        print('  |  Loss : ',total_loss.item(), end='')
        print()
        torch.save(model.state_dict(), f'./mymodels321/{epoch}.pt')

    loss_list.append(total_loss.item())

