---
id: TC-FA-ASTL-BE-091-query-search-sort-filter
title: "Search, Sort, dan Filter server"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-SRC-1, EB-FLT-3, EB-SRT-1, EB-SRT-2]
smoke: []
dependsOn: []
trace:
  EB-SRC-1: [2, 4, 6]
  EB-FLT-3: [8, 10]
  EB-SRT-1: [13, 15, 18, 20]
  EB-SRT-2: [16, 22, 24]
anchor: []
---

# Search, Sort, dan Filter server

## Prerequisites
- Aktor: Total Control (Hendra).
- Data:
  - DU-091-1: User, total Control seluruh client: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-091-2: Group, tiga group tanpa induk: Name `IT {runId}`, Group kedua `GA {runId}`, Group ketiga `Cabang Bandung {runId}`.
  - DU-091-3: Asset, aset huruf kecil pertama dengan Purchase Cost 18,5 juta: Name `kamera CCTV - T1 {runId}`, Group `IT {runId}`, Status `Available`, Purchase Cost `Rp 18.500.000,00`, Purchase Date `T0 - 30 hari`, Warranty Expiry `T0 + 100 hari`.
  - DU-091-4: Asset, aset Damaged dengan Purchase Cost 9 juta: Name `Kursi Kerja - T2 {runId}`, Group `IT {runId}`, Status `Damaged`, Purchase Cost `Rp 9.000.000,00`, Purchase Date `T0 - 10 hari`, Warranty Expiry `T0 + 300 hari`.
  - DU-091-5: Asset, aset Damaged di GA dengan Purchase Cost 18,5 juta: Name `Laptop Pro 16 - T3 {runId}`, Group `GA {runId}`, Status `Damaged`, Purchase Cost `Rp 18.500.000,00`, Purchase Date `T0 - 20 hari`, Warranty Expiry `T0 + 200 hari`.
  - DU-091-6: Asset, aset Damaged di cabang tanpa Asset Class: Name `Meja Rapat - T4 {runId}`, Group `Cabang Bandung {runId}`, Status `Damaged`, Purchase Cost `Rp 2.000.000,00`, Purchase Date `T0 - 5 hari`, Warranty Expiry `kosong`.

## Test Steps

### Search mencocokkan substring tanpa membedakan huruf besar-kecil
1. Hendra mencari `KAMERA CCTV - T1 {runId}`
2. Verifikasi hasil pencarian memuat `kamera CCTV - T1 {runId}` walau huruf besar-kecilnya berbeda
3. Hendra mencari `era CCTV - T1 {runId}`
4. Verifikasi hasil pencarian memuat `kamera CCTV - T1 {runId}` karena kata kunci cocok sebagai substring di tengah nama
5. Hendra mencari `Zebra Tidak Ada {runId}`
6. Verifikasi hasil pencarian tidak memuat baris apa pun dan menampilkan `No results found`

### Filter menggabungkan antar-field dengan AND dan dalam satu field dengan OR
7. Hendra memfilter Group `IT {runId}` atau `GA {runId}`
8. Verifikasi hasil filter memuat `kamera CCTV - T1 {runId}`, `Kursi Kerja - T2 {runId}`, dan `Laptop Pro 16 - T3 {runId}`, dan tidak memuat `Meja Rapat - T4 {runId}`
9. Hendra menambahkan filter Status `Damaged` pada filter Group tersebut
10. Verifikasi hasil filter memuat `Kursi Kerja - T2 {runId}` dan `Laptop Pro 16 - T3 {runId}`, dan tidak memuat `kamera CCTV - T1 {runId}` karena Status-nya bukan `Damaged`

### Sort menurut tipe data
11. Hendra mencari `{runId}`
12. Hendra mengurutkan kolom Asset Name secara ascending
13. Verifikasi urutan nama adalah `kamera CCTV - T1 {runId}`, `Kursi Kerja - T2 {runId}`, `Laptop Pro 16 - T3 {runId}`, lalu `Meja Rapat - T4 {runId}`, sehingga huruf besar-kecil tidak memengaruhi urutan
14. Hendra mengurutkan kolom Purchase Cost secara ascending
15. Verifikasi urutan memuat `Meja Rapat - T4 {runId}` (`Rp 2.000.000,00`), `Kursi Kerja - T2 {runId}` (`Rp 9.000.000,00`), lalu dua baris `Rp 18.500.000,00`, sehingga angka diurutkan menurut nilainya
16. Verifikasi dua baris `Rp 18.500.000,00` berurutan `kamera CCTV - T1 {runId}` lalu `Laptop Pro 16 - T3 {runId}` menurut default sort Name A-Z
17. Hendra mengurutkan kolom Purchase Date secara ascending
18. Verifikasi urutan Oldest First adalah `kamera CCTV - T1 {runId}`, `Laptop Pro 16 - T3 {runId}`, `Kursi Kerja - T2 {runId}`, lalu `Meja Rapat - T4 {runId}`
19. Hendra mengurutkan kolom Purchase Date secara descending
20. Verifikasi urutan Newest First adalah `Meja Rapat - T4 {runId}`, `Kursi Kerja - T2 {runId}`, `Laptop Pro 16 - T3 {runId}`, lalu `kamera CCTV - T1 {runId}`

### Nilai kosong di akhir saat ascending dan di awal saat descending
21. Hendra mengurutkan kolom Warranty Expiry secara ascending
22. Verifikasi baris `Meja Rapat - T4 {runId}` yang Warranty Expiry-nya kosong berada paling akhir
23. Hendra mengurutkan kolom Warranty Expiry secara descending
24. Verifikasi baris `Meja Rapat - T4 {runId}` yang Warranty Expiry-nya kosong berada paling awal
