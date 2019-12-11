# Alfred 一键上传图片到github

在编写markdown文件中，截图作说明，可以直接截图后将图片上传到github，并且返回markdown格式的图片语法

## 工作原理
通过`Alfred`的Workflow，设置Hotkey触发（默认`command + g`）。

## 支持图片类型
- JPG
- PNG

注意：Pillow模块不支持从剪贴板获取gif图片，所以目前不支持gif上传

## 安装

安装python的Pillow模块
```
pip install Pillow
```

下载Alfred的Workflow




## 使用说明

### 截取图片到剪贴板（微信截图、mac自带截图工具）
1. 截取图片到剪贴板
2. command+g

![image](https://github.com/sunshinev/remote_pics/raw/master/kapture-alfred.gif)

### 复制jpg、png文件

1. 复制图片文件
2. command+g


## 说明

相关原理借鉴了[《快速上传图片到七牛云空间kaito-kidd/markdown-image-alfred》](https://github.com/kaito-kidd/markdown-image-alfred) 
