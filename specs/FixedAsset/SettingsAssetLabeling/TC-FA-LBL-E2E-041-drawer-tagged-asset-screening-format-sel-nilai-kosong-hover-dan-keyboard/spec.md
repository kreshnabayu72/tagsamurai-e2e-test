---
id: TC-FA-LBL-E2E-041-drawer-tagged-asset-screening-format-sel-nilai-kosong-hover-dan-keyboard
title: "Drawer Tagged Asset: screening, format sel, nilai kosong, hover, dan penutupan keyboard"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/screening
  - FALB:obl/T-ALB-02/cell-format
  - FALB:obl/T-ALB-02/hover/FLD-25
  - FALB:obl/T-ALB-02/hover/FLD-21
  - FALB:obl/T-ALB-02/hover/FLD-22
  - FALB:obl/T-ALB-02/empty-value/FLD-25
  - FALB:obl/T-ALB-02/empty-value/FLD-21
  - FALB:obl/T-ALB-02/empty-value/FLD-22
  - FALB:defaults-ordering-spec/tampilan-nilai-kosong
  - FALB:obl/T-ALB-02/keyboard
coverage:
  web: automated
---

# Drawer Tagged Asset: screening, format sel, nilai kosong, hover, dan penutupan keyboard

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-041` dengan 12 aset Active bersuffix `{runId}-041`, lebih dari satu halaman; sebagian aset tanpa tag aktif, Brand, dan Model/Type).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset. Hook `before` membuat label dan 12 aset `DU-59` lewat API dan melabelinya; hook `after` menghapus label dan aset itu.
- State global: spec ini hanya membaca; tidak mengubah konfigurasi kolom atau state global.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset

### FALB:obl/T-ALB-02/screening: Screening Drawer Tagged Asset dari atas ke bawah

3. Verifikasi header Drawer menampilkan judul `Tagged Assets` (tanpa nama label) dan ikon `[✕]` di pojok kanan atas
4. Verifikasi blok info identitas berbentuk grid label:value dengan tiga pasang: Label (chip badge bernama `DU-59`), Color Hex (kode warna yang sama dengan kolom Color Hex baris label itu di Labels List), dan Total Asset bernilai 12
5. Verifikasi Table Tools Drawer berurutan `Search | Filter | Download`
6. Verifikasi header kolom tabel Tagged Asset List berurutan `Name | Asset ID | TAG | Brand | Model/Type | Group | Status | Last Updated`
7. Verifikasi kolom Hidden `Measurement`, `Label`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tidak tampil
8. Verifikasi footer Drawer menampilkan kontrol Pagination
9. Verifikasi Drawer tidak memuat tombol aksi selain Download dan tidak memuat tombol teks `Close`
10. Ubah ukuran halaman Pagination menjadi 25 agar 12 aset `DU-59` tampil dalam satu halaman

### FALB:obl/T-ALB-02/cell-format: Format sel kolom default tabel Tagged Asset List

11. Verifikasi sel Name baris aset `DU-59` berformat `[Asset Name] - [Increment]` (mis. `Laptop Dell - 12`)
12. Verifikasi sel TAG baris aset bertag aktif menampilkan satu ikon per tipe tag aktif (`RFID`, `QR`, `NFC`, atau `BARCODE`) dan semua ikon tampil penuh
13. Verifikasi sel Brand berupa badge Dark dengan nama Brand penuh
14. Verifikasi sel Model/Type berupa badge Dark dengan nama Model/Type penuh
15. Verifikasi sel Last Updated berformat tanggal dan jam sesuai Date Format dan Time Format di Global Settings > General Settings

### FALB:obl/T-ALB-02/hover/FLD-25: Hover kolom TAG

16. Arahkan kursor ke ikon tag pada sel TAG baris aset bertag aktif
17. Verifikasi tooltip menampilkan label tipe tag pada ikon (mis. `RFID`)

### FALB:obl/T-ALB-02/hover/FLD-21: Hover kolom Brand

18. Arahkan kursor ke badge Brand pada baris aset ber-Brand
19. Verifikasi tooltip menampilkan nama Brand penuh

### FALB:obl/T-ALB-02/hover/FLD-22: Hover kolom Model/Type

20. Arahkan kursor ke badge Model/Type pada baris aset ber-Model/Type
21. Verifikasi tooltip menampilkan nama Model/Type penuh

### FALB:obl/T-ALB-02/empty-value/FLD-25: Nilai kosong kolom TAG

22. Verifikasi sel TAG baris aset tanpa tag aktif menampilkan `—`

### FALB:obl/T-ALB-02/empty-value/FLD-21: Nilai kosong kolom Brand

23. Verifikasi sel Brand baris aset tanpa Brand menampilkan `—`

### FALB:obl/T-ALB-02/empty-value/FLD-22: Nilai kosong kolom Model/Type

24. Verifikasi sel Model/Type baris aset tanpa Model/Type menampilkan `—`

### FALB:defaults-ordering-spec/tampilan-nilai-kosong: Tampilan nilai kosong mengikuti kolom Nilai Kosong

25. Verifikasi sel Name dan Asset ID terisi pada baris aset yang diamati (kolom tidak pernah kosong)
26. Verifikasi sel TAG, Brand, dan Model/Type yang tidak bernilai tampil `—`, bukan sel blank dan bukan teks `null`

### FALB:obl/T-ALB-02/keyboard: Penutupan Drawer lewat `[✕]` dan Esc

27. Klik area backdrop di luar Drawer
28. Verifikasi Drawer `Tagged Assets` tetap tampil
29. Tekan Esc
30. Verifikasi Table Tools Labels List (Search, Filter, Download, Changelog, `[+ Label]`) tampil
31. Verifikasi Drawer `Tagged Assets` tidak tampil
32. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset kembali
33. Klik `[✕]` pada header Drawer
34. Verifikasi Table Tools Labels List (Search, Filter, Download, Changelog, `[+ Label]`) tampil
35. Verifikasi Drawer `Tagged Assets` tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 dan 32 (membuka Drawer), serta 10 (ukuran halaman 25 agar seluruh aset teramati tanpa berpindah halaman).
- Anchor positif (bagian 8b butir 2): langkah 6 mendahului absence kolom pada langkah 7; langkah 30 dan 34 mendahului absence Drawer pada langkah 31 dan 35.
- Pembagian klausa lintas spec: `FALB:defaults-ordering-spec/tampilan-nilai-kosong` diasersi di spec ini untuk tabel Tagged Asset List; klausa untuk tabel Modal Changelog: Labels ada di spec 053.
- Temuan PRD: klausa "fokus kembali ke pemicu" pada `FALB:obl/T-ALB-02/keyboard` tidak dinyatakan PRD. PRD §4.1.1 hanya menyatakan Drawer ditutup lewat `[✕]` atau `Esc`, dan `prd-conventions.md` §9.10c hanya menyatakan klik backdrop tidak menutup; tidak ada klausa fokus kembali maupun focus trap. Klausa itu tidak diasersi; langkah 27 sampai 35 mengasersi penutupan lewat Esc dan `[✕]` serta klik backdrop yang tidak menutup.
- Cakupan kolom: isi sel, Search, Sort, Filter, dan hover kolom Group dan Status ditahan (IGAP-0046 dan IGAP-0051), sehingga langkah 6 hanya mengasersi header keduanya. Kolom Hidden Category, Transactional Policy, dan Custom Field (`FLD-08`, `FLD-27`, `FLD-31`) ditahan dan tidak diasersi pada langkah 7.
- Cakupan data: `DU-59` tidak memuat Brand atau Model/Type lebih dari 25 karakter, sehingga aturan truncation badge (`prd-conventions.md` §9.14: 12 huruf pertama, `..`, 12 huruf terakhir) tidak diasersi; langkah 13, 14, 19, dan 21 mengasersi nama penuh.
- Klausa format kolom Hidden (Measurement, Label, Last Scanned, Asset Value, Warranty Expiry) pada `FALB:obl/T-ALB-02/cell-format` diasersi di spec 043; kolom Group dan Status ditahan.
