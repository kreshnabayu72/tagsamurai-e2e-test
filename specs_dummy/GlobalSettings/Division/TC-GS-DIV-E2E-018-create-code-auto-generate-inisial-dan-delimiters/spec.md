---
id: TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters
title: "Auto-Generate Code: Pemecahan Token Kata, Numerik, Alfanumerik Campuran, Delimiter Spasi/Tanda Hubung/Garis Bawah/Miring"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-50
  - TC-GS-DIV-51
  - TC-GS-DIV-52
  - TC-GS-DIV-53
  - TC-GS-DIV-54
coverage:
  web: automated
---

# Auto-Generate Code: Pemecahan Token Kata, Numerik, Alfanumerik Campuran, Delimiter Spasi/Tanda Hubung/Garis Bawah/Miring

## Prerequisites

- Login sebagai Role: Total Control
- Modal Create Division terbuka dengan field Code dikosongkan
- User berada di Global Settings > User > Division
- Code `CC` belum dipakai Division lain
- Code `CC` sudah dipakai (TC-GS-DIV-50)

## Test Steps

### Auto-generate Code: dua token alfabetik menjadi inisial (TC-GS-DIV-50)

1. Klik `[+ Division]`
2. Isi Division Name `Customer Care`
3. Biarkan Code kosong
4. Klik `[Submit]`
5. Lihat baris di tabel
6. Verifikasi Muncul toast sukses: `Success, division has been created.`
7. Verifikasi Tabel menampilkan Code `CC`

### Auto-generate Code: token numerik murni diteruskan utuh (TC-GS-DIV-51)

8. Klik `[+ Division]`
9. Isi Division Name `Region 5`
10. Biarkan Code kosong
11. Klik `[Submit]`
12. Lihat baris di tabel
13. Verifikasi Muncul toast sukses: `Success, division has been created.`
14. Verifikasi Tabel menampilkan Code `R5`

### Auto-generate Code: token numerik beberapa digit diteruskan utuh (TC-GS-DIV-52)

15. Klik `[+ Division]`
16. Isi Division Name `Branch 123`
17. Biarkan Code kosong
18. Klik `[Submit]`
19. Lihat baris di tabel
20. Verifikasi Muncul toast sukses: `Success, division has been created.`
21. Verifikasi Tabel menampilkan Code `B123`

### Auto-generate Code: token alfanumerik campuran hanya karakter pertama (TC-GS-DIV-53)

22. Klik `[+ Division]`
23. Isi Division Name `A1 Logistics`
24. Biarkan Code kosong
25. Klik `[Submit]`
26. Lihat baris di tabel
27. Verifikasi Muncul toast sukses: `Success, division has been created.`
28. Verifikasi Tabel menampilkan Code `AL`

### Auto-generate Code: pemisah hyphen, garis miring, dan underscore memecah token (TC-GS-DIV-54)

29. Klik `[+ Division]`
30. Isi Division Name `Customer-Care/Support_24`
31. Biarkan Code kosong
32. Klik `[Submit]`
33. Lihat baris di tabel
34. Verifikasi Muncul toast sukses: `Success, division has been created.`
35. Verifikasi Tabel menampilkan Code `CCS24`

## Notes

- Memvalidasi algoritma F-DIV-09 langkah 1-3: tokenisasi inisial (Customer Care -> CC, Region 5 -> R5, Branch 123 -> B123, A1 Logistics -> AL, Customer-Care/Support_24 -> CCS24) (PRD §9.2).
- Sumber pemetaan test case granular: TC-GS-DIV-50, TC-GS-DIV-51, TC-GS-DIV-52, TC-GS-DIV-53, TC-GS-DIV-54.
