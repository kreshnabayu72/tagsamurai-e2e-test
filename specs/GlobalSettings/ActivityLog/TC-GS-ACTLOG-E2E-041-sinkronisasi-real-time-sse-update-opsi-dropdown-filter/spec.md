---
id: TC-GS-ACTLOG-E2E-041-sinkronisasi-real-time-sse-update-opsi-dropdown-filter
title: "Sinkronisasi real-time SSE: Opsi dropdown Filter Panel terupdate otomatis saat entitas baru tercatat"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-55
  - TC-GS-ACTLOG-141
coverage:
  web: automated
---

# Sinkronisasi real-time SSE: Opsi dropdown Filter Panel terupdate otomatis saat entitas baru tercatat

## Prerequisites

- Login sebagai Role: Total Control
- Dropdown filter sedang terbuka saat entri baru masuk via SSE

## Test Steps

1. Buka Filter Panel Tab Session lalu buka dropdown User
2. Simulasikan pengguna baru yang belum pernah ada di log melakukan login di tab lain
3. Amati daftar opsi dropdown User tanpa reload halaman
4. Verifikasi nama pengguna baru langsung muncul dalam daftar opsi dropdown
5. Klik tab "User Action", buka Filter Panel lalu buka dropdown Action
6. Simulasikan aksi baru (mis. Combine di TAG Registry) tercatat untuk pertama kalinya
7. Amati daftar opsi dropdown Action tanpa reload halaman
8. Verifikasi opsi "Combine" langsung muncul dalam daftar opsi dropdown Action

## Notes

- Opsi filter dinamis terikat langsung dengan data distinct di backend via SSE.
