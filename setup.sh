#!/usr/bin/env bash

# Shared software-development prerequisites for BuggyBot.
# Hardware-specific and project runtime libraries will be added as needed.

set -euo pipefail

sudo apt-get update
sudo apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-venv

git --version
python3 --version
