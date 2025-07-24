import ccxt
import time

# اتصال به CoinEx (بدون API Key برای تست)
coinex = ccxt.coinex({
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
    symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT']  # چند تا کوین
    
    print("🤖 ربات تستی CoinEx شروع شد...")
    print("در حال دریافت داده‌های بازار... (بدون پول واقعی)")
    print("=" * 50)
    
    while True:
        try:
            for symbol in symbols:
                # دریافت داده‌های بازار
                data = get_market_data(symbol)
                if data:
                    print(f"📊 {symbol}:")
                    print(f"   قیمت فعلی: ${data['last']:,.2f}")
                    print(f"   حجم 24h: ${data['quoteVolume']:,.0f}")
                    print("-" * 30)
            
            print(f"⏰ بروزرسانی: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("=" * 50)
            
            # استراحت 30 ثانیه
            time.sleep(30)
            
        except KeyboardInterrupt:
            print("\n👋 ربات متوقف شد")
            break
        except Exception as e:
            print(f"❌ خطا: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
