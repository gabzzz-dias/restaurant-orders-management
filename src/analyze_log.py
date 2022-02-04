import csv
from typing import Counter


def read(path):
    result = []

    with open(path) as file:
        read = csv.reader(file)
        for i in read:
            result.append(i)

        return result


def write(data):
    with open("data/mkt_campaign.txt", "w") as path:
        for i in data:
            path.write(f"""{i}\n""")


def favorite(name, arr):
    result = []

    for i in arr:
        if i[0] == name:
            result.append(i[1])
    favorite_meal = Counter(result).most_common(1)[0][0]

    return favorite_meal


def orders_counter(name, meal, arr):
    result = []

    for i in arr:
        if i[0] == name and i[1] == meal:
            result.append(i[1])

            return Counter(result).most_common(1)[0][1]


def get_orders(list):
    result = []

    for i in list:
        result.append(i[1])

    return set(result)


def get_customer_orders(name, arr):
    result = []

    for i in arr:
        if i[0] == name:
            result.append(i[1])

    return set(result)


def never(name, list):
    orders = get_orders(list)
    customer_orders = get_customer_orders(name, list)

    return orders.symmetric_difference(customer_orders)


def get_day(arr):
    result = []

    for i in arr:
        result.append(i[2])

    return result


def get_order_by_day(name, arr):
    result = []

    for i in arr:
        if i[0] == name:
            result.append(i[2])

    return result


def day_never(name, list):
    order_by_customer = set(get_order_by_day(name, list))
    days = set(get_day(list))

    return days.symmetric_difference(order_by_customer)


def analyze_log(path_to_file):
    csv_reader = read(path_to_file)
    fav_by_customer = favorite("maria", csv_reader)
    orders_count = orders_counter("arnaldo", "hamburguer", csv_reader)
    never_order = never("joao", csv_reader)
    never_order_by_day = day_never("joao", csv_reader)

    data = [
        fav_by_customer,
        orders_count,
        never_order,
        never_order_by_day,
    ]

    write(data)


analyze_log("data/orders_1.csv")
