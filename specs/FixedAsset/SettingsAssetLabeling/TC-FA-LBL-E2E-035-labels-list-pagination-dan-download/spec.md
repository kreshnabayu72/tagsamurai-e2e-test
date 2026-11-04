---
id: TC-FA-LBL-E2E-035-labels-list-pagination-dan-download
title: "Labels List: Pagination dan Download (menu, nama berkas, kolom, dan baris)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:global-table-rules/pagination
  - FALB:obl/T-ALB-01/pagination
  - FALB:global-table-rules/download
  - FALB:obl/T-ALB-01/download
coverage:
  web: automated
---

# Labels List: Pagination dan Download (menu, nama berkas, kolom, dan baris)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-035-01` sampai `Lst-{runId}-035-12`, Total Asset 0 sampai 3 sehingga filter Total Asset Min 1 dan Max 2 menghasilkan sedikitnya satu baris).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; kemampuan membaca nama berkas unduhan, baris header, dan jumlah baris data berkas CSV dan XLSX; penghapusan preferensi kolom tersimpan di browser untuk tabel Labels List di hook `after`.
- State global: konfigurasi kolom Labels List tersimpan di browser (bukan di server); spec memulihkannya lewat langkah 37 sampai 39. Hook `after` menghapus preferensi kolom sebagai cadangan dan menghapus label seed `DU-56` lewat sesi API.

## Test Steps

### FALB:global-table-rules/pagination: Ukuran halaman bawaan dan pilihan

1. Ketik Search `DU-56` (nama dasar `Lst-{runId}-035`), tekan Enter
2. Verifikasi Pagination menampilkan jumlah baris per halaman bawaan 10 dan halaman pertama memuat 10 baris label `DU-56`
3. Buka pilihan jumlah baris per halaman
4. Verifikasi pilihan jumlah baris per halaman adalah 10, 25, 50, dan 100 tanpa opsi All
5. Tutup pilihan jumlah baris per halaman dengan Esc

### FALB:obl/T-ALB-01/pagination: Navigasi dan perubahan ukuran halaman

6. Pindah ke halaman 2 lewat navigasi Pagination
7. Verifikasi halaman 2 aktif memuat 2 baris sisa label `DU-56`
8. Isi input nomor halaman dengan 1, tekan Enter
9. Verifikasi halaman 1 aktif memuat 10 baris label `DU-56`
10. Pindah ke halaman 2 lewat navigasi Pagination
11. Pilih 25 baris per halaman
12. Verifikasi halaman 1 aktif memuat seluruh 12 baris label `DU-56`
13. Pilih 10 baris per halaman

### FALB:global-table-rules/download: Format, nama berkas, dan cakupan Search

14. Klik ikon Download di toolbar
15. Verifikasi overlay Download menampilkan `Download as CSV` dan `Download as XLSX`
16. Pilih `Download as CSV`
17. Verifikasi berkas terunduh bernama `Labels.csv`
18. Verifikasi berkas `Labels.csv` memuat 12 baris data, yaitu seluruh baris hasil Search dan bukan hanya baris halaman pertama
19. Klik ikon Download di toolbar, pilih `Download as XLSX`
20. Verifikasi berkas terunduh bernama `Labels.xlsx`

### FALB:obl/T-ALB-01/download: Berkas mengikuti Search, Filter, dan kolom tampil

21. Klik ikon Download di toolbar, pilih `Download as CSV`
22. Verifikasi toast sukses tidak tampil
23. Verifikasi header berkas `Labels.csv` terdiri atas kolom Label, Color Hex, Total Asset, Modified By, dan Last Updated
24. Klik ikon Filter di toolbar
25. Isi input `Min` pada field Total Asset dengan 1
26. Isi input `Max` pada field Total Asset dengan 2
27. Klik `[Apply]`
28. Telusuri seluruh halaman Pagination dan catat jumlah baris hasil tersaring (N)
29. Klik ikon Download di toolbar, pilih `Download as CSV`
30. Verifikasi berkas `Labels.csv` memuat N baris data
31. Klik `[Clear Field]`, klik `[Apply]`
32. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
33. Hapus centang kolom Last Updated
34. Klik `[Save]`
35. Klik ikon Download di toolbar, pilih `Download as CSV`
36. Verifikasi header berkas `Labels.csv` terdiri atas kolom Label, Color Hex, Total Asset, dan Modified By tanpa kolom Last Updated
37. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
38. Centang kolom Last Updated
39. Klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-56`, R-16), langkah 5 dan 13 (menutup pilihan dan mengembalikan ukuran halaman bawaan), langkah 24 sampai 28 (menyiapkan filter), langkah 31 (mengosongkan filter, S-09), langkah 32 dan 37 (membuka Modal Setup Column).
- Pemulihan Setup Column (8b.14): langkah 37 sampai 39 mengembalikan kolom Last Updated tanpa `Verifikasi`. Kolom Last Updated hanya disembunyikan sebagai objek uji cakupan kolom berkas.
- Anchor positif (bagian 8b butir 11): pemicu Download pada langkah 21 menjadi anchor langkah 22; berkas terunduh pada langkah 23 membuktikan respons sudah diproses.
- Pembagian klausa lintas spec: klausa isi sel berkas (nilai sel, kolom Modified By berisi nama lengkap user, BOM, tipe sel) dari `FALB:global-table-rules/download` dan `FALB:obl/T-ALB-01/download` diasersi di spec 067; spec ini mengasersi menu, nama berkas, kolom header, dan jumlah baris. Klausa `FALB:global-table-rules/pagination` untuk Tagged Asset List dan tabel Modal Changelog diasersi di spec 050 dan 054; spec ini mengasersi Labels List.
- Spec ini di atas smell 35 langkah (39 langkah). Alasan dipertahankan: seluruh blok satu kelas harness (Pagination dan Download pada tabel yang sama) dengan dataset `DU-56` yang sama; tiap blok mengembalikan state yang diubahnya (ukuran halaman, filter, kolom) sehingga berdiri sendiri.
