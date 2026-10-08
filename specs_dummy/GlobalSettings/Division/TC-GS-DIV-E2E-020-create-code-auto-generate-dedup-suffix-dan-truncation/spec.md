---
id: TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation
title: "Auto-Generate Code: Dedup Suffix Angka (2, 3, dst.), Truncation 15 Karakter pada 16 Token, dan Siklus Suffix Lanjutan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-58
  - TC-GS-DIV-59
  - TC-GS-DIV-60
  - TC-GS-DIV-61
  - TC-GS-DIV-62
coverage:
  web: automated
---

# Auto-Generate Code: Dedup Suffix Angka (2, 3, dst.), Truncation 15 Karakter pada 16 Token, dan Siklus Suffix Lanjutan

## Prerequisites

- Login sebagai Role: Total Control
- Divisi dengan Code HR dan HR2 sudah ada di entitas
- User berada di Global Settings > User > Division
- Code `HR` sudah dipakai Human Resources
- Code `HR` dan `HR2` sudah dipakai (TC-GS-DIV-58)
- Code `ABCDEFGHIJKLMNO` sudah dipakai (TC-GS-DIV-60)
- Division Pre-setup `Legal` dengan Code `LGL` sudah ada

## Test Steps

### Auto-generate Code: kandidat bentrok ditambah suffix angka 2 (TC-GS-DIV-58)

1. Klik `[+ Division]`
2. Isi Division Name `Hotel Reservation`
3. Biarkan Code kosong
4. Klik `[Submit]`
5. Lihat baris di tabel
6. Verifikasi Muncul toast sukses: `Success, division has been created.`
7. Verifikasi Tabel menampilkan Code `HR2`

### Auto-generate Code: suffix angka berlanjut ke 3 saat HR dan HR2 dipakai (TC-GS-DIV-59)

8. Klik `[+ Division]`
9. Isi Division Name `Hospital Records`
10. Biarkan Code kosong
11. Klik `[Submit]`
12. Lihat baris di tabel
13. Verifikasi Muncul toast sukses: `Success, division has been created.`
14. Verifikasi Tabel menampilkan Code `HR3`

### Auto-generate Code: kandidat dipotong maksimum 15 karakter (TC-GS-DIV-60)

15. Klik `[+ Division]`
16. Isi Division Name `A B C D E F G H I J K L M N O P`
17. Biarkan Code kosong
18. Klik `[Submit]`
19. Lihat baris di tabel
20. Verifikasi Muncul toast sukses: `Success, division has been created.`
21. Verifikasi Tabel menampilkan Code `ABCDEFGHIJKLMNO`

### Auto-generate Code: kandidat 15 karakter bentrok: basis dipotong agar total 15 karakter dengan suffix (TC-GS-DIV-61)

22. Klik `[+ Division]`
23. Isi Division Name `A B C D E F G H I J K L M N O Q`
24. Biarkan Code kosong
25. Klik `[Submit]`
26. Lihat baris di tabel
27. Verifikasi Muncul toast sukses: `Success, division has been created.`
28. Verifikasi Tabel menampilkan Code `ABCDEFGHIJKLMN2`

### Auto-generate Code dihitung unik tanpa membedakan huruf besar kecil (TC-GS-DIV-62)

29. Klik `[+ Division]`
30. Isi Division Name `Local Government Liaison`
31. Biarkan Code kosong
32. Klik `[Submit]`
33. Verifikasi Kandidat `LGL` bentrok dengan Code `LGL` yang sudah ada sehingga Code menjadi `LGL2`
34. Verifikasi Tabel menampilkan Code `LGL2`

## Notes

- Memvalidasi algoritma F-DIV-09 langkah 5-6: dedup suffix angka saat kandidat sudah dipakai (HR -> HR2, HR3), truncation ke maks 15 char pada 16 token, dan siklus dedup tak terbatas (PRD §9.2).
- Sumber pemetaan test case granular: TC-GS-DIV-58, TC-GS-DIV-59, TC-GS-DIV-60, TC-GS-DIV-61, TC-GS-DIV-62.
