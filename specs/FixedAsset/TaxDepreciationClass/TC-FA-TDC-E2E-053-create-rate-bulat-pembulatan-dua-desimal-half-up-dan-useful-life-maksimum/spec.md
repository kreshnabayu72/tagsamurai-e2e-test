---
id: TC-FA-TDC-E2E-053-create-rate-bulat-pembulatan-dua-desimal-half-up-dan-useful-life-maksimum
title: "Create - Rate Bulat, Pembulatan Dua Desimal Half-up, dan Useful Life Maksimum"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-168
  - TC-FA-TDC-169
  - TC-FA-TDC-170
  - TC-FA-TDC-172
sourceRules: ["FATDC-LOGIC-03f.1", "FATDC-LOGIC-03f.2"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-03f.1": [4, 7, 10, 13, 17, 20, 23, 26, 29, 32]
  "FATDC-LOGIC-03f.2": [5, 8, 11, 14, 18, 21, 24, 27, 30, 33]
anchor: [15]
coverage:
  web: automated
---

# Create - Rate Bulat, Pembulatan Dua Desimal Half-up, dan Useful Life Maksimum

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: tujuh class seed bawaan (`Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE) dalam keadaan belum diubah. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (tidak ada Submit). Asset Type `Non-building`; Allowed Methods `Straight Line` dan `Declining Balance`. Tabel Useful Life dan rate yang diharapkan (Drawer menulis rate tanpa simbol `%`):

| Useful Life | Straight Line Rate (%) | Declining Balance Rate (%) |
|---|---|---|
| 4 | 25 | 50 |
| 8 | 12.5 | 25 |
| 16 | 6.25 | 12.5 |
| 20 | 5 | 10 |
| 3 | 33.33 | 66.67 |
| 6 | 16.67 | 33.33 |
| 7 | 14.29 | 28.57 |
| 32 | 3.13 | 6.25 |
| 64 | 1.56 | 3.13 |
| 100 | 1 | 2 |

- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-168: Create - rate dihitung dari Useful Life yang menghasilkan nilai bulat (4, 8, 16, 20)

1. Klik `+ Class` di toolbar
2. Pilih Asset Type `Non-building` dan Allowed Methods `Straight Line` dan `Declining Balance`
3. Isi Useful Life `4` dan amati kedua rate
4. Verifikasi Straight Line Rate (%) "25" (Useful Life `4`)
5. Verifikasi Declining Balance Rate (%) "50" (Useful Life `4`)
6. Isi Useful Life `8` dan amati kedua rate
7. Verifikasi Straight Line Rate (%) "12.5" (Useful Life `8`)
8. Verifikasi Declining Balance Rate (%) "25" (Useful Life `8`)
9. Isi Useful Life `16` dan amati kedua rate
10. Verifikasi Straight Line Rate (%) "6.25" (Useful Life `16`)
11. Verifikasi Declining Balance Rate (%) "12.5" (Useful Life `16`)
12. Isi Useful Life `20` dan amati kedua rate
13. Verifikasi Straight Line Rate (%) "5" (Useful Life `20`)
14. Verifikasi Declining Balance Rate (%) "10" (Useful Life `20`)
15. Verifikasi nilai pada field read-only Straight Line Rate (%) dan Declining Balance Rate (%) di Drawer ditulis tanpa simbol `%` karena label field memuat `(%)`

### TC-FA-TDC-169: Create - rate dibulatkan ke 2 desimal (Useful Life 3, 6, 7)

16. Isi Useful Life `3` dan amati kedua rate
17. Verifikasi Straight Line Rate (%) "33.33" (Useful Life `3`)
18. Verifikasi Declining Balance Rate (%) "66.67" (Useful Life `3`; 2 × 33.333… dibulatkan, bukan 2 × 33.33)
19. Isi Useful Life `6` dan amati kedua rate
20. Verifikasi Straight Line Rate (%) "16.67" (Useful Life `6`)
21. Verifikasi Declining Balance Rate (%) "33.33" (Useful Life `6`)
22. Isi Useful Life `7` dan amati kedua rate
23. Verifikasi Straight Line Rate (%) "14.29" (Useful Life `7`)
24. Verifikasi Declining Balance Rate (%) "28.57" (Useful Life `7`)

### TC-FA-TDC-170: Create - pembulatan half-up pada nilai tepat di tengah (Useful Life 32 dan 64)

25. Isi Useful Life `32` dan amati kedua rate
26. Verifikasi Straight Line Rate (%) "3.13" (Useful Life `32`; nilai tepat di tengah dibulatkan ke atas)
27. Verifikasi Declining Balance Rate (%) "6.25" (Useful Life `32`)
28. Isi Useful Life `64` dan amati kedua rate
29. Verifikasi Straight Line Rate (%) "1.56" (Useful Life `64`)
30. Verifikasi Declining Balance Rate (%) "3.13" (Useful Life `64`; nilai tepat di tengah dibulatkan ke atas)

### TC-FA-TDC-172: Create - rate pada Useful Life maksimum 100

31. Isi Useful Life `100` dan amati kedua rate
32. Verifikasi Straight Line Rate (%) "1" (Useful Life `100`)
33. Verifikasi Declining Balance Rate (%) "2" (Useful Life `100`)
34. Klik `[Clear Field]`
35. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 3, 6, 9, 12, 16, 19, 22, 25, 28, dan 31 mengganti isi Useful Life yang sudah berisi dengan nilai baru ("Isi Useful Life ... dan amati kedua rate" menyalin LK TC); langkah 34 (`[Clear Field]`; S-09), langkah 35 (menutup Drawer yang bersih).
- Expected c TC-FA-TDC-170 ("pembulatan 2 desimal memakai half-up") adalah kesimpulan dari nilai pada langkah 26 sampai 30 dan tidak teramati terpisah, sehingga diasersi lewat nilai-nilai itu (S-03). Expected e TC-FA-TDC-168 diasersi pada langkah 15.
- Pembagian TC lintas spec: tampilan rate mengikuti metode (TC-FA-TDC-165 sampai 167) dan batas 100 (TC-FA-TDC-171) ada di spec `TC-FA-TDC-E2E-052-create-rate-tampil-mengikuti-metode-read-only-dan-batas-seratus`.
- Temuan untuk QA:
  - Hasil rate tabel di atas diturunkan dari Expected TC (TC-FA-TDC-168 sampai 170 dan 172); tidak ada sumber lain.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
