---
id: TC-FA-GRP-E2E-182-tab-users-setup-column-centang-kolom-curated-temporary-user-until-tag-dan-custom-field
title: "Tab Users Setup Column: Centang Kolom Curated Temporary User, Temporary Until, TAG, dan Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-639
  - TC-FA-GRP-640
  - TC-FA-GRP-641
  - TC-FA-GRP-642
coverage:
  web: automated
---

# Tab Users Setup Column: Centang Kolom Curated Temporary User, Temporary Until, TAG, dan Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).

  | Kolom |
  |---|
  | Temporary User |
  | Temporary Until |
  | TAG |
  | Custom Field aktif Phone |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 8): Buka Popup Setup Column
3. Centang kolom pada baris tabel di Popup Setup Column
4. Verifikasi Live Preview langsung menampilkan kolom tersebut
5. Klik [Save]
6. Verifikasi kolom tersebut tampil di tabel
7. Refresh F5, lalu klik angka Total User Warehouse A
8. Verifikasi konfigurasi bertahan setelah F5 (kolom tersebut tetap tampil di tabel)

## Notes

- Langkah 2 sampai 8 berulang untuk setiap baris tabel Prerequisites. Kolom yang dicentang pada iterasi sebelumnya tetap tampil dan tidak memengaruhi asersi iterasi berikut; dipulihkan lewat hook `after`.
- Langkah penghubung (S-03): `Refresh F5, lalu klik angka Total User Warehouse A` (TC tidak menyebut keadaan popup sesudah F5).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-639 sampai 642 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
