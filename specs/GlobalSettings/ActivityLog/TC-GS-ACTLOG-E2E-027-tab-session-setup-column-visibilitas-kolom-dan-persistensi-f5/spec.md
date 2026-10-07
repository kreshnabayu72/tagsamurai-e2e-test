---
id: TC-GS-ACTLOG-E2E-027-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5
title: "Tab Session Setup Column: Pengaturan Visibilitas 10 Kolom Hideable dan Persistensi F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-96
coverage:
  web: automated
---

# Tab Session Setup Column: Pengaturan Visibilitas 10 Kolom Hideable dan Persistensi F5

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab Session

## Test Steps

### Uji Visibilitas 10 Kolom Hideable
1. Buka popup Setup Column Tab Session.
2. Lakukan pengujian untuk masing-masing dari 10 kolom: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device / Browser:
   a. Hilangkan centang pada kolom.
   b. Verifikasi kolom hilang pada tabel pratinjau di balik popup.
   c. Klik [Save].
   d. Verifikasi kolom tersembunyi dari tabel utama.
   e. Lakukan refresh halaman (F5), verifikasi kolom tetap tersembunyi.
   f. Buka kembali popup Setup Column, centang kembali kolom tersebut, klik [Save].
   g. Verifikasi kolom tampil kembali di tabel utama.

## Notes

- Pengaturan visibilitas kolom tersimpan di local cache browser per pengguna.
