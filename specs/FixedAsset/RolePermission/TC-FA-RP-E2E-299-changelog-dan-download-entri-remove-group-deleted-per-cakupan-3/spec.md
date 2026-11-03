---
id: TC-FA-RP-E2E-299-changelog-dan-download-entri-remove-group-deleted-per-cakupan-3
title: "Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1118
  - TC-FA-RP-1119
coverage:
  web: automated
---

# Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager (`IT Infrastructure`) (Pre-setup #5, Fajar Nugroho), email `groupManager_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #18 (pohon group), #24 (Company Changelog). Penugasan tambahan Fajar Nugroho di `Dock 1` (TC-FA-RP-1118) dan di `Logistics Warehouse` (TC-FA-RP-1119) dibuat lewat seeding API. Pre-setup dianggap utuh pada awal tiap blok (Catatan TC).
- Kemampuan teknis: sesi API Total Control (Pre-setup #2) untuk menghapus dan memulihkan group; pembaca berkas unduhan CSV (disediakan tim FE/BE); hook `after` memulihkan group yang dihapus spec ini.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1118: Changelog dan Download Tab Group Manager bagi Group Manager: entri Remove (Group Deleted) untuk group yang ancestor pada path tersimpannya tidak dikelola aktor tidak tampil

1. Klik Tab `Group Manager`
2. Tetapkan Fajar Nugroho sebagai Group Manager di group `Dock 1` lewat seeding API (penugasan terpisah dari `IT Infrastructure`, aditif; tanpa penugasan pada `Logistics Warehouse` maupun `Head Office`)
3. Hapus group `Dock 1` dan group `Data Center` lewat sesi API Total Control hingga tersimpan; penugasan Fajar Nugroho di `Dock 1` ikut dilepas dan log memuat dua entri `Remove (Group Deleted)` dengan path tersimpan `Head Office > Logistics Warehouse > Dock 1` dan `Head Office > IT Infrastructure > Data Center`
4. Klik ikon Changelog di toolbar Tab Group Manager
5. Amati entri modal
6. Verifikasi modal memuat entri `Remove (Group Deleted)` `Kevin Susanto — Data Center` karena ancestor pada path tersimpan, `IT Infrastructure`, dikelola aktor
7. Verifikasi entri `Remove (Group Deleted)` `Fajar Nugroho — Dock 1` tidak tampil: ancestor pada path tersimpan (`Logistics Warehouse`, `Head Office`) tidak dikelola aktor, dan penugasan aktor pada `Dock 1` itu sendiri tidak dihitung
8. Tutup modal
9. Unduh Changelog sebagai CSV
10. Verifikasi file Download memuat baris yang sama dengan modal, dan baris `Kevin Susanto — Data Center` ada
11. Verifikasi tidak ada baris di file Download yang menyebut `Dock 1`
12. Pulihkan group `Dock 1` dan `Data Center` serta penugasan Fajar Nugroho di `Dock 1` dilepas lewat seeding API

### TC-FA-RP-1119: Changelog dan Download Tab Group Manager bagi Group Manager: entri Remove (Group Deleted) untuk descendant yang ikut terhapus bersama ancestor-nya tidak tampil bagi aktor yang cakupannya hanya lewat ancestor yang ikut terhapus itu

13. Tetapkan Fajar Nugroho sebagai Group Manager di `Logistics Warehouse` lewat seeding API (penugasan terpisah dari `IT Infrastructure`, aditif; `Logistics Warehouse` bukan ancestor `Data Center`; tanpa penugasan pada `Head Office`)
14. Hapus group `IT Infrastructure` beserta descendant-nya (`Data Center`, `Helpdesk`, `Rack A1`) dalam satu transaksi Delete lewat sesi API Total Control hingga tersimpan; penugasan Fajar Nugroho di `IT Infrastructure` dan Kevin Susanto di `Data Center` ikut dilepas dan log memuat entri `Remove (Group Deleted)` `Kevin Susanto — Data Center` dengan path tersimpan `Head Office > IT Infrastructure > Data Center`
15. Klik ikon Changelog di toolbar Tab Group Manager
16. Tunggu modal Changelog selesai dimuat
17. Verifikasi modal Changelog tampil dengan Table Tools (anchor permukaan termuat)
18. Verifikasi modal tidak memuat entri `Remove (Group Deleted)` `Kevin Susanto — Data Center`: ancestor `IT Infrastructure` pada path tersimpan sudah tidak ada sehingga tidak dihitung, ancestor `Head Office` tidak dikelola aktor, dan penugasan aktor pada `Logistics Warehouse` bukan ancestor pada path tersimpan
19. Verifikasi entri `Remove (Group Deleted)` `Fajar Nugroho — IT Infrastructure` tidak tampil karena ancestor `Head Office` pada path tersimpan tidak dikelola aktor
20. Tutup modal
21. Unduh Changelog sebagai CSV
22. Verifikasi file Download memuat baris yang sama dengan modal
23. Verifikasi tidak ada baris di file Download yang menyebut `Data Center`
24. Pulihkan group `IT Infrastructure` beserta descendant-nya (`Data Center`, `Helpdesk`, `Rack A1`) lewat seeding API

## Notes

- Asersi isi berkas Download (baris yang dibandingkan dengan layar atau modal) tetap berada di spec fungsional ini dan tidak dipecah ke spec kelas f (konvensi bagian 3 butir 13f, [KEPUTUSAN 2026-11-02]).
- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 24 langkah.
- Langkah penghubung (S-03): langkah 1, 8, 16, 20. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 2–3, 12–14, 24; tidak ada `Verifikasi`.
- Pembagian TC lintas spec: TC-FA-RP-1111 dan 1115 ada di spec 054; TC-FA-RP-1112, 1116, dan 1120 ada di spec 055.
- Asersi absence pada langkah 7 didahului langkah 6 (entri lain pada modal yang sama tampil); pada TC-FA-RP-1119 tidak ada entri lain yang dijamin tampil, sehingga anchor adalah langkah 17 (Table Tools modal Changelog termuat, butir 8b.2 untuk permukaan yang sudah termuat).
- Temuan untuk QA:
  - TC-FA-RP-1118 dan 1119 precondition d menyebut penghapusan group tanpa pelaku dan mekanisme; spec menulisnya lewat sesi API Total Control (kemampuan disediakan tim FE/BE).
  - TC-FA-RP-1119 Expected a: pada kondisi ini modal tidak memuat entri apa pun yang tampak bagi aktor; TC tidak menyebut empty state Changelog sehingga anchor asersi absence adalah Table Tools yang termuat (bukan baris pembanding).
  - Entri `Remove (Group Deleted)` bersifat audit trail permanen; asersi absence antar blok mengandalkan Catatan TC bahwa Pre-setup #24 utuh pada awal tiap TC (seed ulang log disediakan tim FE/BE).
  - Post Condition kedua TC (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
