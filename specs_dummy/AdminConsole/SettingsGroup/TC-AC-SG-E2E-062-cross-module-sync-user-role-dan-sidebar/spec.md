---
id: TC-AC-SG-E2E-062-cross-module-sync-user-role-dan-sidebar
title: "Sinkronisasi lintas modul: popup Select Group di User, kolom Group di Role, dan sidebar modul downstream"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-124
  - TC-AC-SG-125
  - TC-AC-SG-126
coverage:
  web: automated
---

# Sinkronisasi lintas modul: popup Select Group di User, kolom Group di Role, dan sidebar modul downstream

## Prerequisites

- Login sebagai Role: Total Control
- Modul Settings > User dan Settings > Role & Permission aktif

## Test Steps

### Sinkronisasi ke Popup Select Group (User)
1. Buat group baru `"Node Sync E2E"` di `Settings > Group`
2. Navigasi ke `Settings > User > Detail User > Tab Role > Assign Group Role`
3. Buka popup `"Select Group"`
4. Verifikasi node baru `"Node Sync E2E"` muncul di daftar popup Select Group (sumber data tunggal tanpa duplikasi)
### Sinkronisasi Rename ke Kolom Group (Role)
5. Kembali ke `Settings > Group` dan rename node menjadi `"Node Sync Renamed"`
6. Buka `Settings > Role & Permission > Group Role Detail`
7. Verifikasi nama group yang tertera langsung ter-update mengikuti nama baru via Foreign Key
### Sinkronisasi Rename ke Sidebar Modul Lain
8. Buka sidebar group di Distributor/Partner/Client Detail atau User List
9. Verifikasi nama baru `"Node Sync Renamed"` seketika muncul di seluruh sidebar konsumen

## Notes

- TC-AC-SG-127 s/d 129 dicakup pada pengujian integrasi backend.
