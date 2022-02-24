Plugin Architecture Design and Notes
====================================

This plugin architecture is going to be designed to handle plugins for a web application.  This will have to include a
few components: API section, Datastore (likely object aka key-value store) connection, and UI section.  The initial
focus of this plugin framework will be to manage api sections for Python Flask, however the framework will not be
limited to only supporting Python Flask.  Python Flask is great for handling the API aspects of web apps, however most
web apps (and their plugins) have other work that needs to be performed.

Requirements
------------
* Plugins shall be able to contain the following components:
   * API section
   * UI section

* Plugins shall have the following service made available to the plugin:
   * Configuration service
   * Logging service
   * Metrics reporting service
   * Object datastore service (key-value datastore that can handle fairly large values)

* Plugins shall be able to be specified in the following ways:
   * URLs to archive in config file
   * URLs submitted to management API and saved to datastore (persistence through restart)
   * Archives copied to a plugins folder (prevents needing to pull the archives from the internet)

* Manager shall contain the following management APIs:
   * Loading and unloading plugins
   * Enumerating loaded plugins (including how to access API and UI sections of each plugin)

Core Design
-----------
The `kneedeepio.plugins.core` module will provide the underlying functionality of this plugin system.  The core classes
will include the configuration service, logging service, metrics reporting service, and object datastore service.  The
core will also include the plugin loader and the plugin runner.

Configuration Service
~~~~~~~~~~~~~~~~~~~~~

The configuration service makes information available to the plugin that the plugin may need for controlling operation.
The service will be included and accessible from withing the plugin itself.

Logging Service
~~~~~~~~~~~~~~~

Metrics Reporting Service
~~~~~~~~~~~~~~~~~~~~~~~~~

Object Datastore Service
~~~~~~~~~~~~~~~~~~~~~~~~

Plugin Design
-------------

Manager Design
--------------

Open Questions
--------------
* How should federation of plugins for high availability be handled?

* Should this be focused on a microservice model, or have the ability to operate as a monolith?

* Should licensing be included in this?
   * Likely not, licensing should be an exercise for a particular implementation.

* Should the plugin framework provide a logging service, or should each plugin just use Python's logging module
  directly?
