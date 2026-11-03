---
id: TC-AC-SU-E2E-170-tidak-ada-notifikasi-in-app-untuk-event-tertentu
title: "Tidak Ada Notifikasi In-App ke Target untuk Event Deactivate dan Assign Total Control"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-585
  - TC-AC-SU-587
coverage:
  web: automated
---

# Tidak Ada Notifikasi In-App ke Target untuk Event Deactivate dan Assign Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Konteks kedua: jendela browser privat untuk target (objek asersi notifikasi), dibuka per blok TC dan ditutup bersama sesi loginnya sebelum blok berikutnya (S-09); password target dari `Spectra.env.AC_SU_SEEDED_PASSWORD` (nama env baru, didaftarkan pemilik repo).
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (target Activated, dapat login ke Admin Console, memiliki satu notifikasi lama sebagai anchor; jumlah notifikasi seeding dibaca dari Fixture BE sebagai baseline N):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Jane Smith {runId}-170A` | `janesmith+{runId}-170a@qwertysystem.net` | Activated, Active, tanpa tier (TC-585) |
| U2 | `Mike Tan {runId}-170B` | `miketan+{runId}-170b@qwertysystem.net` | Activated, Active, tanpa tier (TC-587) |

- Kemampuan teknis: Fixture BE (seeding user, notifikasi anchor, dan pembacaan jumlah notifikasi); konteks browser kedua. Jendela tunggu 5 detik tanpa memuat ulang halaman sebelum asersi absence notifikasi adalah pilihan spec (bukan nilai TC atau PRD). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-585: Deactivate
1. Ketik Search `Jane Smith {runId}-170A`, tekan Enter
2. Toggle Active ON ke OFF pada baris U1, lalu klik `[Deactivate]` pada dialog Deactivate User
3. Tunggu aksi selesai, lalu toggle Active OFF ke ON pada baris U1 dan klik `[Activate]` pada dialog Activate User
4. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U1, lalu klik lonceng notifikasi navbar
5. Verifikasi notifikasi anchor milik U1 yang sudah ada tampil di daftar
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Verifikasi jumlah notifikasi U1 sama dengan baseline N (tidak ada notifikasi baru untuk event Deactivate)
### TC-AC-SU-587: Assign Total Control
8. Tutup konteks kedua dan hapus sesi loginnya, klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu assign U2 (`Mike Tan {runId}-170B`) ke Total Control
9. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U2, lalu klik lonceng notifikasi navbar
10. Verifikasi notifikasi anchor milik U2 yang sudah ada tampil di daftar
11. Tunggu 5 detik tanpa memuat ulang halaman
12. Verifikasi jumlah notifikasi U2 sama dengan baseline N (tidak ada notifikasi baru untuk event Assign Total Control)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), re-aktivasi U1 (langkah 3, sesuai Langkah 2 TC-585 "aktifkan kembali dulu lalu login"), pembukaan konteks kedua dan login target (langkah 4 dan serupa), menutup konteks kedua beserta sesi loginnya (S-09), dan jendela tunggu 5 detik.
- Asersi absence notifikasi memakai anchor positif (notifikasi lama yang tampil, bagian 8b butir 2) dan asersi jumlah terhadap baseline N dari seeding; konteks kedua target adalah objek asersi (kelas c).
- Temuan untuk QA:
  - TC-585 dan TC-587 menyebut "Notifikasi lain yang sudah ada tetap tampil (anchor)" tanpa menyebut asal notifikasi lama; spec men-seed satu notifikasi anchor per target (kemampuan disediakan tim FE/BE).
  - TC-585 mensyaratkan mengaktifkan kembali target sebelum login; event Activate itu sendiri tidak dinyatakan TC memicu notifikasi atau tidak, sehingga jumlah notifikasi dibandingkan terhadap baseline seeding.
  - TC memakai nama literal `Jane Smith` dan `Mike Tan`; spec memakai nama bersuffix (S-12). Password target seeding memakai env baru `AC_SU_SEEDED_PASSWORD`.
