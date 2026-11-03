---
id: TC-AC-DN-E2E-114-setup-column-pin
title: "Setup Column List: Pin dan Unpin Tiap Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-332
coverage:
  web: automated
---

# Setup Column List: Pin dan Unpin Tiap Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti dan #17 seed 120 baris sebagai isi tabel dan Live Preview. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Tabel "Kolom uji" untuk langkah berulang (langkah 2 sampai 7): `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`.
- State global: tidak ada yang diubah; pin tidak disimpan (`[Save]` tidak diklik) dan modal ditutup di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-332: Pin dan unpin tiap kolom List di modal Setup Column

1. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
2. Klik ikon Pin pada kolom uji
3. Verifikasi ikon Pin kolom uji berubah aktif
4. Verifikasi Live Preview membekukan kolom uji di sisi kiri
5. Klik ikon Pin pada kolom uji lagi
6. Verifikasi ikon Pin kolom uji berubah nonaktif
7. Verifikasi Live Preview melepaskan kolom uji
8. Untuk setiap baris tabel "Kolom uji", ulangi langkah 2 sampai 7
9. Klik ikon close `(✕)` pada modal Setup Column

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03): langkah 9 menutup modal tanpa menyimpan.
- Ukuran spec (9 langkah nominal, 6 langkah per iterasi dikali enam kolom ditambah dua langkah pembuka dan penutup, sekitar 38 langkah dengan ekspansi; di atas smell 35 langkah, kode R3 dan bagian 8b butir 7): satu TC, satu topik, parameter tiap iterasi ada di tabel "Kolom uji" tanpa langkah bersyarat, dan `Verifikasi` yang diulang tetap satu per klausa.
- TC-AC-DN-333 dan TC-AC-DN-334 (Pin saat gulir, F5, dan batas pin ke-4) ada di spec 123.
- Temuan untuk QA:
  - TC-AC-DN-332 Expected per kolom memuat tiga klausa (ikon aktif, ikon nonaktif, Live Preview membekukan lalu melepaskan); spec memecahnya per klausa (langkah 3, 4, 6, 7).
