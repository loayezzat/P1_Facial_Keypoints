## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 32, 3 , padding = 1 )
        self.batch1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, 3, padding = 1 )
        self.batch2 = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 128, 3, padding = 1 )
        self.batch3 = nn.BatchNorm2d(128)
        self.conv4 = nn.Conv2d(128, 256, 3, padding = 1 )
        self.batch4 = nn.BatchNorm2d(256)
        self.pool =  nn.MaxPool2d(2, 2)    
        self.dropout = nn.Dropout(0.3)
        
        self.fc1 = nn.Linear(256 *14*14,1024)
        self.fc2 = nn.Linear(1024,136)
        
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        batch_size = x.shape[0]
        x = self.pool(self.batch1(F.relu(self.conv1(x))))
        x = self.pool(self.batch2(F.relu(self.conv2(x))))
        x = self.pool(self.batch3(F.relu(self.conv3(x))))
        x = self.pool(self.batch4(F.relu(self.conv4(x))))
        x = x.view (batch_size, -1)
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.fc2(x)
        # a modified x, having gone through all the layers of your model, should be returned
        return x
