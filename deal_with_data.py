import json
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "YOUR_KEY"
client = OpenAI()


def get_class(user_text):
    """
    从用户话语中选择用户想要什么物品（有备选答案list） ✅
    :param user_text: 用户发言
    :return: 筛选出来的类别
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
ユーザーの発言から最も買いたい商品を抽出してください。
商品リスト：
['スナック', 'ポテトチップス', '軽食', 'ビスケット', 'クッキー', 'クラッカー', '肉', '鶏肉', 'サラダチキン', 'ビーフ', 'ビーフジャーキー']
生成格式：
{
    ‘class’:从商品リスト中选择一个最符合用户想买的类别;
    ‘reply’:AI reply
}"""},
            {"role": "user", "content": 'ユーザー発言:「' + user_text['speech'] + '」\n商品リスト内のもの一つだけ抽出してください！'}
        ]
    )
    reply = response.choices[0].message.content
    return eval(reply)["class"]


def get_reco_list(classification, neo4j_db):
    """
    推荐list（3个）：只包含当前用户希望买的种类 ✅
    :param classification: 上一步检测出来的的类别
    :param neo4j_db: neo4j数据库
    :return: 重新编码过的推荐list
    """
    result = neo4j_db.search_reco_list(classification)
    reco_list = []
    for record in result:
        record_data = record.data()["node"]
        # 使用indent参数增加可读性
        # 同时改一下编码
        json_data = bytes(json.dumps(record_data, indent=2), 'utf-8').decode('unicode_escape')
        reco_list.append(json_data)
    return reco_list


def get_ai_reply(reco_list):
    """
    在KG查询之后将查询结果放在prompt中，让ChatGPT进行比较生成一段文字给用户 ✅
    :param reco_list: 推荐list（3个）
    :return: ChatGPT生成的一段文字
    """
    node_list = []
    for i in range(len(reco_list)):
        json_data = json.loads(reco_list[i].replace("\n", ""))
        node_info = {"node_id": json_data["node_id"],
                     "title": json_data["title"],
                     "introduce": json_data["introduce"],
                     "price": json_data["price"],
                     "star": json_data["star"],
                     "star_number": json_data["star_number"]}
        node_list.append(node_info)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"""
商品間の相違点とそれぞれの特徴（150字）を、下記の商品ノードの情報に基づいて論理的に比較してください
商品ノード
{node_list}"""},
            {"role": "user", "content": 'お願いします'}
        ]
    )
    reply = response.choices[0].message.content
    return reply


def get_other_reco(classification, classification_jp, neo4j_db):
    """
    其他推荐list（3个）：同属于一个大类的其他推荐 ✅
    :param classification: 用户想买的
    :param classification_jp: 用户想买的（日语）
    :param neo4j_db: neo4j数据库
    :return: 其他推荐list（3个）
    """
    result = neo4j_db.search_other_reco(classification, classification_jp)
    other_reco_list = []
    for record in result:
        record_data = record.data()["node"]
        # 使用indent参数增加可读性
        # 同时改一下编码
        json_data = bytes(json.dumps(record_data, indent=2), 'utf-8').decode('unicode_escape')
        other_reco_list.append(json_data)
    return other_reco_list


def get_page(neo4j_db):
    result = neo4j_db.search_page()
    detail_list = []
    for record in result:
        record_data = record.data()["node"]
        # 使用indent参数增加可读性
        # 同时改一下编码
        json_data = bytes(json.dumps(record_data, indent=2), 'utf-8').decode('unicode_escape')
        detail_list.append(json_data)
    return detail_list
