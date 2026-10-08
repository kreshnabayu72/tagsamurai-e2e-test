---
id: TC-AC-ACAL-E2E-010-tab-session-search-per-kolom-dan-guard-date
title: "Tab Session — Search toolbar per kolom dan guard kolom Date yang tidak tercakup search text"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-33
  - TC-AC-ACAL-34
  - TC-AC-ACAL-35
  - TC-AC-ACAL-36
  - TC-AC-ACAL-37
  - TC-AC-ACAL-38
  - TC-AC-ACAL-39
  - TC-AC-ACAL-40
  - TC-AC-ACAL-41
  - TC-AC-ACAL-42
  - TC-AC-ACAL-43
coverage:
  web: automated
---

# Tab Session — Search toolbar per kolom dan guard kolom Date yang tidak tercakup search text

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data dengan variasi nama User, Employee ID, Position, Division, IP Address, dan Device/Browser

## Test Steps

### Screening Search Toolbar

1. Buka menu `Admin Console > Activity Log` (Tab Session aktif)
2. Klik icon Search `[🔍]` pada toolbar
3. Verifikasi input search reveal dengan auto-focus, placeholder `"Search by user, employee ID, IP address, or device..."`, dan tooltip `🔖 Search`

### Search per Kolom yang Didukung

4. Masukkan substring nama User (contoh: `"john"`) lalu tekan Enter
5. Verifikasi baris dengan User yang memuat `"john"` tampil (case-insensitive)
6. Masukkan substring Employee ID lalu tekan Enter
7. Verifikasi baris yang cocok tampil
8. Masukkan substring Position (contoh: `"manager"`) lalu tekan Enter
9. Verifikasi baris Position cocok tampil
10. Masukkan substring Division (contoh: `"finance"`) lalu tekan Enter
11. Verifikasi baris Division cocok tampil
12. Masukkan keyword Note (contoh: `"started"`) lalu tekan Enter
13. Verifikasi hanya baris dengan Note `"Session started"` yang tampil
14. Masukkan substring IP Address (contoh: `"192.168"`) lalu tekan Enter
15. Verifikasi baris IP Address cocok tampil
16. Masukkan keyword Device/Browser (contoh: `"chrome"`) lalu tekan Enter
17. Verifikasi baris dengan Browser Chrome tampil

### Guard Kolom Date

18. Masukkan string tanggal (contoh: `"14 Jul 2026"`) pada kotak Search lalu tekan Enter
19. Verifikasi tidak ada pencarian berdasarkan tanggal lewat kotak teks search (hasil tidak menyaring berdasarkan tanggal atau tampil `"No results found"`)

## Notes

- Penyaringan berdasarkan tanggal harus dilakukan melalui Filter Panel (Date Picker), bukan melalui kotak Search toolbar.
