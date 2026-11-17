---
id: TC-FA-FAAC-E2E-050-create-berhasil-variasi-method-straight-line-declining-balance-dan-units-of-production
title: "Create Asset Class Berhasil: Variasi Method Straight Line, Declining Balance, dan Units of Production"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-88
  - TC-FA-FAAC-89
  - TC-FA-FAAC-90
sourceRules: ["T-01", "§[F-FAAC-01] Create Asset Class#b5", "ST-01", "§4.1.1#r8", "§4.1.1#r4", "FLD-07"]
smoke: []
dependsOn: []
trace:
  "T-01": [5, 14, 26]
  "§[F-FAAC-01] Create Asset Class#b5": 6
  "ST-01": 6
  "§4.1.1#r8": 7
  "§4.1.1#r4": [17, 29]
  "FLD-07": 22
coverage:
  web: automated
---

# Create Asset Class Berhasil: Variasi Method Straight Line, Declining Balance, dan Units of Production

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Tax Depreciation Class `Bukan bangunan – Kelompok 1` dan `Bukan bangunan – Kelompok 2` Active; plan Multi Depreciation (Enterprise) dengan Max depreciation methods minimal 3, Asset Class lain memakai Straight Line.
- Data yang dibuat spec (nama literal dari TC): Asset Class `B-INACT`, `B-DB`, dan `B-UOP`. Ketiga Class Code belum ada sebelum spec; fixture BE menghapusnya bila ada. Hook `after` menghapus ketiganya lewat fixture BE (pembersihan tidak mengandalkan setup berhasil penuh).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-88: Create sederhana tanpa Asset Name untuk dinonaktifkan

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-INACT`, Class Name `Inactive Candidate`
3. Pada tab Depreciation pilih Method `Straight Line`, isi Useful Life `48`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 1` lalu Tax Method `Straight Line`
4. Klik `[Submit]`
5. Verifikasi toast sukses `Success, asset class has been created.`
6. Verifikasi halaman tetap terbuka dalam mode Edit dengan Badge Status `Active`
7. Verifikasi Asset Names `0`

### TC-FA-FAAC-89: Create dengan Method Declining Balance

8. Klik breadcrumb `Asset Class` untuk kembali ke tabel
9. Klik tombol `[+ Asset Class]` di toolbar tabel
10. Pada tab General isi Class Code `B-DB`, Class Name `Declining Fixture`
11. Pada tab Depreciation pilih Method `Declining Balance`; isi Useful Life `48` dan Declining Rate `50`
12. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 1` lalu Tax Method `Declining Balance`
13. Klik `[Submit]`
14. Verifikasi toast sukses `Success, asset class has been created.`
15. Klik breadcrumb `Asset Class` untuk kembali ke tabel
16. Ketik Search `B-DB`, tekan Enter
17. Verifikasi baris `B-DB` menampilkan Commercial `Declining Balance · 4 yrs · 50%/yr`

### TC-FA-FAAC-90: Create dengan Method Units of Production

18. Klik tombol `[+ Asset Class]` di toolbar tabel
19. Pada tab General isi Class Code `B-UOP`, Class Name `UoP Fixture`
20. Pada tab Depreciation pilih Method `Units of Production`
21. Isi Useful Life `60`
22. Verifikasi helper Useful Life berbunyi `1 to 600 months. Maximum useful life, even if estimated units are not yet used.`
23. Isi Total Estimated Units `80000`, pilih Unit Type `Hour meter`
24. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 2` lalu Tax Method `Straight Line`
25. Klik `[Submit]`
26. Verifikasi toast sukses `Success, asset class has been created.`
27. Klik breadcrumb `Asset Class` untuk kembali ke tabel
28. Ganti isi kotak search dengan `B-UOP`, tekan Enter
29. Verifikasi baris `B-UOP` menampilkan Commercial `Units of Production · 80,000 Hour meter`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-88, 89, 90). TC-FA-FAAC-96 dan TC-FA-FAAC-606 ada di spec 062. Tidak ada TC hanya-BE di spec ini.
- Pengecualian beralasan atas S-06 dan S-12: Class Code dan Class Name literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 8, 15, dan 27 (kembali ke tabel lewat breadcrumb), langkah 16 dan 28 (Search untuk menemukan baris target; langkah 28 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah breadcrumb).
- Langkah 22 diasersi segera setelah Useful Life diisi karena helper terkait nilai yang baru diketik (8b.5).
- Temuan untuk QA:
  - TC-88 dan TC-89 tidak menyebut Plan; TC-89 dan TC-90 mensyaratkan plan Multi Depreciation (Enterprise) dengan Max depreciation methods minimal 2 atau 3. Spec memakai satu client Enterprise dengan nilai minimal 3 untuk ketiga TC.
  - TC-88 judul "untuk dinonaktifkan" tidak punya langkah penonaktifan; Post Condition (Asset Class tersimpan Active tanpa Asset Name) dipakai TC lain dan tidak diasersi tambahan di spec ini.
