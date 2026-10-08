---
id: TC-GS-ACTLOG-E2E-033-download-log-resilience-kegagalan-jaringan-dan-toast-error
title: "Ketahanan Ekspor Log: Penanganan Kegagalan Jaringan / HTTP 500 dan Toast Feedback Error di Kedua Tab"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-138
  - TC-GS-ACTLOG-139
coverage:
  web: automated
---

# Ketahanan Ekspor Log: Penanganan Kegagalan Jaringan / HTTP 500 dan Toast Feedback Error di Kedua Tab

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Mock/intercept endpoint export CSV/XLSX untuk mengembalikan status HTTP 500 Internal Server Error

## Test Steps

### Simulasi Error Download Tab Session
1. Buka Tab Session di menu Global Settings > Activity Log.
2. Aktifkan simulasi intercept kegagalan jaringan HTTP 500 pada endpoint unduh.
3. Klik tombol Download > 'Download CSV'.
4. Verifikasi tidak ada berkas rusak yang terunduh ke peramban.
5. Verifikasi toast banner error berwarna merah muncul dengan pesan: 'Error, failed to download Activity-Log-Session.'.
6. Uji hal yang sama untuk 'Download XLSX', verifikasi toast error yang sama muncul.
### Simulasi Error Download Tab User Action
7. Klik tab 'User Action'.
8. Klik tombol Download > 'Download CSV'.
9. Verifikasi toast banner error berwarna merah muncul dengan pesan: 'Error, failed to download Activity-Log-User-Action.'.
10. Verifikasi antarmuka tabel tetap utuh dan pengguna dapat melanjutkan interaksi normal.

## Notes

- Kegagalan ekspor jaringan ditangani dengan graceful feedback tanpa merusak state halaman.
