---
id: TC-FA-TDC-E2E-163-popup-used-by-screening-isi-kolom-dan-penanda-warning
title: "Popup Used By: Screening, Isi Kolom, dan Penanda Warning"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-579
  - TC-FA-TDC-580
  - TC-FA-TDC-581
  - TC-FA-TDC-582
coverage:
  web: automated
---

# Popup Used By: Screening, Isi Kolom, dan Penanda Warning

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah Asset Class pemakai:
  - Sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data (NB-1 Used By 5 dengan Class Name `Bukan bangunan – Kelompok 1`; NB-SL Used By 4).
  - NB-1 (TC-FA-TDC-579 dan 580) dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
  - NB-SL (hanya Straight Line; TC-FA-TDC-581 dan 582) dipakai 4 Asset Class: `AC-11 – Mesin Cetak` memakai Declining Balance dan tiga lainnya memakai Straight Line (nama tiga Asset Class itu tidak disebut TC; lihat Temuan untuk QA).
- Kemampuan teknis: mengarahkan kursor untuk tooltip; navigasi keyboard dengan Tab; membaca label aksesibilitas ikon ⚠.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-579: Screening Popup Used By

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
2. Verifikasi Header: Title `Used By`
3. Verifikasi Header: satu baris teks polos `NB-1 – Bukan bangunan – Kelompok 1` di bawah judul
4. Verifikasi Header: ikon Close `(X)` tampil
5. Verifikasi Header: tidak ada tombol teks `[Close]`
6. Verifikasi Header: toolbar tabel memuat Search dan Download
7. Verifikasi Header: `Download` adalah aksi sekunder, bukan primary
8. Verifikasi Body: kolom berurutan `Asset Class`, `Tax Method`, `Asset Names`, dan `Column Visibility (⋯)`
9. Verifikasi Body: `Asset Class`, `Tax Method`, dan `Asset Names` sortable, sedangkan `Column Visibility (⋯)` unsortable (klik header membuka Overlay Column Visibility)
10. Verifikasi Body: 5 baris urut Asset Class A-Z: AC-01, AC-02, AC-03, AC-04, AC-05
11. Verifikasi Footer: Pagination dengan page size default 10

### TC-FA-TDC-580: Isi kolom Popup Used By: format Asset Class, Tax Method, dan Asset Names

12. Verifikasi Asset Class berformat `[Class Code] – [Class Name]`: `AC-01 – Mesin Produksi`, `AC-02 – Peralatan Kantor`, `AC-03 – Kendaraan Operasional`, `AC-04 – Komputer`, `AC-05 – Furnitur`
13. Verifikasi Tax Method: AC-01 `Straight Line`, AC-02 `Straight Line`, AC-03 `Declining Balance`, AC-04 `Declining Balance`, AC-05 `Straight Line`
14. Verifikasi Asset Names (integer): AC-01 `12`, AC-02 `30`, AC-03 `7`, AC-04 `25`, AC-05 `18`
15. Verifikasi jumlah baris tabel (5) sama dengan angka Used By `5` pada baris NB-1 di tabel utama
16. Tutup Popup Used By lewat ikon Close `(X)`

### TC-FA-TDC-581: Penanda ⚠ pada Asset Class yang Tax Method-nya tidak lagi diizinkan

17. Klik angka `4` pada baris NB-SL untuk membuka Popup Used By
18. Verifikasi ikon ⚠ tampil di depan `AC-11 – Mesin Cetak`
19. Verifikasi tiga Asset Class lain tanpa ikon ⚠
20. Arahkan kursor ke ikon ⚠ pada `AC-11 – Mesin Cetak`
21. Verifikasi tooltip `Tax method Declining Balance is no longer allowed by this class.`
22. Inspeksi label aksesibilitas ikon ⚠
23. Verifikasi label aksesibilitas ikon sama dengan teks tooltip
24. Tutup Popup Used By lewat ikon Close `(X)`

### TC-FA-TDC-582: Tooltip ⚠ dapat diakses lewat keyboard focus

25. Klik angka `4` pada baris NB-SL untuk membuka Popup Used By
26. Tekan Tab hingga fokus berada pada ikon ⚠
27. Verifikasi tooltip `Tax method Declining Balance is no longer allowed by this class.` tampil saat ikon ⚠ menerima fokus
28. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-579, 580, 581, 582. TC-FA-TDC-579 dan 580 memakai Popup Used By NB-1 yang sama sehingga dibuka sekali (langkah 1) dan ditutup sesudah TC-FA-TDC-580 (langkah 16); langkah TC "Klik angka `5`" TC-FA-TDC-580 dan "Amati 5 baris tabel" diwakili langkah 1 dan 12 sampai 14. TC-FA-TDC-581 dan 582 memakai NB-SL sehingga popup dibuka ulang (langkah 25) agar fokus keyboard dimulai dari popup baru, bukan dari kursor hover langkah 20.
- Langkah penghubung (S-03): langkah 16, 24, dan 28 (menutup popup lewat ikon Close; TC tidak menyebut cara menutup).
- Asersi absence langkah 5 didahului anchor positif langkah 4 (ikon Close tampil pada header yang sama; 8b.2), dan langkah 19 didahului langkah 18 (ikon ⚠ pada baris lain di tabel yang sama tampil).
- Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 dan NB-SL tidak perlu dicari lewat Search (8b.13).
- Temuan untuk QA:
  - TC-FA-TDC-579 butir Header iv menyebut `Download` sebagai aksi sekunder tanpa cara observasi (gaya tombol); spec mengasersinya apa adanya.
  - TC-FA-TDC-581 tidak menyebut nama tiga Asset Class lain milik NB-SL selain `AC-11 – Mesin Cetak`; TC-FA-TDC-929 menyebut `AC-12`, `AC-13`, dan `AC-14` pada data yang sama. Label aksesibilitas (atribut) tidak disebut TC; spec mengasersi kesamaannya dengan teks tooltip.
  - TC-FA-TDC-582 tidak menyebut jumlah penekanan Tab hingga fokus mencapai ikon ⚠; spec menulis "Tekan Tab hingga fokus berada pada ikon ⚠".
  - Email akun Total Control tidak tertulis di TC.
