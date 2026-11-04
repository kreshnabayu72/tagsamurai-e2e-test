---
id: TC-FA-TDC-E2E-182-guided-tooltip-replay-skip-dan-tombol-back
title: "Guided Tooltip: Replay, Skip, dan Tombol Back"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-652
  - TC-FA-TDC-653
  - TC-FA-TDC-654
  - TC-FA-TDC-655
coverage:
  web: automated
---

# Guided Tooltip: Replay, Skip, dan Tombol Back

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite dan seeding mengikuti `suite.md`. Pengecualian flag Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tax-depreciation-class` true untuk akun Total Control (keadaan awal blok TC-FA-TDC-652 dan TC-FA-TDC-655); spec ini menghapus flag sesudah hook pada langkah 18 dan 26 untuk blok TC-FA-TDC-653 dan TC-FA-TDC-654, dan hook `after` memulihkan flag ke true.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.seedClasses` berisi tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) belum diubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menghapus flag Guided Tooltip akun (disediakan tim FE/BE; nama kunci flag dari TC); mengarahkan kursor (hover) untuk tooltip; navigasi baru ke layar Settings > Accounting > Tax Depreciation Class.
- State global yang diubah: flag Guided Tooltip akun Total Control. Blok TC-FA-TDC-653 dan TC-FA-TDC-654 menyimpan flag seen lewat `[Skip]` dan klik overlay (langkah 21 dan 29), sehingga keadaan akhir flag true seperti keadaan awal suite.

## Test Steps

### TC-FA-TDC-652: Replay lewat tombol [?] tanpa mereset flag seen

1. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
2. Verifikasi tooltip tombol `Show guide`
3. Klik tombol `[?]`
4. Verifikasi walkthrough mulai dari Step 1 of 6
5. Klik `[Skip]`
6. Verifikasi walkthrough tertutup
7. Muat ulang halaman (F5)
8. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
9. Verifikasi walkthrough tidak muncul otomatis setelah F5 (flag seen tetap true)

### TC-FA-TDC-655: Tombol Back

10. Klik tombol `[?]`
11. Verifikasi tombol `[Skip]` dan `[Next]` tampil pada Step 1
12. Verifikasi tombol `[Back]` tidak dirender pada Step 1
13. Klik `[Next]`
14. Verifikasi Step 2 of 6 tampil
15. Klik `[Back]`
16. Verifikasi kembali ke Step 1 of 6
17. Klik `[Skip]`

### TC-FA-TDC-653: Skip lewat tombol menutup walkthrough dan menyimpan flag seen

18. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
19. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
20. Verifikasi walkthrough muncul otomatis dimulai dari Step 1 of 6
21. Klik `[Skip]` pada Step 1
22. Verifikasi walkthrough tertutup
23. Muat ulang halaman (F5)
24. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
25. Verifikasi walkthrough tidak muncul otomatis setelah F5

### TC-FA-TDC-654: Skip lewat klik overlay gelap menutup walkthrough dan menyimpan flag seen

26. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
27. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
28. Verifikasi walkthrough muncul otomatis dimulai dari Step 1 of 6
29. Klik area overlay gelap di luar spotlight
30. Verifikasi walkthrough tertutup
31. Muat ulang halaman (F5)
32. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
33. Verifikasi walkthrough tidak muncul otomatis setelah F5

## Notes

- Urutan TC dalam spec: TC-FA-TDC-652, TC-FA-TDC-655, TC-FA-TDC-653, lalu TC-FA-TDC-654. TC-FA-TDC-652 dan TC-FA-TDC-655 berjalan dengan flag seen true (keadaan awal suite), sedangkan TC-FA-TDC-653 dan TC-FA-TDC-654 menghapus flag; urutan ini membatasi penghapusan flag pada dua blok terakhir.
- Asersi tambahan di luar Expected TC (S-03): langkah 20 dan 28 (walkthrough sempat muncul dari Step 1 sebagai anchor positif sebelum asersi "tertutup"), langkah 8, 24, dan 32 (halaman termuat sebagai anchor absence walkthrough, 8b.2), dan langkah 11 mendahului langkah 12 sebagai anchor tombol `[Back]` tidak dirender.
- Langkah penghubung (S-03): langkah 17 (menutup walkthrough dengan `[Skip]`), langkah 18, 19, 26, dan 27 (menghapus flag dan membuka layar awal untuk kunjungan pertama).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-653 dan TC-FA-TDC-654 menyebut "Flag seen belum ada" tanpa cara menyetelnya; mekanismenya disediakan tim FE/BE (S-13).
  - TC-FA-TDC-652 butir c dan d, TC-FA-TDC-653 butir a, dan TC-FA-TDC-654 butir a mengasersi ketiadaan walkthrough tanpa anchor di TC; spec menambah anchor halaman termuat.
  - TC-FA-TDC-655 tidak menyebut flag seen; spec memakai flag true (keadaan awal suite).
