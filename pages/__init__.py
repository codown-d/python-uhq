# pages/__init__.py
from .home import Home
from .mine import Mine
from .other import Other

# 创建一个字典以便于导出页面类
PAGE_CLASSES = {
    "home": Home,
    "mine": Mine,
    "other": Other,
}