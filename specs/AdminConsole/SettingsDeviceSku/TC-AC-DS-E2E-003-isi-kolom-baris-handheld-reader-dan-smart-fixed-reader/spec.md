---
id: TC-AC-DS-E2E-003-isi-kolom-baris-handheld-reader-dan-smart-fixed-reader
title: "Isi Kolom Baris SKU Handheld Reader (Stok Lebih dari 0 dan Stok 0) dan Smart Fixed Reader"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-7
  - TC-AC-DS-8
  - TC-AC-DS-9
coverage:
  web: automated
---

# Isi Kolom Baris SKU Handheld Reader (Stok Lebih dari 0 dan Stok 0) dan Smart Fixed Reader

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100`, `HHR-ARC-200`, `SFR-VEL-4P`) dan seed #30 (129 SKU Principal); General Settings #35 (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta, tidak diubah spec ini). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-7: Baris SKU Handheld Reader stok lebih dari 0

1. Ketik Search `HHR-ARC-100`, tekan Enter
2. Verifikasi Photo baris `HHR-ARC-100` menampilkan thumbnail foto default
3. Verifikasi Device Name baris `HHR-ARC-100` adalah `UHF Handheld Reader`
4. Verifikasi SKU `HHR-ARC-100` tampil sebagai teks tautan
5. Verifikasi Category badge `UHF Handheld` berformat Badge Primary
6. Verifikasi Brand badge `Arcturus` berformat Badge Dark
7. Verifikasi Model/Type badge `H100` berformat Badge Dark
8. Verifikasi Current Stock `120`
9. Verifikasi Last Modified `01/10/26 09:15`

### TC-AC-DS-8: Baris SKU stok 0 tetap tampil

10. Ganti isi kotak search dengan `HHR-ARC-200`, tekan Enter
11. Verifikasi baris `HHR-ARC-200` tampil di List
12. Verifikasi Device Name baris `HHR-ARC-200` adalah `UHF Handheld Reader`
13. Verifikasi Category badge `UHF Handheld`
14. Verifikasi Brand badge `Arcturus`
15. Verifikasi Model/Type badge `H200`
16. Verifikasi Current Stock `0`, bukan kosong dan bukan `—`
17. Verifikasi Last Modified `28/09/26 14:40`

### TC-AC-DS-9: Baris SKU Smart Fixed Reader

18. Ganti isi kotak search dengan `SFR-VEL-4P`, tekan Enter
19. Verifikasi Device Name baris `SFR-VEL-4P` adalah `4-Port Fixed Reader`
20. Verifikasi SKU `SFR-VEL-4P` tampil pada baris
21. Verifikasi Category badge `Portal Reader`
22. Verifikasi Brand badge `Veltrix`
23. Verifikasi Model/Type badge `SF-4`
24. Verifikasi Current Stock `36`
25. Verifikasi Last Modified `20/09/26 11:05`
26. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-7, TC-8, TC-9.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 10, 18 (Search untuk menemukan baris target; TC menulis "cari baris pada halaman List, pindah halaman bila perlu", spec memakai Search agar baris pasti ditemukan, R-16) dan langkah 26 (mengosongkan Search sebelum spec berakhir).
- Langkah 5 sampai 7 memuat format badge sesuai TC (Badge Primary untuk Category, Badge Dark untuk Brand dan Model/Type).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal dan nilai Pre-setup #29/#30 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 dan #35 di environment belum diverifikasi.
  - TC-7, TC-8, TC-9 menyuruh mencari baris "pada halaman List (pindah halaman bila perlu)"; spec memakai Search sebagai langkah penghubung.
  - TC-9 tidak menyebut badge Photo; spec tidak mengasersinya.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
