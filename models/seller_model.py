from dataclasses import dataclass

@dataclass
class Seller:
    id: str
    address: str

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address
        }