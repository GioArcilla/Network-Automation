# Network-Automation
Intended for Cisco IOS networks. Tasks like config backups, health checks, interface audits, and VLAN deployment across access, distribution, and core switches. Scalable, production-ready.

## Overview
This repository demonstrates practical network automation workflows for Cisco IOS
based environments using Python.
It focuses on real operational tasks commonly performed by network engineers in
enterprise networks—access, distribution, and core layers.
Rather than toy examples, these scripts are designed to reflect day-to-day
activities such as configuration backup, health monitoring, interface auditing, and
controlled configuration deployment.

## Key Features
- Configuration Backups
- Health Monitoring
- Interface Auditing
- VLAN Deployment

## Baseline Configuration
- Jinja2 template for standardized network settings
- NTP
- Syslog
- Banners
- Global best practices

## Tools/Resources List
- Python 3
- Netmiko
- Jinja2 
- YAML 
- TextFSM / NTC Templates
- Rich / Tabulate 

## Principles
- Idempotent operations
- Read-before-write
- Role-based device handling
- Centralized inventory
- Clear logging and error handling
- Separation of data, logic, and templates

## Structuring Details
- Easy to read
- Easy to extend
- Easy to refactor into frameworks like Ansible or Nornir

## Common Use Cases
- EOD automated configuration backups
- Daily health checks across access, distribution, and core layers
- Auditing access switches for error-prone ports
- Safely deploying VLANs across multiple switches
- Enforcing baseline configurations

## Getting Started
1. Clone the repository
2. Populate inventory/devices.yaml
3. Set credentials via environment variables
4. Run scripts from the scripts/ directory
Note: All scripts are designed to fail safely and report errors clearly.

## Roadmap / Future Enhancements
- Config drift detection
- Automated remediation actions
- Role-based baseline deployment
- Integration with monitoring systems
- Migration to Nornir / Ansible inventory models

## Why This Repo Exists
This exists to demonstrate deployable network automation, not just Python
syntax.

## Disclaimer
All scripts are intended for dry-runs and isolated environments unless properly tested and
validated for production use.

## Version History
- 1-31-2026: Initial version
