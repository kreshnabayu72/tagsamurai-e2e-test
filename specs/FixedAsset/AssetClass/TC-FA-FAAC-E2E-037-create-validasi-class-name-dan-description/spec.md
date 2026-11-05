---
id: TC-FA-FAAC-E2E-037-create-validasi-class-name-dan-description
title: "Create Asset Class: Validasi Class Name dan Description (Kosong, Batas Panjang, Emoji)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-101
  - TC-FA-FAAC-102
  - TC-FA-FAAC-103
  - TC-FA-FAAC-104
coverage:
  web: automated
---

# Create Asset Class: Validasi Class Name dan Description (Kosong, Batas Panjang, Emoji)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active, mengizinkan Tax Method `Declining Balance`). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Submit pada langkah 5 ditolak validasi sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup; Class Code `B-X1` dan nilai uji lain adalah input uji kebijakan yang submit-nya diblokir dan boleh literal.
- Kemampuan teknis: membaca jumlah Asset Class lewat kemampuan baca BE (disediakan tim FE/BE) untuk baseline N0 sebelum Submit.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel

### TC-FA-FAAC-101: Submit dengan Class Name kosong

3. Isi Class Code `B-X1`
4. Isi Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`; biarkan Class Name kosong
5. Klik `Submit`
6. Verifikasi caption di bawah Class Name: `Class name must not be empty`
7. Verifikasi tab General diberi titik peringatan
8. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-102: Class Name lebih dari 120 karakter

9. Isi Class Name dengan 121 karakter `a`
10. Verifikasi caption langsung muncul: `Max. 120 characters`
11. Ganti isi Class Name menjadi 120 karakter `a`
12. Verifikasi tidak ada caption pada Class Name

### TC-FA-FAAC-103: Class Name memuat emoji

13. Ketik Class Name `Mesin 😀` sebagai pengganti isi sebelumnya
14. Verifikasi emoji diblok di input Class Name (nilai field tidak memuat emoji)

### TC-FA-FAAC-104: Description lebih dari 360 karakter

15. Kosongkan isi Class Name
16. Isi Description dengan 361 karakter `d`
17. Verifikasi caption langsung muncul: `Max. 360 characters`
18. Ganti isi Description menjadi 360 karakter `d`
19. Verifikasi tidak ada caption pada Description

### Penutup

20. Klik breadcrumb `Asset Class`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-101 sampai 104). Tidak ada TC hanya-BE di spec ini.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 2 dan tiap TC mengganti isi field yang diuji.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), langkah 15 (mengosongkan Class Name agar TC-104 tidak membawa nilai TC-103), dan langkah 20 sampai 22 (menutup form dirty, S-08).
- Asersi "tidak ada Asset Class dibuat" (langkah 8) memakai selisih terhadap baseline N0 dengan anchor positif berupa caption penolakan pada langkah 6. Asersi "tidak ada caption" (langkah 12 dan 19) didahului caption pada field yang sama (langkah 10 dan 17).
- TC-103 Expected memuat dua jalur ("diblok di input; bila lolos, caption ..."). Spec mengasersi jalur pertama (emoji diblok); jalur kedua tidak ditulis karena langkah bersyarat tidak dipakai.
- Temuan untuk QA:
  - TC-103 langkah 2 menyebut "ketik atau tempel" tanpa memilih satu aksi; spec memakai ketik (tempel teks ke field angka ada di spec 042).
  - TC-103 Expected bersyarat ("bila lolos") tidak menetapkan perilaku tunggal yang diharapkan; jalur kedua (`Class name contains invalid characters`) tidak diasersi.
  - TC-101 Expected butir b memuat "tidak ada Asset Class dibuat" yang dibuktikan lewat selisih jumlah terhadap baseline; TC tidak memberi cara lain untuk mengamatinya.
