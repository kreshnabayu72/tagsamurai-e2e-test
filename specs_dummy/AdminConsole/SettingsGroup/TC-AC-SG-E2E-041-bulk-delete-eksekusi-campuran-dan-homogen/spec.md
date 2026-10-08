---
id: TC-AC-SG-E2E-041-bulk-delete-eksekusi-campuran-dan-homogen
title: "Eksekusi Bulk Delete sukses: varian homogen, varian campuran dengan pelompataan baris, dan penanganan level 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-70
  - TC-AC-SG-71
  - TC-AC-SG-74
  - TC-AC-SG-76
coverage:
  web: automated
---

# Eksekusi Bulk Delete sukses: varian homogen, varian campuran dengan pelompataan baris, dan penanganan level 1

## Prerequisites

- Login sebagai Role: Total Control
- Dataset campuran: group level 1 kosong, subgroup kosong, dan subgroup memiliki member

## Test Steps

### Eksekusi Varian Homogen
1. Centang 2 group kosong yang aman (termasuk 1 group level 1)
2. Klik `[Delete]` di Bulk Action Bar lalu klik `[Delete]` pada dialog konfirmasi
3. Verifikasi toast sukses homogen `"Success, group has been deleted."` tampil
4. Verifikasi kedua group terhapus
### Eksekusi Varian Campuran (Skipped Items)
5. Centang 2 group aman dan 1 group yang memiliki member
6. Klik `[Delete]` di Bulk Action Bar
7. Verifikasi dialog menampilkan 2 kelompok bullet: `"The following will be deleted:"` dan `"The following have members and won't be deleted:"` dengan penutup `"Are you sure you want to continue? This action cannot be undone."`
8. Klik tombol `[Continue]`
9. Verifikasi toast sukses campuran tampil: `"Success, group has been deleted. Some items were skipped (still has members)."`
10. Verifikasi hanya group yang aman yang terhapus, sedangkan group ber-member tetap tersisa

## Notes

- TC-AC-SG-78 (race condition server re-evaluasi kondisi item) dicakup pada pengujian backend.
