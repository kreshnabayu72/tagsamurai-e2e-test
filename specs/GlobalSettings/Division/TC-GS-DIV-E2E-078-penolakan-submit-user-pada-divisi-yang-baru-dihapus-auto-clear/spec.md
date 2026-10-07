---
id: TC-GS-DIV-E2E-078-penolakan-submit-user-pada-divisi-yang-baru-dihapus-auto-clear
title: "Penanganan Submit User pada Divisi yang Baru Dihapus: Pesan Error Field, Auto-Clear Dropdown, dan Refresh Opsi Otomatis"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-253
coverage:
  web: automated
---

# Penanganan Submit User pada Divisi yang Baru Dihapus: Pesan Error Field, Auto-Clear Dropdown, dan Refresh Opsi Otomatis

## Prerequisites

- Login sebagai Role: Total Control
- Form Create User sedang memilih divisi bebas relasi, lalu divisi tersebut dihapus oleh admin lain sebelum form User disubmit
- User berada di Global Settings > User > Division
- Division `Public Relations` sudah dihapus (TC-GS-DIV-116)

## Test Steps

1. Buka form Create User dan buka dropdown Division
2. Verifikasi Opsi `Public Relations` tidak ada pada dropdown Division

## Notes

- Memvalidasi penanganan breaking change §11: submit user dengan divisi yang baru dihapus ditolak dengan error "This division no longer exists. Please select another.", field auto-clear, dan opsi dropdown di-refresh (PRD §11, error-handling-convention.md §5.5).
- Sumber pemetaan test case granular: TC-GS-DIV-253.
