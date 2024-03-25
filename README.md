## 介绍

日语项目（但是注释是中文）

![image](https://github.com/ryukirin/LLM_KG_Recommendation/assets/47234906/90d4613a-9fa6-4a45-a3b2-f9e56167b098)

## 项目结构

```
.
├─ create_example.py # create KG
├─ database_operation.py
├─ data_flask.py
├─ deal_with_data.py
├─ start_neo4j_and_run.bat
└─ frontend
   ├─ index.html
   ├─ 聊天机器人.png
   ├─ img
   │  └─page's images
   ├─ css
   │  └─ style.css
   └─ js
      └─ index.js
```

## 必要环境

- [Neo4j](https://neo4j.com/)
- [flask](https://flask.palletsprojects.com/en/3.0.x/)
- python3 (需要在运行时 import ``py2neo`` ``flask`` ``flask_cors`` ``openai`` ``json``)

## 运行方法

1. 在 ``deal_with_data.py`` line 5 添加你的 OpenAI key 
2. 创建你的neo4j database并且将数据库信息添加到 ``data_flask.py`` line 9 to 11 和 ``create_example.py`` line 3 to 4
3. 创建 KG
   ```
   python create_example.py
   ```
4. 改变 ``start_neo4j_and_run.bat`` 中的Neo4j路径
5. 点击 ``start_neo4j_and_run.bat``

## 运行例

![image](https://github.com/ryukirin/LLM_KG_Recommendation/assets/47234906/8a3ed8f0-7df1-4dd4-b484-fe144a0631fb)

点击右下角机器人图标

![image](https://github.com/ryukirin/LLM_KG_Recommendation/assets/47234906/52c38dfe-a63f-43ff-9b9b-0b082950f1de)

## 关于数据

20个左右从Amazon上复制的（仅用于实验）
