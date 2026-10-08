---
id: TC-GS-DIV-E2E-047-bulk-delete-campuran-sebagian-in-use-dan-batal
title: "Bulk Delete Campuran (D-03): Segregasi Item Dihapus vs Dilewati, Pembatalan via Cancel, dan Eksekusi Continue dengan Toast Skipping"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-134
  - TC-GS-DIV-135
  - TC-GS-DIV-287
coverage:
  web: automated
---

# Bulk Delete Campuran (D-03): Segregasi Item Dihapus vs Dilewati, Pembatalan via Cancel, dan Eksekusi Continue dengan Toast Skipping

## Prerequisites

- Login sebagai Role: Total Control
- Pilih campuran: 1 divisi bebas relasi dan 1 divisi in-use (Human Resources)
- User berada di Global Settings > User > Division
- Division `Data Analytics` bebas relasi; `Human Resources` dipakai user
- Division `Engineering` bebas relasi (TC-GS-DIV-30); `Human Resources` dipakai user

## Test Steps

### Bulk Delete campuran menampilkan Dialog campuran dengan dua kelompok (TC-GS-DIV-134)

1. Centang baris `Human Resources` dan `Data Analytics`
2. Klik aksi `[Delete]` pada Bulk Action Bar
3. Verifikasi Title `Delete Divisions` (severity warning)
4. Verifikasi Body: `The following will be deleted:` bullet `Data Analytics`
5. Verifikasi Lalu `The following are still in use and will be skipped:` bullet `Human Resources`
6. Verifikasi Lalu `Are you sure you want to continue? This action cannot be undone.`
7. Verifikasi Tombol `[Cancel]` dan `[Continue]` (filled, danger)

### Continue pada Bulk Delete campuran menghapus yang aman dan melewati yang in-use (TC-GS-DIV-135)

8. Centang baris `Human Resources` dan `Data Analytics`
9. Klik aksi `[Delete]` pada Bulk Action Bar
10. Klik `[Continue]`
11. Verifikasi Division `Data Analytics` terhapus dan `Human Resources` tetap ada
12. Verifikasi Muncul toast sukses: `Success, division has been deleted. Some items were skipped.`
13. Verifikasi Hanya 1 entri log Delete tercatat (untuk `Data Analytics`)

### Cancel pada dialog Bulk Delete campuran tidak menghapus apa pun (TC-GS-DIV-287)

14. Centang baris `Human Resources` dan `Engineering`
15. Klik aksi `[Delete]` pada Bulk Action Bar
16. Klik `[Cancel]` pada dialog `Delete Divisions`
17. Verifikasi Dialog `Delete Divisions` tertutup tanpa toast
18. Verifikasi Baris `Human Resources` dan `Engineering` tetap ada di tabel
19. Verifikasi Tidak ada entri log baru

## Notes

- Memvalidasi Dialog 3 (D-03: title "Delete Divisions", segregasi "will be deleted" vs "will be skipped", [Cancel] dan [Continue]), pembatalan tidak menghapus data, dan eksekusi memunculkan toast "Success, division has been deleted. Some items were skipped." (NC-10, PRD §4.2d).
- Sumber pemetaan test case granular: TC-GS-DIV-134, TC-GS-DIV-135, TC-GS-DIV-287.
