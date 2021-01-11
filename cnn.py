from PIL import Image
import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, ZeroPadding2D, MaxPooling2D
from keras.optimizers import SGD

'''
   第一步：读取图片数据
   说明：这个过程需要安装pillow模块：pip install pillow
'''
##1张1通道的256*256的灰度图片
##data[0,0,0,0]：表示第一张图片的第一个通道的坐标为(0,0)的像素值
img_width, img_height = 256, 256
data = np.empty((1, 1, img_width, img_height), dtype="float32")
##打开图片
img = Image.open("D:\\hacker\\1.png")
##把图片转换成数组形式
arr = np.asarray(img, dtype="float32")
for i in 32:
    data[i, :, :, :] = arr


'''
    第二步：设置权重
    说明：注意最外围是5个方括号
'''
weights = [[[[[-1]], [[0]], [[1]]], [[[-2]], [[0]], [[2]]], [[[-1]], [[0]], [[1]]]]]
weights = np.array(weights)

'''
   第三步：组织卷积神经网络
   说明：
   1.因为实验采用的是默认的tensorflow后端，而输入图像是channels_first模式，所以注意data_format参数的设置
   2.为了实验的效果，所以strides、pool_size等参数设置成了1
'''

##第一次卷积
model = Sequential()
model.add(ZeroPadding2D(padding=(2, 2), data_format='channels_first', batch_input_shape=(1, 1, img_width, img_height)))
model.add(Convolution2D(filters=1, kernel_size=(3, 3), strides=(1, 1), activation='relu', name='conv1_1',
                        data_format='channels_first'))
model.set_weights(weights)

##第二次卷积
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(filters=1, kernel_size=(3, 3), strides=(1, 1), activation='relu', name='conv1_2',
                        data_format='channels_first'))
model.set_weights(weights)

##池化操作
model.add(ZeroPadding2D((0, 0)))
model.add(MaxPooling2D(pool_size=1, strides=None, data_format='channels_first'))

'''
   第四步： 设置优化参数并编译网络
'''

# 优化函数，设定学习率（lr）等参数
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# 使用mse作为loss函数
model.compile(loss='mse', optimizer=sgd, class_mode='categorical')

'''
    第五步：预测结果
'''
result = model.predict(data, batch_size=1, verbose=0)

'''
    第六步：保存结果到图片
'''
img_new = Image.fromarray(result[0][0]).convert('L')
img_new.save("D:\\hacker\\3.jpg")
