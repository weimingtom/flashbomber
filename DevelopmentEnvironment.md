# Note #

**Draft page**

This page describes development environment installation & configuration for the project. At the moment only Windows platform is covered, but there should be no problem creating equivalent system for Mac & Linux.

# Windows #

**Download & install Subversion client**

  * Such as TortoiseSVN 1.5.3 (or newer)

**Download & install Flex SDK**

  * suggested location `c:\FlexSDK`
  * add \bin directory to PATH

**Download & install Java Development Kit (JDK 1.6.0 or newer)**

  * default location
  * add \bin directory to PATH

**Download & install Apache Ant (1.7.0 or newer)**

  * unpack to `C:\Program Files`
  * copy file `flexTasks.jar` from `C:\FlexSDK\ant\lib` to `C:\Program Files\apache-ant-1.7.1\lib`

**Download & install Cygwin**

> This is optional, but quite helpful. Better command line and utilities.

**Editor or IDE for development**

  * suggestion: jEdit

**Set up local build properties**

  * copy `local.build.properties_template´ to `local.build.properties`
  * change the `local.build.properties` file contents to match your environment

**How to build the application**

  * run "ant" in the project directory, it will run "compile" as default target

**How to test the application**

> with web browser go to:

  * open the `flashbomberman\flash\build\bomberman.swf` in web browser