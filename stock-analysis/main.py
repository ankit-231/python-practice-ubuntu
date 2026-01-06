# CELL 1: Import and Setup
import sqlite3
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Optional: Install if not available
# !pip install TA-Lib
# !pip install ta

# Try importing technical analysis libraries
# try:
#     import talib

#     TALIB_AVAILABLE = True
#     print("✅ TA-Lib imported successfully")
# except ImportError:
#     TALIB_AVAILABLE = False
#     print("❌ TA-Lib not available")

# try:
#     from ta.momentum import RSIIndicator
#     from ta import add_all_ta_features

#     TA_AVAILABLE = True
#     print("✅ TA library imported successfully")
# except ImportError:
#     TA_AVAILABLE = False
#     print("❌ TA library not available")

# print("📊 Basic libraries ready")


# # CELL 2: Database Connection and Data Loader
class DataLoader:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_stock_data(self, symbol, limit=None):
        """Get stock data for a symbol, ordered chronologically"""
        conn = sqlite3.connect(self.db_path)

        query = """
        SELECT date, close, open, high, low, volume 
        FROM prices 
        WHERE symbol = ? AND close IS NOT NULL 
        ORDER BY date ASC
        """

        if limit:
            query += f" LIMIT {limit}"

        df = pd.read_sql_query(query, conn, params=(symbol,))
        conn.close()

        if df.empty:
            return None

        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)
        return df

    def get_all_symbols(self):
        """Get all available symbols"""
        conn = sqlite3.connect(self.db_path)
        query = "SELECT DISTINCT symbol FROM prices WHERE close IS NOT NULL"
        symbols = pd.read_sql_query(query, conn)["symbol"].tolist()
        conn.close()
        return symbols

    def get_ltp_of_stock(self, symbol):
        """Get the last traded price (LTP) for a given stock symbol"""
        conn = sqlite3.connect(self.db_path)
        query = """
        SELECT close
        FROM prices 
        WHERE symbol = ? AND close IS NOT NULL
        ORDER BY date DESC
        LIMIT 1
        """

        result = pd.read_sql_query(query, conn, params=(symbol,))
        conn.close()

        if not result.empty:
            return result["close"].iloc[0]
        else:
            return None

    def get_n_price_of_stock(self, symbol, n):
        """Get the last traded price (LTP) for a given stock symbol"""
        conn = sqlite3.connect(self.db_path)
        query = """
        SELECT close
        FROM prices 
        WHERE symbol = ? AND close IS NOT NULL
        ORDER BY date DESC
        LIMIT ?
        """

        result = pd.read_sql_query(query, conn, params=(symbol, n))
        conn.close()

        if not result.empty:
            return result["close"]
        else:
            return None


# # Initialize data loader
loader = DataLoader("stocks.db")  # Update path
# symbols = loader.get_all_symbols()
# print(f"📈 Found {len(symbols)} symbols in database")
# print(f"Sample symbols: {symbols[:10]}")


# # CELL 3: RSI Method 1 - Classic Wilder's Smoothing (Manual)
# class RSI_Wilders:
#     @staticmethod
#     def calculate(prices, period=14):
#         """
#         Classic Wilder's RSI calculation
#         This is the original method used by Welles Wilder
#         """
#         if len(prices) < period + 1:
#             return None

#         prices = np.array(prices, dtype=float)
#         deltas = np.diff(prices)

#         # Separate gains and losses
#         gains = np.where(deltas > 0, deltas, 0.0)
#         losses = np.where(deltas < 0, -deltas, 0.0)

#         # Initial averages (SMA for first period)
#         avg_gain = np.mean(gains[:period])
#         avg_loss = np.mean(losses[:period])

#         # Wilder's smoothing for remaining periods
#         for i in range(period, len(gains)):
#             avg_gain = (avg_gain * (period - 1) + gains[i]) / period
#             avg_loss = (avg_loss * (period - 1) + losses[i]) / period

#         # Handle edge cases
#         if avg_loss == 0:
#             return 100.0 if avg_gain > 0 else 50.0

#         rs = avg_gain / avg_loss
#         rsi = 100 - (100 / (1 + rs))

#         return rsi


# # CELL 4: RSI Method 2 - Exponential Moving Average Approach
# class RSI_EMA:
#     @staticmethod
#     def calculate(prices, period=14):
#         """
#         RSI using Exponential Moving Average
#         More common in modern implementations
#         """
#         if len(prices) < period + 1:
#             return None

#         df = pd.DataFrame({"close": prices})
#         delta = df["close"].diff()

#         gain = delta.where(delta > 0, 0.0)
#         loss = -delta.where(delta < 0, 0.0)

#         # Use pandas EMA with alpha = 1/period (Wilder's smoothing factor)
#         avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
#         avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()

#         rs = avg_gain / avg_loss
#         rsi = 100 - (100 / (1 + rs))

#         return rsi.iloc[-1] if not pd.isna(rsi.iloc[-1]) else None


# # CELL 5: RSI Method 3 - Simple Moving Average (Alternative)
# class RSI_SMA:
#     @staticmethod
#     def calculate(prices, period=14):
#         """
#         RSI using Simple Moving Average instead of Wilder's smoothing
#         Some platforms use this variation
#         """
#         if len(prices) < period + 1:
#             return None

#         df = pd.DataFrame({"close": prices})
#         delta = df["close"].diff()

#         gain = delta.where(delta > 0, 0.0)
#         loss = -delta.where(delta < 0, 0.0)

#         # Simple moving average
#         avg_gain = gain.rolling(window=period).mean()
#         avg_loss = loss.rolling(window=period).mean()

#         rs = avg_gain / avg_loss
#         rsi = 100 - (100 / (1 + rs))

#         return rsi.iloc[-1] if not pd.isna(rsi.iloc[-1]) else None


# # CELL 6: RSI Method 4 - TA-Lib (Industry Standard)
# class RSI_TALib:
#     @staticmethod
#     def calculate(prices, period=14):
#         """
#         TA-Lib RSI - considered the gold standard
#         """
#         if not TALIB_AVAILABLE:
#             return None

#         if len(prices) < period * 2:  # TA-Lib needs more data
#             return None

#         prices_array = np.array(prices, dtype=float)
#         try:
#             rsi_values = talib.RSI(prices_array, timeperiod=period)
#             return rsi_values[-1] if not pd.isna(rsi_values[-1]) else None
#         except:
#             return None


# # CELL 7: RSI Method 5 - TA Library
# class RSI_TA:
#     @staticmethod
#     def calculate(prices, period=14):
#         """
#         Using TA library - another popular choice
#         """
#         if not TA_AVAILABLE:
#             return None

#         if len(prices) < period + 1:
#             return None

#         try:
#             df = pd.DataFrame({"close": prices})
#             rsi_indicator = RSIIndicator(close=df["close"], window=period)
#             rsi_values = rsi_indicator.rsi()
#             return rsi_values.iloc[-1] if not pd.isna(rsi_values.iloc[-1]) else None
#         except:
#             return None


# # CELL 8: RSI Method 6 - Modified Wilder's with Different Initialization
# class RSI_ModifiedWilders:
#     @staticmethod
#     def calculate(prices, period=14):
#         """
#         Modified Wilder's - uses EMA for initial calculation instead of SMA
#         Some platforms prefer this approach
#         """
#         if len(prices) < period + 1:
#             return None

#         prices = np.array(prices, dtype=float)
#         deltas = np.diff(prices)

#         gains = np.where(deltas > 0, deltas, 0.0)
#         losses = np.where(deltas < 0, -deltas, 0.0)

#         # Use exponential moving average from the start
#         alpha = 1.0 / period
#         avg_gain = gains[0]  # Initialize with first gain
#         avg_loss = losses[0]  # Initialize with first loss

#         for i in range(1, len(gains)):
#             avg_gain = alpha * gains[i] + (1 - alpha) * avg_gain
#             avg_loss = alpha * losses[i] + (1 - alpha) * avg_loss

#         if avg_loss == 0:
#             return 100.0 if avg_gain > 0 else 50.0

#         rs = avg_gain / avg_loss
#         rsi = 100 - (100 / (1 + rs))

#         return rsi


# # CELL 9: Timeframe Converter
# class TimeframeConverter:
#     @staticmethod
#     def to_weekly(df):
#         """Convert daily data to weekly (Friday close or last available)"""
#         if df.empty:
#             return df
#         weekly = (
#             df.resample("W-FRI")
#             .agg(
#                 {
#                     "open": "first",
#                     "high": "max",
#                     "low": "min",
#                     "close": "last",
#                     "volume": "sum",
#                 }
#             )
#             .dropna()
#         )
#         return weekly

#     @staticmethod
#     def to_monthly(df):
#         """Convert daily data to monthly (month-end close)"""
#         if df.empty:
#             return df
#         monthly = (
#             df.resample("M")
#             .agg(
#                 {
#                     "open": "first",
#                     "high": "max",
#                     "low": "min",
#                     "close": "last",
#                     "volume": "sum",
#                 }
#             )
#             .dropna()
#         )
#         return monthly


# # CELL 10: RSI Calculator Main Class
# class RSICalculator:
#     def __init__(self, data_loader):
#         self.loader = data_loader
#         self.methods = {
#             "wilders": RSI_Wilders.calculate,
#             "ema": RSI_EMA.calculate,
#             "sma": RSI_SMA.calculate,
#             "talib": RSI_TALib.calculate,
#             "ta": RSI_TA.calculate,
#             "modified_wilders": RSI_ModifiedWilders.calculate,
#         }

#     def calculate_all_methods(
#         self, symbol, timeframe="daily", period=14, data_limit=500
#     ):
#         """
#         Calculate RSI using all available methods

#         Args:
#             symbol: Stock symbol
#             timeframe: 'daily', 'weekly', 'monthly'
#             period: RSI period (usually 14)
#             data_limit: How many data points to fetch
#         """
#         # Get raw data
#         df = self.loader.get_stock_data(symbol, limit=data_limit)
#         if df is None or len(df) < 50:
#             return None

#         # Convert timeframe
#         if timeframe == "weekly":
#             df = TimeframeConverter.to_weekly(df)
#         elif timeframe == "monthly":
#             df = TimeframeConverter.to_monthly(df)

#         if len(df) < period + 10:  # Ensure enough data
#             return None

#         prices = df["close"].values
#         results = {}

#         # Test all methods
#         for method_name, method_func in self.methods.items():
#             try:
#                 rsi_value = method_func(prices, period)
#                 results[method_name] = {
#                     "rsi": round(rsi_value, 4) if rsi_value is not None else None,
#                     "data_points": len(prices),
#                     "latest_price": prices[-1],
#                 }
#             except Exception as e:
#                 results[method_name] = {
#                     "rsi": None,
#                     "error": str(e),
#                     "data_points": len(prices),
#                     "latest_price": prices[-1] if len(prices) > 0 else None,
#                 }

#         return {
#             "symbol": symbol,
#             "timeframe": timeframe,
#             "period": period,
#             "calculation_date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "methods": results,
#         }


# # Initialize calculator
# calculator = RSICalculator(loader)


# # CELL 11: Test Multiple Stocks and Methods
# def test_rsi_methods(symbols_to_test=None, timeframe="daily"):
#     """Test RSI calculations on multiple stocks"""
#     if symbols_to_test is None:
#         symbols_to_test = symbols[:5]  # Test first 5 symbols

#     results = []

#     for symbol in symbols_to_test:
#         print(f"Testing {symbol}...")
#         print("LTP:", loader.get_ltp_of_stock(symbol))
#         result = calculator.calculate_all_methods(symbol, timeframe=timeframe)
#         if result:
#             results.append(result)

#     return results


# # Run tests
# print("🧪 Testing RSI calculations...")
# test_results = test_rsi_methods(
#     ["NABIL", "ADBL", "NICA", "BNL", "HLI", "API", "CHDC"], "daily"
# )  # Replace with actual symbols

# # Display results
# for result in test_results:
#     print(f"\n📊 {result['symbol']} - {result['timeframe']} RSI:")
#     print("-" * 50)
#     for method, data in result["methods"].items():
#         if data["rsi"] is not None:
#             print(f"{method:15}: {data['rsi']:8.4f}")
#         else:
#             print(f"{method:15}: {'ERROR':>8}")


# # CELL 1: Data Investigation - Check Your Recent Data
# def investigate_recent_data(symbol, days_back=30):
#     """Check what recent data you have vs what NepseAlpha might be using"""
#     df = loader.get_stock_data(symbol, limit=50)
#     if df is None:
#         return None

#     print(f"🔍 Recent data for {symbol}:")
#     print("=" * 50)
#     print(f"Latest date in your DB: {df.index[-1].strftime('%Y-%m-%d')}")
#     print(f"Data points available: {len(df)}")
#     print(f"\nLast {min(10, len(df))} trading days:")

#     recent = df.tail(10)[["close", "volume"]].copy()
#     recent["price_change"] = recent["close"].pct_change() * 100
#     print(recent)

#     return df


# # Test with your symbols
# for symbol in ["NABIL", "ADBL", "NICA"]:
#     investigate_recent_data(symbol)
#     print("\n" + "=" * 60 + "\n")


# # CELL 2: Date Range Sensitivity Test
# def test_date_ranges(symbol, nepsealpha_rsi):
#     """Test RSI with different date ranges to see if that's the issue"""
#     print(f"📅 Date Range Sensitivity Test for {symbol}")
#     print(f"Target RSI (NepseAlpha): {nepsealpha_rsi}")
#     print("-" * 50)

#     # Test different data limits
#     data_limits = [100, 200, 300, 500, 750, 1000]

#     for limit in data_limits:
#         df = loader.get_stock_data(symbol, limit=limit)
#         if df is None or len(df) < 50:
#             continue

#         prices = df["close"].values

#         # Test SMA method (seems most promising)
#         rsi_sma = RSI_SMA.calculate(prices, 14)
#         rsi_wilders = RSI_Wilders.calculate(prices, 14)

#         diff_sma = abs(rsi_sma - nepsealpha_rsi) if rsi_sma else float("inf")
#         diff_wilders = (
#             abs(rsi_wilders - nepsealpha_rsi) if rsi_wilders else float("inf")
#         )

#         print(
#             f"Data points: {limit:4d} | "
#             f"SMA: {rsi_sma:6.2f} (diff: {diff_sma:5.2f}) | "
#             f"Wilders: {rsi_wilders:6.2f} (diff: {diff_wilders:5.2f}) | "
#             f"Latest: {df.index[-1].strftime('%Y-%m-%d')}"
#         )


# # Test the most promising stocks
# test_data = [("ADBL", 44.52), ("NICA", 39.72), ("API", 47.4)]

# for symbol, target_rsi in test_data:
#     test_date_ranges(symbol, target_rsi)
#     print("\n")


# # CELL 3: Price Data Verification
# def verify_price_data(symbol):
#     """Verify if your price data looks reasonable"""
#     df = loader.get_stock_data(symbol, limit=100)
#     if df is None:
#         return

#     print(f"💰 Price Data Verification for {symbol}")
#     print("-" * 40)

#     # Basic stats
#     print(f"Price range: {df['close'].min():.2f} - {df['close'].max():.2f}")
#     print(f"Current price: {df['close'].iloc[-1]:.2f}")
#     print(f"30-day volatility: {df['close'].pct_change().std() * 100:.2f}%")

#     # Look for suspicious patterns
#     price_changes = df["close"].pct_change()
#     large_moves = price_changes[abs(price_changes) > 0.1]  # >10% moves

#     if len(large_moves) > 0:
#         print(f"⚠️  Found {len(large_moves)} large price moves (>10%)")
#         print("Recent large moves:")
#         for date, change in large_moves.tail(5).items():
#             print(f"  {date.strftime('%Y-%m-%d')}: {change*100:+.1f}%")

#     # Check for gaps or missing data
#     date_diff = df.index.to_series().diff()
#     large_gaps = date_diff[date_diff > pd.Timedelta(days=5)]

#     if len(large_gaps) > 0:
#         print(f"⚠️  Found {len(large_gaps)} data gaps (>5 days)")

#     return df


# # Verify your data quality
# for symbol in ["NABIL", "ADBL", "NICA"]:
#     verify_price_data(symbol)
#     print("\n")


# # CELL 4: Custom RSI with Different Parameters
# class RSI_CustomTuned:
#     @staticmethod
#     def calculate_multiple_periods(prices, periods=[10, 12, 14, 16, 20]):
#         """Test RSI with different periods"""
#         results = {}
#         for period in periods:
#             if len(prices) >= period + 10:
#                 # Try SMA method since it's closest
#                 df = pd.DataFrame({"close": prices})
#                 delta = df["close"].diff()
#                 gain = delta.where(delta > 0, 0.0)
#                 loss = -delta.where(delta < 0, 0.0)

#                 avg_gain = gain.rolling(window=period).mean()
#                 avg_loss = loss.rolling(window=period).mean()

#                 rs = avg_gain / avg_loss
#                 rsi = 100 - (100 / (1 + rs))

#                 results[f"RSI_{period}"] = (
#                     rsi.iloc[-1] if not pd.isna(rsi.iloc[-1]) else None
#                 )

#         return results

#     @staticmethod
#     def calculate_with_smoothing_variations(prices, period=14):
#         """Test different smoothing approaches"""
#         if len(prices) < period + 10:
#             return {}

#         df = pd.DataFrame({"close": prices})
#         delta = df["close"].diff()
#         gain = delta.where(delta > 0, 0.0)
#         loss = -delta.where(delta < 0, 0.0)

#         results = {}

#         # Method 1: Standard SMA
#         avg_gain_sma = gain.rolling(window=period).mean()
#         avg_loss_sma = loss.rolling(window=period).mean()
#         rs_sma = avg_gain_sma / avg_loss_sma
#         rsi_sma = 100 - (100 / (1 + rs_sma))
#         results["SMA"] = rsi_sma.iloc[-1]

#         # Method 2: EMA with different alphas
#         for alpha in [1 / period, 2 / (period + 1), 1 / (period * 2)]:
#             avg_gain_ema = gain.ewm(alpha=alpha, adjust=False).mean()
#             avg_loss_ema = loss.ewm(alpha=alpha, adjust=False).mean()
#             rs_ema = avg_gain_ema / avg_loss_ema
#             rsi_ema = 100 - (100 / (1 + rs_ema))
#             results[f"EMA_alpha_{alpha:.4f}"] = rsi_ema.iloc[-1]

#         return results


# # CELL 5: Comprehensive Parameter Testing
# def find_best_parameters(symbol, target_rsi):
#     """Find the best parameters that match NepseAlpha"""
#     print(f"🎯 Parameter Optimization for {symbol} (Target: {target_rsi})")
#     print("=" * 60)

#     best_match = {"method": None, "rsi": None, "diff": float("inf")}

#     # Test different data amounts
#     for data_limit in [200, 300, 500]:
#         df = loader.get_stock_data(symbol, limit=data_limit)
#         if df is None or len(df) < 50:
#             continue

#         prices = df["close"].values

#         # Test different periods
#         period_results = RSI_CustomTuned.calculate_multiple_periods(prices)
#         for method, rsi_val in period_results.items():
#             if rsi_val is not None:
#                 diff = abs(rsi_val - target_rsi)
#                 if diff < best_match["diff"]:
#                     best_match = {
#                         "method": f"{method}_data_{data_limit}",
#                         "rsi": rsi_val,
#                         "diff": diff,
#                     }

#                 print(
#                     f"Data: {data_limit:3d} | {method:6} | RSI: {rsi_val:6.2f} | Diff: {diff:5.2f}"
#                 )

#         # Test smoothing variations
#         smooth_results = RSI_CustomTuned.calculate_with_smoothing_variations(prices)
#         for method, rsi_val in smooth_results.items():
#             if rsi_val is not None:
#                 diff = abs(rsi_val - target_rsi)
#                 if diff < best_match["diff"]:
#                     best_match = {
#                         "method": f"{method}_data_{data_limit}",
#                         "rsi": rsi_val,
#                         "diff": diff,
#                     }

#     print(f"\n🏆 Best match: {best_match['method']}")
#     print(f"RSI: {best_match['rsi']:.4f} (diff: {best_match['diff']:.4f})")

#     return best_match


# # Find best parameters for each stock
# optimization_results = {}
# test_stocks = [("ADBL", 44.52), ("NICA", 39.72), ("API", 47.4)]

# for symbol, target in test_stocks:
#     optimization_results[symbol] = find_best_parameters(symbol, target)
#     print("\n" + "=" * 60 + "\n")


# # CELL 6: Check for Data Freshness
# def check_data_freshness():
#     """Check how recent your data is"""
#     conn = sqlite3.connect("stocks.db")

#     # Get the most recent date in your database
#     query = "SELECT MAX(date) as latest_date, COUNT(*) as total_records FROM prices WHERE close IS NOT NULL"
#     result = pd.read_sql_query(query, conn)

#     latest_date = pd.to_datetime(result["latest_date"].iloc[0])
#     total_records = result["total_records"].iloc[0]

#     print(f"📅 Database Information:")
#     print(f"Latest date: {latest_date.strftime('%Y-%m-%d')}")
#     print(f"Days ago: {(pd.Timestamp.now() - latest_date).days} days")
#     print(f"Total price records: {total_records:,}")

#     # Check how many symbols have recent data
#     recent_query = """
#     SELECT COUNT(DISTINCT symbol) as symbols_with_recent_data
#     FROM prices
#     WHERE date >= date('now', '-30 days') AND close IS NOT NULL
#     """
#     recent_result = pd.read_sql_query(recent_query, conn)
#     print(
#         f"Symbols with data in last 30 days: {recent_result['symbols_with_recent_data'].iloc[0]}"
#     )

#     conn.close()


# check_data_freshness()

# # CELL 7: Final Recommendation
# print("\n" + "🎯 ANALYSIS COMPLETE - RECOMMENDATIONS:" + "\n")
# print("1. SMA method gives closest results for some stocks")
# print("2. Try different RSI periods (12, 16, 20) instead of 14")
# print("3. Your data might be stale - check if NepseAlpha has newer data")
# print("4. Consider that NepseAlpha might use adjusted prices")
# print("5. Test with exactly 250 trading days of data (industry standard)")

# # If you want to implement the best found method:
# print("\n" + "🚀 NEXT STEPS:")
# print("- Use SMA method for RSI calculation")
# print("- Test with 300-500 data points")
# print("- Consider using RSI period of 12 or 16 instead of 14")
# print("- Verify your data is as recent as NepseAlpha's")

# # print(loader.get_n_price_of_stock("NABIL", 10))

# from datetime import datetime, timedelta


class TradingDaysRSI:
    def __init__(self, data_loader):
        self.loader = data_loader

        # Nepal Stock Exchange holidays (add known holidays)
        # You might need to research NEPSE's exact holiday calendar
        self.nepse_holidays = {
            # # 2024 Holidays
            # "2024-01-12",  # Prithvi Jayanti
            # "2024-01-15",  # Maghe Sankranti
            # "2024-02-10",  # Sonam Losar
            # "2024-02-19",  # National Democracy Day
            # "2024-03-08",  # International Women's Day
            # "2024-03-29",  # Ghode Jatra
            # "2024-04-10",  # Ramjan Edul Fikra
            # "2024-04-13",  # Nepali New Year / Bisket Jatra
            # "2024-04-17",  # Ram Nawami
            # "2024-05-01",  # Labor Day / Ubhauli Parba
            # "2024-05-02",  # Kirat Rai Bhasa Diwas / Ubhauli Parba
            # "2024-05-23",  # Buddha Jayanti
            # "2024-05-29",  # Republic Day
            # "2024-06-17",  # Eid al-Adha
            # "2024-08-19",  # Janai Purnima / Raksha Bandhan / Gai Jatra / Gaijatra
            # "2024-08-20",  # Gaura Parba
            # "2024-08-26",  # Krishna Janmashtami
            # "2024-09-06",  # Hartalika Teej
            # "2024-09-16",  # Eid al-Adha (Id-ul-Azha)
            # "2024-09-17",  # Indra Jatra
            # "2024-09-20",  # Constitution Day
            # "2024-09-25",  # Jitiya Parba
            # "2024-10-03",  # Ghatasthapana
            # "2024-10-10",  # Phulpati / Fulpati (Dashain)
            # "2024-10-11",  # Astami (Dashain)
            # "2024-10-12",  # Nawami (Dashain)
            # "2024-10-13",  # Vijaya Dashami / Dashami (Dashain)
            # "2024-10-14",  # Ekadashi (Dashain)
            # "2024-10-15",  # Dwadashi (Dashain)
            # "2024-10-16",  # Kojagrat Purnima
            # "2024-10-31",  # Kaag Tihar (Tihar)
            # "2024-11-01",  # Kukur Tihar (Tihar)
            # "2024-11-02",  # Laxmi Puja (Tihar)
            # "2024-11-03",  # Govardhan Puja (Tihar)
            # "2024-11-04",  # Bhai Tika (Tihar)
            # "2024-11-07",  # Chhath Parba
            # "2024-11-15",  # Guru Nanak Jayanti
            # "2024-11-18",  # Phalgunanda Jayanti
            # "2024-12-11",  # Udhauli Parva
            # "2024-12-15",  # Udhauli Parva / Yomari Punhi
            # "2024-12-25",  # Christmas
            # "2024-12-30",  # Tamu Lhosar
            # # 2025 Holidays (up to Sep 2025, as per your data)
            # "2025-01-11",  # Prithvi Jayanti
            # "2025-01-14",  # Maghe Sankranti
            # "2025-01-29",  # Martyrs' Day
            # "2025-01-30",  # Sonam Lhosar / Martyrs' Memorial Day
            # "2025-02-19",  # National Democracy Day / Prajatantra Diwas
            # "2025-02-26",  # Maha Shivaratri
            # "2025-02-28",  # Gyalpo Lhosar
            # "2025-03-08",  # International Women's Day / Nari Dibas
            # "2025-03-13",  # Holi Purnima (Hill region) / Fagu Purnima
            # "2025-03-14",  # Holi Purnima (Terai region)
            # "2025-03-29",  # Ghode Jatra / Godhe Yatra
            # "2025-03-31",  # Ramjan Edul Fikra / Eid-Ul-Fitr
            # "2025-04-06",  # Ram Nawami
            # "2025-04-14",  # Nepali New Year
            # "2025-05-01",  # Labor Day / Majdoor Divas
            # "2025-05-12",  # Buddha Jayanti / Ubhauli Parva
            # "2025-05-29",  # Republic Day / Ganatantra Diwas
            # "2025-05-30",  # Bhoto Jatra
            # "2025-06-07",  # Eid al-Adha / Edul Aajaha
            # "2025-08-09",  # Janai Purnima / Raksha Bandhan
            # "2025-08-10",  # Gai Jatra
            # "2025-08-16",  # Krishna Janmashtami / Shree Krishna Janamashtami
            # "2025-08-26",  # Hartalika Teej
            # "2025-08-31",  # Gaura Parba
            # "2025-09-06",  # Indra Jatra
            # "2025-09-15",  # Jitiya Parwa
            # "2025-09-17",  # National Mourning Day
            # "2025-09-19",  # Constitution Day
            # "2025-09-22",  # Ghatasthapana
        }

    def get_trading_days_data(self, symbol, trading_days_count=500):
        """
        Get exactly N trading days of data, excluding weekends and holidays
        This mimics how NepseAlpha likely handles data
        """
        # Get more data than needed to filter down to trading days
        raw_df = self.loader.get_stock_data(symbol, limit=trading_days_count * 2)

        if raw_df is None or raw_df.empty:
            return None

        # Filter out weekends (Saturday = 5, Sunday = 6 in Nepal context)
        # Note: Nepal's weekend might be different, adjust if needed
        trading_df = raw_df.copy()
        # trading_df = trading_df[trading_df.index.dayofweek < 5]  # Mon-Fri only
        trading_df = trading_df[
            trading_df.index.dayofweek.isin([0, 1, 2, 3, 6])
        ]  # Sun (6), Mon (0), Tue (1), Wed (2), Thu (3)

        # Filter out known holidays
        holiday_dates = pd.to_datetime(list(self.nepse_holidays))
        trading_df = trading_df[~trading_df.index.isin(holiday_dates)]

        # Remove any rows with missing close prices
        trading_df = trading_df.dropna(subset=["close"])

        # Take only the requested number of trading days
        if len(trading_df) > trading_days_count:
            trading_df = trading_df.tail(trading_days_count)

        return trading_df

    def calculate_rsi_sma_method(self, prices, period=14):
        """
        The SMA method that's giving you the closest results
        """
        if len(prices) < period + 1:
            return None

        df = pd.DataFrame({"close": prices})
        delta = df["close"].diff()

        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        # Simple moving average (this is your winning method)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi.iloc[-1] if not pd.isna(rsi.iloc[-1]) else None

    def calculate_rsi_wilders_method(self, prices, period=14):
        """
        Wilder's method for comparison
        """
        if len(prices) < period + 1:
            return None

        prices = np.array(prices, dtype=float)
        deltas = np.diff(prices)

        gains = np.where(deltas > 0, deltas, 0.0)
        losses = np.where(deltas < 0, -deltas, 0.0)

        # Initial averages
        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])

        # Wilder's smoothing
        for i in range(period, len(gains)):
            avg_gain = (avg_gain * (period - 1) + gains[i]) / period
            avg_loss = (avg_loss * (period - 1) + losses[i]) / period

        if avg_loss == 0:
            return 100.0 if avg_gain > 0 else 50.0

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi

    def find_optimal_rsi(self, symbol, target_rsi, max_attempts=10):
        """
        Try different combinations to match NepseAlpha exactly
        """
        print(f"🎯 Finding optimal RSI for {symbol} (Target: {target_rsi})")
        print("-" * 50)

        best_match = {"config": None, "rsi": None, "diff": float("inf")}

        # Test different configurations
        configs_to_test = [
            # (trading_days, period, method_name)
            (250, 14, "SMA"),
            (300, 14, "SMA"),
            (400, 14, "SMA"),
            (500, 14, "SMA"),
            (600, 14, "SMA"),
            (250, 12, "SMA"),
            (300, 12, "SMA"),
            (500, 12, "SMA"),
            (250, 16, "SMA"),
            (300, 16, "SMA"),
            (500, 16, "SMA"),
            # Try Wilder's too
            (250, 14, "Wilders"),
            (500, 14, "Wilders"),
            (750, 14, "Wilders"),
            (1000, 14, "Wilders"),
        ]

        for trading_days, period, method in configs_to_test:
            try:
                trading_df = self.get_trading_days_data(symbol, trading_days)

                if trading_df is None or len(trading_df) < period + 10:
                    continue

                prices = trading_df["close"].values

                if method == "SMA":
                    rsi_val = self.calculate_rsi_sma_method(prices, period)
                else:  # Wilders
                    rsi_val = self.calculate_rsi_wilders_method(prices, period)

                if rsi_val is not None:
                    diff = abs(rsi_val - target_rsi)

                    print(
                        f"Days: {trading_days:3d} | Period: {period:2d} | {method:7} | "
                        f"RSI: {rsi_val:7.4f} | Diff: {diff:6.4f} | "
                        f"Latest: {trading_df.index[-1].strftime('%Y-%m-%d')}"
                    )

                    if diff < best_match["diff"]:
                        best_match = {
                            "config": f"{method}_{period}_days_{trading_days}",
                            "rsi": rsi_val,
                            "diff": diff,
                            "trading_days": trading_days,
                            "period": period,
                            "method": method,
                        }

            except Exception as e:
                continue

        print(f"\n🏆 Best match: {best_match['config']}")
        print(f"RSI: {best_match['rsi']:.4f} (diff: {best_match['diff']:.4f})")

        return best_match


# Initialize the trading-days-aware calculator
trading_rsi = TradingDaysRSI(loader)

# Test with your problematic stocks
test_stocks_with_targets = [
    ("NABIL", 51.3),
    ("ADBL", 44.52),
    ("NICA", 39.72),
    ("BNL", 37.57),
    ("HLI", 45.19),
    ("API", 47.4),
    ("CHDC", 37.69),
    ("CHDC", 37.69),
    ("AKPL", 47.08),
    ("TTL", 48.35),
    ("GBBL", 49.46),
]

optimal_configs = {}

for symbol, target in test_stocks_with_targets:
    try:
        optimal_configs[symbol] = trading_rsi.find_optimal_rsi(symbol, target)
        print("\n" + "=" * 60 + "\n")
    except Exception as e:
        print(f"❌ Error with {symbol}: {e}")
        continue

# Summary of best configurations
print("📊 SUMMARY OF OPTIMAL CONFIGURATIONS:")
print("=" * 60)
for symbol, config in optimal_configs.items():
    if config and config["diff"] < 2.0:  # Only show good matches
        print(
            f"{symbol:6}: {config['method']} Period-{config['period']} "
            f"Days-{config['trading_days']} → RSI: {config['rsi']:.4f} "
            f"(diff: {config['diff']:.4f})"
        )


# Create a standardized function based on best results
def calculate_nepsealpha_like_rsi(symbol, method="SMA", period=14, trading_days=500):
    """
    Calculate RSI that matches NepseAlpha's methodology
    Use the optimal parameters found above
    """
    trading_df = trading_rsi.get_trading_days_data(symbol, trading_days)

    if trading_df is None or len(trading_df) < period + 10:
        return None

    prices = trading_df["close"].values

    if method == "SMA":
        return trading_rsi.calculate_rsi_sma_method(prices, period)
    else:
        return trading_rsi.calculate_rsi_wilders_method(prices, period)


print("\n🎯 FINAL RECOMMENDATION:")
print("Use the calculate_nepsealpha_like_rsi() function with parameters")
print("from your optimal configurations above!")
