# Security

This document outlines security practices for Keirin Prediction AI.

## Supply Chain

- SBOMs are generated with Syft and scanned by Grype during CI.
- Container images are signed with cosign and include lightweight SLSA provenance.

## Application

- Admin routes require JWT authentication with role-based access control.
- Sensitive tokens, API keys, and email addresses are masked in logs to prevent data leakage.
- Known vulnerabilities can be temporarily allow-listed with expiry dates.

## Monitoring

Audit logs are rotated daily and stored for later analysis.
