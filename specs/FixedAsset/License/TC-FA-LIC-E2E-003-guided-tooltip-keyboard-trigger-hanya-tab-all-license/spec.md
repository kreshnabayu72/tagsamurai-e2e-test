---
id: TC-FA-LIC-E2E-003-guided-tooltip-keyboard-trigger-hanya-tab-all-license
title: "Guided Tooltip: Navigasi Keyboard, Trigger Hanya di Tab All License, dan Putar Ulang dengan [?]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-7
  - TC-FA-LIC-9
  - TC-FA-LIC-592
coverage:
  web: automated
---

# Guided Tooltip: Navigasi Keyboard, Trigger Hanya di Tab All License, dan Putar Ulang dengan [?]

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control tur Pre-setup #19 `totalControlTour_automated_{namaCompany}@qwertysystem.net` (client Paid; kredensial `Spectra.env.FA_TOUR_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit di langkah 25): Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (flag `guided_tooltip_seen_fa-license` = true; kredensial `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (#1).
- Pengecualian flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-license` sendiri. Sesudah hook suite `before`, flag akun #19 dihapus (belum seen) lewat fixture BE di awal tiap blok TC akun #19; hook `after` suite memulihkan flag ke true. Kemampuan menghapus dan membaca flag lewat fixture BE disediakan tim FE/BE.
- Data Pre-setup: kuota dan hierarki #12, sesi aktif #14 (client PT Sejahtera); hanya dibaca. Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Kemampuan teknis: menekan tombol keyboard (Enter, panah kiri, Esc) dan membuka route tab License langsung lewat URL.
- Hook dan kemampuan suite (sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-9: Navigasi keyboard Esc, Enter, panah

1. Hapus flag `guided_tooltip_seen_fa-license` akun lewat fixture BE
2. Muat ulang halaman License (F5)
3. Tekan Enter
4. Verifikasi Enter memajukan walkthrough ke Step 2
5. Tekan panah kiri
6. Verifikasi panah kiri kembali ke Step 1
7. Tekan Esc
8. Verifikasi Esc menutup walkthrough
9. Verifikasi flag seen disetel true (dibaca lewat fixture BE)

### TC-FA-LIC-592: Trigger `[?]` dan tur first-visit hanya ada di Tab All License

10. Hapus flag `guided_tooltip_seen_fa-license` akun lewat fixture BE
11. Buka route Tab `Concurrent User` langsung lewat URL sebagai kunjungan pertama
12. Verifikasi Breadcrumb `License > Concurrent User`
13. Verifikasi tombol `[?]` tidak tampil di sebelah Breadcrumb
14. Verifikasi walkthrough tidak berjalan otomatis
15. Klik Tab `Allocation Quota`
16. Verifikasi Breadcrumb `License > Allocation Quota`
17. Verifikasi tombol `[?]` tidak tampil di sebelah Breadcrumb
18. Verifikasi walkthrough tidak berjalan otomatis
19. Klik Tab `All License`
20. Verifikasi Breadcrumb `License > All License`
21. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
22. Verifikasi walkthrough Step 1 muncul otomatis
23. Verifikasi flag seen belum disetel oleh kunjungan ke tab lain (dibaca lewat fixture BE)
24. Klik `[Skip]` pada Step 1

### TC-FA-LIC-7: Tombol `[?]` memutar ulang dari Step 1 tanpa mereset flag seen

25. Ganti akun: Logout, lalu login sebagai Total Control Pre-setup #1 (`Spectra.env.FA_TC_PASSWORD`)
26. Klik tombol `[?]` di sebelah Breadcrumb
27. Verifikasi walkthrough mulai dari Step 1
28. Klik `[Skip]`
29. Muat ulang halaman License (F5)
30. Verifikasi Breadcrumb `License > All License` tampil
31. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang
32. Verifikasi flag seen tetap true (dibaca lewat fixture BE)

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-7, 9, 592). TC-FA-LIC-10 dan 11 (tooltip toolbar) ada di spec 130. Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor agar semua blok akun #19 berurutan sebelum satu kali ganti akun ke #1 (S-07, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1, 2, 10 (menghapus flag dan memuat ulang halaman agar walkthrough muncul), langkah 24 (menutup walkthrough dengan `[Skip]` sebelum ganti akun), langkah 25 (ganti akun eksplisit). Langkah 2 ("Muat ulang halaman License") menggantikan "Buka License" TC-9 karena halaman sudah dibuka hook `beforeEach`.
- Langkah 30 menjadi anchor positif untuk asersi absence pada langkah 31; langkah 12, 16, 20 menjadi anchor untuk asersi absence pada langkah 13, 14, 17, 18.
- Temuan untuk QA:
  - TC-9 dan TC-592 tidak menyebut cara membaca flag seen; langkah 9, 23, dan 32 membaca flag lewat fixture BE (kemampuan disediakan tim FE/BE). Butir parentetis TC-592 c ("flag seen belum disetel oleh kunjungan ke tab lain") diasersi di langkah 23.
  - TC-7 Precondition menyebut flag seen = true untuk Pre-setup #1; flag itu diasumsikan sudah true sejak Pre-setup (hook suite hanya memulihkan akun aktor spec), dan tidak ada langkah penyetelan di TC.
