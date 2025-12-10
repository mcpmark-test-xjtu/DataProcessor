"""
DataProcessor - 数据处理工具库

提供常用的数据格式转换、验证和处理功能
"""

__version__ = "0.1.0"
__author__ = "DataProcessor Team"

from .core import (
    parse_json,
    to_json,
    parse_csv_line,
    validate_email,
    validate_phone,
    flatten_dict,
    merge_dicts,
    filter_dict_keys
)

__all__ = [
    "parse_json",
    "to_json", 
    "parse_csv_line",
    "validate_email",
    "validate_phone",
    "flatten_dict",
    "merge_dicts",
    "filter_dict_keys"
]

