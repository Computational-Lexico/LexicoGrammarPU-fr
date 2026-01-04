import spacy
import csv
from collections import Counter

# === 加载 spaCy 法语模型 ===
try:
    nlp = spacy.load("fr_core_news_lg")
except:
    print("请先运行：python -m spacy download fr_core_news_lg")
    exit()

# === 路径：你的 fp.csv 文件 ===
csv_path = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/fp.csv"

# === 读取表达式内容 ===
expressions = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            text = str(row[0]).strip()
            if text.startswith("[") and text.endswith("]"):
                continue
            expressions.append(text)

# === 分析所有表达式文本，提取动词 lemma ===
all_verbs = []

for expr in expressions:
    doc = nlp(expr)
    for token in doc:
        if token.pos_ == "VERB":
            all_verbs.append(token.lemma_.lower())

# === 统计频率 ===
verb_freq = Counter(all_verbs)

# === 输出前 20 个最常见动词 ===
print("📊 Top 20 des verbes les plus fréquents dans fp.csv :")
for verb, freq in verb_freq.most_common(20):
    print(f"{verb} : {freq} fois")

# === 可选：保存为 CSV ===
with open("frequence_verbes_fp.csv", "w", encoding="utf-8", newline='') as out_f:
    writer = csv.writer(out_f)
    writer.writerow(["verbe", "frequence"])
    for verb, freq in verb_freq.most_common():
        writer.writerow([verb, freq])

print("✅ Résultat enregistré dans frequence_verbes_fp.csv")
