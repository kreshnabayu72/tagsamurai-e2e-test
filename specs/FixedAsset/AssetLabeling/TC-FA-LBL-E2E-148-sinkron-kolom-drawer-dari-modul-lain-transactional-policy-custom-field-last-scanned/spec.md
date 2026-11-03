---
id: TC-FA-LBL-E2E-148-sinkron-kolom-drawer-dari-modul-lain-transactional-policy-custom-field-last-scanned
title: "Sinkron Kolom Drawer dari Modul Lain (Transactional Policy, Custom Field, Last Scanned)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-563
  - TC-FA-LBL-564
  - TC-FA-LBL-565
coverage:
  web: automated
---

# Sinkron Kolom Drawer dari Modul Lain (Transactional Policy, Custom Field, Last Scanned)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Sesi 2 hanya memicu perubahan di modul lain lewat sesi API (bukan sesi UI kedua); sesi 1 (UI) yang diasersi menerima pembaruan tanpa memuat ulang halaman.
- Akun aktor hook `before`: Total Control Company Probe (Pre-setup #37, pengguna `Total Control Probe`; email pola `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = nama company itu), `Fixture.assetLabeling.akun.totalControlProbe`, `Spectra.env.FA_TC_PROBE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Ganti akun di tengah spec (satu kali): Gate-Full Company Gate (Pre-setup #44; email pola `gateFull_automated_{namaCompany}@qwertysystem.net`), `Fixture.assetLabeling.akun.gateFull`, `Spectra.env.FA_GATE_FULL_PASSWORD` (langkah 13 sampai 15). Hook `after` mengembalikan sesi ke akun default suite.
- Env var: `Spectra.env.FA_TC_PROBE_PASSWORD` dan `Spectra.env.FA_GATE_FULL_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Pre-setup: #37 Company Probe, #38 dan #44 Company Gate (label `Gate Label` dengan Asset Name `Gate Item`).
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-148`, Color `Fixture.assetLabeling.warnaSeed`):
  - TC-FA-LBL-563 (Company Probe): label `Policy Sync 563 {runId}-148` tertempel pada aset `Policy Sync Asset {runId}-148` (Asset Name `Policy Sync Item {runId}-148`, seluruh policy Off).
  - TC-FA-LBL-564 (Company Gate): Custom Field Active `Sync Field 564 {runId}-148` (General, Text, Scope Asset Name `Gate Item`).
  - TC-FA-LBL-565 (Company Probe): label `Scan Sync 565 {runId}-148` tertempel pada aset `Scan Sync Asset {runId}-148` yang belum pernah dipindai; Task Audit yang memuat aset itu.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor untuk sesi 2 (mengubah Transactional Policy Asset Name, menonaktifkan Custom Field, dan memindai aset pada Audit), fixture BE untuk seeding, dan penerimaan pembaruan real-time (push) pada sesi 1; endpoint tidak ditulis di TC.
- State global: konfigurasi kolom Drawer (Setup Column) disimpan sebagai preferensi browser; hook `after` menghapus preferensi itu (bagian 4). Custom Field dan Transactional Policy seed dihapus atau dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-563: Ubah Transactional Policy Asset Name memperbarui kolom Transactional Policy di Drawer

1. Ketik Search `Policy Sync 563 {runId}-148`, tekan Enter, lalu buka Drawer `Policy Sync 563 {runId}-148`
2. Buka Setup Column Drawer, centang kolom `Transactional Policy`, lalu klik `[Save]`
3. Verifikasi sel `Transactional Policy` aset `Policy Sync Asset {runId}-148` menampilkan `—`
4. Sesi 2 (sesi API): ubah policy Borrow Asset Name `Policy Sync Item {runId}-148` menjadi On hingga perubahan tersimpan
5. Verifikasi sel `Transactional Policy` aset `Policy Sync Asset {runId}-148` menampilkan ikon Borrow tanpa muat ulang halaman (real-time push)
6. Tutup Drawer

### TC-FA-LBL-565: Pindai aset pada Audit memperbarui kolom Last Scanned di Drawer

7. Ganti isi kotak search dengan `Scan Sync 565 {runId}-148`, tekan Enter, lalu buka Drawer `Scan Sync 565 {runId}-148`
8. Buka Setup Column Drawer, centang kolom `Last Scanned`, lalu klik `[Save]`
9. Verifikasi sel `Last Scanned` aset `Scan Sync Asset {runId}-148` menampilkan `—`
10. Sesi 2 (sesi API): pindai aset `Scan Sync Asset {runId}-148` pada Task Audit hingga pemindaian tersimpan
11. Verifikasi sel `Last Scanned` menampilkan tanggal pemindaian sesuai format General Settings tanpa muat ulang halaman (real-time push)
12. Tutup Drawer

### TC-FA-LBL-564: Nonaktifkan Custom Field menghilangkan kolomnya dari Setup Column Drawer

13. Ganti akun: logout dari Total Control Company Probe
14. Login sebagai Gate-Full Company Gate (Pre-setup #44)
15. Buka Fixed Asset > Settings > Asset Master > tab Labels, ketik Search `Gate Label`, tekan Enter, lalu buka Drawer `Gate Label`
16. Buka Setup Column Drawer
17. Verifikasi kolom `Sync Field 564 {runId}-148` tersedia di Setup Column dan berstatus Hidden secara default
18. Centang kolom `Sync Field 564 {runId}-148`, lalu klik `[Save]`
19. Verifikasi kolom `Sync Field 564 {runId}-148` tampil di tabel Drawer
20. Buka Setup Column Drawer
21. Sesi 2 (sesi API): ubah Custom Field `Sync Field 564 {runId}-148` menjadi Inactive hingga perubahan tersimpan
22. Verifikasi Setup Column masih memuat kolom lain (kolom `Asset Name`)
23. Verifikasi kolom `Sync Field 564 {runId}-148` hilang dari Setup Column tanpa muat ulang halaman (real-time push)
24. Tutup Setup Column
25. Verifikasi kolom `Sync Field 564 {runId}-148` hilang dari tabel Drawer tanpa muat ulang halaman (real-time push)
26. Tutup Drawer

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 7, 15 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 6, 12, 13, 14, 16, 20, 24, 26 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan: akun Company Probe dipakai untuk TC-FA-LBL-563 dan 565, dan Gate-Full untuk TC-FA-LBL-564; urutan di spec TC-FA-LBL-563, 565, lalu 564 (penyimpangan urutan TC, bagian 3) supaya hanya satu kali ganti akun (langkah 13 sampai 15); tiap TC memakai seed sendiri dan tidak bergantung pada TC lain.
- Asersi "Setup Column masih memuat kolom lain" (langkah 22) adalah anchor absence kolom `Sync Field 564` (bagian 8b butir 2); bukan bagian Expected TC (S-03).
- Temuan untuk QA:
  - TC-FA-LBL-563, 564, dan 565 bertanda Manual Only (d) dua sesi paralel di TC sumber; sesi 2 hanya memicu perubahan state di modul lain, sehingga spec memakainya lewat sesi API dan mengasersi sesi 1 (UI) saja (P-2 [2026-10-30]).
  - TC-FA-LBL-563 dan 565 menyebut "sesi 2: ubah policy / pindai pada Audit" tanpa memerinci mekanismenya (UI Settings > Asset Transactional Policy atau Audit mobile); spec menulis kemampuan sesi API tim FE/BE dan tidak mengarang endpoint (S-13).
  - Aktor sesi 2 pada TC-FA-LBL-563 sampai 565 tidak disebut TC; spec memakai akun yang sama dengan sesi 1 lewat sesi API.
  - TC-FA-LBL-565 menyebut `task_item.scanned_at` Audit sebagai sumber nilai; TC-FA-LBL-563 mencantumkan dependensi NC-14 pada kolom Dependensi TC sumber.
