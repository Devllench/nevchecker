#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import csv
import os

parser = argparse.ArgumentParser()

# обязательные аргумены
parser.add_argument('-cl', '--client-list', type=str, dest='customer_file', help='customer delete list file')
parser.add_argument('-bl', '--beget-list', type=str, dest='beget_file', help='customer delete list file')



# не обязательные аргументы
#parser.add_argument('--date', dest='date_block', help='Block date')
#parser.add_argument('-e', '--email', type=str, dest='email_block', help='Block email')
#parser.add_argument('-s', '--site', type=str, dest='site', help='Block site')

args = parser.parse_args()
if args is not None:
#    print("Email кастомера - " + str(args.email_block))
    print("Файл кастомера с невалидным иящиками - " + str(args.customer_file))
    print("Файл кастомера с невалидным иящиками - " + str(args.beget_file))
else:
    pass


# собрать массив из файла кастомера
def read_client_file_txt(client_file):
    with open(client_file) as file:
        client_list = [row.strip() for row in file]
    return client_list

def read_client_file_csv(client_file):
    pass

def create_client_list(client_file):
    ext = os.path.splitext(client_file)
    print(str(ext))
    if ".txt" in ext:
        print("file in "+str(ext[1]))
        client_list = read_client_file_txt(client_file)
    elif ".csv" in ext:
        print("file in "+str(ext[1]))
        client_list = read_client_file_csv(client_file)

    return client_list

# собрать массив из нашешл (из логов)
def create_beget_list_from_file(beget_file):
    with open(beget_file) as file:
        beget_list = [row.strip() for row in file]
    return beget_list


# формируем массив из лога
# def crete_beget_list_from_log(date_block, block_email):
# сравнить список кастомера с нашем
def comparison_lists(client_list, beget_list):
    delete_email = []
    dont_delete_email = []
    check1 = 0
    check2 = 0

    for email_beget in beget_list:
        if email_beget in client_list:
            delete_email.append(email_beget)
        elif email_beget not in client_list:
            dont_delete_email.append(email_beget)

    for i in delete_email:
        check1 = check1 + 1
    for j in dont_delete_email:
        check2 = check2 + 1

# вывести результат( сколько ящиков из списка кастомера совпало с нашим списком)
    print("удалены "+str(delete_email))
    print("Всего удалено - " + str(check1))
    print("не удалены "+str(dont_delete_email))
    print("Всего не удалено удалено - " + str(check2))
    input("Press Enter to Continue. . .: ")



# main

blist1 = create_beget_list_from_file(str(args.beget_file))
clist2 = create_client_list(str(args.customer_file))

print(":-"+str(clist2))
input("Press Enter to Continue. . .: ")

comparison_lists(clist2, blist1)

