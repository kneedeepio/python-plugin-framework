#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import InProcessLoggingService
from kneedeepio.plugins.plugin import Plugin

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestPlugin(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")
        # Setup a the logging service
        self.logging_service = InProcessLoggingService()

    @patch.multiple(Plugin, __abstractmethods__ = set())
    def test_init_no_services(self):
        self.logger.debug("test_init_no_services")
        with self.assertRaises(TypeError):
            tmp_plugin = Plugin()

    @patch.multiple(Plugin, __abstractmethods__ = set())
    def test_init_bad_services(self):
        self.logger.debug("test_init_no_services")
        with self.assertRaises(TypeError):
            tmp_plugin = Plugin({"logging": "bad_logger"})

    @patch.multiple(Plugin, __abstractmethods__ = set())
    def test_setup(self):
        self.logger.debug("test_setup")
        tmp_plugin = Plugin({"logging": self.logging_service})
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_plugin.setup()

    @patch.multiple(Plugin, __abstractmethods__ = set())
    def test_tick(self):
        self.logger.debug("test_tick")
        tmp_plugin = Plugin({"logging": self.logging_service})
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_plugin.tick()

    @patch.multiple(Plugin, __abstractmethods__ = set())
    def test_teardown(self):
        self.logger.debug("test_teardown")
        tmp_plugin = Plugin({"logging": self.logging_service})
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_plugin.teardown()
