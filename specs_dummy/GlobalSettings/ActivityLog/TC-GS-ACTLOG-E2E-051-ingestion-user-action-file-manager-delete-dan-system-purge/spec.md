---
id: TC-GS-ACTLOG-E2E-051-ingestion-user-action-file-manager-delete-dan-system-purge
title: "Ingestion User Action: File Manager Permanently Delete dan Background System Auto-Purge Actor Audit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-209
  - TC-GS-ACTLOG-210
  - TC-GS-ACTLOG-211
coverage:
  web: automated
---

# Ingestion User Action: File Manager Permanently Delete dan Background System Auto-Purge Actor Audit

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat berkas yang dihapus permanen dari Recycle Bin File Manager oleh admin
- Terdapat berkas kedaluwarsa di Recycle Bin yang dibersihkan secara otomatis oleh worker sistem

## Test Steps

### File Manager: Permanently Delete oleh Admin
1. Buka Tab User Action di Global Settings > Activity Log.
2. Cari entri penghapusan berkas permanen dari Recycle Bin File Manager.
3. Verifikasi kolom Object menampilkan 'File Manager', dan kolom Action menampilkan 'Permanently Delete'.
4. Buka Filter Panel, verifikasi 'Permanently Delete' tersedia dalam pilihan dropdown Action.
### Background System Auto-Purge & System Actor
5. Cari entri pembersihan otomatis berkas Recycle Bin oleh cron job sistem.
6. Verifikasi kolom Modified By menampilkan teks 'System' utuh (tanpa pemotongan atau singkatan nama).
7. Arahkan kursor tetikus ke teks 'System', verifikasi tooltip menampilkan 'System'.
8. Buka Filter Panel, periksa dropdown filter Modified By.
9. Verifikasi opsi 'System' muncul dalam daftar pilihan filter Modified By.
10. Terapkan filter Modified By = 'System', verifikasi tabel hanya menyaring entri yang dieksekusi oleh sistem.

## Notes

- Sistem otomatis dicatat dengan identitas 'System' dan memiliki perlakuan khusus pada tooltip serta filter.
