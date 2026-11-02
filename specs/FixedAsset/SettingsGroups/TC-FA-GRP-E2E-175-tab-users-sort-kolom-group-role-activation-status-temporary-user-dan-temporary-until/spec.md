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

  | Kolom |
  |---|
  | Group Role |
  | Activation Status |
  | Temporary User |

- Kolom Activation Status dan Temporary User adalah kolom curated yang ditampilkan lewat Column Visibility pada iterasi masing-masing; Temporary Until juga curated dan ditampilkan sebelum disort. Pemulihan: hapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 8): Pastikan kolom pada baris tabel tampil (kolom curated ditampilkan via Column Visibility)
3. Klik header kolom pada baris tabel 1x
4. Verifikasi urutan ascending A-Z case-insensitive (mis. `anggur` sebelum `Apel`)
5. Klik header kolom pada baris tabel 2x
6. Verifikasi urutan descending Z-A
7. Klik header kolom pada baris tabel 3x
8. Verifikasi urutan kembali ke default tabel (Name A-Z)

### TC-622: Sort Temporary Until

9. Tampilkan kolom Temporary Until via Column Visibility
10. Klik header Temporary Until 1x
11. Verifikasi urutan Oldest First
12. Klik header Temporary Until 2x
13. Verifikasi urutan Newest First
14. Klik header Temporary Until 3x
15. Verifikasi urutan kembali ke default tabel (Name A-Z)

## Notes

- Langkah 2 sampai 8 berulang untuk setiap baris tabel Prerequisites (Group Role, Activation Status, Temporary User); Temporary Until memakai urutan Oldest First dan Newest First sehingga ditulis sebagai blok sendiri (langkah 9 sampai 15).
- Spec memiliki 15 langkah nominal dan 29 langkah setelah ekspansi (3 iterasi x 7 langkah + 8), di bawah smell 35 langkah.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - Pre-setup tidak menyebut nilai Temporary Until bervariasi; spec mensyaratkan sedikitnya dua tanggal distinct pada Warehouse A.
