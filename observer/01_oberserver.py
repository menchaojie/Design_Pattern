from abc import ABC, abstractmethod
from typing import List

# 观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        """观察者更新方法"""
        pass

# 主题接口
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        """注册观察者"""
        pass
   
    @abstractmethod
    def remove_observer(self, observer: Observer):
        """移除观察者"""
        pass
   
    @abstractmethod
    def notify_observers(self):
        """通知所有观察者"""
        pass

# 股票监控系统示例
class Stock:
    """股票类"""
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol  # 股票代码
        self._price = price   # 当前价格
        self._history = [price]  # 价格历史
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        """设置价格并记录历史"""
        old_price = self._price
        self._price = value
        self._history.append(value)
        return old_price, value
    
    def get_price_change(self) -> float:
        """获取价格变化百分比"""
        if len(self._history) < 2:
            return 0.0
        return ((self._history[-1] - self._history[-2]) / self._history[-2]) * 100

class StockMarket(Subject):
    """股票市场 - 具体主题"""
    def __init__(self):
        self._observers: List[Observer] = []
        self._stocks = {}  # 股票字典: {代码: Stock对象}
    
    def register_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self, stock: Stock):
        """通知观察者特定股票的变化"""
        change = stock.get_price_change()
        message = f"{stock.symbol}: ${stock.price:.2f} ({change:+.2f}%)"
        
        for observer in self._observers:
            observer.update(message)
    
    def add_stock(self, symbol: str, initial_price: float):
        """添加股票到市场"""
        self._stocks[symbol] = Stock(symbol, initial_price)
    
    def update_stock_price(self, symbol: str, new_price: float):
        """更新股票价格并通知观察者"""
        if symbol in self._stocks:
            stock = self._stocks[symbol]
            old_price, current_price = stock.price, new_price
            stock.price = new_price
            
            # 只有价格真正变化时才通知
            if old_price != current_price:
                self.notify_observers(stock)

class Investor(Observer):
    """投资者 - 具体观察者"""
    def __init__(self, name: str, interest_stocks: List[str] = None):
        self.name = name
        self.interest_stocks = interest_stocks or []
        self.notifications = []
    
    def update(self, message: str):
        """接收股票更新"""
        stock_symbol = message.split(":")[0]
        
        # 只关注感兴趣的股票
        if not self.interest_stocks or stock_symbol in self.interest_stocks:
            self.notifications.append(message)
            print(f"投资者 {self.name} 收到: {message}")
    
    def show_notifications(self):
        """显示所有通知"""
        print(f"\n=== {self.name} 的通知记录 ===")
        for notification in self.notifications:
            print(f"  - {notification}")

def demo_stock_market():
    """股票市场演示"""
    print("\n=== 股票市场监控系统演示 ===\n")
    
    # 创建股票市场
    market = StockMarket()
    
    # 添加股票
    market.add_stock("AAPL", 150.0)
    market.add_stock("GOOGL", 2800.0)
    market.add_stock("TSLA", 250.0)
    
    # 创建投资者
    investor1 = Investor("技术投资者", ["AAPL", "GOOGL"])
    investor2 = Investor("新能源投资者", ["TSLA"])
    investor3 = Investor("全市场投资者")
    
    # 注册投资者
    market.register_observer(investor1)
    market.register_observer(investor2)
    market.register_observer(investor3)
    
    # 模拟股票价格变化
    print("开始模拟股票交易...")
    market.update_stock_price("AAPL", 152.5)   # AAPL 上涨
    market.update_stock_price("TSLA", 245.0)   # TSLA 下跌
    market.update_stock_price("GOOGL", 2820.0) # GOOGL 上涨
    market.update_stock_price("AAPL", 151.0)   # AAPL 小幅下跌
    
    # 显示投资者通知记录
    investor1.show_notifications()
    investor2.show_notifications()
    investor3.show_notifications()

# 运行股票市场演示
demo_stock_market()