---
id: TC-FA-RP-E2E-092-mobile-mode-checkbox-floating-bottom-bulk-bar-dan-select-all
title: "Mobile: mode checkbox, Floating Bottom Bulk Bar, dan Select All"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-305
  - TC-FA-RP-306
  - TC-FA-RP-307
coverage:
  mobile: automated
---

# Mobile: mode checkbox, Floating Bottom Bulk Bar, dan Select All

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list. Perangkat atau emulator Android dengan aplikasi native TAG Samurai Fixed Asset terpasang, serta kemampuan long press dan mengetuk elemen UI. Perangkat Android uji dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`; akun kedua untuk TC-FA-RP-307: Total Control `Company Volume` (Pre-setup #23, `Total Control Volume`), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_VOLUME_TC_PASSWORD`. Login akun pertama di aplikasi Android dilakukan di hook `before` spec ini; ganti akun ke Company Volume pada langkah 17 dan 18; hook `after` mengembalikan sesi ke akun default suite (Total Control Siti Rahmawati).
- Environment variable: `FA_TC_PASSWORD`, `FA_VOLUME_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: pool #15 (Budi Santoso, Budi Setiawan; keduanya memegang Global Role `Manage Open API` dan `Manage accounting`) dan #23 (`Company Volume`, 120 penugasan Global Role `Import data`). Disiapkan lewat seed API di hook `before`; spec tidak mengubah data (tidak ada aksi yang dikonfirmasi).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan `Manage Open API` dan `Manage accounting` pool #15), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-305: Mobile: long press masuk mode checkbox lalu Floating Bottom Bulk Bar tampil

1. Buka Fixed Asset > Settings > Role & Permission > System di aplikasi Android, lalu buka Detail Role `Manage Open API`
2. Long press card Budi Santoso
3. Verifikasi mode checkbox aktif
4. Verifikasi card Budi Santoso terpilih
5. Ketuk card Budi Setiawan
6. Verifikasi Floating Bottom Bulk Bar memuat `(✕)`, counter `2 Selected`, `[Select All]`, dan aksi langsung `[Remove]` (severity danger)
7. Verifikasi bar tidak memakai dropdown `Bulk Action`
8. Ketuk `(✕)` pada bar untuk membatalkan seleksi

### TC-FA-RP-306: Mobile: selama mode checkbox aktif baris checkbox C/U/D pada card inert

9. Buka Detail Role `Manage accounting`
10. Long press card Budi Santoso
11. Ketuk checkbox Create pada card
12. Verifikasi checkbox Create tidak berubah
13. Verifikasi tidak ada dialog
14. Verifikasi tidak ada toast
15. Verifikasi ketukan hanya memilih atau melepas card: status pilihan card Budi Santoso berubah, bukan checkbox Create
16. Ketuk `(✕)` pada bar atau keluar dari mode checkbox

### TC-FA-RP-307: Mobile: [Select All] hanya memilih card halaman aktif yang checkbox-nya enabled

17. Ganti akun: Logout dari aplikasi Android
18. Login di aplikasi Android sebagai Total Control `Company Volume`
19. Buka Fixed Asset > Settings > Role & Permission > System, lalu buka Detail Role `Import data` pada Company Volume
20. Long press satu card
21. Ketuk `[Select All]`
22. Verifikasi hanya card pada halaman aktif yang tercentang (10 card)
23. Verifikasi card di halaman lain tidak tercentang
24. Verifikasi tidak ada tombol `Select All (120 records)`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-305, TC-FA-RP-306, TC-FA-RP-307).
- Langkah penghubung (S-03): membuka halaman di aplikasi Android; membatalkan seleksi atau keluar dari mode checkbox (langkah 8 dan 16); ganti akun pada langkah 17 dan 18.
- Automation TC: Manual Only (b) native Android; hambatan teknis bukan alasan mengeluarkan TC dari spec (bagian 2). `coverage.mobile` diusulkan `automated`; kemampuan mobile ditulis di Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-305 dan TC-FA-RP-306 tidak menyebut apakah Budi Santoso dan Budi Setiawan memegang `Manage Open API` dan `Manage accounting`; spec mengasumsikan penugasan itu.
  - Expected TC-FA-RP-306 menyebut "ketukan hanya memilih atau melepas card" tanpa status akhir pilihan; spec mengasersi status pilihan card berubah.
  - Akun Total Control `Company Volume` tidak tertulis di Pre-setup TC; dicatat "disediakan tim FE" (S-11).
