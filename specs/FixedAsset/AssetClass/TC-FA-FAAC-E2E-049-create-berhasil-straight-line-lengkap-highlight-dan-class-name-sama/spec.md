---
id: TC-FA-FAAC-E2E-049-create-berhasil-straight-line-lengkap-highlight-dan-class-name-sama
title: "Create Asset Class Berhasil: Method Straight Line Lengkap dengan Akun, Highlight Baris Baru, dan Class Name yang Sama"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-14
  - TC-FA-FAAC-87
  - TC-FA-FAAC-95
sourceRules: ["T-01", "§4.2b#p1", "§[F-FAAC-01] Create Asset Class#b5", "ST-01", "§4.1.2#r4", "§4.1.2#r5", "§5#b13", "ST-02", "§5#b12", "§4.1.1#r1", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r7", "§4.1.1#r3"]
smoke: []
dependsOn: []
trace:
  "T-01": [9, 31]
  "§4.2b#p1": [10, 11]
  "§[F-FAAC-01] Create Asset Class#b5": [10, 12]
  "ST-01": 11
  "§4.1.2#r4": 13
  "§4.1.2#r5": 13
  "§5#b13": [15, 25]
  "ST-02": [16, 26]
  "§5#b12": [16, 26]
  "§4.1.1#r1": 17
  "§4.1.1#r4": 17
  "§4.1.1#r5": 17
  "§4.1.1#r6": 17
  "§4.1.1#r8": 17
  "§4.1.1#r9": 17
  "§4.1.1#r7": 18
  "§4.1.1#r3": 32
coverage:
  web: automated
---

# Create Asset Class Berhasil: Method Straight Line Lengkap dengan Akun, Highlight Baris Baru, dan Class Name yang Sama

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Chart of Accounts memuat akun Active kelima Account Function `11001 – Machinery Cost`, `12001 – Accumulated Depreciation Machinery`, `51001 – Depreciation Expense Machinery`, `81001 – Gain on Disposal`, `82001 – Loss on Disposal`; Tax Depreciation Class `Bukan bangunan – Kelompok 1` dan `Bukan bangunan – Kelompok 3` Active; jumlah Asset Class belum mencapai Master Data Count Limit.
- Data yang dibuat spec (nama literal dari TC): Asset Class `B-ANCHOR`, `HLT-EQ`, dan `B-SAMENAME`. Ketiga Class Code belum ada sebelum spec; fixture BE menghapusnya bila ada. Hook `after` menghapus ketiganya lewat fixture BE (pembersihan tidak mengandalkan setup berhasil penuh); seed `B-ANCHOR` untuk spec lain disediakan ulang fixture BE per spec.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Kemampuan teknis: pengamatan highlight baris sesaat lalu memudar pada tabel (kemampuan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-87: Create dengan semua field termasuk akun, Method Straight Line

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-ANCHOR`, Class Name `Anchor Heavy Equipment`, Description `Asset class fixture group B`
3. Klik tab `Depreciation`
4. Pilih Method `Straight Line`, isi Useful Life `120`, isi Residual Value `10` dengan unit `Percent`
5. Biarkan Depreciation Start Convention `Full month from in-service date`; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Declining Balance`
6. Biarkan Tax Depreciation Start Rule `Month of expenditure`; isi Capitalization Threshold `5000000`
7. Klik tab `Accounts` dan pilih kelima akun: Asset Cost `11001 – Machinery Cost`, Accumulated Depreciation `12001 – Accumulated Depreciation Machinery`, Depreciation Expense `51001 – Depreciation Expense Machinery`, Gain on Disposal `81001 – Gain on Disposal`, Loss on Disposal `82001 – Loss on Disposal`
8. Klik `[Submit]`
9. Verifikasi toast sukses `Success, asset class has been created.`
10. Verifikasi halaman tetap terbuka dalam mode Edit dengan judul `Edit Asset Class`
11. Verifikasi baris `B-ANCHOR – Anchor Heavy Equipment` dengan Badge Status `Active`
12. Verifikasi tab `Asset Names` aktif
13. Verifikasi Last Posted Period dan Last Exported Period bernilai `—`
14. Klik breadcrumb `Asset Class` untuk kembali ke tabel
15. Verifikasi tabel Asset Class berada di sort default Class Code A-Z, Search kosong, Filter kosong, dan menampilkan halaman yang memuat `B-ANCHOR`
16. Verifikasi baris `B-ANCHOR` di-highlight sesaat lalu highlight memudar
17. Verifikasi baris `B-ANCHOR`: toggle Active On; Commercial `Straight Line · 10 yrs · 10%`; Fiscal `Bukan bangunan – Kelompok 3 · Declining Balance`; Capitalization Threshold `5,000,000`; Asset Names `0` sebagai teks biasa; Assets `0`
18. Verifikasi ikon Accounts baris `B-ANCHOR` lengkap (hijau)

### TC-FA-FAAC-14: Baris Asset Class baru di-highlight sesaat lalu memudar

19. Klik tombol `[+ Asset Class]` di toolbar tabel
20. Pada tab General isi Class Code `HLT-EQ`, Class Name `Highlight Equipment`
21. Buka tab `Depreciation`: pilih Method `Straight Line`, isi Useful Life `60`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 1`, pilih Tax Method `Straight Line`; biarkan Depreciation Start Convention dan Tax Depreciation Start Rule pada nilai awal
22. Klik `[Submit]`
23. Tunggu aksi selesai
24. Klik breadcrumb `Asset Class` untuk kembali ke tabel
25. Verifikasi tabel berada di sort default dan menampilkan halaman yang memuat `HLT-EQ`
26. Verifikasi baris `HLT-EQ` ter-highlight sesaat lalu highlight memudar

### TC-FA-FAAC-95: Create dengan Class Name yang sama seperti Asset Class lain

27. Klik tombol `[+ Asset Class]` di toolbar tabel
28. Pada tab General isi Class Code `B-SAMENAME` dan Class Name `Anchor Heavy Equipment` (sama dengan `B-ANCHOR`)
29. Isi field lain dengan nilai valid: Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
30. Klik `[Submit]`
31. Verifikasi toast sukses `Success, asset class has been created.`
32. Verifikasi tidak ada caption error pada Class Name

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-14, 87, 95). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-87 lebih dulu karena TC-95 memakai Class Name `B-ANCHOR` yang dibuat TC-87 (S-10).
- Pengecualian beralasan atas S-06 dan S-12: Class Code dan Class Name literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 14 dan 24 (kembali ke tabel lewat breadcrumb), langkah 23 ("Tunggu aksi selesai" sebelum pindah surface; hasil `[Submit]` TC-14 tidak diasersi langsung). Langkah 5 dan 6 menyalin "biarkan nilai awal" dari TC sebagai aksi tanpa asersi.
- Langkah 16 dan 26 diasersi segera setelah tabel tampil karena highlight bersifat sementara (8b.5).
- Temuan untuk QA:
  - TC-87 menyebut Class Code `B-ANCHOR` sebagai data yang dibuat TC itu sendiri sekaligus "seed Pre-setup" untuk TC lain; spec ini membutuhkan `B-ANCHOR` belum ada di awal, sedangkan spec lain membutuhkannya sudah ada. Fixture BE per spec harus menyiapkan keduanya.
  - TC-87 Expected d ("Asset Names 0 sebagai teks biasa", "Assets 0") disalin sebagai satu `Verifikasi` nilai kolom satu baris; TC-87 tidak menyebut nilai Status baris tabel selain toggle Active On.
