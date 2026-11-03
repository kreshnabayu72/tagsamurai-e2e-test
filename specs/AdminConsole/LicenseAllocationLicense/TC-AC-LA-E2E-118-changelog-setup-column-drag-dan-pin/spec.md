---
id: TC-AC-LA-E2E-118-changelog-setup-column-drag-dan-pin
title: "Modal Changelog Setup Column: Drag Urutan dan Pin Kolom Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-489
  - TC-AC-LA-490
coverage:
  web: automated
---

# Modal Changelog Setup Column: Drag Urutan dan Pin Kolom Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status dan 25 entri Changelog) bersifat baca-saja untuk spec ini; spec tidak menulis data alokasi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column Changelog (urutan dan pin). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4). Lebar Modal Changelog atau viewport dipersempit agar scroll horizontal tabel Changelog tersedia.
- Parameter langkah 3 sampai 10 (TC-AC-LA-489), satu baris per kolom: `Date`, `Action`, `Allocation ID`, `Field`, `Old Value`, `New Value`.
- Parameter langkah 19 sampai 32 (TC-AC-LA-490), satu baris per kolom: `Date`, `Action`, `Allocation ID`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-489: Geser urutan kolom Hideable Changelog

1. Klik ikon Changelog
2. Buka Popup Setup Column
3. Untuk setiap baris tabel parameter TC-AC-LA-489 (langkah 3 sampai 10): geser Kolom ke posisi terakhir di Popup Setup Column
4. Verifikasi Kolom berada di posisi terakhir pada Preview
5. Klik `[Save]`
6. Verifikasi Kolom berada di posisi terakhir pada tabel
7. Muat ulang halaman (F5)
8. Klik ikon Changelog
9. Verifikasi urutan Kolom di posisi terakhir tetap setelah F5
10. Buka Popup Setup Column
11. Geser `Modified By` ke posisi pertama di Popup Setup Column
12. Verifikasi `Modified By` berada di posisi pertama pada Preview
13. Klik `[Save]`
14. Verifikasi `Modified By` berada di posisi pertama pada tabel
15. Muat ulang halaman (F5)
16. Klik ikon Changelog
17. Verifikasi urutan `Modified By` di posisi pertama tetap setelah F5

### TC-AC-LA-490: Pin dan unpin kolom Hideable Changelog

18. Buka Popup Setup Column
19. Untuk setiap baris tabel parameter TC-AC-LA-490 (langkah 19 sampai 32): klik ikon Pin pada Kolom
20. Klik `[Save]`
21. Scroll tabel Changelog horizontal
22. Verifikasi Kolom tetap di kiri saat scroll horizontal
23. Muat ulang halaman (F5)
24. Klik ikon Changelog
25. Scroll tabel Changelog horizontal
26. Verifikasi pin Kolom persist setelah F5 (Kolom tetap di kiri)
27. Buka Popup Setup Column
28. Klik ikon Pin pada Kolom untuk Unpin
29. Klik `[Save]`
30. Scroll tabel Changelog horizontal
31. Verifikasi Kolom ikut bergeser saat scroll horizontal
32. Buka Popup Setup Column
33. Klik `(X)` untuk menutup Popup Setup Column

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-373 sampai TC-AC-LA-378 ada di spec 117.
- Langkah `Buka Popup Setup Column` berarti: klik `⋯` pada header kolom Actions Changelog, lalu klik `Setup Column...`.
- Langkah 3 sampai 10 diulang untuk enam baris tabel parameter (48 langkah terekspansi) dan langkah 19 sampai 32 diulang untuk tujuh baris (98 langkah terekspansi); total sekitar 165 langkah terekspansi. Verifikasi tetap satu per klausa per iterasi (butir a sampai g TC-AC-LA-489 dan TC-AC-LA-490).
- Alasan spec melewati sekitar 35 langkah: dua TC satu topik (konfigurasi urutan dan pin kolom Hideable Modal Changelog) pada satu dataset baca-saja dengan langkah berulang per kolom berparameter tabel Prerequisites, tanpa langkah bersyarat (konvensi bagian 8b butir 7).
- Langkah penghubung (S-03): langkah 8, 16, 24 (membuka Modal Changelog lagi sesudah muat ulang halaman menutupnya), langkah 10, 18, 27, 32 (membuka Popup lagi), langkah 33 (menutup Popup tanpa mengubah).
- Temuan untuk QA:
  - TC-AC-LA-489 langkah 3 menyuruh enam kolom digeser ke posisi terakhir lalu `Modified By` ke posisi pertama; hasil akhir `Modified By` sudah di posisi pertama sebab seluruh kolom lain dipindah ke akhir. Spec mengikuti langkah TC apa adanya.
  - TC-AC-LA-490 tidak menyebut lebar yang membuat scroll horizontal tabel Changelog tersedia (tujuh kolom); spec menuliskannya sebagai kemampuan teknis.
  - Muat ulang halaman menutup Modal Changelog; TC tidak menyebut pembukaan ulang modal, sehingga spec menambah langkah penghubung.
