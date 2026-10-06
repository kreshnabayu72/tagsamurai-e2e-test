---
id: TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel
title: "Pengujian Toolbar Detail Role: Siklus Search Box dan Filter Panel 6 Field Dinamis"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-73
  - TC-GS-ROLE-130
  - TC-GS-ROLE-139
  - TC-GS-ROLE-140
  - TC-GS-ROLE-141
  - TC-GS-ROLE-142
  - TC-GS-ROLE-143
  - TC-GS-ROLE-237
coverage:
  web: automated
---

# Pengujian Toolbar Detail Role: Siklus Search Box dan Filter Panel 6 Field Dinamis

## Prerequisites

- Login sebagai Role: Total Control
- Buka halaman Detail pada role 'Manage user and role'

## Test Steps

1. Buka Tab System > Detail role 'Manage user and role'
2. Klik icon Search pada toolbar Detail, ketik keyword nama user ter-assign, lalu tekan Enter
3. Verifikasi tabel Detail menyaring baris user yang cocok
4. Klik (✕) untuk menghapus teks, lalu tekan Enter pada input kosong untuk mereset tabel
5. Klik tombol Filter pada toolbar Detail
6. Verifikasi Filter Panel Detail memuat 6 field: Position, Division, Activation Status, Temporary User, Temporary Until, TAG
7. Terapkan filter Position dan Division secara terpisah dan verifikasi hasil tabel Detail
8. Terapkan filter Activation Status, Temporary User, Temporary Until, dan TAG secara bergantian
9. Verifikasi chip filter dirender dan dapat dihapus via icon (✕) maupun via uncheck di dropdown

## Notes

- Halaman Detail menyediakan 6 field penyaringan yang relevan dengan daftar user assignment (role.md §4.2).
