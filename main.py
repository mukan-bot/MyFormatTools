import math

import numpy as np
import pandas

# ランダムな値を入れたDataFrameを作成
df = pandas.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9],
    }
)

# assignメソッドで新しい列を追加
df.assign(
    D = df["A"] + df["B"],
    E = df["B"] - df["C"],
    F = df["C"] * df["A"],
    G = df["A"] / df["B"],
    H = df["B"] // df["C"],
    I = df["C"] % df["A"],
    P = df["A"].add(df["B"]),  # 関数を使って新しい列を追加
    Q = df["B"].sub(df["C"]),
    R = df["C"].mul(df["A"]),
    S = df["A"].floordiv(df["B"]),
    T = df["B"].mod(df["C"]),
    U = df["C"].pow(df["A"]),
    J = lambda df: df["A"] + df["B"],  # ラムダ式を使って新しい列を追加
    K = lambda df: df["B"] - df["C"],
    L = lambda df: df["C"] * df["A"],
    M = lambda df: df["A"] / df["B"],
    N = lambda df: df["B"] // df["C"],
    O = lambda df: df["C"] % df["A"],
    V = df["A"].add(
        other=df["B"]
    ),  # 関数を使って新しい列を追加（キーワードを使って引数）
    W = df["B"].sub(other=df["C"]),
    X = df["C"].mul(other=df["A"]),
    Y = df["A"].floordiv(other=df["B"]),
    Z = df["B"].mod(other=df["C"]),
    AA = df["C"].pow(other=df["A"]),
    AB = df["A"].add(
        other=df["B"]
    ),  # 関数を使って新しい列を追加（キーワードを使って引数、引数の順番を変える）
    AC = df["B"].sub(other=df["C"]),
    AD = df["C"].mul(other=df["A"]),
    AE = df["A"].floordiv(other=df["B"]),
    AF = df["B"].mod(other=df["C"]),
    AG = df["C"].pow(other=df["A"]),
    # np.where関数を使って新しい列を追加
    Hoge = np.where(df["A"] > 1, "A", "B"),
    # np.select関数を使って新しい列を追加
    Fuga = np.select(
        [df["A"] >= 1, df["B"] > 1],
        ["A", "B"],
        default="C",
    ),
    # np.piecewise関数を使って新しい列を追加
    Piyo = np.piecewise(
        df["A"],
        [df["A"] == 1, df["B"] > 1],
        ["A", "B"],
    ),
)


def test(text: str) -> str:
    print(text)
    return text


if test(text="Hello") == "Hello":
    print("Success")

print(test(text="Hello"))

if test.__name__ == "test":
    print("Hello")

if test("__main__") == "__main__":
    df_test = df
    print(df_test)
print("Hello")
