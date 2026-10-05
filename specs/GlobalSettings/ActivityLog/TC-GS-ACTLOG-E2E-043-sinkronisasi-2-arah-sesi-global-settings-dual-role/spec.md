---
id: TC-GS-ACTLOG-E2E-043-sinkronisasi-2-arah-sesi-global-settings-dual-role
title: "Sinkronisasi 2-arah sesi Global Settings Dual-Role mencatat event Session started dan Session ended"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-226
coverage:
  web: automated
---

# Sinkronisasi 2-arah sesi Global Settings Dual-Role mencatat event Session started dan Session ended

## Prerequisites

- Login sebagai Role: Total Control masuk dan keluar dari modul Global Settings

## Test Steps

1. Login dan klik card "Global Settings" dari portal aplikasi
2. Buka menu `Global Settings > Activity Log > Tab Session`
3. Verifikasi entri baru dengan Activity "Session", Note "Session started", dan Status strip (`—`) tercatat di baris teratas
4. Tutup sesi Global Settings (atau biarkan idle hingga sesi berakhir)
5. Buka kembali Tab Session dari sesi baru
6. Verifikasi entri baru dengan Activity "Session", Note "Session ended", dan Status strip (`—`) tercatat di tabel

## Notes

- Global Settings memancarkan event siklus hidup sesinya sendiri ke tabel session_logs.
