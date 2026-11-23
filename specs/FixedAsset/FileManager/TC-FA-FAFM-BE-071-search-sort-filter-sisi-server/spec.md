---
id: TC-FA-FAFM-BE-071-search-sort-filter-sisi-server
title: "Search, sort, dan filter sisi server per kelas kolom"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["EB-SRC-1", "EB-FLT-3", "EB-SRT-1", "EB-SRT-2"]
smoke: []
dependsOn: []
trace:
  "EB-SRC-1": [2, 4, 6, 8, 10, 12, 42, 44, 46]
  "EB-FLT-3": [14, 16, 18, 20]
  "EB-SRT-1": [22, 24, 27, 30, 32, 34, 36]
  "EB-SRT-2": [25, 28, 38, 40]
---

# Search, sort, dan filter sisi server per kelas kolom

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`.
- Data:
  - DU-071-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-071-2: User `Budi Santoso {runId}`, pelaku soft-delete.
  - DU-071-3: User `Budi Hartono {runId}`, pelaku soft-delete.
  - DU-071-4: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`.
  - DU-071-5: Aset `Printer HP M404 {runId}`, group `Branch Bandung`, Status `Active`.
  - DU-071-6: Aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Status `Active`.
  - DU-071-7: Aset Draft `Camera Canon EOS 90D {runId}`, group `Head Office`, Status `Draft`; baris file-nya di Recycle Bin menampilkan Asset `—`.
  - DU-071-8: File `Anggur-lama-{runId}.png` di Recycle Bin, Category `Asset Photo`, Source `Asset Photo`, File Format PNG, aset DU-071-4, group `Head Office`, Size `900.0 KB` dari 921600 byte, Deleted By `Budi Santoso {runId}`, di-soft-delete ketiga dari enam file.
  - DU-071-9: File `apel-lama-{runId}.jpg` di Recycle Bin, Category `Asset Photo`, Source `Asset Photo`, File Format JPG, aset DU-071-5, group `Branch Bandung`, Size `1.0 MB` dari 1048576 byte, Deleted By `Budi Hartono {runId}`, di-soft-delete pertama dari enam file.
  - DU-071-10: File `Dokumen-garansi-{runId}.pdf` di Recycle Bin, Category `Asset Documents`, Source `Attachment`, File Format PDF, aset DU-071-4, group `Head Office`, Size `300.0 KB` dari 307200 byte, Deleted By `System`, di-soft-delete keenam dari enam file.
  - DU-071-11: File `draft-foto-{runId}.jpg` di Recycle Bin, Category `Asset Photo`, Source `Asset Photo`, File Format JPG, aset DU-071-7 (Asset `—`), group `Head Office`, Size `450.0 KB` dari 460800 byte, Deleted By `Budi Santoso {runId}`, di-soft-delete kelima dari enam file.
  - DU-071-12: File `repair-{runId}.jpg` di Recycle Bin, Category `Damaged`, Source `Repair Photo`, File Format JPG, aset DU-071-5, group `Branch Bandung`, Size `900.0 KB` dari 921600 byte, Deleted By `Budi Hartono {runId}`, di-soft-delete kedua dari enam file.
  - DU-071-13: File `Zebra-{runId}.pdf` di Recycle Bin, Category `Disposal`, Source `Disposal Document`, File Format PDF, aset DU-071-6, group `Branch Bandung`, Size `3.0 MB` dari 3145728 byte, Deleted By `System`, di-soft-delete keempat dari enam file.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.

## Test Steps

### Search sisi server per kelas kolom
1. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `ggur-lama-{runId}` langsung ke server
2. Verifikasi hasil memuat file `Anggur-lama-{runId}.png` dan tidak memuat file lain milik spec ini, karena kata kunci dicocokkan sebagai substring di tengah nama
3. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `GGUR-LAMA-{runId}` langsung ke server
4. Verifikasi hasil sama dengan langkah 2, karena pencarian tidak membedakan huruf besar dan kecil
5. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `Branch Bandung` langsung ke server
6. Verifikasi hasil memuat file `apel-lama-{runId}.jpg`, `repair-{runId}.jpg`, dan `Zebra-{runId}.pdf`, serta tidak memuat `Anggur-lama-{runId}.png`, `Dokumen-garansi-{runId}.pdf`, dan `draft-foto-{runId}.jpg` (kolom badge Group)
7. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `Repair Photo` langsung ke server
8. Verifikasi hasil memuat file `repair-{runId}.jpg` dan tidak memuat file lain milik spec ini (kolom enum Source)
9. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `System` langsung ke server
10. Verifikasi hasil memuat file `Dokumen-garansi-{runId}.pdf` dan `Zebra-{runId}.pdf`, serta tidak memuat file lain milik spec ini (kolom teks Deleted By)
11. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `tidak-ada-{runId}` langsung ke server
12. Verifikasi hasil tidak memuat satu pun baris

### Filter sisi server: OR dalam satu field dan AND antar field
13. `Bagas Pratama {runId}` memfilter Recycle Bin dengan File Format `JPG` dan kata kunci `{runId}` langsung ke server
14. Verifikasi hasil memuat file `apel-lama-{runId}.jpg`, `draft-foto-{runId}.jpg`, dan `repair-{runId}.jpg`, serta tidak memuat `Anggur-lama-{runId}.png`, `Dokumen-garansi-{runId}.pdf`, dan `Zebra-{runId}.pdf`
15. `Bagas Pratama {runId}` memfilter Recycle Bin dengan File Format `JPG` dan `PNG` serta kata kunci `{runId}` langsung ke server
16. Verifikasi hasil memuat file `Anggur-lama-{runId}.png`, `apel-lama-{runId}.jpg`, `draft-foto-{runId}.jpg`, dan `repair-{runId}.jpg` (OR dalam satu field), serta tidak memuat `Dokumen-garansi-{runId}.pdf` dan `Zebra-{runId}.pdf`
17. `Bagas Pratama {runId}` memfilter Recycle Bin dengan File Format `JPG` dan Group `Branch Bandung` serta kata kunci `{runId}` langsung ke server
18. Verifikasi hasil memuat file `apel-lama-{runId}.jpg` dan `repair-{runId}.jpg` (AND antar field), serta tidak memuat `draft-foto-{runId}.jpg` (JPG di `Head Office`) dan `Zebra-{runId}.pdf` (PDF di `Branch Bandung`)
19. `Bagas Pratama {runId}` memfilter Recycle Bin dengan Source `Repair Photo` dan `Disposal Document`, Deleted By `System`, serta kata kunci `{runId}` langsung ke server
20. Verifikasi hasil memuat file `Zebra-{runId}.pdf` dan tidak memuat `repair-{runId}.jpg` (Deleted By `Budi Hartono {runId}`) maupun `Dokumen-garansi-{runId}.pdf` (Source `Attachment`)

### Sort sisi server per tipe kolom
21. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut File Name A-Z dengan kata kunci `{runId}` langsung ke server
22. Verifikasi urutan file milik spec ini: `Anggur-lama-{runId}.png`, `apel-lama-{runId}.jpg`, `Dokumen-garansi-{runId}.pdf`, `draft-foto-{runId}.jpg`, `repair-{runId}.jpg`, `Zebra-{runId}.pdf`, tanpa membedakan huruf besar dan kecil
23. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Size naik dengan kata kunci `{runId}` langsung ke server
24. Verifikasi urutan file milik spec ini menurut nilai byte: `Dokumen-garansi-{runId}.pdf`, `draft-foto-{runId}.jpg`, `Anggur-lama-{runId}.png`, `repair-{runId}.jpg`, `apel-lama-{runId}.jpg`, `Zebra-{runId}.pdf`
25. Verifikasi `Anggur-lama-{runId}.png` berada di atas `repair-{runId}.jpg` walau Size keduanya sama, karena nilai sama diurutkan menurut default Deleted Date terbaru
26. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Size turun dengan kata kunci `{runId}` langsung ke server
27. Verifikasi urutan file milik spec ini: `Zebra-{runId}.pdf`, `apel-lama-{runId}.jpg`, `Anggur-lama-{runId}.png`, `repair-{runId}.jpg`, `draft-foto-{runId}.jpg`, `Dokumen-garansi-{runId}.pdf`
28. Verifikasi `Anggur-lama-{runId}.png` tetap berada di atas `repair-{runId}.jpg` pada urutan turun, karena tie-breaker mengikuti default sort tabel
29. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Deleted Date Oldest First dengan kata kunci `{runId}` langsung ke server
30. Verifikasi urutan file milik spec ini: `apel-lama-{runId}.jpg`, `repair-{runId}.jpg`, `Anggur-lama-{runId}.png`, `Zebra-{runId}.pdf`, `draft-foto-{runId}.jpg`, `Dokumen-garansi-{runId}.pdf`
31. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Deleted Date Newest First dengan kata kunci `{runId}` langsung ke server
32. Verifikasi urutan file milik spec ini adalah kebalikan langkah 30
33. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Deleted By A-Z dengan kata kunci `{runId}` langsung ke server
34. Verifikasi urutan file milik spec ini menurut nama lengkap pelaku: `repair-{runId}.jpg` dan `apel-lama-{runId}.jpg` (`Budi Hartono {runId}`), `draft-foto-{runId}.jpg` dan `Anggur-lama-{runId}.png` (`Budi Santoso {runId}`), lalu `Dokumen-garansi-{runId}.pdf` dan `Zebra-{runId}.pdf` (`System`)
35. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Group A-Z dengan kata kunci `{runId}` langsung ke server
36. Verifikasi urutan file milik spec ini: `Zebra-{runId}.pdf`, `repair-{runId}.jpg`, `apel-lama-{runId}.jpg` (`Branch Bandung`), lalu `Dokumen-garansi-{runId}.pdf`, `draft-foto-{runId}.jpg`, `Anggur-lama-{runId}.png` (`Head Office`)
37. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Asset A-Z dengan kata kunci `{runId}` langsung ke server
38. Verifikasi nilai kosong berada di akhir pada urutan naik: `Dokumen-garansi-{runId}.pdf`, `Anggur-lama-{runId}.png`, `repair-{runId}.jpg`, `apel-lama-{runId}.jpg`, `Zebra-{runId}.pdf`, lalu `draft-foto-{runId}.jpg` dengan Asset `—`
39. `Bagas Pratama {runId}` mengurutkan Recycle Bin menurut Asset Z-A dengan kata kunci `{runId}` langsung ke server
40. Verifikasi nilai kosong berada di awal pada urutan turun: `draft-foto-{runId}.jpg` dengan Asset `—`, lalu `Zebra-{runId}.pdf`, `repair-{runId}.jpg`, `apel-lama-{runId}.jpg`, `Dokumen-garansi-{runId}.pdf`, dan `Anggur-lama-{runId}.png`

### Search sebagian kata dan beda huruf pada kolom badge, enum, dan teks pengguna
41. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `RANCH BANDU` langsung ke server
42. Verifikasi hasil memuat file `apel-lama-{runId}.jpg`, `repair-{runId}.jpg`, dan `Zebra-{runId}.pdf`, serta tidak memuat `Anggur-lama-{runId}.png`, `Dokumen-garansi-{runId}.pdf`, dan `draft-foto-{runId}.jpg`, karena potongan nama group dengan huruf besar tetap cocok (kolom badge Group)
43. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `PAIR PHOT` langsung ke server
44. Verifikasi hasil memuat file `repair-{runId}.jpg` dan tidak memuat file lain milik spec ini, karena potongan label Source dengan huruf besar tetap cocok (kolom enum Source)
45. `Bagas Pratama {runId}` mencari di Recycle Bin dengan kata kunci `SYSTE` langsung ke server
46. Verifikasi hasil memuat file `Dokumen-garansi-{runId}.pdf` dan `Zebra-{runId}.pdf`, serta tidak memuat file lain milik spec ini, karena potongan teks pelaku dengan huruf besar tetap cocok (kolom teks Deleted By)
