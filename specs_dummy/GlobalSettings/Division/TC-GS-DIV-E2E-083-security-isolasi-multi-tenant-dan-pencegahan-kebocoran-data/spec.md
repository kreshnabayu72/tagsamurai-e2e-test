---
id: TC-GS-DIV-E2E-083-security-isolasi-multi-tenant-dan-pencegahan-kebocoran-data
title: "Isolasi Total Multi-Tenant: Entitas A Dilarang Melihat atau Mengakses Data Katalog Division Entitas B"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-266
coverage:
  web: automated
---

# Isolasi Total Multi-Tenant: Entitas A Dilarang Melihat atau Mengakses Data Katalog Division Entitas B

## Prerequisites

- Login sebagai Role: Total Control Entitas A dan Entitas B
- Entitas A dan Entitas B terpisah, masing-masing memiliki divisi unik
- Entitas B memiliki Division yang tidak ada di entitas A

## Test Steps

1. Login sbg Total Control entitas A dan buka Tab Division
2. Bandingkan dengan Division milik entitas B
3. Kirim request daftar Division dengan token entitas A
4. Verifikasi Hanya Division milik entitas A yang tampil
5. Verifikasi Division entitas B tidak muncul di tabel, Changelog, maupun hasil request

## Notes

- Memvalidasi batas keamanan isolasi multi-tenant: query tabel, modal changelog, dan API response entitas A tidak pernah membocorkan data divisi milik entitas B (PRD §9.11, entity-isolation.md).
- Sumber pemetaan test case granular: TC-GS-DIV-266.
