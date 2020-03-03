#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

print("hello")

parser = argparse.ArgumentParser()

# обязательные аргумены
parser.add_argument('-cl', '--client-list', type=str, dest='customer_list', help='customer delete list file')
parser.add_argument('-bl', '--beget-list', type=str, dest='beget_list', help='customer delete list file')



# не обязательные аргументы
#parser.add_argument('--date', dest='date_block', help='Block date')
#parser.add_argument('-e', '--email', type=str, dest='email_block', help='Block email')
#parser.add_argument('-s', '--site', type=str, dest='site', help='Block site')

args = parser.parse_args()
if args is not None:
#    print("Email кастомера - " + str(args.email_block))
    print("Файл кастомера с невалидным иящиками - " + str(args.customer_list))
else:
    pass


# собрать массив из файла кастомера
def create_client_list(client_file):
    with open(client_file) as file:
        client_list = [row.strip() for row in file]
    return client_list


# собрать массив из нашешл (из логов)
def create_beget_list_from_file():
    with open("list_b1.txt") as file:
        beget_list = [row.strip() for row in file]
    return beget_list


# формируем массив из лога
# def crete_beget_list_from_log(date_block, block_email):
# сравнить список кастомера с нашем
def comparison_lists(client_list, beget_list):
    delete_email = []
    dont_delete_email = []
    for email_beget in beget_list:
        if email_beget in client_list:
            delete_email.append(email_beget)
        elif email_beget not in client_list:
            dont_delete_email.append(email_beget)
    check1 = 0
    check2 = 0
    for i in delete_email:
        check1 = check1 + 1
    for j in dont_delete_email:
        check2 = check2 + 1

    print("удалены "+str(delete_email))
    print("Всего удалено - " + str(check1))
    print("не удалены "+str(dont_delete_email))
    print("Всего не удалено удалено - " + str(check2))
    input("Press Enter to Continue. . .: ")


# вывести результат( сколько ящиков из списка кастомера совпало с нашим списком)
# main

blist1 = create_beget_list_from_file()
clist2 = create_client_list(str(args.customer_list))

comparison_lists(clist2, blist1)
