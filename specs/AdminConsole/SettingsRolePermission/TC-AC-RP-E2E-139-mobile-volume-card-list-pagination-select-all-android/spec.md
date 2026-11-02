---
id: TC-AC-RP-E2E-139-mobile-volume-card-list-pagination-select-all-android
title: "Mobile Android Volume 105 User: Pagination Card List Default 10 dan Select All Hanya Halaman Aktif Role Detail"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-426
coverage:
  mobile: automated
---

# Mobile Android Volume 105 User: Pagination Card List Default 10 dan Select All Hanya Halaman Aktif Role Detail

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6). Spec hanya membaca dan memilih card secara lokal; tidak ada checkbox CRUD yang diubah dan tidak ada perubahan state server.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang (Tabel Data Uji Pre-setup #22), serta kemampuan tap dan long press. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control entitas `Distributor Seleksi Besar` `Hadi Gunawan`, `totalControlBigRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_BIG_TC_PASSWORD`. Login di aplikasi Android dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun `Siti Nurhaliza`). Nama env `AC_RP_BIG_TC_PASSWORD` dipakai spec 069, 088, 116, dan 138 dengan arti yang sama dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #20 (entitas `Distributor Seleksi Besar` dengan 105 user Standard yang memegang `Manage group`; volume sudah ada di environment dan tidak di-seed spec ini; kelas volume data, bagian 3 prinsip 13e), #22.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `+{runId}-139`, maupun cleanup.
- Hook suite web (`beforeEach` pembuka halaman) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah spec ini, dan flag Guided Tooltip `guided_tooltip_seen_role-permission` untuk akun aktor disetel `true` oleh hook `before` suite (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-AC-RP-426: Card list mobile memakai Pagination default 10 dan Select All hanya memilih card halaman aktif

1. Buka halaman `Settings > Role & Permission` di aplikasi Android
2. Klik tab `System`
3. Pada section Global Role, klik `⋯` pada baris `Manage group` lalu klik `Detail`; hitung card yang tampil dan perhatikan Pagination
4. Verifikasi 10 card tampil (Pagination default 10 per halaman, sama dengan web)
5. Verifikasi Pagination tampil
6. Long press satu card
7. Ketuk `[Select All]` pada Floating Bottom Bulk Bar
8. Verifikasi seluruh card pada halaman aktif yang checkbox-nya enabled tercentang
9. Verifikasi counter "[N] Selected" sama dengan jumlah card tercentang itu (maksimum 10), bukan total 105 baris
10. Pindah ke halaman 2 pada Pagination
11. Verifikasi card pada halaman lain tidak tercentang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03, S-14): langkah 10 (pindah ke halaman 2 agar "card pada halaman lain tidak tercentang" teramati). Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web.
- Pembagian TC lintas spec: TC-AC-RP-427 (Role Detail Global mobile, selection mode) ada di spec 019. Spec ini memuat TC-AC-RP-426 saja, kelas volume data (bagian 3 prinsip 13e) pada perangkat Android.
- Temuan untuk QA:
  - TC-AC-RP-426 Expected a menyebut "Pagination default 10 per halaman" untuk 105 baris, tetapi tidak menyebut halaman terakhir; spec tidak mengasersi isi halaman lain selain card tidak tercentang.
  - Post Condition TC-AC-RP-426 bernilai "-" sehingga tidak ada yang diasersi.
