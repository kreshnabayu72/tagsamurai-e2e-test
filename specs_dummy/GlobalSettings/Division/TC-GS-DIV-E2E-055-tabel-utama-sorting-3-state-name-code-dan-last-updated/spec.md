---
id: TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated
title: "Sorting 3-State Kolom Tabel Utama: Siklus Ascending, Descending, Default pada Name, Code, dan Last Updated, Serta Reset Halaman ke 1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-158
  - TC-GS-DIV-159
  - TC-GS-DIV-160
  - TC-GS-DIV-161
  - TC-GS-DIV-162
coverage:
  web: automated
---

# Sorting 3-State Kolom Tabel Utama: Siklus Ascending, Descending, Default pada Name, Code, dan Last Updated, Serta Reset Halaman ke 1

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi data
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Ganti kolom sort saat Search dan Filter aktif tidak mereset saringan (TC-GS-DIV-158)

1. Cari `a` lalu Enter dan terapkan Filter
2. Klik header Name
3. Klik header Code
4. Verifikasi Sort berpindah ke kolom Code (ascending) dan ikon sort Name kembali netral
5. Verifikasi Search dan Filter tetap aktif

### Empty state hasil kombinasi pulih saat salah satu saringan dilepas (TC-GS-DIV-159)

6. Cari `a` lalu Enter
7. Terapkan Filter rentang 1 Jan 2020 sampai 31 Jan 2020 sehingga hasil kosong
8. Buka Filter, klik `[Clear Field]` dan `[Apply]`
9. Verifikasi Saat kosong tampil `No results found` dan `Try adjusting your search or filter.`
10. Verifikasi Setelah filter dilepas tabel pulih menampilkan hasil search `a`

### Seleksi checkbox bertahan saat Search dikosongkan (TC-GS-DIV-160)

11. Cari `Accounting` lalu Enter
12. Centang baris `Accounting`
13. Kosongkan Search dengan `(✕)` lalu Enter
14. Verifikasi Baris `Accounting` tetap tercentang dan counter `1 Division selected` tetap tampil

### Division baru yang tidak cocok dengan Search aktif tidak muncul (TC-GS-DIV-161)

15. Cari `Accounting` lalu Enter
16. Buat Division `Tax Compliance` (Code `TAX`) lewat `[+ Division]`
17. Verifikasi Toast sukses `Success, division has been created.`
18. Verifikasi Baris `Tax Compliance` tidak tampil karena tidak cocok dengan keyword
19. Verifikasi Setelah Search dikosongkan baris `Tax Compliance` tampil

### Edit Name yang membuat Division tidak lagi cocok dengan Search aktif menghilangkannya dari tabel (TC-GS-DIV-162)

20. Cari `Customer` lalu Enter
21. Edit baris `Customer Service` dan ubah Name menjadi `Client Care`
22. Klik `[Save]`
23. Verifikasi Toast sukses `Success, division has been updated.`
24. Verifikasi Baris `Client Care` hilang dari tabel karena tidak lagi cocok dengan keyword `Customer`
25. Verifikasi Baris `Customer Care` tetap tampil

## Notes

- Memvalidasi siklus klik 3-state: Ascending -> Descending -> Default (Name A-Z), dukungan sort pada kolom Code (NC-07), Last Updated (Newest/Oldest), dan reset navigasi ke halaman 1 (PRD §4.1.1, §5, prd-conventions.md §9.7).
- Sumber pemetaan test case granular: TC-GS-DIV-158, TC-GS-DIV-159, TC-GS-DIV-160, TC-GS-DIV-161, TC-GS-DIV-162.
