#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import InProcessLoggingService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestLoggingService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_debug(self):
        self.logger.debug("test_debug")
        tmp_ipls = InProcessLoggingService()
        with patch.object(tmp_ipls.logger, 'debug') as mock_debug:
            tmp_ipls.debug("key_one")
        mock_debug.assert_called_once_with("key_one")

    def test_info(self):
        self.logger.debug("test_info")
        tmp_ipls = InProcessLoggingService()
        with patch.object(tmp_ipls.logger, 'info') as mock_info:
            tmp_ipls.info("key_two")
        mock_info.assert_called_once_with("key_two")

    def test_warning(self):
        self.logger.debug("test_warning")
        tmp_ipls = InProcessLoggingService()
        with patch.object(tmp_ipls.logger, 'warning') as mock_warning:
            tmp_ipls.warning("key_three")
        mock_warning.assert_called_once_with("key_three")

    def test_error(self):
        self.logger.debug("test_error")
        tmp_ipls = InProcessLoggingService()
        with patch.object(tmp_ipls.logger, 'error') as mock_error:
            tmp_ipls.error("key_four")
        mock_error.assert_called_once_with("key_four")

    def test_critical(self):
        self.logger.debug("test_critical")
        tmp_ipls = InProcessLoggingService()
        with patch.object(tmp_ipls.logger, 'critical') as mock_critical:
            tmp_ipls.critical("key_five")
        mock_critical.assert_called_once_with("key_five")
