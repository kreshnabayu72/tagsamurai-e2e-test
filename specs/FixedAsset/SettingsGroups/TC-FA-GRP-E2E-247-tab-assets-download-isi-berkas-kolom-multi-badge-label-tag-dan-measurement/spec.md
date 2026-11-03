---
id: TC-FA-GRP-E2E-247-tab-assets-download-isi-berkas-kolom-multi-badge-label-tag-dan-measurement
title: "Tab Assets Download Isi Berkas: Multi-Badge Status, Label A-Z, TAG, dan Measurement Symbol UoM"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1143
  - TC-FA-GRP-1184
  - TC-FA-GRP-1195
  - TC-FA-GRP-1202
coverage:
  web: automated
---

# Tab Assets Download Isi Berkas: Multi-Badge Status, Label A-Z, TAG, dan Measurement Symbol UoM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Multi Badge Node (Tabel Dinamis No 7) berisi hanya aset A1 (overlay Borrowed + Damaged; badge dalam sel alfabetis: Borrowed lalu Damaged), A2 (Assigned), A3 (Damaged), A4 (Draft); Multi Label Node (Pre-setup tambahan, Tabel Dinamis No 9, level 1) berisi hanya aset L1 (Finance, Fragile, Priority), L2 (Fragile, Priority), L3 (Priority), L4 (tanpa label), L5 (Finance); Value Gate Node A (Tabel Dinamis No 10) berisi aset G1 sampai G6; pairing tag aktif G1 RFID dan QR, G3 NFC, G4 BARCODE, G6 QR, G5 BARCODE tidak aktif, G2 tanpa pairing (Tabel Dinamis No 15); Measurement (Tabel Dinamis No 14): Laptop Dell, Printer HP, dan Monitor LG Piece `pcs`, Forklift Toyota Unit `unit`, Kabel Roll Meter `m`. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: membaca isi berkas unduhan CSV/XLSX (nilai sel, hyphen `-`) disediakan tim FE; asersi berkas memakai kemampuan itu.
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1143: Download Tab Assets, sel multi-badge ditulis badge dipisah koma

1. Ketik Search `Multi Badge Node` pada Groups List, tekan Enter
2. Buka Detail Multi Badge Node (Tab Assets)
3. Klik icon Download
4. Pilih Download as XLSX
5. Buka berkas
6. Verifikasi kolom Status: A1 = `Borrowed, Damaged` (badge urut alfabetis dipisah `", "`), A2 = `Assigned`, A3 = `Damaged`, A4 = `Draft`
7. Verifikasi nilai Status ditulis sebagai teks tanpa warna badge
8. Tutup Popup Detail Group

### TC-FA-GRP-1184: Download Tab Assets, kolom Label seluruh label A–Z dipisah koma, kosong ditulis -

9. Ganti isi kotak Search Groups List dengan `Multi Label Node`, tekan Enter
10. Buka Detail Multi Label Node (Tab Assets)
11. Buka Popup Setup Column
12. Centang Label
13. Klik [Save]
14. Klik icon Download
15. Pilih Download as CSV
16. Verifikasi tidak ada toast sukses
17. Buka berkas
18. Verifikasi kolom Label aset L1 berisi `Finance, Fragile, Priority` (seluruh label termasuk yang tersembunyi di balik `+1 more`, urut A–Z, dipisah `", "`)
19. Verifikasi sel Label aset L4 (tanpa label) ditulis hyphen tunggal `-`
20. Tutup Popup Detail Group

### TC-FA-GRP-1195: Download Tab Assets, kolom TAG ditulis label tipe tag, tanpa Tag Code

21. Ganti isi kotak Search Groups List dengan `Value Gate Node A`, tekan Enter
22. Buka Detail Value Gate Node A (Tab Assets)
23. Klik icon Download
24. Pilih Download as CSV
25. Verifikasi tidak ada toast sukses
26. Buka berkas
27. Verifikasi kolom TAG: G3 = `NFC`, G4 = `BARCODE`, G6 = `QR`, dan G1 memuat `RFID` dan `QR` dipisah `", "` (urutan label tidak diasersikan)
28. Verifikasi sel TAG G2 dan G5 ditulis hyphen tunggal `-`
29. Verifikasi berkas tidak memuat Tag Code

### TC-FA-GRP-1202: Download Tab Assets, kolom Measurement ditulis Symbol UoM

30. Buka Popup Setup Column
31. Centang Measurement
32. Klik [Save]
33. Klik icon Download
34. Pilih Download as CSV
35. Verifikasi tidak ada toast sukses
36. Buka berkas
37. Verifikasi kolom Measurement berisi `pcs` (G1, G2, G3, G6), `unit` (G4), dan `m` (G5)
38. Verifikasi Unit Name tidak ditulis di kolom Measurement

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular. Kelas harness f (isi berkas); nama berkas, header, dan jumlah baris diasersi di spec Download fungsional.
- Langkah penghubung (S-03): menutup Popup Detail Group antar node; Setup Column centang Label sebelum TC-1184 (precondition d); Setup Column centang Measurement adalah langkah TC-1202. Asersi tidak ada toast sukses diletakkan segera sesudah memilih format Download dan sebelum membuka berkas (8b butir 11); anchor positifnya adalah Verifikasi isi berkas sesudahnya.
- Spec ini 38 langkah, di atas smell 35 langkah: seluruh blok satu kelas harness (isi berkas unduhan) dengan alur yang sama (buka detail group, Download, buka berkas) dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Multi Badge Node`, `Multi Label Node`, `Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA (S-15): (1) Expected TC-1143 tidak menyebut nama berkas atau ketiadaan toast; hanya dua butir (Status dan teks tanpa warna). (2) TC memakai "Buka file" tanpa menyebut sheet atau pemisah CSV; kolom dibaca per nama header. (3) TC-1195 tidak mengasersikan urutan label pada G1. (4) TC-1202 tidak menyebut state awal Setup Column; preferensi kolom dikosongkan di hook `before`.
