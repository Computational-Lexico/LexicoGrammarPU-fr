import csv

# 设定路径
csv_path = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/projetUNI/fp.csv"
txt_path = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/projetUNI/idioms.txt"

# 读取 CSV 并写入 TXT（假设 idiomes 在第一列）
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    with open(txt_path, 'w', encoding='utf-8') as txtfile:
        for row in reader:
            if row:  # 跳过空行
                txtfile.write(row[0].strip() + '\n')

print(" 转换完成：idioms.txt 已创建。")
