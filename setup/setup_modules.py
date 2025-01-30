#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================== #
####    Information     ####
# ------------------------ #
# Version   : V0
# Author    : Kamal Atmeh
# Date      : 18/01/2025

####    Objective        ####
# ------------------------ #
# This script is used to import the required modules
# and to install the module if it is not available

####    To Do         ####
# ------------------------ #

####    Packages        ####
# ------------------------ #
import sys
import subprocess

####    Variables        ####
# ------------------------ #

# Function to install modules if they are not installed yet
def install_modules(module_names: list[str]):
    """Installs and imports the required modules

    Args:
        module_names (list[str]): Modules to import
    """
    for module_name in module_names:
        try:
            __import__(module_name)
        except ImportError:
            print(f"{module_name} is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
            print(f"{module_name} has been installed.")

# List of modules to check and install if needed
modules_to_verify = ["json", "pytest", "requests"]

# Install modules
install_modules(modules_to_verify)