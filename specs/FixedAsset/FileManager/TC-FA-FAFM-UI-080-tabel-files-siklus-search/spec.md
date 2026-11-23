---
id: TC-FA-FAFM-UI-080-tabel-files-siklus-search
title: "Tabel Files: siklus kotak Search"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TBL-03b", "§4.4#b6", "EB-SRC-4@tabel-files"]
smoke: []
dependsOn: []
trace:
  "TBL-03b": [11, 12, 13, 15, 16, 17]
  "§4.4#b6": [7, 11, 12, 13, 15, 16, 17]
  "EB-SRC-4@tabel-files": [2, 3, 5, 6, 11, 12, 13, 15, 16, 17, 18, 23, 24, 26, 27, 28, 30, 31, 32, 37, 38, 40, 41, 42, 43, 44]
anchor: []
coverage:
  web: automated
---

# Tabel Files: siklus kotak Search

## Prerequisites
- Aktor: Total Control.
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-080-1: `warranty-card-lpt0004.pdf`, PDF, Source Attachment, Reference `General`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `310.0 KB`, Uploaded By `Rina A`, Upload Date `28/10/26 09:00`.
  - DU-080-2: `invoice-lpt0004.pdf`, PDF, Source Attachment, Reference `Purchase`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `450.2 KB`, Uploaded By `Budi S`, Upload Date `05/11/26 10:15`.
  - DU-080-3: `warranty-card-scn0003.pdf`, PDF, Source Custom Field Document, Reference `Warranty Card`, Asset `Scanner Epson DS-530 - 3`, Asset ID `SCN-2026-0003`, Group `Branch Bandung`, Size `300.0 KB`, Uploaded By `Rina A`, Upload Date `20/10/26 08:45`.
- Kondisi:
  - K1: tab `Asset Documents` aktif; tabel berisi DU-080-1, DU-080-2, dan DU-080-3; kotak Search belum dibuka dan belum ada kata kunci tersimpan.

## Test Steps

### Ikon Search membuka kotak input dengan fokus
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi ikon Search tampil
3. Verifikasi kotak input Search tidak tampil
4. Klik ikon Search
5. Verifikasi kotak input Search tampil
6. Verifikasi fokus berada di kotak input Search
7. Verifikasi placeholder `Search file name, asset...` tampil pada kotak input Search

### Pencarian berjalan saat Enter, bukan saat mengetik
8. Tampilkan Tabel File Manager tab Files dengan kondisi K1
9. Klik ikon Search
10. Ketik `warranty` pada kotak input Search
11. Verifikasi baris `invoice-lpt0004.pdf` tampil
12. Verifikasi baris `warranty-card-lpt0004.pdf` tampil
13. Verifikasi baris `warranty-card-scn0003.pdf` tampil
14. Tekan Enter
15. Verifikasi baris `warranty-card-lpt0004.pdf` tampil
16. Verifikasi baris `warranty-card-scn0003.pdf` tampil
17. Verifikasi baris `invoice-lpt0004.pdf` tidak tampil
18. Verifikasi kotak input Search tetap berisi `warranty`

### Tombol ✕ sebelum Enter tidak mereset, Enter dengan kotak kosong mereset
19. Tampilkan Tabel File Manager tab Files dengan kondisi K1
20. Klik ikon Search
21. Ketik `warranty` pada kotak input Search
22. Tekan Enter
23. Verifikasi baris `warranty-card-lpt0004.pdf` tampil
24. Verifikasi baris `invoice-lpt0004.pdf` tidak tampil
25. Klik tombol ✕ pada kotak input Search
26. Verifikasi placeholder `Search file name, asset...` tampil kembali pada kotak input Search
27. Verifikasi kotak input Search masih terbuka
28. Verifikasi baris `invoice-lpt0004.pdf` masih tidak tampil
29. Tekan Enter
30. Verifikasi baris `invoice-lpt0004.pdf` tampil
31. Verifikasi baris `warranty-card-lpt0004.pdf` tampil
32. Verifikasi baris `warranty-card-scn0003.pdf` tampil

### Tombol (←) menutup kotak sekaligus mereset
33. Tampilkan Tabel File Manager tab Files dengan kondisi K1
34. Klik ikon Search
35. Ketik `invoice` pada kotak input Search
36. Tekan Enter
37. Verifikasi baris `invoice-lpt0004.pdf` tampil
38. Verifikasi baris `warranty-card-lpt0004.pdf` tidak tampil
39. Klik tombol (←) pada kotak input Search
40. Verifikasi ikon Search tampil
41. Verifikasi kotak input Search tidak tampil
42. Verifikasi baris `invoice-lpt0004.pdf` tampil
43. Verifikasi baris `warranty-card-lpt0004.pdf` tampil
44. Verifikasi baris `warranty-card-scn0003.pdf` tampil
