# Enterprise Portal & Virtual Network Lab

A full-stack enterprise infrastructure project that combines software development, networking, virtualization, and cloud technologies.

The project simulates a small business environment with an employee-facing web portal, REST API, segmented enterprise network, virtual machines, and eventually cloud deployment.

## Project Status

🚧 **In Development — Version 1**

Current focus:
- Full-stack application development
- Cisco Packet Tracer network
- VMware virtual environment
- Windows client/server infrastructure

---

## Project Architecture

```text
                    Enterprise Environment
                            |
          +-----------------+-----------------+
          |                                   |
     Network Lab                        Enterprise Portal
          |                                   |
 Cisco Packet Tracer                   HTML / CSS / JS
          |                                   |
   VLAN 10 - HR                         Flask REST API
   VLAN 20 - IT                               |
          |                              Ticket Data
          |                                   |
    Router-on-a-Stick                    PostgreSQL
                                              |
                                          AWS Cloud
                                         (planned)
