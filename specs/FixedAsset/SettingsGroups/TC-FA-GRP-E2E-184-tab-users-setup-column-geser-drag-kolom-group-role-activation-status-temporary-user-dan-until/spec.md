---
id: TC-FA-GRP-E2E-184-tab-users-setup-column-geser-drag-kolom-group-role-activation-status-temporary-user-dan-until
title: "Tab Users Setup Column: Geser (Drag) Kolom Group Role, Activation Status, Temporary User, dan Temporary Until"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-647
  - TC-FA-GRP-649
  - TC-FA-GRP-650
  - TC-FA-GRP-651
coverage:
  web: automated
---

# Tab Users Setup Column: Geser (Drag) Kolom Group Role, Activation Status, Temporary User, dan Temporary Until

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Posisi tujuan drag: paling akhir daftar kolom (setelah kolom terakhir pada daftar Setup Column); tiap iterasi memindahkan kolom pada baris tabel ke posisi itu.

  | Kolom |
  |---|
  | Group Role |
  | Activation Status |
  | Temporary User |
  | Temporary Until |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 9): Buka Popup Setup Column
3. Pastikan kolom pada baris tabel tampil (kolom curated dicentang di Popup Setup Column)
4. Drag kolom pada baris tabel ke posisi paling akhir daftar kolom
5. Verifikasi urutan Live Preview mengikuti posisi baru (kolom tersebut berada di posisi paling akhir)
6. Klik [Save]
7. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
8. Refresh F5, lalu klik angka Total User Warehouse A
9. Verifikasi urutan kolom tabel tetap berubah setelah F5

## Notes

- Langkah 2 sampai 9 berulang untuk setiap baris tabel Prerequisites (8b butir 7). Kolom curated (Activation Status, Temporary User, Temporary Until) dicentang lebih dulu agar perubahan urutan teramati di tabel; dipulihkan lewat hook `after`.
- Langkah penghubung (S-03): mencentang kolom curated dan `Refresh F5, lalu klik angka Total User Warehouse A`.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-647 sampai 651 menulis "ke posisi lain" tanpa posisi tujuan, dan TC curated tidak menyebut mencentang kolom padahal Expected b memeriksa urutan di tabel; spec menetapkan posisi paling akhir dan mencentang kolom curated.
  - TC-647 sampai 651 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
