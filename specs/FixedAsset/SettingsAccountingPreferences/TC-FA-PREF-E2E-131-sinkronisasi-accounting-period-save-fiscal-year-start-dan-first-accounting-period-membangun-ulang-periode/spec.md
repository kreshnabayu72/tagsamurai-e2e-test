---
id: TC-FA-PREF-E2E-131-sinkronisasi-accounting-period-save-fiscal-year-start-dan-first-accounting-period-membangun-ulang-periode
title: "Sinkronisasi ke Accounting Period: Save Fiscal Year Start dan First Accounting Period Membangun Ulang Periode"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-394
  - TC-FA-PREF-395
coverage:
  web: automated
---

# Sinkronisasi ke Accounting Period: Save Fiscal Year Start dan First Accounting Period Membangun Ulang Periode

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Periode Mar 2026 sampai Dec 2026 berstatus Open; belum ada posting penyusutan dan transaksi bertanggal; Tax Depreciation Class hanya versi pertama. Jumlah periode pada dialog dan hasil bangun ulang bergantung bulan berjalan Oktober 2026: jam sistem Oktober 2026 (lihat butir Jam sistem; PC-15 Time Zone Asia/Jakarta).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): kendali jam sistem (clock). Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, kunci periode) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- State yang diubah spec: Preferences company dan periode akuntansi hasil bangun ulang. Preferences dan periode dipulihkan ke nilai awal PC-1 lewat seed antar-TC dan di hook `after`; jam sistem dipulihkan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-394: Save Fiscal Year Start membangun ulang seluruh periode di Accounting Period

1. Pilih "July" pada Select Fiscal Year Start
2. Klik [Save changes]
3. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "16 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
4. Klik [Save] pada dialog Save Changes
5. Verifikasi toast "Success, accounting preferences have been saved." tampil
6. Buka daftar periode di modul Accounting Period (`settings-accounting-period/`), pilih filter Fiscal Year = All, atur ukuran halaman ke 25, lalu amati periode yang tampil
7. Verifikasi dengan filter Fiscal Year = All, Accounting Period memuat 16 periode bulanan dari Mar 2026 sampai Jun 2027
8. Verifikasi seluruh 16 periode berstatus Open
9. Verifikasi tahun fiskal pertama berisi 4 periode (Mar 2026 sampai Jun 2026)
10. Verifikasi tahun fiskal berikutnya dimulai Jul 2026
11. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-395: Save First Accounting Period membangun ulang periode dari bulan baru

12. Pilih bulan "January" dan tahun "2026" pada Select First Accounting Period
13. Klik [Save changes]
14. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "12 accounting periods will be rebuilt." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
15. Verifikasi dialog Save Changes tidak memuat bullet "Tax year start also follows Fiscal Year Start." (PV-05, Fiscal Year Start tidak berubah)
16. Klik [Save] pada dialog Save Changes
17. Verifikasi toast "Success, accounting preferences have been saved." tampil
18. Buka daftar periode di modul Accounting Period (`settings-accounting-period/`), atur ukuran halaman ke 25, dan amati periode yang tampil
19. Verifikasi Accounting Period memuat 12 periode bulanan dari Jan 2026 sampai Dec 2026
20. Verifikasi seluruh 12 periode berstatus Open
21. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: Save atau perubahan state pelaku kedua, lalu pembacaan modul konsumen (Asset Class, Tax Depreciation Class, Accounting Period, Chart of Accounts, Changelog). Tidak ada asersi absence log (kelas g).
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 11, 21 (seed precondition TC, menunggu aksi selesai, Search untuk menemukan baris target (R-16, 8b butir 12), membersihkan Search, pemulihan state antar-TC).
- Modul Accounting Period (`settings-accounting-period/`) adalah modul data periode, bukan tab Settings > Accounting (Catatan TC); langkah membukanya mengikuti TC. Tabel periode tidak memakai Search sehingga tidak ada langkah Search di spec ini.
- Pada TC-FA-PREF-395, PV-05 tidak tampil karena Fiscal Year Start tidak berubah; asersi absence bullet itu didahului `Verifikasi` dialog dengan bullet pertama tampil (anchor positif, 8b butir 2).
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Post Condition TC-FA-PREF-394 dan 395 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).
  - TC-FA-PREF-395 tidak menyebut filter Fiscal Year pada langkah membuka daftar periode (hanya ukuran halaman 25); spec mengikuti TC.
