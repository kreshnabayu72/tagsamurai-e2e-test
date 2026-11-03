---
id: TC-AC-DN-E2E-099-usage-search-siklus-clear-dan-empty-state
title: "Usage by Company: Siklus Clear Search dan Empty State Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-594
  - TC-AC-DN-265
coverage:
  web: automated
---

# Usage by Company: Siklus Clear Search dan Empty State Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, ketik, hover, dan membaca urutan baris serta isi sel tabel Usage by Company.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-594: Siklus ikon Clear pada Search dialog Detail: teks terhapus dan tabel reset hanya setelah Enter pada input kosong

2. Klik ikon Search pada toolbar tabel Usage
3. Ketik `Company B`, tekan Enter
4. Verifikasi tabel hanya memuat `Company B`
5. Klik ikon `(✕)` pada input Search
6. Verifikasi teks pada input terhapus dan kolom pencarian tetap terbuka dengan placeholder "Search by company name"
7. Verifikasi tabel masih memuat `Company B` saja
8. Tekan Enter pada input kosong
9. Verifikasi tabel menampilkan lima Company

### TC-AC-DN-265: Filter Usage tanpa hasil menampilkan empty state S-06

10. Ketik `zzz` pada input Search yang terbuka, tekan Enter
11. Verifikasi tabel Usage menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
12. Verifikasi tidak ada baris Company yang tampil
13. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: siklus Clear (TC-AC-DN-594) dahulu; sesudahnya input Search terbuka dan kosong, sehingga TC-AC-DN-265 mengetik `zzz` langsung dan langkah "Klik ikon Search" TC-AC-DN-265 tidak diulang. Penutup `[X]` pada akhir spec adalah langkah penghubung (S-03) yang membuang state Search.
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - Judul TC-AC-DN-265 menyebut "Filter Usage" tetapi langkah dan Expected-nya memakai Search `zzz`; spec mengikuti langkah TC.
