"""
Tests for core data processing functions
"""

import unittest
from dataprocessor import (
    parse_json,
    to_json,
    parse_csv_line,
    validate_email,
    validate_phone,
    flatten_dict,
    merge_dicts,
    filter_dict_keys
)


class TestParseJson(unittest.TestCase):
    """Tests for parse_json function"""
    
    def test_valid_json(self):
        result = parse_json('{"name": "Alice", "age": 30}')
        self.assertEqual(result, {"name": "Alice", "age": 30})
    
    def test_invalid_json(self):
        result = parse_json("not valid json")
        self.assertIsNone(result)
    
    def test_empty_string(self):
        result = parse_json("")
        self.assertIsNone(result)


class TestToJson(unittest.TestCase):
    """Tests for to_json function"""
    
    def test_simple_dict(self):
        result = to_json({"name": "Bob"})
        self.assertEqual(result, '{"name": "Bob"}')
    
    def test_pretty_format(self):
        result = to_json({"a": 1}, pretty=True)
        self.assertIn("\n", result)


class TestParseCsvLine(unittest.TestCase):
    """Tests for parse_csv_line function"""
    
    def test_simple_csv(self):
        result = parse_csv_line("apple,banana,cherry")
        self.assertEqual(result, ["apple", "banana", "cherry"])
    
    def test_empty_line(self):
        result = parse_csv_line("")
        self.assertEqual(result, [])
    
    def test_custom_delimiter(self):
        result = parse_csv_line("a;b;c", delimiter=";")
        self.assertEqual(result, ["a", "b", "c"])


class TestValidateEmail(unittest.TestCase):
    """Tests for validate_email function"""
    
    def test_valid_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("test.user@domain.org"))
    
    def test_invalid_email(self):
        self.assertFalse(validate_email("invalid"))
        self.assertFalse(validate_email("@domain.com"))
        self.assertFalse(validate_email("user@"))


class TestValidatePhone(unittest.TestCase):
    """Tests for validate_phone function"""
    
    def test_valid_cn_phone(self):
        self.assertTrue(validate_phone("13812345678", "CN"))
    
    def test_invalid_cn_phone(self):
        self.assertFalse(validate_phone("12345678", "CN"))


class TestFlattenDict(unittest.TestCase):
    """Tests for flatten_dict function"""
    
    def test_nested_dict(self):
        result = flatten_dict({"user": {"name": "Alice", "age": 30}})
        self.assertEqual(result, {"user.name": "Alice", "user.age": 30})
    
    def test_simple_dict(self):
        result = flatten_dict({"a": 1, "b": 2})
        self.assertEqual(result, {"a": 1, "b": 2})


class TestMergeDicts(unittest.TestCase):
    """Tests for merge_dicts function"""
    
    def test_merge_two_dicts(self):
        result = merge_dicts({"a": 1}, {"b": 2})
        self.assertEqual(result, {"a": 1, "b": 2})
    
    def test_merge_with_override(self):
        result = merge_dicts({"a": 1}, {"a": 2})
        self.assertEqual(result, {"a": 2})


class TestFilterDictKeys(unittest.TestCase):
    """Tests for filter_dict_keys function"""
    
    def test_include_keys(self):
        result = filter_dict_keys({"a": 1, "b": 2, "c": 3}, ["a", "b"])
        self.assertEqual(result, {"a": 1, "b": 2})
    
    def test_exclude_keys(self):
        result = filter_dict_keys({"a": 1, "b": 2, "c": 3}, ["c"], include=False)
        self.assertEqual(result, {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()

