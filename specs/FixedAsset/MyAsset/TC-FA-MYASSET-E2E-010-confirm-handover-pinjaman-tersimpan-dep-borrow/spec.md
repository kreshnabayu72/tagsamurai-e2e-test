---
id: TC-FA-MYASSET-E2E-010-confirm-handover-pinjaman-tersimpan-dep-borrow
title: "Confirm Handover pinjaman: aset tercentang menjadi Borrowed dan Task hilang"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-05", "T-MYA-01", "§1.2#r10", "§1.2#r12", "§1.2#r61", "§2.1#r3", "§3#p5", "§4.2.5#p2", "§4.2.5#p3", "§4.4#r3", "§4.4#r38", "§4.8#r2", "§4.8#r3", "§7.3#r1", "§9.2#b1", "§9.2#r1", "§9.4.2#r64", "§9.4.2#r66", "§9.6#r1", "§9.7#r1", "§9.7#r2", "EB-EDG-2", "EB-FB-1@confirm-handover"]
smoke: ["EB-FB-1@confirm-handover"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "FI-05": 31
  "T-MYA-01": [6, 21]
  "§1.2#r10": [4, 6]
  "§1.2#r12": 14
  "§1.2#r61": 18
  "§2.1#r3": 17
  "§3#p5": [17, 31]
  "§4.2.5#p2": 10
  "§4.2.5#p3": 32
  "§4.4#r3": [10, 13, 14]
  "§4.4#r38": 18
  "§4.8#r2": 6
  "§4.8#r3": 8
  "§7.3#r1": [13, 26]
  "§9.2#b1": 6
  "§9.2#r1": [17, 30]
  "§9.4.2#r64": 30
  "§9.4.2#r66": 27
  "§9.6#r1": [13, 14]
  "§9.7#r1": 4
  "§9.7#r2": [14, 31]
  "EB-EDG-2": [13, 26]
  "EB-FB-1@confirm-handover": 13
anchor: []
coverage:
  web: automated
---

# Confirm Handover pinjaman: aset tercentang menjadi Borrowed dan Task hilang

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman. Aktor Borrow pada Group `Head Office` memicu Handover.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-010-1: Pinjaman milik Borrower berstatus `Waiting for Handover` dengan satu aset: Name `Proyektor Epson EB-X06 {runId}`, Asset ID `PRJ-1-{runId}`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Duration `3 days`.
  - DU-010-2: Aset pertama pinjaman multi-aset milik Borrower berstatus `Waiting for Handover`: Name `Laptop Dell Latitude 5420 - 1 {runId}`, Asset ID `LPT-1-{runId}`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Duration `3 days`.
  - DU-010-3: Aset kedua pinjaman yang sama dengan DU-010-2: Name `Laptop Dell Latitude 5420 - 2 {runId}`, Asset ID `LPT-2-{runId}`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Duration `3 days`.
  - DU-010-4: Aset ketiga pinjaman yang sama dengan DU-010-2: Name `Laptop Dell Latitude 5420 - 3 {runId}`, Asset ID `LPT-3-{runId}`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Duration `3 days`.
- Kondisi: Date Format bernilai `dd/MM/yy`. Flag Guided Tooltip My Asset milik Borrower sudah disetel, sehingga Guided Tooltip tidak terbuka otomatis saat My Asset dibuka.

## Test Steps

### Task muncul saat Aktor Borrow memulai Handover
1. Catat jumlah pada badge tab `Task`, dengan badge yang tidak tampil dicatat sebagai `0`
2. Aktor Borrow memulai Handover untuk pinjaman DU-010-1
3. Aktor Borrow memulai Handover untuk pinjaman DU-010-2, DU-010-3, dan DU-010-4 yang berada dalam satu BRW
4. Verifikasi jumlah pada badge tab `Task` bertambah `2` dari jumlah yang dicatat
5. Ketik Search Transaction ID pinjaman DU-010-1, tekan Enter
6. Verifikasi baris Task dengan Task `Confirm Handover` dan Total Asset `1` tampil

### Confirm Handover satu aset: Task hilang dan aset menjadi Borrowed
7. Klik `⋯` pada baris Task pinjaman DU-010-1
8. Verifikasi opsi `Confirm Handover` tersedia pada menu baris
9. Klik `Confirm Handover`
10. Verifikasi dialog `Confirm Handover` tampil dengan aset `Proyektor Epson EB-X06 {runId}` tercentang
11. Catat nilai Return by aset `Proyektor Epson EB-X06 {runId}`
12. Klik `[Confirm]`
13. Verifikasi toast `Success, 1 asset has been handed over.` tampil
14. Verifikasi empty state `No results found` tampil karena baris Task pinjaman DU-010-1 sudah hilang
15. Klik tab `Borrowed`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris `Proyektor Epson EB-X06 {runId}` berstatus `Borrowed`
18. Verifikasi Due Date baris `Proyektor Epson EB-X06 {runId}` sama dengan Return by yang dicatat

### Confirm Handover sebagian: aset tidak tercentang tetap Waiting for Handover
19. Klik tab `Task`
20. Ganti isi kotak search dengan Transaction ID pinjaman DU-010-2, tekan Enter
21. Verifikasi baris Task dengan Task `Confirm Handover` dan Total Asset `3` tampil
22. Klik `⋯` pada baris Task pinjaman DU-010-2
23. Klik `Confirm Handover`
24. Hapus centang aset `Laptop Dell Latitude 5420 - 3 {runId}`
25. Klik `[Confirm]`
26. Verifikasi toast `Success, 2 assets have been handed over.` tampil
27. Verifikasi empty state `No results found` tampil karena baris Task pinjaman DU-010-2 sudah hilang
28. Klik tab `Borrowed`
29. Ganti isi kotak search dengan `{runId}`, tekan Enter
30. Verifikasi baris `Laptop Dell Latitude 5420 - 1 {runId}` dan `Laptop Dell Latitude 5420 - 2 {runId}` berstatus `Borrowed`
31. Verifikasi baris `Laptop Dell Latitude 5420 - 3 {runId}` berstatus `Waiting for Handover`
32. Verifikasi keterangan `Not received` tidak tampil pada baris `Laptop Dell Latitude 5420 - 3 {runId}`
