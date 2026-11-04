---
id: TC-FA-TDC-E2E-066-edit-validasi-class-code-duplikat-trim-dan-class-name-kosong
title: "Edit: Validasi Class Code Duplikat, Class Name Kosong, dan Class Code Disimpan Ter-trim"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-225
  - TC-FA-TDC-226
  - TC-FA-TDC-227
  - TC-FA-TDC-228
  - TC-FA-TDC-229
coverage:
  web: automated
---

# Edit: Validasi Class Code Duplikat, Class Name Kosong, dan Class Code Disimpan Ter-trim

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Kemampuan teknis: kemampuan baca jumlah entri Changelog tax depreciation class sebelum aksi (audit trail permanen, N tidak dapat diturunkan dari seeding); disediakan tim FE/BE tanpa endpoint karangan (S-11, 8b.10). Asersi memakai selisih terhadap N yang dicatat pada langkah 16. Kemampuan baca nilai class (Class Name) lewat fixture BE untuk `Verifikasi` "tidak ada data tersimpan" pada langkah 14; disediakan tim FE/BE tanpa endpoint karangan (S-11).
- Data (seed idempotent di hook `before` lewat API; class `KHS-*` dihapus di hook `after`, termasuk class hasil ganti kode `KHS-T1`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `nb1` | `NB-1` | Pre-setup Example Data (Used By 5, Active); hanya sebagai pembanding duplikat, tidak diubah |

- Nilai Class Code duplikat yang diuji (dipakai langkah 3 sampai 5, satu iterasi per baris):

| No | TC | Nilai Class Code | Keterangan |
|---|---|---|---|
| 1 | TC-FA-TDC-225 | `NB-1` | sama persis dengan class lain |
| 2 | TC-FA-TDC-226 | `nb-1` | berbeda kapitalisasi |
| 3 | TC-FA-TDC-226 | `Nb-1` | berbeda kapitalisasi |
| 4 | TC-FA-TDC-227 | ` NB-1 ` (spasi di awal dan akhir) | sama dengan `NB-1` setelah trim |

- Class Code `KHS-T1` belum ada saat spec mulai; hook `before` memastikannya dengan menghapus sisa run sebelumnya.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`

### TC-FA-TDC-225, TC-FA-TDC-226, TC-FA-TDC-227: Class Code sama dengan class lain ditolak

Untuk setiap baris tabel nilai Class Code duplikat pada `## Prerequisites` (langkah 3 sampai 5):

3. Ganti isi Class Code dengan nilai baris lalu berhenti mengetik
4. Verifikasi sekitar 500 ms setelah berhenti mengetik caption `Class code already exists` muncul pada Class Code
5. Ganti isi Class Code dengan `KHS-E1`

### TC-FA-TDC-229: Class Name kosong atau hanya spasi ditolak

6. Hapus seluruh isi Class Name
7. Klik `[Save]`
8. Verifikasi caption `Class name must not be empty` muncul pada Class Name
9. Ganti isi Class Name dengan `Kelompok edit uji`
10. Isi Class Name dengan tiga spasi (`   `)
11. Klik `[Save]`
12. Verifikasi caption `Class name must not be empty` muncul pada Class Name
13. Verifikasi Drawer tetap terbuka
14. Verifikasi tidak ada data tersimpan: Class Name class `KHS-E1` tetap `Kelompok edit uji` (dibaca lewat fixture BE)
15. Ganti isi Class Name dengan `Kelompok edit uji`

### TC-FA-TDC-228: Class Code dengan spasi tepi disimpan ter-trim

16. Catat jumlah entri Changelog tax depreciation class sebagai N
17. Ganti isi Class Code dengan `  KHS-T1  ` (dua spasi di awal dan akhir)
18. Klik `[Save]`
19. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
20. Ganti isi kotak search dengan `KHS-T1`, tekan Enter
21. Verifikasi baris tabel menampilkan Class Code `KHS-T1` tanpa spasi tepi
22. Buka popup Changelog lewat ikon Changelog pada Table Tools
23. Verifikasi jumlah entri Changelog menjadi N + 1
24. Verifikasi entri Changelog teratas: L-02 dengan Old Value `KHS-E1` dan New Value `KHS-T1`
25. Tutup popup Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 20 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13); langkah 5 mengembalikan Class Code ke `KHS-E1` sehingga caption sebelumnya hilang sebelum nilai berikutnya diasersi (R-12); langkah 9 dan 15 mengembalikan Class Name ke nilai tersimpan; langkah 25 menutup popup Changelog.
- Langkah berulang: langkah 3 sampai 5 diulang untuk empat baris tabel nilai (8b.7); `Verifikasi` tetap satu per klausa (S-01).
- Urutan TC: validasi diblokir lebih dulu (TC-FA-TDC-225 sampai TC-FA-TDC-227, lalu TC-FA-TDC-229), aksi sukses terakhir (TC-FA-TDC-228) (S-10). Drawer `KHS-E1` yang sama dipakai berturut-turut tanpa dibuka ulang karena nilai field dipulihkan ke nilai tersimpan pada langkah 5 dan 15 (S-09).
- Langkah 14 (tidak ada data tersimpan): dibaca lewat fixture BE; caption langkah 12 dan Drawer tetap terbuka (langkah 13) menjadi anchor bahwa `[Save]` sudah ditolak (8b.2). Entri Changelog langkah 23 dan 24 memakai selisih terhadap N (S-12) dan dibaca pada baris teratas urutan default `Date` terbaru (S-14).
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - Kolom Data Uji TC-FA-TDC-228 dan TC-FA-TDC-229 memuat nilai field lain (Regulation Reference, Class Name `Kelompok uji validasi`, Asset Type, Useful Life, Allowed Methods, Class Code `KHS-N1`) seperti form Create; langkah TC hanya mengubah satu field pada class `KHS-E1` yang sudah terisi, sehingga nilai itu tidak dipakai (S-15).
  - TC-FA-TDC-228 Expected c menyebut entri log L-02 tanpa menyebut surface log (Changelog, System Log, atau Activity Log) dan kolom yang dibaca; spec membaca popup Changelog dengan kolom Old Value dan New Value mengikuti TC-FA-TDC-193 (S-15).
  - TC-FA-TDC-225 sampai TC-FA-TDC-227 dan TC-FA-TDC-229 Post Condition ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-TDC-225 sampai TC-FA-TDC-227 tidak menyebut klik `[Save]` setelah caption duplikat; spec mengikuti TC (tanpa Save).
