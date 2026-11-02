---
id: TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki
title: "Tab Assets Download Isi Berkas: Transformasi Tipe Badge, Date, Empty, Brand/Model/Type Nama Penuh, dan Category Hierarki Penuh dari Root"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-727
  - TC-FA-GRP-728
  - TC-FA-GRP-729
  - TC-FA-GRP-1086
  - TC-FA-GRP-1186
coverage:
  web: automated
---

# Tab Assets Download Isi Berkas: Transformasi Tipe Badge, Date, Empty, Brand/Model/Type Nama Penuh, dan Category Hierarki Penuh dari Root

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Kelas harness: binary buffer (f); spec ini hanya mengasersi isi berkas. Nama berkas, header, dan jumlah baris diasersi di spec 230.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal.
- Data tambahan di Warehouse A (disediakan tim FE/BE; tidak ada di Tabel Data Uji): aset ber-Brand `Dell` dan Model/Type `Latitude 5420`; aset ber-Brand dan Model/Type `International Business Machines Corporation` (> 25 karakter); sedikitnya satu aset dengan sel kosong (`—`) pada kolom yang tampil; aset ber-Category `Laptop` (parent `IT Equipment`) dan aset ber-Category level 1 (tanpa parent).
- Kemampuan teknis (disediakan tim FE): membuka berkas unduhan XLSX dan CSV, membaca nilai sel, dan membaca warna latar sel; format tanggal General Settings client dibaca lewat fixture BE (dipakai langkah 6).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (centang Category pada langkah 12, `[Save]` pada langkah 13); hook `after` menghapus preferensi kolom Tab Assets di browser (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-727, TC-FA-GRP-728, TC-FA-GRP-729, dan TC-FA-GRP-1086: Isi berkas XLSX

1. Klik angka Total Asset Warehouse A
2. Klik icon Download
3. Pilih Download as XLSX
4. Buka file XLSX yang terunduh
5. Verifikasi sel kolom Status (tipe badge) ditulis label teks apa adanya tanpa warna
6. Verifikasi sel kolom Last Updated (tipe date) mengikuti format tanggal General Settings
7. Verifikasi sel yang kosong (`—`) di tabel ditulis hyphen tunggal `-` di berkas
8. Verifikasi kolom Brand dan Model/Type memuat nama penuh `Dell`, `Latitude 5420`, dan `International Business Machines Corporation` tanpa truncation `..`
9. Verifikasi nilai Brand dan Model/Type ditulis nama saja, tanpa hierarki dan tanpa warna badge

### TC-FA-GRP-1186: Category ditulis hierarki penuh dari root

10. Klik icon (⋯) pada header kolom terakhir
11. Klik [Setup Column]
12. Centang Category
13. Klik [Save]
14. Klik icon Download
15. Pilih Download as CSV
16. Verifikasi tidak ada toast sukses
17. Buka file CSV yang terunduh
18. Verifikasi sel Category aset ber-Category `Laptop` berisi hierarki penuh dari root `IT Equipment > Laptop`
19. Verifikasi sel Category aset ber-Category level 1 berisi nama Category itu saja

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-FA-GRP-727, 728, 729, dan 1086 memiliki Langkah 1 sampai 4 yang identik (Download as XLSX, buka file); satu unduhan berkas dipakai untuk keempatnya dan langkah 5 sampai 9 membaca berkas yang sama.
- Langkah penghubung (S-03): langkah 4 dan 17 membuka berkas unduhan; langkah 10 sampai 13 menampilkan kolom Category (precondition TC-FA-GRP-1186, tidak diasersi).
- Langkah 13 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Langkah 16 (absence toast sukses) diletakkan segera sesudah pemicu Download dan sebelum asersi berkas; berkas terbuka (langkah 17) dan sel terbaca (langkah 18) menjadi bukti respons diproses (8b butir 11).
- Spec ini tidak memakai butir `P-n`: seluruh TC berkelas f.
- Temuan untuk QA:
  - TC-FA-GRP-727 Expected "Kolom badge ditulis label teks apa adanya tanpa warna" tidak menyebut kolom badge mana yang diperiksa; spec memeriksa kolom Status.
  - TC-FA-GRP-728 Expected "Kolom tanggal mengikuti format General Settings" tidak menyebut kolom tanggal mana; spec memeriksa kolom Last Updated.
  - TC-FA-GRP-729 tidak menyebut kolom yang berisi nilai kosong; spec menyatakan data sel kosong sebagai data tambahan tim FE/BE.
  - TC-FA-GRP-1086 dan 1186 memakai Brand/Model/Type/Category literal yang tidak ada di Tabel Data Uji; spec menyatakannya sebagai data disediakan tim FE/BE.
