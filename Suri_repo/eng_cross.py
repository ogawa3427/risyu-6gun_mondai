import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('20231119235802.csv')

# 倍率を計算する
df['倍率'] = df['全登録数'] / df['適正人数']

# 全体の倍率の平均と標準偏差
average_overall = df['倍率'].mean()
stddev_overall = df['倍率'].std()

# 6群の英語クラスの倍率の平均と標準偏差
average_6_english = df[(df['区分'].str.startswith('6')) & (df['時間割名'].str.contains('英語クラス'))]['倍率'].mean()
stddev_6_english = df[(df['区分'].str.startswith('6')) & (df['時間割名'].str.contains('英語クラス'))]['倍率'].std()

# 6群の日本語クラスの倍率の平均と標準偏差
average_6_japanese = df[(df['区分'].str.startswith('6')) & (~df['時間割名'].str.contains('英語クラス'))]['倍率'].mean()
stddev_6_japanese = df[(df['区分'].str.startswith('6')) & (~df['時間割名'].str.contains('英語クラス'))]['倍率'].std()

# 6群以外の英語クラスの倍率の平均と標準偏差
average_non6_english = df[(~df['区分'].str.startswith('6')) & (df['時間割名'].str.contains('英語クラス'))]['倍率'].mean()
stddev_non6_english = df[(~df['区分'].str.startswith('6')) & (df['時間割名'].str.contains('英語クラス'))]['倍率'].std()

# 6群以外の日本語クラスの倍率の平均と標準偏差
average_non6_japanese = df[(~df['区分'].str.startswith('6')) & (~df['時間割名'].str.contains('英語クラス'))]['倍率'].mean()
stddev_non6_japanese = df[(~df['区分'].str.startswith('6')) & (~df['時間割名'].str.contains('英語クラス'))]['倍率'].std()

print('全体の倍率の平均: ', average_overall)
print('全体の倍率の標準偏差: ', stddev_overall)
print('6群の英語クラスの倍率の平均: ', average_6_english)
print('6群の英語クラスの倍率の標準偏差: ', stddev_6_english)
print('6群の日本語クラスの倍率の平均: ', average_6_japanese)
print('6群の日本語クラスの倍率の標準偏差: ', stddev_6_japanese)
print('6群以外の英語クラスの倍率の平均: ', average_non6_english)
print('6群以外の英語クラスの倍率の標準偏差: ', stddev_non6_english)
print('6群以外の日本語クラスの倍率の平均: ', average_non6_japanese)
print('6群以外の日本語クラスの倍率の標準偏差: ', stddev_non6_japanese)
