---
id: TC-AC-DS-E2E-191-sort-list-last-modified-oldest-dan-newest-first
title: "Sort List: Last Modified Oldest First dan Newest First"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-338
coverage:
  web: automated
---

# Sort List: Last Modified Oldest First dan Newest First

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Pemulihan Last Modified Pre-setup ke keadaan awal dijamin fixture BE yang disediakan tim FE/BE dan dinyatakan di `suite.md`. Nilai Last Modified dibaca dari tabel saat run, bukan ditulis sebagai literal.
- Nilai Last Modified terkecil dan terbesar masing-masing dimiliki satu baris (TAG-ARC-USR dan HHR-ARC-100 menurut Pre-setup #29), sehingga kesamaan baris pertama dan terakhir tidak bergantung pada urutan baris seri. Halaman 1 pada Oldest First dan pada Newest First memuat sedikitnya dua nilai Last Modified berbeda (S-11).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.settingsDeviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Sort kembali netral di langkah 15.

## Test Steps

1. Klik header kolom Last Modified sekali
2. Verifikasi Oldest First: Last Modified baris pada halaman 1 berurut menaik
3. Catat baris pertama halaman 1 (SKU dan Last Modified) sebagai O_pertama
4. Klik nomor halaman terakhir pada Pagination
5. Catat baris terakhir halaman terakhir (SKU dan Last Modified) sebagai O_terakhir
6. Klik nomor halaman 1 pada Pagination
7. Klik header kolom Last Modified sekali lagi
8. Verifikasi Newest First: Last Modified baris pada halaman 1 berurut menurun
9. Catat baris pertama halaman 1 (SKU dan Last Modified) sebagai N_pertama
10. Klik nomor halaman terakhir pada Pagination
11. Catat baris terakhir halaman terakhir (SKU dan Last Modified) sebagai N_terakhir
12. Verifikasi baris pertama saat Oldest First (O_pertama) sama dengan baris terakhir halaman terakhir saat Newest First (N_terakhir)
13. Verifikasi baris pertama saat Newest First (N_pertama) sama dengan baris terakhir halaman terakhir saat Oldest First (O_terakhir)
14. Klik nomor halaman 1 pada Pagination
15. Klik header kolom Last Modified sekali lagi
16. Verifikasi kembali ke urutan default SKU A-Z: baris pertama `BLE-KIN-GW1`

## Notes

- Sumber TC-AC-DS-336 dan TC-AC-DS-337 ada di spec TC-AC-DS-E2E-098.
- Asersi sort memakai hubungan relatif (berurut menaik atau menurun pada halaman 1; baris pertama sama dengan baris terakhir halaman terakhir pada arah sebaliknya), tidak memakai nilai Last Modified literal (A-11). Expected butir a dan b TC-AC-DS-338 dipecah per klausa: urutan halaman 1 (langkah 2 dan 8) dan kesamaan baris pertama dengan baris terakhir arah sebaliknya (langkah 12 dan 13), yang menunggu pencatatan kedua arah.
- Langkah penghubung tanpa `Verifikasi` (S-03, S-14): langkah 3, 5, 9, dan 11 (mencatat baris), langkah 4, 6, 10, dan 14 (pindah halaman agar baris pertama dan terakhir halaman terakhir teramati dan header diklik dari halaman 1).
- Pengecualian S-12 A-11: `BLE-KIN-GW1`, `TAG-ARC-USR`, dan `HHR-ARC-100` adalah SKU Pre-setup bernama literal tanpa suffix (dinyatakan di `suite.md`); tidak ada data yang diubah spec ini.
- Temuan untuk QA:
  - TC 338 Expected butir c ("default SKU A-Z") tidak menyebut baris yang diamati; spec mempertahankan asersi baris pertama `BLE-KIN-GW1` pada urutan A-Z Pre-setup.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.settingsDeviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
