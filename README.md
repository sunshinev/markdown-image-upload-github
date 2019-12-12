
# Alfred Workflow 一键上传图片到github 
![](https://img.shields.io/badge/Mac-osx-brightgreen)
![](https://img.shields.io/badge/Alfred-workflow-brightgreen)
![GitHub last commit](https://img.shields.io/github/last-commit/sunshinev/markdown-image-upload-github)
![GitHub](https://img.shields.io/github/license/sunshinev/markdown-image-upload-github)
![GitHub repo size](https://img.shields.io/github/repo-size/sunshinev/markdown-image-upload-github)
![GitHub stars](https://img.shields.io/github/stars/sunshinev/markdown-image-upload-github?style=social)
![GitHub forks](https://img.shields.io/github/forks/sunshinev/markdown-image-upload-github?style=social)

有没有在写markdown时，因为想上传一张图片而苦恼？

现在可以直接截图后将图片上传到github，并且返回markdown格式的图片语法

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

## Fork 建议
### 能否支持其他git仓库呢？可以的

因为脚本的上传动作完全是由下面的git命令完成的，推送到远端仓库

```python
    # Git
    cmd = '''
    cd {}
    git add .
    git commit -m 'clipboard'
    git push'''.format(self.project_path)
```
所以我们只需要，保证`project_path`的仓库是支持git命令即可，比如可以提交到gitLab自己搭建的仓库等。

### 能否支持gif图片呢？
1. 目前Pillow不支持gif上传
2. 如果采用`Pyobjc`的`AppKit`模块中的`NSPasteboard`，会受到操作系统版本的影响，可能需要安装最新的Pyobjc

## 相关资料
[Using Variables in Workflows](https://www.alfredapp.com/help/workflows/advanced/variables/)

[Overview: What are workflows?](https://www.alfredapp.com/help/workflows/)

[《快速上传图片到七牛云空间kaito-kidd/markdown-image-alfred》](https://github.com/kaito-kidd/markdown-image-alfred) 
