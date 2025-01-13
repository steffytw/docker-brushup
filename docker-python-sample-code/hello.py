

def hello():
    pattern = [
        " *   *   *****   *       *        *****",
        " *   *   *       *       *        *   *",
        " *****   *****   *       *        *   *",
        " *   *   *       *       *        *   *",
        " *   *   *****   *****   ******   *****"
    ]
    for line in pattern:
        print(line)
    print(f"\033[1m Welcome to the sample python program with docker! \033[0m")


if __name__ == "__main__":
    hello()