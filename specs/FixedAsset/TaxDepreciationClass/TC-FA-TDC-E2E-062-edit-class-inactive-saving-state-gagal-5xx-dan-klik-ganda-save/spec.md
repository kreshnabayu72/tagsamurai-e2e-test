---
id: TC-FA-TDC-E2E-062-edit-class-inactive-saving-state-gagal-5xx-dan-klik-ganda-save
title: "Edit: Saving State, Klik Ganda Save, Gagal 5xx, dan Class Inactive Dapat Diedit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-197
  - TC-FA-TDC-198
  - TC-FA-TDC-199
  - TC-FA-TDC-219
coverage:
  web: automated
---

# Edit: Saving State, Klik Ganda Save, Gagal 5xx, dan Class Inactive Dapat Diedit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk (a) menunda respons endpoint update class 3 detik (TC-FA-TDC-197) dan (b) mengembalikan 500 untuk endpoint update class (TC-FA-TDC-198); pencatat jumlah request jaringan ke endpoint update (TC-FA-TDC-199). Endpoint tidak dikarang: nama endpoint update disediakan tim FE/BE (S-13). Intercept dilepas segera setelah pemicu selesai (langkah 9 dan 28) dan di hook `after` sebagai cadangan.
- Jeda nyata 5 detik pada langkah 23 dipilih spec (di bawah batas ±30 detik) untuk membuktikan toast error tidak hilang otomatis.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `khsOld` | `KHS-OLD` | Class Inactive, Class Name `Kelompok khusus lama`, Used By 0 (pengganti `NB-OLD` Pre-setup untuk target tulis, S-06) |

- Blok berjalan berurutan pada class `KHS-E1` yang sama; Class Name berubah antar blok.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-197: Tombol Save masuk Saving state

1. Tunda respons endpoint update class selama 3 detik (intercept)
2. Ketik Search `KHS-E1`, tekan Enter
3. Klik link Class Code `KHS-E1`
4. Ganti Class Name menjadi `Kelompok edit uji T`
5. Klik `[Save]`
6. Verifikasi tombol `[Save]` menampilkan spinner dan tidak dapat diklik
7. Verifikasi tombol `[Clear Field]`, ikon ✕, dan semua field tidak interaktif selama request
8. Verifikasi setelah respons diterima muncul toast sukses: `Success, tax depreciation class has been updated.`
9. Lepas intercept penundaan respons endpoint update

### TC-FA-TDC-199: Klik ganda cepat pada Save

10. Tunggu toast sukses sebelumnya hilang otomatis
11. Klik link Class Code `KHS-E1`
12. Ganti Class Name menjadi `Kelompok edit uji D`
13. Klik `[Save]` dua kali dengan cepat
14. Verifikasi tombol `[Save]` disabled setelah klik pertama
15. Verifikasi hanya satu request update class yang diproses
16. Verifikasi muncul tepat satu toast sukses: `Success, tax depreciation class has been updated.`

### TC-FA-TDC-198: Edit gagal 5xx

17. Tunggu toast sukses sebelumnya hilang otomatis
18. Paksa endpoint update class mengembalikan 500 (intercept)
19. Klik link Class Code `KHS-E1`
20. Ganti Class Name menjadi `Kelompok edit uji G`
21. Klik `[Save]`
22. Verifikasi muncul toast error: `Error, failed to update tax depreciation class.`
23. Tunggu 5 detik tanpa memuat ulang halaman
24. Verifikasi toast error masih tampil tanpa di-dismiss
25. Verifikasi Drawer tetap terbuka dengan Class Name `Kelompok edit uji G` dipertahankan
26. Verifikasi tombol `[Save]` kembali enabled
27. Dismiss toast error
28. Lepas intercept respons 500 endpoint update class
29. Klik ikon ✕
30. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Cancel]` dan `[Leave]`
31. Klik `[Leave]`

### TC-FA-TDC-219: Class Inactive dapat diedit dan disimpan

32. Ganti isi kotak search dengan `KHS-OLD`, tekan Enter
33. Klik link Class Code `KHS-OLD`
34. Ganti Class Name menjadi `Kelompok khusus lama diubah`
35. Klik `[Save]`
36. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
37. Verifikasi baris `KHS-OLD` tetap berstatus Active = Off
38. Verifikasi baris `KHS-OLD` menampilkan Class Name `Kelompok khusus lama diubah`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- P-5 (butir b): TC-FA-TDC-198 adalah satu-satunya TC objek-uji ringan kelas b (respons 500 yang dipaksa) di spec fungsional ini; ia tanpa harness eksternal dan tanpa state berat sendiri, dan permukaannya sama (Drawer Edit dan Save).
- Langkah penghubung (S-03): langkah 2 dan 32 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13), Search `KHS-E1` dipertahankan untuk langkah 11 dan 19; langkah 9, 28 melepas intercept segera setelah pemicu selesai (S-09); langkah 10 dan 17 menunggu toast lama hilang otomatis sebelum menghitung toast berikutnya (R-12); langkah 27 men-dismiss toast error; langkah 29 sampai 31 menutup form dirty secara deterministik (S-08).
- Urutan TC: TC-FA-TDC-197, TC-FA-TDC-199, TC-FA-TDC-198, TC-FA-TDC-219 (S-10): blok dengan hasil sukses lebih dulu, gagal 5xx menutup dengan form dirty yang dibuang, class Inactive terakhir.
- Langkah 7: daftar elemen yang tidak interaktif disebut utuh dalam satu butir Expected TC, sehingga satu `Verifikasi` (S-01).
- Alasan spec melewati sekitar 35 langkah: empat blok Edit pada Drawer yang sama (saving state, klik ganda, kegagalan 5xx, class Inactive) berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah dibentuk `Verifikasi` per klausa (S-01) dan langkah pembuka berulang per blok.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-*` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-219 memakai `NB-OLD` (Pre-setup Example Data) sebagai target Edit; spec memakai class Inactive milik spec `KHS-OLD` (S-06) dengan Class Name awal `Kelompok khusus lama`.
  - TC-FA-TDC-198 Post Condition (Class Name tersimpan tetap, tidak ada entri log) dan TC-FA-TDC-199 Post Condition (tepat satu entri L-02) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01).
  - TC-FA-TDC-199 Expected a ("hanya satu request diproses") membutuhkan pencatat jumlah request; TC tidak menyebut cara mengamatinya (S-11).
  - TC-FA-TDC-198 Expected a mengharuskan toast error "tetap tampil sampai di-dismiss"; TC tidak menyebut durasi pengamatan, spec memakai jeda 5 detik.
