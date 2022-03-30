#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from kneedeepio.plugins.services import InMemoryObjectDatastoreService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestInMemoryObjectDatastoreService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_get_value(self):
        self.logger.debug("test_get_value")
        tmp_imods = InMemoryObjectDatastoreService()
        self.assertEqual(tmp_imods._data, {})
        tmp_imods._data["key_one"] = "value_one"
        self.assertEquals(tmp_imods.get_value("key_one"), "value_one")

    def test_set_value(self):
        self.logger.debug("test_set_value")
        tmp_imods = InMemoryObjectDatastoreService()
        self.assertEqual(tmp_imods._data, {})
        tmp_imods.set_value("key_two", "value_two")
        self.assertEqual(tmp_imods._data, {"key_two": "value_two"})
