---
id: TC-FA-TDC-E2E-064-edit-clear-field-field-dikembalikan-dan-reload-bawaan-browser
title: "Edit: Clear Field, Field Dikembalikan Dianggap Bersih, dan Reload Bawaan Browser"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-200
  - TC-FA-TDC-208
  - TC-FA-TDC-209
coverage:
  web: automated
---

# Edit: Clear Field, Field Dikembalikan Dianggap Bersih, dan Reload Bawaan Browser

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Kemampuan teknis: spec menangani dialog bawaan browser `beforeunload` (menerima konfirmasi reload pada langkah 27) dan menyatakan ada atau tidaknya dialog itu pada langkah 26 dan 31; kemampuan ini disediakan tim FE (S-08).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Tidak ada Save di spec ini: nilai tersimpan class tidak pernah berubah di server.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-200: Clear Field mengosongkan field tanpa merevert dan tanpa menutup Drawer

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`
3. Klik `[Clear Field]`
4. Verifikasi Regulation Reference dikosongkan
5. Verifikasi Class Code dikosongkan
6. Verifikasi Class Name dikosongkan
7. Verifikasi Useful Life dikosongkan
8. Verifikasi Allowed Methods dikosongkan
9. Verifikasi Asset Type tetap Disabled dengan nilai `Non-building`
10. Verifikasi Drawer tetap terbuka
11. Verifikasi fokus pada field pertama yang dapat diisi
12. Verifikasi tidak ada dialog konfirmasi
13. Verifikasi caption error tidak tampil
14. Klik ikon ✕
15. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Cancel]` dan `[Leave]`
16. Klik `[Leave]`

### TC-FA-TDC-208: Field diubah lalu dikembalikan dianggap bersih

17. Klik link Class Code `KHS-E1`
18. Ganti Class Name menjadi `Kelompok edit uji U`
19. Ganti kembali Class Name menjadi `Kelompok edit uji`
20. Klik ikon ✕
21. Verifikasi Drawer langsung tertutup
22. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-FA-TDC-209: Reload halaman saat Drawer berubah

23. Klik link Class Code `KHS-E1`
24. Ganti Class Name menjadi `Kelompok edit uji U`
25. Tekan F5
26. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
27. Terima konfirmasi bawaan browser sehingga halaman dimuat ulang
28. Ganti isi kotak search dengan `KHS-E1`, tekan Enter
29. Klik link Class Code `KHS-E1`
30. Tekan F5 tanpa mengubah field apa pun
31. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
32. Verifikasi tabel tampil kembali
33. Verifikasi Drawer sebelumnya tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (Ketik Search) dan 28 (ganti isi kotak search; Search dipertahankan sesudah F5, 8b.9) memuat `KHS-E1` agar baris target ada di halaman teramati (R-16, 8b.13); langkah 14 sampai 16 menutup form dirty secara deterministik (S-08); langkah 27 menerima konfirmasi `beforeunload` agar reload dijalankan (Drawer yang berubah dibuang oleh reload; tidak ada perubahan tersimpan, S-09).
- Langkah 22 (dialog tidak muncul) didahului langkah 21 (Drawer tertutup) sebagai anchor positif (8b.2, 8b.11). Langkah 31 mengasersi reload tanpa konfirmasi; langkah 32 (tabel tampil kembali) menjadi anchor positif bagi langkah 33 (Drawer sebelumnya sudah tidak tampil), keduanya bukti halaman dimuat ulang (8b.2). Search, Filter, Sort, dan halaman dipertahankan sesudah F5, jadi kotak Search tidak dipakai sebagai bukti reload.
- Urutan TC: TC-FA-TDC-200, TC-FA-TDC-208, TC-FA-TDC-209 (S-10); reload paling akhir karena membuang Drawer yang sedang terbuka.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-200 Post Condition ("Tidak ada data tersimpan berubah") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-TDC-209 langkah 4 ("Ulangi dengan Drawer Edit tanpa perubahan") tidak menyebut cara membuka Drawer lagi setelah reload; spec memakai Search dan klik Class Code (langkah 28 dan 29).
  - TC-FA-TDC-209 Expected tidak menyebut apakah konfirmasi diterima atau dibatalkan; spec menerimanya agar reload berjalan (langkah 27).
