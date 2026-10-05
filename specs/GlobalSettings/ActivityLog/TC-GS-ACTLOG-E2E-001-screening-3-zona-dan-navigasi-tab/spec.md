---
id: TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab
title: "Screening 3 Zona, navigasi tab Session dan User Action, serta perilaku baris non-interaktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-01
  - TC-GS-ACTLOG-02
  - TC-GS-ACTLOG-03
  - TC-GS-ACTLOG-240
coverage:
  web: automated
---

# Screening 3 Zona, navigasi tab Session dan User Action, serta perilaku baris non-interaktif

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Terdapat entri riwayat aktivitas pada Tab Session dan Tab User Action

## Test Steps

### Screening Tab Session

1. Buka menu `Global Settings > Activity Log`
2. Verifikasi Tab "Session" aktif secara default
3. Verifikasi Header: breadcrumb "Activity Log" statis dan tidak berubah saat berganti tab
4. Verifikasi Tab bar menampilkan dua tab: `Session (aktif) | User Action`
5. Verifikasi Table Tools di sisi kanan memuat: `Search 🔖 | Filter | Download` tanpa tombol create
6. Verifikasi Body tabel memuat 10 kolom sortable: `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`, serta kolom `Actions (⋯)` unsortable
7. Verifikasi kolom Actions (⋯) tidak memiliki tombol row action per baris (read-only murni)
8. Verifikasi Footer tabel menampilkan pagination dengan default 10 per halaman, dan opsi page size 10/25/50/100

### Navigasi Tab & Independensi State

9. Masukkan keyword "John" di kotak pencarian Search Toolbar Tab Session lalu tekan Enter
10. Verifikasi tabel Tab Session tersaring menampilkan entri dengan keyword "John"
11. Klik tab "User Action"
12. Verifikasi Tab "User Action" kini berstatus aktif
13. Verifikasi kotak pencarian Search Toolbar di Tab User Action kosong (state pencarian tidak bocor antar tab)
14. Verifikasi Body tabel Tab User Action memuat 8 kolom sortable: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`, serta kolom `Actions (⋯)` unsortable
15. Klik kembali tab "Session"
16. Verifikasi Tab "Session" aktif kembali dan keyword "John" masih aktif menyaring data di tabel

### Baris Non-Interaktif

17. Klik pada area baris data di luar kolom Actions pada Tab Session
18. Verifikasi tidak ada navigasi halaman, dialog detail, atau aksi apa pun yang terpicu (baris purely informational)
19. Klik tab "User Action" dan lakukan klik pada area baris data
20. Verifikasi tidak ada navigasi atau modal detail yang terbuka

## Notes

- Activity Log adalah modul read-only murni tanpa operasi CRUD dan tanpa halaman detail per entri.
- Kolom Actions (⋯) hanya berfungsi sebagai trigger Setup Column saat header diklik; sel baris kosong.
