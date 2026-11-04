---
id: TC-FA-LBL-E2E-051-drawer-tagged-asset-kolom-curated-tidak-tampil-sampai-dicentang-di-setup-column
title: "Drawer Tagged Asset: kolom curated (Measurement, Label, Last Scanned, Asset Value, Warranty Expiry) tidak tampil sampai dicentang di Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/setup-column/curated/FLD-26
  - FALB:obl/T-ALB-02/setup-column/curated/FLD-24
  - FALB:obl/T-ALB-02/setup-column/curated/FLD-28
  - FALB:obl/T-ALB-02/setup-column/curated/FLD-29
  - FALB:obl/T-ALB-02/setup-column/curated/FLD-30
coverage:
  web: automated
---

# Drawer Tagged Asset: kolom curated (Measurement, Label, Last Scanned, Asset Value, Warranty Expiry) tidak tampil sampai dicentang di Setup Column

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-051` dengan 12 aset Active bersuffix `{runId}-051`, dipakai agar tabel Tagged Asset List memuat baris data).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat label dan aset `DU-59`; hook `after` menghapusnya.
- State global: spec ini tidak menyimpan konfigurasi kolom; modal Setup Column ditutup tanpa `[Save]` pada langkah 25 sehingga perubahan pratinjau dibuang (`prd-conventions.md` §9.3). Hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset

### FALB:obl/T-ALB-02/setup-column/curated/FLD-26: Kolom Measurement tidak tampil sampai dicentang

3. Verifikasi header kolom Name tampil pada tabel Tagged Asset List
4. Verifikasi header kolom Measurement tidak tampil pada tabel Tagged Asset List
5. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
6. Verifikasi checkbox kolom Measurement tidak tercentang dan dapat dicentang
7. Centang kolom Measurement
8. Verifikasi pratinjau tabel di balik modal menampilkan header kolom Measurement

### FALB:obl/T-ALB-02/setup-column/curated/FLD-24: Kolom Label tidak tampil sampai dicentang

9. Verifikasi pratinjau tabel di balik modal tidak menampilkan header kolom Label
10. Verifikasi checkbox kolom Label tidak tercentang dan dapat dicentang
11. Centang kolom Label
12. Verifikasi pratinjau tabel di balik modal menampilkan header kolom Label

### FALB:obl/T-ALB-02/setup-column/curated/FLD-28: Kolom Last Scanned tidak tampil sampai dicentang

13. Verifikasi pratinjau tabel di balik modal tidak menampilkan header kolom Last Scanned
14. Verifikasi checkbox kolom Last Scanned tidak tercentang dan dapat dicentang
15. Centang kolom Last Scanned
16. Verifikasi pratinjau tabel di balik modal menampilkan header kolom Last Scanned

### FALB:obl/T-ALB-02/setup-column/curated/FLD-29: Kolom Asset Value tidak tampil sampai dicentang

17. Verifikasi pratinjau tabel di balik modal tidak menampilkan header kolom Asset Value (Commercial) dan Asset Value (Fiscal)
18. Verifikasi checkbox kolom Asset Value (Commercial) dan Asset Value (Fiscal) tidak tercentang dan dapat dicentang
19. Centang kolom Asset Value (Commercial) dan Asset Value (Fiscal)
20. Verifikasi pratinjau tabel di balik modal menampilkan header kolom Asset Value (Commercial) dan Asset Value (Fiscal)

### FALB:obl/T-ALB-02/setup-column/curated/FLD-30: Kolom Warranty Expiry tidak tampil sampai dicentang

21. Verifikasi pratinjau tabel di balik modal tidak menampilkan header kolom Warranty Expiry
22. Verifikasi checkbox kolom Warranty Expiry tidak tercentang dan dapat dicentang
23. Centang kolom Warranty Expiry
24. Verifikasi pratinjau tabel di balik modal menampilkan header kolom Warranty Expiry
25. Klik `[✕]` pada modal Setup Column

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 5 (membuka modal Setup Column), dan 25 (menutup modal tanpa `[Save]` sehingga susunan kolom tersimpan tidak berubah; R-24).
- Anchor positif (bagian 8b butir 2): langkah 3 mendahului absence kolom pada langkah 4; absence pada langkah 9, 13, 17, dan 21 memakai kolom yang sudah tampil pada pratinjau (langkah 8) sebagai anchor.
- Tampil diasersi pada pratinjau tabel di balik modal, yang merefleksikan perubahan secara langsung sebelum `[Save]` (`prd-conventions.md` §9.3). Penyimpanan lewat `[Save]` diasersi pada spec 042 untuk kolom Hideable.
- Isi sel kolom curated diasersi di spec 043; Search dan Filter kolom Measurement, Label, dan Asset Value di spec 052; Sort kolom curated di spec 049.
- Kolom curated Category, Transactional Policy, dan Custom Field (`FLD-08`, `FLD-27`, `FLD-31`) ditahan (IGAP-0046, IGAP-0047, IGAP-0052) dan tidak diasersi.
