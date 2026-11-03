---
id: TC-AC-LA-E2E-105-setup-column-list-screening-dan-ceklis
title: "Setup Column List: Screening Overlay dan Popup, serta Ceklis Kolom Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-320
  - TC-AC-LA-321
  - TC-AC-LA-322
coverage:
  web: automated
---

# Setup Column List: Screening Overlay dan Popup, serta Ceklis Kolom Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada tab Current) bersifat baca-saja untuk spec ini; spec tidak menulis data alokasi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column. Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-320: Screening overlay Column Visibility

1. Klik `⋯` pada header kolom Actions
2. Verifikasi daftar kolom berurutan `Allocation ID`, `License Type`, `Product`, `Client`, `Subscription ID`, `Quantity`, `Plan Owner`, `Allocated By`, `Status`, `Last Updated` tercentang dan enabled
3. Verifikasi `Plan`, `Payment`, `Paid From`, dan `Cost` tidak tercentang dan enabled
4. Verifikasi drag handle tersedia pada tiap kolom
5. Verifikasi item `Setup Column...` tampil di bagian bawah

### TC-AC-LA-321: Screening Popup Setup Column

6. Klik `Setup Column...`
7. Verifikasi Header: judul `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol silang `(X)`
8. Verifikasi Body: daftar 14 kolom tampil
9. Verifikasi checkbox tersedia pada tiap kolom
10. Verifikasi drag handle tersedia pada tiap kolom
11. Verifikasi ikon Pin tersedia pada tiap kolom
12. Verifikasi Live Preview tabel tampil
13. Verifikasi Footer: `[Reset to Default]` dan `[Save]`
14. Verifikasi tidak ada `[Cancel]`

### TC-AC-LA-322: Ceklis dan unceklis kolom Hideable

15. Hapus centang `Allocation ID`, `License Type`, `Product`, `Client`, dan `Subscription ID`
16. Verifikasi kelima kolom itu hilang dari Preview
17. Klik `[Save]`
18. Verifikasi kelima kolom itu hilang dari tabel
19. Muat ulang halaman (F5)
20. Verifikasi kelima kolom itu tetap tersembunyi
21. Klik `⋯` pada header kolom Actions
22. Klik `Setup Column...`
23. Centang kembali `Allocation ID`, `License Type`, `Product`, `Client`, dan `Subscription ID`
24. Hapus centang `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated`
25. Verifikasi kelima kolom `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated` hilang dari Preview
26. Klik `[Save]`
27. Verifikasi `Allocation ID`, `License Type`, `Product`, `Client`, dan `Subscription ID` tampil lagi di tabel
28. Verifikasi `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated` hilang dari tabel
29. Muat ulang halaman (F5)
30. Verifikasi `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated` tetap tersembunyi
31. Klik `⋯` pada header kolom Actions
32. Klik `Setup Column...`
33. Centang kembali `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated`
34. Klik `[Save]`
35. Verifikasi `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated` tampil lagi di tabel

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Popup Setup Column dari TC-AC-LA-321 (langkah 6) tetap terbuka sebagai awal TC-AC-LA-322 (langkah 15).
- Langkah 15, 23, 24, 33 menangani lima kolom sekaligus; `Verifikasi` yang menyebut kelima kolom adalah daftar elemen yang disebut utuh dan sama-sama hilang atau tampil (S-01, daftar elemen). Klausa Preview, tabel, dan F5 tetap `Verifikasi` terpisah per kolom grup.
- Langkah penghubung (S-03): langkah 21 dan 22, 31 dan 32 (membuka Popup lagi sesudah muat ulang).
- Temuan untuk QA:
  - TC-AC-LA-322 Expected a sampai e memakai satu kalimat untuk empat klausa per kolom (Preview, tabel setelah Save, F5, tampil lagi); spec memecahnya per klausa dan menyatukan lima kolom satu grup dalam satu `Verifikasi`.
  - TC-AC-LA-322 langkah 3 menyuruh Save sesudah mencentang kembali grup kedua tetapi tidak menyebut asersi sesudah Save selain butir "tampil lagi"; spec mengasersi hanya butir itu.
