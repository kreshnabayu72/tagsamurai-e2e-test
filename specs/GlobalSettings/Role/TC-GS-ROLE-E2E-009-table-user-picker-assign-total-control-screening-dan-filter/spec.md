---
id: TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter
title: "Screening Popup Table User Picker Assign Total Control, Pencarian, Filter Kelayakan, dan Validasi Nol Pilihan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-15
  - TC-GS-ROLE-18
  - TC-GS-ROLE-19
  - TC-GS-ROLE-20
  - TC-GS-ROLE-313
coverage:
  web: automated
---

# Screening Popup Table User Picker Assign Total Control, Pencarian, Filter Kelayakan, dan Validasi Nol Pilihan

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user eligible (aktif dan pending activation dengan akses GS=true)
- Tersedia user yang sedang Read Only
- Tersedia user tanpa akses Global Settings
- Tersedia user berstatus Inactive

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik tombol [+ Assign] pada toolbar
3. Verifikasi popup modal Table User Picker terbuka dengan judul dan tabel multi-select
4. Verifikasi kolom tabel picker memuat: Checkbox (Select All di header), Name, Email, Position, Division, Status
5. Verifikasi user yang sedang berstatus Read Only tidak muncul di daftar pilihan picker
6. Verifikasi user tanpa hak akses Global Settings tidak muncul di daftar pilihan picker
7. Verifikasi user dengan status Inactive tidak muncul di daftar pilihan picker
8. Verifikasi user dengan status Pending Activation dan akses GS=true muncul di daftar pilihan picker
9. Ketik keyword nama user pada Search box picker dan tekan Enter
10. Verifikasi tabel picker memfilter hasil secara akurat berdasarkan keyword nama atau email
11. Pastikan tidak ada checkbox baris user yang tercentang (0 user terpilih)
12. Klik tombol [Assign] di bagian footer popup modal
13. Verifikasi alert inline berwarna merah muncul 4px di atas tombol footer dengan teks "You must pick a user"
14. Verifikasi popup tetap terbuka dan tidak ada data yang ter-assign
15. Klik tombol silang (✕) pada header modal untuk menutup popup picker

## Notes

- Tombol [Assign] selalu enabled dan validasi 0-user menampilkan alert text inline rata kanan di atas tombol (role.md §4.2, §6).
