---
id: TC-GS-ACTLOG-E2E-034-download-log-di-atas-5000-baris-loading-screen-dan-batas-threshold
title: "Download Log Skala Besar (>5.000 Baris): Loading Screen Modal dan Pengujian Batas Threshold"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-136
  - TC-GS-ACTLOG-137
coverage:
  web: automated
---

# Download Log Skala Besar (>5.000 Baris): Loading Screen Modal dan Pengujian Batas Threshold

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Dataset log disiapkan/dimock untuk tepat 5.000 baris dan 5.001 baris pada kedua tab

## Test Steps

### Pengujian Tepat 5.000 Baris (Direct Download)
1. Buka Tab Session, saring data hingga menghasilkan tepat 5.000 baris.
2. Klik icon Download, pilih 'Download as CSV'.
3. Verifikasi berkas langsung terunduh secara instan tanpa menampilkan loading screen modal dan tanpa toast.
### Pengujian 5.001 Baris (Loading Screen Modal)
4. Saring data Tab Session hingga menghasilkan 5.001 baris.
5. Klik icon Download, pilih 'Download as CSV'.
6. Verifikasi sistem menampilkan loading screen modal hingga berkas siap dibuat.
7. Verifikasi setelah proses selesai berkas 'Activity-Log-Session.csv' otomatis terunduh.
8. Verifikasi tidak ada toast sukses dan tidak ada notifikasi in-app yang dikirimkan.
### Verifikasi Threshold pada Tab User Action
9. Buka Tab User Action, uji unduhan pada 5.000 baris (langsung terunduh tanpa loading screen).
10. Uji unduhan Tab User Action pada 5.001 baris, verifikasi loading screen modal muncul hingga berkas selesai terunduh.

## Notes

- Sesuai keputusan NC-03 dan PRD §4.3 S-07, ekspor skala besar menggunakan loading screen sinkron tanpa antrean notifikasi in-app.
