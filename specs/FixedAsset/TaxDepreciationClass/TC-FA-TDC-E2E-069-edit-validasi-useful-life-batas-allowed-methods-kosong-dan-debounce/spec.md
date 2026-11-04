---
id: TC-FA-TDC-E2E-069-edit-validasi-useful-life-batas-allowed-methods-kosong-dan-debounce
title: "Edit: Validasi Batas Useful Life 1 sampai 100, Allowed Methods Kosong, dan Debounce Keunikan Class Code"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-241
  - TC-FA-TDC-242
  - TC-FA-TDC-243
  - TC-FA-TDC-246
coverage:
  web: automated
---

# Edit: Validasi Batas Useful Life 1 sampai 100, Allowed Methods Kosong, dan Debounce Keunikan Class Code

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data (seed idempotent di hook `before` lewat API; class `KHS-E1` dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `nb1` | `NB-1` | Pre-setup Example Data (Used By 5); hanya sebagai pembanding duplikat, tidak diubah |

- Nilai Useful Life TC-FA-TDC-241 (dipakai langkah 3 sampai 5, satu iterasi per baris): `0`, `101`, `150`, `1.5`.
- Nilai Useful Life TC-FA-TDC-242 (dipakai langkah 6 sampai 8, satu iterasi per baris): `1`, `100`.
- Kemampuan teknis: pembacaan nilai class lewat fixture BE untuk `Verifikasi` "tidak ada data tersimpan" pada langkah 14; disediakan tim FE/BE tanpa endpoint karangan (S-11).
- Tidak ada Save yang berhasil di spec ini: Save pada langkah 11 diblokir validasi dan form berakhir dalam keadaan bersih (semua nilai dipulihkan ke nilai tersimpan).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`

### TC-FA-TDC-241: Useful Life di luar 1 sampai 100 atau bukan bilangan bulat ditolak

Untuk setiap nilai Useful Life TC-FA-TDC-241 pada `## Prerequisites` (langkah 3 sampai 5):

3. Ganti isi Useful Life dengan nilai baris
4. Verifikasi caption `Useful life must be between 1 and 100 years` muncul segera pada Useful Life
5. Ganti isi Useful Life dengan `8`

### TC-FA-TDC-242: Useful Life 1 dan 100 diterima

Untuk setiap nilai Useful Life TC-FA-TDC-242 pada `## Prerequisites` (langkah 6 sampai 8):

6. Ganti isi Useful Life dengan nilai baris
7. Verifikasi field Useful Life berisi nilai baris
8. Verifikasi tidak ada caption error pada Useful Life

9. Ganti isi Useful Life dengan `8`

### TC-FA-TDC-243: Allowed Methods kosong pada Asset Type Non-building ditolak

10. Lepas semua pilihan pada Allowed Methods (hapus chip `Straight Line` dan `Declining Balance`)
11. Klik `[Save]`
12. Verifikasi caption `Allowed methods must not be empty` muncul pada Allowed Methods
13. Verifikasi Drawer tetap terbuka
14. Verifikasi tidak ada data tersimpan: Allowed Methods class `KHS-E1` tetap `Straight Line` dan `Declining Balance` (dibaca lewat fixture BE)
15. Pilih kembali `Straight Line` dan `Declining Balance` pada Allowed Methods

### TC-FA-TDC-246: Pengecekan keunikan Class Code berjalan setelah jeda sekitar 500 ms

16. Ganti isi Class Code dengan `NB-1` karakter demi karakter dengan jeda antar karakter di bawah 300 ms
17. Verifikasi field Class Code berisi `NB-1`
18. Verifikasi selama mengetik tanpa jeda caption `Class code already exists` tidak muncul
19. Berhenti mengetik dan tunggu sekitar 500 ms
20. Verifikasi caption `Class code already exists` muncul pada Class Code
21. Ganti isi Class Code dengan `KHS-E1`
22. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 Search `KHS-E1` agar baris target ada di halaman teramati (R-16, 8b.13); langkah 5, 9, 15, dan 21 mengembalikan field ke nilai tersimpan sehingga caption sebelumnya hilang dan Drawer berakhir bersih (R-12, S-09); langkah 22 menutup Drawer yang bersih (tanpa dialog Unsaved Changes). Langkah 19 menunggu jeda debounce sekitar 500 ms (di bawah batas ±30 detik).
- Langkah berulang: langkah 3 sampai 5 diulang untuk empat nilai dan langkah 6 sampai 8 untuk dua nilai (8b.7); `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi, jumlah langkah efektif sekitar 35.
- Urutan TC: TC-FA-TDC-241, TC-FA-TDC-242, TC-FA-TDC-243, lalu TC-FA-TDC-246 (S-10). Pada TC-FA-TDC-242, `Verifikasi` nilai tampil mendahului `Verifikasi` tidak ada caption sebagai anchor (8b.2); urutan Expected TC (a: tidak ada caption pada `1`, b: tidak ada caption pada `100`) dipertahankan per iterasi.
- Langkah 18 (caption tidak muncul selama mengetik) ditulis sebelum langkah berikutnya mengubah state (8b.5) dan memakai langkah 17 sebagai anchor. Langkah 14 (tidak ada data tersimpan, dibaca lewat fixture BE): caption langkah 12 dan Drawer tetap terbuka (langkah 13) menjadi anchor.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - Kolom Data Uji TC-FA-TDC-240 dan TC-FA-TDC-243 memuat nilai field lain (Class Code `KHS-M1`, Class Name `Kelompok uji validasi`, dan sebagainya) seperti form Create; langkah TC hanya mengubah satu field pada class `KHS-E1` yang sudah terisi, sehingga nilai itu tidak dipakai (S-15).
  - Post Condition "Tidak ada data berubah dan tidak ada entri log" TC-FA-TDC-241 sampai TC-FA-TDC-243 tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-TDC-246 tidak menyebut klik `[Save]` setelah caption duplikat muncul; spec mengikuti TC.
  - Pemilihan ulang Allowed Methods pada langkah 15 (`Straight Line` dan `Declining Balance`) memulihkan nilai tersimpan; urutan chip hasil pemilihan ulang dapat berbeda dari urutan asli, tetapi nilai yang dibandingkan form dirty tidak bergantung urutan (asumsi spec).
