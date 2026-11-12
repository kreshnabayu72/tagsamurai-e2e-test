---
id: TC-FA-FAAC-E2E-036-create-validasi-class-code
title: "Create Asset Class: Validasi Class Code (Kosong, Batas Panjang, Karakter, Duplikat)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-97
  - TC-FA-FAAC-98
  - TC-FA-FAAC-99
  - TC-FA-FAAC-100
coverage:
  web: automated
---

# Create Asset Class: Validasi Class Code (Kosong, Batas Panjang, Karakter, Duplikat)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Asset Class `B-ANCHOR` (seed Pre-setup, dipakai TC-100 sebagai Class Code yang sudah ada; hanya dibaca, tidak diubah). Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active, mengizinkan Tax Method `Declining Balance`). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Semua Submit di spec ini ditolak validasi sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup; Class Code uji (`ABCDEFGHIJKLMNOP`, `AB#1 x`, `A-b_1.2`, `b-anchor`) adalah input uji kebijakan yang submit-nya diblokir dan boleh literal.
- Kemampuan teknis: membaca jumlah Asset Class lewat kemampuan baca BE (disediakan tim FE/BE) untuk baseline N0 sebelum Submit pertama; membaca jumlah entri Changelog Asset Class, System Log aktor, dan Activity Log FAMS lewat kemampuan baca BE (audit trail permanen, jumlah dibaca tepat sebelum aksi pemicu TC-100, S-12).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec; hook `after` tidak perlu memulihkan data.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel

### TC-FA-FAAC-97: Submit dengan Class Code kosong dan hanya spasi

3. Isi Class Code dengan 3 spasi
4. Isi field lain dengan nilai valid: Class Name `Test Class`, Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
5. Klik `Submit`
6. Verifikasi caption merah di bawah Class Code: `Class code must not be empty`
7. Verifikasi halaman tetap terbuka
8. Verifikasi tab General diberi titik peringatan merah
9. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-98: Class Code lebih dari 15 karakter

10. Kosongkan isi Class Code
11. Ketik Class Code `ABCDEFGHIJKLMNOP` (16 karakter)
12. Verifikasi caption langsung muncul saat mengetik: `Max. 15 characters`
13. Ganti isi Class Code menjadi `ABCDEFGHIJKLMNO` (15 karakter)
14. Verifikasi tidak ada caption pada Class Code

### TC-FA-FAAC-99: Class Code dengan karakter di luar whitelist

15. Ganti isi Class Code dengan `AB#1 x`
16. Verifikasi caption langsung muncul: `Class code contains invalid characters`
17. Ganti isi Class Code menjadi `A-b_1.2`
18. Verifikasi tidak ada caption pada Class Code

### TC-FA-FAAC-100: Class Code sama dengan Asset Class lain tanpa membedakan huruf besar-kecil

19. Ganti isi Class Code dengan `b-anchor` (huruf kecil; `B-ANCHOR` sudah ada) dan tunggu sekitar 500 ms
20. Verifikasi caption muncul setelah jeda ketik (debounce sekitar 500 ms): `Class code already exists`
21. Isi ulang field lain dengan nilai valid: Class Name `Test Class`, Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
22. Catat jumlah entri Changelog Asset Class (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca BE
23. Klik `Submit`
24. Verifikasi halaman tetap terbuka
25. Verifikasi jumlah Asset Class sama dengan N0 (Submit tidak membuat Asset Class)
26. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
27. Verifikasi jumlah entri System Log aktor sama dengan Ns (tidak ada entri baru)
28. Verifikasi jumlah entri Activity Log FAMS sama dengan Na (tidak ada entri baru)

### Penutup

29. Klik breadcrumb `Asset Class`
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-97 sampai 100). Tidak ada TC hanya-BE di spec ini.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 2; tiap TC mengganti isi field yang diuji, bukan membuka form baru. Field lain yang diisi valid pada langkah 4 tetap terisi untuk TC-98 dan TC-99; langkah 21 mengisinya ulang karena TC-100 mensyaratkan field lain valid.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), langkah 10 (mengosongkan Class Code agar TC-98 dimulai dari input kosong), langkah 22 (baseline jumlah entri log tepat sebelum Submit TC-100, S-12), dan langkah 29 sampai 31 (menutup form dirty, S-08).
- Asersi "tidak ada Asset Class dibuat" (langkah 9 dan 25) dibuktikan lewat selisih jumlah terhadap baseline N0 dengan anchor positif berupa caption penolakan pada langkah 6 dan 20. Asersi "tidak ada caption" (langkah 14 dan 18) didahului caption pada field yang sama (langkah 12 dan 16) sebagai anchor.
- S-05: Expected TC-100 butir b "tidak ada entri baru" di Changelog Asset Class, System Log, dan Activity Log diasersi sebagai selisih jumlah entri terhadap baseline (langkah 22, 26 sampai 28; kemampuan baca BE); ini asersi jumlah atas penolakan validasi form, bukan request langsung ditolak (kelas a) dan bukan kelas g. Anchor positif: caption penolakan pada langkah 20 dan halaman tetap terbuka pada langkah 24.
- Temuan untuk QA:
  - TC-97 langkah 2 tidak menyebut apakah spasi di Class Code dipangkas; spec mengasersi caption yang tertulis di Expected.
