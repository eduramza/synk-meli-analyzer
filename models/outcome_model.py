
from attr import dataclass


@dataclass
class PagingInfo:
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
    info: PagingInfo 
    data: object

    def to_dict(self):
        return {
            'paging_info': self.info.to_dict(),
            'data': self.data
        }