---
id: TC-AC-ACAL-E2E-024-tab-user-action-search-per-kolom
title: "Tab User Action — Search toolbar per kolom untuk seluruh field teks"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-128
  - TC-AC-ACAL-129
  - TC-AC-ACAL-130
  - TC-AC-ACAL-131
  - TC-AC-ACAL-132
  - TC-AC-ACAL-133
  - TC-AC-ACAL-134
  - TC-AC-ACAL-135
coverage:
  web: automated
---

# Tab User Action — Search toolbar per kolom untuk seluruh field teks

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data aktivitas write dengan beragam Action (Create, Edit, Delete, Reassign), Object (Client, Partner, Distributor, User), Name, Field, Old Value, New Value, dan Modified By

## Test Steps

### Screening Search Toolbar Tab User Action

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Klik icon Search `[🔍]` pada toolbar
3. Verifikasi input search reveal dengan placeholder `"Search by action, name, field, or value..."`

### Search per Kolom yang Didukung

4. Masukkan substring Action (contoh: `"reassign"`) lalu tekan Enter
5. Verifikasi baris dengan Action `"Reassign"` tampil (case-insensitive)
6. Masukkan substring Object (contoh: `"partner"`) lalu tekan Enter
7. Verifikasi baris dengan Object Partner tampil
8. Masukkan substring Name (contoh nama entitas / pengguna) lalu tekan Enter
9. Verifikasi baris dengan Name terkait tampil
10. Masukkan substring Field (contoh: `"email"`) lalu tekan Enter
11. Verifikasi baris dengan Field email tampil
12. Masukkan substring Old Value lalu tekan Enter
13. Verifikasi baris dengan Old Value terkait tampil
14. Masukkan substring New Value lalu tekan Enter
15. Verifikasi baris dengan New Value terkait tampil
16. Masukkan substring nama Modified By lalu tekan Enter
17. Verifikasi baris yang dimodifikasi oleh nama tersebut tampil

## Notes

- Memverifikasi pencarian multi-kolom yang didukung oleh backend pada Tab User Action.
