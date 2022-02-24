#!/usr/bin/env python3

### IMPORTS ###
import abc
#import logging

from kneedeepio.plugins.core import ConfigurationService
from kneedeepio.plugins.core import LoggingService
#from kneedeepio.plugins.core import MetricsReportingService
from kneedeepio.plugins.core import ObjectDatastoreService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Plugin(metaclass = abc.ABCMeta):
    def __init__(self, config_srv, logging_srv, metrics_srv, object_srv):
        if isinstance(config_srv, ConfigurationService):
            self.config = config_srv
        else:
            raise TypeError("Invalid object passed as Configuration Service")

        if isinstance(logging_srv, LoggingService):
            self.logger = logging_srv
        else:
            raise TypeError("Invalid object passed as Loggin Service")

        # if isinstance(metrics_srv, MetricsReportingService):
        #     self.metric = metrics_srv
        # else:
        #     raise TypeError("Invalid object passed as Metrics Reporting Service")

        if isinstance(object_srv, ObjectDatastoreService):
            self.object = object_srv
        else:
            raise TypeError("Invalid object passed as Object Datastore Service")

        self.logger.debug("Plugin Initialized: %s", type(self).__name__)

    @abc.abstractmethod
    def setup(self):
        # This method should do whatever is needed to initialize the plugin's operation.
        raise NotImplementedError

    @abc.abstractmethod
    def tick(self):
        # FIXME: Pick a better name for this
        # This method should do some small piece of work for the plugin.
        raise NotImplementedError

    @abc.abstractmethod
    def teardown(self):
        # This method should do whatever is needed to un-setup the plugin, stopping operation.
        raise NotImplementedError

class ExamplePlugin(Plugin):
    def __init__(self, config_srv, logging_srv, metrics_srv, object_srv):
        super().__init__(config_srv, logging_srv, metrics_srv, object_srv)
        self.logger.debug("Inputs - config_srv: %s, logging_srv: %s, metrics_srv: %s, object_srv: %s",
                          config_srv, logging_srv, metrics_srv, object_srv)

    def setup(self):
        # This method should do whatever is needed to initialize the plugin's operation.
        self.logger.debug("setup method")

    def tick(self):
        # FIXME: Pick a better name for this
        # This method should do some small piece of work for the plugin.
        self.logger.debug("tick method")

    def teardown(self):
        # This method should do whatever is needed to un-setup the plugin, stopping operation.
        self.logger.debug("teardown method")