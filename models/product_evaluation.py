from dataclasses import dataclass

@dataclass
class CompetitionCounter:
    no_value: int
    leader: int
    gold: int
    platinum: int

    def to_dict(self):
        return {
            "no_value": self.no_value,
            "leader": self.leader,
            "gold": self.gold,
            "platinum": self.platinum
        }

@dataclass
class SalesCounter:
    minimum_qtd: int
    maximum_qtd: int
    total: int

    def to_dict(self):
        return {
            "minimum_qtd": self.minimum_qtd,
            "maximum_qtd": self.maximum_qtd,
            "total": self.total
        }

@dataclass
class ProductEvaluation:
    competition: CompetitionCounter
    sales: SalesCounter
    price_range: tuple

    def to_dict(self):
        return {
            "competition": self.competition.to_dict(),
            "sales": self.sales.to_dict(),
            "price_range": self.price_range
        }