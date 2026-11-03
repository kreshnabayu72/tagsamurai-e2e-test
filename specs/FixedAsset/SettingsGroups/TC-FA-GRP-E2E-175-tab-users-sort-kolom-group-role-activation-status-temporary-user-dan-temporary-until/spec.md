---
id: TC-FA-GRP-E2E-175-tab-users-sort-kolom-group-role-activation-status-temporary-user-dan-temporary-until
title: "Tab Users Sort Kolom Group Role, Activation Status, Temporary User, dan Temporary Until"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-618
  - TC-FA-GRP-620
  - TC-FA-GRP-621
  - TC-FA-GRP-622
coverage:
  web: automated
---

# Tab Users Sort Kolom Group Role, Activation Status, Temporary User, dan Temporary Until

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Kolom yang disort memuat nilai bervariasi (huruf besar dan kecil, angka, dan kosong) dengan sedikitnya dua nilai distinct, termasuk sepasang nilai yang membedakan case-insensitive dari case-sensitive (mis. `anggur` dan `Apel`).

  | Kolom default (sudah tampil, tidak perlu dicentang) |
  |---|
  | Group Role |

  | Kolom curated (perlu dicentang lewat Column Visibility) |
  |---|
  | Activation Status |
  | Temporary User |

- Kolom Activation Status dan Temporary User adalah kolom curated yang ditampilkan lewat Column Visibility pada iterasi masing-masing; Temporary Until juga curated dan ditampilkan sebelum disort. Pemulihan: hapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Untuk setiap baris tabel kolom default (langkah 2 sampai 7): Klik header kolom pada baris tabel 1x
3. Verifikasi urutan ascending A-Z case-insensitive (mis. `anggur` sebelum `Apel`)
4. Klik header kolom pada baris tabel 2x
5. Verifikasi urutan descending Z-A
6. Klik header kolom pada baris tabel 3x
7. Verifikasi urutan kembali ke default tabel (Name A-Z)
8. Untuk setiap baris tabel kolom curated (langkah 8 sampai 14): Tampilkan kolom pada baris tabel via Column Visibility
9. Klik header kolom pada baris tabel 1x
10. Verifikasi urutan ascending A-Z case-insensitive (mis. `anggur` sebelum `Apel`)
11. Klik header kolom pada baris tabel 2x
12. Verifikasi urutan descending Z-A
13. Klik header kolom pada baris tabel 3x
14. Verifikasi urutan kembali ke default tabel (Name A-Z)

### TC-622: Sort Temporary Until

15. Tampilkan kolom Temporary Until via Column Visibility
16. Klik header Temporary Until 1x
17. Verifikasi urutan Oldest First
18. Klik header Temporary Until 2x
19. Verifikasi urutan Newest First
20. Klik header Temporary Until 3x
21. Verifikasi urutan kembali ke default tabel (Name A-Z)

## Notes

- Langkah 2 sampai 7 berulang untuk baris tabel kolom default (Group Role); langkah 8 sampai 14 berulang untuk baris tabel kolom curated (Activation Status, Temporary User) dan diawali langkah menampilkan kolom lewat Column Visibility, karena kolom default sudah tampil dan tidak perlu dicentang (8b butir 7). Temporary Until memakai urutan Oldest First dan Newest First sehingga ditulis sebagai blok sendiri (langkah 15 sampai 21).
- Spec memiliki 21 langkah nominal dan 28 langkah setelah ekspansi (1 iterasi x 6 langkah + 2 iterasi x 7 langkah + 8), di bawah smell 35 langkah.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - Pre-setup tidak menyebut nilai Temporary Until bervariasi; spec mensyaratkan sedikitnya dua tanggal distinct pada Warehouse A.
