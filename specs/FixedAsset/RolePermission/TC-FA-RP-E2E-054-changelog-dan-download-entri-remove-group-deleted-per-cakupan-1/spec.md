---
id: TC-FA-RP-E2E-054-changelog-dan-download-entri-remove-group-deleted-per-cakupan-1
title: "Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1111
  - TC-FA-RP-1115
coverage:
  web: automated
---

# Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager (`IT Infrastructure`) (Pre-setup #5, Fajar Nugroho), email `groupManager_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #18 (pohon group), #24 (Company Changelog: log 25 entri campuran). Entri `Remove (Group Deleted)` dihasilkan oleh penghapusan group pada langkah seeding tiap blok; entri dari blok lain dianggap tidak ada pada awal tiap blok karena Pre-setup dianggap utuh pada awal tiap TC (Catatan TC).
- Kemampuan teknis: sesi API Total Control (Pre-setup #2) untuk menghapus dan memulihkan group; pembaca berkas unduhan CSV (disediakan tim FE/BE); hook `after` memulihkan group yang dihapus spec ini.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1111: Changelog dan Download Tab Group Manager bagi Group Manager: entri Remove (Group Deleted) tetap tampil dengan nama group tersimpan

1. Klik Tab `Group Manager`
2. Hapus group `Data Center` lewat sesi API Total Control hingga tersimpan; log memuat entri `Remove (Group Deleted)` Kevin Susanto dengan path tersimpan `Head Office > IT Infrastructure > Data Center` dan entri Group Manager `Lina Marlina — Head Office`
3. Klik ikon Changelog di toolbar Tab Group Manager
4. Amati entri modal
5. Verifikasi modal memuat entri Action `Remove (Group Deleted)` dengan User Name — Group Name `Kevin Susanto — Data Center`, Field `Group Manager`, Old Value `Assigned`, New Value `—`
6. Verifikasi nama group `Data Center` tampil dari nama tersimpan pada entri walau group sudah tidak ada di hierarki; entri tampil karena path tersimpan memuat `IT Infrastructure` yang dikelola aktor
7. Verifikasi entri `Lina Marlina — Head Office` tidak tampil karena di luar cakupan `IT Infrastructure`
8. Tutup modal
9. Unduh Changelog sebagai CSV
10. Verifikasi file Download memuat baris yang sama dengan modal
11. Verifikasi file Download memuat baris `Remove (Group Deleted)` dengan nama group `Data Center`
12. Pulihkan group `Data Center` lewat seeding API

### TC-FA-RP-1115: Changelog dan Download Tab Group Manager bagi Group Manager: entri Remove (Group Deleted) untuk group yang semula di luar cakupan aktor tidak tampil

13. Hapus group `Data Center` dan group `Logistics Warehouse` (sibling `IT Infrastructure`, Group Manager Hesti Rahma lewat seed API) lewat sesi API Total Control hingga tersimpan; log memuat dua entri `Remove (Group Deleted)` dengan path tersimpan `Head Office > IT Infrastructure > Data Center` dan `Head Office > Logistics Warehouse`
14. Klik ikon Changelog di toolbar Tab Group Manager
15. Amati entri modal
16. Verifikasi modal memuat entri `Remove (Group Deleted)` dengan User Name — Group Name `Kevin Susanto — Data Center` (group semula berada di bawah cakupan `IT Infrastructure`)
17. Verifikasi entri `Remove (Group Deleted)` `Hesti Rahma — Logistics Warehouse` tidak tampil karena path tersimpan `Head Office > Logistics Warehouse` tidak memuat group dalam cakupan aktor
18. Tutup modal
19. Unduh Changelog sebagai CSV
20. Verifikasi file Download memuat baris yang sama dengan modal, dan baris `Kevin Susanto — Data Center` ada
21. Verifikasi tidak ada baris di file Download yang menyebut `Hesti Rahma` atau `Logistics Warehouse`
22. Pulihkan group `Data Center` dan `Logistics Warehouse` (beserta `Dock 1`) lewat seeding API

## Notes

- Asersi isi berkas Download (baris yang dibandingkan dengan layar atau modal) tetap berada di spec fungsional ini dan tidak dipecah ke spec kelas f (konvensi bagian 3 butir 13f, [KEPUTUSAN 2026-11-02]).
- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- Langkah penghubung (S-03): langkah 1, 8, 18. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 2, 12–13, 22; tidak ada `Verifikasi`.
- TC-FA-RP-1111 dan 1115 punya Post Condition pemulihan group; dipenuhi langkah seeding pemulihan dan hook `after` (S-09).
- Pembagian TC lintas spec: TC-FA-RP-1112, 1116, dan 1120 ada di spec 055; TC-FA-RP-1118 dan 1119 ada di spec 299. TC-FA-RP-1111, 1115, 1118, dan 1119 menguji Changelog Tab Group Manager; TC-FA-RP-1112 dan 1116 menguji Changelog Detail Role Group Role.
- Temuan untuk QA:
  - TC-FA-RP-1111, 1115: precondition d menyebut group "sudah dihapus di Settings > Groups" tanpa menyebut pelaku dan mekanismenya. Spec menulis penghapusan lewat sesi API Total Control (kemampuan disediakan tim FE/BE); log memuat entri yang dihasilkan penghapusan itu.
  - Entri `Remove (Group Deleted)` bersifat audit trail permanen; asersi absence pada TC-FA-RP-1115 (entri `Hesti Rahma — Logistics Warehouse` dan baris di file) dan blok sesudahnya tidak dapat memisahkan entri baru dari entri blok lain bila log tidak di-seed ulang. Spec mengandalkan aturan Catatan TC bahwa Pre-setup #24 utuh pada awal tiap TC (seed ulang log disediakan tim FE/BE).
  - Cara membuka dan memilih format unduh Changelog (`Download as CSV` pada modal) tidak dirinci TC; spec menulis "Unduh Changelog sebagai CSV" mengikuti TC.
  - TC-FA-RP-1111 Post Condition dan TC-FA-RP-1115 Post Condition tidak punya langkah observasi dan tidak diasersi.
