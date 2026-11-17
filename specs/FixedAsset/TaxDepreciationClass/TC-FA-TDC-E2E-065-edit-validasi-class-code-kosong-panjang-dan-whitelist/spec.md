---
id: TC-FA-TDC-E2E-065-edit-validasi-class-code-kosong-panjang-dan-whitelist
title: "Edit: Validasi Class Code Kosong, Batas Panjang 15 Karakter, dan Whitelist Karakter"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-220
  - TC-FA-TDC-221
  - TC-FA-TDC-222
  - TC-FA-TDC-223
  - TC-FA-TDC-224
sourceRules: ["V-01", "E-FATDC-04", "V-02", "V-03", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "V-01": [5, 9]
  "E-FATDC-04": 11
  "V-02": [13, 15, 17, 18]
  "V-03": [20, 23, 24]
  "§4.2c#b1": 26
anchor: [10, 28]
coverage:
  web: automated
---

# Edit: Validasi Class Code Kosong, Batas Panjang 15 Karakter, dan Whitelist Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Nilai Class Code yang diuji untuk TC-FA-TDC-223 (dipakai langkah 19 sampai 21, satu iterasi per baris):

| No | Nilai Class Code |
|---|---|
| 1 | `NB 1` (dengan spasi) |
| 2 | `NB#1` |
| 3 | `NB/1` |
| 4 | `NB@1` |
| 5 | `NBé1` |

- Tidak ada Save yang berhasil di spec ini: semua Save diblokir validasi dan semua form ditutup tanpa menyimpan.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`

### TC-FA-TDC-220: Class Code kosong atau hanya spasi ditolak

3. Hapus seluruh isi Class Code
4. Klik `[Save]`
5. Verifikasi caption `Class code must not be empty` muncul pada Class Code setelah klik tombol
6. Ganti isi Class Code dengan `KHS-E1`
7. Isi Class Code dengan tiga spasi (`   `)
8. Klik `[Save]`
9. Verifikasi caption `Class code must not be empty` muncul pada Class Code setelah klik tombol
10. Verifikasi Drawer tetap terbuka
11. Verifikasi tidak ada toast sukses

### TC-FA-TDC-221: Class Code 16 karakter ditolak saat mengetik

12. Ganti isi Class Code dengan `ABCDEFGHIJKLMNOP`
13. Verifikasi segera setelah mengetik caption `Max. 15 characters` muncul pada Class Code
14. Klik `[Save]`
15. Verifikasi tidak ada toast sukses

### TC-FA-TDC-222: Class Code tepat 15 karakter diterima

16. Ganti isi Class Code dengan `ABCDEFGHIJKLMNO`
17. Verifikasi nilai tampil utuh 15 karakter di field: `ABCDEFGHIJKLMNO`
18. Verifikasi tidak ada caption error pada Class Code

### TC-FA-TDC-223: Class Code di luar whitelist ditolak

Untuk setiap baris tabel nilai Class Code TC-FA-TDC-223 pada `## Prerequisites` (langkah 19 sampai 21):

19. Ganti isi Class Code dengan nilai baris
20. Verifikasi caption `Class code contains invalid characters` muncul segera pada Class Code
21. Ganti isi Class Code dengan `KHS-E1`

### TC-FA-TDC-224: Class Code huruf, angka, tanda hubung, underscore, dan titik diterima

22. Ganti isi Class Code dengan `Ab-1_2.x`
23. Verifikasi nilai `Ab-1_2.x` tampil utuh
24. Verifikasi tidak ada caption error pada Class Code setelah jeda debounce

### Penutup

25. Klik ikon ✕
26. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Cancel]` dan `[Leave]`
27. Klik `[Leave]`
28. Verifikasi baris `KHS-E1` tetap menampilkan Class Code `KHS-E1` (tidak ada data tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 Search `KHS-E1` agar baris target ada di halaman teramati (R-16, 8b.13); langkah 6 dan 21 mengembalikan Class Code ke `KHS-E1` agar caption error sebelumnya hilang sebelum nilai berikutnya diasersi (R-12); langkah 25 sampai 27 menutup form dirty secara deterministik (S-08, S-09). Langkah 28 mengamati Expected c TC-FA-TDC-220 "tidak ada data tersimpan".
- Langkah berulang: langkah 19 sampai 21 diulang untuk lima baris tabel nilai (8b.7); `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi, jumlah langkah efektif sekitar 40.
- Alasan spec melewati sekitar 35 langkah: seluruh blok adalah validasi satu field (Class Code) pada Drawer Edit yang sama, tanpa Save yang berhasil, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Tambahan langkah berasal dari ekspansi iterasi whitelist.
- Urutan TC: validasi diblokir (TC-FA-TDC-220, TC-FA-TDC-221) lebih dulu, lalu nilai batas dan whitelist (S-10). Pada TC-FA-TDC-222 dan TC-FA-TDC-224, `Verifikasi` nilai tampil utuh mendahului `Verifikasi` tidak ada caption (anchor, 8b.2); urutan Expected TC dibalik.
- Langkah 11 dan 15 (tidak ada toast sukses): caption error pada langkah 9 dan 13 menjadi anchor positif pada surface yang sama (8b.2).
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - Kolom Data Uji TC-FA-TDC-220 memuat nilai field lain (Regulation Reference, Class Name `Kelompok uji validasi`, Asset Type, Useful Life, Allowed Methods) seperti form Create; langkah TC hanya mengubah Class Code pada class `KHS-E1` yang sudah terisi, sehingga nilai itu tidak dipakai (S-15).
  - TC-FA-TDC-221 Expected b ("Tidak ada Submit/Save yang berhasil bila diklik") tidak ada di Langkah TC; spec menambah klik `[Save]` pada langkah 14.
  - Post Condition "Tidak ada data berubah dan tidak ada entri log" pada TC-FA-TDC-221 sampai TC-FA-TDC-224 tidak punya langkah observasi di TC dan tidak diasersi, kecuali langkah 28 (S-01).
