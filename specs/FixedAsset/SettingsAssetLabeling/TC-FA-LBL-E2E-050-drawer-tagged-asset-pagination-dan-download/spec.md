---
id: TC-FA-LBL-E2E-050-drawer-tagged-asset-pagination-dan-download
title: "Drawer Tagged Asset: Pagination dan Download (menu, nama berkas, kolom, dan baris)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:global-table-rules/pagination
  - FALB:obl/T-ALB-02/download
  - FALB:obl/T-ALB-02/pagination
coverage:
  web: automated
---

# Drawer Tagged Asset: Pagination dan Download (menu, nama berkas, kolom, dan baris)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-050` dengan 12 aset Active bersuffix `{runId}-050`, lebih dari satu halaman pada ukuran halaman bawaan 10; minimal dua Asset Name dan dua Brand).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; kemampuan membaca nama berkas, header kolom, dan jumlah baris data berkas CSV unduhan. Hook `before` membuat label dan aset `DU-59`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List tersimpan di browser (bukan di server). Spec menyembunyikan kolom Asset ID pada langkah 25 dan memulihkannya pada langkah 28; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset

### FALB:global-table-rules/pagination: Pagination Drawer memakai ukuran halaman dan pilihan yang sama dengan Labels List

3. Verifikasi Pagination menampilkan 10 baris per halaman secara bawaan (halaman pertama memuat 10 dari 12 aset `DU-59`)
4. Buka pilihan jumlah baris per halaman
5. Verifikasi pilihan jumlah baris per halaman adalah 10, 25, 50, dan 100
6. Tutup pilihan jumlah baris per halaman dengan Esc

### FALB:obl/T-ALB-02/download: Download CSV dan XLSX mengikuti Search, Filter, dan kolom tampil

7. Klik Download pada toolbar Drawer
8. Verifikasi menu Download memuat opsi `Download as CSV` dan `Download as XLSX`
9. Klik `Download as CSV`
10. Verifikasi tidak ada toast sukses yang tampil
11. Verifikasi berkas CSV terunduh bernama `Tagged-Assets-` diikuti nama label `DU-59` dengan ekstensi `.csv`
12. Verifikasi berkas memuat 12 baris data (seluruh aset `DU-59`, bukan hanya 10 baris halaman pertama)
13. Verifikasi header berkas memuat kolom tampil berurutan `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
14. Klik Download pada toolbar Drawer, klik `Download as XLSX`
15. Verifikasi berkas XLSX terunduh bernama `Tagged-Assets-` diikuti nama label `DU-59` dengan ekstensi `.xlsx`
16. Ketik Search nama Brand salah satu aset `DU-59`, tekan Enter
17. Klik Download pada toolbar Drawer, klik `Download as CSV`
18. Verifikasi berkas hanya memuat baris aset hasil Search
19. Klik `(←)` pada kotak Search
20. Klik ikon Filter di toolbar Drawer
21. Pilih satu opsi Brand pada field `Brand`, klik `[Apply]`
22. Klik Download pada toolbar Drawer, klik `Download as CSV`
23. Verifikasi berkas hanya memuat baris aset hasil Filter
24. Klik `[Clear Field]`, klik `[Apply]`
25. Klik header kolom Actions (`⋯`) pada tabel Drawer, hapus centang kolom Asset ID
26. Klik Download pada toolbar Drawer, klik `Download as CSV`
27. Verifikasi header berkas tidak memuat kolom Asset ID
28. Centang kembali kolom Asset ID pada panel Column Visibility

### FALB:obl/T-ALB-02/pagination: Navigasi halaman Pagination Drawer

29. Pindah ke halaman 2 lewat navigasi halaman berikutnya
30. Verifikasi halaman 2 memuat 2 baris sisa aset `DU-59`
31. Ketik nomor halaman `1` pada input nomor halaman, tekan Enter
32. Verifikasi halaman 1 aktif dan memuat 10 baris
33. Ubah ukuran halaman Pagination menjadi 25
34. Verifikasi tabel kembali ke halaman 1 dan memuat seluruh 12 aset `DU-59`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 6 (menutup pilihan jumlah baris), 19 (menutup Search), 20 (membuka Filter Panel), 24 (mengosongkan Filter Panel, S-09), 25 dan 28 (menyembunyikan lalu menampilkan kembali kolom Asset ID lewat panel Column Visibility, yang berlaku langsung; 8b.14, R-24).
- Anchor positif (bagian 8b butir 11): langkah 9 adalah pemicu yang menjadi anchor absence toast pada langkah 10; berkas terunduh pada langkah 11 membuktikan unduhan diproses.
- Pembagian klausa lintas spec: `FALB:global-table-rules/pagination` diasersi di spec ini untuk Tagged Asset List; klausa Labels List ada di spec 035 dan klausa Modal Changelog: Labels di spec 054. `FALB:obl/T-ALB-02/download` diasersi di spec ini untuk nama berkas, kolom, dan jumlah baris, dan di spec 067 untuk isi sel berkas (kelas binary buffer).
- Kasus tepi Pagination (nomor halaman tidak valid, penghapusan baris terakhir) dan kegagalan unduh tidak punya klausa pada aturan yang dikutip spec ini sehingga tidak diasersi.
