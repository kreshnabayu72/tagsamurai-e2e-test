---
id: TC-FA-CAT-E2E-194-modal-changelog-sort-3-state-kolom-modified-by-dan-date
title: "Modal Changelog: Sort 3-State pada Kolom Modified By dan Date"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-398
  - TC-FA-CAT-399
coverage:
  web: automated
---

# Modal Changelog: Sort 3-State pada Kolom Modified By dan Date

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Changelog CatMain bertambah oleh spec lain dan tidak pernah dikosongkan. Asersi isi dan urutan hanya atas baris seed Pre-setup #23, dibatasi Filter Date 20 Jun 2026 sampai 1 Jul 2026 (rentang tanggal Example Data PRD §4.1, tanggal baris spec lain berada di luar rentang itu; S-14). Filter dipasang lewat langkah penghubung.

## Test Steps

### TC-FA-CAT-398: Sort 3-state Changelog kolom Modified By

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal, pilih rentang tanggal 20 Jun 2026 sampai 1 Jul 2026 pada field Date, lalu klik `[Apply]`
3. Klik header Modified By satu kali
4. Verifikasi kolom terurut Ascending dengan nama lengkap underlying (bukan format singkat)
5. Klik header Modified By kedua kali
6. Verifikasi kolom terurut Descending kebalikan penuh dari Ascending
7. Klik header Modified By ketiga kali
8. Verifikasi kolom kembali Netral dengan urutan default Date Newest First

### TC-FA-CAT-399: Sort 3-state Changelog kolom Date

9. Klik header Date satu kali
10. Verifikasi kolom Date terurut Ascending (↑) Oldest First (tanggal terlama di atas)
11. Klik header Date kedua kali
12. Verifikasi kolom Date terurut Descending (↓) Newest First (kebalikan penuh)
13. Klik header Date ketiga kali
14. Verifikasi kolom Date kembali Netral dengan urutan default Date Newest First
15. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-FA-CAT-397 ada di spec 115. TC-FA-CAT-398 dan TC-FA-CAT-399 memakai modal yang sama sehingga modal tidak dibuka ulang di antara keduanya; state Sort dikembalikan ke Netral oleh klik ketiga TC-FA-CAT-398 sebelum TC-FA-CAT-399 (S-09).
- Langkah penghubung (S-03, S-14): langkah 2 membatasi Changelog ke rentang Date baris seed Pre-setup #23; langkah terakhir menutup modal.
- Temuan untuk QA:
  - TC-FA-CAT-398 menyebut Ascending "nama lengkap underlying (bukan format singkat)" sementara kolom Modified By tampil berformat [First Name] [Last Initial] (konvensi R-14); spec mengasersi urutan berdasarkan nama lengkap underlying dan tidak mengasersi teks yang tampil. Mohon QA menjelaskan cara memverifikasi nama lengkap underlying dari UI.
