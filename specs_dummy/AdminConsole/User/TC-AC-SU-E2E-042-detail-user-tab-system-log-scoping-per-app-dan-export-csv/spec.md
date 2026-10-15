---
id: TC-AC-SU-E2E-042-detail-user-tab-system-log-scoping-per-app-dan-export-csv
title: "Detail User Tab System Log: Log Aktivitas User Sebagai Aktor Lintas Aplikasi dan Export"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-134
  - TC-AC-SU-135
  - TC-AC-SU-137
  - TC-AC-SU-138
  - TC-AC-SU-139
  - TC-AC-SU-141
coverage:
  web: automated
---

# Detail User Tab System Log: Log Aktivitas User Sebagai Aktor Lintas Aplikasi dan Export

## Prerequisites

- Login sebagai Total Control
- Target user telah melakukan beberapa aktivitas di berbagai aplikasi TAG Samurai

## Test Steps

### Screening Tab System Log dan Identifikasi Aktor
1. Buka Detail User target > klik tab `System Log`
2. Verifikasi tabel memuat rekaman audit aktivitas di mana user ini bertindak sebagai pelaku/aktor
3. Verifikasi kolom memuat: `Timestamp`, `Application`, `Activity`, `Target Object`, `IP Address`

### Filter Scoping per Aplikasi dan Ekspor
4. Buka dropdown filter aplikasi pada toolbar
5. Pilih opsi aplikasi `"Admin Console"`
6. Verifikasi baris log tersaring hanya menampilkan aktivitas yang dilakukan di Admin Console
7. Klik tombol `[Download]` pada toolbar
8. Verifikasi berkas CSV System Log terunduh dengan data aktivitas yang sesuai filter

## Notes

Memvalidasi transparansi jejak aktivitas pengguna lintas sistem aplikasi.
