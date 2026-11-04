---
id: TC-FA-TDC-E2E-067-edit-validasi-class-name-panjang-emoji-trim-dan-duplikat-diizinkan
title: "Edit: Validasi Class Name Batas Panjang 120 Karakter, Emoji, Trim, dan Nama Duplikat Diizinkan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-230
  - TC-FA-TDC-231
  - TC-FA-TDC-232
  - TC-FA-TDC-233
  - TC-FA-TDC-234
  - TC-FA-TDC-235
coverage:
  web: automated
---

# Edit: Validasi Class Name Batas Panjang 120 Karakter, Emoji, Trim, dan Nama Duplikat Diizinkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Kemampuan teknis: (a) menyuntikkan nilai langsung ke DOM field Class Name tanpa melewati filter keystroke FE (langkah 16), disediakan tim FE; (b) kemampuan baca jumlah entri Changelog tax depreciation class sebelum aksi (audit trail permanen, N tidak dapat diturunkan dari seeding), disediakan tim FE/BE tanpa endpoint karangan (S-11, 8b.10); N dicatat pada langkah 22; (c) pembacaan nilai class lewat fixture BE untuk `Verifikasi` "tidak ada data tersimpan" pada langkah 20, disediakan tim FE/BE tanpa endpoint karangan.
- Data (seed idempotent di hook `before` lewat API; class `KHS-*` dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `nb1` | `NB-1` | Pre-setup Example Data: Class Name `Bukan bangunan – Kelompok 1`, Used By 5; hanya dibaca, tidak diubah |

- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`

### TC-FA-TDC-230: Class Name 121 karakter ditolak saat mengetik

3. Ganti isi Class Name dengan 121 karakter `A`
4. Verifikasi segera setelah input caption `Max. 120 characters` muncul pada Class Name

### TC-FA-TDC-231: Class Name tepat 120 karakter diterima

5. Ganti isi Class Name dengan 120 karakter `A`
6. Verifikasi field Class Name berisi 120 karakter `A`
7. Verifikasi tidak ada caption error pada Class Name

### TC-FA-TDC-232: Emoji pada Class Name diblok saat diketik atau ditempel

8. Ganti isi Class Name dengan `Kelompok edit uji`
9. Ketik `😀` pada Class Name
10. Verifikasi karakter emoji tidak masuk ke nilai field Class Name
11. Verifikasi tidak ada caption error pada Class Name
12. Ganti isi Class Name dengan `Kelompok edit uji`
13. Tempel `😀` pada Class Name
14. Verifikasi karakter emoji hasil tempel tidak masuk ke nilai field Class Name
15. Verifikasi tidak ada caption error pada Class Name setelah tempel

### TC-FA-TDC-233: Emoji yang lolos filter input ditolak dengan pesan fallback

16. Suntikkan nilai `Uji 😀` langsung ke DOM field Class Name (bypass filter keystroke FE, simulasi drag-drop)
17. Klik `[Save]`
18. Verifikasi caption `Class name contains invalid characters` muncul pada Class Name
19. Verifikasi Drawer tetap terbuka
20. Verifikasi tidak ada data tersimpan: Class Name class `KHS-E1` tetap `Kelompok edit uji` (dibaca lewat fixture BE)

### TC-FA-TDC-234: Class Name dengan spasi tepi disimpan ter-trim

21. Ganti isi Class Name dengan `  Kelompok trim  ` (dua spasi di awal dan akhir)
22. Catat jumlah entri Changelog tax depreciation class sebagai N
23. Klik `[Save]`
24. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
25. Verifikasi baris `KHS-E1` menampilkan Class Name `Kelompok trim` tanpa spasi tepi
26. Buka popup Changelog lewat ikon Changelog pada Table Tools
27. Verifikasi jumlah entri Changelog menjadi N + 1
28. Verifikasi entri Changelog teratas: L-02 dengan Old Value `Kelompok edit uji` dan New Value `Kelompok trim`
29. Tutup popup Changelog

### TC-FA-TDC-235: Class Name sama dengan class lain diizinkan

30. Klik link Class Code `KHS-E1`
31. Ganti isi Class Name dengan `Bukan bangunan – Kelompok 1`
32. Klik `[Save]`
33. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
34. Verifikasi tidak ada caption error pada Class Name
35. Ganti isi kotak search dengan `Bukan bangunan – Kelompok 1`, tekan Enter
36. Verifikasi tabel memuat dua baris dengan Class Name `Bukan bangunan – Kelompok 1`: `NB-1` dan `KHS-E1`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 36 langkah, di atas ~35 langkah: satu topik (validasi Class Name pada satu class `KHS-E1`), enam TC berurutan pada Drawer Edit yang sama sampai Save pertama pada langkah 23, sehingga memecahnya berarti membuka ulang Drawer dan mencari ulang baris. TC-FA-TDC-232 memuat dua aksi, ketik (langkah 9) dan tempel (langkah 12 sampai 15), masing-masing dengan `Verifikasi` per klausa.
- Langkah penghubung (S-03): langkah 1 dan 35 Search agar baris target ada di halaman teramati (R-16, 8b.13); langkah 8, 12, dan 21 mengganti Class Name ke nilai berikutnya sehingga isi dirty blok sebelumnya (121 karakter, 120 karakter, hasil ketik emoji, nilai hasil suntik DOM) tidak terbawa; langkah 29 menutup popup Changelog.
- Urutan TC: validasi diblokir lebih dulu (TC-FA-TDC-230, TC-FA-TDC-231, TC-FA-TDC-232, TC-FA-TDC-233), aksi sukses terakhir (TC-FA-TDC-234, TC-FA-TDC-235) (S-10). Drawer `KHS-E1` yang sama dipakai berturut-turut sampai Save pertama pada langkah 23; Drawer ditutup oleh Save sukses dan dibuka ulang pada langkah 30.
- Langkah 7, 11, dan 15 (tidak ada caption): langkah 6 (nilai field) serta langkah 8 sampai 10 dan 12 sampai 14 menjadi anchor pada surface yang sama (8b.2). Langkah 20 (tidak ada data tersimpan): dibaca lewat fixture BE; caption langkah 18 dan Drawer tetap terbuka (langkah 19) menjadi anchor bahwa `[Save]` ditolak. Langkah 34: toast sukses langkah 33 menjadi anchor.
- Entri Changelog langkah 27 dan 28 memakai selisih terhadap N (S-12) dan dibaca pada baris teratas urutan default `Date` terbaru (S-14).
- Langkah 36 mengasersi dua baris: baris `NB-1` (Pre-setup) dan `KHS-E1`; hasil Search `Bukan bangunan – Kelompok 1` dibaca di halaman pertama.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - Kolom Data Uji TC-FA-TDC-233 sampai TC-FA-TDC-235 memuat nilai field lain (Class Code `KHS-N2`, `KHS-N3`, `KHS-N4`, Regulation Reference, Asset Type, Useful Life, Allowed Methods) seperti form Create; langkah TC hanya mengubah Class Name pada class `KHS-E1` yang sudah terisi, sehingga nilai itu tidak dipakai (S-15).
  - TC-FA-TDC-234 Expected c menyebut entri log L-02 tanpa menyebut surface log; spec membaca popup Changelog (S-15).
  - TC-FA-TDC-235 Expected c ("dua baris dengan Class Name sama") mengasumsikan tidak ada class Pre-setup lain dengan Class Name itu; spec mengikuti TC.
  - Post Condition "Tidak ada data berubah dan tidak ada entri log" TC-FA-TDC-230 sampai TC-FA-TDC-233 tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-TDC-232 menyebut "ketik atau tempel" tanpa memerinci perbedaannya; spec menjalankan keduanya sebagai dua aksi terpisah (ketik pada langkah 9, tempel pada langkah 13) dengan `Verifikasi` masing-masing dan mengasersi hasil yang sama.
