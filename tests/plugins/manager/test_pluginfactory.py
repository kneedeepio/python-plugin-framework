#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from kneedeepio.plugins.services import InProcessLoggingService
from kneedeepio.plugins.plugin import ExampleLoggingPlugin
from kneedeepio.plugins.manager import PluginFactory
from kneedeepio.plugins.manager import ServiceAlreadyRegisteredException, ServiceNotRegisteredException
from kneedeepio.plugins.manager import PluginAlreadyLoadedException, PluginNotLoadedException

### GLOBALS ###

### FUNCTIONS ###
def callback_method(value):
    logging.debug("This is the value passed to the callback: %s", value)

### CLASSES ###
class MockPlugin(ExampleLoggingPlugin):
    # This is a mock plugin to test for missing services.
    required_services = ["logging", "configuration"]

class TestPluginFactory(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")
        # Setup a the logging service
        self.logging_service = InProcessLoggingService()

    def test_register_service(self):
        self.logger.debug("test_register_service")
        tmp_pf = PluginFactory(self.logging_service) # Uses register_service under the hood
        with self.assertRaises(ServiceAlreadyRegisteredException):
            tmp_pf.register_service("logging", self.logging_service)

    def test_load(self):
        self.logger.debug("test_load")
        tmp_pf = PluginFactory(self.logging_service)
        tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")

    def test_load_repeat(self):
        self.logger.debug("test_load")
        tmp_pf = PluginFactory(self.logging_service)
        tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")
        with self.assertRaises(PluginAlreadyLoadedException):
            tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")

    def test_load_no_plugin(self):
        self.logger.debug("test_load_no_plugin")
        tmp_pf = PluginFactory(self.logging_service)
        with self.assertRaises(TypeError):
            tmp_pf.load("kneedeepio.plugins.services", "ConfigurationService")

    def test_load_missing_service(self):
        self.logger.debug("test_load_missing_service")
        tmp_pf = PluginFactory(self.logging_service)
        with self.assertRaises(ServiceNotRegisteredException):
            tmp_pf.load("tests.plugins.manager.test_pluginfactory", "MockPlugin")

    def test_load_with_callback(self):
        self.logger.debug("test_load_with_callback")
        tmp_pf = PluginFactory(self.logging_service)
        tmp_pf.register_load_callback(callback_method)
        # NOTE: How can one check if the callback method was actually called?
        tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")

    def test_unload(self):
        self.logger.debug("test_unload")
        tmp_pf = PluginFactory(self.logging_service)
        tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")
        tmp_pf.unload("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")

    def test_unload_no_plugin(self):
        self.logger.debug("test_unload_no_plugin")
        tmp_pf = PluginFactory(self.logging_service)
        with self.assertRaises(PluginNotLoadedException ):
            tmp_pf.unload("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")

    def test_unload_with_callback(self):
        self.logger.debug("test_unload_with_callback")
        tmp_pf = PluginFactory(self.logging_service)
        tmp_pf.register_unload_callback(callback_method)
        tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")
        # NOTE: How can one check if the callback method was actually called?
        tmp_pf.unload("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")

    def test_tick_plugins(self):
        self.logger.debug("test_tick_plugins")
        tmp_pf = PluginFactory(self.logging_service)
        tmp_pf.load("kneedeepio.plugins.plugin", "ExampleLoggingPlugin")
        # NOTE: How can one check if the tick method in the plugin was actually called?
        tmp_pf.tick_plugins()