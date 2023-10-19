"""
File: temperature_analysis.py

このスクリプトは、指定したCSVファイルから気温データを読み込み、以下の分析を行います。

1. データの読み込み: ファイル名を引数にしてCSVファイルを読み込む関数を実装します。
2. 月ごとの気温分析: 月毎の平均気温、最高気温、最低気温を計算します。
3. グラフの描画: 月毎の平均気温、最高気温、最低気温のグラフを表示します。

このスクリプトは、データ分析の一環として、特定の期間における気温の変動を調査する目的で使用できます。
"""

# pandasとmatplotlib.pyplotをインポートする
import pandas as pd
import matplotlib.pyplot as plt

# 1 データの読み込み


def load_data(filename: str):
    """
    CSVファイルを読み込み、pandas.DataFrameを返す。
    """
    # pandas.read_csvを使ってCSVファイルを読み込む
    df = pd.read_csv(filename, encoding="utf-8")

    # pandas.DataFrameを返す
    return df


# 同一ディレクトリにあるtemperature.csvを読み込む
df = load_data("temperature.csv")


"""
dfには以下の形式で値が入っています
date,average,max,min
2022/1/1,3.4,7.8,-1.0
1列目（date）から月を取り出して、月毎の平均気温、最高気温、最低気温を計算します
出力、output_dfには以下のような値をいれてください
month,average,max,min
1,10,15,5
2,11,16,6
3,12,17,7
"""
df["month"] = pd.to_datetime(df["date"]).dt.month
output_df = df.groupby("month").mean()
output_df["max"] = df.groupby("month").max()["max"]
output_df["min"] = df.groupby("month").min()["min"]

# 3 グラフの描画
# グラフの描画
output_df.plot(y=["average", "max", "min"], kind="line")
plt.show()
