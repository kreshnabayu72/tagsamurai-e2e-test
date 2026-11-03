---
id: TC-AC-LA-E2E-106-setup-column-list-drag-dan-pin
title: "Setup Column List: Drag Urutan dan Pin Kolom Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-323
  - TC-AC-LA-324
coverage:
  web: automated
---

# Setup Column List: Drag Urutan dan Pin Kolom Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada tab Current; lebar tabel melebihi viewport sehingga scroll horizontal tersedia) bersifat baca-saja untuk spec ini; spec tidak menulis data alokasi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (urutan dan pin). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4). Viewport dipersempit agar scroll horizontal tabel tersedia.
- Parameter langkah 2 sampai 8 (TC-AC-LA-323), satu baris per kolom: `Allocation ID`, `License Type`, `Product`, `Client`, `Subscription ID`, `Quantity`, `Plan Owner`, `Allocated By`, `Status`.
- Parameter langkah 16 sampai 28 (TC-AC-LA-324), satu baris per kolom: `Allocation ID`, `License Type`, `Product`, `Client`, `Subscription ID`, `Quantity`, `Plan Owner`, `Allocated By`, `Status`, `Last Updated`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-323: Geser urutan kolom Hideable

1. Buka Popup Setup Column
2. Untuk setiap baris tabel parameter TC-AC-LA-323 (langkah 2 sampai 8): geser Kolom ke posisi terakhir di Popup Setup Column
3. Verifikasi Kolom berada di posisi terakhir pada Preview
4. Klik `[Save]`
5. Verifikasi Kolom berada di posisi terakhir pada tabel
6. Muat ulang halaman (F5)
7. Verifikasi urutan Kolom di posisi terakhir tetap setelah F5
8. Buka Popup Setup Column
9. Geser `Last Updated` ke posisi pertama di Popup Setup Column
10. Verifikasi `Last Updated` berada di posisi pertama pada Preview
11. Klik `[Save]`
12. Verifikasi `Last Updated` berada di posisi pertama pada tabel
13. Muat ulang halaman (F5)
14. Verifikasi urutan `Last Updated` di posisi pertama tetap setelah F5

### TC-AC-LA-324: Pin dan unpin kolom Hideable

15. Buka Popup Setup Column
16. Untuk setiap baris tabel parameter TC-AC-LA-324 (langkah 16 sampai 28): klik ikon Pin pada Kolom
17. Klik `[Save]`
18. Scroll tabel horizontal
19. Verifikasi Kolom tetap di kiri saat scroll horizontal
20. Muat ulang halaman (F5)
21. Scroll tabel horizontal
22. Verifikasi pin Kolom persist setelah F5 (Kolom tetap di kiri)
23. Buka Popup Setup Column
24. Klik ikon Pin pada Kolom untuk Unpin
25. Klik `[Save]`
26. Scroll tabel horizontal
27. Verifikasi Kolom ikut bergeser saat scroll horizontal
28. Buka Popup Setup Column
29. Klik `(X)` untuk menutup Popup Setup Column

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah `Buka Popup Setup Column` berarti: klik `⋯` pada header kolom Actions, lalu klik `Setup Column...`.
- Langkah 2 sampai 8 diulang untuk sembilan baris tabel parameter (63 langkah terekspansi) dan langkah 16 sampai 28 diulang untuk sepuluh baris tabel parameter (130 langkah terekspansi); total sekitar 215 langkah terekspansi. Verifikasi tetap satu per klausa per iterasi (butir a sampai j TC-AC-LA-323 dan TC-AC-LA-324).
- Alasan spec melewati sekitar 35 langkah: dua TC satu topik (konfigurasi urutan dan pin kolom Hideable) pada satu dataset baca-saja dengan langkah berulang per kolom berparameter tabel Prerequisites, tanpa langkah bersyarat (konvensi bagian 8b butir 7).
- Langkah penghubung (S-03): langkah 8, 23, 28 (membuka Popup lagi sesudah muat ulang), langkah 29 (menutup Popup tanpa mengubah).
- Temuan untuk QA:
  - TC-AC-LA-323 langkah 2 menyuruh `Allocation ID` digeser ke posisi terakhir lalu kolom lain diulang; hasil akhir `Last Updated` ke posisi pertama sudah pada posisi pertama sebab seluruh kolom lain dipindah ke akhir. Spec mengikuti langkah TC apa adanya.
  - TC-AC-LA-324 tidak menyebut lebar viewport yang membuat scroll horizontal tersedia; spec menuliskannya sebagai kemampuan teknis.
  - Batas pin tiga kolom (TC-AC-LA-330) dipenuhi karena tiap kolom di-Unpin sebelum iterasi berikutnya.
