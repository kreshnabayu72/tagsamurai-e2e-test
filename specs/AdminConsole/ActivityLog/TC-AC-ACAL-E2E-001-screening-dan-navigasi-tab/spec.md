---
id: TC-AC-ACAL-E2E-001-screening-dan-navigasi-tab
title: "Screening halaman Activity Log, breadcrumb, 2 tab, toolbar, dan navigasi tab independen"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-01
  - TC-AC-ACAL-02
  - TC-AC-ACAL-03
  - TC-AC-ACAL-20
  - TC-AC-ACAL-21
  - TC-AC-ACAL-22
  - TC-AC-ACAL-263
coverage:
  web: automated
---

# Screening halaman Activity Log, breadcrumb, 2 tab, toolbar, dan navigasi tab independen

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat data riwayat aktivitas pada Tab Session dan Tab User Action

## Test Steps

### Screening Tab Session

1. Buka sidebar menu `Admin Console > Activity Log`
2. Verifikasi breadcrumb menampilkan `"Activity Log"`
3. Verifikasi Tab bar menampilkan dua tab: `Session (aktif) | User Action`
4. Verifikasi Tab "Session" aktif secara default saat pertama kali masuk
5. Verifikasi toolbar sisi kanan memuat: `Search 🔖 | Filter | Download` tanpa tombol create
6. Verifikasi tabel Tab Session memuat 10 kolom: `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`, serta kolom `Actions (⋯)`
7. Verifikasi kolom Actions (⋯) tidak memiliki tombol row action per baris (read-only murni)

### Navigasi Tab & Independensi State

8. Masukkan keyword `"john"` di kotak Search Tab Session lalu tekan Enter
9. Verifikasi tabel Tab Session tersaring menampilkan entri dengan keyword `"john"`
10. Klik tab `"User Action"`
11. Verifikasi Tab "User Action" kini berstatus aktif
12. Verifikasi kotak Search di Tab User Action kosong (state pencarian tidak bocor antar tab)
13. Verifikasi tabel Tab User Action memuat 8 kolom: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`, serta kolom `Actions (⋯)`
14. Klik kembali tab `"Session"`
15. Verifikasi Tab "Session" aktif kembali dan keyword `"john"` masih aktif menyaring data di tabel

### Baris Non-Interaktif & Trigger Column Visibility

16. Klik pada area baris data di luar kolom Actions pada Tab Session
17. Verifikasi tidak ada navigasi halaman, dialog detail, atau aksi apa pun yang terpicu (baris purely informational)
18. Klik tab `"User Action"` dan lakukan klik pada area baris data
19. Verifikasi tidak ada navigasi atau modal detail yang terbuka
20. Klik header kolom `⋯` pada Tab User Action
21. Verifikasi dropdown `"Column Visibility"` terbuka tanpa opsi row action lainnya

## Notes

- Modul Activity Log adalah modul read-only murni tanpa operasi CRUD dan tanpa halaman detail per entri.
- Header kolom `⋯` berfungsi sebagai trigger Setup Column / Column Visibility.
