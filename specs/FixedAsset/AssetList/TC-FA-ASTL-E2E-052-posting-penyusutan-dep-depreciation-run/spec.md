---
id: TC-FA-ASTL-E2E-052-posting-penyusutan-dep-depreciation-run
title: "Posting penyusutan tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-12c", "ASTL-LOGIC-12d", "ASTL-LOGIC-12e", "ASTL-LOGIC-12g", "ASTL-LOGIC-12h", "ASTL-LOGIC-12r", "ASTL-LOGIC-12f", "ASTL-LOGIC-12n", "ASTL-LOGIC-17l", "§9.7#r9"]
smoke: []
dependsOn: ["Depreciation Run: posting periode penyusutan"]
trace:
  "ASTL-LOGIC-12c": 8
  "ASTL-LOGIC-12d": 12
  "ASTL-LOGIC-12e": 14
  "ASTL-LOGIC-12g": [22, 23, 40, 41, 44]
  "ASTL-LOGIC-12h": 10
  "ASTL-LOGIC-12r": [15, 17, 19, 40, 41, 44]
  "ASTL-LOGIC-12f": 9
  "ASTL-LOGIC-12n": 6
  "ASTL-LOGIC-17l": 29
  "§9.7#r9": [8, 29, 36]
anchor: [16, 27]
coverage:
  web: automated
---

# Posting penyusutan tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-052-1: aset `Laptop Pro 16 {runId} - 1`, Group `IT`, Purchase Cost `Rp 18.000.000,00` dari `18000000`, belum punya periode Posted pada kedua buku; akumulasi penyusutan periode pertama `Rp 300.000,00` pada buku Commercial dan `Rp 600.000,00` pada buku Fiscal.
  - DU-052-2: aset `Server Rack {runId} - 1`, Group `IT`, Purchase Cost `Rp 60.000.000,00` dari `60000000`, metode penyusutan berbeda dari `Laptop Pro 16 {runId} - 1`; akumulasi penyusutan periode pertama `Rp 1.000.000,00` pada buku Commercial dan `Rp 2.000.000,00` pada buku Fiscal.
  - DU-052-3: aset `Genset 20kVA {runId} - 1`, Group `Cabang Medan`, Lifecycle `Disposed`, berjejak Posted, jurnal pelepasan sudah Posted.
  - DU-052-4: aset `Meja Rapat {runId} - 1`, Group `GA`, Lifecycle `Disposed`, Purchase Cost `Rp 12.000.000,00` dari `12000000`, akumulasi penyusutan Posted `Rp 2.000.000,00` pada kedua buku, jurnal pelepasan belum Posted.
  - DU-052-5: aset `Mobil Operasional {runId} - 1`, Group `GA`, Condition `Reported Disposal`, Purchase Cost `Rp 30.000.000,00` dari `30000000`, akumulasi penyusutan Posted `Rp 1.000.000,00` pada kedua buku.
  - DU-052-6: aset `Kursi Kerja {runId} - 1`, Group `GA`, Lifecycle `Disposed`, Purchase Cost belum diisi, jurnal pelepasan sudah Posted.
  - DU-052-7: aset `Lemari Besi {runId} - 1`, Group `GA`, Lifecycle `Disposed`, Purchase Cost `Rp 5.000.000,00` dari `5000000`, Asset Name tanpa Asset Class, jurnal pelepasan sudah Posted.

## Test Steps

### Buku tanpa periode Posted menampilkan harga perolehan
1. Ketik Search `{runId}`, tekan Enter
2. Buka Setup Column
3. Centang `Asset Value (Commercial)`
4. Centang `Asset Value (Fiscal)`
5. Tutup Setup Column
6. Verifikasi kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` baris `Laptop Pro 16 {runId} - 1` menampilkan harga perolehan `Rp 18.000.000,00`, bukan `—`

### Posting periode menghitung nilai buku per periode Posted terakhir
7. Pada modul Depreciation Run, Hendra Saputra memposting periode penyusutan pertama, tanpa memuat ulang halaman Fixed Asset > Assets
8. Verifikasi kolom `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 17.700.000,00`, yaitu harga perolehan dikurangi akumulasi penyusutan sampai periode Posted terakhir
9. Verifikasi kolom `Asset Value (Fiscal)` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 17.400.000,00` menurut aturan yang sama dengan kolom Commercial
10. Verifikasi baris `Server Rack {runId} - 1` menampilkan `Rp 59.000.000,00` pada kolom Commercial dan `Rp 58.000.000,00` pada kolom Fiscal, sehingga metode berbeda antar baris dalam satu kolom
11. Periode penyusutan berikutnya berjalan tetapi belum Posted
12. Verifikasi kolom `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1` tetap `Rp 17.700.000,00` karena periode yang belum Posted tidak dihitung
13. Pada modul Depreciation Run, Hendra Saputra memposting Value Change sebesar `Rp 200.000,00` atas `Laptop Pro 16 {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
14. Verifikasi kolom `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 17.500.000,00` dan kolom `Asset Value (Fiscal)` menampilkan `Rp 17.200.000,00`, sesuai nilai buku yang sudah memperhitungkan Value Change Posted

### Aset Disposed dan Reported Disposal pada Asset Value
15. Verifikasi baris `Genset 20kVA {runId} - 1` menampilkan `Rp 0,00` pada kedua kolom buku
16. Verifikasi baris `Meja Rapat {runId} - 1` menampilkan `Rp 10.000.000,00` pada kedua kolom buku
17. Verifikasi baris `Mobil Operasional {runId} - 1` (Reported Disposal) menampilkan `Rp 29.000.000,00` pada kedua kolom buku mengikuti nilai buku periode Posted terakhir
18. Arahkan kursor ke sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1`
19. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `Pending` dengan tooltip `Purchase cost has not been set.`, didahulukan atas `Rp 0,00`

### Periode Posted terakhir tidak terbaca
20. Nilai periode Posted terakhir `Laptop Pro 16 {runId} - 1` tidak dapat dibaca dari Depreciation Run
21. Arahkan kursor ke sel `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1`
22. Verifikasi kedua kolom buku baris `Laptop Pro 16 {runId} - 1` menampilkan `Pending` tanpa tooltip alasan
23. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` tetap `Pending` dengan tooltip `Purchase cost has not been set.`, didahulukan atas `Pending` tanpa tooltip

### Jejak Posted memblok Delete Asset Data dan Purchase
24. Klik kartu `Disposed`
25. Ketik Search `Genset 20kVA {runId}`, tekan Enter
26. Buka menu `⋯` baris `Genset 20kVA {runId} - 1`
27. Verifikasi menu aksi baris `Genset 20kVA {runId} - 1` memuat `Detail`
28. Arahkan kursor ke aksi `Delete Asset Data`
29. Verifikasi aksi `Delete Asset Data` tampil `Disabled` dengan tooltip `Asset has posted depreciation or journal entries. Use Disposal.`
30. Tutup menu aksi baris
31. Klik kartu `All`
32. Ketik Search `Laptop Pro 16 {runId}`, tekan Enter
33. Buka menu `⋯` baris `Laptop Pro 16 {runId} - 1`
34. Klik `Edit Purchase`
35. Arahkan kursor ke field Purchase Cost
36. Verifikasi field Purchase Date, Purchase Cost, dan Additional costs read-only dengan tooltip `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`

### Presedensi sel Asset Value aset Disposed saat predikat tidak terbaca
37. Tutup dialog Edit Purchase
38. Ketik Search `{runId}`, tekan Enter
39. Arahkan kursor ke sel `Asset Value (Commercial)` baris `Lemari Besi {runId} - 1`
40. Verifikasi sel `Asset Value (Commercial)` baris `Lemari Besi {runId} - 1` menampilkan `Pending` dengan tooltip `Asset class has not been set.`, didahulukan atas `Pending` tanpa tooltip dan atas `Rp 0,00`
41. Verifikasi kedua kolom buku baris `Genset 20kVA {runId} - 1` tetap menampilkan `Rp 0,00` walaupun periode Posted terakhir tidak terbaca
42. Status jurnal pelepasan belum Posted atas `Meja Rapat {runId} - 1` tidak dapat dibaca dari Depreciation Run
43. Arahkan kursor ke sel `Asset Value (Commercial)` baris `Meja Rapat {runId} - 1`
44. Verifikasi kedua kolom buku baris `Meja Rapat {runId} - 1` menampilkan `Pending` tanpa tooltip alasan
