---
id: TC-AC-DN-E2E-098-usage-filter-bagian-2
title: "Usage by Company: Sinkron Chip Entity Type dan Filter Rentang Total SKU/Total Stock"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-639
  - TC-AC-DN-263
coverage:
  web: automated
---

# Usage by Company: Sinkron Chip Entity Type dan Filter Rentang Total SKU/Total Stock

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

### TC-AC-DN-639: Sinkron dua arah chip dan checkbox pada field filter Entity Type tabel Usage by Company

2. Klik ikon Filter pada toolbar tabel Usage
3. Klik field `Entity Type`, centang `Distributor` dan `Client`
4. Verifikasi dua chip tampil pada field Entity Type
5. Tutup dropdown `Entity Type` dengan klik area kosong pada Filter Panel
6. Klik ikon `(✕)` pada chip `Distributor` tanpa membuka dropdown
7. Verifikasi chip `Distributor` hilang
8. Klik field `Entity Type`
9. Verifikasi checkbox `Distributor` tidak tercentang
10. Verifikasi chip `Client` tetap ada
11. Hilangkan centang `Client` dari dalam dropdown yang terbuka
12. Verifikasi chip `Client` hilang
13. Centang `Distributor` kembali, lalu klik `[Apply]`
14. Verifikasi tabel menampilkan 2 baris: `Company B` (`Distributor` dan `Client`) dan `Company D` (`Distributor`)
15. Klik ikon Filter pada toolbar tabel Usage
16. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-263: Filter rentang Total SKU dan Total Stock pada Usage by Company

17. Klik ikon Filter pada toolbar tabel Usage
18. Isi field `Total SKU` Min `2` dan Max `3`, lalu klik `[Apply]`
19. Verifikasi baris `Company A` (3) dan `Company B` (2) tampil
20. Klik ikon Filter pada toolbar tabel Usage
21. Klik `[Clear Field]`, isi field `Total Stock` Min `5` dan Max `12`, lalu klik `[Apply]`
22. Verifikasi baris `Company C` (6) dan `Company E` (12) tampil
23. Klik ikon Filter pada toolbar tabel Usage
24. Klik `[Clear Field]`
25. Verifikasi kedua field range menampilkan placeholder `Min` dan `Max`
26. Klik `[Apply]`
27. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): `[Clear Field]` lalu `[Apply]` untuk melepas filter di antara blok dan sebelum menutup dialog, serta membuka kembali Filter Panel setelah `[Apply]`. Penutup `[X]` pada akhir spec membuang state tabel Usage.
- Asersi placeholder `Min` dan `Max` (TC-AC-DN-263 butir c) diperiksa sesudah `[Clear Field]` (langkah 25), karena placeholder hanya tampil pada field kosong (S-15).
- Dropdown `Entity Type` ditutup (langkah 5) sebelum klik `(✕)` chip dan dibuka lagi (langkah 8) sebelum asersi checkbox `Distributor`, karena checkbox hanya teramati pada dropdown terbuka (S-15).
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - TC-AC-DN-639 mengasersi checkbox `Distributor` tidak tercentang tanpa langkah membuka field, dan TC-AC-DN-263 butir c mengasersi placeholder `Min`/`Max` tanpa mengosongkan field; spec menambah langkah penghubung (S-15).
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - TC-AC-DN-639 dan TC-AC-DN-263 hanya menyebut "terapkan filter" atau "panel menerapkan filter"; spec memakai tombol `[Apply]` sesuai TC-AC-DN-630.
