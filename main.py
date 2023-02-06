def bool_to_str(var: bool):
    return str(var)


def sum_list(list: list):
    return sum(list)


def wirte_to_file():
    with open('example.txt', 'w') as file:
        file.write("hello world")


if __name__ == "__main__":
    wirte_to_file()
