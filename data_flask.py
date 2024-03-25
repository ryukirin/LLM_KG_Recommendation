from flask import Flask, request, jsonify
import deal_with_data
import database_operation
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
HOST = "http://localhost:7474"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
DBNAME = "DBNAME"
my_neo4j = database_operation.NeoConn(HOST, USERNAME, PASSWORD, DBNAME)
message_get = {}
classification_dic = {'スナック': 'snack', 'ビスケット': 'biscuit', 'クッキー': 'cookie', 'クラッカー': 'cracker',
                      '軽食': 'light_meal', '鶏肉': 'chicken', '肉': 'meat', 'ビーフ': 'beef', 'ポテトチップス': 'chips',
                      'ビーフジャーキー': 'beef_jerky', 'サラダチキン': 'chicken_salad'}


@app.route('/send_speech', methods=['POST'])
def send_speech():
    """
    receive the POST request
    :return: text to remind that get message
    """
    global message_get
    message_get = request.get_json()
    print(f"Got user speech:{message_get}")
    return message_get


@app.route('/get_reply', methods=['GET'])
def get_reply():
    """
    在这个函数里我希望能实现

    1. ChatGPT实现部分
        1.1 从用户话语中选择用户想要什么物品（有备选答案list） ✅

        1.2 在KG查询之后将查询结果放在prompt中，让ChatGPT进行比较生成一段文字给用户 ✅
    2. KG实现部分
        根据ChatGPT提取出来的物品类别，从KG中提取出两个list，一个是需要交予ChatGPT进行比较的推荐list，一个是直接显示的其他推荐list

        2.1 推荐list（3个）：只包含当前用户希望买的种类 ✅ → 检索出来之后交给ChatGPT进行比较

        2.2 其他推荐list（3个）：同属于一个大类的其他推荐 ✅

    步骤：1.1 → 2.1 & 2.2 → 1.2 → [2.1+1.2+2.2] send to frontend
    """
    """
    deal and send data
    :return: reply and data for white board using json format
    """
    global message_get
    print(f"Now the speech is {message_get}")
    print("Start getting classification...")
    classification_jp = deal_with_data.get_class(message_get)
    print(f"Done! The classification is {classification_jp}.")
    print("Start searching recommend list from KG...")
    classification = classification_dic[classification_jp]
    reco_list = deal_with_data.get_reco_list(classification, my_neo4j)
    print("Done! Now is searching other recommend list from KG...")
    other_reco_list = deal_with_data.get_other_reco(classification, classification_jp, my_neo4j)
    print("Done! Now is asking for AI...")
    reply = deal_with_data.get_ai_reply(reco_list)
    print(f"AI:{reply}")
    print("Done! Now is sending reply to user...")
    message_json = {"reco_list": reco_list,
                    "other_reco_list": other_reco_list,
                    "reply": reply}
    print("Done!🎉")
    return jsonify(message_json)


@app.route('/get_data', methods=['GET'])
def get_data():
    print("Initializing page...")
    detail_list = deal_with_data.get_page(my_neo4j)
    print("Done!")
    return jsonify(detail_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
