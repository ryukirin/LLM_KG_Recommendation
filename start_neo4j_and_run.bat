@echo on

rem 启动Neo4j数据库
rem D:\neo4j\bin\neo4j换成你自己的neo4j路径
echo Starting Neo4j database...
start D:\neo4j\bin\neo4j console
echo Neo4j started successfully.

rem 等待一段时间，确保Neo4j数据库已经启动完成
timeout /t 5

rem 运行Python脚本
echo Running Python script...
rem 记得替换data_flask.py路径
start python data_flask.py
echo Python script completed successfully.

rem 打开HTML文件
echo Opening HTML file...
rem 记得替换HTML文件路径
start "" "frontend\index.html"
echo HTML file opened successfully.
