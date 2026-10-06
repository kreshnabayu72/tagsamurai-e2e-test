---
id: TC-AC-ACAL-E2E-004-empty-state-filtered-no-results
title: "Tampilan empty state no results found saat pencarian tidak menemukan hasil pada kedua tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-10
  - TC-AC-ACAL-11
  - TC-AC-ACAL-44
  - TC-AC-ACAL-136
coverage:
  web: automated
---

# Tampilan empty state no results found saat pencarian tidak menemukan hasil pada kedua tab

## Prerequisites

- Login sebagai Role: Principal Total Control
- Data riwayat log tersedia di Tab Session dan Tab User Action

## Test Steps

### No Results State Tab Session

1. Buka menu `Admin Console > Activity Log`
2. Klik icon Search `[🔍]` pada toolbar Tab Session
3. Masukkan keyword `"zzznotfound"` lalu tekan Enter
4. Verifikasi area tabel menampilkan teks judul `"No results found"` dan subtitle `"Try adjusting your search or filter."`
5. Hapus keyword pencarian dan tekan Enter untuk mengembalikan data tabel

### No Results State Tab User Action

6. Klik tab `"User Action"`
7. Klik icon Search `[🔍]` pada toolbar Tab User Action
8. Masukkan keyword `"zzznotfound"` lalu tekan Enter
9. Verifikasi area tabel menampilkan teks judul `"No results found"` dan subtitle `"Try adjusting your search or filter."`
10. Hapus keyword pencarian dan tekan Enter untuk mengembalikan data tabel

## Notes

- Memastikan pembedaan visual dan pesan teks antara state genuinely empty vs state no results found (filtered).
