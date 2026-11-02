---
id: TC-FA-GRP-E2E-237-tab-assets-sort-brand-model-type-dan-tampilan-badge-dark-truncation-hover
title: "Tab Assets Sort Kolom Brand dan Model/Type serta Tampilan Badge Dark dengan Truncation dan Hover Nama Penuh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1076
  - TC-FA-GRP-1077
  - TC-FA-GRP-1084
coverage:
  web: automated
---

# Tab Assets Sort Kolom Brand dan Model/Type serta Tampilan Badge Dark dengan Truncation dan Hover Nama Penuh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan nilai Brand dan Model/Type bervariasi (huruf besar/kecil, angka, kosong; sedikitnya dua nilai distinct per kolom, S-11), termasuk Brand `Dell`, Model/Type `Latitude 5420`, Brand dan Model/Type bernama `International Business Machines Corporation` (> 25 karakter), aset tanpa Brand, dan aset tanpa Model/Type. Data dibaca lewat kemampuan baca fixture BE; nilai ini tidak ada di Tabel Data Uji Pre-setup (lihat Temuan untuk QA).
- Kolom Brand dan Model/Type tampil pada konfigurasi kolom default tab Assets (precondition "Pastikan kolom tampil" TC-1076 dan TC-1077).
- Kemampuan teknis: membaca data aset Warehouse A; disediakan tim FE/BE tanpa endpoint karangan.
- State global: tidak ada. Spec tidak menyimpan Setup Column; sort dikembalikan ke netral oleh klik header ke-3.

## Test Steps

### TC-FA-GRP-1076: Sort Tab Assets by kolom Brand: siklus Asc, Desc, Netral

1. Buka Detail Warehouse A (Tab Assets)
2. Verifikasi kolom Brand tampil pada tabel (precondition TC)
3. Klik header Brand 1×
4. Verifikasi urutan Ascending A→Z case-insensitive berdasarkan teks badge
5. Klik header 2×
6. Verifikasi urutan Descending Z→A
7. Klik header 3×
8. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1077: Sort Tab Assets by kolom Model/Type: siklus Asc, Desc, Netral

9. Verifikasi kolom Model/Type tampil pada tabel (precondition TC)
10. Klik header Model/Type 1×
11. Verifikasi urutan Ascending A→Z case-insensitive berdasarkan teks badge
12. Klik header 2×
13. Verifikasi urutan Descending Z→A
14. Klik header 3×
15. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1084: Tampilan badge Dark Brand dan Model/Type dengan truncation dan hover nama penuh

16. Amati kolom Brand dan Model/Type
17. Verifikasi nilai Brand `Dell` dan Model/Type `Latitude 5420` (≤ 25 karakter) tampil sebagai badge Dark berisi nama penuh
18. Verifikasi nama > 25 karakter `International Business Machines Corporation` tampil `Internationa.. Corporation` (12 huruf pertama + `..` + 12 huruf terakhir, spasi dihitung)
19. Hover badge Brand ber-nama panjang
20. Verifikasi hover badge Brand menampilkan nama penuh `International Business Machines Corporation` tanpa hierarki
21. Hover badge Model/Type ber-nama panjang
22. Verifikasi hover badge Model/Type menampilkan nama penuh `International Business Machines Corporation` tanpa hierarki
23. Amati aset tanpa Brand dan aset tanpa Model/Type
24. Verifikasi aset tanpa Brand menampilkan `—` pada kolom Brand
25. Verifikasi aset tanpa Model/Type menampilkan `—` pada kolom Model/Type

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan di tabel diamati pada halaman yang tampil; sort bekerja pada seluruh data dan klik ke-3 mengembalikan urutan default Name A→Z.
- Temuan untuk QA:
  - TC-FA-GRP-1076 dan TC-FA-GRP-1077: Expected "kosong" ada di data variasi tetapi posisi nilai kosong pada Ascending/Descending tidak disebut; spec hanya mengasersi urutan nilai berisi.
  - TC-FA-GRP-1084: nilai `Dell`, `Latitude 5420`, dan `International Business Machines Corporation` tidak ada di Tabel Data Uji; Model/Type bernama panjang memakai nilai yang sama dengan Brand (Data TC hanya menyebut satu nilai panjang).
