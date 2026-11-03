---
id: TC-AC-LA-E2E-107-setup-column-list-curated-reset-dan-discard
title: "Setup Column List: Kolom Curated, Reset to Default, dan Discard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-325
  - TC-AC-LA-326
  - TC-AC-LA-327
  - TC-AC-LA-328
coverage:
  web: automated
---

# Setup Column List: Kolom Curated, Reset to Default, dan Discard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada tab Current; Client `PT Sejahtera` dengan Plan `Professional`; Asset Control Station dan Storage dengan Plan `—`; Payment `Free` dan `Wallet`; Paid From `PT ABC (Principal)`; Cost `$150.00`) bersifat baca-saja untuk spec ini; spec tidak menulis data alokasi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column. Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4). Viewport dipersempit agar scroll horizontal tabel tersedia.
- Parameter langkah 11 sampai 15 (TC-AC-LA-326 geser) dan langkah 16 sampai 26 (TC-AC-LA-326 pin), satu baris per kolom: `Plan`, `Payment`, `Paid From`, `Cost`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-325: Ceklis kolom Curated

1. Buka Popup Setup Column
2. Centang `Plan`, `Payment`, `Paid From`, dan `Cost`
3. Klik `[Save]`
4. Verifikasi kolom `Plan`, `Payment`, `Paid From`, dan `Cost` tampil di tabel
5. Verifikasi isi sel Plan adalah Plan snapshot Subscription (`Professional` pada baris PT Sejahtera) dan `—` pada Asset Control Station dan Storage
6. Verifikasi isi sel Payment `Free` atau `Wallet`
7. Verifikasi isi sel Paid From `PT ABC (Principal)` dan `—` pada Payment `Free`
8. Verifikasi isi sel Cost `$150.00` dan `—` pada Payment `Free`
9. Muat ulang halaman (F5)
10. Verifikasi kolom `Plan`, `Payment`, `Paid From`, dan `Cost` tetap tampil

### TC-AC-LA-326: Geser dan pin kolom Curated

11. Untuk setiap baris tabel parameter geser (langkah 11 sampai 15): buka Popup Setup Column
12. Geser Kolom ke posisi pertama
13. Klik `[Save]`
14. Verifikasi Kolom berada di posisi pertama setelah digeser dan Save
15. Muat ulang halaman (F5)
16. Untuk setiap baris tabel parameter pin (langkah 16 sampai 26): buka Popup Setup Column
17. Klik ikon Pin pada Kolom
18. Klik `[Save]`
19. Scroll tabel horizontal
20. Verifikasi Kolom tetap di kiri saat scroll horizontal
21. Muat ulang halaman (F5)
22. Scroll tabel horizontal
23. Verifikasi pin Kolom persist setelah F5 (Kolom tetap di kiri)
24. Buka Popup Setup Column
25. Klik ikon Pin pada Kolom untuk Unpin
26. Klik `[Save]`

### TC-AC-LA-327: Reset to Default

27. Buka Popup Setup Column
28. Hapus centang `Client`
29. Geser `Status` ke posisi pertama
30. Klik ikon Pin pada `Allocation ID`
31. Klik `[Save]`
32. Buka Popup Setup Column
33. Klik `[Reset to Default]`
34. Verifikasi Preview menampilkan 10 kolom Hideable
35. Verifikasi keempat kolom Curated tersembunyi pada Preview
36. Verifikasi tidak ada kolom ter-pin pada Preview
37. Klik `[Save]`
38. Verifikasi tabel menampilkan konfigurasi default (10 kolom Hideable, 4 Curated tersembunyi, tanpa pin)
39. Muat ulang halaman (F5)
40. Verifikasi konfigurasi default persist setelah F5

### TC-AC-LA-328: Tutup Popup membuang perubahan

41. Buka Popup Setup Column
42. Hapus centang `Product` tanpa Save
43. Klik `(X)`
44. Verifikasi perubahan dibuang: kolom `Product` tampil di tabel (konfigurasi tersimpan terakhir)
45. Buka Popup Setup Column
46. Hapus centang `Product` tanpa Save
47. Tekan `Esc`
48. Verifikasi perubahan dibuang: kolom `Product` tampil di tabel (konfigurasi tersimpan terakhir)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah `Buka Popup Setup Column` berarti: klik `⋯` pada header kolom Actions, lalu klik `Setup Column...`.
- Langkah 11 sampai 15 diulang untuk empat baris tabel parameter (20 langkah terekspansi) dan langkah 16 sampai 26 untuk empat baris (44 langkah terekspansi); total sekitar 87 langkah terekspansi. Verifikasi tetap satu per klausa per iterasi.
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (konfigurasi Setup Column List) pada satu dataset baca-saja dengan langkah berulang per kolom berparameter tabel Prerequisites, tanpa langkah bersyarat (konvensi bagian 8b butir 7).
- Langkah penghubung (S-03): langkah 9 dan 21 (muat ulang halaman sebagai bagian langkah TC), langkah 24 dan 25 (Unpin supaya batas tiga pin tidak terlampaui pada iterasi berikutnya).
- Temuan untuk QA:
  - TC-AC-LA-327 langkah 1 ("Ubah visibility, urutan, dan pin kolom") tidak menyebut kolom konkret; spec memakai sembunyikan `Client`, geser `Status` ke posisi pertama, dan pin `Allocation ID`.
  - TC-AC-LA-328 tidak menyebut kolom yang diubah; spec memakai kolom `Product`.
  - TC-AC-LA-326 Expected tidak menyebut hasil sesudah Unpin; spec tidak mengasersinya.
