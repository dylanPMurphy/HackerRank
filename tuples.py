if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())


    x = tuple(i for i in integer_list)
    print(hash(x))
