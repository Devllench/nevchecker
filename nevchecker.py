#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("hello")

import argparse
import time

parser = argparse.ArgumentParser()

# обязательные аргумены
parser.add_argument('--date', dest='date_block', help='Block date')
parser.add_argument('-e', '--email', dest='email_block', help='Block email')
parser.add_argument('-s', '--site', dest='site', help='Block site')
parser.add_argument('-cl', '--client-list', dest='customer_list', help='customer delete list file')
parser.add_argument('-bl', '--beget-list', dest='customer_list', help='customer delete list file')
# не обязательные аргументы

args = parser.parse_args()
if args is not None:
    print("Email кастомера - " + str(args.email_block))
    print("Файл кастомера с невалидным иящиками - " + str(args.customer_list))
else:
    pass


# собрать массив из файла кастомера
def create_client_list():
    with open("list_b1.txt") as file:
        client_list = [row.strip() for row in file]
    return client_list


# собрать массив из нашешл (из логов)
def create_beget_list_from_file():
    with open("list_c1.txt") as file:
        beget_list = [row.strip() for row in file]
    return beget_list


# формируем массив из лога
# def crete_beget_list_from_log(date_block, block_email):
# сравнить список кастомера с нашем
def comparison_lists(client_list, beget_list):
    delete_email = []
    dont_delete_email = []
    for email_in_client_list in client_list:
        print("Удаленные" + str(delete_email))
        print("Не удаленные" + str(dont_delete_email))
        for email_in_beget_list in beget_list:
            # сравниваем емаил кастомера и нашим емаилом
            if email_in_client_list == email_in_beget_list:
                delete_email.append(email_in_client_list)
            elif email_in_beget_list not in dont_delete_email:
                dont_delete_email.append(email_in_beget_list)
            else:
                pass


        input("Press Enter to Continue. . .: ")


# вывести результат( сколько ящиков из списка кастомера совпало с нашим списком)
# main

blist1 = create_beget_list_from_file()
clist2 = create_client_list()

comparison_lists(clist2, blist1)
