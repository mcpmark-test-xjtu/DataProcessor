"""
Core data processing functions
"""

import json
import re
from typing import Any, Dict, List, Optional, Union


def parse_json(json_string: str) -> Optional[Dict[str, Any]]:
    """
    Parse a JSON string into a Python dictionary.
    
    Args:
        json_string: A valid JSON string
        
    Returns:
        Parsed dictionary, or None if parsing fails
        
    Example:
        >>> parse_json('{"name": "Alice", "age": 30}')
        {'name': 'Alice', 'age': 30}
    """
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, TypeError):
        return None


def to_json(data: Any, pretty: bool = False) -> str:
    """
    Convert Python data to JSON string.
    
    Args:
        data: Python data to convert
        pretty: Whether to format with indentation
        
    Returns:
        JSON string representation
        
    Example:
        >>> to_json({"name": "Bob"})
        '{"name": "Bob"}'
    """
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    return json.dumps(data, ensure_ascii=False)


def parse_csv_line(line: str, delimiter: str = ",") -> List[str]:
    """
    Parse a single CSV line into a list of values.
    
    Args:
        line: A CSV line string
        delimiter: Field delimiter (default: comma)
        
    Returns:
        List of field values
        
    Example:
        >>> parse_csv_line("apple,banana,cherry")
        ['apple', 'banana', 'cherry']
    """
    if not line:
        return []
    return [field.strip() for field in line.split(delimiter)]


def validate_email(email: str) -> bool:
    """
    Validate email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
        
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str, country_code: str = "CN") -> bool:
    """
    Validate phone number format.
    
    Args:
        phone: Phone number to validate
        country_code: Country code (CN for China, US for United States)
        
    Returns:
        True if valid, False otherwise
        
    Example:
        >>> validate_phone("13812345678", "CN")
        True
    """
    patterns = {
        "CN": r'^1[3-9]\d{9}$',
        "US": r'^\d{10}$'
    }
    pattern = patterns.get(country_code, patterns["CN"])
    clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
    return bool(re.match(pattern, clean_phone))


def flatten_dict(nested_dict: Dict, separator: str = ".") -> Dict[str, Any]:
    """
    Flatten a nested dictionary into a single-level dictionary.
    
    Args:
        nested_dict: Dictionary with nested structure
        separator: Key separator for nested keys
        
    Returns:
        Flattened dictionary
        
    Example:
        >>> flatten_dict({"user": {"name": "Alice", "age": 30}})
        {'user.name': 'Alice', 'user.age': 30}
    """
    result = {}
    
    def _flatten(obj: Any, prefix: str = ""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{prefix}{separator}{key}" if prefix else key
                _flatten(value, new_key)
        else:
            result[prefix] = obj
    
    _flatten(nested_dict)
    return result


def merge_dicts(*dicts: Dict) -> Dict:
    """
    Merge multiple dictionaries into one.
    
    Args:
        *dicts: Variable number of dictionaries
        
    Returns:
        Merged dictionary (later values override earlier)
        
    Example:
        >>> merge_dicts({"a": 1}, {"b": 2}, {"a": 3})
        {'a': 3, 'b': 2}
    """
    result = {}
    for d in dicts:
        if d:
            result.update(d)
    return result


def filter_dict_keys(data: Dict, keys: List[str], include: bool = True) -> Dict:
    """
    Filter dictionary by keys.
    
    Args:
        data: Input dictionary
        keys: List of keys to include or exclude
        include: If True, keep only specified keys; if False, remove them
        
    Returns:
        Filtered dictionary
        
    Example:
        >>> filter_dict_keys({"a": 1, "b": 2, "c": 3}, ["a", "b"])
        {'a': 1, 'b': 2}
    """
    if include:
        return {k: v for k, v in data.items() if k in keys}
    else:
        return {k: v for k, v in data.items() if k not in keys}

