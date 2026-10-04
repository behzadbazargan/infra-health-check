# Infra Health Check

A lightweight Python tool for checking TCP port availability on infrastructure hosts.

It is designed for quick infrastructure troubleshooting and basic network/service
health checks without requiring external dependencies.

## Features

- TCP port connectivity check
- Multiple ports in a single command
- Configurable connection timeout
- Hostname or IP address support
- Clear OK / FAILED output
- Non-zero exit code when one or more checks fail
- No external Python dependencies

## Requirements

- Python 3.9 or newer

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/infra-health-check.git
cd infra-health-check
