---
id: TC-AC-DS-E2E-024-distributor-kontrol-baris-sku-principal-disabled
title: "Distributor: Aksi Delete Hilang dan Checkbox Disabled pada Baris SKU Principal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-80
  - TC-AC-DS-81
coverage:
  web: automated
---

# Distributor: Aksi Delete Hilang dan Checkbox Disabled pada Baris SKU Principal

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun blok 1 login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun blok 2 diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-80 | Delete-Only Distributor PT Cakra Distribusi (Pre-setup #14) | `manageSkuDistD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_D_PASSWORD` |
| 2 | TC-AC-DS-81 | Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Pre-setup #10) | `totalControlDist_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100`, `TAG-ARC-OBJ` stok 0) dan seed #30, SKU Distributor #31 (`LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`), Selection Limit #36 (nilai awal 1000, tidak diubah spec ini). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_DIST_D_PASSWORD` dan `AC_DS_DIST_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### Blok 1: Delete-Only Distributor (TC-AC-DS-80)

1. Ketik Search `TAG-ARC-OBJ`, tekan Enter
2. Klik ⋯ pada baris `TAG-ARC-OBJ`
3. Verifikasi menu hanya memuat `Detail`; `Delete` tidak tersedia pada baris SKU Principal
4. Tutup menu aksi
5. Hover checkbox baris `TAG-ARC-OBJ`
6. Verifikasi checkbox bulk baris `TAG-ARC-OBJ` tampil (visible) dan berstatus disabled
7. Verifikasi tooltip "You don't have permission to do this." tampil
8. Coba klik checkbox baris `TAG-ARC-OBJ`
9. Verifikasi baris `TAG-ARC-OBJ` tidak tercentang
10. Klik `(←)` pada kotak Search

### Blok 2: Total Control Distributor (TC-AC-DS-81)

11. Ganti akun: Logout dari akun Delete-Only Distributor
12. Login sebagai Total Control Distributor `totalControlDist_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_PASSWORD`
13. Buka halaman `Settings > Device > Device SKU`
14. Ketik Search `R-`, tekan Enter
15. Hover checkbox baris `HHR-ARC-100`
16. Verifikasi checkbox baris `HHR-ARC-100` tampil (visible) dan berstatus disabled
17. Verifikasi tooltip "You don't have permission to do this." tampil
18. Coba klik checkbox baris `HHR-ARC-100`
19. Verifikasi baris `HHR-ARC-100` tidak tercentang
20. Klik checkbox header
21. Verifikasi baris `LOC-NOR-01`, `LOC-NOR-02`, dan `LOC-NOR-03` tercentang
22. Verifikasi baris SKU Principal `HHR-ARC-100` tidak tercentang
23. Verifikasi counter bar menampilkan "3 SKUs selected" dan tidak menghitung baris Principal
24. Hilangkan centang checkbox header
25. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun blok 1 login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-80, TC-81.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 14 (Search untuk menemukan baris target; langkah 14 memakai `R-` agar `HHR-ARC-100` dan `LOC-NOR-01` sampai `LOC-NOR-03` berada pada satu halaman, R-16), 2, 5, 8, 15, 18, 20 (aksi yang hasilnya diasersi pada langkah berikutnya), 4, 10, 24, 25 (menutup menu, mengosongkan Search, dan menghilangkan seleksi, S-09), 11 sampai 13 (ganti akun dan membuka halaman).
- Langkah 3 dan 21 sampai 23 mengasersi keadaan yang ada sesudah aksi (S-14): menu dibuka pada langkah 2, seleksi header dilakukan pada langkah 20.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#31 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #10, #14, #29, #31, dan #36 di environment belum diverifikasi.
  - TC-81 Pre-setup #36 (Selection Limit) disebut di Precondition tetapi tidak diubah atau diasersi; spec hanya mencantumkannya sebagai data yang dibaca.
  - TC-81 langkah 4 menyebut "seluruh baris milik Distributor di halaman aktif"; spec memakai Search `R-` (kode `HHR-ARC-100` dan `LOC-NOR-*` sama-sama memuat `R-`) agar semua baris berada di halaman aktif; perilaku pencocokan substring Search belum diverifikasi.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
