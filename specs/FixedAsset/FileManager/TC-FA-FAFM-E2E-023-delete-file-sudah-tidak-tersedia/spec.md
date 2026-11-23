---
id: TC-FA-FAFM-E2E-023-delete-file-sudah-tidak-tersedia
title: "Delete atas file yang sudah dihapus permanen oleh aktor lain"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [ACT-04e, EC-15, S-20, T-03, T-13, "§4.4#b13", EB-ERR-3]
smoke: []
dependsOn: []
trace:
  ACT-04e: [9, 10, 13, 14]
  EC-15: [25, 26, 29, 31]
  S-20: 9
  T-03: 9
  T-13: 25
  "§4.4#b13": [25, 26]
  EB-ERR-3: [25, 26]
anchor: [2, 16]
coverage:
  web: automated
---

# Delete atas file yang sudah dihapus permanen oleh aktor lain

## Prerequisites
- Aktor: Total Control. Aktor kedua yang memicu perubahan: Total Control lain di entitas yang sama.
- Layar awal: Settings > File Manager.
- Data:
  - DU-023-1: Aset `Scanner Epson DS-530 {runId}`, Group `Branch Bandung`.
  - DU-023-2: File aktif `scanner-front-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `200.0 KB`, Asset `Scanner Epson DS-530 {runId}`, Group `Branch Bandung`.
  - DU-023-3: File aktif `scanner-back-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `210.0 KB`, Asset `Scanner Epson DS-530 {runId}`, Group `Branch Bandung`.
  - DU-023-4: File aktif `scanner-left-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `220.0 KB`, Asset `Scanner Epson DS-530 {runId}`, Group `Branch Bandung`.
  - DU-023-5: File aktif `scanner-right-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `230.0 KB`, Asset `Scanner Epson DS-530 {runId}`, Group `Branch Bandung`.
- Kondisi:
  - Daftar tab `Asset Photo` milik aktor pertama sudah termuat dan tidak dimuat ulang oleh aktor pertama sampai ia mengonfirmasi aksinya.

## Test Steps

### Sebagian item sudah dihapus permanen saat submit
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi file `scanner-front-{runId}.jpg`, `scanner-back-{runId}.jpg`, `scanner-left-{runId}.jpg`, dan `scanner-right-{runId}.jpg` tampil di tab `Asset Photo`
3. Centang baris `scanner-front-{runId}.jpg`
4. Centang baris `scanner-back-{runId}.jpg`
5. Klik `Delete` pada bar aksi bulk
6. Aktor kedua menghapus file `scanner-back-{runId}.jpg`
7. Aktor kedua menghapus permanen file `scanner-back-{runId}.jpg` dari Recycle Bin
8. Klik `[Delete]` pada dialog `Delete Files`
9. Verifikasi toast `Success, file has been deleted. Some items were skipped.` tampil
10. Verifikasi file `scanner-front-{runId}.jpg` dan `scanner-back-{runId}.jpg` tidak tampil lagi di tab `Asset Photo`
11. Klik `Recycle Bin` pada header kartu `Storage Usage`
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi file `scanner-front-{runId}.jpg` tampil di Recycle Bin
14. Verifikasi file `scanner-back-{runId}.jpg` tidak tampil di Recycle Bin
15. Tutup modal `Recycle Bin`

### Seluruh item sudah dihapus permanen saat submit
16. Verifikasi file `scanner-left-{runId}.jpg` dan `scanner-right-{runId}.jpg` masih tampil di tab `Asset Photo`
17. Centang baris `scanner-left-{runId}.jpg`
18. Centang baris `scanner-right-{runId}.jpg`
19. Klik `Delete` pada bar aksi bulk
20. Aktor kedua menghapus file `scanner-left-{runId}.jpg`
21. Aktor kedua menghapus file `scanner-right-{runId}.jpg`
22. Aktor kedua menghapus permanen file `scanner-left-{runId}.jpg` dari Recycle Bin
23. Aktor kedua menghapus permanen file `scanner-right-{runId}.jpg` dari Recycle Bin
24. Klik `[Delete]` pada dialog `Delete Files`
25. Verifikasi toast `This file is no longer available.` tampil
26. Verifikasi file `scanner-left-{runId}.jpg` dan `scanner-right-{runId}.jpg` tidak tampil lagi di tab `Asset Photo`

### Aksi atas file yang sudah tidak tersedia tidak menulis log
27. Klik `Changelog` pada header kartu `Storage Usage`
28. Ketik Search `scanner-left-{runId}.jpg`, tekan Enter
29. Verifikasi Changelog untuk File Name `scanner-left-{runId}.jpg` memuat tepat dua entri, yaitu Action `Delete` dan Action `Permanently Delete`
30. Ganti isi kotak search dengan `scanner-right-{runId}.jpg`, tekan Enter
31. Verifikasi Changelog untuk File Name `scanner-right-{runId}.jpg` memuat tepat dua entri, yaitu Action `Delete` dan Action `Permanently Delete`
32. Tutup modal `Changelog`
