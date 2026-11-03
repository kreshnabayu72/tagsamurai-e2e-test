---
name: Fixed Asset Role Permission
id: suite-fixed-asset-role-permission
description: Spec e2e turunan tc-settings-role-permission.md untuk Fixed Asset > Settings > Role & Permission
executionOrder: 6.0
parallel: false
---

# Suite: Fixed Asset Role Permission

Suite ini mencakup halaman Fixed Asset > Settings > Role & Permission: Tab Total Control, Tab Read Only, Tab Group Manager, Tab Transaction Role (sub-tab Borrowing & Assignment, Transfer, Disposal, Damaged, Missing, Audit, Repair Ticketing, Tracking, Maintenance Routine), Tab System, dan Detail Role (Global Role serta Group Role). Cakupan: screening, Role Matrix, popup Assign (Total Control, Read Only, Group Manager, User ke Role, Role Transaksi), Assign dan Remove tingkat akses, Edit CRUD dan Auto-Revert, Remove baris peran dan Bulk Remove, aturan persetujuan transaksi dan registrasi aset (D-09), Home Group constraint (D-10), Search, Filter, Sort, Pagination, Setup Column, Download, Modal Changelog, pencatatan Changelog, System Log, dan Activity Log, sinkronisasi dengan modul lain, notifikasi in-app, Guided Tooltip, state tenant (Client Suspended, Expired, dan plan tier), defense-in-depth, ketahanan terhadap kegagalan server, konflik antar admin, dan tampilan mobile Android.

`parallel: false` karena spec mengubah state yang dipakai bersama (tingkat akses dan baris peran user Pre-setup, flag Guided Tooltip, format tanggal General Settings, batas Selection Limit, status Client). Spec yang menghapus data atau mencabut tingkat akses dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: hook `before` suite mencatat nilai awal flag lalu menyetelnya `seen` (true) untuk akun aktor yang dipakai spec, dan hook `after` memulihkan nilai awal. Spec yang menguji Guided Tooltip mengatur flag sendiri sesudah hook dan menjelaskan mekanismenya di `## Prerequisites`. `## Prerequisites` spec lain merujuk pernyataan ini dengan satu baris. Kemampuan membaca dan menyetel flag disediakan tim FE/BE. Spec `Mode: mock` mengatur flag lewat respons mock yang tertulis di Prerequisites-nya.
- Halaman dibuka hook `beforeEach` suite: Fixed Asset > Settings > Role & Permission pada tab awal (Total Control) untuk akun aktor yang login di hook `before` spec. `## Prerequisites` spec merujuk pernyataan ini dengan satu baris.
- Pre-setup bersama (pool pengguna #15 dan #16, Home Group #17, penugasan #19, #20, #21, #33, #43, group #18, dan data tabel #36 sampai #42) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC oleh spec yang mengubahnya (seeding di hook `before`, pemulihan di hook `after`), mengikuti catatan "Pemulihan fixture destruktif" di TC. Pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Setelan sistem global (System Limits Selection Limit #34, General Settings Date Format, Time Format, dan Timezone #34, status Client Suspended atau Expired #25 dan #26) dipulihkan oleh spec yang mengubahnya di hook `after`; hal itu ditulis di `## Prerequisites` spec yang bersangkutan.
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir (konvensi bagian 5). Kemampuan itu disediakan tim BE/FE. Pelaku kedua yang hanya memicu perubahan state (admin lain menghapus user, melepas role, atau mengubah tingkat akses) memakai sesi API; sesi UI kedua dipakai hanya bila hasil di sesi itu diasersi (`P-2`). `## Prerequisites` spec merujuk pernyataan ini dengan satu baris.
- Admin kedua: Total Control kedua (Pre-setup #3, Rina Wulandari) memakai env `FA_TC2_PASSWORD`.
- Klien HTTP untuk request langsung ke server (spec defense-in-depth dan absence log) dan pembaca berkas unduhan (spec isi berkas) adalah kemampuan yang disediakan tim FE/BE; spec yang memakainya menulisnya di `## Prerequisites` tanpa menyebut endpoint yang tidak ada di TC, PRD, atau LLD.
- Spec mobile memakai perangkat atau emulator Android bersama dan menulis `parallel: false` di `## Prerequisites`.
- Preferensi kolom Setup Column: hook `after` suite menghapus preferensi kolom Setup Column yang tersimpan di browser (bukan lewat `[Reset to Default]`), supaya spec berikutnya mulai dari kolom bawaan. Kemampuan itu disediakan tim FE. Jenis tabel yang kolomnya disimpan spec: Tab Total Control, Read Only, Group Manager, dan System; tabel Role Transaksi; Detail Role; Table User Picker; Modal Changelog.

## Env password akun aktor

Password akun aktor tidak masuk fixture atau spec. Nama berikut didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (konvensi bagian 5); satu nama satu arti.

- `FA_TC_PASSWORD`: Total Control (Pre-setup #2, Siti Rahmawati).
- `FA_TC2_PASSWORD`: Total Control kedua (Pre-setup #3, Rina Wulandari).
- `FA_DU_PASSWORD`: Default User (Pre-setup #1, Admin Utama).
- `FA_RO_PASSWORD`: Read Only (Pre-setup #4, Dewi Anggraini).
- `FA_GM_PASSWORD`: Group Manager (Pre-setup #5, Fajar Nugroho).
- `FA_GM2_PASSWORD`: Group Manager kedua (Pre-setup #11, Lina Marlina).
- `FA_MUR_GLOBAL_PASSWORD`: Manage global user & role dengan Update (Pre-setup #6, Hendra Wijaya).
- `FA_MUR_GROUP_PASSWORD`: Manage user & role tingkat Group dengan Update (Pre-setup #7, Gita Maharani).
- `FA_MUR_GLOBAL_RO_PASSWORD`: Manage global user & role tanpa Update (Pre-setup #8, Bayu Prakoso).
- `FA_MUR_GROUP_RO_PASSWORD`: Manage user & role tingkat Group tanpa Update (Pre-setup #9, Wulan Sari).
- `FA_NOACCESS_PASSWORD`: Tanpa Akses (Pre-setup #10, Tono Wibowo).
- Total Control pada client khusus (akun disediakan tim FE; email tidak tertulis di Pre-setup TC): `FA_EMPTY_TC_PASSWORD` (`Company Kosong`, #27), `FA_SUSPENDED_TC_PASSWORD` (`Client Suspended`, #25), `FA_EXPIRED_TC_PASSWORD` (`Client Expired`, #26), `FA_BETA_TC_PASSWORD` (`Company Beta`, #28), `FA_EXPORT_TC_PASSWORD` (`Company Export`, #29), `FA_VOLUME_TC_PASSWORD` (`Company Volume`, #23), `FA_CHANGELOG_TC_PASSWORD` (`Company Changelog`, #24), `FA_ISOLATED_TC_PASSWORD` (`Company Isolated`, #35), `FA_STARTER_TC_PASSWORD`, `FA_GROWTH_TC_PASSWORD`, `FA_PROFESSIONAL_TC_PASSWORD`, `FA_ENTERPRISE_TC_PASSWORD` (client per plan, #30), `FA_ADDON_OFF_TC_PASSWORD` dan `FA_ADDON_ON_TC_PASSWORD` (`Client Addon Off` dan `Client Addon On`, #31).
- Akun khusus spec tertentu (akun disediakan tim FE; email tidak tertulis di Pre-setup TC):
  - `FA_CHANGELOG_GM_PASSWORD`: Group Manager dengan cakupan `IT Infrastructure` (TC-FA-RP-120).
  - `FA_CHANGELOG_MUR_GROUP_PASSWORD`: Manage user & role tingkat Group dengan Update, cakupan `IT Infrastructure` (TC-FA-RP-121).
  - `FA_GMMUR_PASSWORD`: Group Manager di `Helpdesk` sekaligus Manage user & role tingkat Group dengan Update di `Logistics Warehouse` (TC-FA-RP-1026, disiapkan lewat seeding API).
  - `FA_HESTI_PASSWORD`: Hesti Rahma (Pre-setup #17, user ber-Home Group).
  - `FA_GUNAWAN_PASSWORD`: Gunawan Halim (Pre-setup #17, user ber-Home Group).
  - `FA_SUSPENDED_RO_PASSWORD`: Read Only pada `Client Suspended` (Pre-setup #25).
