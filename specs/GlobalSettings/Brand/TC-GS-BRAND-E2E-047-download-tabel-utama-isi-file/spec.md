---
id: TC-GS-BRAND-E2E-047-download-tabel-utama-isi-file
title: "Download Tabel Brand: Isi File CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-163
  - TC-GS-BRAND-164
  - TC-GS-BRAND-165
  - TC-GS-BRAND-166
coverage:
  web: automated
---

# Download Tabel Brand: Isi File CSV dan XLSX

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment): 12 brand Client A; referensi Used By (Items) yang dipakai: Vertex Labs `5`, Orion Tech `0`.
- Data Dinamis: Population D-01 (12 brand: `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics`) di-seed lewat API di hook `before` (setara TC-GS-BRAND-1) dengan nama literal; total tabel 24 brand. Dihapus lewat API di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh. Nama literal disengaja (asersi Search dan urutan bergantung pada nama Population; pengecualian S-12): seed idempotent (dilewati bila sudah ada), cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial.
- State global yang dipulihkan di hook `after`: konfigurasi kolom tabel Brand dikembalikan ke default (semua kolom tampil).
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel). Berkas unduhan dihapus di hook `after`.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-163: Download as CSV tanpa filter mengunduh seluruh brand

2. Klik Download
3. Verifikasi popover berisi `Download as CSV` dan `Download as XLSX`
4. Klik `Download as CSV`
5. Verifikasi file `Brand-List.csv` terunduh dan berisi 24 baris (bukan hanya halaman 1)
6. Verifikasi tidak ada toast sukses

### TC-GS-BRAND-166: Isi sel export: Used By (Items) berisi angka

7. Buka isi file `Brand-List.csv` yang diunduh pada langkah 4
8. Verifikasi kolom `Used By (Items)` pada baris Vertex Labs bernilai `5`
9. Verifikasi kolom `Used By (Items)` pada baris Orion Tech bernilai `0` (bukan `-`)
10. Verifikasi seluruh sel kolom `Used By (Items)` berisi angka

### TC-GS-BRAND-164: Download as XLSX dengan search aktif hanya baris tersaring

11. Search `tech`, tekan Enter
12. Klik Download, lalu klik `Download as XLSX`
13. Verifikasi file `Brand-List.xlsx` terunduh dan hanya berisi Harbor Tech dan Orion Tech

### TC-GS-BRAND-165: Kolom tersembunyi tidak ikut terunduh dan kembali setelah di-unhide

14. Hapus keyword Search, tekan Enter
15. Hide kolom Used By (Items) lewat Overlay Column Visibility
16. Klik Download, lalu klik `Download as CSV`
17. Verifikasi file CSV pertama tidak memuat kolom Used By (Items)
18. Unhide kolom Used By (Items) lewat Overlay Column Visibility
19. Klik Download, lalu klik `Download as CSV`
20. Verifikasi file CSV kedua memuat kolom Used By (Items)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec: 163, 166 (keduanya tanpa filter, seluruh data), lalu 164 (search aktif), lalu 165 (mengubah konfigurasi kolom, dipulihkan di langkah 18).
- TC-GS-BRAND-166 membaca berkas `Brand-List.csv` yang sama dengan unduhan TC-GS-BRAND-163 (langkah 4), tanpa unduh ulang: state tabel keduanya identik (tanpa filter, semua kolom, 24 baris), sehingga langkah "Download as CSV" TC-GS-BRAND-166 terpenuhi oleh unduhan itu.
- Langkah penghubung: langkah 14 (menghapus keyword Search TC-GS-BRAND-164 sebelum TC-GS-BRAND-165). Langkah 18 (unhide) sekaligus memulihkan konfigurasi kolom; hook `after` sebagai cadangan.
- Dependensi TC-GS-BRAND-1 pada TC-163 dan TC-164 dipenuhi lewat seeding Population di hook `before`.
- Isi berkas export tabel utama dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f). Download Changelog dan accordion ada di spec `TC-GS-BRAND-E2E-048-download-changelog-dan-item-type-list-isi-file` dan `TC-GS-BRAND-E2E-049-download-device-sku-list-principal-isi-file`.
