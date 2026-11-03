---
id: TC-FA-GRP-E2E-180-tab-users-setup-column-uncheck-kolom-name-email-position
title: "Tab Users Setup Column: Uncheck Kolom Name, Email, dan Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-632
  - TC-FA-GRP-633
  - TC-FA-GRP-634
coverage:
  web: automated
---

# Tab Users Setup Column: Uncheck Kolom Name, Email, dan Position

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).

  | Kolom |
  |---|
  | Name |
  | Email |
  | Position |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 9): Buka Popup Setup Column
3. Uncheck kolom pada baris tabel di Popup Setup Column
4. Verifikasi Live Preview langsung menyembunyikan kolom tersebut
5. Klik [Save]
6. Verifikasi kolom tersebut hilang dari tabel
7. Refresh F5, lalu klik angka Total User Warehouse A
8. Verifikasi kolom Division dan Group Role tampil pada tabel
9. Verifikasi konfigurasi bertahan setelah F5 (kolom tersebut tetap hilang dari tabel)

## Notes

- Langkah 2 sampai 9 berulang untuk setiap baris tabel Prerequisites (Name, Email, Position). Kolom yang sudah di-uncheck pada iterasi sebelumnya tetap tersembunyi dan tidak memengaruhi asersi iterasi berikut; sedikitnya dua kolom (Division, Group Role) tetap visible sehingga guard kolom terakhir tidak terpicu. Dipulihkan lewat hook `after`.
- Langkah penghubung (S-03): `Refresh F5, lalu klik angka Total User Warehouse A` (TC tidak menyebut pembukaan ulang popup sesudah F5; lihat Temuan untuk QA).
- Spec memiliki 9 langkah nominal dan 25 langkah setelah ekspansi (3 iterasi x 8 langkah + 1), di bawah smell 35 langkah.
- Asersi tambahan (S-03, 8b.2): langkah `Verifikasi kolom ... tampil pada tabel` sesudah F5 dan sebelum asersi kolom yang hilang menjadi anchor positif; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-632 sampai 634 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
