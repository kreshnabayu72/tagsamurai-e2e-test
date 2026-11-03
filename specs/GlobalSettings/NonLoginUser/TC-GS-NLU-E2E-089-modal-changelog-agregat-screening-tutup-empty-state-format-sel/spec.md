---
id: TC-GS-NLU-E2E-089-modal-changelog-agregat-screening-tutup-empty-state-format-sel
title: "Modal Changelog Agregat: Screening, Tutup, Empty State, dan Format Sel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-309
  - TC-GS-NLU-310
  - TC-GS-NLU-311
  - TC-GS-NLU-312
coverage:
  web: automated
---

# Modal Changelog Agregat: Screening, Tutup, Empty State, dan Format Sel

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun kedua (hanya TC-GS-NLU-311): Total Control Client PT Bintang Timur (Tabel Data Uji Pre-setup No. 15; tanpa Non-Login User dan tanpa riwayat Changelog Non-Login User). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password `Spectra.env.GS_BINTANGTIMUR_TC_PASSWORD` (nama usulan; belum terdaftar di `.env.example` dan `spectra.config.ts`). Login lewat langkah 25 sampai 27; hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `GS_TC_PASSWORD`, `GS_BINTANGTIMUR_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor Total Control, kemampuan disediakan tim FE/BE): Non-Login User `Budi Kurniawan {runId}-089` (Division Operations, Represented By `Ahmad Fauzi`), dibuat oleh `Siti N` sehingga muncul entri Create (Field `Name`, Old Value kosong). Data ini dipakai TC-GS-NLU-309 dan TC-GS-NLU-312; dihapus di hook `after`.
- Bagian Client PT Bintang Timur: Client dipastikan belum memiliki riwayat Changelog Non-Login User; spec tidak melakukan aksi apa pun pada Client itu sebelum langkah 28. Cara memastikan Client tanpa riwayat pada audit trail permanen disediakan tim FE/BE.
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Kemampuan teknis: klik area gelap di luar modal, tekan `Esc`, hover tooltip Modified By, membaca baris pertama tabel.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-309: Screening Modal Changelog Non-Login User

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
2. Verifikasi header modal: Title `"Changelog: Non-Login User"` dan tombol `✕`
3. Verifikasi toolbar modal: `Search | Filter | Download`
4. Verifikasi placeholder Search `"Search name, action, field, modified by, or value..."`
5. Verifikasi kolom: `Date (sortable) | Action (sortable) | User Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
6. Verifikasi default sort Date terbaru di atas: baris pertama adalah entri Create `Budi Kurniawan {runId}-089`
7. Verifikasi footer modal: pagination default 10

### TC-GS-NLU-310: Modal Changelog tidak menutup lewat klik backdrop dan menutup lewat close dan Esc

8. Klik area gelap di luar modal
9. Verifikasi modal Changelog tetap terbuka
10. Klik `✕`
11. Verifikasi modal Changelog tertutup
12. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
13. Tekan `Esc`
14. Verifikasi modal Changelog tertutup

### TC-GS-NLU-312: Format sel Modal Changelog: User Name teks biasa, Modified By singkat dengan tooltip, Date format General Settings

15. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
16. Ketik Search `Budi Kurniawan {runId}-089`, tekan Enter
17. Verifikasi User Name `Budi Kurniawan {runId}-089` pada baris Create tampil sebagai teks biasa (bukan link)
18. Verifikasi Modified By pada baris itu berformat `[first name lengkap] [huruf pertama last name]`, yaitu `Siti N`
19. Arahkan kursor ke Modified By pada baris itu
20. Verifikasi tooltip Modified By menampilkan nama lengkap `Siti Nurhaliza`
21. Verifikasi Date pada baris itu mengikuti General Settings (Date Format `dd/MM/yy`, Time Format 24 jam)
22. Verifikasi Old Value kosong pada baris Create tampil `—`
23. Klik `(←)` pada kotak Search
24. Klik `✕` untuk menutup Modal Changelog

### TC-GS-NLU-311: Empty state Modal Changelog saat belum ada riwayat

25. Ganti akun: klik Logout dari akun Total Control Siti Nurhaliza
26. Login sebagai Total Control Client PT Bintang Timur (email dan password lihat `## Prerequisites`)
27. Buka Global Settings > User > User List > sub-tab Non-Login User
28. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
29. Verifikasi empty state Modal Changelog: ilustrasi dengan judul `"No changelog yet"` dan deskripsi `"Activities and changes will appear here."`

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan kecuali TC-GS-NLU-311 yang ditaruh paling akhir karena memakai akun Client lain (ganti akun eksplisit pada langkah 25 sampai 27, S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 12, 15, dan 28 (membuka Modal Changelog); langkah 16 (Search `Budi Kurniawan {runId}-089` untuk menemukan baris Create milik spec, R-16); langkah 23 dan 24 (mengosongkan Search dan menutup modal sebelum ganti akun).
- Asersi tambahan (konkretisasi Expected): langkah 6 ("default sort Date terbaru di atas" TC-GS-NLU-309 b.iii ditulis sebagai baris pertama adalah entri Create seeding spec ini, karena audit trail permanen dan hanya entri terbarulah yang dijamin berada di baris pertama, S-14); langkah 16 sampai Verifikasi sesudahnya memakai nama bersuffix, bukan `Budi Kurniawan` polos.
- Pembagian TC lintas spec: Search, Filter, Sort, Pagination, Download, dan Setup Column Modal Changelog agregat ada di spec 090 sampai 094 dan 135; TC-GS-NLU-498 (kegagalan Download) ada di spec resilience.
- Temuan untuk QA:
  - TC-GS-NLU-311: TC tidak menyebut Client, akun, maupun cara mendapat entitas tanpa riwayat pada audit trail permanen. Spec memakai Client PT Bintang Timur (Pre-setup No. 15, tanpa Non-Login User) dan menuliskan mekanisme "disediakan tim FE/BE"; email dan password akun Client itu tidak tertulis di TC (S-11, S-13, R-19).
  - TC-GS-NLU-312: TC menyebut Modified By tooltip `Siti Nurhaliza` dan baris "Create Budi Kurniawan" tanpa menyebut siapa pembuat record Pre-setup; spec memakai record milik spec yang dibuat Total Control (S-06). Format gabungan tanggal dan waktu pada sel Date tidak disebut TC; spec hanya mengasersi kesesuaian dengan Date Format dan Time Format General Settings.
  - TC-GS-NLU-309: kolom Column Visibility (⋯) pada header tabel disebut `unsortable`; spec mengasersinya sebagai bagian daftar kolom tanpa langkah klik sort.
