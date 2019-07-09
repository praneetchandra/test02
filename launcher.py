"""
basic-service Launcher Script (basic-service/launcher.py)
Author: Peak AI
Tenant: Peak
Created: 2019-07-09
Template Version: 1

This script is included to ensure compatibility with SageMaker deployment requirements.
"""

import subprocess

subprocess.call(["orion-service", "run", "-s", "api.py",
                 "-f", "predict", "-v", "sagemaker"])

