---
id: TC-GS-ROLE-E2E-089-defense-in-depth-keamanan-isolasi-multi-tenant
title: "Pertahanan Mendalam: Keamanan Isolasi Multi-Tenant dan Pencegahan Pembacaan Data Lintas-Client"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-262
coverage:
  web: automated
---

# Pertahanan Mendalam: Keamanan Isolasi Multi-Tenant dan Pencegahan Pembacaan Data Lintas-Client

## Prerequisites

- Multi-tenant context (Client A dan Client B)
- Data Uji: Client A vs Client B data
- Setup Hook: dualTenantContext
- Login sbg Role: Total Control (Ahmad Fauzi) pada Client A
- Client B memiliki user Total Control lain

## Test Steps

### Data Role & Permission client lain tidak dapat dibaca (TC-GS-ROLE-262)

1. Kirim permintaan list Tab Total Control dengan parameter/identitas Client B
2. Amati Tab Total Control Client A
3. Verifikasi Permintaan tidak mengembalikan user Client B
4. Verifikasi Tab Total Control hanya memuat user Client A

## Notes

- Memvalidasi alur skenario "Pertahanan Mendalam: Keamanan Isolasi Multi-Tenant dan Pencegahan Pembacaan Data Lintas-Client".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.11; global-settings/role/PRD/role.md §9.4.3 Must NOT.
- Sumber pemetaan test case granular: TC-GS-ROLE-262.
