---
id: TC-FA-FATR-BE-094-list-overrides
title: "Search, sort, dan filter daftar override"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: [EB-SRC-1, EB-FLT-3, EB-SRT-1]
smoke: []
dependsOn: []
trace:
  EB-SRC-1: [6, 8, 9, 11, 13, 15, 28]
  EB-FLT-3: [17, 19, 20, 22, 24, 26, 28]
  EB-SRT-1: [31, 33, 36, 38]
---
# Search, sort, dan filter daftar override

## Prerequisites
- Aktor: Maya Pengelola (DU-094-1) dan Dina Penyunting (DU-094-2), keduanya Total Control dengan cakupan seluruh Group.
- Data:
  - DU-094-1: User, pengelola Total Control pembuat override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-094-2: User, pengelola Total Control kedua pembuat override: Name `Dina Penyunting {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-094-3: Category, Category leaf yang menampung override uji daftar: Name `Perangkat Daftar {runId}`.
  - DU-094-4: Group, Group target override pertama: Name `Workshop Daftar {runId}`.
  - DU-094-5: Group, Group target override dengan nama berawalan huruf kecil: Name `bengkel kecil daftar {runId}`.
  - DU-094-6: Group, Group target override kedua yang namanya memuat Workshop: Name `Workshop Cadangan {runId}`.
  - DU-094-7: Asset, aset target override Asset dan pemilik Asset Name: Name `Truk Daftar {runId}`; Asset Name `Truk Operasional Daftar {runId}`; Category `Perangkat Daftar {runId}`; Group `Workshop Cadangan {runId}`.
  - DU-094-13 sampai DU-094-16 adalah kata kunci Search di langkah masing-masing, bukan record yang sudah ada.
- Kondisi:
  - Seluruh field Category `Perangkat Daftar {runId}` bernilai Inherit dan belum ada override pada Category itu.
  - Daftar override pada entitas bersama juga memuat override pihak lain; seluruh asersi hanya menyangkut override DU-094-8 sampai DU-094-12, dan urutan dibaca relatif di antara kelimanya.

## Test Steps

### Setup: lima override dibuat berurutan oleh dua pengelola
1. Maya Pengelola menambahkan override Group `Workshop Daftar {runId}` pada Category `Perangkat Daftar {runId}` untuk transaksi peminjaman dengan Max duration `30` dan Max extensions `1`
2. Dina Penyunting menambahkan override Group `bengkel kecil daftar {runId}` pada Category `Perangkat Daftar {runId}` untuk transaksi peminjaman dengan Max duration `20`
3. Maya Pengelola menambahkan override Asset Name `Truk Operasional Daftar {runId}` pada Category `Perangkat Daftar {runId}` untuk transaksi peminjaman dengan Max duration `10`
4. Dina Penyunting menambahkan override aset `Truk Daftar {runId}` pada Category `Perangkat Daftar {runId}` untuk transaksi peminjaman dengan Max extensions `2`
5. Dina Penyunting menambahkan override Group `Workshop Cadangan {runId}` pada Category `Perangkat Daftar {runId}` untuk transaksi peminjaman dengan Max extensions `3`
6. Verifikasi daftar override Category `Perangkat Daftar {runId}` memuat kelima override itu

### Search: substring dan huruf besar atau kecil sama-sama cocok
7. Maya Pengelola mencari `shop` di daftar override Category `Perangkat Daftar {runId}`
8. Verifikasi hasil memuat override Group `Workshop Daftar {runId}` dan override Group `Workshop Cadangan {runId}`, karena kata kunci cocok di tengah nama target
9. Verifikasi hasil tidak memuat override Group `bengkel kecil daftar {runId}`
10. Maya Pengelola mencari `WORKSHOP` di daftar override Category `Perangkat Daftar {runId}`
11. Verifikasi hasil memuat override Group `Workshop Daftar {runId}` dan override Group `Workshop Cadangan {runId}`, karena huruf besar dan kecil sama-sama cocok
12. Maya Pengelola mencari `Max extensions` di daftar override Category `Perangkat Daftar {runId}`
13. Verifikasi hasil memuat override Group `Workshop Daftar {runId}`, override aset `Truk Daftar {runId}`, dan override Group `Workshop Cadangan {runId}`, karena kata kunci cocok di kolom Overridden
14. Maya Pengelola mencari `Tidak Ada {runId}` di daftar override Category `Perangkat Daftar {runId}`
15. Verifikasi daftar tidak memuat satu pun override milik spec ini

### Filter: antar-field berlaku AND, dalam satu field berlaku OR
16. Maya Pengelola menyaring Scope `Group` di daftar override Category `Perangkat Daftar {runId}`
17. Verifikasi hasil memuat override Group `Workshop Daftar {runId}`, `bengkel kecil daftar {runId}`, dan `Workshop Cadangan {runId}`, dan tidak memuat override Asset Name maupun override aset
18. Maya Pengelola menyaring Scope `Group` dan `Asset Name` di daftar override Category `Perangkat Daftar {runId}`
19. Verifikasi hasil memuat override Asset Name `Truk Operasional Daftar {runId}` selain ketiga override Group, karena dalam satu field berlaku OR
20. Verifikasi hasil tidak memuat override aset `Truk Daftar {runId}`
21. Maya Pengelola menyaring Scope `Group` dan Created By `Maya Pengelola {runId}` di daftar override Category `Perangkat Daftar {runId}`
22. Verifikasi hasil hanya memuat override Group `Workshop Daftar {runId}`, karena antar-field berlaku AND
23. Maya Pengelola menyaring Scope `Asset` dan Created By `Maya Pengelola {runId}` di daftar override Category `Perangkat Daftar {runId}`
24. Verifikasi hasil tidak memuat satu pun override milik spec ini, karena tidak ada override yang memenuhi kedua field sekaligus
25. Maya Pengelola menyaring Created By `Maya Pengelola {runId}` dan `Dina Penyunting {runId}` di daftar override Category `Perangkat Daftar {runId}`
26. Verifikasi hasil memuat kelima override milik spec ini, karena dalam satu field berlaku OR
27. Maya Pengelola menyaring Created By `Dina Penyunting {runId}` dan mencari `shop` di daftar override Category `Perangkat Daftar {runId}`
28. Verifikasi hasil hanya memuat override Group `Workshop Cadangan {runId}`, karena Search dan Filter berlaku bersama

### Sort: teks tanpa membedakan huruf besar atau kecil, tanggal Oldest First dan Newest First
29. Maya Pengelola menyaring Scope `Group` di daftar override Category `Perangkat Daftar {runId}`
30. Maya Pengelola mengurutkan kolom Target A-Z
31. Verifikasi urutan hasil: `bengkel kecil daftar {runId}`, `Workshop Cadangan {runId}`, lalu `Workshop Daftar {runId}`, karena teks diurutkan tanpa membedakan huruf besar atau kecil
32. Maya Pengelola mengurutkan kolom Target Z-A di daftar override Group yang sama
33. Verifikasi urutan hasil berbalik: `Workshop Daftar {runId}`, `Workshop Cadangan {runId}`, lalu `bengkel kecil daftar {runId}`
34. Maya Pengelola menghapus saringan di daftar override Category `Perangkat Daftar {runId}`
35. Maya Pengelola mengurutkan kolom Created At dari Newest First
36. Verifikasi urutan relatif kelima override: override Group `Workshop Cadangan {runId}`, override aset `Truk Daftar {runId}`, override Asset Name `Truk Operasional Daftar {runId}`, override Group `bengkel kecil daftar {runId}`, lalu override Group `Workshop Daftar {runId}`
37. Maya Pengelola mengurutkan kolom Created At dari Oldest First
38. Verifikasi urutan relatif kelima override berbalik: override Group `Workshop Daftar {runId}` paling dulu, dan override Group `Workshop Cadangan {runId}` paling akhir
