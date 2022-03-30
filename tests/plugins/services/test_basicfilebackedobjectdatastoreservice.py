#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch, mock_open

from kneedeepio.plugins.services import BasicFileBackedObjectDatastoreService

### GLOBALS ###
READ_DATA = '{"key_one": "value_one"}'
WRITE_DATA = '{"key_one": "value_one", "key_two": "value_two"}'

### FUNCTIONS ###

### CLASSES ###
class TestBasicFileBackedObjectDatastoreService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_get_value(self):
        self.logger.debug("test_get_value")
        with patch("builtins.open", mock_open(read_data = READ_DATA)) as tmp_mock:
            tmp_bfbods = BasicFileBackedObjectDatastoreService(filename = "/tmp/file.json")
            self.assertEquals(tmp_bfbods.get_value("key_one"), "value_one")
        tmp_mock.assert_called_once_with("/tmp/file.json", mode = "r", encoding = "utf8")

    def test_get_value_file_not_found(self):
        self.logger.debug("test_get_value")
        with patch("builtins.open", mock_open()) as tmp_mock:
            tmp_mock.side_effect = FileNotFoundError
            tmp_bfbods = BasicFileBackedObjectDatastoreService(filename = "/tmp/file.json")
            with self.assertRaises(KeyError):
                # NOTE: Currently, this raises a key error.  Should this return an empty string instead?
                self.assertEquals(tmp_bfbods.get_value("key_one"), "value_one")
        tmp_mock.assert_called_once_with("/tmp/file.json", mode = "r", encoding = "utf8")

    def test_set_value(self):
        self.logger.debug("test_set_value")
        with patch("builtins.open", mock_open(read_data = READ_DATA)) as tmp_mock1:
            tmp_bfbods = BasicFileBackedObjectDatastoreService(filename = "/tmp/file.json")
        with patch("builtins.open", mock_open(read_data = READ_DATA)) as tmp_mock2:
            tmp_bfbods.set_value("key_two", "value_two")
        # FIXME: Why can't the mock be called multiple times?
        tmp_mock1.assert_called_once_with("/tmp/file.json", mode = "r", encoding = "utf8")
        tmp_mock2.assert_called_once_with("/tmp/file.json", mode = "w", encoding = "utf8")
        tmp_mock2().write.assert_called_once_with(WRITE_DATA)
