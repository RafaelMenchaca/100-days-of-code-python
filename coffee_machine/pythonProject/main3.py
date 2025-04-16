# from numba.cuda.printimpl import print_item
#
# lista = [2200, 2350, 2600, 2130, 2190]
#
# extra_spend_feb = lista[1] - lista[0]
# print(f"Etra spend in FEB ${extra_spend_feb}")
#
# first_quarter = lista[0] + lista[1] + lista[2]
# print(f"Total expense in first quarter {first_quarter}")
#
# # for i in range(len(lista)):
# #     if lista[i] == 2000:
# #         print(f"2000 spent in {i}")
# spent_2000 = 2000 in lista
# print(f"Dis i spent 2000$ in any month? {spent_2000}")
#
# lista.append(1980)
# print(lista)
#
# lista[3] -= 200
# print(lista)
#
#
# heros = ['spider man','thor','hulk','iron man','captain america']
#
# print(len(heros))
# heros.append("black panther")
# print(heros)
#
# heros.remove("black panther")
# print(heros)
# heros.insert(3, "black panther")
# print(heros)
# # heros[1] = "doctor strange"
# # heros.remove("hulk")
# heros[1:3] = ["doctor strange"]
# print(heros)
#
# heros.sort()
# print(heros)

max_number = int(input("enter max number \n"))
lista = []
for i in range(max_number):
    if i % 2 != 0:
        lista.append(i)

print(lista)