---
id: TC-FA-FAFM-E2E-040-android-recycle-bin-bottom-sheet
title: "Mobile: Recycle Bin sebagai bottom sheet"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-03"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-03": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30]
anchor: []
coverage:
  android: automated
---

# Mobile: Recycle Bin sebagai bottom sheet

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-040-1: Asset `Laptop Dell Latitude {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-040-2: File di Recycle Bin `laptop-old-{runId}.png`, Source `Asset Photo`, Category `Asset Photo`, Size `1.0 MB` dari 1048576 byte, Deleted Date `T0 − 2 hari`, Deleted By `System`, Auto-Purge In `28 days` dari retensi 30 hari dikurangi 2 hari, milik DU-040-1.
  - DU-040-3: Asset `Toyota Avanza {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-040-4: File di Recycle Bin `damage-01-{runId}.jpg`, Source `Damaged Photo`, Category `Damaged`, Size `900.0 KB` dari 921600 byte, Deleted Date `T0 − 5 hari`, Deleted By `System`, Auto-Purge In `25 days` dari retensi 30 hari dikurangi 5 hari, milik DU-040-3.
  - DU-040-5: File di Recycle Bin `repair-02-{runId}.jpg`, Source `Repair Photo`, Category `Damaged`, Size `880.0 KB` dari 901120 byte, Deleted Date `T0 − 28 hari`, Deleted By `System`, Auto-Purge In `2 days` dari retensi 30 hari dikurangi 28 hari, milik DU-040-3.
  - DU-040-6: Asset `Printer HP M404 {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-040-7: File di Recycle Bin `maint-before-{runId}.jpg`, Source `Maintenance Before Photo`, Category `Maintenance`, Size `750.0 KB` dari 768000 byte, Deleted Date `T0 − 29 hari`, Deleted By `System`, Auto-Purge In `1 day` dari retensi 30 hari dikurangi 29 hari, milik DU-040-6.
  - Urutan Deleted Date dari yang terbaru: DU-040-2, DU-040-4, DU-040-5, DU-040-7.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.

## Test Steps

### Recycle Bin dibuka dan kartu file tampil
1. Ketuk ikon dengan label aksesibel `Recycle Bin` pada header kartu Storage Usage
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi isi Recycle Bin tampil sebagai Card List di dalam bottom sheet

### Isi kartu foto aset yang diganti
4. Verifikasi kartu `laptop-old-{runId}.png` tampil
5. Verifikasi kartu `laptop-old-{runId}.png` menampilkan Source `Asset Photo`
6. Verifikasi kartu `laptop-old-{runId}.png` menampilkan Asset milik DU-040-1
7. Verifikasi kartu `laptop-old-{runId}.png` menampilkan Size `1.0 MB`
8. Verifikasi kartu `laptop-old-{runId}.png` menampilkan Auto-Purge In `28 days`

### Isi kartu foto kerusakan
9. Verifikasi kartu `damage-01-{runId}.jpg` tampil
10. Verifikasi kartu `damage-01-{runId}.jpg` menampilkan Source `Damaged Photo`
11. Verifikasi kartu `damage-01-{runId}.jpg` menampilkan Asset milik DU-040-3
12. Verifikasi kartu `damage-01-{runId}.jpg` menampilkan Size `900.0 KB`
13. Verifikasi kartu `damage-01-{runId}.jpg` menampilkan Auto-Purge In `25 days`

### Isi kartu foto perbaikan dan foto maintenance
14. Verifikasi kartu `repair-02-{runId}.jpg` tampil
15. Verifikasi kartu `repair-02-{runId}.jpg` menampilkan Source `Repair Photo`
16. Verifikasi kartu `repair-02-{runId}.jpg` menampilkan Size `880.0 KB`
17. Verifikasi kartu `repair-02-{runId}.jpg` menampilkan Auto-Purge In `2 days`
18. Verifikasi kartu `maint-before-{runId}.jpg` tampil
19. Verifikasi kartu `maint-before-{runId}.jpg` menampilkan Source `Maintenance Before Photo`
20. Verifikasi kartu `maint-before-{runId}.jpg` menampilkan Asset milik DU-040-6
21. Verifikasi kartu `maint-before-{runId}.jpg` menampilkan Auto-Purge In `1 day`

### Urutan default kartu menurut Deleted Date
22. Verifikasi urutan kartu dari atas ke bawah: `laptop-old-{runId}.png`, `damage-01-{runId}.jpg`, `repair-02-{runId}.jpg`, `maint-before-{runId}.jpg`

### Search menyaring kartu Recycle Bin
23. Ganti isi kotak Search dengan `Toyota Avanza {runId}`, tekan Enter
24. Verifikasi kartu `damage-01-{runId}.jpg` tampil
25. Verifikasi kartu `repair-02-{runId}.jpg` tampil
26. Verifikasi kartu `laptop-old-{runId}.png` tidak tampil
27. Verifikasi kartu `maint-before-{runId}.jpg` tidak tampil

### File Name pada kartu membuka File Preview
28. Ketuk File Name `damage-01-{runId}.jpg` pada kartunya
29. Verifikasi File Preview untuk `damage-01-{runId}.jpg` tampil sebagai bottom sheet berjudul `File Preview`
30. Verifikasi bottom sheet menampilkan nama file `damage-01-{runId}.jpg`
