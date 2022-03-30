#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import ConfigurationService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestConfigurationService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    @patch.multiple(ConfigurationService, __abstractmethods__ = set())
    def test_load_config(self):
        self.logger.debug("test_load_config")
        tmp_cs = ConfigurationService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_cs.load_config("config_zero")

    @patch.multiple(ConfigurationService, __abstractmethods__ = set())
    def test_get_value(self):
        self.logger.debug("test_get_value")
        tmp_cs = ConfigurationService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_cs.get_value("key_one")

    @patch.multiple(ConfigurationService, __abstractmethods__ = set())
    def test_set_value(self):
        self.logger.debug("test_set_value")
        tmp_cs = ConfigurationService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_cs.set_value("key_two", "value_two")
