from functools import reduce

if __name__ == "__main__":
    new_list = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, new_list)
    print(total)
