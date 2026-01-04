import os

# 读取原始文件
file_path = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/frechcorpora.txt"
output_dir = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/chunks"
os.makedirs(output_dir, exist_ok=True)

# 读取文本并切分为词
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
    words = text.split()

# 定义 chunk 参数
total_words = len(words)
num_chunks = 200
chunk_size = total_words // num_chunks

# 写入每个 chunk 到单独的文件
for i in range(num_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_chunks - 1 else total_words
    chunk_words = words[start:end]
    chunk_text = ' '.join(chunk_words)

    output_path = os.path.join(output_dir, f"chunk_{i+1:03d}.txt")
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write(chunk_text)

print(f"{num_chunks} fichiers créés dans le dossier : {output_dir}")
