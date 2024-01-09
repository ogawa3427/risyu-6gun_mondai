import pandas as pd

# CSVデータを読み込む
df = pd.read_csv('20231119235802.csv')

# 適正人数が0でない行だけを残す（0で割るとエラーになるため）
df = df[df['適正人数'] != 0]

# 倍率を計算する
df['倍率'] = df['全登録数'] / df['適正人数']

# 区分が6から始まる科目とそれ以外の科目を分ける
df_6 = df[df['区分'].str.startswith('6')]
df_other = df[~df['区分'].str.startswith('6')]

# それぞれの倍率の平均を計算する
mean_ratio_6 = df_6['倍率'].mean()
mean_ratio_other = df_other['倍率'].mean()

print('区分6から始まる科目の倍率の平均: ', mean_ratio_6)
print('区分6から始まらない科目の倍率の平均: ', mean_ratio_other)

# 全科目の倍率の平均を計算する
mean_ratio_all = df['倍率'].mean()

print('全科目の倍率の平均: ', mean_ratio_all)

# それぞれの倍率の分散と標準偏差を計算する
var_ratio_all = df['倍率'].var()
std_ratio_all = df['倍率'].std()

var_ratio_6 = df_6['倍率'].var()
std_ratio_6 = df_6['倍率'].std()

var_ratio_other = df_other['倍率'].var()
std_ratio_other = df_other['倍率'].std()

print('全科目の倍率の分散: ', var_ratio_all)
print('全科目の倍率の標準偏差: ', std_ratio_all)

print('区分6から始まる科目の倍率の分散: ', var_ratio_6)
print('区分6から始まる科目の倍率の標準偏差: ', std_ratio_6)

print('区分6から始まらない科目の倍率の分散: ', var_ratio_other)
print('区分6から始まらない科目の倍率の標準偏差: ', std_ratio_other)