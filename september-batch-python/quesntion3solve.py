def question(*args):
    lst = list(args)
    dic = {}

    for i in lst:
        if i in dic.keys():
            pass
        else:
            if lst.count(i) != 1:
                dic[i] = lst.count(i)
    
    print(dic)

question(1, 2, 5, 1, 2, 3, 1, 2, 3, 1, 3)



# lst = [1, 2, 3, 5, 7, 4, 78, 1, 1, 1, 190, 67, 56, 2, 1, 1, 9]

# x = 0

# for i in lst:
#     if i == 1:
#         x = x + 1

# print(x)


# # print(lst.count(2))


