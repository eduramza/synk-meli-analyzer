from dataclasses import dataclass

@dataclass
class Seller:
    id: str
    nickname: str
    power_seller_status: str
    address: str

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'power_seller_status': self.power_seller_status,
            'address': self.address
        }