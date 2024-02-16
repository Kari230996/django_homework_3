from .models import Client, Product, Order

# Создание нового клиента
def create_client(name, email, phone_number, address):
    return Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)

# Получение всех клиентов
def get_all_clients():
    return Client.objects.all()

# Получение клиента по его ID
def get_client_by_id(client_id):
    return Client.objects.get(pk=client_id)

# Обновление информации о клиенте
def update_client(client_id, name=None, email=None, phone_number=None, address=None):
    client = get_client_by_id(client_id)
    if name:
        client.name = name
    if email:
        client.email = email
    if phone_number:
        client.phone_number = phone_number
    if address:
        client.address = address
    client.save()
    return client

# Удаление клиента
def delete_client(client_id):
    client = get_client_by_id(client_id)
    client.delete()



# Создание нового товара
def create_product(name, description, price, quantity):
    return Product.objects.create(name=name, description=description, price=price, quantity=quantity)

# Получение всех товаров
def get_all_products():
    return Product.objects.all()

# Получение товара по его ID
def get_product_by_id(product_id):
    return Product.objects.get(pk=product_id)

# Обновление информации о товаре
def update_product(product_id, name=None, description=None, price=None, quantity=None):
    product = get_product_by_id(product_id)
    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if quantity:
        product.quantity = quantity
    product.save()
    return product

# Удаление товара
def delete_product(product_id):
    product = get_product_by_id(product_id)
    product.delete()


# Создание нового заказа
def create_order(client, products, total_amount):
    order = Order.objects.create(client=client, total_amount=total_amount)
    order.products.set(products)
    return order

# Получение всех заказов
def get_all_orders():
    return Order.objects.all()

# Получение заказа по его ID
def get_order_by_id(order_id):
    return Order.objects.get(pk=order_id)

# Обновление информации о заказе
def update_order(order_id, client=None, products=None, total_amount=None):
    order = get_order_by_id(order_id)
    if client:
        order.client = client
    if products:
        order.products.set(products)
    if total_amount:
        order.total_amount = total_amount
    order.save()
    return order

# Удаление заказа
def delete_order(order_id):
    order = get_order_by_id(order_id)
    order.delete()