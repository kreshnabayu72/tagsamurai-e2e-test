---
id: TC-FA-GRP-E2E-176-tab-users-sort-kolom-tag-custom-field-dan-nilai-kosong-tie-breaker
title: "Tab Users Sort Kolom TAG, Custom Field, dan Nilai Kosong (Akhir Asc, Awal Desc, Tie-Breaker Name)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-623
  - TC-FA-GRP-624
  - TC-FA-GRP-1137
coverage:
  web: automated
---

# Tab Users Sort Kolom TAG, Custom Field, dan Nilai Kosong (Akhir Asc, Awal Desc, Tie-Breaker Name)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Kolom yang disort memuat nilai bervariasi (huruf besar dan kecil, angka, dan kosong) dengan sedikitnya dua nilai distinct, termasuk sepasang nilai yang membedakan case-insensitive dari case-sensitive (mis. `anggur` dan `Apel`).

  | Kolom |
  |---|
  | TAG |
  | Custom Field Phone |

- Untuk TC-1137: Warehouse A memuat user dengan Position kosong dan beberapa user ber-Position sama (page size 10 default). Kolom TAG dan Custom Field Phone adalah kolom curated yang ditampilkan lewat Column Visibility; pemulihan lewat hook `after` (hapus preferensi kolom).

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 8): Pastikan kolom pada baris tabel tampil (kolom curated ditampilkan via Column Visibility)
3. Klik header kolom pada baris tabel 1x
4. Verifikasi urutan ascending A-Z case-insensitive (mis. `anggur` sebelum `Apel`)
5. Klik header kolom pada baris tabel 2x
6. Verifikasi urutan descending Z-A
7. Klik header kolom pada baris tabel 3x
8. Verifikasi urutan kembali ke default tabel (Name A-Z)

### TC-1137: Nilai kosong dan tie-breaker Name

9. Klik header Position 1x (ascending)
10. Pindah ke halaman terakhir
11. Verifikasi baris Position kosong berada di akhir seluruh dataset
12. Telusuri halaman satu per satu dari halaman pertama sampai terakhir
13. Verifikasi user ber-Position sama diurut Name A-Z secara konsisten antar halaman
14. Klik header Position 2x (descending)
15. Pindah ke halaman pertama
16. Verifikasi baris Position kosong berada di awal
17. Telusuri halaman satu per satu dari halaman pertama sampai terakhir
18. Verifikasi user ber-Position sama diurut Name A-Z secara konsisten antar halaman
19. Klik header Position 3x

## Notes

- Langkah 2 sampai 8 berulang untuk setiap baris tabel Prerequisites (TAG, Custom Field Phone). Langkah penghubung (S-03): pindah halaman, menelusuri halaman, dan klik header Position ke-3 untuk mengembalikan urutan default di akhir spec.
- Spec memiliki 19 langkah nominal dan 26 langkah setelah ekspansi (1 + 2 iterasi x 7 langkah + 11), di bawah smell 35 langkah.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-1137 menyebut "amati seluruh halaman"; spec menelusuri halaman satu per satu karena tie-breaker Name hanya teramati jika baris sama-Position berada di lebih dari satu halaman (S-14).
