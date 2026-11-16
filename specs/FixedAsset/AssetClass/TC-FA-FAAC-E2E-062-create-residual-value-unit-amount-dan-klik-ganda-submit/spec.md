---
id: TC-FA-FAAC-E2E-062-create-residual-value-unit-amount-dan-klik-ganda-submit
title: "Create Asset Class: Residual Value Unit Amount dan Klik Ganda Submit Hanya Memproses Satu Permintaan"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-96
  - TC-FA-FAAC-606
sourceRules: ["T-01", "§4.1.1#r4", "§4.1.1#b6", "ST-13", "E-FAAC-80", "L-01", "§8.2#p1", "§8.3#p1"]
smoke: []
dependsOn: []
trace:
  "T-01": 6
  "§4.1.1#r4": 9
  "§4.1.1#b6": 9
  "ST-13": 16
  "E-FAAC-80": 21
  "L-01": 22
  "§8.2#p1": 23
  "§8.3#p1": 24
coverage:
  web: automated
---

# Create Asset Class: Residual Value Unit Amount dan Klik Ganda Submit Hanya Memproses Satu Permintaan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Tax Depreciation Class `Bukan bangunan – Kelompok 3` Active.
- Data yang dibuat spec (nama literal dari TC): Asset Class `B-RESAMT` dan `B-DBL`. Kedua Class Code belum ada sebelum spec; fixture BE menghapusnya bila ada. Hook `after` menghapus keduanya lewat fixture BE (pembersihan tidak mengandalkan setup berhasil penuh).
- Kemampuan teknis: `Spectra.intercept` parsial di atas backend nyata untuk menahan respons permintaan pembuatan Asset Class lalu melepasnya (agar state Loading tombol `[Submit]` dan klik ganda teramati; kemampuan disediakan tim FE, tanpa endpoint karangan); membaca jumlah entri Create untuk Class Code `B-DBL` pada Changelog Asset Class, System Log aktor, dan Activity Log FAMS lewat kemampuan baca BE (audit trail permanen; asersi memakai selisih terhadap baseline).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-96: Create dengan Residual Value unit Amount

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-RESAMT`, Class Name `Residual Amount Fixture`
3. Isi field lain dengan nilai valid: Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
4. Pilih unit `Amount` pada Residual Value dan isi `2000000`
5. Klik `[Submit]`
6. Verifikasi toast sukses `Success, asset class has been created.`
7. Klik breadcrumb `Asset Class` untuk kembali ke tabel
8. Ketik Search `B-RESAMT`, tekan Enter
9. Verifikasi baris `B-RESAMT` menampilkan Commercial `Straight Line · 5 yrs · 2,000,000` (nominal tanpa simbol mata uang)

### TC-FA-FAAC-606: Klik ganda Submit hanya memproses satu permintaan

10. Catat jumlah entri Create untuk Class Code `B-DBL` pada Changelog Asset Class (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca BE
11. Klik tombol `[+ Asset Class]` di toolbar tabel
12. Pada tab General isi Class Code `B-DBL`, Class Name `Test Class`
13. Isi field lain dengan nilai valid: Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
14. Tahan respons permintaan pembuatan Asset Class (intercept)
15. Klik ganda cepat tombol `[Submit]`
16. Verifikasi tombol `[Submit]` non-interaktif dengan spinner selama permintaan
17. Lepas tahanan respons
18. Tunggu aksi selesai
19. Klik breadcrumb `Asset Class` untuk kembali ke tabel
20. Ganti isi kotak search dengan `B-DBL`, tekan Enter
21. Verifikasi hanya satu baris `B-DBL` tampil (satu Asset Class `B-DBL` dibuat)
22. Verifikasi jumlah entri Create untuk `B-DBL` pada Changelog Asset Class bertambah tepat satu dari Nc
23. Verifikasi jumlah entri Create untuk `B-DBL` pada System Log aktor bertambah tepat satu dari Ns
24. Verifikasi jumlah entri Create untuk `B-DBL` pada Activity Log FAMS bertambah tepat satu dari Na

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-96, 606). Tidak ada TC hanya-BE di spec ini. Pembagian TC lintas spec: TC-FA-FAAC-88, 89, dan 90 (variasi Method) ada di spec 050.
- Pengecualian beralasan atas S-06 dan S-12: Class Code dan Class Name literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 7 dan 19 (kembali ke tabel lewat breadcrumb), langkah 8 dan 20 (Search untuk menemukan baris target; langkah 20 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah breadcrumb, 8b.9), langkah 10 (baseline tiga surface log, S-12), langkah 14 dan 17 (menahan dan melepas respons agar state Loading teramati; intercept dilepas segera sesudah asersi langkah 16, S-09), langkah 18 ("Tunggu aksi selesai" sebelum pindah surface).
- Langkah 16 diasersi sebelum respons dilepas karena spinner bersifat sementara (8b.5, 8b.11).
- Temuan untuk QA:
  - TC-606 tidak menyebut Class Name; spec memakai `Test Class` dari TC Create lain.
  - TC-606 menyebut satu entri Create di Changelog Asset Class, System Log, dan Activity Log tanpa cara membaca ketiganya; spec memakai kemampuan baca BE sebagai selisih terhadap baseline (langkah 10, 22 sampai 24).
  - TC-606 tidak menyebut cara membuat klik ganda terjadi saat permintaan berjalan; spec menahan respons lewat intercept (kemampuan disediakan tim FE).
