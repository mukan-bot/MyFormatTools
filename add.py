import tokenize
from io import StringIO

def format_assign_args(assign_args):
    tokens = tokenize.generate_tokens(StringIO(assign_args).readline)
    result = []
    inside_assign = False

    for token in tokens:
        tok_type, tok_string, _, _, _ = token
        
        # 「assign」の関数呼び出しの直下にいるかどうかを判断
        if tok_string == "assign":
            inside_assign = True
        elif inside_assign and tok_string == "=":
            # 「assign」直下の引数にある「=」の前後にスペースを追加
            result.append(" = ")
        else:
            result.append(tok_string)
            # 関数の終わりを検出した場合にフラグをリセット
            if tok_string in [")", ","]:
                inside_assign = False

    return "".join(result)

# テスト用コード
assign_args = 'df.assign(var1=val1, var2=(nested_val1, nested_val2), var3=val3)'
formatted_args = format_assign_args(assign_args)
print(formatted_args)