import py2neo


class NeoConn:

    def __init__(self, host, username, password, dbname):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__dbname = dbname
        self.__graph = None
        self.__node = None

    def __conn_rdf(self):
        try:
            self.__graph = py2neo.Graph(self.__host,
                                        auth=(self.__username, self.__password),
                                        name=self.__dbname)
            print("Neo4j connect success!")
        except py2neo.errors as e:
            print(e)

    def search_reco_list(self, classification):
        """
        :return: 推荐商品list
        """
        self.__conn_rdf()
        cql = f"""MATCH ({classification}:{classification})-[:`含む`*0..]->(subclass)
MATCH (subclass)<-[:is]-(node)
RETURN node
ORDER BY toInteger(node.star_number) DESC
LIMIT 3;"""
        node_list = self.__graph.run(cql)
        return node_list

    def search_other_reco(self, classification, classification_jp):
        """
        :param classification: 用户想买的
        :param classification_jp: 用户想买的（日语）
        :return: 其他推荐list
        """
        self.__conn_rdf()
        if classification not in ['snack', 'meat', 'light_meal']:
            cql = f"""MATCH ({classification}:{classification})<-[:`含む`]-(class)
MATCH (class)-[:`含む`*]->(subclass)
WHERE NOT (subclass)-[:`含む`]-({classification}:{classification}) and not subclass.name="{classification_jp}"
WITH subclass
MATCH (subclass)<-[:is]-(node)
RETURN node order by toInteger(node.star_number) limit 3"""
        else:
            cql = f"""MATCH ({classification}:{classification})-[:`含む`*]->(subclass)
MATCH (subclass)<-[:is]-(node)
RETURN node
ORDER BY toInteger(node.star_number) DESC
SKIP 3
LIMIT 3;"""
        node_list = self.__graph.run(cql)
        return node_list

    def search_page(self):
        """
        初始化页面
        :return: 评分最高的8个商品
        """
        self.__conn_rdf()
        cql = f"""MATCH (subclass)<-[:is]-(node)
RETURN node
ORDER BY toInteger(node.star_number) DESC
LIMIT 8;"""
        node_list = self.__graph.run(cql)
        return node_list
