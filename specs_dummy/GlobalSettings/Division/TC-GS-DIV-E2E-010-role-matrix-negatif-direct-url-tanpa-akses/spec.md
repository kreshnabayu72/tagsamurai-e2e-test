---
id: TC-GS-DIV-E2E-010-role-matrix-negatif-direct-url-tanpa-akses
title: "Akses Langsung Direct URL Tab Division Tanpa Capability Ditolak dengan Toast 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-25
coverage:
  web: automated
---

# Akses Langsung Direct URL Tab Division Tanpa Capability Ditolak dengan Toast 403

## Prerequisites

- Login sebagai Role: System Role Tanpa Capability
- Login sebagai Role: System Role tanpa capability Manage user and role
- URL Tab Division disalin dari akun Total Control

## Test Steps

1. Salin URL Tab Division dari akun Total Control
2. Login sbg aktor tanpa capability lalu tempel URL tersebut di address bar
3. Verifikasi Toast error `You don't have permission to do this.`
4. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tersembunyi, tanpa redirect ke halaman terpisah
5. Verifikasi Data Division tidak tampil

## Notes

- Memvalidasi penolakan direct URL navigasi: muncul toast error "You don't have permission to do this.", elemen tidak berhak tetap tersembunyi, dan data tidak bocor (PRD §9.3, §9.11).
- Sumber pemetaan test case granular: TC-GS-DIV-25.
