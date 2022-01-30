
from datetime import datetime, timedelta
import requests
import json
from pandas import DataFrame


class BinanceSource:

    url_base: str
    symbols: list
    permissions: list
    exchange_info: dict

    def __init__(self):
        self.url_base = "https://api.binance.com"
        
        self.exchange_info = self._load_exchange_info()
        self.symbols = [symbol["symbol"] for symbol in self.exchange_info["symbols"]]

    def _load_exchange_info(self):
        url_path = "/api/v3/exchangeInfo"
        return requests.get(
            url=f"{self.url_base}{url_path}"
        ).json()

    def get_candlestick_data(self, symbol: str):
        url_path = "/api/v3/klines"
        url = f"{self.url_base}{url_path}"
        now = datetime.now()
        params = {
            "symbol": symbol,
            "interval": "15m",
            "startTime": now - timedelta(days=1),
            "endTime": now,
        }
        response = requests.get(
            url=url,
            params=params
        )
        parsed: list = []
        for candle in response.json():
            parsed.append({
                "open_time": datetime.fromtimestamp(candle[0] / 1000),
                "open": candle[1],
                "high": candle[2],
                "low": candle[3],
                "close": candle[4],
                "volume": candle[5],
                "close_time": datetime.fromtimestamp(candle[6] / 1000),
                "qoute_asset_volume": candle[7],
                "taker_buy_base_asset_volume": candle[8],
                "taker_buy_qoute_asset_volume": candle[9],
            })
        return DataFrame.from_records(parsed)

    def get_candlestick_data_local(self):
        with open("out.json", "r") as fp:
            source = fp.read()

        parsed: list = []
        for candle in json.loads(source):
            parsed.append({
                "open_time": datetime.fromtimestamp(candle[0] / 1000),
                "open": candle[1],
                "high": candle[2],
                "low": candle[3],
                "close": candle[4],
                "volume": candle[5],
                "close_time": datetime.fromtimestamp(candle[6] / 1000),
                "qoute_asset_volume": candle[7],
                "taker_buy_base_asset_volume": candle[8],
                "taker_buy_qoute_asset_volume": candle[9],
            })
        return DataFrame.from_records(parsed)