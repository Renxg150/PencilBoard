import numpy as np
import torch
from PIL import Image
from torch import nn, optim
from torch.autograd import Variable
from torchvision import datasets, transforms


# 定义网络结构
# 不是le-net5的结构
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Sequential表示在搭建网络模型中要执行的一系列的步骤
        # Dropout中,p=0.5表示50%的神经元不工作
        # layer3:输出层 一般输出层中不需要加Dropout
        # Conv2d Conv:卷积 2d:表示2维的卷积
        # nn.Conv2d的几个参数
        # 1：输入通道数：1表示黑白的图片 彩色的话就是3
        # 32：输出通道数：表示要生成多少个特征图
        # 5:是卷积核的大小，(5,5)表示是5*5的窗口。可以只写一个5
        # 1表示步长。步长默认值就是1
        # 2表示在padding外面填2圈0 这个相当于samepadding
        # nn.MaxPool2d的几个参数
        # 第一个2是池化的窗口的大小是2*2 第二个2表示步长为2
        self.conv1 = nn.Sequential(nn.Conv2d(1, 32, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2, 2))
        self.conv2 = nn.Sequential(nn.Conv2d(32, 64, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2, 2))
        self.fc1 = nn.Sequential(nn.Linear(64 * 7 * 7, 1000), nn.Dropout(p=0.5), nn.ReLU())
        self.fc2 = nn.Sequential(nn.Linear(1000, 10), nn.Softmax(dim=1))
        # dim=1代表对第一个维度，计算概率值
        # 因为batch = 64
        # 所以fc1输出的是（64,10）
        # 所以dim=1，表示对第二个维度进行softmax求值

    def forward(self, x):
        # ([64,1,28,28])变成2维的数据->(64,784) 全连接层做计算，必须是2维的数据
        # x = x.view(x.size()[0],-1)
        # 但是卷积只能对四维的数据进行计算 ([64,1,28,28])
        # 64表示批次的数量，1表示通道数 28表示长宽
        x = self.conv1(x)
        x = self.conv2(x)

        # 将原来x四维的数据，改变为2维的数据
        # (64,64,7,7)
        x = x.view(x.size()[0], -1)

        x = self.fc1(x)
        x = self.fc2(x)
        return x

def onehot_to_num(onehot:torch.Tensor):
    list1 = onehot.detach().numpy()
    list1 = list1[0]
    for index,value in enumerate(list1):
        if value > 0.5:
            return index


if __name__ == '__main__':
    the_model = Net()  # 定义模型
    the_model.load_state_dict(torch.load("model_parameters/parame"))  # 读取参数
    # image =
    im1 = Image.open('111.png').convert("L")
    im2 = im1.copy()
    im2.thumbnail((28,28))
    # im2.save('222.png')
    # print("im1的大小：",im1.size)
    # print("im2的大小：",im2.size)
    im2 = 255 - np.array(im2)
    im2 = im2/255
    # for i in im2:
    #     print(i)
    im2 = torch.Tensor(im2)
    im2 = im2.view(1,1,28,28)
    # im2 = Variable(im2)
    result = the_model(im2)
    print(result)
    print(onehot_to_num(result))