from address import Address
from mailing import Mailing

to_address = Address('199004', 'г. Санкт-Петербург', 'Средний проспект В.О.',
                     '27', '12')

from_address = Address('115093', 'г. Москва', 'ул. Павла Андреева', '5', '61')

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    track='56457678875SM',
    cost=280.70
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
