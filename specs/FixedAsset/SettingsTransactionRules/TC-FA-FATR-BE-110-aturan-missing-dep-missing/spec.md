---
id: TC-FA-FATR-BE-110-aturan-missing-dep-missing
title: "Long missing after pada Missing"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
owner: BE
sourceRules: ["§Aturan Logika Modul#r31", §4.1#r157, §4.1#r158, §4.1#r159, §4.1#r160, §4.1#r173, §4.1#r174, §9.2#b272, §9.2#b392, §9.2#b399, §9.2#b415, §9.2#b416, §9.2#b417, §9.2#b418, §9.2#b421, §9.2#b422, §9.7#r34, §11#r17]
smoke: []
dependsOn: ["Missing: penanda Long missing dan Mark as Found"]
trace:
  §4.1#r157: [3, 4, 5]
  §4.1#r158: 8
  §9.2#b399: [8, 10, 11, 34, 35]
  §9.2#b392: [9, 35]
  §4.1#r159: 11
  §4.1#r160: 12
  §11#r17: [8, 12]
  §9.2#b415: 14
  §9.2#b416: 15
  "§Aturan Logika Modul#r31": 18
  §9.2#b421: 18
  §9.2#b422: 18
  §9.2#b417: 19
  §9.2#b418: 22
  §4.1#r173: 25
  §4.1#r174: 27
  §9.2#b272: [30, 31, 38, 39]
  §9.7#r34: [30, 31, 38, 39]
---

# Long missing after pada Missing

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-110-1: entitas khusus `Entitas Aset Hilang {runId}`, tidak dipakai spec lain; semua data di bawah ada di entitas ini.
  - DU-110-2: aset `Pompa Air {runId}`, Condition `Missing`, Missing sejak `T0 − 31 hari` (T0 adalah waktu run), ada record Missing aktif.
  - DU-110-3: aset `Trafo Mini {runId}`, Condition `Missing`, Missing sejak `T0 − 29 hari`, ada record Missing aktif.
  - DU-110-4: aset `Bor Listrik {runId}`, Condition `Missing`, Missing sejak `T0 − 5 hari`, ada record Missing aktif.
  - DU-110-5: aset `Tangga Lipat {runId}`, Condition `Missing`, Missing sejak `T0 − 5 hari`, ada record Missing aktif.
  - DU-110-6: aset `Rak Besi {runId}`, Condition `Missing`, Missing sejak `T0 − 5 hari`, ada record Missing aktif, dengan Disposal Source `Manual` berstatus Waiting for Approval yang diajukan atas aset itu.
  - DU-110-7: berkas Damaged Photo `bor-listrik-rusak.jpg`.
  - DU-110-8: berkas Photo `tangga-lipat-ditemukan.jpg`.
  - DU-110-9: aset `Kursi Kerja {runId}`, Condition `Missing`, Missing sejak `T0 − 30 hari kalender, pukul 00:30` pada zona waktu client, ada record Missing aktif. Waktu yang sama menurut UTC adalah `T0 − 31 hari kalender, pukul 17:30`.
  - DU-110-10: aset `Lemari Arsip {runId}`, sebelum dilaporkan Condition `Missing`, Missing sejak `T0 − 5 hari`, dengan record Missing aktif; sudah dilaporkan lewat laporan pelepasan aset berstatus `Proceeded`, dan transaksi pelepasan aset yang berasal dari laporan itu berstatus Waiting for Approval.
- Kondisi:
  - Long missing after bernilai `30` (days) pada awal spec.
  - After photo required bernilai `OFF` pada awal spec.
  - Transaction timeout bernilai `1` (days).
  - Zona waktu client bernilai `Asia/Jakarta` (UTC+7), dan T0 adalah pukul `10:00` pada zona waktu itu.

## Test Steps

### Long missing after 0 menonaktifkan penanda, notifikasi, dan saran
1. Total Control menyimpan Long missing after bernilai `0` di All categories
2. Job harian berjalan
3. Verifikasi aset `Pompa Air {runId}` yang Missing sejak `T0 − 31 hari` tidak diberi penanda Long missing
4. Verifikasi tidak ada notifikasi `missing_long` untuk aset `Pompa Air {runId}`
5. Verifikasi tidak ada saran Report disposal untuk aset `Pompa Air {runId}`

### Record Missing yang lebih lama dari Long missing after
6. Total Control menyimpan Long missing after bernilai `30` di All categories
7. Job harian berjalan
8. Verifikasi aset `Pompa Air {runId}` yang Missing sejak `T0 − 31 hari` diberi penanda Long missing
9. Verifikasi lama Missing aset `Pompa Air {runId}` dihitung dalam zona waktu client dari acuan awalnya, yaitu saat aset menjadi Missing
10. Verifikasi aset `Trafo Mini {runId}` yang Missing sejak `T0 − 29 hari` tidak diberi penanda Long missing
11. Verifikasi notifikasi `missing_long` untuk aset `Pompa Air {runId}` terkirim
12. Verifikasi saran Report disposal untuk aset `Pompa Air {runId}` tersedia

### missing_long dikirim sekali per record Missing
13. Job harian berjalan
14. Verifikasi notifikasi `missing_long` untuk aset `Pompa Air {runId}` tercatat tepat satu kali
15. Verifikasi tidak ada eskalasi atau pengulangan notifikasi overdue lain untuk aset `Pompa Air {runId}` sesudah job harian kedua

### Ambang diturunkan berlaku untuk record yang belum terkirim notifikasinya
16. Total Control menyimpan Long missing after bernilai `10` di All categories
17. Job harian berjalan
18. Verifikasi notifikasi `missing_long` untuk aset `Trafo Mini {runId}` yang Missing sejak `T0 − 29 hari` terkirim sesuai nilai `10` yang berlaku saat job berjalan
19. Verifikasi notifikasi `missing_long` untuk aset `Pompa Air {runId}` tidak terkirim ulang setelah ambang diubah

### Ambang dinaikkan tidak mencabut notifikasi yang sudah terkirim
20. Total Control menyimpan Long missing after bernilai `60` di All categories
21. Job harian berjalan
22. Verifikasi notifikasi `missing_long` untuk aset `Pompa Air {runId}` yang sudah terkirim tetap ada

### After photo required tidak mengatur Mark as Found
23. Total Control menyimpan After photo required bernilai `ON` di All categories
24. Kirim Mark as Found untuk record Missing aset `Bor Listrik {runId}` sebagai ditemukan dalam kondisi rusak, dengan foto kondisi rusak `bor-listrik-rusak.jpg` dan tanpa After photo
25. Verifikasi Mark as Found sebagai ditemukan dalam kondisi rusak diterima tanpa After photo saat After photo required `ON`
26. Kirim Mark as Found untuk record Missing aset `Tangga Lipat {runId}` sebagai ditemukan dalam kondisi Normal, dengan Photo `tangga-lipat-ditemukan.jpg` tanpa After photo
27. Verifikasi Mark as Found berstatus Normal diterima tanpa After photo saat After photo required `ON`

### Pelepasan aset yang kena Transaction timeout mengembalikan Condition dan record Missing
28. Waktu berlalu sampai batas Transaction timeout `1` (days) terlewati sejak transaksi pelepasan aset (Source `Manual`) atas aset `Rak Besi {runId}` diajukan
29. Job Transaction timeout berjalan
30. Verifikasi Condition aset `Rak Besi {runId}` kembali ke `Missing`, nilai sebelum pelepasan aset diajukan
31. Verifikasi record Missing aset `Rak Besi {runId}` kembali ke nilai sebelum pelepasan aset diajukan

### Batas hari kalender dihitung menurut zona waktu client
32. Total Control menyimpan Long missing after bernilai `30` di All categories
33. Job harian berjalan
34. Verifikasi aset `Pompa Air {runId}` yang Missing sejak `T0 − 31 hari` diberi penanda Long missing
35. Verifikasi aset `Kursi Kerja {runId}` yang Missing sejak `T0 − 30 hari kalender, pukul 00:30` pada zona waktu client `Asia/Jakarta`, yaitu tepat `30` hari kalender dan belum lebih dari `30` hari kalender menurut zona waktu client walaupun menurut UTC (Missing sejak `T0 − 31 hari kalender, pukul 17:30`) sudah lebih dari `30` hari kalender, tidak diberi penanda Long missing

### Pelepasan aset dari laporan pelepasan aset yang kena Transaction timeout mengembalikan Condition dan record Missing
36. Waktu berlalu sampai batas Transaction timeout `1` (days) terlewati sejak transaksi pelepasan aset yang berasal dari laporan pelepasan aset atas aset `Lemari Arsip {runId}` diajukan
37. Job Transaction timeout berjalan
38. Verifikasi Condition aset `Lemari Arsip {runId}` kembali ke `Missing`, nilai sebelum aset dilaporkan
39. Verifikasi record Missing aset `Lemari Arsip {runId}` kembali ke nilai sebelum aset dilaporkan
