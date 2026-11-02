---
id: TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role
title: "Tab Users Download Isi Berkas: Tipe Empty, Badge Activation Status, Date Temporary Until, CSV BOM/Escaping, dan Kolom Group Role [N] roles"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-674
  - TC-FA-GRP-1035
  - TC-FA-GRP-1036
  - TC-FA-GRP-1138
  - TC-FA-GRP-1147
coverage:
  web: automated
---

# Tab Users Download Isi Berkas: Tipe Empty, Badge Activation Status, Date Temporary Until, CSV BOM/Escaping, dan Kolom Group Role [N] roles

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Data Dinamis untuk TC-1138: user ber-Name `Budi, "Santoso {runId}-191"` (nama mengandung koma dan tanda kutip) dibuat lewat API di hook `before`, di-assign ke Warehouse A, dan dihapus di hook `after`; selama spec berjalan Total User Warehouse A bertambah satu dan Last Updated Warehouse A dapat berubah (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE): membaca isi berkas CSV dan XLSX yang terunduh (nilai sel, BOM, jumlah sheet dan nama sheet) lewat penangkap unduhan browser.
- Warehouse A memuat user dengan Activation Status berbeda (Activated dan Pending Activation) dan Temporary User dengan Temporary Until; Date Format General Settings tidak diubah spec. Kolom Activation Status dan Temporary Until adalah kolom curated yang ditampilkan lewat Column Visibility; pemulihan lewat hook `after` (hapus preferensi kolom).
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Data Dinamis No 8 (Pre-setup tambahan, di-seed lewat API di hook `before`, dibersihkan di hook `after`; disediakan tim FE/BE tanpa endpoint karangan): node level 1 `Multi Role Node {runId}-191` (Assignable) dengan lima user subjek U-GM (tier Group Manager + Group Role Asset Admin), U-2R (Asset Admin + Asset Auditor), U-1R (Asset Admin), U-AU (Asset Auditor), U-3R (Asset Custodian + Asset Technician), dipakai bersama user client Pre-setup No 1, 2, 3 sehingga tabel memuat tepat 8 baris. Email subjek: fixture baru `Fixture.groupsTabUsers.<kode>191.email`.
- Password user subjek: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru; tidak ada login subjek di spec ini).

## Test Steps

1. Klik angka Total User Warehouse A

### TC-674: Tipe empty

2. Klik icon Download
3. Pilih Download as XLSX
4. Baca isi berkas XLSX
5. Verifikasi nilai kosong (`—`) di tabel ditulis hyphen tunggal `-` di berkas

### TC-1035: Tipe badge Activation Status

6. Tampilkan kolom Activation Status via Column Visibility
7. Klik icon Download
8. Pilih Download as XLSX
9. Baca isi berkas XLSX
10. Verifikasi kolom Activation Status ditulis sebagai label teks apa adanya tanpa warna badge

### TC-1036: Tipe date Temporary Until

11. Tampilkan kolom Temporary Until via Column Visibility
12. Klik icon Download
13. Pilih Download as XLSX
14. Baca isi berkas XLSX
15. Verifikasi kolom Temporary Until mengikuti format tanggal General Settings

### TC-1138: CSV BOM dan escaping, XLSX satu sheet, urutan mengikuti Sort

16. Klik header Name 2x (descending)
17. Klik icon Download
18. Pilih Download as CSV
19. Baca isi berkas CSV di editor teks
20. Verifikasi CSV diawali BOM UTF-8
21. Verifikasi nilai Name `Budi, "Santoso {runId}-191"` ter-escape sehingga tetap satu sel
22. Klik icon Download
23. Pilih Download as XLSX
24. Baca isi berkas XLSX
25. Verifikasi XLSX berisi satu sheet bernama `Sheet1`
26. Verifikasi urutan baris mengikuti Sort aktif (Name Z-A)
27. Klik header Name 1x agar sort kembali netral

### TC-1147: Kolom Group Role [N] roles

28. Kembali ke Groups List
29. Klik angka Total User Multi Role Node
30. Klik icon Download
31. Pilih Download as XLSX
32. Baca isi berkas XLSX
33. Verifikasi sel Group Role U-2R bernilai `Asset Admin, Asset Auditor` (nama role dipisah koma, bukan `2 roles`)
34. Verifikasi sel Group Role U-3R bernilai `Asset Custodian, Asset Technician`
35. Verifikasi sel Group Role U-1R bernilai `Asset Admin` dan U-GM bernilai `Group Manager`
36. Verifikasi sel Group Role user Total Control bernilai `Total Control`

## Notes

- Kelas f (binary buffer): spec ini berisi asersi isi berkas; nama berkas, header, dan jumlah baris ada di spec 190.
- Langkah penghubung (S-03): menampilkan kolom curated, klik header Name ke-3 untuk mengembalikan sort, dan kembali ke Groups List sebelum membuka Multi Role Node.
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (isi berkas Download Tab Users) dan tiap TC berdiri sendiri; TC-1147 memakai fixture Multi Role Node yang tidak dipakai TC lain di spec ini.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-1138 mensyaratkan user ber-Name `Budi, "Santoso"` di Warehouse A (data Pre-setup yang tidak ada); membuatnya mengubah Total User dan Last Updated Warehouse A selama spec berjalan, dan nama bersuffix per run dipakai (S-12).
  - Kode user subjek Multi Role Node tidak punya email di TC; spec memakai fixture baru ditetapkan tim FE.
