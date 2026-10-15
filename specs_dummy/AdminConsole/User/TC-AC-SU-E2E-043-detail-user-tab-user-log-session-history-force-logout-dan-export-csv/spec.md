---
id: TC-AC-SU-E2E-043-detail-user-tab-user-log-session-history-force-logout-dan-export-csv
title: "Detail User Tab User Log: Riwayat Sesi Login, Event Force Logout, dan Export CSV"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-240
  - TC-AC-SU-241
  - TC-AC-SU-242
  - TC-AC-SU-244
  - TC-AC-SU-245
  - TC-AC-SU-246
coverage:
  web: automated
---

# Detail User Tab User Log: Riwayat Sesi Login, Event Force Logout, dan Export CSV

## Prerequisites

- Login sebagai Total Control
- Target user memiliki riwayat sesi login, logout, dan force-logout

## Test Steps

### Screening Struktur Kolom Tab User Log
1. Buka Detail User target > klik tab `User Log`
2. Verifikasi tabel memuat 6 kolom baku: `Session ID`, `Login Time`, `Logout Time`, `IP Address`, `Device / Browser`, `Status / Terminated Reason`

### Verifikasi Event Force Logout dan Filter
3. Temukan baris sesi yang dihentikan paksa oleh administrator
4. Verifikasi teks pada kolom Terminated Reason menampilkan alasan jelas: `"Force Logout by Administrator"` atau `"Account Deactivated"`
5. Buka panel filter tanggal untuk menyaring riwayat sesi pada kurun waktu tertentu
6. Klik tombol `[Download]` untuk mengekspor histori sesi ke dalam format CSV

## Notes

Memastikan visibilitas sesi login dan riwayat penghentian akses pengguna.
