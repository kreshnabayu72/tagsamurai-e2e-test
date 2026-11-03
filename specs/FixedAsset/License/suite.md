---
name: Fixed Asset License
id: suite-fixed-asset-license
description: Spec e2e turunan tc-license.md untuk Fixed Asset > License
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset License

Suite ini mencakup halaman License pada Fixed Asset: Tabs Bar dan Breadcrumb, Guided Tooltip, License Summary (T-FALIC-05), sub-tab Subscription History (T-FALIC-01) dan Allocation History (T-FALIC-04), Tab Allocation Quota (Sidebar Group Tree, Group Quota Summary T-FALIC-06, Group License Allocation T-FALIC-03), Tab Concurrent User (Active Sessions T-FALIC-02), Renewal Reminder Banner, Edit Allocation, Remove Allocation, Force Logout, Download, Search, Filter, Sort, Setup Column, paginasi, dua modal Changelog, pencatatan log di tiga surface, sinkron lintas modul (registrasi aset, transfer, approval, aksi Manage, Settings > Groups, Admin Console), peringatan kuota tenant, role matrix, state tenant, defense-in-depth, resilience, dan konkurensi.

`parallel: false` karena spec mengubah atau bergantung pada state global: plan dan toggle `License allocation per group`, cap plan Starter, Total Asset License dan penanda tingkat peringatan kuota, status term dan tanggal fixture banner, format tanggal General Settings, status Client, jam job per jam, hierarki dan alokasi grup, serta flag Guided Tooltip. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

Pernyataan hook dan kemampuan suite (dinyatakan sekali di sini; `## Prerequisites` tiap spec merujuknya dengan satu baris):

- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir; disediakan tim BE/FE. Pelaku kedua yang hanya memicu perubahan state memakai sesi ini.
- Login akun aktor pertama spec di hook `before` spec itu (akun dibaca dari `## Prerequisites`); hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1). Halaman Fixed Asset > License dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license`: hook `before` menyetelnya true untuk akun aktor spec dan hook `after` memulihkannya. Spec Guided Tooltip yang menguji flag itu menulis pengecualiannya dan mengatur flag sendiri.
- Fixture BE pemulih Pre-setup (hierarki dan kuota #12, riwayat #13, sesi aktif #14 dan #26, riwayat Changelog #27 dan #31, aset #20 dan #28): dijalankan di hook `before` dan `after` spec yang mengubah data serta sebagai langkah penghubung antar blok TC dalam satu spec. Disediakan tim FE/BE (idempotent); efeknya (Last Updated, entri Changelog, System Log, dan Activity Log) dicatat di `## Prerequisites` spec yang bersangkutan. Pengecualian S-12 `[KEPUTUSAN 2026-11-02]`: fixture pemulih riwayat #27 dan #31 juga menghapus entri baru yang ditambahkan spec lain pada Changelog Allocation Quota dan Changelog Concurrent User, sehingga total entri Changelog absolut hanya valid tepat setelah pemulihan itu; di luar keadaan itu asersi jumlah memakai selisih terhadap baseline.
- Fixture BE penukar (menukar data Pre-setup ke variasi yang dibutuhkan satu blok TC lewat langkah penghubung eksplisit; hook `after` memulihkannya; disediakan tim FE/BE, idempotent): sesi aktif Pre-setup #14 (18 sesi) dan #26 (lima sesi cuplikan); Pre-setup #30 (lima sesi #26 ditambah sesi kedua Dewi Lestari dengan IP Address `192.0.2.100`, Online Users 6/25); fixture 25 sesi (tabel Active Sessions 25 baris pada client Paid Pre-setup #1, beserta kata kunci Search yang mengembalikan lebih dari 10 baris dan opsi Filter `Position` yang mengembalikan sedikitnya satu baris sebagai kunci fixture); dan variasi Pre-setup #12 dengan node Kantor Pusat memiliki 12 child (kode grup berawalan `GRP-`).
- Fixture BE penyetel state: tanggal "hari ini" dan status term live (banner #15), plan dan toggle `License allocation per group` serta cap plan Starter, Total Asset License, Used, Reserved, Unmanaged, dan penanda tingkat (#16), status aset (Draft, Waiting for Approval, Active), dan jam job per jam. Disediakan tim FE/BE; endpoint tidak dikarang.
- Pemulihan konfigurasi kolom: spec yang menyimpan Setup Column mendaftarkannya di sini; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`), kemampuan disediakan tim FE.
- Kemampuan membaca berkas unduhan CSV dan XLSX (nama berkas, encoding, sheet, baris, sel) disediakan tim FE untuk spec yang mengasersi berkas.
- Jam fixture atau jam server yang digeser: sesi UI dan sesi API aktor tetap valid selama jam digeser, jam dipulihkan di hook `after`, dan asersi Date log memakai selisih jumlah entri terhadap baseline.
- Password akun aktor lewat env var `FA_<ROLE>_PASSWORD` (`Spectra.env.*`), didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Fixture BE client Suspended dan Expired (Pre-setup #18: `totalControlSuspended_automated_{namaCompany}@qwertysystem.net` dan `totalControlExpired_automated_{namaCompany}@qwertysystem.net`, data kuota dan hierarki Pre-setup #12; status diubah setelah sesi dibuka) disediakan tim FE/BE untuk E2E-035.
- Kemampuan membaca jumlah entri Changelog, System Log, dan Activity Log sebelum aksi (baseline, S-12) disediakan tim FE/BE untuk spec yang mengasersi entri baru atau tidak adanya entri baru (mis. E2E-045, 107, 108, 109, 143, 168).
- Fixture BE grup milik spec bersuffix `{runId}-<nomor spec>` (dibuat di `before`, dihapus di `after`) disediakan tim FE/BE untuk spec yang me-rename atau menghapus grup (E2E-048, 109, 112, 143, 144).
