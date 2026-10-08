---
id: TC-GS-USER-E2E-004-create-user-scan-pair-tag
title: Buat user dengan Scan dan Pair TAG menampilkan TAG terverifikasi di list
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-475
coverage:
  web: automated
---

# Buat user dengan Scan dan Pair TAG menampilkan TAG terverifikasi di list

## Prerequisites

- Login sebagai Role: Total Control
- Kolom TAG terlihat lewat Setup Column
- TAG "RFID-00321" terdaftar untuk client ini dan belum dipasangkan ke user mana pun
- Division "Finance" ada di master data
- Lingkungan uji dapat menyimulasikan scan RFID, karena browser tidak bisa melakukan scan perangkat keras
- TAG "RFID-00321" dalam keadaan belum dipasangkan di awal setiap run, dan pembersihan melepas pasangannya lagi

## Test Steps

1. Klik `[+ User]` untuk membuka modal Create
2. Isi First Name "Taufik", Last Name "Hidayat", Email unik, dan Division "Finance"
3. Pilih Access "Global Settings" saja
4. Scan dan pasangkan TAG "RFID-00321"
5. Verifikasi toast sukses pairing muncul
6. Klik `[Submit]`
7. Verifikasi baris user baru muncul di User List
8. Verifikasi kolom TAG menampilkan "RFID-00321"
9. Verifikasi TAG menampilkan badge hijau "Verified"

## Notes

- Scan TAG adalah scan RFID perangkat keras yang tidak bisa dilakukan browser. Kebutuhan simulasi scan diminta dari tim FE di Prerequisites.
- Kegagalan validasi scan TAG (TC-GS-USER-343, 344, dan 345) dicakup `TC-GS-USER-E2E-032-validasi-scan-tag`.
- User dihapus saat pembersihan.
