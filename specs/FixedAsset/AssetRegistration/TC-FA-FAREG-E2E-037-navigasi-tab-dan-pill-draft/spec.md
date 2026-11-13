---
id: TC-FA-FAREG-E2E-037-navigasi-tab-dan-pill-draft
title: "Tab Registration: jumlah pada pill Draft mengikuti data"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#p3"]
smoke: []
dependsOn: []
trace:
  "§4.1#p3": [4, 5, 10, 11, 24, 29, 36, 37]
anchor: [2, 35]
coverage:
  web: automated
---

# Tab Registration: jumlah pada pill Draft mengikuti data

## Prerequisites
- Aktor: `Wulan S {runId}` (DU-037-6), Group Manager Group `Wilayah Selatan {runId}`, cakupan Group itu beserta sub-group. Total Control memicu perubahan di langkah 33 (aktor pemicu, bukan aktor yang diuji).
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-037-1: Batch Draft dengan Group `Gudang Kemang {runId}` (sub-group `Wilayah Selatan {runId}`), Origin `—`, Total Asset `8`, Progress `50%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, ada di cakupan aktor.
  - DU-037-2: Batch Draft dengan Group `Gudang Tebet {runId}` (sub-group `Wilayah Selatan {runId}`), Origin `—`, Total Asset `15`, Progress `100%`, Requested By `Agus P`, Last Updated `T0 − 2 hari`, ada di cakupan aktor.
  - DU-037-3: Group `Gudang Cikini {runId}`, sub-group `Wilayah Selatan {runId}`, node Assignable dan bukan Excess, ada di cakupan aktor.
  - DU-037-4: Master Asset Name `Laptop Draft {runId}`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`.
  - DU-037-7: Group `Wilayah Selatan {runId}`, node induk dari `Gudang Kemang {runId}`, `Gudang Tebet {runId}`, dan `Gudang Cikini {runId}`.
  - DU-037-8: Group `Gudang Pluit {runId}`, node Assignable, bukan sub-group `Wilayah Selatan {runId}`, sehingga di luar cakupan aktor.
  - Rina W dan Agus P adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.

## Test Steps

### Jumlah pada pill Draft tidak mengikuti Search
1. Catat jumlah pada judul pill `Draft` sebagai jumlah awal
2. Verifikasi tabel sub tab Draft memuat baris `Gudang Kemang {runId}` dan baris `Gudang Tebet {runId}`
3. Ketik Search `Gudang Kemang {runId}`, tekan Enter
4. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Kemang {runId}` dan tidak memuat baris `Gudang Tebet {runId}`
5. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah awal
6. Klik `(←)` pada kotak Search

### Jumlah pada pill Draft tidak mengikuti Filter
7. Klik ikon Filter
8. Pilih Group `Gudang Tebet {runId}` pada field `Group`
9. Klik `[Apply]`
10. Verifikasi tabel sub tab Draft memuat baris `Gudang Tebet {runId}` dan tidak memuat baris `Gudang Kemang {runId}`
11. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah awal

### Jumlah pada pill Draft bertambah satu setelah Draft dibuat
12. Klik ikon Filter
13. Klik `[Clear Field]`
14. Klik `[Apply]`
15. Catat jumlah pada judul pill `Draft` sebagai jumlah sebelum Draft dibuat
16. Klik `[+ Register Asset]`
17. Pilih Group `Gudang Cikini {runId}`
18. Pilih Asset Name `Laptop Draft {runId}` pada Item 1
19. Pilih Brand `Dell` pada Item 1
20. Pilih Model `Latitude 5440` pada Item 1
21. Isi Quantity Item 1 dengan `2`
22. Klik `[Save draft]`
23. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)
24. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah sebelum Draft dibuat ditambah 1

### Jumlah pada pill Draft berkurang satu setelah Draft dihapus
25. Catat jumlah pada judul pill `Draft` sebagai jumlah sebelum Draft dihapus
26. Ketik Search `Gudang Tebet {runId}`, tekan Enter
27. Klik ikon `Delete` pada baris `Gudang Tebet {runId}`
28. Klik `[Delete]` pada dialog `Delete Draft`
29. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah sebelum Draft dihapus dikurangi 1
30. Klik `(←)` pada kotak Search

### Draft di luar cakupan Group tidak ikut terhitung pada pill Draft
31. Catat jumlah pada judul pill `Draft` sebagai jumlah sebelum Draft di luar cakupan dibuat
32. Muat ulang halaman
33. Total Control menyimpan Draft untuk Group `Gudang Pluit {runId}` dengan Asset Name `Laptop Draft {runId}`, Brand `Dell`, Model `Latitude 5440`, Quantity `1` (DU-037-9)
34. Muat ulang halaman
35. Verifikasi tabel sub tab Draft memuat baris `Gudang Kemang {runId}`
36. Verifikasi baris `Gudang Pluit {runId}` tidak tampil di tabel sub tab Draft
37. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah sebelum Draft di luar cakupan dibuat
