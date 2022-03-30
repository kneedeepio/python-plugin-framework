#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import ObjectDatastoreService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestObjectDatastoreService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    @patch.multiple(ObjectDatastoreService, __abstractmethods__ = set())
    def test_get_value(self):
        self.logger.debug("test_get_value")
        tmp_ods = ObjectDatastoreService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ods.get_value("key_one")

    @patch.multiple(ObjectDatastoreService, __abstractmethods__ = set())
    def test_set_value(self):
        self.logger.debug("test_set_value")
        tmp_ods = ObjectDatastoreService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ods.set_value("key_two", "value_two")
