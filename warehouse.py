import uuid


class Product:

    def __init__(self, product_name: str, price: int):
        self.product_name = product_name
        self.price = price
        self.id = Product.get_id()

    def __repr__(self) -> str:
        return (f"This is {self.product_name}, price is: {self.price}")

    @staticmethod
    def get_id() -> str:
        raw_id = []
        prod_id = ""
        raw_id = str(uuid.uuid4()).split("-")
        prod_id = raw_id[4]
        return prod_id


class Warehouse:

    def __init__(self) -> None:
        self.products = []

    def add_product(self, product_name, price):
        self.product_name = product_name
        self.price = price

        if product_name in self.products:
            print("This product already exists")
        else:
            product = Product(product_name, price)
            self.products.append(product)

    # commented lines were used for testing this method:
    def remove_product(self, product_name):
        k = 0
        i = 0
        for element in self.products:
            if product_name == element.product_name:
                # print("found it")
                i = k
                self.products.pop(i)
                print(f"{product_name} was removed")
            else:
                # print("not found")
                pass
            k += 1
            # print(i)
        if i > 0:
            pass
        else:
            print("product not found in warehouse")

    def display_products(self):
        for element in self.products:
            print(f"{element.id}, {element.product_name}, {element.price}")

    @staticmethod
    def get_product_price(product):
        return product.price

    def sort_by_price(self, ascending=True):
        if ascending == True:
            ascending = False
        else:
            ascending = True
        sorted_list = sorted(self.products,
                             key=self.get_product_price,
                             reverse=ascending)
        return sorted_list

        # or I gould get this func also to print the wanted list not only returning it.
        # this case instead of line 74 I would use this two lines:
        """ for element in sorted_list:
            print(f"{element.product_name}, {element.price}") """


warehouse = Warehouse()

warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)

for product in warehouse.sort_by_price():
    print(product)

# this is for testing all methods:
""" print(warehouse.products)

warehouse.remove_product('USB Cable')

warehouse.display_products()

print("without arg:")
warehouse.sort_by_price()
print("with arg=False:")
warehouse.sort_by_price(False)

print(warehouse.products) """