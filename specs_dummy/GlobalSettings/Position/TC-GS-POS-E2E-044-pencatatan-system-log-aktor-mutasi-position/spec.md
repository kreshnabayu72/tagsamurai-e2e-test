---
id: TC-GS-POS-E2E-044-pencatatan-system-log-aktor-mutasi-position
title: "External Harness: Pencatatan mutasi Position ke System Log Tab pada Detail User aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-251
  - TC-GS-POS-305
  - TC-GS-POS-306
  - TC-GS-POS-307
coverage:
  web: automated
---

# External Harness: Pencatatan mutasi Position ke System Log Tab pada Detail User aktor

## Prerequisites

- Login sebagai Total Control (Budi Santoso)
- Akses ke User List > Detail User Budi Santoso > Tab System Log

## Test Steps

### Pencatatan Create pada System Log Aktor

1. Buat record Position baru "Log Test Specialist"
2. Buka menu Global Settings > User > User List
3. Buka halaman Detail User milik aktor yang sedang login (Budi Santoso)
4. Klik tab "System Log"
5. Verifikasi entri baru tercatat dengan aksi pembuatan master data Position

### Pencatatan Edit pada System Log Aktor

6. Kembali ke tab Position, edit "Log Test Specialist" menjadi "Lead Log Test Specialist"
7. Buka kembali Tab System Log pada Detail User Budi Santoso
8. Verifikasi entri Edit Position tercatat lengkap dengan detail perubahannya

### Pencatatan Delete & Bulk Delete pada System Log Aktor

9. Hapus record "Lead Log Test Specialist"
10. Verifikasi entri Delete Position tercatat pada System Log
11. Lakukan Bulk Delete pada 2 record Position bebas relasi
12. Verifikasi pada System Log tercatat satu entri terpisah untuk masing-masing item yang terhapus (total 2 entri)

## Notes

- Menggabungkan pencatatan ke System Log aktor (TC-GS-POS-251, 305, 306, 307) dalam kelas External Harness.
