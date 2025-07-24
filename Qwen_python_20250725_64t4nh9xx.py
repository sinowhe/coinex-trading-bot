import ccxt
import time
import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()

# اتصال به CoinEx
coinex = ccxt.coinex({
    'apiKey': os.getenv('COINEX_API_KEY'),
    'secret': os.getenv('COINEX_SECRET'),
    'enableRateLimit': True,
})

def get_market_data(symbol):
    """دریافت داده‌های بازار"""
    try:
        ticker = coinex.fetch_ticker(symbol)
        return ticker
    except Exception as e:
        print(f"خطا در دریافت داده: {e}")
        return None

def main():
    symbol = 'BTC/USDT'  # می‌تونیم تغییرش بدیم
    
    while True:
        try:
            # دریافت داده‌های بازار
            data = get_market_data(symbol)
            if data:
                print(f"{symbol}: قیمت = {data['last']}")
                # اینجا منطق معاملاتی میاد
            
            # استراحت 5 ثانیه
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("ربات متوقف شد")
            break
        except Exception as e:
            print(f"خطا: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()