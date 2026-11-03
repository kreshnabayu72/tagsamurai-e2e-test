---
id: TC-FA-GRP-E2E-185-tab-users-setup-column-geser-drag-kolom-tag-custom-field-dan-kolom-actions
title: "Tab Users Setup Column: Geser (Drag) Kolom TAG dan Custom Field, Satu Kolom Curated per Custom Field Aktif, dan Kolom Actions Hanya Pemicu Column Visibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-652
  - TC-FA-GRP-653
  - TC-FA-GRP-676
  - TC-FA-GRP-954
coverage:
  web: automated
---

# Tab Users Setup Column: Geser (Drag) Kolom TAG dan Custom Field, Satu Kolom Curated per Custom Field Aktif, dan Kolom Actions Hanya Pemicu Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Posisi tujuan drag: paling akhir daftar kolom (setelah kolom terakhir pada daftar Setup Column); tiap iterasi memindahkan kolom pada baris tabel ke posisi itu.

  | Kolom |
  |---|
  | TAG |
  | Custom Field aktif `Phone {runId}` |

- Custom Field spec ini di-seed sendiri (S-11; baris tabel di atas dan TC-676): di hook `before` lewat sesi API aktor dibuat Custom Field User `Phone {runId}` (aktif), `Badge No {runId}` (aktif), dan satu Custom Field nonaktif bersuffix `{runId}` dengan nama dasar `Fixture.groupsTabUsers.cfNonaktif`; hook `after` menghapus ketiganya dan preferensi kolom. Custom Field lain milik client boleh ada; asersi daftar curated hanya memeriksa ketiga Custom Field seeded (lihat Temuan untuk QA).

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

### TC-676: Satu kolom curated per Custom Field aktif

10. Klik icon (⋯) di header kolom terakhir
11. Verifikasi daftar curated memuat `Phone {runId}` dan `Badge No {runId}`
12. Verifikasi daftar curated tidak memuat Custom Field nonaktif (`Fixture.groupsTabUsers.cfNonaktif` bersuffix `{runId}`)
13. Tekan Esc untuk menutup overlay

### TC-954: Kolom Actions hanya pemicu Column Visibility

14. Verifikasi kolom Actions tampil paling kanan
15. Klik header kolom Actions (⋯)
16. Verifikasi klik header membuka dropdown Column Visibility (termasuk kolom curated)
17. Verifikasi tidak ada row action per baris
18. Tekan Esc untuk menutup dropdown

## Notes

- Langkah 2 sampai 9 berulang untuk setiap baris tabel Prerequisites (TAG, Custom Field `Phone {runId}`). Langkah penghubung (S-03): `Refresh F5, lalu klik angka Total User Warehouse A` dan menutup overlay dengan Esc.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-652 dan 653 menulis "ke posisi lain" tanpa posisi tujuan; spec menetapkan posisi paling akhir. TC-676 membutuhkan client dengan Custom Field Phone, Badge No, dan satu nonaktif yang tidak tertulis di Pre-setup; spec men-seed ketiganya di hook `before` dan menghapusnya di hook `after` (S-11).
  - TC-652 dan 653 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
