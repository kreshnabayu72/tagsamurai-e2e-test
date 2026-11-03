---
id: TC-FA-GRP-E2E-174-tab-users-sort-kolom-name-email-position-dan-division
title: "Tab Users Sort Kolom Name, Email, Position, dan Division"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-614
  - TC-FA-GRP-615
  - TC-FA-GRP-616
  - TC-FA-GRP-617
coverage:
  web: automated
---

# Tab Users Sort Kolom Name, Email, Position, dan Division

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Kolom yang disort memuat nilai bervariasi (huruf besar dan kecil, angka, dan kosong) dengan sedikitnya dua nilai distinct, termasuk sepasang nilai yang membedakan case-insensitive dari case-sensitive (mis. `anggur` dan `Apel`).

  | Kolom |
  |---|
  | Name |
  | Email |
  | Position |
  | Division |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 8): Pastikan kolom pada baris tabel tampil
3. Klik header kolom pada baris tabel 1x
4. Verifikasi urutan ascending A-Z case-insensitive (mis. `anggur` sebelum `Apel`)
5. Klik header kolom pada baris tabel 2x
6. Verifikasi urutan descending Z-A
7. Klik header kolom pada baris tabel 3x
8. Verifikasi urutan kembali ke default tabel (Name A-Z)

## Notes

- Langkah 2 sampai 8 berulang untuk setiap baris tabel Prerequisites (Name, Email, Position, Division); satu `Verifikasi` per klausa tetap dipertahankan (8b butir 7).
- Spec memiliki 8 langkah nominal dan 29 langkah setelah ekspansi (4 iterasi x 7 langkah + 1), di bawah smell 35 langkah.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-615 sampai 617 menulis Expected c "urutan kembali ke default tabel (Name A→Z)" untuk klik ke-3 pada kolom selain Name sama dengan TC-614; spec mengikuti teks TC.
