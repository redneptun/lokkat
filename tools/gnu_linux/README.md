README for tools/gnu_linux
==========================

This directory contains:
- QtIFW-3.1.1: This is the Qt Installer Framework for GNU/Linux. It can be used to create an installer for GNU/Linux systems

- qtedit: a small convenience script. You may choose to place it in /usr/bin to use it to edit `.ui` files and automatically convert them afterwards to Python code using pyuic5. Usage requires:
  - Qt5 creator [Installation guide for Ubuntu](https://wiki.qt.io/Install_Qt_5_on_Ubuntu)
  - pyqt5 (can be installed via pip: `pip install pyqt5`)
    - usage: qtedit gui.ui
      - causes the Qt designer to open
      - after closing it, the file is automatically converted to: gui/gui.py