import pandas as pd
import numpy as np

# 生成 5000 条模拟数据
num_galaxies = 5000
data = {
    'objID': np.arange(num_galaxies),
    'ra': np.random.uniform(0, 360, num_galaxies),    # 赤经 0-360
    'dec': np.random.uniform(-90, 90, num_galaxies),  # 赤纬 -90 到 90
    'redshift': np.random.uniform(0, 0.5, num_galaxies),
    'distance_mpc': np.random.uniform(10, 2000, num_galaxies) # 距离 10Mpc 到 2000Mpc
}

df = pd.DataFrame(data)
# 按照你代码中的逻辑：跳过前2行保存
with open('galactic_data.csv', 'w') as f:
    f.write("Header Line 1\n")
    f.write("objID, ra, dec, redshift, distance_mpc\n")
    df.to_csv(f, index=False, header=False)