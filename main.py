import math


class item:
    def __init__(self, name=None, cost=None, shipping=None, quantity_shipped=None, quantity_per_unit=1):
        self.name = name
        self.cost = cost
        self.shipping = shipping
        self.quantity_shipped = quantity_shipped
        self.quantity_per_unit = quantity_per_unit
        self.order_quantity = 0

    def __repr__(self):
        return str(
            [self.name, self.cost, self.shipping, self.quantity_shipped, self.quantity_per_unit, self.order_quantity])


class product:
    def __init__(self, path=None, production_run=1):
        self.items = list()
        self.path = path
        self.material_cost = None
        self.shipping_cost = None
        self.production_run = production_run

        self.read_file(self.path)
        self.price_per_unit = self.find_price_per_unit(self.production_run)

    def __repr__(self):
        return str([round(self.material_cost, 2), round(self.shipping_cost, 2), round(self.price_per_unit, 2)])

    def read_file(self, path=None):
        # makes for faster debugging
        if path is None:
            path = 'example_product.txt'

        with open(path, 'r', encoding='UTF-8') as f:
            lines = [x.strip() for x in f.readlines()]  # bad practice for large datasets, but not a problem here

        # file parsing! yay!
        for line in lines:
            text = line.split(',')
            for i in range(len(text)):
                text[i] = text[i].lower().strip()
            if text[0].startswith('#') or text[0] == '':
                continue
            elif text[0] == 'item':
                new_item = item(text[1], float(text[2]), float(text[3]),
                                int(text[4]))
                try:
                    new_item.quantity_per_unit = int(text[5])
                except IndexError:
                    print(f'Assuming quantity per unit for {text[1]} is 1')
                finally:
                    self.items.append(new_item)
            else:
                print(f'Unknown line found {line}')

    def find_price_per_unit(self, x=None):
        """

        :param x: Number of units being made
        :return:
        """
        if x is None:
            x = self.production_run

        # find the cost of materials and shipping to produce x units
        self.material_cost = 0
        self.shipping_cost = 0
        for item in self.items:
            item.order_quantity = math.ceil((x * item.quantity_per_unit) / item.quantity_shipped)
            self.material_cost += item.cost * item.order_quantity
            self.shipping_cost += item.shipping * item.order_quantity

        return (self.material_cost + self.shipping_cost) / x


if __name__ == '__main__':
    test = product(production_run=5)
    print(test)
    print(test.items)
