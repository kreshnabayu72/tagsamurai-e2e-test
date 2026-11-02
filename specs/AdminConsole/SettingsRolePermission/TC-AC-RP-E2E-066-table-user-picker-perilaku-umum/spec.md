---
id: TC-AC-RP-E2E-066-table-user-picker-perilaku-umum
title: "Table User Picker: Selection Counter, Kolom Curated, dan Eksklusi User yang Sudah Di-assign oleh Sesi Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-221
  - TC-AC-RP-230
  - TC-AC-RP-232
  - TC-AC-RP-411
coverage:
  web: automated
---

# Table User Picker: Selection Counter, Kolom Curated, dan Eksklusi User yang Sudah Di-assign oleh Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Admin B (TC-AC-RP-230 dan TC-AC-RP-411): sesi API sesuai Hook suite "Sesi API aktor"; akun Admin B disediakan tim FE. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Pelaku kedua lewat sesi API tidak membuka konteks UI kedua.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`Alex Tan`, `John Dohan`, `Maya Putri` Pending Activation, `Agus Salim` akun sementara), #24 (Admin B).
- Data Dinamis: spec ini tidak membuat Data Dinamis; target Assign oleh Admin B adalah user Pre-setup `Alex Tan`. Nilai bersuffix `+{runId}-066` tidak dipakai karena tidak ada data yang dibuat spec.
- Perubahan Pre-setup: `Alex Tan` ditetapkan sebagai Total Control (TC-AC-RP-230) dan Read Only (TC-AC-RP-411) oleh Admin B. Pemulihan ke Standard memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Changelog Tab Total Control dan Read Only menerima entri Assign dan Remove; Last Updated berubah.
- Pemulihan Setup Column: preferensi kolom picker dihapus di browser pada hook `after` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-221: Selection counter popup picker

1. Klik "+ Assign"
2. Centang `Alex Tan` dan `John Dohan`
3. Verifikasi selection counter tampil "2 Users selected"
4. Verifikasi selection counter berupa komponen Bulk Action tanpa menu aksi
5. Klik `✕` pada popup

### TC-AC-RP-232: Kolom curated picker opt-in via Setup Column

6. Klik "+ Assign"
7. Klik header kolom Actions pada picker lalu pilih Column Visibility
8. Centang Activation Status dan Temporary User
9. Verifikasi kolom Activation Status tampil dan `Maya Putri` bernilai `Pending Activation`
10. Verifikasi kolom Temporary User tampil dengan teks `Yes`/`No` dan `Agus Salim` bernilai `Yes`
11. Verifikasi kolom Email tetap Visible dan hideable
12. Klik `✕` pada popup

### TC-AC-RP-230: User yang sudah di-assign Total Control tidak muncul di picker Assign

13. Sesi B (sesi API Admin B): Assign Total Control ke `Alex Tan` hingga Total Control tersimpan
14. Sesi A: klik "+ Assign"
15. Sesi A: ketik Search `Alex Tan` pada kolom Search picker, tekan Enter
16. Verifikasi `Alex Tan` tidak muncul di daftar kandidat picker (empty state hasil pencarian "No results found")
17. Verifikasi tidak ada jalur UI untuk Assign ulang `Alex Tan` ke Total Control
18. Klik `✕` pada popup
19. Pulihkan baseline automation: `Alex Tan` kembali Standard

### TC-AC-RP-411: User yang sudah di-assign Read Only tidak muncul di picker Assign Read Only

20. Muat ulang halaman
21. Sesi A: klik tab `Read Only`
22. Sesi B (sesi API Admin B): Assign Read Only ke `Alex Tan` hingga Read Only tersimpan
23. Sesi A: klik "+ Assign"
24. Sesi A: ketik Search `Alex Tan` pada kolom Search picker, tekan Enter
25. Verifikasi `Alex Tan` tidak muncul di daftar kandidat picker (empty state hasil pencarian "No results found")
26. Klik `✕` pada popup
27. Pulihkan baseline automation: `Alex Tan` kembali Standard

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Pembagian TC lintas spec: TC-AC-RP-437 dan TC-AC-RP-231 ada di spec 128.
- Langkah penghubung (S-03): langkah 5, 12, 18, dan 26 (tutup popup; popup picker ditutup `✕` tanpa dialog Unsaved Changes karena bukan form), 19 dan 27 (pemulihan baseline), 20 (muat ulang agar Tab Total Control hasil pemulihan tampil sebelum berpindah tab).
- Search (R-16): langkah 15 dan 24 mencari target absence `Alex Tan` pada kolom Search picker; empty state "No results found" adalah anchor positif asersi absence (bagian 8b butir 2).
- Urutan TC: 221, 232, 230, 411. Alasan: blok tanpa pelaku kedua dan tanpa perubahan data didahulukan (S-10).
- Temuan untuk QA:
  - TC-AC-RP-230 Expected b ("tidak ada jalur UI untuk Assign ulang") tidak punya Expected terukur lain selain empty state pada Expected a; langkah 17 mengasersi bahwa tidak ada baris `Alex Tan` yang dapat dicentang pada picker.
  - TC-AC-RP-230 dan TC-AC-RP-411 menyebut "dua sesi browser paralel" (Manual Only kriteria d) dengan Sesi B hanya memicu perubahan state; spec memakai sesi API untuk Sesi B. Bila QA menghendaki sesi UI kedua, spec dipindah ke kelas c.
  - TC-AC-RP-232 Expected menyebut `Maya Putri` dan `Agus Salim` tanpa Search; baris tersebut bergantung pada halaman yang teramati (S-14).
  - TC-AC-RP-232 tidak menyatakan apakah preferensi kolom picker tersimpan; spec menghapus preferensi kolom di browser pada hook `after`.
  - Email Admin B (Pre-setup #24) tidak tertulis; ditulis "disediakan tim FE".
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
