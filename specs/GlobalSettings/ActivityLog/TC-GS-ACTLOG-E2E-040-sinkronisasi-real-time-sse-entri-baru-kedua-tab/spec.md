---
id: TC-GS-ACTLOG-E2E-040-sinkronisasi-real-time-sse-entri-baru-kedua-tab
title: "Sinkronisasi real-time SSE: Entri baru di Tab Session dan Tab User Action muncul otomatis tanpa reload"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-224
  - TC-GS-ACTLOG-225
coverage:
  web: automated
---

# Sinkronisasi real-time SSE: Entri baru di Tab Session dan Tab User Action muncul otomatis tanpa reload

## Prerequisites

- Login sebagai Role: Total Control
- Tab Session dan Tab User Action terbuka di browser saat mutasi data berlangsung di latar belakang

## Test Steps

1. Buka Tab Session di browser
2. Simulasikan login baru dilakukan oleh user lain di tab/sesi berbeda
3. Amati tabel Tab Session tanpa melakukan reload manual
4. Verifikasi entri Login baru muncul otomatis di baris teratas via SSE auto-refresh
5. Klik tab "User Action"
6. Simulasikan pembuatan data Brand baru dilakukan oleh admin lain di modul Brand
7. Amati tabel Tab User Action tanpa melakukan reload manual
8. Verifikasi entri changelog Create Brand baru muncul otomatis di baris teratas via SSE

## Notes

- Server-Sent Events (SSE) memperbarui baris teratas tabel secara silent tanpa prompt konfirmasi reload.
