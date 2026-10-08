---
id: TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position
title: "Audit Log: Pencatatan Create, Edit, Delete, Bulk Delete, snapshot, dan import omission di Changelog & Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-242
  - TC-GS-POS-243
  - TC-GS-POS-244
  - TC-GS-POS-245
  - TC-GS-POS-247
  - TC-GS-POS-248
  - TC-GS-POS-249
  - TC-GS-POS-250
  - TC-GS-POS-252
  - TC-GS-POS-253
coverage:
  web: automated
---

# Audit Log: Pencatatan Create, Edit, Delete, Bulk Delete, snapshot, dan import omission di Changelog & Activity Log

## Prerequisites

- Login sebagai Total Control
- Hak akses ke Global Settings > User > Position dan Activity Log

## Test Steps

### Verifikasi Entri Create & Field Name

1. Buka tab Position, klik "[+ Position]", buat record "Network Engineer", klik "[Submit]"
2. Buka Popup Changelog: Position
3. Verifikasi entri baru tercatat dengan Action "Create", Position Name "Network Engineer", Field "—", Old Value "—", New Value "—"
4. Buka menu Activity Log, verifikasi entri Create Position tercatat selaras

### Verifikasi Entri Edit & Snapshot Persistensi

5. Edit "Network Engineer" menjadi "Senior Network Engineer", simpan
6. Buka Popup Changelog
7. Verifikasi entri Edit tercatat dengan Action "Edit", Field "Position Name" (NC-05), Old Value "Network Engineer", New Value "Senior Network Engineer", dan kolom Position Name berisi nama sesudah perubahan (NC-08)
8. Lakukan edit kedua mengubahnya menjadi "Principal Network Engineer"
9. Verifikasi baris snapshot entri edit sebelumnya tidak berubah/rusak
10. Lakukan perubahan kapitalisasi saja, verifikasi tercatat sebagai entri Edit di Changelog

### Verifikasi Entri Delete & Bulk Delete

11. Hapus record "Principal Network Engineer"
12. Verifikasi entri Delete tercatat di Changelog dengan Action "Delete"
13. Lakukan Bulk Delete campuran (sebagian sukses, sebagian diskip karena in-use)
14. Verifikasi Changelog hanya mencatat entri untuk item yang benar-benar terhapus (item yang diskip tidak dicatat terhapus)

### Pengecualian Hasil Import vs Create Missing Positions

15. Amati riwayat untuk record "Field Technician" yang berasal dari Import Type Position
16. Verifikasi import massal tidak menghasilkan entri di Popup Changelog modul Position (NC/PRD)
17. Verifikasi record yang dibuat dari fitur [Create Missing Positions] tercatat sebagai entri Create normal

## Notes

- Menggabungkan seluruh validasi audit log mutasi Position (TC-GS-POS-242, 243, 244, 245, 247, 248, 249, 250, 252, 253).
