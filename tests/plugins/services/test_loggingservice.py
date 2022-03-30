#!/usr/bin/env python3

# Disabling the "abstract-class-instantiated" as this specifically tests the abstract class
# pylint: disable=E0110

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import LoggingService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestLoggingService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    @patch.multiple(LoggingService, __abstractmethods__ = set())
    def test_debug(self):
        self.logger.debug("test_debug")
        tmp_ls = LoggingService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ls.debug("key_one")

    @patch.multiple(LoggingService, __abstractmethods__ = set())
    def test_info(self):
        self.logger.debug("test_info")
        tmp_ls = LoggingService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ls.info("key_two")

    @patch.multiple(LoggingService, __abstractmethods__ = set())
    def test_warning(self):
        self.logger.debug("test_warning")
        tmp_ls = LoggingService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ls.warning("key_three")

    @patch.multiple(LoggingService, __abstractmethods__ = set())
    def test_error(self):
        self.logger.debug("test_error")
        tmp_ls = LoggingService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ls.error("key_four")

    @patch.multiple(LoggingService, __abstractmethods__ = set())
    def test_critical(self):
        self.logger.debug("test_critical")
        tmp_ls = LoggingService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_ls.critical("key_five")
