---
id: TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia
title: "Permanently Delete atas file yang sudah dihapus permanen oleh aktor lain"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [ACT-06e, EC-05, EC-06, EC-15, F-FAFM-03g, S-22, T-08, T-13, V-13]
smoke: []
dependsOn: []
trace:
  ACT-06e: [16, 17]
  EC-05: [7, 8]
  EC-06: [16, 17]
  EC-15: [26, 27, 31, 33]
  F-FAFM-03g: [7, 8]
  S-22: 16
  T-08: 16
  T-13: [7, 26]
  V-13: 7
anchor: [3, 10, 19]
coverage:
  web: automated
---

# Permanently Delete atas file yang sudah dihapus permanen oleh aktor lain

## Prerequisites
- Aktor: Total Control. Aktor kedua yang memicu perubahan: Total Control lain di entitas yang sama.
- Layar awal: Settings > File Manager.
- Data:
  - DU-027-1: Aset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-027-2: File di Recycle Bin `damage-race-{runId}.jpg`, Source `Damaged Photo`, Size `150.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-027-3: File di Recycle Bin `damage-1-sebagian-{runId}.jpg`, Source `Damaged Photo`, Size `160.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-027-4: File di Recycle Bin `damage-2-sebagian-{runId}.jpg`, Source `Damaged Photo`, Size `170.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-027-5: File di Recycle Bin `damage-3-sebagian-{runId}.jpg`, Source `Damaged Photo`, Size `180.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-027-6: File di Recycle Bin `damage-1-seluruh-{runId}.jpg`, Source `Damaged Photo`, Size `190.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-027-7: File di Recycle Bin `damage-2-seluruh-{runId}.jpg`, Source `Damaged Photo`, Size `200.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
- Kondisi:
  - Daftar Recycle Bin milik aktor pertama sudah termuat dan tidak dimuat ulang oleh aktor pertama sampai ia mengonfirmasi aksinya.

## Test Steps

### Satu file sudah dihapus permanen saat konfirmasi
1. Klik `Recycle Bin` pada header kartu `Storage Usage`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi file `damage-race-{runId}.jpg` tampil di Recycle Bin
4. Klik `Permanently Delete` pada baris `damage-race-{runId}.jpg`
5. Aktor kedua menghapus permanen file `damage-race-{runId}.jpg` dari Recycle Bin
6. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
7. Verifikasi toast `This file is no longer available.` tampil
8. Verifikasi file `damage-race-{runId}.jpg` tidak tampil lagi di Recycle Bin

### Bulk dengan sebagian item sudah dihapus permanen saat konfirmasi
9. Ganti isi kotak search dengan `sebagian-{runId}`, tekan Enter
10. Verifikasi file `damage-1-sebagian-{runId}.jpg`, `damage-2-sebagian-{runId}.jpg`, dan `damage-3-sebagian-{runId}.jpg` tampil di Recycle Bin
11. Centang baris `damage-1-sebagian-{runId}.jpg`
12. Klik `Select All`
13. Klik `Permanently Delete` pada bar aksi bulk
14. Aktor kedua menghapus permanen file `damage-2-sebagian-{runId}.jpg` dari Recycle Bin
15. Klik `[Permanently Delete]` pada dialog `Permanently Delete Files`
16. Verifikasi toast `Success, file has been permanently deleted. Some items were skipped.` tampil
17. Verifikasi file `damage-1-sebagian-{runId}.jpg`, `damage-2-sebagian-{runId}.jpg`, dan `damage-3-sebagian-{runId}.jpg` tidak tampil lagi di Recycle Bin

### Bulk dengan seluruh item sudah dihapus permanen saat konfirmasi
18. Ganti isi kotak search dengan `seluruh-{runId}`, tekan Enter
19. Verifikasi file `damage-1-seluruh-{runId}.jpg` dan `damage-2-seluruh-{runId}.jpg` tampil di Recycle Bin
20. Centang baris `damage-1-seluruh-{runId}.jpg`
21. Centang baris `damage-2-seluruh-{runId}.jpg`
22. Klik `Permanently Delete` pada bar aksi bulk
23. Aktor kedua menghapus permanen file `damage-1-seluruh-{runId}.jpg` dari Recycle Bin
24. Aktor kedua menghapus permanen file `damage-2-seluruh-{runId}.jpg` dari Recycle Bin
25. Klik `[Permanently Delete]` pada dialog `Permanently Delete Files`
26. Verifikasi toast `This file is no longer available.` tampil
27. Verifikasi file `damage-1-seluruh-{runId}.jpg` dan `damage-2-seluruh-{runId}.jpg` tidak tampil lagi di Recycle Bin
28. Tutup modal `Recycle Bin`

### Aksi atas file yang sudah tidak tersedia tidak menulis log
29. Klik `Changelog` pada header kartu `Storage Usage`
30. Ketik Search `damage-1-seluruh-{runId}.jpg`, tekan Enter
31. Verifikasi Changelog untuk File Name `damage-1-seluruh-{runId}.jpg` memuat tepat satu entri dengan Action `Permanently Delete`
32. Ganti isi kotak search dengan `damage-2-seluruh-{runId}.jpg`, tekan Enter
33. Verifikasi Changelog untuk File Name `damage-2-seluruh-{runId}.jpg` memuat tepat satu entri dengan Action `Permanently Delete`
34. Tutup modal `Changelog`
