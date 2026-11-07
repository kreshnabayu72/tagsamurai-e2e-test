---
id: TC-FA-LBL-E2E-146-format-tanggal-jam-dan-timezone-general-settings-di-labels-list-changelog-dan-drawer
title: "Format Tanggal, Jam, dan Timezone General Settings di Labels List, Changelog, dan Drawer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-437
  - TC-FA-LBL-438
  - TC-FA-LBL-439
coverage:
  web: automated
---

# Format Tanggal, Jam, dan Timezone General Settings di Labels List, Changelog, dan Drawer

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Ganti akun di tengah spec (TC-FA-LBL-438): Total Control Company Changelog (Pre-setup #17), `Fixture.assetLabeling.akun.totalControlChangelog`, `Spectra.env.FA_TC_CHANGELOG_PASSWORD` (langkah 11 sampai 12). Hook `after` mengembalikan sesi ke akun default suite.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` dan `Spectra.env.FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Pre-setup (hanya dibaca): #12 katalog Company Alpha (kolom Last Updated Labels List), #13 aset berlabel `Finance Department` (kolom Last Updated Drawer), #17 Company Changelog dengan tujuh baris seed (Date 08 sampai 15 Sep 2026) yang dipisahkan lewat Filter Date `08 Sep 2026` sampai `15 Sep 2026` (kolom Date Modal Changelog; hanya baris seed `Edit High Priority` dan `Delete Old Tag` yang diasersi; entri TC lain bertanggal hari run berada di luar rentang).
- Nilai General Settings uji (default entitas, TC-FA-LBL-437 sampai 439; `global-settings/general-settings/PRD/general-settings.md` §9.5). Fixture `fixtures/asset-labeling.json` (disediakan tim FE; belum ada, S-12). Kunci yang dipakai spec ini:

  | Kunci | Nilai | Contoh tampilan |
  |---|---|---|
  | `Fixture.assetLabeling.formatTanggal` | Date Format `dd/MM/yy` | `15/09/26`, `08/09/26`, `14/09/26`, `10/09/26` |
  | `Fixture.assetLabeling.formatJam` | Time Format `HH:mm` (24 jam) | `14:25`, `13:00`, `09:00` |
  | `Fixture.assetLabeling.zonaWaktu` | Time Zone `Asia/Jakarta` (UTC+07:00); nilai seed ditulis dalam Time Zone entitas | 15 Sep 2026 14:25 tampil `15/09/26 14:25` |

- State global yang diubah: General Settings (Date Format, Time Format, dan Time Zone) Company Alpha dan Company Changelog dipastikan bernilai default pada tabel di atas lewat fixture BE di hook `before` dan dipulihkan ke nilai awal di hook `after`. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- Cleanup: tidak ada data yang dibuat spec selain pengaturan General Settings di atas.

## Test Steps

### TC-FA-LBL-437: Format tanggal, jam, dan timezone General Settings pada Labels List

1. Verifikasi kolom Last Updated baris `High Priority` tampil `15/09/26 14:25`
2. Klik icon Filter, lalu pilih rentang `14 Sep 2026` sampai `15 Sep 2026` pada `Last Updated`
3. Verifikasi kotak input Filter `Last Updated` menampilkan tanggal `14/09/26` dan `15/09/26`
4. Tutup panel Filter tanpa menerapkan filter

### TC-FA-LBL-439: Format tanggal, jam, dan timezone General Settings pada Drawer Tagged Asset

5. Ketik Search `Finance Department`, tekan Enter, lalu buka Drawer `Finance Department`
6. Verifikasi kolom Last Updated aset `Laptop Dell - 1` tampil `14/09/26 09:00`
7. Verifikasi kolom Last Updated aset `Projector Epson - 5` tampil `10/09/26 09:00`
8. Buka Filter Drawer, lalu pilih rentang `12 Sep 2026` sampai `14 Sep 2026` pada `Last Updated`
9. Verifikasi kotak input Filter Drawer menampilkan tanggal `12/09/26` dan `14/09/26`
10. Tutup Drawer

### TC-FA-LBL-438: Format tanggal, jam, dan timezone General Settings pada Modal Changelog

11. Ganti akun: logout dari Total Control Company Alpha
12. Login sebagai Total Control Company Changelog (Pre-setup #17)
13. Buka Fixed Asset > Settings > Asset Master > tab Labels
14. Buka Modal Changelog
15. Buka Filter Modal Changelog, lalu pilih rentang `08 Sep 2026` sampai `15 Sep 2026` pada `Date` dan klik `[Apply]`
16. Verifikasi kolom Date baris seed `Edit High Priority` tampil `15/09/26 14:25`
17. Verifikasi kolom Date baris seed `Delete Old Tag` tampil `08/09/26 13:00`
18. Pilih rentang `14 Sep 2026` sampai `15 Sep 2026` pada `Date` di panel Filter Modal Changelog
19. Verifikasi kotak input Filter `Date` menampilkan tanggal `14/09/26` dan `15/09/26`
20. Tutup panel Filter dan Modal Changelog tanpa menerapkan rentang kedua

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 5 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 4, 8, 10, 11, 12, 13, 14, 18, 20 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan: TC-FA-LBL-439 ditaruh sebelum TC-FA-LBL-438 supaya akun default suite dipakai lebih dulu dan ganti akun ke Company Changelog hanya sekali.
- Rentang Filter dan contoh tampilan diambil dari Data Uji TC-FA-LBL-437 sampai 439. Rentang pertama `08 Sep 2026` sampai `15 Sep 2026` (langkah 15) di-Apply supaya baris seed dibaca atas hasil Filter Date; rentang kedua `14 Sep 2026` sampai `15 Sep 2026` (langkah 18) tidak diterapkan: TC hanya mengasersi teks tanggal pada kotak input Filter dan kolom tanggal, sehingga panel Filter ditutup tanpa menerapkan rentang kedua (S-09).
- Temuan untuk QA:
  - Langkah 18: panel Filter Modal Changelog diasumsikan tetap terbuka sesudah `[Apply]` pada langkah 15 (pola Filter Panel Drawer, bagian 8b butir 9), sehingga ikon Filter tidak diklik lagi; perilaku panel Modal Changelog sesudah `[Apply]` belum dikonfirmasi dan ditanyakan ke tim FE (D-11, F-305).
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; disediakan tim FE.
