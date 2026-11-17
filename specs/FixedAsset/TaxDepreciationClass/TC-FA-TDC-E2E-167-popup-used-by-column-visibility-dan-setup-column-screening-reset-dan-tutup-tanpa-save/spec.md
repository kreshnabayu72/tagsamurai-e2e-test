---
id: TC-FA-TDC-E2E-167-popup-used-by-column-visibility-dan-setup-column-screening-reset-dan-tutup-tanpa-save
title: "Popup Used By: Column Visibility, Setup Column Screening, Reset, dan Tutup Tanpa Save"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-595
  - TC-FA-TDC-596
  - TC-FA-TDC-600
  - TC-FA-TDC-601
sourceRules: ["§4.1.6#r1", "§4.1.6#r2", "§4.1.6#r3", "§4.4#r11", "§4.1#r8"]
smoke: []
dependsOn: []
trace:
  "§4.1.6#r1": [4, 5, 12, 13, 23, 27]
  "§4.1.6#r2": [4, 5, 12, 13, 23, 27]
  "§4.1.6#r3": [4, 5, 12, 13, 23, 27]
  "§4.4#r11": 7
  "§4.1#r8": 9
anchor: [3, 6, 10, 11, 14, 15, 16, 32, 33, 38, 39]
coverage:
  web: automated
---

# Popup Used By: Column Visibility, Setup Column Screening, Reset, dan Tutup Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
- Kemampuan teknis: Overlay Column Visibility dan Popup Setup Column pada Popup Used By; drag and drop kolom; tombol Esc; konfigurasi kolom Popup Used By tersimpan di browser dan dibaca ulang setelah muat ulang halaman (pemulihan lewat langkah eksplisit; 8b.14, R-24).
- State global yang diubah: konfigurasi kolom Popup Used By (Asset Class disembunyikan dan Asset Names digeser pada langkah 17 sampai 19) dikembalikan ke default oleh `[Reset to Default]` dan `[Save]` (langkah 22 sampai 24). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-595: Screening Overlay Column Visibility Popup Used By

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
2. Klik icon `⋯` pada header kolom Actions
3. Verifikasi Overlay tampil menempel pada pemicu tanpa backdrop
4. Verifikasi Overlay memuat daftar kolom berurutan: `Asset Class | Tax Method | Asset Names`
5. Verifikasi status checkbox default: Asset Class checked dan enabled; Tax Method checked dan enabled; Asset Names checked dan enabled
6. Verifikasi setiap baris kolom memiliki drag handle
7. Verifikasi item `Setup Column...` ada di bagian bawah panel

### TC-FA-TDC-596: Screening Popup Setup Column Popup Used By

8. Klik `Setup Column...`
9. Verifikasi Header: Title `Setup Column`
10. Verifikasi Header: Deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi Header: tombol Close `(X)` di kanan atas
12. Verifikasi Body: daftar kolom berurutan `Asset Class | Tax Method | Asset Names` dengan checkbox, drag handle, dan icon Pin per baris
13. Verifikasi Body: status checkbox default: Asset Class checked; Tax Method checked; Asset Names checked
14. Verifikasi Body: Live Preview tabel menampilkan urutan header dan data sel yang sama dengan tabel asli
15. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan
16. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-FA-TDC-600: Reset to Default di Popup Setup Column Popup Used By

17. Hapus centang kolom Asset Class
18. Drag kolom Asset Names ke posisi paling atas daftar
19. Klik `[Save]`
20. Klik icon `⋯` pada header kolom Actions
21. Klik `Setup Column...`
22. Klik `[Reset to Default]`
23. Verifikasi Live Preview kembali ke susunan default (urutan dan visibilitas awal)
24. Klik `[Save]`
25. Muat ulang halaman (F5)
26. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
27. Verifikasi susunan kolom tabel sama dengan default awal

### TC-FA-TDC-601: Menutup Popup Setup Column Popup Used By tanpa Save membuang perubahan

28. Klik icon `⋯` pada header kolom Actions
29. Klik `Setup Column...`
30. Hapus centang kolom Asset Class
31. Klik `(X)` pada Popup Setup Column
32. Verifikasi Popup Setup Column tertutup
33. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (Asset Class tampil)
34. Klik icon `⋯` pada header kolom Actions
35. Klik `Setup Column...`
36. Hapus centang kolom Asset Class
37. Tekan Esc
38. Verifikasi Popup Setup Column tertutup
39. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (Asset Class tampil)
40. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-595, 596, 600, 601. Popup Used By NB-1 dibuka sekali (langkah 1) dan dipertahankan sepanjang TC, kecuali muat ulang langkah 25 yang menutupnya sehingga dibuka lagi pada langkah 26. Popup Setup Column dari TC-FA-TDC-596 dipertahankan terbuka dan dipakai langsung oleh TC-FA-TDC-600 (langkah 17); langkah TC "Buka Popup Setup Column" TC-FA-TDC-600 pertama diwakili popup yang sudah terbuka.
- Alasan lebih dari sekitar 35 langkah (40 langkah): satu popup dan satu topik (Overlay Column Visibility dan Popup Setup Column pada Popup Used By), satu kelas harness, dan tiap blok TC berdiri sendiri; langkah buka overlay dan popup berulang karena TC memang membukanya kembali tiap blok.
- Langkah penghubung (S-03): langkah 25 dan 26 (muat ulang dan membuka kembali Popup Used By agar TC-FA-TDC-600 mengasersi persistensi sesuai TC), langkah 40 (menutup popup). Pemulihan Setup Column: `[Reset to Default]` lalu `[Save]` pada langkah 22 sampai 24 adalah bagian TC-FA-TDC-600 dan sekaligus memulihkan default (8b.14, R-24). Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 tidak perlu dicari lewat Search (8b.13).
- Asersi absence langkah 16 didahului anchor positif langkah 15 (tombol lain footer tampil; 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-595, 596, 600, dan 601 menyebut ikon `⋯` pada "header kolom Actions", sedangkan TC-FA-TDC-579 menyebut kolom itu `Column Visibility (⋯)`; spec memakai notasi TC masing-masing.
  - TC-FA-TDC-600 langkah 2 menulis dua pengaturan sekaligus (uncheck Asset Class, drag Asset Names) tanpa Expected antara; spec tidak mengasersi keadaan antara.
  - TC-FA-TDC-601 Expected tidak menyebut keadaan Live Preview saat popup ditutup; spec mengasersi popup tertutup dan tabel memakai konfigurasi tersimpan.
  - Email akun Total Control tidak tertulis di TC.
