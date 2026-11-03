---
id: TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline
title: "Screening Halaman Custom Fields dan Isi Tabel Baseline Tab General"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-1
  - TC-FA-CF-2
  - TC-FA-CF-5
  - TC-FA-CF-10
  - TC-FA-CF-12
  - TC-FA-CF-13
coverage:
  web: automated
---

# Screening Halaman Custom Fields dan Isi Tabel Baseline Tab General

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif, General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` (nama field, Data Type, Value Setting, Placeholder, Scope, Value Type, Required, Modified By, Last Updated). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah (General Settings Alpha tetap pada nilai baseline). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-1: Screening halaman Settings > Custom Fields tab General

1. Amati Header, Body, dan Footer halaman tanpa mengisi atau mengklik apa pun
2. Verifikasi Header: Breadcrumb `Settings > Custom Fields` (dua segmen)
3. Verifikasi segmen `Settings` pada Breadcrumb tidak dapat diklik
4. Verifikasi segmen `Custom Fields` pada Breadcrumb tidak dapat diklik
5. Verifikasi Header: tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
6. Verifikasi Header: Tab `General (aktif) | Purchasing | Accounting`
7. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Custom Field]` tampil
8. Verifikasi tidak ada Page Title di bawah Breadcrumb
9. Verifikasi Body: kolom `Checkbox | Active (sortable) | Field Name (sortable) | Data Type (sortable) | Value Setting (sortable) | Placeholder (sortable) | Scope (sortable) | Value Type (sortable) | Required (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable — klik header = buka Overlay Column Visibility, isi per baris = row action menu)`
10. Verifikasi Body: delapan baris custom field tab General tampil
11. Verifikasi Footer: pagination default 10 baris per halaman

### TC-FA-CF-2: Tabs Bar tab General aktif pada client berlisensi FA-7

12. Amati Tabs Bar
13. Verifikasi Tabs Bar menampilkan `General | Purchasing | Accounting` berurutan dengan `General` aktif
14. Verifikasi tab `Accounting` tampil enabled tanpa icon gembok 🔒
15. Verifikasi tab `Accounting` dapat diklik (tidak disabled)

### TC-FA-CF-5: Delapan baris tab General dengan nilai kolom sesuai definisi PRD

16. Verifikasi urutan baris: `Asset Serial Tag`, `Compliance File`, `Depreciated Ratio`, `Equipment Class`, `Legacy Tag`, `Operating Voltage`, `Storage Capacity`, `Total Cost`
17. Verifikasi baris `Asset Serial Tag`: Active ON, Data Type `Text`, Value Setting `—`, Placeholder `Enter asset serial tag`, Scope `General`, Value Type `Specific`, Required `Yes`, Modified By `Budi S`, Last Updated `17/10/26, 10:45`
18. Verifikasi baris `Total Cost`: Active ON, Data Type `Formula`, Value Setting `—`, Placeholder `—`, Scope `General`, Value Type `—`, Required `—`, Modified By `Joko W`, Last Updated `13/10/26, 16:30`
19. Verifikasi baris `Depreciated Ratio`: switch Active OFF, Data Type `Percentage`, Value Setting `2 Decimal Places`

### TC-FA-CF-10: Value Type dan Required strip untuk field Formula

20. Verifikasi kolom Value Type baris `Total Cost` menampilkan `—`
21. Verifikasi kolom Required baris `Total Cost` menampilkan `—`

### TC-FA-CF-12: Last Updated mengikuti Date Format dan Time Format General Settings

22. Verifikasi kolom Last Updated baris `Asset Serial Tag` menampilkan `17/10/26, 10:45`

### TC-FA-CF-13: Kolom Active menampilkan switch ON dan OFF

23. Verifikasi switch Active baris `Asset Serial Tag` pada posisi ON
24. Verifikasi switch Active baris `Depreciated Ratio` pada posisi OFF

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Seluruh asersi adalah baca halaman (screening) tanpa aksi yang mengubah data; subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 1, 2, 5, 10, 12, 13 (screening dahulu, S-10). Tidak ada TC yang mengubah state tabel, sehingga tidak ada langkah pembersihan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 12 (mengamati halaman dan Tabs Bar sesuai langkah uji TC).
- Langkah 3 dan 4 adalah dua klausa Header i TC-FA-CF-1 ("tidak ada segmen yang dapat diklik"); diasersi sebagai label statis tanpa klik karena TC tidak memberi langkah klik. Langkah 15 (tab `Accounting` dapat diklik) diasersi dari state enabled tanpa mengklik, supaya spec ini tidak berpindah tab.
- Langkah 17 sampai 19 menulis satu `Verifikasi` per baris dengan seluruh sel yang disebut Expected TC (daftar kolom satu baris disebut utuh).
- Last Updated pada langkah 17 dan 22 bernilai sama dengan Expected TC-FA-CF-5 b dan TC-FA-CF-12; keduanya mengandalkan Date Format baseline Company Alpha (Pre-setup #11) tanpa mengubah General Settings (R-08).
- Temuan untuk QA:
  - TC-FA-CF-12 Precondition b merujuk "Pre-setup #11 dan #27", padahal #27 adalah varian General Settings (`dd MMM yy`, 12 jam, `USD`) sedangkan Expected `17/10/26, 10:45` mengikuti baseline #11; spec memakai #11 dan tidak mengubah General Settings.
  - TC-FA-CF-1 Header ii-iv dan Body ii menyebut "Delapan baris" bersama pagination 10 baris per halaman; spec mengasersi keduanya apa adanya (delapan baris pada satu halaman).
  - TC-FA-CF-5 b mengasersi Placeholder `Enter asset serial tag`, sedangkan Pre-setup #12 hanya menyatakan Placeholder dikosongkan dengan nilai efektif default tipe; aturan default untuk tipe Text tidak ada di Data Uji TC.
  - TC-FA-CF-2 b menyatakan tab `Accounting` "dapat diklik" tanpa langkah klik; spec tidak mengklik.
