---
id: TC-GS-ROLE-E2E-019-detail-table-user-picker-assign-role-screening-dan-empty-states
title: "Screening Popup Table User Picker Assign Role ([+ Add User]), Counter Seleksi, dan Empty States"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-36
  - TC-GS-ROLE-331
coverage:
  web: automated
---

# Screening Popup Table User Picker Assign Role ([+ Add User]), Counter Seleksi, dan Empty States

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mock endpoint assignable-users list disiapkan untuk berbagai varian respons

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System > Detail role 'Manage master reference'
2. Klik tombol [+ Assign] (atau [+ Add User]) pada toolbar
3. Verifikasi popup Table User Picker terbuka dengan tabel multi-select
4. Centang 2 user pada tabel picker
5. Verifikasi teks counter seleksi muncul menampilkan "2 users selected"
6. Batalkan centang kedua user sehingga 0 user terpilih
7. Klik tombol [Assign] di bagian footer
8. Verifikasi alert inline berwarna merah muncul 4px di atas tombol footer dengan teks "You must pick a user"
9. Simulasikan respons di mana seluruh user eligible telah ter-assign ke role ini
10. Verifikasi ilustrasi kosong tampil dengan Title: "All eligible users have been assigned" dan Description: "There are no additional eligible users available to select."
11. Simulasikan respons pencarian yang tidak menghasilkan kecocokan
12. Verifikasi ilustrasi kosong tampil dengan Title: "No results found" dan Description: "Try adjusting your search or filter."

## Notes

- Table User Picker memiliki 2 varian empty state resmi: seluruh user ter-assign vs pencarian tanpa hasil (role.md §7.1).
