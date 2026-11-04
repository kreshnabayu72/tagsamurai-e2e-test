---
id: TC-FA-LBL-E2E-049-drawer-tagged-asset-sort-kolom-curated
title: "Drawer Tagged Asset: Sort kolom curated (Measurement, Label, Asset Value, Last Scanned, Warranty Expiry)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/sort/FLD-26
  - FALB:obl/T-ALB-02/sort/FLD-24
  - FALB:obl/T-ALB-02/sort/FLD-29
  - FALB:obl/T-ALB-02/sort/FLD-28
  - FALB:obl/T-ALB-02/sort/FLD-30
coverage:
  web: automated
---

# Drawer Tagged Asset: Sort kolom curated (Measurement, Label, Asset Value, Last Scanned, Warranty Expiry)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-049` dengan 12 aset Active bersuffix `{runId}-049`), `DU-60` (atribut curated pada aset `DU-59`: Measurement dengan sedikitnya dua Symbol berbeda, Last Scanned dengan sebagian belum pernah dipindai, Asset Value Commercial dan Fiscal dengan sedikitnya dua nilai berbeda, Warranty Expiry dengan sedikitnya dua tanggal berbeda; nilai Date berbeda menit), `DU-61` (sebagian aset `DU-59` menempel pada lebih dari 2 label dengan jumlah label berbeda antar aset).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label, aset, dan atribut aset; hook `before` menunggu pergantian menit (maksimum 60 detik, bagian 6) sesudah seeding kelompok aset pertama agar nilai Date berbeda menit; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat data `DU-59`, `DU-60`, dan `DU-61`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List tersimpan di browser (bukan di server). Spec menampilkan enam kolom curated pada langkah 4 sampai 6 dan memulihkannya pada langkah 32 sampai 34; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman
4. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
5. Centang kolom Measurement, Label, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry
6. Klik `[Save]`

### FALB:obl/T-ALB-02/sort/FLD-26: Sort kolom Measurement

7. Verifikasi tabel memuat sedikitnya dua aset dengan Symbol Measurement berbeda
8. Klik header kolom Measurement
9. Verifikasi baris terurut menurut Symbol Measurement A–Z

### FALB:obl/T-ALB-02/sort/FLD-24: Sort kolom Label

10. Klik header kolom Label
11. Verifikasi baris terurut menaik menurut jumlah label (aset dengan jumlah label paling sedikit lebih dulu)
12. Verifikasi baris berjumlah label sama terurut menurut label pertama A–Z
13. Klik header kolom Label lagi
14. Verifikasi baris terurut menurun menurut jumlah label (aset dengan jumlah label terbanyak lebih dulu)
15. Verifikasi badge di dalam setiap sel Label tetap terurut A–Z walau baris diurutkan menurun

### FALB:obl/T-ALB-02/sort/FLD-29: Sort kolom Asset Value

16. Klik header kolom Asset Value (Commercial)
17. Verifikasi baris terurut menaik menurut nilai numerik asli Asset Value (Commercial), bukan menurut teks tampilan
18. Klik header kolom Asset Value (Commercial) lagi
19. Verifikasi baris terurut menurun menurut nilai numerik asli Asset Value (Commercial)
20. Klik header kolom Asset Value (Fiscal)
21. Verifikasi baris terurut menaik menurut nilai numerik asli Asset Value (Fiscal)

### FALB:obl/T-ALB-02/sort/FLD-28: Sort kolom Last Scanned

22. Klik header kolom Last Scanned
23. Verifikasi baris terurut Oldest First menurut Last Scanned
24. Verifikasi sel `—` (belum pernah dipindai) berada paling akhir
25. Klik header kolom Last Scanned lagi
26. Verifikasi baris terurut Newest First menurut Last Scanned
27. Verifikasi sel `—` berada paling awal

### FALB:obl/T-ALB-02/sort/FLD-30: Sort kolom Warranty Expiry

28. Klik header kolom Warranty Expiry
29. Verifikasi baris terurut Oldest First menurut Warranty Expiry
30. Klik header kolom Warranty Expiry lagi
31. Verifikasi baris terurut Newest First menurut Warranty Expiry
32. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
33. Hapus centang kolom Measurement, Label, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry
34. Klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 3 (ukuran halaman 25; asersi urutan memakai satu halaman penuh milik spec, 8b.15 butir a), 4 sampai 6 (menampilkan kolom curated sebagai precondition), serta 32 sampai 34 (pemulihan Setup Column tanpa `Verifikasi`; 8b.14, R-24).
- Anchor positif (bagian 8b butir 15d): langkah 7 membuktikan tabel memuat sedikitnya dua nilai Symbol berbeda sebelum asersi sort pertama.
- Pembagian klausa lintas spec: `FALB:obl/T-ALB-02/sort/FLD-29` dan `FALB:obl/T-ALB-02/sort/FLD-30` diasersi di spec ini untuk urutan numerik dan tanggal bagi pemegang hak dan di spec 044 untuk penempatan `No access` paling akhir.
- Posisi sel `—` pada Asset Value dan Warranty Expiry tidak diasersi: PRD §4.1.1 hanya menyatakan posisi `—` untuk Last Scanned (`prd-conventions.md` §9.7), langkah 24 dan 27.
