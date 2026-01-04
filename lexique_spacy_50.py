import spacy
from spacy.matcher import PhraseMatcher
import csv
import os

# === spaCy 模型加载 & 设置 max_length ===
try:
    nlp = spacy.load("fr_core_news_lg")
    nlp.max_length = 100_000_000
except:
    print("模型 fr_core_news_lg 未安装。请先运行：python -m spacy download fr_core_news_lg")
    exit()

# === 加载表达式列表 CSV ===
csv_path = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/fp.csv"
expressions = []

try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if row:
                expr = str(row[0]).strip()
                if expr.startswith("[") and expr.endswith("]"):
                    continue
                expressions.append(expr)
except Exception as e:
    print(f"无法读取 CSV 文件 : {e}")
    exit()

if not expressions:
    print("CSV 中无有效表达式。")
    exit()

# === 构建 PhraseMatcher 匹配器 ===
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(expr) for expr in expressions]
matcher.add("IDIOMS", patterns)

# === 循环处理前 50 个 chunk 文件 ===
chunks_dir = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/chunks"
output_dir = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/results50"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 51):  # 处理 chunk_001.txt 到 chunk_050.txt
    chunk_name = f"chunk_{i:03d}.txt"
    text_path = os.path.join(chunks_dir, chunk_name)
    
    try:
        with open(text_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"无法读取 {chunk_name}：{e}")
        continue

    print(f"\n正在处理：{chunk_name}")
    found = set()
    
    # 分段处理（防止超长崩溃）
    chunk_size = 10000
    for j in range(0, len(text), chunk_size):
        segment = text[j:j+chunk_size]
        doc = nlp(segment)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            found.add(span.text)
    
    # 输出匹配到的表达式
    if found:
        print(f"{chunk_name} 中找到 {len(found)} 个表达式")
    else:
        print(f"{chunk_name} 中未检测到表达式")

    # 写入 CSV
    output_csv = os.path.join(output_dir, f"idiomes_trouves_{chunk_name.replace('.txt', '')}.csv")
    with open(output_csv, 'w', encoding='utf-8', newline='') as out_f:
        writer = csv.writer(out_f)
        writer.writerow(["expression_trouvée"])
        for expr in sorted(found):
            writer.writerow([expr])
