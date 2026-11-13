---
id: TC-FA-FAREG-E2E-039-draft-search
title: "Sub tab Draft: hasil Search"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§5#r3", "EB-SRC-2@tabel-draft", "EB-SRC-3@tabel-draft", "EB-SRC-5@tabel-draft", "EB-SRC-1"]
smoke: ["EB-SRC-1"]
dependsOn: []
trace:
  "§4.1#r22": [2]
  "§4.1#r23": [4]
  "§4.1#r24": [6]
  "§4.1#r25": [8]
  "§4.1#r26": [10, 38, 44]
  "§4.1#r27": [14]
  "§5#r3": [2]
  "EB-SRC-2@tabel-draft": [2, 12, 14]
  "EB-SRC-3@tabel-draft": [22, 24, 26, 28, 30, 34]
  "EB-SRC-5@tabel-draft": [44, 47]
  "EB-SRC-1": [16, 18, 20, 36]
anchor: [32, 40]
coverage:
  web: automated
---

# Sub tab Draft: hasil Search

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-039-1: Batch Draft dengan Group `Gudang Mampang {runId}`, Origin `REG-20261105-03901`, Total Asset `47`, Progress `65%`, Requested By `Hadi K`, Last Updated `T0 − 1 hari`.
  - DU-039-2: Batch Draft dengan Group `Gudang Hadi Jaya {runId}`, Origin `—`, Total Asset `23`, Progress `0%`, Requested By `Siti N`, Last Updated `T0 − 2 hari`.
  - DU-039-3: Batch Draft dengan Group `Gudang Procurement Pusat {runId}`, Origin `—`, Total Asset `9`, Progress `100%`, Requested By `Dewi A`, Last Updated `T0 − 3 hari`.
  - DU-039-4: Batch Draft dengan Group `Gudang_Pola {runId}`, Origin `—`, Total Asset `14`, Progress `20%`, Requested By `Agus P`, Last Updated `T0 − 4 hari`.
  - DU-039-5: Batch Draft dengan Group `Gudang Pola {runId}`, Origin `—`, Total Asset `8`, Progress `10%`, Requested By `Budi S`, Last Updated `T0 − 5 hari`.
  - DU-039-6: Batch Draft dengan Group `Gudang Timur.* {runId}`, Origin `—`, Total Asset `31`, Progress `80%`, Requested By `Agus P`, Last Updated `T0 − 6 hari`.
  - DU-039-7: Batch Draft dengan Group `Gudang Timur Raya {runId}`, Origin `—`, Total Asset `6`, Progress `30%`, Requested By `Budi S`, Last Updated `T0 − 7 hari`.
  - DU-039-8: Batch Draft dengan Group `Gudang Head Office Room {runId}`, Origin `—`, Total Asset `11`, Progress `70%`, Requested By `Dewi A`, Last Updated `T0 − 8 hari`.
  - DU-039-9: Batch Draft dengan Group `Gudang Barat {runId}`, Origin `—`, Total Asset `22`, Progress `90%`, Requested By `Rina W`, Last Updated `T0 − 9 hari`.
  - DU-039-10: Batch Draft dengan Group `Gudang Barat {runId} Daya`, Origin `—`, Total Asset `5`, Progress `75%`, Requested By `Rina W`, Last Updated `T0 − 10 hari`.
  - Hadi K, Siti N, Dewi A, Agus P, Budi S, dan Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.
- Kondisi: format tanggal General Settings `dd/MM/yy` dan format waktu 24 jam; kolom Requested By tampil.

## Test Steps

### Search pada kolom Group (Link + Badge)
1. Ketik Search `Gudang Mampang {runId}`, tekan Enter
2. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Mampang {runId}` dan tidak memuat baris `Gudang Hadi Jaya {runId}`

### Search pada kolom Origin (Text)
3. Ganti isi kotak search dengan `REG-20261105-03901`, tekan Enter
4. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}` dan tidak memuat baris `Gudang Hadi Jaya {runId}`

### Search pada kolom Total Asset (Number)
5. Ganti isi kotak search dengan `47`, tekan Enter
6. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}` dan tidak memuat baris `Gudang Hadi Jaya {runId}`

### Search pada kolom Progress (Progress bar)
7. Ganti isi kotak search dengan `65%`, tekan Enter
8. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}` dan tidak memuat baris `Gudang Hadi Jaya {runId}`

### Search pada kolom Requested By (User)
9. Ganti isi kotak search dengan `Hadi K`, tekan Enter
10. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}` dan tidak memuat baris `Gudang Hadi Jaya {runId}`

### Kata kunci cocok di dua kolom berbeda
11. Ganti isi kotak search dengan `Hadi`, tekan Enter
12. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}` yang cocok di kolom Requested By dan baris `Gudang Hadi Jaya {runId}` yang cocok di kolom Group

### Tanggal tidak dicari lewat Search
13. Ganti isi kotak search dengan tanggal Last Updated baris `Gudang Hadi Jaya {runId}` dalam Date Format `dd/MM/yy`, dari `T0 − 2 hari`, tekan Enter
14. Verifikasi tabel sub tab Draft tidak memuat baris `Gudang Hadi Jaya {runId}`

### Substring di tengah dan beda huruf kapital
15. Ganti isi kotak search dengan `curement Pusat {runId}`, tekan Enter
16. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Procurement Pusat {runId}` dan tidak memuat baris `Gudang Mampang {runId}`
17. Ganti isi kotak search dengan `GUDANG PROCUREMENT PUSAT {runId}`, tekan Enter
18. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Procurement Pusat {runId}` dan tidak memuat baris `Gudang Mampang {runId}`

### Kata kunci tanpa hasil
19. Ganti isi kotak search dengan `Zzqxv {runId}`, tekan Enter
20. Verifikasi `No results found` tampil

### Spasi di awal dan akhir kata kunci dibuang
21. Ganti isi kotak search dengan `  Gudang Mampang {runId}  `, tekan Enter
22. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Mampang {runId}` dan tidak memuat baris `Gudang Hadi Jaya {runId}`

### Spasi di tengah dipertahankan dan query hanya spasi
23. Ganti isi kotak search dengan `Gudang  Procurement Pusat {runId}`, tekan Enter
24. Verifikasi `No results found` tampil
25. Ganti isi kotak search dengan `   `, tekan Enter
26. Verifikasi `No results found` tidak tampil

### Karakter khusus dicari sebagai teks
27. Ganti isi kotak search dengan `Gudang_Pola {runId}`, tekan Enter
28. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang_Pola {runId}` dan tidak memuat baris `Gudang Pola {runId}`
29. Ganti isi kotak search dengan `Timur.* {runId}`, tekan Enter
30. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Timur.* {runId}` dan tidak memuat baris `Gudang Timur Raya {runId}`

### Kata kunci tidak dipecah per kata
31. Ganti isi kotak search dengan `Gudang Head Office Room {runId}`, tekan Enter
32. Verifikasi tabel sub tab Draft memuat baris `Gudang Head Office Room {runId}`
33. Ganti isi kotak search dengan `Head Room`, tekan Enter
34. Verifikasi baris `Gudang Head Office Room {runId}` tidak tampil di tabel sub tab Draft

### Nilai yang menjadi substring nilai lain
35. Ganti isi kotak search dengan `Gudang Barat {runId}`, tekan Enter
36. Verifikasi tabel sub tab Draft memuat baris `Gudang Barat {runId}` dan baris `Gudang Barat {runId} Daya`

### Kolom dengan nilai seragam tetap dicari
37. Ganti isi kotak search dengan `Rina W`, tekan Enter
38. Verifikasi tabel sub tab Draft memuat baris `Gudang Barat {runId}` dan baris `Gudang Barat {runId} Daya`

### Kolom yang disembunyikan tidak dicari
39. Ganti isi kotak search dengan `Hadi K`, tekan Enter
40. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}`
41. Klik header kolom Actions `⋯`
42. Hilangkan centang `Requested By` pada panel Column Visibility
43. Ganti isi kotak search dengan `Hadi K`, tekan Enter
44. Verifikasi baris `Gudang Mampang {runId}` tidak tampil di tabel sub tab Draft
45. Centang kembali `Requested By` pada panel Column Visibility
46. Ganti isi kotak search dengan `Hadi K`, tekan Enter
47. Verifikasi tabel sub tab Draft memuat baris `Gudang Mampang {runId}`
