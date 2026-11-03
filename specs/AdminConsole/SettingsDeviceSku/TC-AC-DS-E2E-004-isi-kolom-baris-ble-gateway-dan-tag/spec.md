---
id: TC-AC-DS-E2E-004-isi-kolom-baris-ble-gateway-dan-tag
title: "Isi Kolom Baris SKU BLE Gateway dan TAG (User TAG dan Object)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-10
  - TC-AC-DS-11
  - TC-AC-DS-12
coverage:
  web: automated
---

# Isi Kolom Baris SKU BLE Gateway dan TAG (User TAG dan Object)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`BLE-KIN-GW1`, `TAG-ARC-USR`, `TAG-ARC-OBJ`) dan seed #30 (129 SKU Principal); General Settings #35 (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta, tidak diubah spec ini). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-10: Baris SKU BLE Gateway

1. Ketik Search `BLE-KIN-GW1`, tekan Enter
2. Verifikasi Device Name baris `BLE-KIN-GW1` adalah `BLE Gateway`
3. Verifikasi SKU `BLE-KIN-GW1` tampil pada baris
4. Verifikasi Category badge `BLE Gateway`
5. Verifikasi Brand badge `Kinetia`
6. Verifikasi Model/Type badge `GW-1`
7. Verifikasi Current Stock `8`
8. Verifikasi Last Modified `12/09/26 16:20`

### TC-AC-DS-11: Baris SKU TAG dengan This is User TAG dicentang

9. Ganti isi kotak search dengan `TAG-ARC-USR`, tekan Enter
10. Verifikasi Device Name baris `TAG-ARC-USR` adalah `Wearable TAG`
11. Verifikasi SKU `TAG-ARC-USR` tampil pada baris
12. Verifikasi Category badge `Wearable TAG`
13. Verifikasi Brand badge `Arcturus`
14. Verifikasi Model/Type badge `T-USR`
15. Verifikasi Current Stock `500`
16. Verifikasi Last Modified `30/08/26 08:00`

### TC-AC-DS-12: Baris SKU TAG tanpa User TAG dan stok 0

17. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
18. Verifikasi Device Name baris `TAG-ARC-OBJ` adalah `Asset TAG`
19. Verifikasi SKU `TAG-ARC-OBJ` tampil pada baris
20. Verifikasi Category badge `Asset TAG`
21. Verifikasi Brand badge `Arcturus`
22. Verifikasi Model/Type badge `T-OBJ`
23. Verifikasi Current Stock `0`
24. Verifikasi Last Modified `30/08/26 08:05`
25. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-10, TC-11, TC-12.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 9, 17 (Search untuk menemukan baris target; TC menulis "cari baris pada halaman List, pindah halaman bila perlu", spec memakai Search agar baris pasti ditemukan, R-16) dan langkah 25 (mengosongkan Search sebelum spec berakhir).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal dan nilai Pre-setup #29/#30 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 dan #35 di environment belum diverifikasi.
  - TC-11 dan TC-12 tidak menyebut kolom TAG Type pada Expected (kolom itu default Hidden); spec tidak mengasersinya.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
