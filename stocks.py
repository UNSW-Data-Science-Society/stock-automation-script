from dataclasses import dataclass

@dataclass
class StockDef:
	company: str
	ticker: str
	desiredPrice: float

stock_list = [
	StockDef("Apple", "AAPL", 100)
]
