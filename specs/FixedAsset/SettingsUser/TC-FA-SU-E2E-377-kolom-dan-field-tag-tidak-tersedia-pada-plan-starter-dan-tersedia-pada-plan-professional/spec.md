---
id: TC-FA-SU-E2E-377-kolom-dan-field-tag-tidak-tersedia-pada-plan-starter-dan-tersedia-pada-plan-professional
title: "Kolom dan Field TAG: Tidak Tersedia pada Plan Starter dan Tersedia pada Plan Professional"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-367
coverage:
  web: automated
---

# Kolom dan Field TAG: Tidak Tersedia pada Plan Starter dan Tersedia pada Plan Professional

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: tenant plan Starter `FaUserStarter` dan plan Professional `FaUserPro` (Pre-setup #32), masing-masing memuat pengguna Budi Santoso (TAG `TAG-0001`), serta Pre-setup #20. Perpindahan tenant dengan akun aktor yang sama adalah kemampuan "disediakan tim FE" (TC tidak menyebut caranya, lihat Temuan untuk QA). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- State global: spec ini tidak mengubah plan Client `FaUserMain`. Hook `after` mengembalikan sesi ke tenant `FaUserMain`.
- Setup Column hanya dibuka dan ditutup dengan `[✕]` tanpa `[Save]`, sehingga preferensi kolom tidak berubah.

## Test Steps

### TC-FA-SU-367: Kolom dan field TAG pada plan Starter dan Professional

1. Pindah ke tenant plan Starter `FaUserStarter` dengan akun aktor yang sama, lalu buka Fixed Asset > Settings > User
2. Klik header kolom Actions (⋯), klik `Setup Column...`
3. Verifikasi sedikitnya satu kolom lain tersedia pada daftar Setup Column
4. Verifikasi kolom `TAG` tidak tersedia pada daftar Setup Column
5. Klik `[✕]` pada Setup Column
6. Verifikasi sedikitnya satu kolom lain tampil di tabel User List
7. Verifikasi kolom `TAG` tidak tampil di tabel User List
8. Ketik Search `Budi Santoso`, tekan Enter, klik ⋯ pada baris Budi Santoso, klik `Detail`
9. Verifikasi sedikitnya satu field lain tampil di General Information Detail Budi Santoso
10. Verifikasi field `TAG` tidak tampil di General Information Detail Budi Santoso
11. Pindah ke tenant plan Professional `FaUserPro` dengan akun aktor yang sama, lalu buka Fixed Asset > Settings > User
12. Ketik Search `Budi Santoso`, tekan Enter, klik ⋯ pada baris Budi Santoso, klik `Detail`
13. Verifikasi field `TAG` tampil di General Information Detail Budi Santoso
14. Klik breadcrumb `User`
15. Klik header kolom Actions (⋯), klik `Setup Column...`
16. Verifikasi kolom `TAG` tersedia pada daftar Setup Column
17. Klik `[✕]` pada Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas h (state tenant): ditulis sebagai spec tersendiri (bukan di spec 107) karena TC-FA-SU-367 semula mengubah plan Client `FaUserMain` lewat Principal Automation tanpa justifikasi P-5. Spec ini memakai tenant `FaUserStarter` dan `FaUserPro` (Pre-setup #32) dan tidak mengubah plan apa pun. Per P-5 butir b, ini satu TC objek-uji ringan kelas h tanpa harness eksternal.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 dan 11 (pindah tenant), 2 dan 15 (membuka Setup Column), 5 dan 17 (menutup Setup Column), 8 dan 12 (membuka Detail Budi Santoso), dan 14 (kembali ke User List). Langkah 3, 6, dan 9 adalah anchor positif (kolom atau field lain tampil) untuk asersi absence kolom `TAG` dan field `TAG` pada langkah 4, 7, dan 10 (8b.2).
- Langkah 8 dan 12 juga Search untuk menemukan baris target (R-16, 8b.13): kotak Search kosong sehingga ditulis "Ketik Search"; User List dapat memuat lebih dari satu halaman.
- Temuan untuk QA (S-15): (1) TC-FA-SU-367 langkah 1 menyebut "Login pada tenant plan Starter" tanpa menyebut tenant dan cara berpindah; spec memakai `FaUserStarter` dan `FaUserPro` (varian Pre-setup #32) dan perpindahan "disediakan tim FE". (2) Pre-setup #32 tidak dirinci di TC, termasuk keberadaan Budi Santoso pada kedua tenant. (3) Langkah 4 TC ("Ulangi pada tenant plan Professional") dituliskan sebagai Detail lalu Setup Column; pemeriksaan tabel tidak diulang pada Professional karena Expected c hanya menyebut ketersediaan kolom dan field. (4) Expected c (`—` bila belum paired) bersyarat dan TC tidak menyebut pengguna yang belum paired; hanya ketersediaan kolom dan field `TAG` yang diasersi.
