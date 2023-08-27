
from attr import dataclass


@dataclass
class ApiInfo:
    total: int
    offset: int
    limit: int

    def to_dict(self):
        return {
            'total': self.total,
            'offset': self.offset,
            'limit': self.limit
        }

@dataclass
class ApiResponse:
    info: ApiInfo 
    data: object

    def to_dict(self):
        return {
            'info': self.info.to_dict(),
            'data': self.data
        }