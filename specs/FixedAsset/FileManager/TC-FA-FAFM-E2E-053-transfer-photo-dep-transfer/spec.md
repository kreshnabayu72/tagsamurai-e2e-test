---
id: TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer
title: "Send Photo, Receive Photo, dan perpindahan group aset pada Transfer"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, EC-14, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-13, SRC-14, SYN-01b, SYN-01e, SYN-01h, SYN-07a, SYN-07b, SYN-07c, SYN-07d, "§9.4.1#r13"]
smoke: []
dependsOn: ["Transfer: foto Send dan Receive serta perpindahan group aset"]
trace:
  ACT-02e: [32, 35]
  ARS-01c: 35
  DIM-14a: 35
  DIM-14b: 37
  EC-14: [12, 15, 19, 20]
  FAFM-LOGIC-02c: [32, 35]
  FAFM-LOGIC-02e: 35
  FAFM-LOGIC-02f: 37
  SRC-13: [3, 22, 35]
  SRC-14: [16, 23, 36]
  SYN-01b: 35
  SYN-01e: 35
  SYN-01h: 39
  SYN-07a: 15
  SYN-07b: 15
  SYN-07c: [19, 20]
  SYN-07d: 15
  "§9.4.1#r13": [15, 18]
anchor: [4, 5]
coverage:
  web: automated
---

# Send Photo, Receive Photo, dan perpindahan group aset pada Transfer

## Prerequisites
- Aktor: Group Manager atas group `Head Office` beserta descendant `Fleet`; aktor pemicu: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-053-1: Aset `Server Dell R750 {runId}`, Group `Head Office`, ada di entitas aktor.
  - DU-053-2: Aset `Printer Zebra ZT230 {runId}`, Group `Head Office`, ada di entitas aktor.
  - DU-053-3: Transaksi Transfer aset DU-053-1 yang sudah Send ke group `Fleet` dan belum selesai.
  - DU-053-4: Transaksi Transfer aset DU-053-2 yang sudah Send ke group `Branch Bandung` dan belum selesai.
  - DU-053-5: File `send-x-{runId}.jpg`, Source `Send Photo`, Reference ID transaksi DU-053-3, aktif, Send Photo transaksi DU-053-3.
  - DU-053-6: File `send-y-{runId}.jpg`, Source `Send Photo`, Reference ID transaksi DU-053-4, aktif, Send Photo transaksi DU-053-4.
  - DU-053-7: File `recv-x-{runId}.jpg`, Source `Receive Photo`, Reference ID transaksi DU-053-3, dipilih saat Transfer DU-053-3 diselesaikan.
  - DU-053-8: File `recv-y-{runId}.jpg`, Source `Receive Photo`, Reference ID transaksi DU-053-4, dipilih saat Transfer DU-053-4 diselesaikan.

## Test Steps

### Send Photo terdaftar di tab Transfer pada group asal
1. Klik tab `Transfer`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `send-x-{runId}.jpg` tampil dengan Source `Send Photo`
4. Verifikasi baris file `send-x-{runId}.jpg` menampilkan Group `Head Office`
5. Verifikasi baris file `send-y-{runId}.jpg` menampilkan Group `Head Office`
6. Catat nilai Uploaded By baris file `send-x-{runId}.jpg`
7. Catat Reference baris file `send-x-{runId}.jpg`

### Transfer diselesaikan aktor lain, lalu aktor yang kehilangan scope mendapat pesan file tidak tersedia saat aksi
8. Total Control menyelesaikan Transfer aset `Server Dell R750 {runId}` ke group `Fleet` dengan Receive Photo `recv-x-{runId}.jpg`
9. Total Control menyelesaikan Transfer aset `Printer Zebra ZT230 {runId}` ke group `Branch Bandung` dengan Receive Photo `recv-y-{runId}.jpg`
10. Klik aksi Delete pada baris file `send-y-{runId}.jpg`
11. Klik `[Delete]` pada dialog Delete File
12. Verifikasi toast `This file is no longer available.` tampil

### File mengikuti group terkini dan file di luar scope tidak tampil
13. Muat ulang halaman
14. Ganti isi kotak Search dengan `{runId}`, tekan Enter
15. Verifikasi baris file `send-x-{runId}.jpg` menampilkan Group `Fleet`
16. Verifikasi baris file `recv-x-{runId}.jpg` tampil dengan Source `Receive Photo`
17. Catat Reference baris file `recv-x-{runId}.jpg`
18. Verifikasi Uploaded By baris file `send-x-{runId}.jpg` sama dengan nilai yang dicatat pada langkah 6
19. Verifikasi tidak ada baris file `send-y-{runId}.jpg` di tab `Transfer`
20. Verifikasi tidak ada baris file `recv-y-{runId}.jpg` di tab `Transfer`

### Delete Send Photo mengosongkan field tanpa mengubah transaksi
21. Buka transaksi Transfer aset `Server Dell R750 {runId}`
22. Verifikasi ID transaksi Transfer yang dibuka sama dengan Reference yang dicatat dari baris file `send-x-{runId}.jpg`
23. Verifikasi ID transaksi Transfer yang dibuka sama dengan Reference yang dicatat dari baris file `recv-x-{runId}.jpg`
24. Catat Status transaksi Transfer
25. Buka Settings > File Manager
26. Klik tab `Transfer`
27. Ketik Search `send-x-{runId}.jpg`, tekan Enter
28. Klik aksi Delete pada baris file `send-x-{runId}.jpg`
29. Klik `[Delete]` pada dialog Delete File
30. Klik tombol Recycle Bin pada header kartu Storage Usage
31. Ketik Search `send-x-{runId}.jpg`, tekan Enter
32. Verifikasi baris file `send-x-{runId}.jpg` tampil di Recycle Bin
33. Tutup modal Recycle Bin
34. Buka transaksi Transfer aset `Server Dell R750 {runId}`
35. Verifikasi field Send Photo pada transaksi Transfer menampilkan `—`
36. Verifikasi field Receive Photo pada transaksi Transfer tetap menampilkan file `recv-x-{runId}.jpg`
37. Verifikasi Status transaksi Transfer sama dengan nilai yang dicatat pada langkah 24
38. Buka Changelog transaksi Transfer aset `Server Dell R750 {runId}`
39. Verifikasi entri dengan Action `Edit`, Old Value `send-x-{runId}.jpg`, dan New Value `—` tampil
40. Tutup Changelog transaksi Transfer
