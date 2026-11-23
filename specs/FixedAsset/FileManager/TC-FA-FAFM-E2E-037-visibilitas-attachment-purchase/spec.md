---
id: TC-FA-FAFM-E2E-037-visibilitas-attachment-purchase
title: "File Attachment kelompok Purchase hanya terlihat oleh role yang berhak"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [F-FAFM-01f, FAFM-LOGIC-09a, FAFM-LOGIC-09b, FAFM-LOGIC-09c, "§9.11#r8"]
smoke: []
dependsOn: []
trace:
  F-FAFM-01f: [4, 11, 27]
  FAFM-LOGIC-09a: [4, 5, 8, 12, 16, 19]
  FAFM-LOGIC-09b: [7, 27, 28, 29, 33, 38, 42]
  FAFM-LOGIC-09c: [1, 23, 49]
  "§9.11#r8": [27, 29, 33, 38, 42]
anchor: [6, 26, 32, 37, 41]
coverage:
  web: automated
---

# File Attachment kelompok Purchase hanya terlihat oleh role yang berhak

## Prerequisites
- Aktor: Alya Akses Purchase `{runId}` (aktor pertama; pemegang Manage files Read pada group `Head Office` dengan akses Attachments kelompok Purchase menurut Asset List §9.11) dan Bima Tanpa Purchase `{runId}` (aktor kedua pada konteks browser kedua yang terpisah; pemegang Manage files Read pada group `Head Office` tanpa akses Attachments kelompok Purchase).
- Layar awal: Settings > File Manager, tab bawaan `Asset Photo` aktif untuk kedua aktor.
- Data:
  - DU-037-1: User `Alya Akses Purchase {runId}`, role `Pembaca File Purchase {runId}`, capability `Manage files: Read` pada group `Head Office`, akses Attachments kelompok Purchase.
  - DU-037-2: User `Bima Tanpa Purchase {runId}`, role `Pembaca File Non-Purchase {runId}`, capability `Manage files: Read` pada group `Head Office`, tanpa akses Attachments kelompok Purchase.
  - DU-037-3: File `invoice-forklift-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `Purchase`, Asset `Forklift Gudang {runId}` (Increment dibentuk server), Group `Head Office`, Size `420.0 KB`, Uploaded By `Budi S`, Upload Date `T0 − 3 hari, pukul 10:15`.
  - DU-037-4: File `warranty-forklift-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Forklift Gudang {runId}` (Increment dibentuk server), Group `Head Office`, Size `310.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 5 hari, pukul 09:00`.
  - DU-037-5: File `invoice-bandung-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `Purchase`, Asset `Genset Bandung {runId}` (Increment dibentuk server), Group `Branch Bandung` (di luar group kedua aktor), Size `380.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 4 hari, pukul 14:00`.
  - DU-037-6: File `invoice-lama-{runId}.pdf`, File Format `PDF`, Category `Asset Documents`, Source `Attachment`, Reference `Purchase`, Asset `Forklift Gudang {runId}` (Increment dibentuk server), Group `Head Office`, Size `260.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 1 hari, pukul 09:00`, ada di Recycle Bin dan di Changelog (aksi Delete).
  - DU-037-7: File `warranty-lama-{runId}.pdf`, File Format `PDF`, Category `Asset Documents`, Source `Attachment`, Reference `General`, Asset `Forklift Gudang {runId}` (Increment dibentuk server), Group `Head Office`, Size `150.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 1 hari, pukul 09:30`, ada di Recycle Bin dan di Changelog (aksi Delete).

## Test Steps

### Aktor 1 dengan akses Attachments kelompok Purchase melihat baris Purchase
1. Verifikasi kartu `Storage Usage` tampil
2. Klik tab `Asset Documents`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi baris `invoice-forklift-{runId}.pdf` tampil pada tabel
5. Verifikasi baris `invoice-forklift-{runId}.pdf` menampilkan File Format `PDF`, Source `Attachment`, Reference `Purchase`, Group `Head Office`, dan Size `420.0 KB`
6. Verifikasi baris `warranty-forklift-{runId}.pdf` tampil pada tabel
7. Verifikasi baris `invoice-bandung-{runId}.pdf` tidak ada pada tabel
8. Verifikasi paginator menampilkan `Showing 1 to 2 of 2`

### Recycle Bin dan Changelog Aktor 1
9. Klik `Recycle Bin` pada header kartu Storage Usage
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris `warranty-lama-{runId}.pdf` tampil pada Recycle Bin
12. Verifikasi baris `invoice-lama-{runId}.pdf` tampil pada Recycle Bin
13. Tutup dialog Recycle Bin
14. Klik `Changelog` pada header kartu Storage Usage
15. Ketik Search `{runId}`, tekan Enter
16. Verifikasi baris log dengan File Name `invoice-lama-{runId}.pdf` tampil pada Changelog
17. Klik `Filter` pada dialog Changelog
18. Klik filter `File Name`
19. Verifikasi opsi `invoice-lama-{runId}.pdf` tampil
20. Tutup panel Filter
21. Tutup dialog Changelog

### Aktor 2 tanpa akses Attachments kelompok Purchase pada konteks browser kedua
22. Beralih ke konteks browser kedua (Bima Tanpa Purchase `{runId}`, Settings > File Manager terbuka)
23. Verifikasi kartu `Storage Usage` tampil
24. Klik tab `Asset Documents`
25. Ketik Search `{runId}`, tekan Enter
26. Verifikasi baris `warranty-forklift-{runId}.pdf` tampil pada tabel
27. Verifikasi baris `invoice-forklift-{runId}.pdf` tidak ada pada tabel
28. Verifikasi baris `invoice-bandung-{runId}.pdf` tidak ada pada tabel
29. Verifikasi paginator menampilkan `Showing 1 to 1 of 1`

### Recycle Bin dan Changelog Aktor 2
30. Klik `Recycle Bin` pada header kartu Storage Usage
31. Ketik Search `{runId}`, tekan Enter
32. Verifikasi baris `warranty-lama-{runId}.pdf` tampil pada Recycle Bin
33. Verifikasi baris `invoice-lama-{runId}.pdf` tidak ada pada Recycle Bin
34. Tutup dialog Recycle Bin
35. Klik `Changelog` pada header kartu Storage Usage
36. Ketik Search `{runId}`, tekan Enter
37. Verifikasi baris log dengan File Name `warranty-lama-{runId}.pdf` tampil pada Changelog
38. Verifikasi baris log dengan File Name `invoice-lama-{runId}.pdf` tidak ada pada Changelog
39. Klik `Filter` pada dialog Changelog
40. Klik filter `File Name`
41. Verifikasi opsi `warranty-lama-{runId}.pdf` tampil
42. Verifikasi opsi `invoice-lama-{runId}.pdf` tidak ada

### Angka Fixed Asset pada kartu sama untuk kedua aktor
43. Tutup panel Filter
44. Tutup dialog Changelog
45. Muat ulang halaman
46. Catat angka `Fixed Asset` pada kartu Storage Usage aktor kedua
47. Beralih ke konteks browser pertama (Alya Akses Purchase `{runId}`)
48. Muat ulang halaman
49. Verifikasi angka `Fixed Asset` pada kartu Storage Usage sama dengan angka yang dicatat pada aktor kedua
