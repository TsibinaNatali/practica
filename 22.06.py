# st=[6,5,39,346,85]
# print(st)
# max = st[0]
# for i in range(len(st)):
#     if max<st[i]:
#         max = st[i]
#         max_index = i
#     if min>st[i]:
#         min = st[i]
#         min_index = i
#     print(f"максимальное число {max} индекс")
#     print(f"максимальное число {min}")
# for i in st:
#     if i % 2==0:
#         print(i)
# sum = 0
# for i in (st):
#     sum+=i
#     print(sum)
# for i in range(st):

#
# ls=[23,5,3,5,2,72,3]
# for i in range(len(ls)):
#     flag = True
#     for j in range(1,len(ls)):
#         if i != j:
#             continue
#         if ls[i] != ls[j]:
#             flag = False
#             break
#         if flag:
#             print(ls[i],end="")
ls1=[23,5,3,5,2,72,3]
ls2=[23,5,3,5,2,72,3]
for i in ls1:
    for j in ls2:
        if i == j:
            print("+")