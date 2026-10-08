---
id: TC-AC-SU-E2E-008-user-list-sorting-3-state-dan-guard-kolom-non-sortable
title: "Sorting 3-state pada 12 kolom sortable User List, transisi header sort, dan guard kolom non-sortable"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-19
  - TC-AC-SU-274
  - TC-AC-SU-275
  - TC-AC-SU-276
coverage:
  web: automated
---

# Sorting 3-state pada 12 kolom sortable User List, transisi header sort, dan guard kolom non-sortable

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat dataset pengguna dengan data variatif pada ke-12 kolom sortable
- Kolom non-sortable (TAG dan Custom Field) dalam keadaan ditampilkan

## Test Steps

### Verifikasi Default Sort
1. Buka halaman `Settings > User`
2. Verifikasi default sorting tabel adalah kolom `Name` ascending (A-Z)

### Siklus 3-State Sorting (Ascending -> Descending -> Netral)
3. Klik header kolom `Name`
4. Verifikasi arah panah berubah menjadi Descending (Z-A) dan urutan tabel terbalik
5. Klik header kolom `Name` sekali lagi
6. Verifikasi kolom kembali ke status netral (default sort Name A-Z)
7. Ulangi siklus 3 kali klik untuk kolom teks lain: `Email`, `Position`, `Division`, `Employee ID`, `Modified By`
8. Verifikasi pengurutan teks mengikuti kolasi alfabetis en-US
9. Ulangi siklus 3 kali klik pada kolom tanggal: `Last Updated` dan `Temporary Until`
10. Verifikasi pengurutan beralih antara Oldest First dan Newest First
11. Ulangi siklus pada kolom switch `Active`
12. Verifikasi pengurutan beralih antara Active First dan Inactive First

### Transisi Header Sort Saat Filter Aktif & Guard Kolom Non-Sortable
13. Terapkan saringan pencarian nama pada toolbar
14. Klik header kolom `Position` untuk mengurutkan berdasarkan jabatan
15. Verifikasi pengurutan beralih ke kolom Position TANPA mereset keyword pencarian toolbar
16. Arahkan kursor ke header kolom `TAG` dan kolom `Custom Field`
17. Verifikasi tidak ada indikator panah sort pada kedua header kolom tersebut
18. Klik header kolom `TAG` dan `Custom Field`
19. Verifikasi klik tidak memicu pengurutan apa pun dan urutan baris tabel tidak berubah

## Notes

- Seluruh 12 kolom sortable mendukung siklus penuh 3-state (Asc -> Desc -> Default).
