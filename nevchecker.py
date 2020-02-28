print("hello")


# собрать массив из файла кастомера
def create_client_list():
    with open("clienmailslist_test.txt") as file:
        client_list = [row.strip() for row in file]
    return client_list


# собрать массив из нашешл (из логов)
def create_beget_list():
    with open("begetmaillist_test1.txt") as file:
        beget_list = [row.strip() for row in file]
    return beget_list


# сравнить список кастомера с нашем
def comparison_lists(list1, list2):
    if list1 == list2:
        print ("Списки равны")
    elif list1 != list2:
        print("Списки не равны")
    else:
        print("Что то не так")

# вывести результат( сколько ящиков из списка кастомера совпало с нашим списком)

# main


blist1 = create_beget_list()
clist2 = create_client_list()
comparison_lists(blist1, clist2)
