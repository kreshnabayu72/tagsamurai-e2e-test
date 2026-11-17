---
id: TC-FA-FAAC-E2E-046-create-opsi-tax-depreciation-class-disabled-dan-inactive
title: "Create Asset Class: Opsi Tax Depreciation Class Inactive Tidak Ditawarkan dan Select Disabled Bila Tidak Ada Class Active"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-130
  - TC-FA-FAAC-129
sourceRules: ["FAAC-LOGIC-02e", "§4.1.2#r14", "FI-05", "V-19"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02e": [4, 6, 8]
  "§4.1.2#r14": [4, 8]
  "FI-05": [16, 17]
  "V-19": 19
coverage:
  web: automated
---

# Create Asset Class: Opsi Tax Depreciation Class Inactive Tidak Ditawarkan dan Select Disabled Bila Tidak Ada Class Active

## Prerequisites

- Mode: FE+BE
- Akun aktor awal: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-129): Total Control pada client seed khusus yang semua Tax Depreciation Class-nya berstatus Inactive. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_NOTAXCLASS_PASSWORD` (nama usulan, belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE).
- Data Pre-setup (hanya dibaca): Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active) dan `Bukan bangunan – Kelompok 4` (Inactive) pada client akun aktor awal; seluruh Tax Depreciation Class berstatus Inactive pada client seed khusus. Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Spec tidak membuat Asset Class (Submit pada langkah 18 ditolak validasi) sehingga tidak ada cleanup.
- Kemampuan teknis: membaca daftar Tax Depreciation Class berstatus Inactive lewat kemampuan baca BE (disediakan tim FE/BE); ganti akun dan client lewat logout dan login.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`. Flag Guided Tooltip untuk akun aktor kedua disetel true oleh hook `before` spec ini dan dipulihkan hook `after`.
- State global: tidak ada yang diubah. Hook `after` mengembalikan sesi ke akun default suite.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-130: Tax Depreciation Class Inactive tidak ditawarkan di Select

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`
3. Buka Select Tax Depreciation Class
4. Verifikasi opsi `Bukan bangunan – Kelompok 3` (Active) tampil
5. Cari `Kelompok 4` pada Select Tax Depreciation Class
6. Verifikasi Tax Depreciation Class `Bukan bangunan – Kelompok 4` (Inactive) tidak ada di daftar opsi
7. Kosongkan pencarian pada Select Tax Depreciation Class
8. Verifikasi daftar opsi hanya memuat Tax Depreciation Class berstatus Active (tidak ada nama dari daftar Tax Depreciation Class Inactive menurut kemampuan baca BE)
9. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-129: Select Tax Depreciation Class Disabled bila tidak ada class Active

10. Logout
11. Login sebagai Total Control client seed khusus (semua Tax Depreciation Class Inactive)
12. Buka Fixed Asset > Settings > Accounting > tab Asset Class
13. Klik tombol `+ Asset Class` di toolbar tabel
14. Klik tab `Depreciation`
15. Klik Select Tax Depreciation Class
16. Verifikasi Select Tax Depreciation Class Disabled
17. Verifikasi daftar opsi Select Tax Depreciation Class tidak terbuka (tidak dapat dibuka)
18. Klik `Submit`
19. Verifikasi caption: `Tax depreciation class must not be empty`
20. Klik breadcrumb `Asset Class`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-130 dan 129). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di dalam spec: TC-130 lebih dulu, TC-129 sesudahnya. Alasannya: TC-129 membutuhkan client lain sehingga ganti akun (langkah 10 sampai 12) diletakkan di tengah spec dan bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (bagian 3, pemisah beda akun butir b); sesi dikembalikan ke akun default oleh hook `after`.
- Langkah penghubung (S-03): langkah 2 (klik tab Depreciation sesuai TC), langkah 7 (mengosongkan pencarian agar langkah 8 mengamati seluruh daftar), langkah 9 dan 20 (menutup form Create; form belum berisi isian sehingga tidak ada dialog `Unsaved Changes` yang diasersi). Langkah 12 membuka layar secara eksplisit sesudah ganti akun (S-07).
- Asersi absence langkah 6 didahului langkah 4 dan langkah 17 didahului langkah 16 sebagai anchor positif pada surface yang sama (bagian 8b butir 2). Asersi "hanya class Active" pada langkah 8 memakai daftar Inactive dari kemampuan baca BE.
- Temuan untuk QA:
  - TC-129 mensyaratkan "client seed khusus Pre-setup" tanpa menyebut akun Total Control client itu di Tabel Data Uji Pre-setup; Email akun ini tidak tertulis di Pre-setup TC dan disediakan tim FE.
  - TC-129 butir b ("Submit tetap menampilkan caption") tidak menyebut isian field lain; Submit pada langkah 18 dapat menampilkan caption field wajib lain, dan hanya caption Tax Depreciation Class yang diasersi.
  - TC-130 butir b ("Hanya class Active yang ditawarkan") tidak menyebut daftar class Active yang diharapkan; langkah 8 membandingkan dengan daftar Inactive.
