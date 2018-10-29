# Pan He——【ICCV2017】Single Shot Text Detector With Regional Attention

## 作者和代码    

[caffe检测torch7识别代码](https://github.com/MhLiao/TextBoxes_plusplus)

## 关键词

文字检测，多方向，SSD

## 方法亮点

- 

## 方法概述

本文方法是对TextBoxes（水平文字检测）进行改进，用于**多方向文字检测**。和SSD一样，该方法是one-stage的



## 方法细节

##### 网络结构

##### 其他细节点

- default box的aspect ratio从1,2,3,5,7 换成1,2,3,5,$\frac{1}{2}$,$\frac{1}{3}$,$\frac{1}{5}$
- 

## 实验结果

- ICDAR13

- 速度

## 总结与收获

这篇和其他水平转倾斜方法进行改进的文章相比，细节介绍的比较有趣，增加boundingbox的regression loss思路也很直观（监督信息越多，效果应该是会越好）。







