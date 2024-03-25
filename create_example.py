from py2neo import Node, Relationship, Graph

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

graph = Graph('http://localhost:7474', auth=(USERNAME, PASSWORD), name='test')

graph.delete_all()

# add node

# 类别
# 弃用 node_food = Node('food', name='食品')
node_snack = Node('snack', name='スナック')
node_biscuit = Node('biscuit', name='ビスケット')
node_cookie = Node('cookie', name='クッキー')
node_cracker = Node('cracker', name='クラッカー')
node_light_meal = Node('light_meal', name='軽食')
node_chicken = Node('chicken', name='鶏肉')
node_meat = Node('meat', name='肉')
node_beef = Node('beef', name='ビーフ')
node_chips_potato = Node('chips', name='ポテトチップス')
node_beef_jerky = Node('beef_jerky', name='ビーフジャーキー')
node_chicken_salad = Node('chicken_salad', name='サラダチキン')

# 商品名
node_1 = Node(node_id='cookie01',
              title='オートミール×おからのグルテンフリークッキー『FruOats（フルオーツ）』30枚入り／ドライフルーツ5種×6枚 '
                    '食物繊維1/2日分 糖質・脂質・カロリーオフ 100%植物由来素材使用 おからクッキー オートミールクッキー オーツ麦 '
                    'お菓子 おやつ ヴィーガン プラントベース チアシード アマニ 糖質オフ 低糖質 白砂糖不使用',
              url='https://www.amazon.co.jp/%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9F%E3%83%BC%E3%83%AB%C3%97%E3%81%8A%E3%'
                  '81%8B%E3%82%89%E3%81%AE%E3%82%B0%E3%83%AB%E3%83%86%E3%83%B3%E3%83%95%E3%83%AA%E3%83%BC%E3%82%AF%E3%'
                  '83%83%E3%82%AD%E3%83%BC%E3%80%8EFruOats%EF%BC%88%E3%83%95%E3%83%AB%E3%82%AA%E3%83%BC%E3%83%84%EF%BC%'
                  '89%E3%80%8F30%E6%9E%9A%E5%85%A5%E3%82%8A%EF%BC%8F%E3%83%89%E3%83%A9%E3%82%A4%E3%83%95%E3%83%AB%E3%'
                  '83%BC%E3%83%845%E7%A8%AE%C3%976%E6%9E%9A-%E7%B3%96%E8%B3%AA%E7%B4%8465-%E3%82%AA%E3%83%95-100-%E6%'
                  'A4%8D%E7%89%A9%E7%94%B1%E6%9D%A5%E7%B4%A0%E6%9D%90%E4%BD%BF%E7%94%A8-%E3%81%8A%E3%81%8B%E3%82%89%E3%'
                  '82%AF%E3%83%83%E3%82%AD%E3%83%BC-%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9F%E3%83%BC%E3%83%AB%E3%82%AF%E3%'
                  '83%83%E3%82%AD%E3%83%BC/dp/B09CYY2JG1/ref=sr_1_1_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%'
                  '8A&crid=ZQQKUIFQDL5Z&keywords=%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC&qid=1706149576&sprefix=%E3%82%AF%'
                  'E3%83%83%E3%82%AD%E3%83%BC%2Caps%2C171&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
              brand='フルオーツ', price='3,380(113/枚)',
              introduce='✅1日に必要な食物繊維1/2入り！（約10g） '
                        '✅健康、美容効果の高い「オートミール」「おからパウダー」「チアシード」「アマニ」などの植物由来のスーパーフードを使用'
                        '✅バター、卵、小麦粉、白砂糖、人工甘味料、保存料不使用 '
                        '✅通常のクッキーより糖質約47%オフ！食物繊維は約20倍！（※｢日本食品標準成分表2020年版（八訂）｣ ソフトクッキー比較）'
                        '✅5種類のフレーバー（ストロベリーピスタチオ、マンゴーココナッツ、イチジクアーモンド、アップルシナモン、オレンジチョコレート）',
              star='4.1', star_number='397', classification='cookie')
node_2 = Node(node_id='cookie02',
              title='BASE Cookies ベースクッキー クッキー5種 '
                    '14袋（さつまいも4袋・ココナッツ4袋・ココア2袋・抹茶2袋・アールグレイ2袋）完全栄養食 食物繊維 低糖質 高たんぱく質',
              url='https://www.amazon.co.jp/Cookies-%E3%83%99%E3%83%BC%E3%82%B9%E3%82%AF%E3%83%83%E3%82%AD%E3%83%'
                  'BC-%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC5%E7%A8%AE-14%E8%A2%8B%EF%BC%88%E3%81%95%E3%81%A4%E3%81%'
                  'BE%E3%81%84%E3%82%824%E8%A2%8B%E3%83%BB%E3%82%B3%E3%82%B3%E3%83%8A%E3%83%83%E3%83%844%E8%A2%8B%'
                  'E3%83%BB%E3%82%B3%E3%82%B3%E3%82%A22%E8%A2%8B%E3%83%BB%E6%8A%B9%E8%8C%B62%E8%A2%8B%E3%83%BB%E3%'
                  '82%A2%E3%83%BC%E3%83%AB%E3%82%B0%E3%83%AC%E3%82%A42%E8%A2%8B%EF%BC%89%E5%AE%8C%E5%85%A8%E9%A3%'
                  '9F-%E9%AB%98%E3%81%9F%E3%82%93%E3%81%B1%E3%81%8F%E8%B3%AA/dp/B0B281BGQ4/ref=sr_1_2_sspa?'
                  'crid=2CZHOIT3EJV23&keywords=%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC&qid=1706150642&sprefix=%2Caps%'
                  '2C185&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
              brand='ベースフード', price='3,330(238/袋)',
              introduce='【BASE Cookies】26種のビタミン＆ミネラル、約7gのたんぱく質 、食物繊維など 、からだに必要な栄養素がぎゅっとつまった完全栄養食の低糖質クッキー '
                        '【33種類の栄養素】ビタミンやミネラル、タンパク質、食物繊維など欠かせない栄養素33種類を凝縮 '
                        '【たんぱく質】1食4袋で27.6ℊ配合 '
                        '【様々なシーンで】忙しい朝の朝食としても、栄養が足りていない時の栄養補給にも、トレーニング時の栄養補給にも最適 '
                        '【5種類の味】さつまいも、ココナッツ、ココア、抹茶、アールグレイ '
                        '【安心の品質】合成保存料、合成着色料不使用で安心',
              star='4.1', star_number='298', classification='cookie')
node_3 = Node(node_id='cookie03',
              title='うの花クッキー ビスケットタイプ 1kg×2セット（1袋250g×8袋）ダイエットクッキー 豆乳おからクッキー',
              url='https://www.amazon.co.jp/%E3%82%A8%E3%82%B9%E3%83%93%E3%83%BC%E3%82%B7%E3%83%BC-ONLINE-%E3%83%93%'
                  'E3%82%B9%E3%82%B1%E3%83%83%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97-1kg%EF%BC%881%E8%A2%8B250g%C3%974%'
                  'E8%A2%8B%EF%BC%89%E3%83%80%E3%82%A4%E3%82%A8%E3%83%83%E3%83%88%E3%82%AF%E3%83%83%E3%82%AD%E3%83%'
                  'BC-%E8%B1%86%E4%B9%B3%E3%81%8A%E3%81%8B%E3%82%89%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC/dp/B07M9QVVHY/'
                  'ref=sr_1_3_sspa?crid=2CZHOIT3EJV23&keywords=%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC&qid=1706150642&'
                  'sprefix=%2Caps%2C185&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1',
              brand='エスビーシー', price='5,443(680/袋)',
              introduce='うの花クッキーがさらに美味しくなって新登場！ '
                        'ビスケットタイプだから、うの花クッキーより低脂肪・低カロリー　白砂糖や卵、バター不使用 '
                        '国産原料使用で大豆イソフラボンや食物繊維がたっぷり '
                        'おからの満腹感で、1日1食置き換えダイエットをしっかりサポート！',
              star='4.0', star_number='424', classification='cookie')
node_4 = Node(node_id='cookie04',
              title='薬膳 おからクッキー ダイエット 低カロリー 生おから 国産大豆 イヌリン入り 食物繊維 菊芋 お菓子 おやつ 1袋約25枚入り [1個セット]',
              url='https://www.amazon.co.jp/%E3%81%8A%E3%81%8B%E3%82%89%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC-%E3%83%80%'
                  'E3%82%A4%E3%82%A8%E3%83%83%E3%83%88-%E4%BD%8E%E3%82%AB%E3%83%AD%E3%83%AA%E3%83%BC-%E3%82%A4%E3%83%'
                  '8C%E3%83%AA%E3%83%B3%E5%85%A5%E3%82%8A-1%E8%A2%8B%E7%B4%8425%E6%9E%9A%E5%85%A5%E3%82%8A/dp/'
                  'B0BJ6CTRSK/ref=sr_1_4_sspa?crid=2CZHOIT3EJV23&keywords=%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC&'
                  'qid=1706150642&sprefix=%2Caps%2C185&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1',
              brand='めぐりこまち', price='1,840(1,840/袋)',
              introduce='【薬膳おからクッキーの3つこだわり】'
                        '[薬膳スーパーフード"菊芋"]"菊芋"に豊富に含まれるイヌリンは、善玉菌のエサとなる水溶性食物繊維です。ダイエットをサポートします。'
                        '[100%国産"生おから"]100％国産大豆の新鮮な「生おから」を使用しています。'
                        'おからは低カロリーでありながら、タンパク質、カルシウム、食物繊維などの栄養が豊富です。ダイエット中に最適な嬉しい食材です。'
                        '[良質なコラーゲン＆ココナッツオイル]ココナツオイルは燃焼をサポートするアディポネクチンとラウリン酸が含まれております。'
                        '時短でエネルギーに変わりやすい特徴があります。コラーゲンペプチドを使用することで、ココナッツオイルをしっかりと吸収することができます。',
              star='4.0', star_number='43', classification='cookie')
node_5 = Node(node_id='cookie05',
              title='神戸トラッドクッキー クッキー詰め合わせ / 個包装で39枚入り 一口サイズで女性にもおすすめのサイズ / '
                    'ココナッツ・紅茶・チョコアーモンド・カフェキャラメル・モザイク・プレーン / TC-15N',
              url='https://www.amazon.co.jp/%E7%A5%9E%E6%88%B8%E3%83%88%E3%83%A9%E3%83%83%E3%83%89%E3%82%AF%E3%83%83%E3'
                  '%82%AD%E3%83%BC-%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC%E8%A9%B0%E3%82%81%E5%90%88%E3%82%8F%E3%81%'
                  '9B-%E5%80%8B%E5%8C%85%E8%A3%85%E3%81%A742%E6%9E%9A%E5%85%A5%E3%82%8A-%E4%B8%80%E5%8F%A3%E3%82%'
                  'B5%E3%82%A4%E3%82%BA%E3%81%A7%E5%A5%B3%E6%80%A7%E3%81%AB%E3%82%82%E3%81%8A%E3%81%99%E3%81%99%'
                  'E3%82%81%E3%81%AE%E3%82%B5%E3%82%A4%E3%82%BA-%E3%82%B3%E3%82%B3%E3%83%8A%E3%83%83%E3%83%84%E3%83%BB%'
                  'E7%B4%85%E8%8C%B6%E3%83%BB%E3%83%81%E3%83%A7%E3%82%B3%E3%82%A2%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%89%'
                  'E3%83%BB%E3%82%AB%E3%83%95%E3%82%A7%E3%82%AD%E3%83%A3%E3%83%A9%E3%83%A1%E3%83%AB%E3%83%BB%E3%83%A2%'
                  'E3%82%B6%E3%82%A4%E3%82%AF%E3%83%BB%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%C3%97%E5%90%847%E6%9E%9A/dp/'
                  'B084LC84TF/ref=sr_1_5?crid=2CZHOIT3EJV23&keywords=%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC&'
                  'qid=1706150642&sprefix=%2Caps%2C185&sr=8-5',
              brand='神戸浪漫', price='1,700(40/個)',
              introduce='女性でもお召し上がりやすいサイズのクッキーです。６種類のクッキーが計39枚入っており、ちょっとした手土産や返礼品にもおすすめです。<br/>'
                        'サクサクした食感がくせになる神戸トラッドクッキーは伝統的な手法でていねいに焼き上げたオーソドックスな焼き菓子です。<br/>'
                        '来客用お茶菓子にもおすすめのクッキーです。6種類の味と食感をお楽しみください。',
              star='4.0', star_number='240', classification='cookie')
node_6 = Node(node_id='cracker01',
              title='ナビスコ プレミアム オリジナル クラッカー 241g×3',
              url='https://www.amazon.co.jp/%E3%83%8A%E3%83%93%E3%82%B9%E3%82%B3-%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%'
                  'E3%83%A0-%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB-%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%'
                  'BC-241g%C3%973/dp/B07BFJ2Y5B/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&'
                  'crid=2QH6D1JH6O3SO&keywords=%E3%82%BD%E3%83%BC%E3%83%80%E3%82%AF%E3%83%A9%E3%83%83%E3%82%'
                  'AB%E3%83%BC&qid=1706154545&sprefix=%E3%82%BD%E3%83%BC%E3%83%80%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%'
                  'E3%83%BC%2Caps%2C177&sr=8-5',
              brand='ナビスコ', price='1,790(248/100g)',
              introduce='ナビスコ プレミアムクラッカー 業務用<br/>'
                        '軽い塩味のプレーンクラッカー。 サクッと広がる贅沢なコクと香りです。<br/>'
                        '内容量 241gx3個',
              star='4.0', star_number='160', classification='cracker')
node_7 = Node(node_id='cracker02',
              title='【 低糖質おやつ 】 ZENB ゼンブ チップス 10袋 クラッカー 豆チップス '
                    '[ 低糖質 グルテンフリー 糖質オフ 糖質制限 糖質コントロール 置き換え ダイエット 時の食物繊維補給に たんぱく質 食物繊維 鉄分 ]',
              url='https://www.amazon.co.jp/ZENB-%E3%83%81%E3%83%83%E3%83%97%E3%82%B9-%E7%B3%96%E8%B3%AA%E3%82%AA%'
                  'E3%83%95-%E7%B3%96%E8%B3%AA%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%AB-%E3%82%B0%E3%'
                  '83%AB%E3%83%86%E3%83%B3%E3%83%95%E3%83%AA%E3%83%BC/dp/B0BWDH2SPD/ref=sr_1_1_sspa?__mk_ja_JP=%E3%'
                  '82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=IFBIC50JVJCE&keywords=%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%'
                  'E3%83%BC&qid=1706155314&sprefix=%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC%2Caps%2C180&'
                  'sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
              brand='ZENB', price='4,080(408/袋)',
              introduce='☕植物由来の素材でつくった低糖質※の豆チップス：'
                        'うす皮までまるごと使った黄えんどう豆にオリーブオイルを加えて丁寧に焼き上げ、味付けは岩塩だけで仕上げたシンプルなおいしさの豆クラッカー（ゼンブチップス）。'
                        '小麦不使用のグルテンフリー※1で素材本来のおいしさが味わえます。'
                        '※ ゼンブチップス1袋あたり糖質10g ※1本品は「グルテンフリー」ですが、小麦アレルギーの方に対応するものではありません。 '
                        '☕ノンフライのヘルシー豆チップス：高温かつ短時間で焼き上げることで、豆の香ばしい香りを引き出し、パリッとサクッとした食感が、また食べたくなる味わいです。 '
                        '☕低糖質、食物繊維たっぷり※2 ：いつものクラッカーよりたんぱく質1.6倍、食物繊維5.9倍、糖質30%オフ、塩分50%オフ、鉄分5倍(※2)。'
                        '※2：日本食品標準成分表2020年版（八訂）オイルスプレークラッカーとソーダクラッカーの平均値との比較。'
                        'チップス100gあたり たんぱく質 15.62g,食物繊維 12.46g、糖質 41.8g、食塩相当量 0.8g、鉄分 3.91mg '
                        '☕こんな方におすすめ：小腹がすいたときにちょっとつまみたいけど、糖質を控えたい、'
                        'おつまみも健康を考えてグルテンフリーの食品を食べたい、食物繊維不足が気になる、たんぱく質を摂りたい。'
                        '普段、糖質オフや低糖質のおやつ、こんにゃくチップス、おからクッキー、ロカボ（ローカーボ）商品、ダイエット食品や置き換えダイエット食品などを食べている方。'
                        '置き換えダイエット（おきかえダイエット）やダイエットをしていて食物繊維を取りたい方。プラント ベースフード（植物由来の食品）をお探しの方。'
                        '大豆ライス ( ダイズライス ) を食べている方。小腹がすいた時に食べる 食べ物をお探しの方。 *置き換えとはいつもの食事を別のものに変更すること '
                        '☕食事がちゃんととれていない方や糖質制限したい方、小さなお子様がいる方におすすめです。 ',
              star='3.5', star_number='49', classification='cracker')
node_8 = Node(node_id='cracker03',
              title='【まとめ買い】前田製菓 10種類の野菜クラッカー(5枚×6袋入)×2箱',
              url='https://www.amazon.co.jp/%E5%89%8D%E7%94%B0%E8%A3%BD%E8%8F%93-%E3%80%90%E3%81%BE%E3%81%A8%E3%82%81%'
                  'E8%B2%B7%E3%81%84%E3%80%91%E5%89%8D%E7%94%B0%E8%A3%BD%E8%8F%93-10%E7%A8%AE%E9%A1%9E%E3%81%AE%E9%87%'
                  '8E%E8%8F%9C%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC-5%E6%9E%9A%C3%976%E8%A2%8B%E5%85%A5-%C3%'
                  '972%E7%AE%B1/dp/B08NHFD2VX/ref=sr_1_4_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&'
                  'crid=IFBIC50JVJCE&keywords=%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC&qid=1706155314&'
                  'sprefix=%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC%2Caps%2C180&sr=8-4-spons&'
                  'sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
              brand='前田製菓', price='1,048(17/個)',
              introduce='【まとめ買い】前田製菓 10種類の野菜クラッカー(5枚×6袋入)×2箱 野菜を10種類も練り込んだ、健康志向なあなたにオススメのクラッカー。 '
                        '2袋でレタス半個分の食物繊維を含みます。香料・着色料を使用せずに焼き上げた、野菜本来の味をお楽しみください。'
                        '<10種類の野菜>たまねぎ・赤ピーマン・パセリ・ごぼう・じゃがいも・かぼちゃ・モロヘイヤ・トマト・ほうれん草・にんじん',
              star='3.9', star_number='35', classification='cracker')
node_9 = Node(node_id='cracker04',
              title='森永製菓 小麦胚芽のクラッカー 64枚×4個',
              url='https://www.amazon.co.jp/%E6%A3%AE%E6%B0%B8%E8%A3%BD%E8%8F%93-%E5%B0%8F%E9%BA%A6%E8%83%9A%E8%8A%BD%'
                  'E3%81%AE%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC-64%E6%9E%9A%C3%974%E5%80%8B/dp/B0B1T4RYHV/'
                  'ref=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=IFBIC50JVJCE&keywords=%E3%82%AF%'
                  'E3%83%A9%E3%83%83%E3%82%AB%E3%83%BC&qid=1706155314&sprefix=%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%'
                  'E3%83%BC%2Caps%2C180&sr=8-6',
              brand='森永乳業', price='1,192(298/袋)',
              introduce='小麦胚芽入りで食物繊維を手軽においしく摂れる、食べやすいサイズのクラッカー。'
                        'そのまま食べるのはもちろん、チーズなどとの相性も抜群です '
                        '原材料・成分 小麦粉(国内製造)、小麦胚芽、ショートニング、植物油脂、砂糖、小麦ふすま、脱脂粉乳、'
                        '食塩、調味パウダー( 大豆・鶏肉・豚肉を含む)、モルトエキス/膨脹剤、乳化剤',
              star='4.5', star_number='172', classification='cracker')
node_10 = Node(node_id='cracker05',
               title='ブルボン プレーンクラッカーS 30枚×5箱',
               url='https://www.amazon.co.jp/%E3%83%96%E3%83%AB%E3%83%9C%E3%83%B3-%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%'
                   'E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%BCS-30%E6%9E%9A%C3%975%E7%AE%B1/dp/B06WP2KY4W/'
                   'ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=IFBIC50JVJCE&keywords=%E3%82%AF%E3%'
                   '83%A9%E3%83%83%E3%82%AB%E3%83%BC&qid=1706155314&sprefix=%E3%82%AF%E3%83%A9%E3%83%83%E3%82%AB%E3%83%'
                   'BC%2Caps%2C180&sr=8-5',
               brand='ブルボン', price='879(35/袋)',
               introduce='国産小麦を80%(小麦粉中)使用し、じっくり発酵させて焼きあげた、食べやすい形状のクラッカーです。'
                         '小麦のおいしさを感じられる、シンプルな味わいに仕上げました。'
                         'スリムな長方形にすることで、オードブルのようにクラッカーの上にトッピングする際にも食べやすい形状となっています。'
                         '1個装は6枚入りで、パーソナルユースからパーティーユースまで使い勝手の良い仕様です。',
               star='4.2', star_number='244', classification='cracker')
node_11 = Node(node_id='chips01',
               title='湖池屋 ポテトチップス 金のコンソメ 60g✕12袋',
               url='https://www.amazon.co.jp/%E6%B9%96%E6%B1%A0%E5%B1%8B-530247-%E3%83%9D%E3%83%86%E3%83%88%E3%83%81'
                   '%E3%83%83%E3%83%97%E3%82%B9-%E3%83%AA%E3%83%83%E3%83%81%E3%82%B3%E3%83%B3%E3%82%BD%E3%83%A1-60g'
                   '%C3%9712%E8%A2%8B/dp/B07BCHQLW2/ref=sr_1_4_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A'
                   '&crid=112Q0IEGUQZLY&keywords=%E3%83%9D%E3%83%86%E3%83%88%E3%83%81%E3%83%83%E3%83%97%E3%82%B9&qid'
                   '=1706156057&sprefix=%E3%83%9D%E3%83%86%E3%83%88%E3%83%81%E3%83%83%E3%83%97%E3%82%B9%2Caps%2C184'
                   '&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
               brand='湖池屋', price='1,624(226/100g)',
               introduce='湖池屋のポテトチップスは、国内産のじゃがいも100%で出来ております。<br/>あえて少し皮を残したことで、じゃがいも本来の風味やおいしさが、口いっぱいに広がります。<br'
                         '/>チキンとポークに特製スパイスをブレンドし、黄金比の美味しさをギュッと詰め込んだ風味豊かで濃厚なやみつきの味です。',
               star='4.4', star_number='1046', classification='chips')
node_12 = Node(node_id='chips02',
               title='湖池屋 ピュアポテト オホーツクの塩と岩塩 55g✕12袋',
               url='https://www.amazon.co.jp/%E6%B9%96%E6%B1%A0%E5%B1%8B-%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82'
                   '%82%E5%BF%83%E5%9C%B0-%E3%82%AA%E3%83%9B%E3%83%BC%E3%83%84%E3%82%AF%E3%81%AE%E5%A1%A9%E3%81%A8%E5'
                   '%B2%A9%E5%A1%A9%E3%81%AE%E5%90%88%E3%82%8F%E3%81%9B%E5%A1%A9%E5%91%B3-58g%C3%9712%E8%A2%8B/dp'
                   '/B07G1HMV68/ref=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=112Q0IEGUQZLY'
                   '&keywords=%E3%83%9D%E3%83%86%E3%83%88%E3%83%81%E3%83%83%E3%83%97%E3%82%B9&qid=1706156057&sprefix'
                   '=%E3%83%9D%E3%83%86%E3%83%88%E3%83%81%E3%83%83%E3%83%97%E3%82%B9%2Caps%2C184&sr=8-6',
               brand='湖池屋', price='1,719(260/100g)',
               introduce='湖池屋のポテトチップスは、国内産のじゃがいも100%で出来ております。<br/>あえて少し皮を残したことで、じゃがいも本来の風味やおいしさが、口いっぱいに広がります。<br'
                         '/>チキンとポークに特製スパイスをブレンドし、黄金比の美味しさをギュッと詰め込んだ風味豊かで濃厚なやみつきの味です。',
               star='4.3', star_number='1537', classification='chips')
node_13 = Node(node_id='chips03',
               title='プリングルス ケロッグ プリングルズ サワークリーム&オニオン S缶 53g×12個',
               url='https://www.amazon.co.jp/%E3%82%B1%E3%83%AD%E3%83%83%E3%82%B0-%E3%83%97%E3%83%AA%E3%83%B3%E3%82'
                   '%B0%E3%83%AB%E3%82%BA-%E3%82%B5%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%A0%EF%BC%86%E3'
                   '%82%AA%E3%83%8B%E3%82%AA%E3%83%B3-S%E7%BC%B6-53g%C3%9712%E5%80%8B/dp/B0BD73VYKB?ref_=ast_slp_dp',
               brand='プリングルス', price='1,826(152/個)',
               introduce='新しく生まれ変わったブランドロゴが印象的に映える緑のパッケージの「サワークリーム&オニオン」。<br'
                         '/>サワークリームの酸味とオニオンのうまみが濃厚な深い味わいが特長の「サワークリーム&オニオン」は、プリングルズ不動の人気ナンバーワンフレーバーです。',
               star='4.1', star_number='35', classification='chips')
node_14 = Node(node_id='chips04',
               title='プリングルス 【Amazon.co.jp限定】 ケロッグ プリングルズS缶3種アソートセット(うましお・サワークリームオニオン・CHEEEEEEESE) 【セット買い】',
               url='https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91-%E3%82%B1%E3%83%AD%E3'
                   '%83%83%E3%82%B0-%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%AB%E3%82%BAS%E7%BC%B63%E7%A8%AE%E3%82'
                   '%A2%E3%82%BD%E3%83%BC%E3%83%88%E3%82%BB%E3%83%83%E3%83%88-%E3%81%86%E3%81%BE%E3%81%97%E3%81%8A%EF'
                   '%BD%A5%E3%82%B5%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%8B%E3%82%AA'
                   '%E3%83%B3%EF%BD%A5CHEEEEEEESE-%E3%80%90%E3%82%BB%E3%83%83%E3%83%88%E8%B2%B7%E3%81%84%E3%80%91/dp'
                   '/B0BDRBC3WT?ref_=ast_slp_dp',
               brand='プリングルス', price='1,594(177/個)',
               introduce='【サワークリームオニオン】サワークリームの酸味とオニオンのうまみが濃厚な深い味わい酸味・サワークリーム・塩味'
                         '・オニオンなどの味の要素の全体的なバランスを整えたプリングルズらしいユニークな味わい。'
                         'オニオンの深い味わいとクリーミーさがアップした、クセになる味です<br/>【うましお】ポテトのうまみが引き立つシンプルな塩味です。'
                         '日本人が好む“しお味"を徹底的に研究し、ポテトの味わい・うまみがパワーアップ。まさに、うましお味という名前にふさわしい味です。'
                         '<br/>【CHEEEEEESE】毎回高い人気を誇るチーズ味がついに定番化!4種のチーズを使ったコクのある味わいです。',
               star='4.2', star_number='214', classification='chips')
node_15 = Node(node_id='chips05',
               title='【Amazon.co.jp限定】 ケロッグ プリングルズ S缶 4種アソートセット (うましお・サワークリームオニオン・CHEEEEEEESE・黒トリュフ) ※時期によりセット内容に変更あり',
               url='https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91-%E3%83%97%E3%83%AA%E3'
                   '%83%B3%E3%82%B0%E3%83%AB%E3%82%BA-4%E7%A8%AE%E3%82%A2%E3%82%BD%E3%83%BC%E3%83%88%E3%82%BB%E3%83'
                   '%83%E3%83%88-%E3%81%86%E3%81%BE%E3%81%97%E3%81%8A%EF%BD%A5%E3%82%B5%E3%83%AF%E3%83%BC%E3%82%AF%E3'
                   '%83%AA%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%8B%E3%82%AA%E3%83%B3%EF%BD%A5CHEEEEEEESE%EF%BD%A5%E9%BB'
                   '%92%E3%83%88%E3%83%AA%E3%83%A5%E3%83%95-%E2%80%BB%E6%99%82%E6%9C%9F%E3%81%AB%E3%82%88%E3%82%8A%E3'
                   '%82%BB%E3%83%83%E3%83%88%E5%86%85%E5%AE%B9%E3%81%AB%E5%A4%89%E6%9B%B4%E3%81%82%E3%82%8A/dp'
                   '/B0BDR86RYD?ref_=ast_slp_dp&th=1&psc=1',
               brand='プリングルス', price='2,086(174/個)',
               introduce='【サワークリームオニオン】サワークリームの酸味とオニオンのうまみが濃厚な深い味わい酸味・サワークリーム・塩味・'
                         'オニオンなどの味の要素の全体的なバランスを整えたプリングルズらしいユニークな味わい。'
                         'オニオンの深い味わいとクリーミーさがアップした、クセになる味です '
                         '【うましお】ポテトのうまみが引き立つシンプルな塩味です。日本人が好む“しお味""を徹底的に研究し、ポテトの味わい・'
                         'うまみがパワーアップ。まさに、うましお味という名前にふさわしい味です。'
                         '【CHEEEEEESE】毎回高い人気を誇るチーズ味がついに定番化!4種のチーズを使ったコクのある味わいです。'
                         '【ガーリックシュリンプ】エビの濃厚な味わいと豊かな香りに加え、ガーリックのしっかりとしたパンチが楽しめる、夏にぴったりのフレーバー。'
                         'アルコールや炭酸飲料などとも相性抜群。',
               star='4.0', star_number='964', classification='chips')
node_16 = Node(node_id='chicken_salad01',
               title='【 サラダチキン おためし４種 】uchipac レトルトおかず 4品目 セット 保存料 着色料 無添加'
                     ' 常温保存 賞味期限 半年～1年 非常食 手土産 贈り物 レトルト食品 詰め合わせ 保存食品 サラダ チキン',
               url='https://www.amazon.co.jp/%E3%82%B5%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3-%E3%81%8A%E3%81'
                   '%9F%E3%82%81%E3%81%97%EF%BC%94%E7%A8%AE-%E3%80%91uchipac-%E3%83%AC%E3%83%88%E3%83%AB%E3%83%88%E3'
                   '%81%8A%E3%81%8B%E3%81%9A-%E3%83%AC%E3%83%88%E3%83%AB%E3%83%88%E9%A3%9F%E5%93%81/dp/B0BJ1JPK8B/ref'
                   '=sr_1_2_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1OVM87YYLTE3I&keywords=%E3%82'
                   '%B5%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3&qid=1706162799&sprefix=%E3%82%B5%E3%83%A9%E3%83'
                   '%80%E3%83%81%E3%82%AD%E3%83%B3%2Caps%2C193&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'
                   '/B0BDR86RYD?ref_=ast_slp_dp&th=1&psc=1',
               brand='uchipac', price='1,620(1,620/セット)',
               introduce='外部ロジを使用しているため注文時の在庫状況によって賞味期限が短い場合もございますがご了承くださいませ。 '
                         '★人気のサラダチキン4つの味をお楽しみいただけます（プレーン・ブラックペッパー&ガーリック・カレー・長ネギ&生姜） ★国産の鶏胸肉を使用。保存料・着色料・増粘剤無添加！ '
                         '★常温で保存ができるサラダチキンです。賞味期限１年。 '
                         '★一般的な冷蔵品のサラダチキンのようなブヨブヨとした加工品の食感の商品ではありません。'
                         '市販品のサラダチキンをお求めの方にはお勧めしません。鶏胸肉のそのものの食感です。シーチキンの食感によく似ています。'
                         '開封前に軽くもみほぐしてからお召し上がりください。 '
                         '★uchipacシリーズは最終工程で無菌まで高温で殺菌をするので保存料無添加なのに、出来たて手作りのお惣菜が常温で保存が出来るようになりました。',
               star='3.8', star_number='205', classification='chicken_salad')
node_17 = Node(node_id='chicken_salad02',
               title='【Amazon.co.jp限定】 サラダクラブ チキンささみ(ほぐし肉)(国産) サラダチキン 常温保存 80g ×8個',
               url='https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91-%E3%82%B5%E3%83%A9%E3'
                   '%83%80%E3%82%AF%E3%83%A9%E3%83%96-%E3%83%81%E3%82%AD%E3%83%B3%E3%81%95%E3%81%95%E3%81%BF-%E3%81'
                   '%BB%E3%81%90%E3%81%97%E8%82%89-80g/dp/B084CC7ZQV/ref=sr_1_8?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82'
                   '%AB%E3%83%8A&crid=1OVM87YYLTE3I&keywords=%E3%82%B5%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3'
                   '&qid=1706162799&sprefix=%E3%82%B5%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3%2Caps%2C193&sr=8-8',
               brand='サラダクラブ', price='2,222(278/個)',
               introduce='・ほんのりと塩やこしょうで味付けし、サラダのトッピングに最適なチキンに仕上げました。そのまま、お使いいただけます。 '
                         '・「サラダクラブ」のパウチシリーズは、「サラダとお料理の素材」をコンセプトにしたシリーズです。 ・素材の下処理が不要でそのまま使え、しかも、使い切りの容量に仕立てています。 '
                         '・調理する時間がない時やあと一つ素材を加えたい時などに大変便利です。 ・また、常温保管できますので、ご家庭での常備品としても最適です。 1袋(80g)当たり '
                         'エネルギー・・・93kcaL たんぱく質・・・21.4g 脂質・・・0.6g 炭水化物・・・0.6g 食塩相当量・・・1g',
               star='4.0', star_number='284', classification='chicken_salad')
node_18 = Node(node_id='chicken_salad03',
               title='ホテイフーズコーポレーション 無添加サラダチキン 70g ×6個',
               url='https://www.amazon.co.jp/%E3%83%9B%E3%83%86%E3%82%A4-%E3%83%9B%E3%83%86%E3%82%A4%E3%83%95%E3%83'
                   '%BC%E3%82%BA%E3%82%B3%E3%83%BC%E3%83%9D%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3-%E7%84%A1%E6'
                   '%B7%BB%E5%8A%A0%E3%82%B5%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3-70g-%C3%976%E5%80%8B/dp'
                   '/B07XD39538/ref=sr_1_9?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1OVM87YYLTE3I'
                   '&keywords=%E3%82%B5%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3&qid=1706162799&sprefix=%E3%82%B5'
                   '%E3%83%A9%E3%83%80%E3%83%81%E3%82%AD%E3%83%B3%2Caps%2C193&sr=8-9',
               brand='ホテイ', price='1,026(171/個)',
               introduce='柔らかな肉質の若鶏の胸肉を、オイル不使用でシンプルな水煮に仕上げたサラダチキンです。'
                         '原材料は鶏肉、でん粉、食塩のみで食品添加物（化学調味料・リン酸塩）は不使用です。'
                         '一口サイズにカットした胸肉を調味液に漬けこみ、未加熱の状態で缶に詰め、殺菌工程で調理するという製法を採用しました。'
                         '事前ボイルなどを省くことで、鶏肉への熱ダメージを減らすとともに、鶏の旨味をしっかり残して柔らかな食感に仕上げています。'
                         '丁寧に皮をはいだ原料を使用しており、1 缶あたりのカロリーが67kcal と低脂肪である所も嬉しいポイントです。',
               star='3.8', star_number='44', classification='chicken_salad')
node_19 = Node(node_id='beef_jerky01',
               title='テング ビーフステーキジャーキー ミディアムチャンク レギュラー150g',
               url='https://www.amazon.co.jp/%E3%83%86%E3%83%B3%E3%82%B0-%E3%83%93%E3%83%BC%E3%83%95%E3%82%B9%E3%83'
                   '%86%E3%83%BC%E3%82%AD%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC-%E3%83%9F%E3%83%87%E3%82%A3%E3'
                   '%82%A2%E3%83%A0%E3%83%81%E3%83%A3%E3%83%B3%E3%82%AF-%E3%83%AC%E3%82%AE%E3%83%A5%E3%83%A9%E3%83'
                   '%BC150g/dp/B0B1PVBFT3/ref=sr_1_1_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid'
                   '=23P10NOZ4SC1K&keywords=%E3%83%93%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC'
                   '&qid=1706165476&sprefix=%E3%83%93%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AD%E3%83%BC'
                   '%2Caps%2C222&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
               brand='テング', price='1,498',
               introduce='厳選された牛もも肉を使用し、醤油をベースとした味付けのビーフステーキジャーキーです。'
                         'しっかりとした歯応えが特長で、噛めば噛むほど味わいを感じられる商品です。ビール等のおつまみに最適な商品です。'
                         '中身はテング ビーフステーキジャーキー レギュラー100gと同じものとなります。超お徳用大袋サイズ! !',
               star='4.5', star_number='3166', classification='beef_jerky')
node_20 = Node(node_id='beef_jerky02',
               title='なとり ザ・ビーフジャーキー 45g×5袋【エネルギー108kcal たんぱく質17.3g 脂質2.7g ※1袋当たり】',
               url='https://www.amazon.co.jp/%E3%81%AA%E3%81%A8%E3%82%8A-%E3%82%B6%E3%83%BB%E3%83%93%E3%83%BC%E3%83'
                   '%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC-45g%C3%975%E8%A2%8B/dp/B09WN31XMC/ref=sr_1_7'
                   '?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=23P10NOZ4SC1K&keywords=%E3%83%93%E3%83%BC'
                   '%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC&qid=1706165476&sprefix=%E3%83%93%E3%83%BC'
                   '%E3%83%95%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AD%E3%83%BC%2Caps%2C222&sr=8-7',
               brand='なとり', price='2,191(438/袋)',
               introduce='素材が持つおいしさを大切にした旨みを味わうビーフジャーキーです。'
                         'お酒のおつまみというよりも、おやつや小腹満たしでも食べられる方にもぴったりな肉の旨みを生かしたマイルドな味付けです。'
                         '牛肉はアイルランド産のモモ肉を厳選しました。アイルランド産牛肉は、穏やかな気候と広大な牧草地で育ち、適度な脂のさしが'
                         '入ったビーフジャーキーにぴったりな肉質が特長です。',
               star='4.2', star_number='268', classification='beef_jerky')
node_21 = Node(node_id='beef_jerky03',
               title='今川製菓 ジャーキー ビーフジャーキー 250g ブラックアンガス牛使用 おつまみ 業務用 大容量 (ビーフ)',
               url='https://www.amazon.co.jp/%E3%83%93%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC'
                   '-250g-%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%82%A2%E3%83%B3%E3%82%AC%E3%82%B9%E7%89%9B%E4%BD%BF'
                   '%E7%94%A8-%E3%81%8A%E3%81%A4%E3%81%BE%E3%81%BF-%E6%A5%AD%E5%8B%99%E7%94%A8/dp/B098Q6LD6D/ref'
                   '=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=23P10NOZ4SC1K&keywords=%E3%83%93%E3'
                   '%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC&qid=1706165476&sprefix=%E3%83%93%E3'
                   '%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AD%E3%83%BC%2Caps%2C222&sr=8-6',
               brand='今川製菓', price='2,299',
               introduce='原料にオーストラリア産のブラックアンガス種の牛モモ肉を使用しております。 原料となる牛は穀物肥育しており、赤身の中に適度にサシが入っているのが特徴です。 '
                         '醤油ベースのタレで付け込んで味付けすることで、臭みがなく食べやすく仕上げています。 '
                         '適度にサシが入っており、脂身と一緒に食べることで旨味があふれるビーフジャーキーです。（脂身を残して生産しておりますので、牛肉の旨味が味わえる一品です。） '
                         '冬季の低温時に表面に白色状のものが析出する場合がありますが、調味料・脂肪等が析出したものです。'
                         'また、夏季の高温時には脂肪が溶出してべたつく場合があります。いずれも品質には異常ありませんので、安心してお召し上がりください。 '
                         '栄養成分表示(100g当たり)：エネルギー383kcal たんぱく質34.9g 脂質20.3g 炭水化物15.2g 食塩相当量4.5g ※この表示は目安です。',
               star='3.9', star_number='548', classification='beef_jerky')
node_22 = Node(node_id='beef_jerky04',
               title='なとり THEおつまみBEEF 厚切ビーフジャーキー 塩ガーリック味 37g×5袋',
               url='https://www.amazon.co.jp/%E3%81%AA%E3%81%A8%E3%82%8A-THE%E3%81%8A%E3%81%A4%E3%81%BE%E3%81%BFBEEF'
                   '-%E5%8E%9A%E5%88%87%E3%83%93%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC-%E5'
                   '%A1%A9%E3%82%AC%E3%83%BC%E3%83%AA%E3%83%83%E3%82%AF%E5%91%B3-37g%C3%975%E8%A2%8B/dp/B0CJ51RHZF'
                   '/ref=sr_1_9?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=23P10NOZ4SC1K&keywords=%E3%83%93'
                   '%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC&qid=1706165476&sprefix=%E3%83%93'
                   '%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AD%E3%83%BC%2Caps%2C222&sr=8-9',
               brand='なとり', price='2,455(491/袋)',
               introduce='牛肉を「スチームロール製法」で、肉厚で、しっかりとした肉の食感を残しつつ、食べやすく仕上げました。'
                         '肉好きにはたまらない、ビーフジャーキーです。'
                         'ドイツ産岩塩とガーリックパウダーで味付けし、塩味とガーリックの香りを存分にお楽しみいただける味わいに仕上げました。'
                         'ガーリック好きにはたまらないパンチのあるおつまみです。',
               star='4.0', star_number='15', classification='beef_jerky')
node_23 = Node(node_id='beef_jerky05',
               title='国内製造 ビーフジャーキー 81ｇ 和風仕立て 牛もも肉の赤身使用',
               url='https://www.amazon.co.jp/%E5%9B%BD%E5%86%85%E8%A3%BD%E9%80%A0-%E3%83%93%E3%83%BC%E3%83%95%E3%82'
                   '%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC-100%EF%BD%87-%E5%92%8C%E9%A2%A8%E4%BB%95%E7%AB%8B%E3%81'
                   '%A6-%E7%89%9B%E3%82%82%E3%82%82%E8%82%89%E3%81%AE%E8%B5%A4%E8%BA%AB%E4%BD%BF%E7%94%A8/dp'
                   '/B088PJBKD1/ref=sr_1_10?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=23P10NOZ4SC1K'
                   '&keywords=%E3%83%93%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%AD%E3%83%BC&qid=1706165476'
                   '&sprefix=%E3%83%93%E3%83%BC%E3%83%95%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AD%E3%83%BC%2Caps%2C222&sr'
                   '=8-10',
               brand='つまみ蔵', price='890(11/g)',
               introduce='牛もも肉の赤身を使用したビーフジャーキーです。肉のうまみと和風味が美味しいビーフジャーキです。 国内工場にて製造しております。 '
                         '物足りなさを感じさせない丁度いい量感です。チャック付き袋です。 '
                         '原材料：牛肉、醤油、ビーフエキス、食塩、香辛料／ソルビット、調味料（有機酸等）、'
                         '酸化防止剤（エリソルビン酸ＮＡ）、増粘剤（キサンタンガム）、発色剤（亜硝酸Ｎａ）、'
                         '（一部に小麦・牛肉・大豆を含む） ✅内容量：81ｇ',
               star='4.1', star_number='181', classification='beef_jerky')
node_list = [node_snack, node_biscuit, node_cracker, node_light_meal, node_chicken,
             node_meat, node_beef, node_chips_potato, node_beef_jerky, node_chicken_salad, node_cookie, node_1, node_2,
             node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, node_11, node_12, node_13, node_14,
             node_15, node_16, node_17, node_18, node_19, node_20, node_21, node_22, node_23]

# node_list = []

for n in node_list:
    graph.create(n)
# 弃用 1-11
r1 = Relationship(node_2, 'is', node_cookie)
r2 = Relationship(node_3, 'is', node_cookie)
r3 = Relationship(node_4, 'is', node_cookie)
r4 = Relationship(node_5, 'is', node_cookie)
r5 = Relationship(node_6, 'is', node_cracker)
r6 = Relationship(node_7, 'is', node_cracker)
r7 = Relationship(node_8, 'is', node_cracker)
r8 = Relationship(node_9, 'is', node_cracker)
r9 = Relationship(node_10, 'is', node_cracker)
r10 = Relationship(node_11, 'is', node_chips_potato)
r11 = Relationship(node_12, 'is', node_chips_potato)


r12 = Relationship(node_snack, '含む', node_chips_potato)
# r13 = Relationship(node_snack, '含む', node_cracker)
r14 = Relationship(node_snack, '含む', node_biscuit)
r15 = Relationship(node_snack, '含む', node_beef_jerky)
# r16 = Relationship(node_snack, '含む', node_cookie)
r17 = Relationship(node_light_meal, '含む', node_chicken_salad)
r18 = Relationship(node_biscuit, '含む', node_cracker)
r19 = Relationship(node_biscuit, '含む', node_cookie)
r20 = Relationship(node_meat, '含む', node_beef)
r21 = Relationship(node_meat, '含む', node_chicken)
r22 = Relationship(node_beef, '含む', node_beef_jerky)
r23 = Relationship(node_chicken, '含む', node_chicken_salad)
# r24 = Relationship(node_meat, '含む', node_chicken_salad)
r25 = Relationship(node_1, 'is', node_cookie)
r26 = Relationship(node_13, 'is', node_chips_potato)
r27 = Relationship(node_14, 'is', node_chips_potato)
r28 = Relationship(node_15, 'is', node_chips_potato)
r29 = Relationship(node_16, 'is', node_chicken_salad)
r30 = Relationship(node_17, 'is', node_chicken_salad)
r31 = Relationship(node_18, 'is', node_chicken_salad)
r32 = Relationship(node_19, 'is', node_beef_jerky)
r33 = Relationship(node_20, 'is', node_beef_jerky)
r34 = Relationship(node_21, 'is', node_beef_jerky)
r35 = Relationship(node_22, 'is', node_beef_jerky)
r36 = Relationship(node_23, 'is', node_beef_jerky)


#
relation_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12,  r14, r15,  r17, r18, r19, r20,
                 r21, r22, r23,  r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35, r36]

for r in relation_list:
    graph.create(r)
