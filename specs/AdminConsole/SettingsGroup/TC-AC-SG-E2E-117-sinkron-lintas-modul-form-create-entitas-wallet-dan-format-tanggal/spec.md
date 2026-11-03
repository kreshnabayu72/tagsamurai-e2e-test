---
id: TC-AC-SG-E2E-117-sinkron-lintas-modul-form-create-entitas-wallet-dan-format-tanggal
title: "Sinkron Lintas Modul: Form Create Distributor, Partner, Client, Wallet, dan Format Tanggal General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-342
  - TC-AC-SG-351
  - TC-AC-SG-352
coverage:
  web: automated
---

# Sinkron Lintas Modul: Form Create Distributor, Partner, Client, Wallet, dan Format Tanggal General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke form Create Distributor, Create Partner, Create Client, modul Wallet, dan Global Settings > General Settings tersedia (Pre-setup #40 hanya menyebut form Create dan modul terkait secara umum; akses Wallet dan General Settings tidak tertulis di Pre-setup, lihat Temuan untuk QA).
- Form yang diuji (langkah 5 sampai 8 diulang per baris):

  | Form |
  |---|
  | Create Distributor |
  | Create Partner |
  | Create Client |

- Data yang dibuat langkah spec pada tree Principal, dihapus hook `after` lewat Fixture BE: `Region Form {runId}-117` (TC-AC-SG-342) dan `Region Wallet {runId}-117` (TC-AC-SG-351). Pohon Uji Utama (Pre-setup #16) tidak diubah. Entri Changelog dari kedua group itu menjadi data baca bagi kolom Date pada TC-AC-SG-352.
- State global: Date Format dan Time Format General Settings entitas Principal diubah oleh TC-AC-SG-352. Nilai awal dicatat di langkah 16 dan dipulihkan di langkah 25 serta di hook `after` (bila spec berhenti di tengah). Suite berjalan serial (`parallel: false`).
- Jam server dan jam browser sinkron; tidak ada asersi waktu aksi.
- Kemampuan teknis: Fixture BE (pemulihan group, pemulihan Date Format dan Time Format awal; disediakan tim FE/BE).

## Test Steps

### TC-AC-SG-342: Group baru muncul di dropdown Select Group form Create Distributor, Partner, dan Client

1. Klik `[+] Group` di Sidebar Group Tree
2. Ketik `Region Form {runId}-117` lalu klik `[Submit]`
3. Tunggu aksi selesai (dialog/popup tertutup)
4. Untuk setiap baris tabel "Form yang diuji" (langkah 5 sampai 8), lakukan langkah berikut
5. Buka form sesuai baris tabel (Create Distributor, Create Partner, atau Create Client)
6. Buka dropdown Select Group pada form
7. Verifikasi opsi `Region Form {runId}-117` tersedia pada dropdown Select Group form sesuai baris tabel
8. Tutup form dengan `✕`

### TC-AC-SG-351: Group baru muncul pada Sidebar Group Tree modul Wallet (konsumen tree)

9. Buka halaman Settings > Group lewat sidebar
10. Klik `[+] Group` di Sidebar Group Tree
11. Ketik `Region Wallet {runId}-117` lalu klik `[Submit]`
12. Tunggu aksi selesai (dialog/popup tertutup)
13. Buka Wallet lewat sidebar
14. Verifikasi Sidebar Group Tree Wallet memuat `Region Wallet {runId}-117`

### TC-AC-SG-352: Format tanggal Last Updated dan Date Changelog mengikuti General Settings

15. Buka Global Settings > General Settings
16. Catat Date Format dan Time Format yang berlaku sebagai nilai awal
17. Ubah Date Format menjadi `DD MMM YY` dan Time Format menjadi 24 jam, lalu simpan
18. Tunggu aksi selesai (dialog/popup tertutup)
19. Buka halaman Settings > Group lewat sidebar
20. Verifikasi kolom Last Updated tabel menampilkan tanggal dan jam sesuai Date Format `DD MMM YY` dan Time Format 24 jam (bukan format tetap)
21. Klik ikon Changelog pada toolbar
22. Verifikasi kolom Date Modal "Changelog: Group" menampilkan tanggal dan jam sesuai Date Format `DD MMM YY` dan Time Format 24 jam (bukan format tetap)
23. Tutup Modal Changelog dengan `✕`
24. Buka Global Settings > General Settings
25. Kembalikan Date Format dan Time Format ke nilai awal yang dicatat, lalu simpan

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 3 dan 18 (`Tunggu aksi selesai (dialog/popup tertutup)`, bagian 8b butir 8) menunggu popup Create tertutup sebelum membuka modul lain dan menunggu simpanan General Settings selesai sebelum membuka Settings > Group; langkah 12 (`Tunggu aksi selesai (dialog/popup tertutup)`) menunggu popup Create tertutup sebelum membuka Wallet; membuka kembali Settings > Group lewat sidebar (langkah 9 dan 19), menutup form dan Modal Changelog dengan `✕` (langkah 8 dan 23), mencatat nilai awal (langkah 16), dan memulihkan Date Format dan Time Format ke nilai awal (langkah 24 dan 25, S-09).
- Form pada langkah 5 sampai 8 dibuka tanpa diisi sehingga tidak dirty dan tidak memunculkan dialog `Unsaved Changes`.
- Ambang sekitar 35 langkah dihitung dengan ekspansi (bagian 8b butir 7): 25 langkah nominal ditambah 8 langkah dari dua iterasi tambahan langkah 5 sampai 8 menjadi 33 langkah.
- Pembagian TC lintas spec: TC-AC-SG-341, 343, dan 348 ada di spec 092.
- Temuan untuk QA:
  - TC-AC-SG-352 Langkah Uji "Ubah Date Format ... menjadi DD MMM YY lalu 24 jam" tidak menyebut tombol penyimpanan General Settings dan tidak menyebut pemulihan format sesudah TC; spec menyimpan perubahan dan memulihkan nilai awal sebagai langkah penghubung.
  - TC-AC-SG-352 Expected menyebut "sesuai Date Format dan Time Format" tanpa contoh keluaran; spec mengasersi kesesuaian dengan format `DD MMM YY` dan 24 jam.
  - Pre-setup TC tidak menyebut akses akun Total Control Principal ke Wallet dan General Settings (Pre-setup #40 hanya menyebut Activity Log, Settings > User, Role & Permission, dan form Create).
  - TC-AC-SG-342 tidak menyebut jalur menu untuk membuka form Create Distributor, Create Partner, dan Create Client; spec menulis "buka form sesuai baris tabel".
