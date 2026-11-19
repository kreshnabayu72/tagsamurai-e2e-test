---
id: TC-FA-BORROW-BE-094-tabel-search-sort-filter-server
title: "Server mencari, mengurutkan, dan menyaring tabel Borrow per kelas kolom dan tipe data"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-SRC-1, EB-FLT-3, EB-SRT-1, EB-SRT-2]
smoke: []
dependsOn: []
trace:
  EB-SRC-1: [5, 6, 8, 9, 11, 13]
  EB-FLT-3: [15, 16, 18, 19, 21, 22]
  EB-SRT-1: [2, 3, 24, 26, 28, 32, 35, 37, 43, 45]
  EB-SRT-2: [29, 30, 33, 39, 41]
anchor: []
---

# Server mencari, mengurutkan, dan menyaring tabel Borrow per kelas kolom dan tipe data

## Prerequisites
- Aktor:
  - Total Control `Hendra Wijaya {runId}`, cakupan seluruh client, pengaju kelima BRW di Data selain DU-094-6.
  - Borrower `Ezra Mahendra {runId}`, karyawan tanpa role Aktor Borrow, cakupan hanya My Asset, pemicu DU-094-6 lewat `Borrow an Asset`.
- Data:
  - Tab Transactions, tabel Borrow. Keenam BRW diajukan berurutan dari DU-094-1 sampai DU-094-6, sehingga Request Date DU-094-1 paling lama dan DU-094-6 paling baru. Transaction ID dibentuk server dan menjadi milik tiap entri.
  - Keenam Borrower adalah karyawan tanpa role Aktor Borrow, cakupan hanya My Asset. Setiap BRW berisi aset berstatus Ready sebanyak Total Asset-nya, dan tiap aset hanya ada di satu BRW.
  - DU-094-1: Borrower `Élan Kusuma {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `2`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-094-2: Borrower `Bambang Prakoso {runId}`, Group `Head Office`, Status `Waiting for Approval`, Total Asset `10`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-094-3: Borrower `de Fretes Marlina {runId}`, Group `Head Office`, Status `Borrowed`, Total Asset `2`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-094-4: Borrower `Anggoro Pratama {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `3`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-094-5: Borrower `Elan Kusuma {runId}`, Group `Head Office`, Status `Waiting for Approval`, Total Asset `1`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-094-6: Borrower `Ezra Mahendra {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `1`, Source `Self-service`, Requested By `—`.
- Kondisi:
  - Aset DU-094-2 dan DU-094-5 memakai aturan approval `Needs approval`, sehingga BRW-nya berstatus `Waiting for Approval` saat diajukan; aset DU-094-1, DU-094-4, dan DU-094-6 tanpa approval; aset DU-094-3 sudah di-Hand Over.
  - Tidak ada Sort aktif kecuali yang disebut langkah; kolom Source tersembunyi seperti pengaturan awal tabel.

## Test Steps

### Urutan awal mengikuti urutan tindakan status
1. Total Control meminta daftar tab Transactions dengan Filter Borrower `Élan Kusuma {runId}`, `Bambang Prakoso {runId}`, `de Fretes Marlina {runId}`, `Anggoro Pratama {runId}`, `Elan Kusuma {runId}`, dan `Ezra Mahendra {runId}`, tanpa Search dan tanpa Sort
2. Verifikasi baris berstatus `Waiting for Handover` (Borrower `Anggoro Pratama {runId}`, `Élan Kusuma {runId}`, dan `Ezra Mahendra {runId}`) berada di atas baris berstatus `Waiting for Approval` (Borrower `Bambang Prakoso {runId}` dan `Elan Kusuma {runId}`)
3. Verifikasi baris berstatus `Waiting for Approval` berada di atas baris berstatus `Borrowed` (Borrower `de Fretes Marlina {runId}`)

### Search mencocokkan substring tanpa membedakan huruf besar dan kecil di kolom teks, badge, dan angka
4. Total Control mencari dengan Search `ambang`, dengan Filter Borrower keenam Borrower di Data
5. Verifikasi baris Borrower `Bambang Prakoso {runId}` tampil, walau `ambang` ditulis huruf kecil dan berada di tengah `Bambang`
6. Verifikasi baris Borrower `Anggoro Pratama {runId}` tidak tampil
7. Total Control mencari dengan Search `for hand`, dengan Filter Borrower keenam Borrower di Data
8. Verifikasi baris Borrower `Anggoro Pratama {runId}`, `Élan Kusuma {runId}`, dan `Ezra Mahendra {runId}` tampil, karena status `Waiting for Handover` mengandung `for hand`
9. Verifikasi baris Borrower `Bambang Prakoso {runId}` tidak tampil, karena statusnya `Waiting for Approval`
10. Total Control mencari dengan Search `10`, dengan Filter Borrower keenam Borrower di Data
11. Verifikasi baris Borrower `Bambang Prakoso {runId}` dengan Total Asset `10` tampil
12. Total Control mencari dengan Search `zzqxv`, dengan Filter Borrower keenam Borrower di Data
13. Verifikasi tidak ada baris yang cocok, sehingga daftar menampilkan `No results found`

### Antar-field Filter berlaku AND dan dalam satu field berlaku OR
14. Total Control meminta daftar dengan Filter Borrower `Anggoro Pratama {runId}` dan `Bambang Prakoso {runId}`
15. Verifikasi baris Borrower `Anggoro Pratama {runId}` dan `Bambang Prakoso {runId}` tampil, masing-masing cocok dengan salah satu Borrower terpilih
16. Verifikasi baris Borrower `Elan Kusuma {runId}` tidak tampil
17. Total Control meminta daftar dengan Filter Borrower `Anggoro Pratama {runId}` dan `Bambang Prakoso {runId}` serta Filter Status `Waiting for Handover`
18. Verifikasi baris Borrower `Anggoro Pratama {runId}` tampil, karena memenuhi Borrower dan Status sekaligus
19. Verifikasi baris Borrower `Bambang Prakoso {runId}` tidak tampil, karena Borrower cocok tetapi statusnya `Waiting for Approval`
20. Total Control meminta daftar dengan Filter Borrower `Anggoro Pratama {runId}`, `Bambang Prakoso {runId}`, dan `de Fretes Marlina {runId}` serta Filter Status `Waiting for Handover` dan `Borrowed`
21. Verifikasi baris Borrower `Anggoro Pratama {runId}` dan `de Fretes Marlina {runId}` tampil, masing-masing cocok dengan salah satu Status terpilih
22. Verifikasi baris Borrower `Bambang Prakoso {runId}` tidak tampil

### Sort teks tidak membedakan huruf besar dan kecil serta menempatkan aksen sesudah huruf polos
23. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Borrower A–Z
24. Verifikasi urutan baris menurut Borrower adalah `Anggoro Pratama {runId}`, `Bambang Prakoso {runId}`, `de Fretes Marlina {runId}`, `Elan Kusuma {runId}`, `Élan Kusuma {runId}`, lalu `Ezra Mahendra {runId}`
25. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Borrower Z–A
26. Verifikasi urutan baris menurut Borrower adalah `Ezra Mahendra {runId}`, `Élan Kusuma {runId}`, `Elan Kusuma {runId}`, `de Fretes Marlina {runId}`, `Bambang Prakoso {runId}`, lalu `Anggoro Pratama {runId}`

### Sort angka natural dan nilai sama mengikuti urutan awal
27. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Total Asset naik
28. Verifikasi baris Total Asset `10` (Borrower `Bambang Prakoso {runId}`) berada paling bawah, sesudah baris Total Asset `3` (Borrower `Anggoro Pratama {runId}`)
29. Verifikasi di antara dua baris Total Asset `1`, baris berstatus `Waiting for Handover` (Borrower `Ezra Mahendra {runId}`) berada di atas baris berstatus `Waiting for Approval` (Borrower `Elan Kusuma {runId}`)
30. Verifikasi di antara dua baris Total Asset `2`, baris berstatus `Waiting for Handover` (Borrower `Élan Kusuma {runId}`) berada di atas baris berstatus `Borrowed` (Borrower `de Fretes Marlina {runId}`)
31. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Total Asset turun
32. Verifikasi baris Total Asset `10` (Borrower `Bambang Prakoso {runId}`) berada paling atas, diikuti baris Total Asset `3` (Borrower `Anggoro Pratama {runId}`)
33. Verifikasi di antara dua baris Total Asset `2`, baris berstatus `Waiting for Handover` (Borrower `Élan Kusuma {runId}`) tetap di atas baris berstatus `Borrowed` (Borrower `de Fretes Marlina {runId}`), tidak ikut terbalik

### Sort tanggal Oldest First dan Newest First
34. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Request Date `Oldest First`
35. Verifikasi urutan baris menurut Request Date adalah Borrower `Élan Kusuma {runId}`, `Bambang Prakoso {runId}`, `de Fretes Marlina {runId}`, `Anggoro Pratama {runId}`, `Elan Kusuma {runId}`, lalu `Ezra Mahendra {runId}`
36. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Request Date `Newest First`
37. Verifikasi urutan baris menurut Request Date adalah Borrower `Ezra Mahendra {runId}`, `Elan Kusuma {runId}`, `Anggoro Pratama {runId}`, `de Fretes Marlina {runId}`, `Bambang Prakoso {runId}`, lalu `Élan Kusuma {runId}`

### Nilai kosong di akhir saat naik dan di awal saat turun, serta badge A-Z
38. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Requested By A–Z
39. Verifikasi baris Borrower `Ezra Mahendra {runId}` dengan Requested By `—` berada paling bawah
40. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Requested By Z–A
41. Verifikasi baris Borrower `Ezra Mahendra {runId}` dengan Requested By `—` berada paling atas
42. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Source A–Z
43. Verifikasi baris Borrower `Ezra Mahendra {runId}` dengan Source `Self-service` berada di bawah kelima baris Source `Admin`
44. Total Control meminta daftar dengan Filter Borrower keenam Borrower di Data dan Sort Source Z–A
45. Verifikasi baris Borrower `Ezra Mahendra {runId}` dengan Source `Self-service` berada di atas kelima baris Source `Admin`
