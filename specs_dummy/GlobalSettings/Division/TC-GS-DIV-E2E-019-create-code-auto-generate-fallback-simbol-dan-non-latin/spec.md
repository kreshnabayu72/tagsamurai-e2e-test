---
id: TC-GS-DIV-E2E-019-create-code-auto-generate-fallback-simbol-dan-non-latin
title: "Auto-Generate Code: Fallback 6 Karakter Kata Tunggal, Fallback DIV pada Karakter Simbolik/Non-Latin, dan Ketiadaan Live Preview"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-55
  - TC-GS-DIV-56
  - TC-GS-DIV-57
  - TC-GS-DIV-63
coverage:
  web: automated
---

# Auto-Generate Code: Fallback 6 Karakter Kata Tunggal, Fallback DIV pada Karakter Simbolik/Non-Latin, dan Ketiadaan Live Preview

## Prerequisites

- Login sebagai Role: Total Control
- Modal Create Division terbuka dengan field Code dikosongkan
- User berada di Global Settings > User > Division
- Code `DIV` sudah dipakai (TC-GS-DIV-56)

## Test Steps

### Auto-generate Code: kandidat kurang dari 2 karakter memakai 6 karakter alfanumerik pertama (TC-GS-DIV-55)

1. Klik `[+ Division]`
2. Isi Division Name `Research`
3. Biarkan Code kosong
4. Klik `[Submit]`
5. Lihat baris di tabel
6. Verifikasi Muncul toast sukses: `Success, division has been created.`
7. Verifikasi Tabel menampilkan Code `RESEAR`

### Auto-generate Code: Name tanpa huruf atau angka ASCII memakai DIV (TC-GS-DIV-56)

8. Klik `[+ Division]`
9. Isi Division Name `!!! ###`
10. Biarkan Code kosong
11. Klik `[Submit]`
12. Lihat baris di tabel
13. Verifikasi Muncul toast sukses: `Success, division has been created.`
14. Verifikasi Tabel menampilkan Code `DIV`

### Auto-generate Code: Name non-Latin memakai DIV lalu dedup suffix (TC-GS-DIV-57)

15. Klik `[+ Division]`
16. Isi Division Name `日本支店`
17. Biarkan Code kosong
18. Klik `[Submit]`
19. Lihat baris di tabel
20. Verifikasi Muncul toast sukses: `Success, division has been created.`
21. Verifikasi Tabel menampilkan Code `DIV2`

### Tidak ada live preview Code hasil auto-generate saat Code kosong (TC-GS-DIV-63)

22. Klik `[+ Division]`
23. Isi Division Name `Energy Management`
24. Perhatikan field Code
25. Verifikasi Field Code tetap kosong dengan placeholder `Enter code, or leave blank to auto-generate`
26. Verifikasi Tidak ada nilai Code yang terisi otomatis sebelum Submit

## Notes

- Memvalidasi algoritma F-DIV-09 langkah 4: fallback 6 karakter (Research -> RESEAR), fallback DIV saat nama hanya simbol (DIV) atau non-Latin, serta FI-03 tanpa live preview di form (PRD §4.4, §9.2).
- Sumber pemetaan test case granular: TC-GS-DIV-55, TC-GS-DIV-56, TC-GS-DIV-57, TC-GS-DIV-63.
