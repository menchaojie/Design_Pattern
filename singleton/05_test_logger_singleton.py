# test_logger_singleton.py - 测试日志记录器单例
from logger_singleton import logger_instance, info, error, get_logger_info

def test_logger():
    print("=== 日志记录器单例测试 ===")
    
    # 测试1: 使用导入的实例
    print("\n1. 使用导入的实例记录日志:")
    logger_instance.log("应用程序启动")
    
    # 测试2: 使用便捷函数
    print("\n2. 使用便捷函数记录日志:")
    info("用户登录成功")
    error("数据库连接失败")
    
    # 测试3: 验证单例性
    print("\n3. 验证单例性:")
    from logger_singleton import logger_instance as logger2
    
    print(f"logger1 内存地址: {id(logger_instance)}")
    print(f"logger2 内存地址: {id(logger2)}")
    print(f"是否是同一个对象: {logger_instance is logger2}")
    
    # 测试4: 状态共享
    print("\n4. 状态共享测试:")
    logger_instance.log_file = "new_app.log"
    print(f"修改后logger1的日志文件: {logger_instance.log_file}")
    print(f"logger2的日志文件: {logger2.log_file}")
    
    # 使用函数获取信息
    print(f"通过函数获取: {get_logger_info()}")


if __name__ == "__main__":
    test_logger()
    
    print("\n=== 测试完成 ===")
    print("说明: 日志记录器在整个应用中都是单例，确保日志配置一致!")