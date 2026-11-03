---
id: TC-FA-PREF-E2E-171-sinkronisasi-save-preferences-tidak-mengubah-data-asset-class-dan-periode-diposting
title: "Sinkronisasi: Save Preferences Tidak Mengubah Data Asset Class dan Periode yang Sudah Diposting"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-410
coverage:
  web: automated
---

# Sinkronisasi: Save Preferences Tidak Mengubah Data Asset Class dan Periode yang Sudah Diposting

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Varian PC-2: posting penyusutan pertama sudah ada (Asset Class IT Equipment memiliki Last Posted Period Apr 2026 dan threshold sendiri 2.000.000); Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pembentukan posting penyusutan pertama lewat fixture BE (Depreciation Run dan Period Close belum disusun; PC-2). Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, kunci periode) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- State yang diubah spec: Preferences company dan kunci posting penyusutan pertama. Hook `after` menghapus kunci posting dan memulihkan Preferences ke nilai awal PC-1 (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-410: Save Preferences tidak mengubah data Asset Class dan periode yang sudah diposting

1. Bentuk posting penyusutan pertama (Last Posted Period Asset Class IT Equipment = Apr 2026) lewat fixture BE hingga tersimpan, lalu muat ulang halaman Preferences (PC-2; dipakai sebagai precondition TC, tidak diasersi)
2. Ubah Default Capitalization Threshold menjadi "10000000"
3. Klik [Save changes]
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
5. Klik [Save] pada dialog Save Changes
6. Tunggu aksi selesai
7. Buka Settings > Accounting > Asset Class
8. Ketik Search "IT Equipment", tekan Enter
9. Buka kelas IT Equipment dan amati Last Posted Period pada tab General
10. Verifikasi kelas IT Equipment tetap Last Posted Period Apr 2026
11. Pilih tab Depreciation dan amati field Capitalization Threshold pada bagian Capitalization
12. Verifikasi kelas IT Equipment tetap memakai threshold sendiri 2.000.000
13. Klik (←) pada kotak Search
14. Hapus kunci posting penyusutan pertama lewat fixture BE dan pulihkan Preferences ke nilai awal PC-1 lewat seed

## Notes

- Kelas fungsional: Save atau perubahan state pelaku kedua, lalu pembacaan modul konsumen (Asset Class, Tax Depreciation Class, Accounting Period, Chart of Accounts, Changelog). Tidak ada asersi absence log (kelas g).
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 6, 8, 13, 14 (seed precondition TC, menunggu aksi selesai, Search untuk menemukan baris target (R-16, 8b butir 12), membersihkan Search, pemulihan state antar-TC).
- TC-FA-PREF-410 membutuhkan data kunci posting penyusutan pertama (PC-2); TC sinkronisasi ke Asset Class dan Tax Depreciation Class lainnya ada di spec 130.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Post Condition TC-FA-PREF-410 ("Data konsumen yang sudah tersimpan tidak berubah oleh Save Preferences") tidak punya langkah observasi sendiri; padanannya ada pada Expected b.
