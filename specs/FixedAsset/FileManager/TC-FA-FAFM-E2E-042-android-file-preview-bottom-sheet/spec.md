---
id: TC-FA-FAFM-E2E-042-android-file-preview-bottom-sheet
title: "Mobile: File Preview sebagai bottom sheet"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAFM-02b", "INV-03b", "INV-03e", "PRV-08", "PRV-09", "S-11", "S-12", "V-01", "§4.4#b2"]
smoke: []
dependsOn: []
trace:
  "F-FAFM-02b": [4]
  "INV-03b": [4]
  "INV-03e": [5, 6, 7, 9, 10, 11, 12, 13, 14]
  "PRV-08": [4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 19, 23, 24, 25]
  "PRV-09": [8, 29]
  "S-11": [29]
  "S-12": [35, 36, 38]
  "V-01": [45, 47]
  "§4.4#b2": [4]
anchor: [2, 18, 31, 37, 40, 46]
coverage:
  android: automated
---

# Mobile: File Preview sebagai bottom sheet

## Prerequisites
- Aktor: Total Control. Aktor pemicu: Total Control lain pada entitas yang sama, hanya untuk perubahan yang memicu keadaan file tidak tersedia.
- Layar awal: Settings > File Manager.
- Data:
  - DU-042-1: Asset `Laptop Dell Latitude {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-042-2: File gambar `laptop-front-{runId}.jpg`, Format `JPG`, Source `Asset Photo`, Category `Asset Photo`, Size `820.4 KB` dari 840090 byte, Dimensions `1600 × 1200 px`, Uploaded By `System`, milik DU-042-1.
  - DU-042-3: File dokumen `warranty-card-{runId}.pdf`, Format `PDF`, Source `Attachment`, Category `Asset Documents`, Size `310.0 KB` dari 317440 byte, Uploaded By `System`, milik DU-042-1.
  - DU-042-4: File gambar `corrupt-photo-{runId}.jpg` yang isinya tidak dapat dimuat sebagai gambar, Format `JPG`, Source `Asset Photo`, Category `Asset Photo`, Size `100.0 KB` dari 102400 byte, Uploaded By `System`, milik DU-042-1.
  - DU-042-5: File `old-label-{runId}.png`, Source `Asset Photo`, Category `Asset Photo`, Size `1.0 MB` dari 1048576 byte, milik DU-042-1.
  - DU-042-6: File `old-invoice-{runId}.pdf`, Source `Attachment`, Category `Asset Documents`, Size `450.2 KB` dari 461005 byte, milik DU-042-1.

## Test Steps

### Preview gambar tampil sebagai bottom sheet
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi kartu `laptop-front-{runId}.jpg` tampil
3. Ketuk File Name `laptop-front-{runId}.jpg` pada kartunya
4. Verifikasi File Preview tampil sebagai bottom sheet berjudul `File Preview`
5. Verifikasi bottom sheet menampilkan nama file `laptop-front-{runId}.jpg`
6. Verifikasi bottom sheet menampilkan gambar file
7. Verifikasi bottom sheet menampilkan Format `JPG`
8. Verifikasi bottom sheet menampilkan Dimensions `1600 × 1200 px`
9. Verifikasi bottom sheet menampilkan Size `820.4 KB`
10. Verifikasi bottom sheet menampilkan Source `Asset Photo`
11. Verifikasi bottom sheet menampilkan Asset milik DU-042-1
12. Verifikasi bottom sheet menampilkan Uploaded By `System`
13. Verifikasi bottom sheet memuat `[Download File]`
14. Verifikasi bottom sheet memuat `[Close]`
15. Ketuk `[Download File]`
16. Verifikasi berkas `laptop-front-{runId}.jpg` terunduh ke perangkat
17. Ketuk `[Close]`
18. Verifikasi kartu `laptop-front-{runId}.jpg` tampil
19. Verifikasi bottom sheet File Preview tidak tampil

### Preview dokumen tanpa Dimensions
20. Ketuk tab `Asset Documents`
21. Ketik Search `{runId}`, tekan Enter
22. Ketuk File Name `warranty-card-{runId}.pdf` pada kartunya
23. Verifikasi bottom sheet menampilkan ikon format dokumen
24. Verifikasi bottom sheet menampilkan Format `PDF`
25. Verifikasi bottom sheet tidak menampilkan Dimensions
26. Ketuk `[Close]`

### Dimensions bila gambar gagal dimuat
27. Ketuk tab `Asset Photo`
28. Ketuk File Name `corrupt-photo-{runId}.jpg` pada kartunya
29. Verifikasi bottom sheet menampilkan Dimensions `—`
30. Ketuk `[Close]`

### Preview file yang sudah tidak tersedia
31. Verifikasi kartu `old-label-{runId}.png` tampil
32. Aktor pemicu menghapus file `old-label-{runId}.png`
33. Aktor pemicu menghapus permanen file `old-label-{runId}.png` dari Recycle Bin
34. Ketuk File Name `old-label-{runId}.png` pada kartunya
35. Verifikasi toast Info `This file is no longer available.` tampil
36. Verifikasi bottom sheet File Preview tidak tampil
37. Verifikasi kartu `laptop-front-{runId}.jpg` tampil
38. Verifikasi kartu `old-label-{runId}.png` tidak tampil

### Download file yang sudah tidak tersedia
39. Ketuk tab `Asset Documents`
40. Verifikasi kartu `old-invoice-{runId}.pdf` tampil
41. Aktor pemicu menghapus file `old-invoice-{runId}.pdf`
42. Aktor pemicu menghapus permanen file `old-invoice-{runId}.pdf` dari Recycle Bin
43. Ketuk `[⋯]` pada kartu `old-invoice-{runId}.pdf`
44. Ketuk `Download`
45. Verifikasi toast Info `This file is no longer available.` tampil
46. Verifikasi kartu `warranty-card-{runId}.pdf` tampil
47. Verifikasi kartu `old-invoice-{runId}.pdf` tidak tampil
