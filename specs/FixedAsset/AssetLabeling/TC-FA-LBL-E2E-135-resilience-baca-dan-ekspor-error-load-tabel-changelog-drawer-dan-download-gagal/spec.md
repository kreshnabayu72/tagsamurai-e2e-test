---
id: TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal
title: "Resilience Baca dan Ekspor: Error Load Tabel, Changelog, Drawer, dan Download Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-12
  - TC-FA-LBL-270
  - TC-FA-LBL-288
  - TC-FA-LBL-322
  - TC-FA-LBL-337
coverage:
  web: automated
---

# Resilience Baca dan Ekspor: Error Load Tabel, Changelog, Drawer, dan Download Gagal

## Prerequisites

- Mode: FE+BE. Backend nyata dengan intercept parsial atas respons 5xx pada List Labels, ekspor Labels List, data Tagged Asset, data Changelog, dan ekspor Changelog; asersi atas state backend (baris label tetap dimuat setelah Try Again).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca, tidak diubah): katalog Company Alpha (Pre-setup #12; `Finance Department` dengan lima aset terkait dari Pre-setup #13) untuk TC-FA-LBL-12, 270, 337; Company Changelog (Pre-setup #17; tujuh baris seed Date 08 sampai 15 Sep 2026, N = jumlah entri log dalam rentang Filter Date `08 Sep 2026` sampai `15 Sep 2026`, entri TC lain bertanggal hari run berada di luar rentang) untuk TC-FA-LBL-288 dan 322.
- Akun ganti: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControlChangelog` (email mengikuti pola Pre-setup #1 untuk Company Changelog; ditetapkan tim FE), password `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; dipakai lewat langkah Ganti akun (langkah 20). Hook `after` mengembalikan sesi ke akun default suite.
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.akun.totalControlChangelog` | identitas akun Total Control Company Changelog |

- Kemampuan teknis: pembacaan jumlah entri log Company Changelog dalam rentang Filter Date `08 Sep 2026` sampai `15 Sep 2026` (N) lewat fixture BE yang disediakan tim FE/BE (endpoint tidak tertulis di TC); dipakai sebelum intercept TC-FA-LBL-288 (bagian 8b butir 10). `Spectra.intercept()` untuk memaksa respons 5xx atau timeout (endpoint ditentukan tim FE dan tidak ditulis di TC); intercept dilepas segera sesudah pemicu selesai (S-09) dan hook `after` melepasnya bila spec gagal di tengah. Tidak ada data yang dibuat spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: tidak ada data yang dibuat spec; hook `after` melepas intercept yang tersisa dan mengembalikan sesi ke akun default suite.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` dan `Spectra.env.FA_TC_CHANGELOG_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-12: Error load Labels List menampilkan ErrorState dan Try Again memulihkan

1. Paksa respons List Labels gagal 5xx (`Spectra.intercept()`)
2. Muat ulang halaman tab Labels
3. Verifikasi ErrorState menampilkan teks `Unable to load this data.` dan tombol `[Try Again]`
4. Verifikasi empty state `No labels yet` tidak tampil
5. Lepas intercept
6. Klik `[Try Again]`
7. Verifikasi tabel memuat sedikitnya satu baris label

### TC-FA-LBL-270: Download gagal memunculkan toast error

8. Paksa fetch data ekspor Labels List gagal (`Spectra.intercept()`)
9. Klik icon Download
10. Klik `Download as CSV`
11. Verifikasi toast error `Error, failed to download Labels.`
12. Lepas intercept

### TC-FA-LBL-337: Error load Drawer dan Try Again

13. Paksa data Tagged Asset gagal 5xx (`Spectra.intercept()`)
14. Klik chip `Finance Department` di kolom Label
15. Verifikasi ErrorState inline `Unable to load this data.` dan `[Try Again]` tampil di Drawer Tagged Asset
16. Lepas intercept
17. Klik `[Try Again]`
18. Verifikasi lima baris tampil di Drawer Tagged Asset
19. Tutup Drawer Tagged Asset

### TC-FA-LBL-288: Error load Modal Changelog dan Try Again

20. Ganti akun: Logout, login sebagai Total Control Company Changelog `Fixture.assetLabeling.akun.totalControlChangelog` (`Spectra.env.FA_TC_CHANGELOG_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
21. Baca jumlah entri N Company Changelog dengan Date `08 Sep 2026` sampai `15 Sep 2026` lewat pembacaan BE
22. Paksa data Changelog gagal 5xx (`Spectra.intercept()`)
23. Klik icon Changelog di Table Tools
24. Verifikasi ErrorState inline di dalam modal: `Unable to load this data.` dan `[Try Again]`
25. Verifikasi header dan `[✕]` modal tetap tampil
26. Lepas intercept
27. Klik `[Try Again]`
28. Klik icon Filter di toolbar modal
29. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`
30. Verifikasi tabel Changelog memuat N baris hasil Filter Date, tepat tujuh baris seed Pre-setup #17
31. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-322: Download Changelog gagal memunculkan toast error

32. Paksa fetch data ekspor Changelog gagal (`Spectra.intercept()`)
33. Klik icon Changelog di Table Tools
34. Klik icon Download di toolbar Modal Changelog
35. Klik `Download as CSV`
36. Verifikasi toast error `Error, failed to download Changelog-Labels.`
37. Lepas intercept

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 1 (TC-FA-LBL-12), 4a (TC-FA-LBL-270), 4b (TC-FA-LBL-288, 322), dan 4c (TC-FA-LBL-337). Subjudul `###` memetakan langkah ke TC granular.
- Langkah 20 adalah Ganti akun eksplisit (S-07) karena TC-FA-LBL-288 dan 322 memakai Company Changelog (Pre-setup #17) yang berbeda dari Company Alpha.
- Urutan TC: TC-FA-LBL-288 dan 322 di akhir spec karena memakai akun Company Changelog, sedangkan TC-FA-LBL-12, 270, dan 337 memakai Company Alpha.
- Langkah penghubung (S-03): pembacaan jumlah entri N dalam rentang Filter Date (langkah 21), pelepasan intercept (S-09), penutupan Drawer, dan penutupan Modal Changelog.
- S-12: Expected TC-FA-LBL-288 menyatakan hasil relatif atas hasil Filter Date (N baris, tepat tujuh baris seed); N = jumlah entri dalam rentang Filter Date `08 Sep 2026` sampai `15 Sep 2026`, dibaca lewat pembacaan BE sebelum intercept (langkah 21), dan Filter Date diterapkan sesudah Try Again (langkah 28 dan 29) supaya ketujuh baris seed tidak bergeser ke luar halaman pertama karena entri TC lain bertanggal hari run.
- Ukuran spec (37 langkah, di atas smell 35 langkah): lima TC resilience satu kelas (intercept respons 5xx atau timeout atas baca dan ekspor) dengan satu Ganti akun dan tanpa data buatan spec; dua langkah bertambah karena TC-FA-LBL-288 kini memuat Filter Date rentang seed sebelum hasilnya diamati (langkah 28 dan 29).
- Temuan untuk QA:
  - TC-FA-LBL-12, 270, 288, 322, dan 337: Post Condition tidak ada. TC-FA-LBL-12 Expected a "bukan empty state `No labels yet`" ditulis sebagai Verifikasi absence berjangkar ErrorState yang tampil sesaat sebelumnya.
  - TC-FA-LBL-337 tidak menyebut kondisi tersaring; spec menyalin Pre-setup #12 dan #13 tanpa Search sehingga `Finance Department` ada di halaman pertama katalog Company Alpha.
  - TC-FA-LBL-270 dan 322 tidak menyebut format berkas selain CSV; spec memilih `Download as CSV`.
  - TC-FA-LBL-288 menyebut Company Changelog dengan `Total Control`; email akun tidak tertulis di Pre-setup TC (lihat Pre-setup #17) dan disediakan tim FE.
