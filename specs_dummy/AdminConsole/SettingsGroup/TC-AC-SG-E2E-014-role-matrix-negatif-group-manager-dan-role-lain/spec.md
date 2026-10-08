---
id: TC-AC-SG-E2E-014-role-matrix-negatif-group-manager-dan-role-lain
title: "Role Matrix Negatif: Penolakan akses menu Settings > Group untuk Group Manager, Client, dan role lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-21
  - TC-AC-SG-26
coverage:
  web: automated
---

# Role Matrix Negatif: Penolakan akses menu Settings > Group untuk Group Manager, Client, dan role lain

## Prerequisites

- User A: Group Manager pada ≥1 node (tanpa Global Role Manage group dan tanpa tier TC/RO)
- User B: Administrator pada entitas bertipe Client
- User C: User entitas tanpa wewenang Global Role GS/AC

## Test Steps

### Penolakan Akses Menu & Direct URL
1. Lakukan pengujian berikut untuk User A, User B, dan User C:
2. Login ke sistem dan amati menu navigasi sidebar aplikasi
3. Verifikasi menu `Settings > Group` tidak tampil (Hidden total)
4. Akses URL langsung halaman `Settings > Group` via address bar browser
5. Verifikasi akses ditolak (dialihkan ke halaman 403 Forbidden atau Dashboard)
6. Khusus User A (Group Manager), verifikasi panggilan langsung ke endpoint `/groups` mengembalikan HTTP 403 Forbidden

## Notes

- Group Manager hanya memegang Peran Grup lokal, bukan Peran Global (PRD §2.1 & GAP-ACSG-E2E-001).
