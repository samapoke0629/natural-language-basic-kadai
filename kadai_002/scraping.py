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
stop_words = ['は', 'が', 'の', 'に', 'を', 'と', 'で', 'である', 'です']

filtered_words = [word for word in cleaned_text.split() if word not in stop_words]

# 最初の1文を取得
first_sentence = "近頃は新しい技術について思っています。"  # 例文を直接指定
# 手動で品詞ごとに区切る
words_in_first_sentence = ['近頃', 'は', '新しい', '技術', 'について', '思って', 'います', '。']

# ストップワードを除去
filtered_first_sentence = [word for word in words_in_first_sentence if word not in stop_words]

# 結果を表示
print(' '.join(filtered_first_sentence))