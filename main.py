class item:
    def __init__(self, name=None, cost=None, shipping=None, quantity_shipped=None, quantity_per_unit=1):
        self.name = name
        self.cost = cost
        self.shipping = shipping
        self.quantityshipped = quantity_shipped
        self.quantityperunit = quantity_per_unit


class product:
    def __init__(self):
        self.items = list()

    def add_item(self, new_item=item()):
        self.items.append(new_item)

    def read_file(self, path=None):
        if path is None:
            path = 'example_product.txt'

        with open(path, 'r', encoding='UTF-8') as f:
            lines = [x.strip() for x in f.readlines()]  # bad practice for large datasets, but not a problem here
        for line in lines:
            text = line.split(',')
            if text[0].lower().strip() == '#' or text[0].lower().strip() == '':
                continue
            elif text[0].lower().strip() == '':
                continue
