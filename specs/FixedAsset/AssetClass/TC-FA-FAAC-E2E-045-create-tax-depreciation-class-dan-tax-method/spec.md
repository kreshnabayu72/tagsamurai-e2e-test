---
id: TC-FA-FAAC-E2E-045-create-tax-depreciation-class-dan-tax-method
title: "Create Asset Class: Tax Method Mengikuti Tax Depreciation Class dan Useful Life & Rate Fiskal Read-Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-126
  - TC-FA-FAAC-127
coverage:
  web: automated
---

# Create Asset Class: Tax Method Mengikuti Tax Depreciation Class dan Useful Life & Rate Fiskal Read-Only

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Tax Depreciation Class `Bangunan permanen` (Active, hanya metode `Straight Line`), `Bukan bangunan – Kelompok 3` (Active, 16 yrs, mengizinkan `Straight Line` dan `Declining Balance`), dan `Bukan bangunan – Kelompok 1` (Active, mengizinkan `Straight Line`). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Spec memilih Tax Depreciation Class dan Tax Method di form Create; satu-satunya Submit (langkah 16) ditolak validasi sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: membaca nilai Useful Life & Rate master Tax Depreciation Class lewat kemampuan baca BE (disediakan tim FE/BE).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`

### TC-FA-FAAC-126: Tax Method dibatasi metode Tax Depreciation Class dan Useful Life & Rate fiskal read-only

3. Verifikasi Useful Life & Rate bernilai `—` sebelum Tax Depreciation Class dipilih
4. Buka Select Tax Depreciation Class
5. Verifikasi opsi Tax Depreciation Class berformat `[Tax Class Name] — [Years] yrs`, misalnya `Bukan bangunan – Kelompok 3 — 16 yrs`
6. Pilih Tax Depreciation Class `Bangunan permanen`
7. Buka select Tax Method
8. Verifikasi opsi `Straight Line` tampil pada Tax Method
9. Verifikasi opsi `Declining Balance` tidak tampil pada Tax Method (Tax Method hanya menawarkan `Straight Line`)
10. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3`
11. Verifikasi Useful Life & Rate terisi sama dengan data master Tax Depreciation Class `Bukan bangunan – Kelompok 3` (dibaca lewat kemampuan baca BE)
12. Verifikasi Useful Life & Rate read-only dan tidak dapat diubah

### TC-FA-FAAC-127: Ganti Tax Depreciation Class mengosongkan Tax Method yang tidak diizinkan dan mempertahankan yang diizinkan

13. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` dan Tax Method `Declining Balance`
14. Ganti Tax Depreciation Class menjadi `Bangunan permanen` (hanya `Straight Line`)
15. Verifikasi Tax Method dikosongkan
16. Klik `Submit`
17. Verifikasi caption pada Tax Method: `Tax method must not be empty`
18. Pilih Tax Method `Straight Line`
19. Ganti Tax Depreciation Class menjadi `Bukan bangunan – Kelompok 1`
20. Verifikasi Tax Method `Straight Line` dipertahankan karena termasuk metode class baru

### Penutup

21. Klik breadcrumb `Asset Class`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-126 dan 127). Tidak ada TC hanya-BE di spec ini. TC-FA-FAAC-128 (Tax Depreciation Class tanpa metode, membuat Asset Class) ada di spec 048.
- Urutan `Verifikasi` TC-126: butir a, d, b, c ditulis menurut urutan state layar (bagian 8b butir 5): `—` sebelum class dipilih (langkah 3), format opsi saat Select terbuka (langkah 5), lalu metode dan nilai fiskal setelah class dipilih. Anchor absence langkah 9 adalah langkah 8.
- Urutan di TC-127: butir c (Submit dengan Tax Method kosong, langkah 16 dan 17) dijalankan sebelum butir b (langkah 18 sampai 20) karena butir c mensyaratkan Tax Method kosong pada class yang punya metode, yaitu state sesudah langkah 14; butir b membutuhkan Tax Method `Straight Line` yang dipilih sesudahnya.
- Langkah penghubung (S-03): langkah 21 sampai 23 (menutup form dirty, S-08). Langkah 13 memilih ulang class dan metode seperti langkah TC-127 walau class `Bukan bangunan – Kelompok 3` sudah terpilih dari langkah 10.
- Temuan untuk QA:
  - TC-127 butir c tidak menyebut field lain saat `Submit`; Submit pada langkah 16 dapat menampilkan caption field wajib lain selain Tax Method, dan hanya caption Tax Method yang diasersi.
  - TC-126 butir c menyebut "tanpa pola teks khusus" untuk nilai Useful Life & Rate; spec membandingkan dengan data master lewat kemampuan baca BE tanpa pola teks.
