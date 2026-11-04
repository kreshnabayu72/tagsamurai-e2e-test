---
id: TC-FA-LBL-E2E-042-drawer-tagged-asset-setup-column-sembunyikan-tampilkan-geser-dan-reset-to-default
title: "Drawer Tagged Asset: Setup Column (sembunyikan, tampilkan, geser, dan Reset to Default)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/setup-column/hide-show
  - FALB:obl/T-ALB-02/setup-column/reorder
  - FALB:obl/T-ALB-02/setup-column/reset
coverage:
  web: automated
---

# Drawer Tagged Asset: Setup Column (sembunyikan, tampilkan, geser, dan Reset to Default)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-042` dengan 12 aset Active bersuffix `{runId}-042`, dipakai agar tabel Tagged Asset List memuat baris data).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat label dan aset `DU-59`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List tersimpan di browser (bukan di server). Spec memulihkannya ke susunan bawaan lewat langkah 8 sampai 11, langkah 16 sampai 18, dan langkah 22 sampai 24; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset

### FALB:obl/T-ALB-02/setup-column/hide-show: Sembunyikan dan tampilkan kolom Hideable

3. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
4. Hapus centang kolom Asset ID
5. Klik `[Save]`
6. Verifikasi header kolom Name tampil pada tabel Tagged Asset List
7. Verifikasi header kolom Asset ID tidak tampil pada tabel Tagged Asset List
8. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
9. Centang kolom Asset ID
10. Klik `[Save]`
11. Verifikasi header kolom Asset ID tampil kembali di antara kolom Name dan kolom TAG

### FALB:obl/T-ALB-02/setup-column/reorder: Geser urutan kolom

12. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
13. Geser kolom TAG ke posisi sebelum kolom Asset ID pada daftar kolom modal Setup Column
14. Klik `[Save]`
15. Verifikasi tabel Tagged Asset List menampilkan header kolom berurutan `Name | TAG | Asset ID | Brand | Model/Type | Group | Status | Last Updated`
16. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
17. Geser kolom TAG kembali ke posisi sesudah kolom Asset ID pada daftar kolom modal Setup Column
18. Klik `[Save]`

### FALB:obl/T-ALB-02/setup-column/reset: Reset to Default

19. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
20. Centang kolom Measurement
21. Hapus centang kolom Model/Type
22. Klik `[Reset to Default]`
23. Verifikasi tabel di balik modal tidak menampilkan kolom Measurement dan menampilkan kembali kolom Model/Type
24. Klik `[Save]`
25. Verifikasi tabel Tagged Asset List menampilkan header kolom berurutan `Name | Asset ID | TAG | Brand | Model/Type | Group | Status | Last Updated`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), dan 3, 8, 12, 16, 19 (membuka modal Setup Column).
- Pemulihan Setup Column (8b.14, R-24): langkah 8 sampai 11 menampilkan kembali kolom Asset ID (dengan `Verifikasi`, karena menampilkan kolom adalah klausa aturan hide-show); langkah 16 sampai 18 memulihkan urutan kolom tanpa `Verifikasi`; langkah 22 sampai 24 memulihkan susunan bawaan lewat `[Reset to Default]` dan `[Save]`, lalu langkah 25 memverifikasi hasil klausa reset.
- Anchor positif (bagian 8b butir 2): langkah 6 mendahului absence kolom pada langkah 7.
- Kolom curated yang tidak tampil sampai dicentang di Setup Column diasersi di spec 051. Hasil reset masuk pratinjau dan baru permanen setelah `[Save]` (`prd-conventions.md` §9.3): langkah 23 mengasersi pratinjau, langkah 25 mengasersi hasil setelah `[Save]`.
- Kolom Group dan Status hanya dipakai sebagai bagian urutan header; isi sel keduanya ditahan (IGAP-0046 dan IGAP-0051).
