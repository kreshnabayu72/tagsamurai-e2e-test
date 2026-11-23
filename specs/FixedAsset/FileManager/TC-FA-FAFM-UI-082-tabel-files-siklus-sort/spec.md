---
id: TC-FA-FAFM-UI-082-tabel-files-siklus-sort
title: "Tabel Files: siklus sort tiga klik"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-SRT-3@tabel-files"]
smoke: []
dependsOn: []
trace:
  "EB-SRT-3@tabel-files": [2, 4, 6, 8, 12, 13, 15, 17, 18, 22, 23, 24]
anchor: []
coverage:
  web: automated
---

# Tabel Files: siklus sort tiga klik

## Prerequisites
- Aktor: Total Control.
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-082-1: `laptop-front.jpg`, JPG, Source Asset Photo, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `02/11/26 14:30`.
  - DU-082-2: `monitor-lg-front.png`, PNG, Source Asset Photo, Asset `Monitor LG 24 - 7`, Asset ID `MON-2026-0007`, Group `Branch Bandung`, Size `640.0 KB`, Uploaded By `Dodi P`, Upload Date `05/11/26 09:00`.
  - DU-082-3: `printer-hp-side.jpg`, JPG, Source Asset Photo, Asset `Printer HP M404 - 1`, Asset ID `PRN-2026-0001`, Group `Branch Bandung`, Size `700.0 KB`, Uploaded By `Rina A`, Upload Date `06/11/26 10:30`.
- Kondisi:
  - K1: tab `Asset Photo` aktif; tabel berisi DU-082-1, DU-082-2, dan DU-082-3; belum ada sort yang diklik oleh aktor.

## Test Steps

### Siklus tiga klik pada satu kolom
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi header kolom `File Name` tampil dengan indikator sort netral
3. Klik header kolom `File Name`
4. Verifikasi header kolom `File Name` menampilkan indikator sort naik
5. Klik header kolom `File Name`
6. Verifikasi header kolom `File Name` menampilkan indikator sort turun
7. Klik header kolom `File Name`
8. Verifikasi header kolom `File Name` kembali menampilkan indikator sort netral

### Klik kolom lain memindahkan indikator
9. Tampilkan Tabel File Manager tab Files dengan kondisi K1
10. Klik header kolom `File Name`
11. Klik header kolom `Size`
12. Verifikasi header kolom `Size` menampilkan indikator sort naik
13. Verifikasi header kolom `File Name` menampilkan indikator sort netral
14. Klik header kolom `Size`
15. Verifikasi header kolom `Size` menampilkan indikator sort turun
16. Klik header kolom `File Format`
17. Verifikasi header kolom `File Format` memulai siklus dengan indikator sort naik
18. Verifikasi header kolom `Size` kembali menampilkan indikator sort netral

### Kolom non-sortable tidak punya ikon sort
19. Tampilkan Tabel File Manager tab Files dengan kondisi K1
20. Klik header kolom `File Name`
21. Klik trigger `Column Visibility` pada header kolom Actions
22. Verifikasi header kolom `File Name` tetap menampilkan indikator sort naik setelah trigger diklik
23. Verifikasi header kolom Actions tidak memiliki ikon sort
24. Verifikasi header kolom pemilih baris (checkbox) tidak memiliki ikon sort
