from bson.objectid import ObjectId
from pystock.app.config import MONGO_SERVICE
from pystock.app.services.movements_service import *
from pystock.app.services.product_service import *


sales_collection = MONGO_SERVICE.get_sales()


def insert_sale(client, products):
    price = 0
    for product in products:
        product_object = get_by_cod(product['cod'])
        movement_price = int(product_object['price']) * int(product['amount'])
        price += movement_price
        movement = set_movement(product['cod'], product['amount'], False)
        if movement[1] == 500:
            return movement

    sales_collection.insert_one({
        'client': client,
        'products': products,
        'price': price
    })
    return {'message': 'Success'}, 200


def get_sales():
    sales = []
    for sale in sales_collection.find({}):
        sales.append(
            {
                "id": str(sale["_id"]),
                "client": sale["client"],
                "products": sale["products"],
                "price": sale["price"],
            })
    return sales, 200


def drop_sales():
    sales_collection.drop()
