# Network-Automation
Intended for Cisco IOS networks. Tasks like config backups, health checks, interface audits, and VLAN deployment across access, distribution, and core switches. Scalable, production-ready.

Overview
This repository demonstrates practical network automation workflows for Cisco IOS
based environments using Python.
It focuses on real operational tasks commonly performed by network engineers in
enterprise networks—access, distribution, and core layers.
Rather than toy examples, these scripts are designed to reflect day-to-day
activities such as configuration backup, health monitoring, interface auditing, and
controlled configuration deployment.

The goal of this project is to showcase:
- Operational thinking
- Safe automation practices
- Reusable, scalable design patterns
- Clean, readable code suitable for production environments

What This Repo Solves
Modern networks demand:
- Consistent configurations
- Visibility into device health
- Faster troubleshooting
- Reduced human error
This project automates repeatable, high-value tasks that are traditionally manual, error
prone, and time-consuming.

network-automation/
├── inventory/
│   └── devices.yaml
├── scripts/
│   ├── backup_configs.py
│   ├── health_check.py
│   ├── vlan_deploy.py
│   └── interface_audit.py
├── templates/
│   └── baseline_config.j2
├── reports/
│   └── health_report.html
└── README.md


Features
Configuration Backups
- Pulls running configurations from Cisco devices
- Stores timestamped, per-device backups
- Enables fast rollback and auditability
  
Health Monitoring
- Collects CPU, memory, uptime, and interface statistics
- Flags warning conditions (errors, high utilization)
- Generates reports (HTML/CSV)

Interface Auditing
Identifies:
- Interfaces with errors (CRC, input/output)
- Active ports missing descriptions
- Potential access-layer issues
Designed for proactive troubleshooting

VLAN Deployment
- Creates VLANs safely and idempotently
- Verifies existing configuration before changes
- Reduces risk during bulk updates

Baseline Configuration
- Jinja2 template for standardized network settings
- Enables consistent deployment of:
-- NTP
-- Syslog
-- Banners
-- Global best practices

Technologies Used:
- Python 3
- Netmiko
- Jinja2 
- YAML 
- TextFSM / NTC Templates
- Rich / Tabulate 

Design Principles
This project intentionally follows best practices used in production environments:
- Idempotent operations
- Read-before-write
- Role-based device handling
- Centralized inventory
- Clear logging and error handling
- Separation of data, logic, and templates
Scripts are structured to be:
- Easy to read
- Easy to extend
- Easy to refactor into frameworks like Ansible or Nornir

Example Use Cases
- EOD automated configuration backups
- Daily health checks across access, distribution, and core layers
- Auditing access switches for error-prone ports
- Safely deploying VLANs across multiple switches
- Enforcing baseline configurations

-Getting Started
1. Clone the repository
2. Populate inventory/devices.yaml
3. Set credentials via environment variables
4. Run scripts from the scripts/ directory
Note: All scripts are designed to fail safely and report errors clearly.

Roadmap / Future Enhancements
- Config drift detection
- Automated remediation actions
- Role-based baseline deployment
- Integration with monitoring systems
- Migration to Nornir / Ansible inventory models

Why This Repo Exists
This project exists to demonstrate deployable network automation skills, not just Python
syntax.
It reflects:
- How enterprise networks are actually operated
- How automation should reduce risk—not introduce it
- How network engineers can bridge traditional networking and modern DevOps
practices

Disclaimer
All scripts are intended for lab and learning environments unless properly tested and
validated for production use.
