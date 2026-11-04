---
id: TC-FA-TDC-E2E-184-guided-tooltip-keyboard-dan-replay-melewati-kolom-tersembunyi
title: "Guided Tooltip: Keyboard dan Replay Melewati Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-659
  - TC-FA-TDC-933
coverage:
  web: automated
---

# Guided Tooltip: Keyboard dan Replay Melewati Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite dan seeding mengikuti `suite.md`. Flag `guided_tooltip_seen_fa-tax-depreciation-class` bernilai true dari hook suite `before` dan tidak diubah spec ini (keadaan awal kedua TC; walkthrough dibuka lewat tombol `[?]`).
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.seedClasses` berisi tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) belum diubah. Data Dinamis: tidak ada.
- Data uji TC-FA-TDC-933: kolom disembunyikan Allowed Methods dan Effective From (kolom Class Code dan Used By tetap tampil); step yang tampil 4 dari 6 (Class Code, Used By, Filter, Changelog).
- Kemampuan teknis: menekan Enter, panah kiri, panah kanan, dan Esc pada walkthrough; Popup Setup Column tabel utama; konfigurasi kolom tabel utama tersimpan di browser; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel utama pada blok TC-FA-TDC-933; kolom Allowed Methods dan Effective From disembunyikan pada langkah 13 sampai 15 dan ditampilkan kembali pada langkah 35 sampai 39. Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-659: Walkthrough dapat dioperasikan dengan keyboard

1. Klik tombol `[?]`
2. Verifikasi kotak tooltip menerima fokus keyboard
3. Tekan Enter
4. Verifikasi Step 2 of 6 tampil
5. Tekan panah kiri
6. Verifikasi Step 1 of 6 tampil
7. Tekan panah kanan
8. Verifikasi Step 2 of 6 tampil
9. Tekan Esc
10. Verifikasi walkthrough tertutup

### TC-FA-TDC-933: Replay melewati step yang kolom targetnya disembunyikan

11. Klik icon `⋯` pada header kolom Actions
12. Klik `Setup Column...`
13. Hapus centang kolom Allowed Methods
14. Hapus centang kolom Effective From
15. Klik `[Save]`
16. Klik tombol `[?]` di sebelah kanan Breadcrumb
17. Verifikasi indikator `Step 1 of 4`
18. Verifikasi Step 1 menyorot header kolom Class Code dengan Title `Tax Depreciation Class`
19. Klik `[Next]`
20. Verifikasi indikator `Step 2 of 4`
21. Verifikasi Step 2 menyorot header kolom Used By dengan Title `Used By`
22. Klik `[Next]`
23. Verifikasi indikator `Step 3 of 4`
24. Verifikasi Step 3 menyorot icon Filter di toolbar dengan Title `Filter Tax Depreciation Classes`
25. Klik `[Next]`
26. Verifikasi indikator `Step 4 of 4`
27. Verifikasi Step 4 menyorot icon Changelog di toolbar dengan Title `Changelog` sebagai step terakhir
28. Verifikasi tidak ada step dengan Title `Allowed Methods` atau `Effective From`
29. Verifikasi tidak ada spotlight pada elemen yang tidak tampil
30. Verifikasi tidak ada penghitung `of 6` pada semua step
31. Verifikasi nomor step berurutan 1, 2, 3, 4 tanpa lompatan
32. Verifikasi walkthrough tidak berpindah halaman
33. Verifikasi walkthrough tidak membuka dialog
34. Klik `[Skip]`
35. Klik icon `⋯` pada header kolom Actions
36. Klik `Setup Column...`
37. Centang kolom Allowed Methods
38. Centang kolom Effective From
39. Klik `[Save]`

## Notes

- Alasan lebih dari sekitar 35 langkah: satu kelas harness dan satu topik (Guided Tooltip pada halaman yang sama dengan flag true); TC-FA-TDC-659 berdiri sendiri sebagai blok pertama dan TC-FA-TDC-933 sebagai blok kedua, dan 10 langkah pada blok kedua adalah pengaturan serta pemulihan kolom (8b.14).
- Asersi tambahan di luar Expected TC (S-03): langkah 2 sampai 4 pada TC-FA-TDC-659 mengamati transisi walkthrough sebelum langkah berikutnya mengubahnya (8b.5), dan Step 2 pada langkah 8 menjadi anchor positif sebelum asersi tertutup pada langkah 10. Langkah 28 dan 29 (absence) didahului langkah 17 sampai 27 yang membuktikan keempat step tampil.
- Langkah penghubung (S-03): langkah 11 sampai 15 (menyembunyikan kolom yang disyaratkan precondition e), langkah 34 (menutup walkthrough dengan `[Skip]`), langkah 35 sampai 39 (menampilkan kembali kolom, 8b.14).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-933 precondition e menyebut kolom disembunyikan lewat Setup Column tanpa menyatakan caranya; spec menyembunyikan kolom lewat Popup Setup Column dan menyimpannya.
  - TC-FA-TDC-933 Expected e ("`[Total]` bernilai 4 di semua step", "`[N]` berurutan 1, 2, 3, 4") dituliskan melalui langkah 17, 20, 23, dan 26 serta langkah 30 dan 31.
  - TC-FA-TDC-659 tidak menyebut tombol atau elemen yang menerima fokus; spec mengasersi kotak tooltip menerima fokus keyboard.
