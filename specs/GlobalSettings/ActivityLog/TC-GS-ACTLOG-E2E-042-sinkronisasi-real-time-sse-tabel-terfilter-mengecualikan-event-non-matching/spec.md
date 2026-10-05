---
id: TC-GS-ACTLOG-E2E-042-sinkronisasi-real-time-sse-tabel-terfilter-mengecualikan-event-non-matching
title: "Sinkronisasi real-time SSE saat tabel terfilter mengecualikan event baru yang tidak cocok kriteria"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-75
  - TC-GS-ACTLOG-160
coverage:
  web: automated
---

# Sinkronisasi real-time SSE saat tabel terfilter mengecualikan event baru yang tidak cocok kriteria

## Prerequisites

- Login sebagai Role: Total Control dengan filter aktif pada Tab Session dan Tab User Action

## Test Steps

1. Buka Tab Session, terapkan filter Activity = "Login"
2. Simulasikan aktivitas baru Logout dilakukan oleh pengguna di sesi lain
3. Amati tabel Tab Session yang sedang terfilter
4. Verifikasi event Logout baru tidak muncul di tabel karena tidak cocok dengan kriteria filter aktif
5. Klik tab "User Action", terapkan filter Object = "Brand"
6. Simulasikan aktivitas baru di modul Measurement dilakukan di sesi lain
7. Amati tabel Tab User Action yang sedang terfilter
8. Verifikasi event mutasi Measurement tidak muncul di tabel karena tidak cocok dengan filter Brand

## Notes

- Event baru tetap diterima di background namun hanya di-render jika memenuhi kriteria filter aktif.
