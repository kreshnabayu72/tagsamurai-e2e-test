---
id: TC-GS-ROLE-E2E-054-security-tenant-isolation-sanitasi-input-dan-guard-notifikasi
title: "Keamanan: Isolasi Multi-Tenant, Sanitasi Payload SQL Injection pada Pencarian, dan Guard Notifikasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-108
  - TC-GS-ROLE-109
  - TC-GS-ROLE-314
  - TC-GS-ROLE-316
coverage:
  web: automated
---

# Keamanan: Isolasi Multi-Tenant, Sanitasi Payload SQL Injection pada Pencarian, dan Guard Notifikasi

## Prerequisites

- Tersedia akun Client A dan Client B yang terpisah
- Login sebagai Role: Total Control Client A

## Test Steps

1. Buka Global Settings > Role & Permission
2. Verifikasi data role, assignment, dan log milik Client B tidak pernah tampil pada sesi Client A (Tenant Isolation)
3. Ketik payload SQL injection pada Search box: ' OR 1=1 --
4. Tekan Enter pada Search box
5. Verifikasi sistem memperlakukan payload sebagai string pencarian biasa tanpa terjadi error database 500 atau kebocoran data (Sanitasi Input)
6. Lakukan pencabutan role pada target user di Client A
7. Periksa notifikasi in-app pada akun target user: verifikasi notifikasi bertipe view-only yang menampilkan tombol [Mark as Read] tanpa tombol navigasi [Detail]
8. Verifikasi modul Global Settings tidak pernah memicu event notifikasi ke Group Manager

## Notes

- Uji keamanan memvalidasi isolasi multi-tenant, sanitasi query, dan kesesuaian payload notifikasi in-app (role.md §9.8, §10.2).
