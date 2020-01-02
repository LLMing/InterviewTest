# -*- coding: utf-8 -*-


def add_big_number(a, b):
    flag = True
    result_array = []
    temp_array = []
    if a.startswith('-') and b.startswith('-'):
        flag = False
        a = a[1:]
        b = b[1:]
    elif a.startswith('-') or b.startswith('-'):
        if a.startswith('-'):
            a = a[1:]
            if len(a) > len(b):
                for i in range(len(a)-len(b)):
                    b = '0' + b
            elif len(a) < len(b):
                for i in range(len(b)-len(a)):
                    a = '0' + a
            if a > b:
                flag = False
                first_array = list(map(int, a))
                second_array = list(map(int, b))
            else:
                second_array = list(map(int, a))
                first_array = list(map(int, b))
        else:
            b = b[1:]
            if len(a) > len(b):
                for i in range(len(a)-len(b)):
                    b = '0' + b
            elif len(a) < len(b):
                for i in range(len(b)-len(a)):
                    a = '0' + a
            if a < b:
                flag = False
                second_array = list(map(int, a))
                first_array = list(map(int, b))
            else:
                first_array = list(map(int, a))
                second_array = list(map(int, b))
        for i in range(len(first_array)):
            temp_array.append(first_array[i] - second_array[i])
        temp_array.reverse()
        for i in range(len(first_array)):
            if temp_array[i] >= 0:
                result_array.append(temp_array[i])
            else:
                if i != len(temp_array)-1:
                    result_array.append(10 + temp_array[i])
                    temp_array[i+1] -= 1
                else:
                    continue
        result_array.reverse()
        a = 0
        for i in range(len(result_array)):
            if result_array[i] != 0:
                break
            if i != len(result_array)-1:
                a += 1
        result_array = result_array[a:]
        if not flag:
            result_array.insert(0, '-')
        result_str = ''.join([str(x) for x in result_array])
        return result_str

    first_array = list(map(int, a))
    second_array = list(map(int, b))
    lens = abs(len(first_array) - len(second_array))
    if len(first_array) > len(second_array):
        for i in range(lens):
            second_array.insert(0, 0)
    elif len(first_array) < len(second_array):
        for i in range(lens):
            first_array.insert(0, 0)
    for i in range(len(first_array)):
        temp_array.append(first_array[i] + second_array[i])
    temp_array.reverse()
    for i in range(len(temp_array)):
        if temp_array[i] >= 10:
            result_array.append(temp_array[i]-10)
            if i != len(temp_array)-1:
                temp_array[i+1] += 1
            else:
                result_array.append(1)
        else:
            result_array.append(temp_array[i])
    if not flag:
        result_array.append('-')
    result_array.reverse()
    result_str = ''.join([str(x) for x in result_array])
    return result_str


if __name__ == '__main__':
    a = input("请输入第一个数字： ")
    b = input("请输入第二个数字： ")
    result = add_big_number(a, b)
    print(result)
