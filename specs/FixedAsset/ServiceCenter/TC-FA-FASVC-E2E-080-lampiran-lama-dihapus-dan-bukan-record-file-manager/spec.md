---
id: TC-FA-FASVC-E2E-080-lampiran-lama-dihapus-dan-bukan-record-file-manager
title: "Lampiran Diganti atau Dihapus pada Edit: Berkas Lama Hilang dari Penyimpanan dan Tidak Masuk File Manager"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceRules: ["FASVC-LOGIC-13d", "FASVC-LOGIC-13e", "FASVC-LOGIC-06d", "RX-FASVC-02", "RX-FASVC-34", "EC-FASVC-63", "F-FASVC-07.k5"]
smoke: []
dependsOn: ["File Manager: halaman Settings > File Manager (tab Files, Recycle Bin)"]
trace:
  "FASVC-LOGIC-13d": [15, 32, 46, 48]
  "FASVC-LOGIC-13e": [37, 39, 41]
  "FASVC-LOGIC-06d": [37, 39, 41]
  "RX-FASVC-02": [13, 15, 18, 30, 32]
  "RX-FASVC-34": [15, 32]
  "EC-FASVC-63": [15, 32, 46, 48]
  "F-FASVC-07.k5": [13, 15, 30, 32]
anchor: [3, 9, 22, 35, 44]
coverage:
  web: automated
---

# Lampiran Diganti atau Dihapus pada Edit: Berkas Lama Hilang dari Penyimpanan dan Tidak Masuk File Manager

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-080-1: Service Center `Ganti Lampiran {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Kota Tinggi {runId}`, Company phone `+60 7555330101`, Attachments `izin-lama-080.pdf` (PDF, 300 KB).
  - DU-080-2: Service Center `Hapus Lampiran {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Mersing {runId}`, Company phone `+60 7555330202`, Attachments `izin-hapus-080.pdf` (PDF, 300 KB).
  - DU-080-3: Berkas pengganti `izin-baru-080.pdf` (PDF, 400 KB), dilampirkan oleh langkah.
  - DU-080-4: Aset `Aset Foto 080 {runId}` dengan Photo `foto-aset-080.jpg`, sehingga tab Files di File Manager memuat sedikitnya satu baris.
  - DU-080-5: Berkas `foto-bin-080.jpg` milik aset `Aset Foto 080 {runId}` yang sudah dihapus lewat Delete di File Manager, sehingga Recycle Bin memuat sedikitnya satu baris.
- Kondisi:
  - Storage entitas aktor tidak penuh.

## Test Steps

### Lampiran lama dapat dibuka sebelum Edit
1. Ketik Search `Ganti Lampiran {runId}`, tekan Enter
2. Klik Name `Ganti Lampiran {runId}`
3. Verifikasi lampiran pada Overview Attachments dapat dibuka
4. Catat alamat lampiran pada Overview Attachments
5. Klik breadcrumb `Service Center`

### Edit mengganti lampiran: berkas lama dihapus dari penyimpanan saat Save
6. Ketik Search `Ganti Lampiran {runId}`, tekan Enter
7. Klik `⋯` pada baris `Ganti Lampiran {runId}`
8. Klik `Edit`
9. Verifikasi baris file `izin-lama-080.pdf` tampil di Attachments
10. Hapus berkas pada baris file `izin-lama-080.pdf` lewat ikon hapus
11. Unggah berkas `izin-baru-080.pdf` (PDF, 400 KB) pada Attachments
12. Klik `[Save]`
13. Verifikasi toast `Success, Ganti Lampiran {runId} has been updated.` tampil
14. Buka alamat lampiran yang dicatat pada langkah 4
15. Verifikasi lampiran tidak dapat dibuka
16. Ketik Search `Ganti Lampiran {runId}`, tekan Enter
17. Klik Name `Ganti Lampiran {runId}`
18. Verifikasi lampiran `izin-baru-080.pdf` pada Overview Attachments dapat dibuka
19. Klik breadcrumb `Service Center`

### Edit menghapus lampiran: berkas dihapus dari penyimpanan saat Save
20. Ketik Search `Hapus Lampiran {runId}`, tekan Enter
21. Klik Name `Hapus Lampiran {runId}`
22. Verifikasi lampiran pada Overview Attachments dapat dibuka
23. Catat alamat lampiran pada Overview Attachments
24. Klik breadcrumb `Service Center`
25. Ketik Search `Hapus Lampiran {runId}`, tekan Enter
26. Klik `⋯` pada baris `Hapus Lampiran {runId}`
27. Klik `Edit`
28. Hapus berkas pada baris file `izin-hapus-080.pdf` lewat ikon hapus
29. Klik `[Save]`
30. Verifikasi toast `Success, Hapus Lampiran {runId} has been updated.` tampil
31. Buka alamat lampiran yang dicatat pada langkah 23
32. Verifikasi lampiran tidak dapat dibuka

### Lampiran Service Center tidak tampil di tab Files File Manager
33. Buka menu `Settings` pada sidebar
34. Klik `File Manager`
35. Verifikasi baris `foto-aset-080.jpg` tampil di tab Files
36. Ketik Search `izin-baru-080.pdf`, tekan Enter
37. Verifikasi tabel menampilkan empty state `No results found`
38. Ganti isi kotak search dengan `izin-lama-080.pdf`, tekan Enter
39. Verifikasi tabel menampilkan empty state `No results found`
40. Ganti isi kotak search dengan `izin-hapus-080.pdf`, tekan Enter
41. Verifikasi tabel menampilkan empty state `No results found`
42. Klik `(←)` pada kotak Search

### Berkas lama tidak masuk Recycle Bin File Manager
43. Klik `[Recycle Bin]`
44. Verifikasi baris `foto-bin-080.jpg` tampil di dialog `Recycle Bin`
45. Ketik Search `izin-lama-080.pdf` pada dialog `Recycle Bin`, tekan Enter
46. Verifikasi tabel pada dialog `Recycle Bin` menampilkan empty state `No results found`
47. Ganti isi kotak search pada dialog `Recycle Bin` dengan `izin-hapus-080.pdf`, tekan Enter
48. Verifikasi tabel pada dialog `Recycle Bin` menampilkan empty state `No results found`
