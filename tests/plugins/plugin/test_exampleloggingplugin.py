#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import InProcessLoggingService
from kneedeepio.plugins.plugin import ExampleLoggingPlugin

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestExampleLoggingPlugin(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")
        # Setup a the logging service
        self.logging_service = InProcessLoggingService()

    def test_setup(self):
        self.logger.debug("test_setup")
        tmp_elp = ExampleLoggingPlugin({"logging": self.logging_service})
        with patch.object(tmp_elp.logger, 'debug') as mock_debug:
            tmp_elp.setup()
        mock_debug.assert_called_once_with("setup method")

    def test_tick(self):
        self.logger.debug("test_tick")
        tmp_elp = ExampleLoggingPlugin({"logging": self.logging_service})
        with patch.object(tmp_elp.logger, 'debug') as mock_debug:
            tmp_elp.tick()
        mock_debug.assert_called_once_with("tick method")

    def test_teardown(self):
        self.logger.debug("test_teardown")
        tmp_elp = ExampleLoggingPlugin({"logging": self.logging_service})
        with patch.object(tmp_elp.logger, 'debug') as mock_debug:
            tmp_elp.teardown()
        mock_debug.assert_called_once_with("teardown method")
