from src.analyze_log import (
    favorite,
    never,
    day_never,
    get_day,
)
from typing import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return favorite(costumer, self.orders)

    def get_nevered_per_costumer(self, costumer):
        return never(costumer, self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return day_never(costumer, self.orders)

    def get_busiest_day(self):
        return Counter(get_day(self.orders)).most_common(1)[0][0]

    def get_least_busy_day(self):
        return Counter(get_day(self.orders)).most_common()[-1][0]
