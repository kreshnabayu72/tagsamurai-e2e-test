---
id: TC-FA-GRP-E2E-181-tab-users-setup-column-uncheck-kolom-division-group-role-dan-centang-activation-status
title: "Tab Users Setup Column: Uncheck Division dan Group Role serta Centang Kolom Curated Activation Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-635
  - TC-FA-GRP-636
  - TC-FA-GRP-638
coverage:
  web: automated
---

# Tab Users Setup Column: Uncheck Division dan Group Role serta Centang Kolom Curated Activation Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).

  | Kolom | Aksi | Efek Live Preview | Posisi di tabel |
  |---|---|---|---|
  | Division | Uncheck | menyembunyikan | hilang dari |
  | Group Role | Uncheck | menyembunyikan | hilang dari |
  | Activation Status | Centang | menampilkan | tampil di |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 9): Buka Popup Setup Column
3. Lakukan Aksi pada baris tabel terhadap kolom pada baris tabel di Popup Setup Column
4. Verifikasi Live Preview langsung memberi Efek Live Preview pada baris tabel untuk kolom tersebut
5. Klik [Save]
6. Verifikasi kolom pada baris tabel hilang dari atau tampil di tabel sesuai kolom Posisi di tabel
7. Refresh F5, lalu klik angka Total User Warehouse A
8. Verifikasi kolom Name, Email, dan Position tampil pada tabel
9. Verifikasi konfigurasi bertahan setelah F5 (posisi kolom di tabel sama dengan sebelum F5)

## Notes

- Langkah 2 sampai 9 berulang untuk setiap baris tabel Prerequisites (Division, Group Role, Activation Status); kolom Aksi dan Efek pada tabel menentukan asersi tiap iterasi tanpa langkah bersyarat. Kolom Name, Email, dan Position tetap visible sehingga guard kolom terakhir tidak terpicu. Dipulihkan lewat hook `after`.
- Langkah penghubung (S-03): `Refresh F5, lalu klik angka Total User Warehouse A` (TC tidak menyebut pembukaan ulang popup sesudah F5; lihat Temuan untuk QA).
- Spec memiliki 9 langkah nominal dan 25 langkah setelah ekspansi (3 iterasi x 8 langkah + 1), di bawah smell 35 langkah.
- Asersi tambahan (S-03, 8b.2): langkah `Verifikasi kolom ... tampil pada tabel` sesudah F5 dan sebelum asersi kolom yang hilang menjadi anchor positif; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-635, 636, dan 638 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
