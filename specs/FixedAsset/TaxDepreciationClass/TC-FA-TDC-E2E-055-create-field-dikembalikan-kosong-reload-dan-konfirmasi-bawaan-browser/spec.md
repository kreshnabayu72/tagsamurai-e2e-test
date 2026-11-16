---
id: TC-FA-TDC-E2E-055-create-field-dikembalikan-kosong-reload-dan-konfirmasi-bawaan-browser
title: "Create - Field Dikembalikan Kosong, Reload, dan Konfirmasi Bawaan Browser"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-123
  - TC-FA-TDC-124
  - TC-FA-TDC-125
sourceRules: ["§4.2c#b1", "FI-09"]
smoke: []
dependsOn: []
trace:
  "§4.2c#b1": [5, 6, 10, 15, 21]
  "FI-09": 22
anchor: [14, 20]
coverage:
  web: automated
---

# Create - Field Dikembalikan Kosong, Reload, dan Konfirmasi Bawaan Browser

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; sesudah satu Create tabel berisi 8 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-13` belum ada (tersimpan); `KHS` dan `KHS-12` hanya diketik dan tidak disimpan. Form valid: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok khusus uji 13`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line` dan `Declining Balance`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Kemampuan teknis: menangani dialog `beforeunload` bawaan browser (diamati lalu dikonfirmasi untuk melanjutkan muat ulang); disediakan tim FE.
- Pemulihan: hook `after` menghapus `KHS-13` lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-123: Field diubah lalu dikembalikan kosong dianggap clean saat menutup Drawer Create

1. Klik `+ Class` di toolbar
2. Ketik `KHS` pada Class Code
3. Hapus semua karakter pada Class Code hingga kosong
4. Klik ikon ✕
5. Verifikasi Drawer langsung tertutup
6. Verifikasi dialog Unsaved Changes tidak muncul

### TC-FA-TDC-124: Reload halaman saat Drawer Create terisi memunculkan konfirmasi bawaan browser

7. Klik `+ Class` di toolbar
8. Isi Class Code `KHS-12`
9. Tekan F5
10. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang
11. Konfirmasi dialog `beforeunload` untuk melanjutkan muat ulang
12. Klik `+ Class` di toolbar
13. Tekan F5 dengan Drawer Create kosong
14. Verifikasi halaman Tax Depreciation Class termuat ulang (tabel tampil)
15. Verifikasi tidak ada konfirmasi bawaan browser

### TC-FA-TDC-125: Konfirmasi bawaan browser tidak muncul setelah Submit berhasil

16. Klik `+ Class` di toolbar
17. Isi form valid dengan Class Code `KHS-13` lalu klik `[Submit]`
18. Tunggu Drawer menutup
19. Tekan F5
20. Verifikasi halaman Tax Depreciation Class termuat ulang (tabel tampil)
21. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
22. Verifikasi baris `KHS-13` tetap ada di tabel

## Notes

- Langkah penghubung (S-03): langkah 11 (mengonfirmasi dialog `beforeunload` agar muat ulang berlanjut; kemampuan ditulis di Prerequisites sesuai S-08), langkah 12 (membuka Drawer Create kosong untuk bagian "ulangi dengan Drawer Create kosong"), langkah 18 (menunggu Drawer menutup sesudah Submit).
- Langkah 12 dan 13 memakai Drawer Create kosong sesuai langkah 4 TC-FA-TDC-124 ("Ulangi dengan Drawer Create kosong"), dengan aksi yang sama (F5).
- Asersi absence langkah 15 dan 21 didahului anchor positif langkah 14 dan 20 (tabel tampil sesudah muat ulang; R-21).
- Jumlah pembukaan Drawer Create (langkah 1, 7, 12, 16) tidak lebih dari jumlah penutupan: dua ditutup ikon ✕ atau Submit (langkah 4 dan 17) dan dua hilang karena muat ulang (langkah 11 dan 13) (S-10).
- Pembagian TC lintas spec: penutupan Drawer lewat ikon, Esc, backdrop, Leave, dan Cancel (TC-FA-TDC-118 sampai 122) ada di spec `TC-FA-TDC-E2E-054-create-menutup-drawer-ikon-esc-backdrop-leave-dan-cancel-dialog`.
- Temuan untuk QA:
  - TC-FA-TDC-124 langkah 4 ("Ulangi dengan Drawer Create kosong") tidak menyebut aksi yang diulang; spec mengulang aksi F5 (langkah 13) sesuai Expected b ("halaman dimuat ulang tanpa konfirmasi").
  - TC-FA-TDC-125 langkah 3 ("Setelah Drawer menutup") tidak punya Expected untuk penutupan Drawer; spec menunggu penutupan sebagai langkah penghubung.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
