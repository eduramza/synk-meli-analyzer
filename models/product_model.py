import datetime
from attr import dataclass, field

from models.seller_model import Seller

@dataclass
class Product:
    id: str
    title: str
    price: float
    sold_quantity: int
    thumbnail: str
    total_revenue: float
    seller_details: Seller

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'sold_quantity': self.sold_quantity,
            'thumbnail': self.thumbnail,
            'total_revenue': self.total_revenue,
            'seller_details': self.seller_details.to_dict() if self.seller_details else None
        }