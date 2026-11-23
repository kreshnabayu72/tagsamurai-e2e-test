---
id: TC-FA-FAFM-E2E-044-draft-asset-dep-asset-registration
title: "Aset Draft: foto registrasi dan penghapusan aset Draft"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, F-FAFM-01g, F-FAFM-01i, F-FAFM-05a, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, FAFM-LOGIC-04e, SRC-01, SYN-01b, SYN-01e, SYN-01h, SYN-06b, SYN-06c]
smoke: []
dependsOn: ["Asset Registration: foto registrasi dan penghapusan aset Draft"]
trace:
  ACT-02e: [16, 20]
  ARS-01c: 20
  DIM-14a: 20
  DIM-14b: 21
  F-FAFM-01g: [3, 4, 36]
  F-FAFM-01i: [8, 9, 41, 48]
  F-FAFM-05a: 34
  FAFM-LOGIC-02c: [16, 20]
  FAFM-LOGIC-02e: 20
  FAFM-LOGIC-02f: 21
  FAFM-LOGIC-04e: 34
  SRC-01: [3, 7]
  SYN-01b: 20
  SYN-01e: 20
  SYN-01h: 23
  SYN-06b: 36
  SYN-06c: [34, 36]
anchor: [10, 33, 47]
coverage:
  web: automated
---

# Aset Draft: foto registrasi dan penghapusan aset Draft

## Prerequisites
- Aktor: Total Control; aktor lain yang masuk ke akunnya sendiri: Group Manager `Manajer Pusat {runId}` (group yang dikelola `Head Office`) dan Group Manager `Manajer Bandung {runId}` (group yang dikelola `Branch Bandung`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-044-1: Aset `Laptop Dell Latitude 5420 {runId}`, Status `Active`, Group `Branch Bandung`, ada di entitas aktor; sebelum Active, aset ini berstatus Draft yang dibuat di Group `Head Office` dan fotonya diganti sekali saat registrasi, lalu sesudah Active aset dipindah ke Group `Branch Bandung`.
  - DU-044-2: File `laptop-front-{runId}.jpg`, aktif, foto aktif aset DU-044-1 yang diunggah di field Photo registrasi.
  - DU-044-3: File `laptop-old-{runId}.png`, Source `Asset Photo`, ada di Recycle Bin, Deleted By `System`, diganti saat aset DU-044-1 masih Draft; baris Recycle Bin memuat Asset `—` dan Group `Head Office` sebagai snapshot saat soft-delete.
  - DU-044-4: Aset `Printer Epson L3250 {runId}`, Status `Draft`, Group `Head Office`, ada di entitas aktor.
  - DU-044-5: File `draft-photo-{runId}.jpg`, Size `2.4 MB`, aktif, foto registrasi aset Draft DU-044-4.
  - DU-044-6: File `draft-old-{runId}.png`, Source `Asset Photo`, Size `1.1 MB`, ada di Recycle Bin, Deleted By `System`, diganti saat aset DU-044-4 masih Draft; baris Recycle Bin memuat Asset `—` dan Group `Head Office` sebagai snapshot saat soft-delete.
  - DU-044-7: User `Manajer Pusat {runId}`, role `Group Manager`, group yang dikelola `Head Office`.
  - DU-044-8: User `Manajer Bandung {runId}`, role `Group Manager`, group yang dikelola `Branch Bandung`.

## Test Steps

### File aset Draft tidak didaftar di tab Files
1. Klik tab `Asset Photo`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `laptop-front-{runId}.jpg` milik aset `Laptop Dell Latitude 5420 {runId}` tampil
4. Verifikasi tidak ada baris file `draft-photo-{runId}.jpg` di tab `Asset Photo`

### Baris Recycle Bin file foto yang diganti saat aset Draft memakai snapshot
5. Klik tombol Recycle Bin pada header kartu Storage Usage
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi baris file `laptop-old-{runId}.png` tampil dengan Source `Asset Photo`
8. Verifikasi baris file `laptop-old-{runId}.png` menampilkan Asset `—`
9. Verifikasi baris file `laptop-old-{runId}.png` menampilkan Group `Head Office`
10. Verifikasi baris file `draft-old-{runId}.png` tampil di Recycle Bin
11. Tutup modal Recycle Bin

### Delete foto registrasi mengosongkan foto aset tanpa mengubah statusnya
12. Klik aksi Delete pada baris file `laptop-front-{runId}.jpg`
13. Klik `[Delete]` pada dialog Delete File
14. Klik tombol Recycle Bin pada header kartu Storage Usage
15. Ketik Search `laptop-front-{runId}.jpg`, tekan Enter
16. Verifikasi baris file `laptop-front-{runId}.jpg` tampil di Recycle Bin
17. Tutup modal Recycle Bin
18. Buka menu Asset
19. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
20. Verifikasi kolom Photo aset `Laptop Dell Latitude 5420 {runId}` menampilkan `Gambar placeholder generik`
21. Verifikasi Status aset `Laptop Dell Latitude 5420 {runId}` tetap `Active`
22. Buka Changelog aset `Laptop Dell Latitude 5420 {runId}`
23. Verifikasi entri dengan Action `Edit`, Old Value `laptop-front-{runId}.jpg`, dan New Value `—` tampil
24. Tutup Changelog aset

### Penghapusan aset Draft memicu cascade purge atas file aset itu
25. Buka Settings > File Manager
26. Catat nilai `Fixed Asset` pada kartu Storage Usage
27. Hapus aset Draft `Printer Epson L3250 {runId}` di Asset Registration
28. Konfirmasi penghapusan aset Draft
29. Cascade purge atas file aset Draft `Printer Epson L3250 {runId}` selesai
30. Muat ulang halaman
31. Klik tombol Recycle Bin pada header kartu Storage Usage
32. Ketik Search `{runId}`, tekan Enter
33. Verifikasi baris file `laptop-old-{runId}.png` tetap tampil di Recycle Bin
34. Verifikasi tidak ada baris file `draft-old-{runId}.png` di Recycle Bin
35. Tutup modal Recycle Bin
36. Verifikasi nilai `Fixed Asset` pada kartu Storage Usage lebih kecil dari nilai yang dicatat pada langkah 26

### Lingkup aktor baris Recycle Bin mengikuti Group snapshot
37. Logout dari akun aktor
38. Login sebagai Group Manager `Manajer Pusat {runId}` dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
39. Klik tombol Recycle Bin pada header kartu Storage Usage
40. Ketik Search `{runId}`, tekan Enter
41. Verifikasi baris file `laptop-old-{runId}.png` dengan Group snapshot `Head Office` tampil di Recycle Bin untuk Group Manager group `Head Office`
42. Tutup modal Recycle Bin
43. Logout dari akun aktor
44. Login sebagai Group Manager `Manajer Bandung {runId}` dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
45. Klik tombol Recycle Bin pada header kartu Storage Usage
46. Ketik Search `{runId}`, tekan Enter
47. Verifikasi baris file `laptop-front-{runId}.jpg` tampil di Recycle Bin
48. Verifikasi baris file `laptop-old-{runId}.png` dengan Group snapshot `Head Office` tidak ada di Recycle Bin untuk Group Manager group `Branch Bandung`
49. Tutup modal Recycle Bin
