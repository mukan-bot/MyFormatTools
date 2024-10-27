import re
import sys
from pathlib import Path

def format_assign_eq_spacing(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # assign関数の引数の=の前後にスペースを追加
    def replace_assign_args(match):
        assign_args = match.group("assign_args")
        # 関数内の引数を区別するために外側のみ対象にする正規表現を使用
        formatted_args = re.sub(r"(\w+)\s*=\s*(?![^(]*\))", r"\1 = ", assign_args)
        return f"{match.group('assign')}{formatted_args}{match.group('assign_end')}"

    # ネストされた括弧やコメントを考慮した正規表現
    formatted_content = re.sub(
        r"(?P<assign>assign\()(?P<assign_args>(?:[^()#]+|\([^()]*\)|#.*)+)(?P<assign_end>\))",
        replace_assign_args,
        content,
        flags=re.MULTILINE | re.DOTALL,
    )
    print(f"Formatted: {file_path}")

    # ==が= =になる場合があるので、それを修正
    formatted_content = re.sub(r"= =", "==", formatted_content)

    # 変更があればファイルに書き戻す
    if content != formatted_content:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(formatted_content)

def main(target_dir):
    print(f"Target directory: {target_dir}")
    # .pyファイルが指定されている場合はそのファイルのみを対象にする
    if Path(target_dir).is_file():
        format_assign_eq_spacing(target_dir)
        return
    # 指定されたディレクトリ以下の全ての.pyファイルを対象にする
    for file_path in Path(target_dir).rglob("*.py"):
        format_assign_eq_spacing(file_path)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    main(target_dir)
