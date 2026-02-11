from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 16', '+79991234567'),
    Smartphone('Samsung', 'Galaxy S25', '+79112583690'),
    Smartphone('Apple', 'iPhone Air', '+79997777777'),
    Smartphone('Nokia', '3310', '+79001237899'),
    Smartphone('Xiaomi', 'Redmi 15', '+79225488795')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
