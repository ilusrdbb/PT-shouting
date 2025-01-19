# PT-shouting

pt站自动喊话脚本  
感谢原作者[https://github.com/huoyart/PT-shouting](https://github.com/huoyart/PT-shouting)，由于两边代码风格差异过大干脆自己fork出了一份维护   
目前支持青蛙、大青虫、tosky，但是由于本人只有青蛙有号，其余站点如果出问题无法解决见谅  
频繁喊话会被ban号，请合理使用本工具，如果因为不规范使用导致账号问题概不负责  
本项目基于pycharm开发，开发环境为python 3.9  

## 使用说明
### Windows
解压release最新版本的压缩包，修改config.yaml配置文件，双击shouting.exe运行  
或使用Pyinstaller从源代码中打包，环境准备见下方Linux说明  
~~~bash
Pyinstaller -F shouting.py
~~~
### Linux
Linux下暂时需要从源代码运行  
安装python3环境，建议3.9及以上  
安装requirements.txt下依赖  
~~~bash
pip install -r requirements.txt
~~~
下载源代码  
~~~bash
git clone https://github.com/ilusrdbb/PT-shouting.git
~~~
修改config.yaml配置文件，运行  
~~~bash
python3 shouting.py &
~~~

## TODO
消息推送 对本人来说意义不大，如果有小伙伴强烈要求那有空再搞  
其他站点支持或代码优化 欢迎提pr  
如果出现bug欢迎提issue  