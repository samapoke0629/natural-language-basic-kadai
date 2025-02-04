import requests
from bs4 import BeautifulSoup
import re

url = "https://www.aozora.gr.jp/cards/000148/files/2371_13943.html"

# スクレイピングを実行
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 本文を取得
text = soup.find('div', class_='main_text').get_text()

# HTMLタグや改行を削除
cleaned_text = re.sub(r'\s+', ' ', text)  # 改行や余分な空白を削除
cleaned_text = re.sub(r'<.*?>', '', cleaned_text)  # HTMLタグを削除

# ストップワードのリスト（例）
stop_words = ['は', 'が', 'の', 'に', 'を', 'と', 'で', 'である', 'です', 'から']  # 『から』を追加

filtered_words = [word for word in cleaned_text.split() if word not in stop_words]

# 最初の1文を取得
first_sentence = "近頃は大分方々の雑誌から談話をしろしろと責められて、頭ががらん胴になったから、当分品切れの看板でも懸かけたいくらいに思っています。"

# 手動で品詞ごとに区切る
words_in_first_sentence = [
    '近頃', 'は', '大分', '方々', 'の', '雑誌', 'から', 
    '談話', 'を', 'しろしろ', 'と', '責められて', '、', 
    '頭', 'が', 'がらん胴', 'に', 'なった', 'から', 
    '、', '当分', '品切れ', 'の', '看板', 'でも', 
    '懸かけたい', 'くらい', 'に', '思って', 'います', '。'
]

# ストップワードを除去
filtered_first_sentence = [word for word in words_in_first_sentence if word not in stop_words]

# 結果を表示
print(' '.join(filtered_first_sentence))