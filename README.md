
# Alfred Workflow 一键上传图片到github 
![](https://img.shields.io/badge/Mac-osx-brightgreen)
![](https://img.shields.io/badge/Alfred-workflow-brightgreen)
![](https://img.shields.io/badge/Markdown-Github-brightgreen)


> 在编写markdown文件中，截图作说明，可以直接截图后将图片上传到github，并且返回markdown格式的图片语法
> 
> https://github.com/sunshinev/markdown-image-upload-github

**注意**：Pillow模块不支持从剪贴板获取gif图片，所以目前不支持gif上传

![image](https://github.com/sunshinev/remote_pics/raw/master/kapture-alfred.gif)

## 运行环境

Alfred + Mac  

## 支持图片类型
- JPG
- PNG

## 工作原理
1. 使用Alfred热键功能触发Workflow工作流程，执行Python脚本。
2. 使用Pillow模块从剪贴板Clipboard中获取`jpg/png`图片文件，并且移动到`project_path`目录下
3. 提交`project_path`目录下的文件到github仓库

## 安装

安装python的Pillow模块
```
pip install Pillow
```

下载Alfred的Workflow并打开安装

[下载Markdown-image-upload-github](https://github.com/sunshinev/markdown-image-upload-github/raw/master/alfred_workflow/Markdown%20image%20upload%20github.alfredworkflow)

## 配置
打开Alfred的Workflow配置脚本的变量

|     配置项      |        说明        |
|-----------------|--------------------|
| github_repo     | 图床仓库名称       |
| github_username | 用户名             |
| project_path    | 本地的图床项目路径 |

**注意**：请先确保`project_path`对应的`Github`项目可以正常使用git命令操作

![image](https://github.com/sunshinev/remote_pics/raw/master/kapture-alfred2.gif)


## 上传图片
上传图片支持两种方式，一种是截取图片到剪贴板、另外一种是直接复制图片文件

### 截取图片到剪贴板（微信截图、mac自带截图工具）
1. 截取图片到剪贴板
2. command+g

### 复制jpg、png文件

1. 复制图片文件
2. command+g


## 说明

相关原理借鉴了[《快速上传图片到七牛云空间kaito-kidd/markdown-image-alfred》](https://github.com/kaito-kidd/markdown-image-alfred) 
