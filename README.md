# DataProcessor

一个简单的数据处理工具库，提供常用的数据格式转换、验证和处理功能。DataProcessor 帮助你快速完成 JSON、CSV 数据解析，数据验证和字典操作等任务。

## Features

- JSON 解析与序列化（parse_json / to_json）- 快速解析和生成 JSON 数据
- CSV 行解析（parse_csv_line）- 将 CSV 行转换为列表
- 邮箱验证（validate_email）- 验证邮箱格式是否正确
- 手机号验证（validate_phone）- 支持中国和美国手机号格式验证
- 字典扁平化（flatten_dict）- 将嵌套字典转换为单层结构
- 字典合并（merge_dicts）- 合并多个字典
- 字典键过滤（filter_dict_keys）- 按键名过滤字典内容

## Installation

### 从源码安装

```bash
git clone https://github.com/mcpmark-test-xjtu/DataProcessor.git
cd DataProcessor
pip install -e .
```

### 开发模式安装

```bash
pip install -e .[dev]
```

## Usage

### 示例 1：JSON 数据处理

```python
from dataprocessor import parse_json, to_json

# 解析 JSON 字符串
data = parse_json('{"name": "Alice", "age": 30}')
print(data)  # 输出: {'name': 'Alice', 'age': 30}

# 生成 JSON 字符串
json_str = to_json({"city": "Beijing"}, pretty=True)
print(json_str)
```

### 示例 2：数据验证

```python
from dataprocessor import validate_email, validate_phone

# 邮箱验证
print(validate_email("user@example.com"))  # 输出: True
print(validate_email("invalid-email"))     # 输出: False

# 手机号验证
print(validate_phone("13812345678", "CN"))  # 输出: True
```

### 示例 3：字典操作

```python
from dataprocessor import flatten_dict, merge_dicts, filter_dict_keys

# 扁平化嵌套字典
nested = {"user": {"name": "Bob", "profile": {"age": 25}}}
flat = flatten_dict(nested)
print(flat)  # 输出: {'user.name': 'Bob', 'user.profile.age': 25}

# 合并多个字典
result = merge_dicts({"a": 1}, {"b": 2}, {"c": 3})
print(result)  # 输出: {'a': 1, 'b': 2, 'c': 3}

# 过滤字典键
filtered = filter_dict_keys({"a": 1, "b": 2, "c": 3}, ["a", "b"])
print(filtered)  # 输出: {'a': 1, 'b': 2}
```

## API Reference

### parse_json(json_string)

解析 JSON 字符串为 Python 字典。

### to_json(data, pretty=False)

将 Python 数据转换为 JSON 字符串。

### parse_csv_line(line, delimiter=",")

解析 CSV 行为值列表。

### validate_email(email)

验证邮箱地址格式。

### validate_phone(phone, country_code="CN")

验证手机号格式。

### flatten_dict(nested_dict, separator=".")

将嵌套字典扁平化。

### merge_dicts(*dicts)

合并多个字典。

### filter_dict_keys(data, keys, include=True)

按键名过滤字典。

## Contributing

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目。

## License

MIT License - 详见 [LICENSE](LICENSE) 文件

