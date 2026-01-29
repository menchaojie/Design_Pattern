# logger_singleton.py - 日志记录器单例示例
import datetime

class Logger:
    def __init__(self):
        self.log_file = "app.log"
        self.log_level = "INFO"
        print(f"日志记录器已初始化，日志文件: {self.log_file}")
    
    def log(self, message, level="INFO"):
        """记录日志"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        # 模拟写入文件
        print(f"写入日志: {log_entry}")
        
        # 实际项目中这里会写入文件
        # with open(self.log_file, "a") as f:
        #     f.write(log_entry + "\n")
        
        return log_entry

# 创建单例日志记录器
logger_instance = Logger()

# 提供便捷函数
def info(message):
    """记录信息级别日志"""
    return logger_instance.log(message, "INFO")

def error(message):
    """记录错误级别日志"""
    return logger_instance.log(message, "ERROR")

def get_logger_info():
    """获取日志记录器信息"""
    return f"日志文件: {logger_instance.log_file}, 级别: {logger_instance.log_level}"