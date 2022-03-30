#!/usr/bin/env python3

# Disabling "protected-access" as this specifically tests the internal data of the class under test
# pylint: disable=W0212

### IMPORTS ###
import logging
import unittest

from kneedeepio.plugins.services import InMemoryConfigurationService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestInMemoryConfigurationService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_load_config(self):
        self.logger.debug("test_load_config")
        tmp_imcs = InMemoryConfigurationService()
        self.assertEqual(tmp_imcs._data, {})
        tmp_imcs.load_config({"key_zero": "value_zero"})
        self.assertEqual(tmp_imcs._data, {"key_zero": "value_zero"})

    def test_get_value(self):
        self.logger.debug("test_get_value")
        tmp_imcs = InMemoryConfigurationService()
        self.assertEqual(tmp_imcs._data, {})
        tmp_imcs._data["key_one"] = "value_one"
        self.assertEqual(tmp_imcs.get_value("key_one"), "value_one")

    def test_set_value(self):
        self.logger.debug("test_set_value")
        tmp_imcs = InMemoryConfigurationService()
        self.assertEqual(tmp_imcs._data, {})
        tmp_imcs.set_value("key_two", "value_two")
        self.assertEqual(tmp_imcs._data, {"key_two": "value_two"})
