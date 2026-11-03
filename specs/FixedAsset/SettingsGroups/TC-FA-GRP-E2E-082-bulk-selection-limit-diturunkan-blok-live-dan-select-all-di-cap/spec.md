---
id: TC-FA-GRP-E2E-082-bulk-selection-limit-diturunkan-blok-live-dan-select-all-di-cap
title: "Bulk Selection Limit: Centang ke-[Selection Limit]+1 Diblok Live dan Select All Di-Cap Otomatis"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-252
  - TC-FA-GRP-253
coverage:
  web: automated
---

# Bulk Selection Limit: Centang ke-[Selection Limit]+1 Diblok Live dan Select All Di-Cap Otomatis

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): 12 group level 1 kosong `Bulk K01` sampai `Bulk K12` (nama distinct, semuanya memuat huruf `K`) sehingga tabel memuat lebih dari satu halaman (page size default 10). N = jumlah total baris tabel Groups List pada tampilan All Groups (Pre-setup level 1 ditambah 12 group seed), dibaca lewat fixture BE sebelum uji dan bukan dari satu halaman tabel (8b butir 10).
- State global: Selection Limit diturunkan menjadi 5 di Lifecycle Settings > System Limits (Admin Console) oleh hook `before` lewat kemampuan fixture BE yang disediakan tim FE/BE (akun pelaku perubahan limit tidak disebut TC, PRD, atau LLD); hook `after` memulihkan nilai awal. Suite berjalan serial. Teks yang memuat `[Selection Limit]` ditulis dengan nilai 5.
- Jeda waktu nyata: satu jeda 5 detik untuk memastikan toast persist (di bawah batas ±30 detik, disebut sebagai pilihan spec).
- Cleanup di `after`: hapus 12 group seed lewat API.

## Test Steps

### TC-FA-GRP-252: Centang ke-[Selection Limit]+1 diblok live

1. Centang baris 1 sampai baris 5 satu per satu
2. Coba centang checkbox baris 6
3. Verifikasi checkbox baris 6 tampil dan disabled
4. Hover checkbox baris 6
5. Verifikasi tooltip "You've reached the maximum selection of 5 rows."
6. Verifikasi baris 1 sampai baris 5 tetap tercentang
7. Verifikasi bar bulk action aktif
8. Klik (X)

### TC-FA-GRP-253: Select All saat N melebihi Selection Limit di-cap otomatis

9. Centang 1 baris, lalu klik Select All ([N] records)
10. Verifikasi seleksi di-cap ke 5 baris pertama tanpa dialog blokir
11. Verifikasi toast error "Error, only the first 5 of N rows were selected. Narrow your filter to include the rest." (N = total baris dari Prerequisites)
12. Tunggu 5 detik
13. Verifikasi toast error masih tampil (persist sampai di-dismiss)
14. Verifikasi bar bulk action dapat dipakai (Bulk Action aktif)
15. Dismiss toast, lalu klik (X)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 8, 12, 15: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Teks TC memuat placeholder `[Selection Limit]` dan `[Limit] of [Total Rows]`; spec mengisinya dengan nilai 5 dan N dari Prerequisites (S-02: nilai pengganti, bukan perubahan makna). Langkah 11 memakai N total dari seeding (8b butir 10).
- Temuan untuk QA:
  - TC-252 dan TC-253 Expected menyebut "bar aktif" dan "bar tetap bisa dipakai" tanpa menyebut aksi yang dicoba; spec mengasersi Bulk Action aktif.
