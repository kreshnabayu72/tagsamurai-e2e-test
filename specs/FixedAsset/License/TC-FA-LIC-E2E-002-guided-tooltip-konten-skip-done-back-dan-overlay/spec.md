---
id: TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay
title: "Guided Tooltip: Konten, Back, Overlay, Resize, Skip, dan Done"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-4
  - TC-FA-LIC-5
  - TC-FA-LIC-6
  - TC-FA-LIC-8
coverage:
  web: automated
---

# Guided Tooltip: Konten, Back, Overlay, Resize, Skip, dan Done

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control tur Pre-setup #19 `totalControlTour_automated_{namaCompany}@qwertysystem.net` (client Paid; kredensial `Spectra.env.FA_TOUR_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Pengecualian flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-license` sendiri. Sesudah hook suite `before`, flag akun #19 dihapus (belum seen) lewat fixture BE di awal tiap blok TC; hook `after` suite memulihkan flag ke true. Kemampuan menghapus dan membaca flag lewat fixture BE disediakan tim FE/BE.
- Kemampuan teknis: mengubah dan memulihkan ukuran viewport browser; muat ulang halaman (F5).
- Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Hook dan kemampuan suite (sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-4: Konten 2 step pada kunjungan pertama

1. Hapus flag `guided_tooltip_seen_fa-license` akun lewat fixture BE
2. Muat ulang halaman License (F5)
3. Verifikasi walkthrough muncul otomatis dari Step 1 pada Tab All License
4. Verifikasi Step 1 menyorot Tabs Bar dengan Title `Switch License Views` dan Description `Switch between the views of this page. Available views depend on your plan.`
5. Klik `[Next]`
6. Verifikasi Step 2 menyorot tabel License Summary dengan Title `Monitor License Capacity` dan Description `Check how much of your license capacity is used and how much remains.`
7. Verifikasi tombol `[Next]` berubah menjadi `[Done]` pada Step 2

### TC-FA-LIC-6: Back tersembunyi di Step 1 dan klik overlay sama dengan Skip

8. Klik `[Back]` pada Step 2
9. Verifikasi Step 1 tampil kembali dengan Title `Switch License Views`
10. Verifikasi tombol `[Back]` tidak tampil (Hidden) pada Step 1
11. Klik area overlay gelap
12. Verifikasi walkthrough tertutup
13. Verifikasi flag seen disetel true (dibaca lewat fixture BE)

### TC-FA-LIC-8: Resize viewport di tengah walkthrough menutup tanpa menyetel flag seen

14. Hapus flag `guided_tooltip_seen_fa-license` akun lewat fixture BE
15. Muat ulang halaman License (F5)
16. Ubah ukuran viewport
17. Verifikasi walkthrough tertutup saat resize
18. Pulihkan ukuran viewport semula
19. Muat ulang halaman License (F5)
20. Verifikasi flag seen tidak disetel (dibaca lewat fixture BE)
21. Verifikasi walkthrough muncul lagi otomatis pada Step 1

### TC-FA-LIC-5: Skip dan Done menyetel flag seen sehingga tidak muncul otomatis lagi

22. Klik `[Skip]` pada Step 1
23. Verifikasi walkthrough tertutup
24. Muat ulang halaman License (F5)
25. Verifikasi Breadcrumb `License > All License` tampil
26. Verifikasi walkthrough tidak muncul otomatis
27. Hapus flag `guided_tooltip_seen_fa-license` akun lewat fixture BE
28. Muat ulang halaman License (F5)
29. Verifikasi walkthrough muncul lagi otomatis
30. Klik `[Next]`
31. Klik `[Done]`
32. Verifikasi `[Done]` menutup walkthrough
33. Muat ulang halaman License (F5)
34. Verifikasi Breadcrumb `License > All License` tampil
35. Verifikasi walkthrough tidak muncul otomatis

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-4, 5, 6, 8). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor untuk menghindari reset flag berulang: blok TC-6 memakai walkthrough yang masih terbuka di Step 2 dari TC-4 (flag belum disetel), TC-8 berakhir dengan walkthrough Step 1 terbuka dan flag belum disetel sehingga TC-5 dapat langsung memulai dengan `[Skip]`. Langkah TC-6 "Klik `[Next]`; klik `[Back]`" dipenuhi oleh `[Next]` pada langkah 5 dan `[Back]` pada langkah 8.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1, 2, 14, 15, 27, 28 (menghapus flag lewat fixture dan memuat ulang halaman agar walkthrough muncul), langkah 18 (memulihkan viewport sebelum memuat ulang), langkah 24, 33 (memuat ulang halaman sesuai langkah TC).
- Langkah 25 dan 34 (Breadcrumb tampil) menjadi anchor positif untuk asersi absence pada langkah 26 dan 35.
- Temuan untuk QA:
  - TC-4 sampai TC-8 tidak menyebut cara mengamati flag seen; langkah 13 dan 20 membaca flag lewat fixture BE (kemampuan disediakan tim FE/BE). TC-5 butir a hanya menyebut "tidak muncul otomatis" dan tidak mengasersi flag.
  - TC-5 langkah 3 meminta "lanjutkan sampai `[Done]`" tanpa menyebut jumlah klik; spec memakai `[Next]` sekali (walkthrough dua step).
