---
name: Fixed Asset Activity Log
id: suite-fixed-asset-activity-log
description: Spec e2e turunan tc-activity-log.md untuk Fixed Asset > Reports & Logs > Activity Log
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Activity Log

Suite ini mencakup halaman Activity Log (Tab Session dan Tab User Action): screening, tampilan sel, Search, Filter, Sort, Setup Column, paginasi, Download (nama berkas dan isi berkas CSV/XLSX), persistensi state, Role Matrix akses, perubahan tier akses, Guided Tooltip, tampilan Android native, format tanggal mengikuti General Settings, pembaruan real-time lewat SSE, pencatatan Tab Session dan Tab User Action dari modul sumber, asersi absence, state tenant dan plan, defense-in-depth, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah atau bergantung pada state global: status client dan subscription, plan, jam server (time-travel Session ended), General Settings staf, tier akses user, flag Guided Tooltip, konfigurasi kolom, jumlah baris log client yang sama, dan volume 5.000 sampai 5.001 baris. Setiap spec menyiapkan dan memulihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, Pre-setup #1, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD`). Spec yang aktor pertamanya akun atau client lain login akun itu di hook `before` spec, dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Fixed Asset > Reports & Logs > Activity Log (layar awal spec). Spec yang membuka layar sendiri (akun tanpa akses, client lain, Android, Guided Tooltip) menulis pengecualian itu di `## Prerequisites`.
- Jaring pengaman form dirty: hook `beforeEach` mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; ini bukan pengganti langkah pemulihan eksplisit spec (S-09).
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set flag true untuk setiap akun aktor yang dipakai agar walkthrough tidak menutupi layar, dan `after` memulihkan nilai awal. Spec Guided Tooltip dan Android (akun Pre-setup #4) dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites`. Mekanisme disediakan tim FE/BE.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI. Dipakai untuk pelaku kedua yang hanya memicu perubahan state (admin lain pada pencabutan tier, pemicu baris log baru, admin Alpha pada pencatatan Section 7). Kemampuan ini disediakan tim BE/FE; tiap spec yang memakainya memuat satu baris rujukan ke butir ini.
- Seed dan pemulihan lewat API: seed data log Tab Session SS-01..SS-11 (Pre-setup #11) dan Tab User Action UA-01..UA-15 (#12), client baru tanpa log (#13, #29), volume 5.000 dan 5.001 baris serta baris berusia 2 tahun (#14), client Batas Waktu (#15), entitas Section 7 dan 9 (#16 sampai #28), serta pemulihan plan, status client, subscription, dan nama group/entitas disediakan tim FE/BE; tiap spec merujuk butir ini dan hanya menulis fakta spesifik spec.
- Prasyarat lingkungan eksternal (log dipulihkan ke Pre-setup): log bersifat append-only, sehingga data log dipulihkan ke keadaan Pre-setup (#11 dan #12) sebelum tiap TC atau tiap run suite oleh tim BE/FE; spec tidak memulihkan log sendiri dan urutan default (SS-01 di halaman 2) bergantung pada prasyarat ini. Pemilik: tim BE/FE.
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom memulihkannya di hook `after` dengan menghapus preferensi kolom di browser, bukan lewat `[Reset to Default]`. Kemampuan itu disediakan tim FE.
- Manipulasi jam: spec time-travel (Session ended karena sesi platform kedaluwarsa) mengatur jam server dan jam browser bersama dan memulihkannya di hook `after`; kemampuan disediakan tim BE/FE.
- Kemampuan teknis tambahan yang disediakan tim FE dan dirujuk spec terkait: aplikasi native Android dengan driver perangkat, penangkap unduhan browser dan parser CSV/XLSX, klien HTTP dan SSE dengan token sesi, mail-catcher untuk email Resend, dan dua sesi browser untuk SSE.

## Env var

Password akun aktor: `FA_TC_PASSWORD` (Total Control, #1), `FA_RO_PASSWORD` (Read Only, #2), `FA_DU_PASSWORD` (Default User, #3), `FA_TCNEWGUIDE_PASSWORD` (Total Control tanpa flag Guided Tooltip, #4), `FA_GM_PASSWORD` (Group Manager, #8), `FA_RO_REVOKE_PASSWORD` (Read Only target pencabutan tier, #9), `FA_RO_STAFB_PASSWORD` (Read Only staf B, #10), `FA_ROLEHOLDER_PASSWORD` (satu password bersama untuk 20 user pemegang Global, Group, dan Transaction Role, #5 sampai #7), `FA_TCBATAS_PASSWORD` (Total Control client Batas Waktu, #15), `FA_JOHNDOE_PASSWORD`, `FA_MIKETAN_PASSWORD`, dan `FA_SITINURBAYA_PASSWORD` (user John Doe, Mike Tan, dan Siti Nurbaya, #16). Akun Total Control client kedua TC-FA-FAAL-250 (Pre-setup #30) disediakan tim FE; nama env var passwordnya ditetapkan tim FE. Semua didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE (R-07); password tidak ditulis di spec atau fixture.

## Data bersama

- Fixture `fixtures/activity-log.json` belum ada dan disediakan tim FE; memuat identitas data Pre-setup yang dirujuk Prerequisites (baris SS-xx dan UA-xx, BD-1..BD-6 dan BD-U1..BD-U6, user dan group Section 7). Nama kunci ditetapkan tim FE.
- Baris log bersifat immutable dan tidak dihapus; asersi baris baru memakai baseline jumlah dan nilai bersuffix `{runId}-<NNN>` pada entitas milik spec (S-06, S-12), kecuali nama literal yang dipakai TC sumber untuk baris seed.
- Data yang butuh fixture backend (volume 5.000 sampai 5.001 baris, baris berusia 2 tahun, status client Suspended, subscription Expired/Archive/Purge/Deleted, empat client plan) ditulis di `## Prerequisites` spec sebagai "disediakan tim FE" tanpa endpoint karangan (S-13).
