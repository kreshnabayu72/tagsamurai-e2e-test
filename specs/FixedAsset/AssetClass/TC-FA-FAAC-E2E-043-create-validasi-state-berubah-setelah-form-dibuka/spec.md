---
id: TC-FA-FAAC-E2E-043-create-validasi-state-berubah-setelah-form-dibuka
title: "Create Asset Class: Submit Ditolak Saat Tax Depreciation Class, Tax Method, atau Akun Berubah Setelah Form Dibuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-118
  - TC-FA-FAAC-119
  - TC-FA-FAAC-120
coverage:
  web: automated
---

# Create Asset Class: Submit Ditolak Saat Tax Depreciation Class, Tax Method, atau Akun Berubah Setelah Form Dibuka

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (diubah sementara lalu dipulihkan): Tax Depreciation Class `Bukan bangunan – Kelompok 2` (Active, mengizinkan Tax Method `Declining Balance`) dan akun Chart of Accounts `11001 – Machinery Cost` (Active). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Semua Submit di spec ini ditolak validasi sehingga tidak ada Asset Class yang dibuat; Class Code `B-S35`, `B-S36`, `B-S28` adalah input uji kebijakan yang submit-nya diblokir dan boleh literal.
- Kemampuan teknis: membaca jumlah Asset Class lewat kemampuan baca BE untuk baseline N0 (disediakan tim FE/BE). Sesi API aktor Total Control (pelaku kedua yang hanya memicu perubahan state: menonaktifkan dan mengaktifkan kembali Tax Depreciation Class, menghapus dan menambahkan kembali metode yang diizinkan, menonaktifkan dan mengaktifkan kembali akun Chart of Accounts) dinyatakan di `suite.md`.
- State global: Tax Depreciation Class `Bukan bangunan – Kelompok 2`, metode `Declining Balance` miliknya, dan akun `11001 – Machinery Cost` diubah lalu dipulihkan oleh langkah penghubung di spec ini; hook `after` memulihkan ketiganya bila spec berhenti di tengah dan efek pada Last Updated master tidak diasersi. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel

### TC-FA-FAAC-118: Submit dengan Tax Depreciation Class yang menjadi Inactive setelah form dibuka

3. Isi Class Code `B-S35` dan field wajib lain dengan Tax Depreciation Class `Bukan bangunan – Kelompok 2` (jangan klik `Submit` dulu)
4. Lewat sesi API aktor Total Control, nonaktifkan Tax Depreciation Class `Bukan bangunan – Kelompok 2` hingga perubahan tersimpan
5. Klik `Submit` pada form
6. Verifikasi caption pada field Tax Depreciation Class: `This tax depreciation class no longer exists. Please select another.`
7. Verifikasi Select Tax Depreciation Class dikosongkan otomatis
8. Buka Select Tax Depreciation Class
9. Verifikasi sedikitnya satu opsi Tax Depreciation Class Active lain tampil
10. Verifikasi opsi `Bukan bangunan – Kelompok 2` tidak ada di daftar opsi
11. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)
12. Lewat sesi API aktor Total Control, aktifkan kembali Tax Depreciation Class `Bukan bangunan – Kelompok 2` hingga perubahan tersimpan

### TC-FA-FAAC-119: Submit dengan Tax Method yang tidak lagi diizinkan Tax Depreciation Class

13. Ganti isi Class Code dengan `B-S36`; isi field wajib lain dengan Tax Depreciation Class `Bukan bangunan – Kelompok 2` dan Tax Method `Declining Balance` (jangan klik `Submit` dulu)
14. Lewat sesi API aktor Total Control, hapus `Declining Balance` dari metode yang diizinkan Tax Depreciation Class `Bukan bangunan – Kelompok 2` hingga perubahan tersimpan
15. Klik `Submit` pada form
16. Verifikasi caption pada field Tax Method: `Selected tax method is not allowed for this tax depreciation class`
17. Buka Select Tax Method
18. Verifikasi sedikitnya satu opsi Tax Method lain tampil
19. Verifikasi opsi `Declining Balance` tidak ada di daftar opsi
20. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)
21. Lewat sesi API aktor Total Control, tambahkan kembali `Declining Balance` ke metode yang diizinkan Tax Depreciation Class `Bukan bangunan – Kelompok 2` hingga perubahan tersimpan

### TC-FA-FAAC-120: Submit dengan akun yang menjadi Inactive setelah form dibuka

22. Ganti isi Class Code dengan `B-S28`; isi field wajib lain dan pada tab Accounts pilih Asset Cost `11001 – Machinery Cost` (jangan klik `Submit` dulu)
23. Lewat sesi API aktor Total Control, nonaktifkan akun `11001 – Machinery Cost` di Chart of Accounts hingga perubahan tersimpan
24. Klik `Submit` pada form
25. Verifikasi caption pada Asset Cost: `This account no longer exists. Please select another.`
26. Verifikasi Select Asset Cost dikosongkan otomatis
27. Buka Select Asset Cost
28. Verifikasi sedikitnya satu opsi akun Active lain tampil
29. Verifikasi opsi `11001 – Machinery Cost` tidak ada di daftar opsi
30. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)
31. Lewat sesi API aktor Total Control, aktifkan kembali akun `11001 – Machinery Cost` hingga perubahan tersimpan

### Penutup

32. Klik breadcrumb `Asset Class`
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-118 sampai 120). Tidak ada TC hanya-BE di spec ini.
- Pelaku kedua ("sesi lain Total Control" pada TC) memakai sesi API aktor yang hanya memicu perubahan state; hasil di sesi itu tidak diasersi, sehingga bukan kelas c dan tidak memakai `P-2` (keputusan 2026-10-30). Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 2 dan tiap TC melanjutkan isian TC sebelumnya.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), langkah 12, 21, dan 31 (memulihkan state master yang diubah pelaku kedua agar TC berikutnya memakai class, metode, dan akun Active), serta langkah 32 sampai 34 (menutup form dirty, S-08). Langkah 9, 18, 28 adalah anchor positif untuk asersi absence opsi pada langkah 10, 19, 29 (bagian 8b butir 2).
- Asersi "tidak ada Asset Class dibuat" (langkah 11, 20, 30) memakai selisih terhadap baseline N0 dengan anchor positif berupa caption penolakan.
- Temuan untuk QA:
  - Kolom Otomasi TC-118, TC-119, dan TC-120 memuat "Manual Only — (d) butuh dua sesi paralel"; spec memakai sesi API aktor sebagai pelaku kedua sehingga TC dapat diotomasi. Konfirmasi bahwa kemampuan sesi API aktor (mengubah Tax Depreciation Class, metode yang diizinkan, dan akun Chart of Accounts) tersedia dari tim FE/BE.
  - TC-118 butir b ("opsinya dimuat ulang tanpa class yang Inactive") dan TC-119 butir b ("Opsi dimuat ulang") tidak menyebut opsi yang diasersi; spec mengasersi bahwa opsi yang diubah tidak ada dan opsi lain tampil.
  - TC-119 tidak menyebut metode lain yang tersisa pada Tax Depreciation Class `Bukan bangunan – Kelompok 2`; anchor pada langkah 18 mengasumsikan sedikitnya satu metode lain tersisa.
