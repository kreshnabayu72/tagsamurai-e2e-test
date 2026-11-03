---
id: TC-AC-DS-E2E-130-detail-usage-by-company-scope-distributor
title: "Usage by Company Distributor: Baris Sendiri dan Client dalam Rantai serta Local Registration Nonaktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-436
  - TC-AC-DS-437
  - TC-AC-DS-569
coverage:
  web: automated
---

# Usage by Company Distributor: Baris Sendiri dan Client dalam Rantai serta Local Registration Nonaktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi (Dewi Lestari, Modified By `Dewi L`, Local Registration aktif) `totalControlDist_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, `Spectra.env.AC_DS_TC_PASSWORD`).
- Akun pendamping: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1), dipakai lewat sesi API aktor (login API password, bukan sesi web; disediakan tim BE/FE) untuk menonaktifkan dan mengaktifkan kembali Local Registration `PT Cakra Distribusi`.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU Principal `HHR-ARC-100` serta seed (#29, #30); SKU lokal Distributor `LOC-NOR-01` (Device Name `Rugged Handheld Reader`, Brand `Nordik`, Model/Type `R-01`) (#31); data Usage by Company dan jaringan entitas (#32, #24). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): mengubah Local Registration Distributor lewat sesi API Principal (TC tidak menyebut jalur UI atau endpoint; tidak dikarang); seeding dan pemulihan Pre-setup di atas.
- State global yang diubah: Local Registration `PT Cakra Distribusi` dinonaktifkan pada TC-AC-DS-569 lalu diaktifkan kembali pada langkah 21 dan di hook `after` (tetap jalan walau spec gagal). Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-436: Distributor yang membuka SKU Principal hanya melihat barisnya sendiri dan Client dalam rantainya

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Verifikasi tiga baris berurutan Company A-Z: `PT Cakra Distribusi` 25, `PT Delta Retail` 5 (Client melalui Partner), dan `PT Surya Logistik` 15
4. Verifikasi `PT Arunika Prima`, `PT Mitra Lintas Nusa`, dan Partner murni `CV Karya Mandiri` tidak tampil

### Pemulihan state antar TC

5. Tutup popup dengan ikon close `[✕]`

### TC-AC-DS-437: Distributor yang membuka SKU miliknya melihat barisnya sendiri dan Client dalam rantainya

6. Klik SKU `LOC-NOR-01`
7. Verifikasi dua baris berurutan Company A-Z: `PT Cakra Distribusi` 9 dan `PT Surya Logistik` 5
8. Verifikasi Info Grid SKU `LOC-NOR-01`, Device Name `Rugged Handheld Reader`, Brand `Nordik`, Model/Type `R-01`

### Pemulihan state antar TC

9. Tutup popup dengan ikon close `[✕]`

### TC-AC-DS-569: Local Registration nonaktif tidak mengubah baris Usage Distributor yang sudah ada

10. Klik SKU `LOC-NOR-01`
11. Verifikasi sebelum perubahan Usage `LOC-NOR-01` dua baris: `PT Cakra Distribusi` 9 dan `PT Surya Logistik` 5
12. Tutup popup dengan ikon close `[✕]`
13. Nonaktifkan Local Registration `PT Cakra Distribusi` lewat sesi API Principal hingga perubahan tersimpan
14. Muat ulang halaman
15. Verifikasi List Device SKU tampil
16. Verifikasi tombol `[+ SKU]` tidak tampil
17. Klik SKU `LOC-NOR-01`
18. Verifikasi Popup `Device SKU Detail` tampil
19. Verifikasi sesudah perubahan Usage `LOC-NOR-01` tetap dua baris: `PT Cakra Distribusi` 9 dan `PT Surya Logistik` 5

### Pemulihan state akhir

20. Tutup popup dengan ikon close `[✕]`
21. Aktifkan kembali Local Registration `PT Cakra Distribusi` lewat sesi API Principal hingga perubahan tersimpan
22. Muat ulang halaman

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 5, 9, 12, 20, 21, dan 22 (S-03, S-09). Langkah 13 dan 21 memakai sesi API aktor Principal (pelaku kedua lewat sesi API, bukan konteks kedua; R-20).
- Langkah 11 memeriksa keadaan sebelum perubahan sesuai Expected 569 butir a; langkah 19 keadaan sesudah. Expected butir b sisi Usage ditutup oleh langkah 19; sisi `[+ SKU]` oleh langkah 16 (anchor: List tampil pada langkah 15).
- Temuan untuk QA:
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100` dan `LOC-NOR-01`; spec mengandalkan keduanya tampil di halaman pertama List Distributor.
  - S-13: jalur untuk mengubah Local Registration Distributor tidak disebut TC ("dengan sesi Principal nonaktifkan"); ditulis sebagai kemampuan yang disediakan tim FE/BE.
  - Fixture rancangan Pre-setup #31, #32, #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_DIST_PASSWORD`, `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
