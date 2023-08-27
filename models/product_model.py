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
    seller_id: str
    created_date: str
    days_since_created: int
    daily_sells: float
    daily_revenue: float
    month_revenue: float

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'sold_quantity': self.sold_quantity,
            'thumbnail': self.thumbnail,
            'total_revenue': self.total_revenue,
            'seller_details': self.seller_id,
            'created_date': self.created_date,
            'days_since_created': self.days_since_created,
            'daily_sells': self.daily_sells,
            'daily_revenue': self.daily_revenue,
            'month_revenue': self.month_revenue
        }