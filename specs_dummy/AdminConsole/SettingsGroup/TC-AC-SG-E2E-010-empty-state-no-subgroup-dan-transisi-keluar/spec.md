---
id: TC-AC-SG-E2E-010-empty-state-no-subgroup-dan-transisi-keluar
title: "Empty state No subgroup yet saat node tanpa child dipilih dan transisi keluar saat buat anak pertama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-185
  - TC-AC-SG-195
coverage:
  web: automated
---

# Empty state No subgroup yet saat node tanpa child dipilih dan transisi keluar saat buat anak pertama

## Prerequisites

- Login sebagai Role: Total Control
- Node level 1 `"Region B"` yang tidak memiliki subgroup sama sekali

## Test Steps

### Empty State No Subgroup Yet
1. Buka `Settings > Group`
2. Klik node `"Region B"` pada sidebar
3. Verifikasi Group Context Header menampilkan `"Region B"`
4. Verifikasi tabel utama merender empty state dengan judul `"No subgroup yet"`
5. Verifikasi subtitle empty state menampilkan `"This group does not have any subgroups."` (§7.1)
### Transisi Keluar dari Empty State
6. Klik elipsis `[⋯]` pada `"Region B"` di sidebar lalu klik `[+ Add Subgroup]`
7. Isi Group Name dengan `"Sub B1"`
8. Klik `[Submit]`
9. Verifikasi toast sukses `"Success, group has been created."` tampil
10. Verifikasi empty state seketika hilang dari tabel utama
11. Verifikasi tabel utama kini merender 1 baris baru `"Sub B1"`
12. Verifikasi node `"Region B"` di sidebar memunculkan icon expander dengan child `"Sub B1"` di bawahnya

## Notes

- Empty state transisional membuktikan reaktivitas tabel terhadap mutasi child pertama.
