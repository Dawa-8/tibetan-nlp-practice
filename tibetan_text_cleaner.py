"""
藏语文本清洗工具
功能：去除藏语文本中的多余空格、特殊符号，统一格式
作者：Dawa-8
"""

import re

def clean_tibetan_text(text):
    """
    清洗藏语文本的核心函数
    """
    # 1. 将所有换行符和多余空格替换为单个空格
    text = re.sub(r'\s+', ' ', text)
    
    # 2. 只保留藏文字符范围 (\u0F00-\u0FFF) 以及基本的标点符号
    # 如果你想保留汉字，可以加上 \u4e00-\u9fff
    text = re.sub(r'[^\u0F00-\u0FFF0-9\s.,;:!?]', '', text)
    
    # 3. 去除首尾空格
    text = text.strip()
    return text

if __name__ == "__main__":
    # 测试一下
    test_text = " བཀྲ་ཤིས་བདེ་ལེགས།  !!! 123 "
    cleaned = clean_tibetan_text(test_text)
    print("清洗前:", test_text)
    print("清洗后:", cleaned)
