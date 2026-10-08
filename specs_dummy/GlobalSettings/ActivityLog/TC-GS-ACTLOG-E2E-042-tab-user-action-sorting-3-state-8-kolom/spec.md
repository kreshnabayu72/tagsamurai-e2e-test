---
id: TC-GS-ACTLOG-E2E-042-tab-user-action-sorting-3-state-8-kolom
title: "Tab User Action: Sorting 3-State untuk 8 Kolom, Kolom Campuran Angka-Teks, dan Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-175
  - TC-GS-ACTLOG-176
  - TC-GS-ACTLOG-177
  - TC-GS-ACTLOG-178
  - TC-GS-ACTLOG-179
coverage:
  web: automated
---

# Tab User Action: Sorting 3-State untuk 8 Kolom, Kolom Campuran Angka-Teks, dan Nilai Kosong

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log User Action dengan variasi data teks, angka, dan nilai kosong

## Test Steps

### Siklus Sort 3-State Kolom Date
1. Buka Tab User Action, klik header kolom Date sekali: indikator (↑) aktif (Oldest First).
2. Klik header Date kedua kali: indikator (↓) aktif (Newest First).
3. Klik header Date ketiga kali: indikator nonaktif, kembali ke urutan default.
### Sort Kolom Teks & Nilai Kosong
4. Uji sort 3 klik pada kolom Action dan Object: verifikasi urutan alfabetis A-Z dan Z-A.
5. Uji sort kolom Name dan Field yang memiliki baris kosong ('—').
6. Verifikasi saat Ascending (↑), nilai terisi urut A-Z dan baris '—' ditaruh di paling bawah.
7. Verifikasi saat Descending (↓), baris '—' ditaruh di paling atas dan nilai terisi urut Z-A.
### Sort Kolom Campuran Angka dan Teks (Old/New Value)
8. Uji sort pada kolom Old Value dan New Value dengan data campuran angka (2, 5, 10), teks (Finance, Marketing), dan kosong ('—').
9. Verifikasi saat Ascending (↑): angka terurut natural terlebih dahulu (2, 5, 10), lalu teks alfabetis (Finance, Marketing), dan baris '—' di paling bawah.
10. Verifikasi saat Descending (↓): baris '—' di paling atas, lalu teks Z-A, lalu angka menurun.
### Sort Kolom Modified By
11. Uji sort kolom Modified By, verifikasi pengurutan mengikuti nama lengkap admin (bukan nama singkat).

## Notes

- Pengurutan kolom campuran tipe data mematuhi prd-conventions.md §9.7: angka natural di depan teks.
