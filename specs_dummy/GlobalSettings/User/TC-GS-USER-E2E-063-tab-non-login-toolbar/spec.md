---
id: TC-GS-USER-E2E-063-tab-non-login-toolbar
title: 'Filter, Search, sort, Download, dan Setup Column di Tab Non-Login User'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-563
  - TC-GS-USER-564
  - TC-GS-USER-566
  - TC-GS-USER-567
coverage:
  web: automated
---

# Filter, Search, sort, Download, dan Setup Column di Tab Non-Login User

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User Login "Ahmad Fauzi" mewakili minimal tiga Non-Login berbeda nilai, termasuk "Rudi Hartono" (Employee ID `EMP-002`, Division `Finance`), "Sari Dewi" (Inactive, Employee ID kosong, Position kosong), dan satu Non-Login bertipe Temporary
- Spec ini tidak mengubah data selain preferensi kolom di browser

## Test Steps

### Search

1. Buka User Detail "Ahmad Fauzi" > Tab Non-Login User lalu cari `Rudi`, `EMP-002`, `Finance`, dan `Inactive`
2. Verifikasi keempat pencarian menemukan baris terkait
3. Cari teks tanggal dari kolom Last Update
4. Verifikasi tidak ada baris yang ditemukan

### Filter

5. Buka Filter dan verifikasi tujuh field: Position, Division, Active, Last Update, Temporary User, Temporary Until, dan Custom Field aktif, tanpa filter untuk Name, Email, dan Employee ID
6. Terapkan tiap field secara bergantian
7. Verifikasi tiap filter memfilter baris dengan benar

### Sort

8. Klik tiap header kolom (Name, Email, Employee ID, Position, Division, Active, Last Update) tiga kali
9. Verifikasi Name, Email, dan Division A-Z lalu Z-A, Employee ID dan Position A-Z dengan nilai kosong di akhir, Active urut Active First lalu Inactive First, Last Update urut terbaru dan terlama, dan klik ketiga kembali ke default Name A-Z

### Download dan Setup Column

10. Hide kolom `Position` lewat Column Visibility, lalu Download CSV
11. Verifikasi berkas hanya berisi baris tab ini dan kolom yang visible (tanpa `Position`)
12. Verifikasi Pin, Unpin, dan Hide berfungsi, dan pengaturan kolom tab ini terpisah dari User List Login User

## Notes

- Sumber `user.md` bagian 4.1, 4.2, 4.2a, serta `prd-conventions.md` bagian 9.3 dan 9.9.
- Tampilan dasar dan empty state tab ini dicakup `TC-GS-USER-E2E-062-tab-non-login-reverse-lookup`.
