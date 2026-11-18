---
id: TC-FA-ASTL-E2E-003-sidebar-group
title: "Sidebar Group membatasi tabel ke group dan descendant"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-14a, ASTL-LOGIC-14d, ASTL-LOGIC-14e, ASTL-LOGIC-14g, ASTL-LOGIC-14j, ASTL-LOGIC-14k, ASTL-LOGIC-14l, ASTL-LOGIC-14n, F-ASTL-13]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-14a: 3
  ASTL-LOGIC-14d: [9, 11]
  ASTL-LOGIC-14e: [4, 14]
  ASTL-LOGIC-14g: [3, 41, 42, 43]
  ASTL-LOGIC-14j: 5
  ASTL-LOGIC-14k: [21, 22, 24, 28, 30, 48, 49, 51]
  ASTL-LOGIC-14l: [16, 18]
  ASTL-LOGIC-14n: [35, 37, 39]
  F-ASTL-13: [9, 12]
anchor: [8]
coverage:
  web: automated
---

# Sidebar Group membatasi tabel ke group dan descendant

## Prerequisites
- Aktor: Group Manager `Rina Wulandari {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-003-1: User `Rina Wulandari {runId}`, role Group Manager, cakupan group `Operasional {runId}` dan descendant-nya.
  - DU-003-2: Group `Kantor Pusat {runId}` dengan dua anak, `Operasional {runId}` dan `Keuangan {runId}`; `Operasional {runId}` punya anak `Gudang {runId}`.
  - DU-003-3: 11 aset `Rak Besi - {n} {runId}` dengan `n` dari 1 sampai 11, di group `Gudang {runId}`, berstatus `Available`.
  - DU-003-4: Aset `Meja Operasional - 1 {runId}` di group `Operasional {runId}`, berstatus `Available`.
  - DU-003-5: Aset `Forklift - 1 {runId}` di group `Operasional {runId}`, Custody `Borrowed`.
  - DU-003-6: Aset `Brankas - 1 {runId}` di group `Keuangan {runId}`, berstatus `Available`.
  - Dengan Search memakai runId spec ini dalam cakupan `Rina Wulandari {runId}` (DU-003-3 sampai DU-003-5, tanpa DU-003-6), kartu `All` `13` dan kartu `In Transaction` `1`; untuk node `Gudang {runId}`, kartu `All` `11` dan kartu `In Transaction` `0`.
- Kondisi:
  - Akun `Rina Wulandari {runId}` aktif dan kredensialnya tersedia.

## Test Steps

### Sidebar memuat hierarki dalam cakupan user
1. Masuk sebagai `Rina Wulandari {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Verifikasi sidebar Group menampilkan node akar `All Groups`
4. Verifikasi sidebar Group memuat `Operasional {runId}` dan `Gudang {runId}`
5. Verifikasi sidebar Group tidak memuat `Keuangan {runId}` yang berada di luar cakupan dan bukan leluhur dari group dalam cakupan

### Memilih node membatasi tabel ke group itu dan descendant-nya
6. Ketik Search `{runId}`, tekan Enter
7. Klik node `Gudang {runId}`
8. Verifikasi tabel memuat `Rak Besi - 1 {runId}`
9. Verifikasi node `Gudang {runId}` terpilih dan tabel tidak memuat `Meja Operasional - 1 {runId}`
10. Klik node `Operasional {runId}`
11. Verifikasi tabel memuat `Meja Operasional - 1 {runId}` dan `Rak Besi - 1 {runId}` dari group descendant `Gudang {runId}`
12. Verifikasi node `Gudang {runId}` tidak lagi terpilih karena pilihan hanya satu
13. Klik node `All Groups`
14. Verifikasi tabel tidak memuat `Brankas - 1 {runId}`

### Angka kartu mengikuti group terpilih
15. Klik node `Operasional {runId}`
16. Verifikasi kartu `All` berjumlah `13` dan kartu `In Transaction` berjumlah `1`
17. Klik node `Gudang {runId}`
18. Verifikasi kartu `All` berjumlah `11` dan kartu `In Transaction` berjumlah `0`

### Node berlaku bersamaan dengan kartu dan Search
19. Klik node `Operasional {runId}`
20. Klik kartu `In Transaction`
21. Verifikasi tabel memuat `Forklift - 1 {runId}`
22. Verifikasi tabel tidak memuat `Meja Operasional - 1 {runId}`
23. Klik node `Gudang {runId}`
24. Verifikasi tabel menampilkan empty state `No results found`
25. Klik kartu `All`
26. Ganti isi kotak search dengan `Forklift - 1 {runId}`, tekan Enter
27. Klik node `Operasional {runId}`
28. Verifikasi tabel memuat `Forklift - 1 {runId}`
29. Klik node `Gudang {runId}`
30. Verifikasi tabel menampilkan empty state `No results found`

### Memilih node memuat ulang tabel dari halaman 1 dan mempertahankan seleksi baris
31. Ganti isi kotak search dengan `{runId}`, tekan Enter
32. Klik node `Operasional {runId}`
33. Centang baris `Rak Besi - 1 {runId}`
34. Klik tombol halaman `2`
35. Verifikasi tombol halaman `2` aktif
36. Klik node `Gudang {runId}`
37. Verifikasi tombol halaman `1` aktif sesudah memilih node
38. Klik node `Operasional {runId}`
39. Verifikasi baris `Rak Besi - 1 {runId}` tetap tercentang

### Node All Groups memuat seluruh cakupan user
40. Klik node `All Groups`
41. Verifikasi tabel memuat `Meja Operasional - 1 {runId}` dan `Forklift - 1 {runId}` dari group `Operasional {runId}`
42. Verifikasi tabel memuat `Rak Besi - 1 {runId}` dari group `Gudang {runId}`
43. Verifikasi kartu `All` berjumlah `13`

### Node berlaku bersamaan dengan filter di Filter Panel
44. Klik node `Operasional {runId}`
45. Klik ikon Filter
46. Pilih Status `Borrowed` pada Filter Panel
47. Klik `[Apply]`
48. Verifikasi tabel memuat `Forklift - 1 {runId}`
49. Verifikasi tabel tidak memuat `Meja Operasional - 1 {runId}`
50. Klik node `Gudang {runId}`
51. Verifikasi tabel menampilkan empty state `No results found`
52. Klik `[Clear Field]`
53. Klik `[Apply]`
