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

  | Kolom default (sudah tampil, tidak perlu dicentang) |
  |---|
  | Group Role |

  | Kolom curated (perlu dicentang di Popup Setup Column) |
  |---|
  | Activation Status |
  | Temporary User |
  | Temporary Until |

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Untuk setiap baris tabel kolom default (langkah 2 sampai 8): Buka Popup Setup Column
3. Drag kolom pada baris tabel ke posisi paling akhir daftar kolom
4. Verifikasi urutan Live Preview mengikuti posisi baru (kolom tersebut berada di posisi paling akhir)
5. Klik [Save]
6. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
7. Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
8. Verifikasi urutan kolom tabel tetap berubah setelah F5
9. Untuk setiap baris tabel kolom curated (langkah 9 sampai 16): Buka Popup Setup Column
10. Centang kolom pada baris tabel di Popup Setup Column
11. Drag kolom pada baris tabel ke posisi paling akhir daftar kolom
12. Verifikasi urutan Live Preview mengikuti posisi baru (kolom tersebut berada di posisi paling akhir)
13. Klik [Save]
14. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
15. Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
16. Verifikasi urutan kolom tabel tetap berubah setelah F5

## Notes

- Langkah 2 sampai 8 berulang untuk baris tabel kolom default (Group Role); langkah 9 sampai 16 berulang untuk baris tabel kolom curated (Activation Status, Temporary User, Temporary Until) dan diawali langkah mencentang kolom, karena kolom default sudah tampil (8b butir 7). Kolom curated dicentang lebih dulu agar perubahan urutan teramati di tabel; dipulihkan lewat hook `after`. Spec memiliki 16 langkah nominal dan 32 langkah setelah ekspansi (1 + 7 + 3 x 8), di bawah smell 35 langkah.
- Langkah penghubung (S-03): mencentang kolom curated dan `Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A`.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-647 sampai 651 menulis "ke posisi lain" tanpa posisi tujuan, dan TC curated tidak menyebut mencentang kolom padahal Expected b memeriksa urutan di tabel; spec menetapkan posisi paling akhir dan mencentang kolom curated.
  - TC-647 sampai 651 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
