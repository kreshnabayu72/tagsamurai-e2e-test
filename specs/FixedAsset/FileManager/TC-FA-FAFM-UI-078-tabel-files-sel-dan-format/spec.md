---
id: TC-FA-FAFM-UI-078-tabel-files-sel-dan-format
title: "Tabel Files: format sel, nilai kosong, dan teks sel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-01", "S-14", "EB-TBL-2@tabel-files", "EB-TBL-4@tabel-files", "EB-TBL-8@tabel-files", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-01": [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36, 38, 39, 40, 42, 43, 45, 46, 48, 50, 51, 53, 54, 56, 58, 59, 60]
  "S-14": [2, 3]
  "EB-TBL-2@tabel-files": [22, 23, 24]
  "EB-TBL-4@tabel-files": [10, 12, 27, 28, 30, 31, 33, 34, 36, 40, 42, 43, 45, 46]
  "EB-TBL-8@tabel-files": [25, 62, 63]
  "EB-XM-1": [13, 21]
anchor: []
coverage:
  web: automated
---

# Tabel Files: format sel, nilai kosong, dan teks sel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-078-1: `laptop-front.jpg`, JPG, Source Asset Photo, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi Santoso`, Upload Date `02/11/26 14:30`.
  - DU-078-2: `warranty-card-lpt0004.pdf`, PDF, Source Attachment, Reference `General`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `310.0 KB`, Uploaded By `Rina Anggraini`, Upload Date `28/10/26 09:00`.
  - DU-078-3: `lease-agreement-lpt0004.pdf`, PDF, Source Attachment, Reference tidak dikirim (null), Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `120.0 KB`, Uploaded By `Budi`, Upload Date `29/10/26 10:05`.
  - DU-078-4: `serial-label-lpt0004.pdf`, PDF, Source Attachment, Reference string kosong, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `88.0 KB`, Uploaded By `Dewi Anggraini`, Upload Date `30/10/26 11:10`.
  - DU-078-5: `serial-label-lpt0005.pdf`, PDF, Source Custom Field Document, Reference kosong karena custom field sumbernya sudah dihapus (null), Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `76.0 KB`, Uploaded By `Dewi Anggreni`, Upload Date `31/10/26 08:20`.
  - DU-078-6: `regional-procurement-and-vendor-management-office-jakarta-agreement.pdf`, PDF, Source Attachment, Reference `General`, Asset `Regional Procurement and Vendor Management Office Jakarta`, Asset ID `OFC-2026-0001`, Group `Head Office`, Size `450.2 KB`, Uploaded By `Buzzlightyear Sumardi`, Upload Date `06/11/26 10:00`.
  - DU-078-7: `rack-layout-svr0002.pdf`, PDF, Source Attachment, Reference `Purchase`, Asset `Server Dell R740 - 2`, Asset ID `SVR-2026-0002`, Group `Jakarta Barat Warehouse 1` (hierarki `Head Office > Jakarta Barat Warehouse 1`), Size `1.4 MB`, Uploaded By `Alexander Graham Bell`, Upload Date `07/11/26 13:20`.
  - DU-078-8: `rack-layout-svr0003.pdf`, PDF, Source Attachment, Reference `Purchase`, Asset `Server Dell R740 - 3`, Asset ID `SVR-2026-0003`, Group `Jakarta Barat Warehouse 12` yang tampil di badge sebagai `Jakarta Bara..Warehouse 12` (hierarki `Head Office > Jakarta Barat Warehouse 12`), Size `1.2 MB`, Uploaded By `Siti Nurbaya`, Upload Date `07/11/26 13:45`.
  - DU-078-9: `floor-plan-srv-room.pdf`, PDF, Source Attachment, Reference `General`, Asset `Rack Cabinet 42U - 1`, Asset ID `RCK-2026-0001`, Group `Server Room` (hierarki `Jakarta Office > Floor 2 > Server Room`), Size `2.1 MB`, Uploaded By `John Lennon`, Upload Date `08/11/26 09:10`.
  - DU-078-10: `handbook-lpt0009.pdf`, PDF, Source Attachment, Reference `General`, Asset `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Group `Head Office`, Size `95.0 KB`, Uploaded By `System`, Upload Date `09/11/26 02:00`.
  - DU-078-11: `site-survey-scans.pdf`, PDF, Source Attachment, Reference `General`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size tampil `1,536.0 GB`, Uploaded By `Rina Anggraini`, Upload Date `10/11/26 15:00`.
  - DU-078-12: `site-survey-photos.pdf`, PDF, Source Attachment, Reference `General`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, ukuran mentah sedikit di bawah 1,000.0 GB yang dibulatkan ke satu desimal menjadi `1,000.0 GB`, Uploaded By `Rina Anggraini`, Upload Date `10/11/26 15:10`.
  - DU-078-13: `loading-dock.jpeg`, JPEG, Source Asset Photo, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `1.1 MB`, Uploaded By `Rina Anggraini`, Upload Date `04/11/26 08:15`.
  - DU-078-14: `card-markup-lpt0004.pdf`, PDF, Source Custom Field Document, Reference `<b>Warranty Card</b>` (teks yang memuat markup), Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `64.0 KB`, Uploaded By `Rina Anggraini`, Upload Date `11/11/26 09:30`.
  - DU-078-15: `insurance-policy-lpt0004.pdf`, PDF, Source Attachment, Reference `Purchase`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `3.2 MB`, Uploaded By `Rina Anggraini`, Upload Date `12/11/26 14:00`.
  - DU-078-16: `<b>handover</b>-lpt0004.pdf` (nama file yang memuat markup), PDF, Source Attachment, Reference `General`, Asset `<i>Laptop Dell</i> - 4` (teks yang memuat markup), Asset ID `LPT-2026-0004`, Group `Head Office`, Size `45.0 KB`, Uploaded By `Rina Anggraini`, Upload Date `13/11/26 10:15`.
- Kondisi:
  - Semua kondisi: Date Format `dd/MM/yy` dan Time Format `HH:mm`; waktu unggah dikirim sebagai saat yang sama dengan jam yang ditulis pada data menurut Time Zone General Settings; kolom File Format dan Size pada data ditulis sebagai nilai tampil yang diharapkan, File Format diturunkan dari ekstensi nama file.
  - K1: tab `Asset Photo` aktif; tabel berisi DU-078-1 dan DU-078-13.
  - K2: tab `Asset Documents` aktif; tabel berisi DU-078-2, DU-078-3, DU-078-4, DU-078-5, dan DU-078-14.
  - K3: tab `Asset Documents` aktif; tabel berisi DU-078-6, DU-078-7, DU-078-8, DU-078-9, dan DU-078-10.
  - K4: tab `Asset Documents` aktif; tabel berisi DU-078-11, DU-078-12, dan DU-078-15.
  - K5: tab `Asset Documents` aktif; tabel berisi DU-078-16.

## Test Steps

### Format kolom pada tab Asset Photo
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi File Name `laptop-front.jpg` tampil sebagai tautan
3. Verifikasi File Name `laptop-front.jpg` dapat difokuskan dengan keyboard
4. Verifikasi File Format baris `laptop-front.jpg` tampil `JPG`
5. Verifikasi File Format baris `loading-dock.jpeg` tampil `JPEG`
6. Verifikasi Asset baris `laptop-front.jpg` tampil `Laptop Dell Latitude 5420 - 4`
7. Verifikasi Asset ID baris `laptop-front.jpg` tampil `LPT-2026-0004`
8. Verifikasi Group baris `laptop-front.jpg` tampil `Head Office`
9. Verifikasi Size baris `laptop-front.jpg` tampil `820.4 KB`
10. Verifikasi Uploaded By baris `laptop-front.jpg` tampil `Budi S`
11. Arahkan kursor ke Uploaded By baris `laptop-front.jpg`
12. Verifikasi teks `Budi Santoso` tersampaikan pada Uploaded By baris `laptop-front.jpg`
13. Verifikasi Upload Date baris `laptop-front.jpg` tampil `02/11/26 14:30`
14. Verifikasi tidak ada header kolom `Source` pada tabel
15. Verifikasi tidak ada header kolom `Reference` pada tabel

### Source, Reference, tanggal, dan nilai kosong pada tab Asset Documents
16. Tampilkan Tabel File Manager tab Files dengan kondisi K2
17. Verifikasi header kolom `Source` tampil
18. Verifikasi header kolom `Reference` tampil
19. Verifikasi Source baris `warranty-card-lpt0004.pdf` tampil `Attachment`
20. Verifikasi Reference baris `warranty-card-lpt0004.pdf` tampil `General`
21. Verifikasi Upload Date baris `warranty-card-lpt0004.pdf` tampil `28/10/26 09:00`
22. Verifikasi Reference baris `lease-agreement-lpt0004.pdf` tampil `—`
23. Verifikasi Reference baris `serial-label-lpt0004.pdf` tampil `—`
24. Verifikasi Reference baris `serial-label-lpt0005.pdf` tampil `—`
25. Verifikasi Reference baris `card-markup-lpt0004.pdf` tampil sebagai teks `<b>Warranty Card</b>` apa adanya

### Nama user pada Uploaded By
26. Tampilkan Tabel File Manager tab Files dengan kondisi K2
27. Verifikasi Uploaded By baris `warranty-card-lpt0004.pdf` tampil `Rina A`
28. Verifikasi Uploaded By baris `lease-agreement-lpt0004.pdf` tampil `Budi`
29. Arahkan kursor ke Uploaded By baris `lease-agreement-lpt0004.pdf`
30. Verifikasi teks `Budi` tersampaikan pada Uploaded By baris `lease-agreement-lpt0004.pdf`
31. Verifikasi Uploaded By baris `serial-label-lpt0004.pdf` tampil `Dewi A`
32. Arahkan kursor ke Uploaded By baris `serial-label-lpt0004.pdf`
33. Verifikasi teks `Dewi Anggraini` tersampaikan pada Uploaded By baris `serial-label-lpt0004.pdf`
34. Verifikasi Uploaded By baris `serial-label-lpt0005.pdf` tampil `Dewi A`
35. Arahkan kursor ke Uploaded By baris `serial-label-lpt0005.pdf`
36. Verifikasi teks `Dewi Anggreni` tersampaikan pada Uploaded By baris `serial-label-lpt0005.pdf`

### Teks panjang, nama panjang, dan aktor System
37. Tampilkan Tabel File Manager tab Files dengan kondisi K3
38. Verifikasi File Name `regional-procurement-and-vendor-management-office-jakarta-agreement.pdf` tampil utuh tanpa dipotong
39. Verifikasi Asset baris DU-078-6 tampil utuh `Regional Procurement and Vendor Management Office Jakarta`
40. Verifikasi Uploaded By baris DU-078-6 tampil `Buzzlightyear S`
41. Arahkan kursor ke Uploaded By baris DU-078-6
42. Verifikasi teks `Buzzlightyear Sumardi` tersampaikan pada Uploaded By baris DU-078-6
43. Verifikasi Uploaded By baris `rack-layout-svr0002.pdf` tampil `Alexander G`
44. Arahkan kursor ke Uploaded By baris `rack-layout-svr0002.pdf`
45. Verifikasi teks `Alexander Graham Bell` tersampaikan pada Uploaded By baris `rack-layout-svr0002.pdf`
46. Verifikasi Uploaded By baris `handbook-lpt0009.pdf` tampil `System`

### Badge Group: batas 25 karakter dan hierarki
47. Tampilkan Tabel File Manager tab Files dengan kondisi K3
48. Verifikasi Group baris `rack-layout-svr0002.pdf` tampil `Jakarta Barat Warehouse 1`
49. Arahkan kursor ke Group baris `rack-layout-svr0002.pdf`
50. Verifikasi teks `Head Office > Jakarta Barat Warehouse 1` tersampaikan pada Group baris `rack-layout-svr0002.pdf`
51. Verifikasi Group baris `rack-layout-svr0003.pdf` tampil `Jakarta Bara..Warehouse 12`
52. Arahkan kursor ke Group baris `rack-layout-svr0003.pdf`
53. Verifikasi teks `Head Office > Jakarta Barat Warehouse 12` tersampaikan pada Group baris `rack-layout-svr0003.pdf`
54. Verifikasi Group baris `floor-plan-srv-room.pdf` tampil `Server Room`
55. Arahkan kursor ke Group baris `floor-plan-srv-room.pdf`
56. Verifikasi teks `Jakarta Office > Floor 2 > Server Room` tersampaikan pada Group baris `floor-plan-srv-room.pdf`

### Format Size
57. Tampilkan Tabel File Manager tab Files dengan kondisi K4
58. Verifikasi Size baris `site-survey-scans.pdf` tampil `1,536.0 GB`
59. Verifikasi Size baris `site-survey-photos.pdf` tampil `1,000.0 GB`
60. Verifikasi Size baris `insurance-policy-lpt0004.pdf` tampil `3.2 MB`

### Markup pada File Name dan Asset tampil sebagai teks
61. Tampilkan Tabel File Manager tab Files dengan kondisi K5
62. Verifikasi File Name `<b>handover</b>-lpt0004.pdf` tampil sebagai teks apa adanya
63. Verifikasi Asset baris DU-078-16 tampil sebagai teks `<i>Laptop Dell</i> - 4` apa adanya
