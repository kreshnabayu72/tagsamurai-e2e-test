---
id: TC-FA-FAFM-E2E-006-tab-files-download
title: "Download CSV dan XLSX dari tab Files"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["INV-10d", "TBL-06b", "TBL-06c", "TBL-06e", "TBL-06d", "EB-DL-1@tabel-files", "EB-DL-2@tabel-files", "EB-DL-3@tabel-files", "EB-DL-4"]
smoke: []
dependsOn: []
trace:
  "INV-10d": 6
  "TBL-06b": 6
  "TBL-06c": 7
  "TBL-06e": [8, 9, 15, 16, 25, 26, 48, 49, 57, 58, 59]
  "TBL-06d": [6, 14, 57]
  "EB-DL-1@tabel-files": [2, 9, 11, 15, 16, 21, 25, 26, 34, 39, 44, 48, 49, 54, 60, 61]
  "EB-DL-2@tabel-files": 7
  "EB-DL-3@tabel-files": [4, 6, 14, 24, 33, 47, 57]
  "EB-DL-4": [8, 30, 34, 36, 39, 58]
anchor: [6, 14, 24, 33, 47, 57]
coverage:
  web: automated
---

# Download CSV dan XLSX dari tab Files

## Prerequisites
- Aktor: Total Control, user `Citra Dewi {runId}` (tampil `Citra D`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Spec ini memakai entitas khusus (seluruh-daftar): entitas hanya berisi 14 file tab `Asset Documents` dan 3 file tab `Asset Photo` di bawah, tanpa file lain.
  - Aset `Mesin Cetak {runId}` dan Group `Gudang Pusat {runId}` ada di entitas aktor; semua file milik aset itu.
  - Urutan pembuatan dari paling lama ke paling baru: DU-006-1, DU-006-2, DU-006-3, lalu DU-006-4; selisih waktu unggah minimal satu menit antar baris.
  - DU-006-1: File File Name `dok-{n}-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Mesin Cetak {runId}`, Group `Gudang Pusat {runId}`, Size `100.0 KB`, Uploaded By `Citra D` (9 file dibuat paling awal, selisih waktu unggah minimal satu menit antar baris).
  - DU-006-2: File File Name `gbr-{n}-{runId}.png`, File Format `PNG`, Source `Attachment`, Reference `General`, Asset `Mesin Cetak {runId}`, Group `Gudang Pusat {runId}`, Size `100.0 KB`, Uploaded By `Citra D` (2 file dibuat sesudah DU-006-1).
  - DU-006-3: File File Name `lap-{n}-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Mesin Cetak {runId}`, Group `Gudang Pusat {runId}`, Size `100.0 KB`, Uploaded By `Citra D` (3 file dibuat paling akhir).
  - DU-006-4: File File Name `foto-{n}-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Mesin Cetak {runId}`, Group `Gudang Pusat {runId}`, Size `100.0 KB`, Uploaded By `Citra D` (3 file).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Download tanpa saringan memuat seluruh baris lintas halaman sebagai CSV
1. Klik tab `Asset Documents`
2. Verifikasi Pagination menampilkan total `14` baris dalam `2` halaman
3. Klik ikon Download
4. Verifikasi pilihan `Download as XLSX` dan `Download as CSV` tampil
5. Klik `Download as CSV`
6. Verifikasi berkas `File-Manager-Files` format CSV terunduh langsung tanpa dialog atau langkah tambahan
7. Verifikasi tidak ada toast sukses setelah unduhan selesai
8. Verifikasi header berkas: `File Name`, `File Format`, `Source`, `Reference`, `Asset`, `Asset ID`, `Group`, `Size`, `Uploaded By`, dan `Upload Date`
9. Verifikasi berkas memuat `14` baris data walaupun tabel menampilkan `10` baris per halaman

### Download mengikuti Search dan Filter yang aktif sebagai XLSX
10. Ketik Search `lap-`, tekan Enter
11. Verifikasi baris `lap-1-{runId}.pdf`, `lap-2-{runId}.pdf`, dan `lap-3-{runId}.pdf` tampil
12. Klik ikon Download
13. Klik `Download as XLSX`
14. Verifikasi berkas `File-Manager-Files` format XLSX terunduh
15. Verifikasi berkas memuat `3` baris data: `lap-1-{runId}.pdf`, `lap-2-{runId}.pdf`, dan `lap-3-{runId}.pdf`
16. Verifikasi berkas tidak memuat baris `dok-1-{runId}.pdf`
17. Klik `(←)` pada kotak Search
18. Klik ikon Filter
19. Pilih File Format `PNG` pada panel Filter
20. Klik `[Apply]`
21. Verifikasi baris `gbr-1-{runId}.png` dan `gbr-2-{runId}.png` tampil
22. Klik ikon Download
23. Klik `Download as CSV`
24. Verifikasi berkas `File-Manager-Files` format CSV terunduh
25. Verifikasi berkas memuat `2` baris data: `gbr-1-{runId}.png` dan `gbr-2-{runId}.png`
26. Verifikasi berkas tidak memuat baris `lap-1-{runId}.pdf`
27. Klik `[Clear Field]`
28. Klik `[Apply]`

### Urutan baris berkas mengikuti sort aktif
29. Klik ikon sort pada header kolom `File Name`
30. Verifikasi baris pertama tabel adalah `dok-1-{runId}.pdf`
31. Klik ikon Download
32. Klik `Download as CSV`
33. Verifikasi berkas `File-Manager-Files` format CSV terunduh
34. Verifikasi baris data pertama berkas adalah `dok-1-{runId}.pdf` mengikuti urutan A-Z
35. Klik ikon sort pada header kolom `File Name` sekali lagi
36. Verifikasi baris pertama tabel adalah `lap-3-{runId}.pdf`
37. Klik ikon Download
38. Klik `Download as CSV`
39. Verifikasi baris data pertama berkas adalah `lap-3-{runId}.pdf` mengikuti urutan Z-A
40. Klik ikon sort pada header kolom `File Name` untuk ketiga kalinya

### Kolom yang disembunyikan tidak ikut diunduh
41. Klik header kolom `Actions` (`⋯`) pada tabel
42. Hilangkan centang kolom `Group` pada panel Column Visibility
43. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
44. Verifikasi kolom `Group` tidak tampil di tabel
45. Klik ikon Download
46. Klik `Download as CSV`
47. Verifikasi berkas `File-Manager-Files` format CSV terunduh
48. Verifikasi header berkas memuat `File Name`, `File Format`, `Source`, `Reference`, `Asset`, `Asset ID`, `Size`, `Uploaded By`, dan `Upload Date`
49. Verifikasi header berkas tidak memuat `Group`
50. Klik header kolom `Actions` (`⋯`) pada tabel
51. Centang kolom `Group` pada panel Column Visibility
52. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility

### Download memuat baris tab aktif saja dengan nama berkas yang sama
53. Klik tab `Asset Photo`
54. Verifikasi baris `foto-1-{runId}.jpg`, `foto-2-{runId}.jpg`, dan `foto-3-{runId}.jpg` tampil
55. Klik ikon Download
56. Klik `Download as CSV`
57. Verifikasi berkas `File-Manager-Files` format CSV terunduh walaupun tab aktif adalah `Asset Photo`
58. Verifikasi header berkas: `File Name`, `File Format`, `Asset`, `Asset ID`, `Group`, `Size`, `Uploaded By`, dan `Upload Date`
59. Verifikasi header berkas tidak memuat `Source` dan `Reference`
60. Verifikasi berkas memuat `3` baris data: `foto-1-{runId}.jpg`, `foto-2-{runId}.jpg`, dan `foto-3-{runId}.jpg`
61. Verifikasi berkas tidak memuat baris `dok-1-{runId}.pdf`
