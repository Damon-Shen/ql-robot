# ql-robot
QQ控制青龙面板实现

原理：使用 nonebot 与 go-cqhttp 实现 QQ机器人

# 安装
1. 安装```python3.7```以上版本

2. 安装```nonebot```机器人
```
pip install nonebot
```
3. 下载安装```go-cqhttp```机器人，配置完成QQ机器人号码，反向连接地址为```ws://127.0.0.1:8090/ws/```

4. 下载本库，修改 ```config.py``` 文件中的```SUPERUSERS```为你使用的QQ号(非机器人账号)

# 使用
1. QQ登陆完成后，用你的管理员QQ号与机器人对话,目前仅支持青龙API对接，发送```青龙```后根据反馈填写对应内容，其中青龙地址需带```http(s)://```前缀

# 目前功能
1. 青龙基础对接完成，对接完毕后会在程序目录生成```config.sqlite```数据库文件，用于保存青龙信息

# 开发计划
1. 支持青龙环境变量 增加 修改 删除
2. 支持青龙定时任务 增加 修改 删除 执行
3. 支持青龙拉库或单拉文件
4. 支持指定青龙任务信息一对一或一对多推送
5. 支持对接淘宝，京东，拼多多返利，比价接口对接

# 插件
本程序所有更新后续基于插件形式，在```awesome\plugins```目录下放入插件文件即可使用
