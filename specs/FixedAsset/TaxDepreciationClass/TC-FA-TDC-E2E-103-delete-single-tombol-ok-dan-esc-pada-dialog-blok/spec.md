---
id: TC-FA-TDC-E2E-103-delete-single-tombol-ok-dan-esc-pada-dialog-blok
title: "Delete Single: Tombol OK dan Esc pada Dialog Blok"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-403
  - TC-FA-TDC-404
  - TC-FA-TDC-405
  - TC-FA-TDC-406
coverage:
  web: automated
---

# Delete Single: Tombol OK dan Esc pada Dialog Blok

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-KHS dengan Last Posted Tax Year 2026 dan Used By 0 (Guard 1); NB-2 dengan Used By 3 dan Last Posted Tax Year kosong (Guard 2). Asset Class pemakai dibentuk lewat fixture API (disediakan tim FE/BE). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Semua blok hanya membuka lalu menutup dialog blok; tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class, Last Posted Tax Year, dan Asset Class pemakai lewat API; kemampuan baca jumlah entri Delete Changelog class NB-KHS dan NB-2 (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12); menekan `Esc`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-403: Tombol OK menutup dialog blok Delete tanpa perubahan

1. Catat baseline jumlah entri Delete Changelog class NB-KHS dan class NB-2
2. Klik tombol `⋯` baris NB-KHS lalu `Delete`
3. Klik `[OK]` pada dialog blok
4. Verifikasi dialog menutup
5. Verifikasi baris NB-KHS tetap ada di tabel
6. Verifikasi tidak ada toast
7. Klik ikon Changelog di toolbar
8. Verifikasi modal Changelog menampilkan sedikitnya satu entri
9. Verifikasi jumlah entri Delete Changelog NB-KHS sama dengan baseline langkah 1 (tidak ada entri Delete untuk NB-KHS)
10. Tutup modal Changelog

### TC-FA-TDC-404: Tombol OK menutup dialog blok Delete Guard 2 tanpa perubahan

11. Klik tombol `⋯` baris NB-2 lalu `Delete`
12. Klik `[OK]` pada dialog blok
13. Verifikasi dialog menutup
14. Verifikasi baris NB-2 tetap ada di tabel
15. Verifikasi tidak ada toast
16. Verifikasi jumlah entri Delete Changelog NB-2 sama dengan baseline langkah 1 (tidak ada entri log Delete)

### TC-FA-TDC-405: Tombol Esc menutup dialog blok Delete Guard 1

17. Klik tombol `⋯` baris NB-KHS lalu `Delete`
18. Tekan tombol `Esc`
19. Verifikasi dialog blok menutup
20. Verifikasi baris NB-KHS tetap ada di tabel
21. Verifikasi tidak ada toast
22. Verifikasi jumlah entri Delete Changelog NB-KHS sama dengan baseline langkah 1 (tidak ada entri log baru)

### TC-FA-TDC-406: Tombol Esc menutup dialog blok Delete Guard 2

23. Klik tombol `⋯` baris NB-2 lalu `Delete`
24. Tekan tombol `Esc`
25. Verifikasi dialog blok menutup
26. Verifikasi baris NB-2 tetap ada di tabel
27. Verifikasi tidak ada toast
28. Verifikasi jumlah entri Delete Changelog NB-2 sama dengan baseline langkah 1 (tidak ada entri log baru)

## Notes

- Langkah penghubung (S-03): langkah 1 (baseline Changelog, dipakai pembanding langkah 9, 16, 22, dan 28 karena tidak ada aksi yang mengubah log di antara blok, S-12) dan langkah 10 (menutup modal Changelog).
- Absence "tidak ada toast" pada langkah 6, 15, 21, dan 27 diletakkan segera setelah pemicu dengan Verifikasi dialog menutup dan baris yang tetap ada sebagai anchor tabel termuat (8b.2, 8b.11). Absence entri pada langkah 9 didahului anchor langkah 8.
- Isi dialog blok Guard 1 dan Guard 2 diasersi di spec 102.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-404, 405, dan 406 menyebut "tidak ada entri log Delete/baru" tanpa pembanding; spec memakai baseline jumlah entri (langkah 1).
