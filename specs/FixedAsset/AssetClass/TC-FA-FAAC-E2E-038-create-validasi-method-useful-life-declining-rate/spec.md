---
id: TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate
title: "Create Asset Class: Validasi Method, Useful Life, dan Declining Rate"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-105
  - TC-FA-FAAC-106
  - TC-FA-FAAC-107
  - TC-FA-FAAC-108
  - TC-FA-FAAC-109
coverage:
  web: automated
---

# Create Asset Class: Validasi Method, Useful Life, dan Declining Rate

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active, mengizinkan Tax Method `Declining Balance`). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Semua Submit di spec ini ditolak validasi sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup; Class Code `B-X2`, `B-X3`, `B-X4` dan nilai uji lain adalah input uji kebijakan yang submit-nya diblokir dan boleh literal.
- Kemampuan teknis: membaca jumlah Asset Class lewat kemampuan baca BE (disediakan tim FE/BE) untuk baseline N0 sebelum Submit pertama.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel

### TC-FA-FAAC-105: Submit dengan Method belum dipilih

3. Isi Class Code `B-X2` dan Class Name `X2`; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` dan Tax Method `Declining Balance`; biarkan Method kosong
4. Klik `Submit`
5. Verifikasi caption di bawah Method: `Method must not be empty`
6. Verifikasi tab Depreciation diberi titik peringatan
7. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-106: Submit Straight Line dengan Useful Life kosong

8. Ganti isi Class Code dengan `B-X3` dan Class Name dengan `X3`; pilih Method `Straight Line` tanpa mengisi Useful Life
9. Klik `Submit`
10. Verifikasi caption: `Useful life must not be empty`
11. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-107: Useful Life di luar rentang 1 sampai 600

12. Ketik Useful Life `0`
13. Verifikasi caption langsung muncul: `Useful life must be between 1 and 600 months`
14. Ganti isi Useful Life menjadi `601`
15. Verifikasi caption langsung muncul: `Useful life must be between 1 and 600 months`
16. Ganti isi Useful Life menjadi `1`
17. Verifikasi tidak ada caption pada Useful Life
18. Ganti isi Useful Life menjadi `600`
19. Verifikasi tidak ada caption pada Useful Life

### TC-FA-FAAC-108: Submit Declining Balance dengan Declining Rate kosong

20. Ganti isi Class Code dengan `B-X4` dan Class Name dengan `X4`; pilih Method `Declining Balance` dan isi Useful Life `48` tanpa mengisi Declining Rate
21. Klik `Submit`
22. Verifikasi caption: `Declining rate must not be empty`
23. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-109: Declining Rate di luar rentang lebih dari 0 sampai 100

24. Ketik Declining Rate `0`
25. Verifikasi caption langsung muncul: `Declining rate must be between 0 and 100`
26. Ganti isi Declining Rate menjadi `100.01`
27. Verifikasi caption langsung muncul: `Declining rate must be between 0 and 100`
28. Ganti isi Declining Rate menjadi `100`
29. Verifikasi tidak ada caption pada Declining Rate
30. Ganti isi Declining Rate menjadi `0.01`
31. Verifikasi tidak ada caption pada Declining Rate

### Penutup

32. Klik breadcrumb `Asset Class`
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-105 sampai 109). Tidak ada TC hanya-BE di spec ini.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 2 dan tiap TC melanjutkan isian TC sebelumnya. Tax Depreciation Class dan Tax Method yang diisi pada langkah 3 tetap terisi untuk TC-106 sampai TC-109 (TC mensyaratkan keduanya valid).
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12) dan langkah 32 sampai 34 (menutup form dirty, S-08). Penggantian Class Code dan Class Name pada langkah 8 dan 20 mengikuti TC-106 dan TC-108.
- Asersi "tidak ada Asset Class dibuat" (langkah 7, 11, 23) memakai selisih terhadap baseline N0 dengan anchor positif berupa caption penolakan pada langkah yang mendahuluinya. Asersi "tidak ada caption" (langkah 17, 19, 29, 31) didahului caption pada field yang sama (langkah 13, 15, 25, 27).
- Temuan untuk QA:
  - TC-106 tidak menyebut apakah field Declining Rate atau field Method lain perlu diasersi; hanya caption `Useful life must not be empty` yang diasersi sesuai Expected.
