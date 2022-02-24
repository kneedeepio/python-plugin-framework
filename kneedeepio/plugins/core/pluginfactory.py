#!/usr/bin/env python3

### IMPORTS ###
import logging
import importlib

from .configurationservice import ConfigurationService
from .loggingservice import LoggingService
#from .metricsreportingservice import MetricsReportingService
from .objectdatastoreservice import ObjectDatastoreService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class PluginAlreadyLoadedException(Exception):
    pass

class PluginNotLoadedException(Exception):
    pass

# FIXME: Need to add some sort of "service request" mechanism so the plugin can
#        request which services it needs and not have services that aren't needed.
class PluginFactory:
    def __init__(self, config_srv, logging_srv, metrics_srv, object_srv):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Inputs - config_srv: %s, logging_srv: %s, metrics_srv: %s, object_srv: %s",
                          config_srv, logging_srv, metrics_srv, object_srv)

        if isinstance(config_srv, ConfigurationService):
            self.configuration_service = config_srv
        else:
            raise TypeError("Invalid object passed as Configuration Service")

        if isinstance(logging_srv, LoggingService):
            self.logging_service = logging_srv
        else:
            raise TypeError("Invalid object passed as Logging Service")

        # if isinstance(metrics_srv, MetricsReportingService):
        #     self.metrics_reporting_service = metrics_srv
        # else:
        #     raise TypeError("Invalid object passed as Metrics Reporting Service")

        if isinstance(object_srv, ObjectDatastoreService):
            self.object_datastore_service = object_srv
        else:
            raise TypeError("Invalid object passed as Object Datastore Service")

        # FIXME: What data structure to use in the registry?
        #        Would this work?
        #           {
        #               "module_name": "example.plugins",
        #               "class_name": "ExamplePlugin"
        #               "instance": <ExamplePlugin ...>
        #           }
        #        Is version tracking needed?
        self._plugin_registry = []
        self._load_callbacks = []
        self._unload_callbacks = []

    def load(self, module_name, class_name):
        self.logger.debug("Inputs - module_name: %s, class_name: %s", module_name, class_name)
        # Check if plugin is already loaded
        for loaded_plugin in self._plugin_registry:
            if loaded_plugin["module_name"] == module_name and loaded_plugin["class_name"] == class_name:
                raise PluginAlreadyLoadedException
        # Import the plugin
        tmp_module = importlib.import_module(module_name)
        self.logger.debug("tmp_module: %s", tmp_module)
        # Create an instance of the plugin
        tmp_class = getattr(tmp_module, class_name)
        self.logger.debug("tmp_class: %s", tmp_class)
        # FIXME: How to check the plugin is subclass of Plugin?
        tmp_instance = tmp_class(
            config_srv = self.configuration_service,
            logging_srv = self.logging_service,
            metrics_srv = None,
            object_srv = self.object_datastore_service
        )
        self.logger.debug("tmp_instance: %s", tmp_instance)
        # Store the instance in the registry list
        self._plugin_registry.append({
            "module_name": module_name,
            "class_name": class_name,
            "instance": tmp_instance
        })
        # Run the plugin instance setup
        tmp_instance.setup()
        # Call the load callbacks
        for cb in self._load_callbacks:
            cb(tmp_instance)
        # FIXME: What needs to be done to "run" the plugins?

    def unload(self, module_name, class_name):
        self.logger.debug("Inputs - module_name: %s, class_name: %s", module_name, class_name)
        # Check if plugin is already loaded
        tmp_plugin = None
        for loaded_plugin in self._plugin_registry:
            if loaded_plugin["module_name"] == module_name and loaded_plugin["class_name"] == class_name:
                tmp_plugin = loaded_plugin
        if tmp_plugin is None:
            raise PluginNotLoadedException
        # FIXME: What needs to be done to "stop running" the plugins?
        # Call the unload callbacks
        for cb in self._unload_callbacks:
            cb(tmp_plugin["instance"])
        # Run the plugin instance teardown
        tmp_plugin["instance"].teardown()
        # Remove the instance from the registry
        self._plugin_registry.remove(tmp_plugin)
        # FIXME: How to un-import the plugin module?
        #        Is the un-import necessary?
        #        Have to check to make sure there aren't any other classes using
        #           the same module.

    def register_load_callback(self, callback_method):
        self.logger.debug("Inputs - callback_method: %s", callback_method)
        # Add the callback method to the list of methods to call back on plugin load.
        # The callback method should take one argument: the instance of the plugin.
        self._load_callbacks.append(callback_method)

    def register_unload_callback(self, callback_method):
        self.logger.debug("Inputs - callback_method: %s", callback_method)
        # Add the callback method to the list of methods to call back on plugin unload.
        # The callback method should take one argument: the instance of the plugin.
        self._unload_callbacks.append(callback_method)

    def tick_plugins(self):
        self.logger.debug("Inputs - None")
        # Call the tick function for each of the plugins.
        # FIXME: Should the be renamed to a "heartbeat"?
        for item in self._plugin_registry:
            item["instance"].tick()