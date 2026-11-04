---
id: TC-FA-LBL-E2E-048-drawer-tagged-asset-sort-kolom-default-dan-urutan-default
title: "Drawer Tagged Asset: Sort kolom default, siklus Sort, dan urutan default"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/sort-default
  - FALB:defaults-ordering-spec/default-sort-tagged-asset-list
  - FALB:obl/T-ALB-02/sort-cycle
  - FALB:obl/T-ALB-02/sort/FLD-07
  - FALB:obl/T-ALB-02/sort/FLD-06
  - FALB:obl/T-ALB-02/sort/FLD-25
  - FALB:obl/T-ALB-02/sort/FLD-21
  - FALB:obl/T-ALB-02/sort/FLD-22
  - FALB:obl/T-ALB-02/sort/FLD-23
coverage:
  web: automated
---

# Drawer Tagged Asset: Sort kolom default, siklus Sort, dan urutan default

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-048` dengan 12 aset Active bersuffix `{runId}-048`; minimal dua Asset Name, dua Brand, dua Model/Type, dan tag RFID, QR, NFC dengan sel multi-ikon).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; hook `before` membuat aset dalam dua kelompok yang dipisah pergantian menit (maksimum 60 detik, bagian 6) agar nilai Last Updated kedua kelompok berbeda menit. Hook `before` membuat label dan aset `DU-59`; hook `after` menghapusnya.
- State global: spec ini tidak mengubah konfigurasi kolom atau state global.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman

### FALB:obl/T-ALB-02/sort-default: Urutan default saat pertama dimuat

4. Verifikasi tabel memuat sedikitnya dua baris aset `DU-59`
5. Verifikasi baris terurut menurut Name A–Z berdasarkan nama aset lalu Increment numerik natural (mis. `- 2` sebelum `- 10`) dan tidak ada kolom lain berindikator sort aktif

### FALB:defaults-ordering-spec/default-sort-tagged-asset-list: Default Sort Tagged Asset List kolom Name Ascending

6. Verifikasi header kolom Name menampilkan indikator ascending aktif sebagai default sort

### FALB:obl/T-ALB-02/sort-cycle: Siklus Sort tiga tahap dengan satu kolom aktif

7. Klik header kolom Model/Type
8. Verifikasi indikator ascending aktif hanya pada kolom Model/Type dan kolom Name tidak lagi berindikator aktif
9. Klik header kolom Brand
10. Verifikasi indikator ascending aktif pada kolom Brand dan kolom Model/Type kembali netral
11. Klik header kolom Brand lagi
12. Verifikasi indikator descending aktif pada kolom Brand
13. Klik header kolom Brand lagi
14. Verifikasi indikator kolom Brand netral dan baris kembali terurut menurut default Name A–Z

### FALB:obl/T-ALB-02/sort/FLD-07: Sort kolom Name

15. Klik header kolom Name
16. Verifikasi baris terurut menurut Name A–Z berdasarkan nama aset (tanpa membedakan huruf besar-kecil) lalu Increment numerik natural

### FALB:obl/T-ALB-02/sort/FLD-06: Sort kolom Asset ID

17. Klik header kolom Asset ID
18. Verifikasi baris terurut menurut Asset ID A–Z

### FALB:obl/T-ALB-02/sort/FLD-25: Sort kolom TAG

19. Klik header kolom TAG
20. Verifikasi baris terurut menaik menurut label ikon A–Z (label pertama dulu lalu berikutnya; urutan yang menjadi awalan urutan lain lebih dulu) dan sel `—` berada paling akhir

### FALB:obl/T-ALB-02/sort/FLD-21: Sort kolom Brand

21. Klik header kolom Brand
22. Verifikasi baris terurut menurut Brand A–Z

### FALB:obl/T-ALB-02/sort/FLD-22: Sort kolom Model/Type

23. Klik header kolom Model/Type
24. Verifikasi baris terurut menurut Model/Type A–Z

### FALB:obl/T-ALB-02/sort/FLD-23: Sort kolom Last Updated

25. Klik header kolom Last Updated
26. Verifikasi aset kelompok seed pertama berada sebelum aset kelompok seed kedua (Oldest First)
27. Klik header kolom Last Updated lagi
28. Verifikasi aset kelompok seed kedua berada sebelum aset kelompok seed pertama (Newest First)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), dan 3 (ukuran halaman 25; asersi urutan memakai satu halaman penuh milik spec, 8b.15 butir a).
- Anchor positif (bagian 8b butir 2 dan 15d): langkah 4 membuktikan tabel memuat sedikitnya dua baris data uji sebelum asersi sort pertama pada langkah 5.
- Urutan sort pada tiap kolom diasersi untuk ascending (klik pertama); arah descending dan kembali netral diasersi pada langkah 11 sampai 14 (siklus tiga tahap, `prd-conventions.md` §9.7). Last Updated diasersi untuk Oldest First dan Newest First pada langkah 25 sampai 28 dan dibatasi pada pasangan aset berbeda menit (kelompok seed pertama dan kedua; bagian 6).
- Sort kolom Group dan Status ditahan (IGAP-0046 dan IGAP-0051); Sort kolom curated diasersi di spec 049 dan spec 044.
