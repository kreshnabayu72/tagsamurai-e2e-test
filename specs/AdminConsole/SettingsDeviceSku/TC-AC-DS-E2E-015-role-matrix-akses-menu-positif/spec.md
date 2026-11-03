---
id: TC-AC-DS-E2E-015-role-matrix-akses-menu-positif
title: "Role Matrix Positif: Principal, Distributor, dan Read Only Melihat Menu Device SKU dan Membuka Halaman"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-52
  - TC-AC-DS-53
  - TC-AC-DS-59
coverage:
  web: automated
---

# Role Matrix Positif: Principal, Distributor, dan Read Only Melihat Menu Device SKU dan Membuka Halaman

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun pertama login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun berikutnya diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-52 | Total Control Principal PT Arunika Prima (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| 2 | TC-AC-DS-53 | Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Pre-setup #10) | `totalControlDist_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_PASSWORD` |
| 3 | TC-AC-DS-59 | Read Only Principal PT Arunika Prima (Pre-setup #3) | `readOnlySku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_RO_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100`) dan seed #30 (total 129 SKU Principal, dari seeding), SKU Distributor PT Cakra Distribusi #31 (`LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`), SKU Distributor lain `NUS-LOC-01` dan `MAN-LOC-01` (#31, tidak boleh terlihat). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_TC_PASSWORD`, `AC_DS_DIST_PASSWORD`, dan `AC_DS_RO_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### Blok 1: Total Control Principal (TC-AC-DS-52)

1. Buka menu Settings pada sidebar
2. Verifikasi menu `Settings > Device` tampil pada sidebar untuk Principal
3. Klik Device
4. Klik sub-tab `Device SKU`
5. Verifikasi sub-tab `Device SKU` tersedia
6. Verifikasi List Device SKU tampil dengan toolbar `Search | Filter | Download | Changelog | [+ SKU]`
7. Ketik Search `LOC-NOR`, tekan Enter
8. Verifikasi tidak ada SKU milik Distributor pada List dan tabel menampilkan "No results found"
9. Klik `(←)` pada kotak Search

### Blok 2: Total Control Distributor (TC-AC-DS-53)

10. Ganti akun: Logout dari akun Total Control Principal PT Arunika Prima
11. Login sebagai Total Control Distributor PT Cakra Distribusi `totalControlDist_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_PASSWORD`
12. Buka menu Settings > Device
13. Klik sub-tab `Device SKU`
14. Verifikasi sub-tab `Device SKU` tampil untuk Distributor
15. Ketik Search `LOC-`, tekan Enter
16. Verifikasi List memuat SKU milik Distributor `LOC-NOR-01`, `LOC-NOR-02`, dan `LOC-NOR-03`
17. Verifikasi SKU `NUS-LOC-01` dan `MAN-LOC-01` tidak tampil pada List
18. Klik `(←)` pada kotak Search
19. Verifikasi List memuat 129 SKU Principal (read-only) dan 3 SKU milik Distributor dengan total 132 baris

### Blok 3: Read Only Principal (TC-AC-DS-59)

20. Ganti akun: Logout dari akun Total Control Distributor PT Cakra Distribusi
21. Login sebagai Read Only Principal `readOnlySku_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_RO_PASSWORD`
22. Buka halaman `Settings > Device > Device SKU`
23. Verifikasi List Device SKU tampil dengan baris SKU Principal
24. Klik SKU `HHR-ARC-100`
25. Verifikasi Popup `Device SKU Detail` terbuka
26. Tutup popup dengan ikon close `[✕]`
27. Klik ikon Changelog
28. Verifikasi modal Changelog terbuka
29. Tutup modal Changelog
30. Klik ikon Download
31. Verifikasi overlay Download memuat `Download as CSV` dan `Download as XLSX`
32. Tutup overlay Download

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-52, TC-53, TC-59.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3, 4, 12, 13, 22 (navigasi menu dan sub-tab), 7, 15 (Search yang hasilnya diasersi pada langkah berikutnya), 9, 18 (mengosongkan Search, S-09), 10, 11, 20, 21 (ganti akun), 24, 26, 27, 29, 30, 32 (membuka dan menutup popup, modal, dan overlay).
- Asersi absence langkah 8 didahului langkah 6 (List tampil sebagai anchor) dan hasil Search "No results found"; langkah 17 didahului langkah 16 (SKU milik Distributor tampil sebagai anchor pada List yang sama).
- Langkah 19 membaca total baris List dari Pagination; angka 129 berasal dari seeding Pre-setup #30 dan 3 dari Pre-setup #31 (8b butir 10).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#30/#31 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #3, #10, #29, #30, dan #31 di environment belum diverifikasi.
  - TC-52 Expected c ("tidak ada SKU milik Distributor") tidak menyebut SKU yang dicari; spec memakai Search `LOC-NOR` seperti TC-77 sebagai cara mengamati absence.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
