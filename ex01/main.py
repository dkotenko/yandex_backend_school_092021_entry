# задание 01 "Состав заказа"

import json



class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.items = {}
        self.status = 'OK'

    def add_item(self, item_id, count):
        if count < 0:
            return
        if item_id not in self.items:
            self.items[item_id] = Item(item_id)
        self.items[item_id].set_count(count)

    def set_status(self, status):
        self.status = status


    def reprJSON(self):
        return dict(id=self.id, items=[i.reprJSON() for i in self.items])


class Item:
    def __init__(self, ids):
        self.id = ids
        self.count = 0

    def set_count(self, count):
        self.count = count

    def reprJSON(self):
        return dict(id=self.id, count=self.count)


class OrderEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Order):
            return obj.reprJSON()
        return json.JSONEncoder.default(self, obj)






def main(filename):

    events = json.load(open(filename, 'r'))
    events.sort(key=lambda x: x['event_id'])
    orders = {}


    for event in events:
        order_id = event['order_id']
        item_id = event['item_id']
        count = event['count'] - event['return_count']
        status = event['status']
        if order_id not in orders:
            orders[order_id] = Order(order_id)
        orders[order_id].add_item(item_id, count)
        orders[order_id].set_status(status)


    l = []
    for order_id, order in orders.items():
        if order.status == 'CANCEL':
            continue
        new_items = []
        for item_id, item in order.items.items():
            if item.count < 1:
                continue
            new_items.append(item)
        order.items = new_items
        if not len(order.items):
            continue
        l.append(order)

    print(json.dumps(l, cls=OrderEncoder))


if __name__ == '__main__':
    filename = 'input.txt'
    #filename = 'test1.txt'
    main(filename)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
