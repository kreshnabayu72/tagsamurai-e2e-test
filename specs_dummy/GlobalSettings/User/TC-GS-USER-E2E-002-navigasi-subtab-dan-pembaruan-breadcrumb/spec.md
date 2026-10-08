---
id: TC-GS-USER-E2E-002-navigasi-subtab-dan-pembaruan-breadcrumb
title: "Navigasi sub-tab dan pembaruan breadcrumb antar tab User List, Position, Division, Custom Field"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-3
  - TC-GS-USER-4
  - TC-GS-USER-5
  - TC-GS-USER-6
coverage:
  web: automated
---

# Navigasi sub-tab dan pembaruan breadcrumb antar tab User List, Position, Division, Custom Field

## Prerequisites

- Login sebagai Role: Total Control
- Berada di halaman Global Settings > User

## Test Steps

### Navigasi Breadcrumb Antar Tab

1. Buka Global Settings > User tab User List
2. Klik tab 'Position', verifikasi breadcrumb berubah menjadi 'User > Position' dan tab Position aktif
3. Klik tab 'Division', verifikasi breadcrumb berubah menjadi 'User > Division' dan tab Division aktif
4. Klik tab 'Custom Field', verifikasi breadcrumb berubah menjadi 'User > Custom Field' dan tab Custom Field aktif
5. Kembali ke tab 'User List', verifikasi breadcrumb kembali menjadi 'User > User List'

### Persistensi State saat Berpindah Tab

6. Di sub-tab Login User, klik ikon Search dan masukkan kata kunci 'Dewi'
7. Klik header kolom Email untuk mengurutkan ascending
8. Pindah ke tab 'Position', lalu kembali lagi ke tab 'User List'
9. Verifikasi kata kunci pencarian 'Dewi' tetap terisi dan urutan sort Email ascending tetap aktif

## Notes

- Menggabungkan 4 test case granular (TC-GS-USER-3 s.d. TC-GS-USER-6).
