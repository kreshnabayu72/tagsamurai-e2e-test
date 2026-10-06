---
id: TC-AC-ACAL-E2E-009-entity-scoping-distributor-partner-principal
title: "Entity Scoping — Isolasi visibilitas log riwayat antar Distributor, Partner, dan Principal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-234
  - TC-AC-ACAL-235
  - TC-AC-ACAL-236
  - TC-AC-ACAL-237
coverage:
  web: automated
---

# Entity Scoping — Isolasi visibilitas log riwayat antar Distributor, Partner, dan Principal

## Prerequisites

- Akun Principal Total Control
- Akun Distributor A ("PT Maju Bersama") dengan Partner A1 ("CV Karya Mandiri") di bawah jaringannya
- Akun Partner A1 ("CV Karya Mandiri")
- Akun Distributor B Rival ("PT Global Tech") yang tidak memiliki relasi jaringan dengan Distributor A
- Telah tercatat aktivitas log Session & User Action pada masing-masing entitas tersebut

## Test Steps

### Visibilitas Distributor A

1. Login sebagai Role: Distributor A Total Control
2. Buka menu `Admin Console > Activity Log`
3. Verifikasi data log yang tampil pada Tab Session dan Tab User Action mencakup aktivitas internal Distributor A dan Partner di bawah jaringannya (Partner A1)
4. Verifikasi tidak ada entri log milik Distributor B Rival yang bocor ke dalam tabel
5. Logout

### Visibilitas Partner A1

6. Login sebagai Role: Partner A1 Total Control
7. Buka menu `Admin Console > Activity Log`
8. Verifikasi data log yang tampil hanya aktivitas milik Partner A1 itu sendiri
9. Verifikasi entri log internal milik Distributor induk (Distributor A) tidak terlihat oleh Partner A1
10. Logout

### Visibilitas Distributor Rival (Distributor B)

11. Login sebagai Role: Distributor B Rival Total Control
12. Buka menu `Admin Console > Activity Log`
13. Verifikasi hanya log milik Distributor B yang tampil, dan 0 data dari Distributor A atau Partner A1 yang terlihat
14. Logout

### Visibilitas Principal (Lintas Seluruh Entitas)

15. Login sebagai Role: Principal Total Control
16. Buka menu `Admin Console > Activity Log`
17. Verifikasi Principal dapat melihat seluruh riwayat log secara terpusat dari Distributor A, Partner A1, dan Distributor B

## Notes

- Memastikan isolasi multi-tenant bekerja sempurna pada surface data audit trail.
