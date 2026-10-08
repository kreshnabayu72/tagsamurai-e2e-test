---
id: TC-GS-ACTLOG-E2E-044-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5
title: "Tab User Action Setup Column: Pengaturan Visibilitas 8 Kolom Hideable dan Persistensi F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-183
coverage:
  web: automated
---

# Tab User Action Setup Column: Pengaturan Visibilitas 8 Kolom Hideable dan Persistensi F5

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab User Action

## Test Steps

### Uji Visibilitas 8 Kolom Hideable
1. Buka popup Setup Column Tab User Action.
2. Lakukan pengujian untuk masing-masing dari 8 kolom: Date, Action, Object, Name, Field, Old Value, New Value, Modified By:
   a. Hilangkan centang pada kolom.
   b. Verifikasi kolom hilang pada tabel pratinjau di balik popup.
   c. Klik [Save].
   d. Verifikasi kolom tersembunyi dari tabel utama.
   e. Lakukan refresh halaman (F5), verifikasi kolom tetap tersembunyi.
   f. Buka kembali popup Setup Column, centang kembali kolom tersebut, klik [Save].
   g. Verifikasi kolom tampil kembali di tabel utama.

## Notes

- Pengaturan visibilitas kolom Tab User Action tersimpan di cache browser pengguna.
