import re

# you need to install this, pip install pandas
import pandas as pd


def lexer(target: str):
    pattern = r"[A-Za-z]+|[\(\)<=;]|\d+\.\d+"
    result = re.findall(pattern, target)
    output = []
    for match in result:
        arr = []
        if match in ["while"]:
            arr.append("keyword")
        elif match in ["(", ")", ";"]:
            arr.append("separator")
        elif match in ["<", "="]:
            arr.append("operator")
        elif "." in match:
            arr.append("real")
        else:
            arr.append("identifier")

        arr.append(match)
        output.append(arr)

    return output


def main():
    f = open("input_scode.txt", "r")
    entire_file = []
    for line in f.readlines():
        entire_file += lexer(line)

    cols = ["token", "lexeme"]
    df = pd.DataFrame(entire_file, columns=cols)

    to_write = open("output.txt", "w")
    to_write.write(df.to_string(header=True, index=False))


if __name__ == "__main__":
    main()
