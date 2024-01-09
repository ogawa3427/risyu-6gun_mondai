from scipy.stats import chi2_contingency

# Aの試行回数と失敗回数
n_A = 12
failures_A = int(n_A * 0.27) # Aの失敗率を0.27として
# Bの試行回数と失敗回数
n_B = 3
failures_B = int(n_B * 0.68)  # Bの失敗率を0.68として

# 成功回数
successes_A = n_A - failures_A
successes_B = n_B - failures_B

# カイ二乗検定
chi2, p_value, _, _ = chi2_contingency([[failures_A, failures_B], [successes_A, successes_B]])

# 一方向の検定のp値を得る
p_value_one_sided = p_value / 2

print(f"カイ二乗統計量: {chi2}")
print(f"一方向の検定のp値: {p_value_one_sided}")