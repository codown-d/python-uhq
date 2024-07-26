# routes.py
from pages import PAGE_CLASSES  # 导入页面类字典

def load_route(page_name):
    """根据路径加载页面类"""
    return PAGE_CLASSES[page_name]