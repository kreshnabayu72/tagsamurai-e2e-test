---
id: TC-FA-TDC-E2E-101-delete-single-screening-cancel-esc-backdrop-lalu-delete-class
title: "Delete Single: Screening Dialog, Cancel, Esc, Backdrop, lalu Delete Class"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-393
  - TC-FA-TDC-396
  - TC-FA-TDC-397
  - TC-FA-TDC-398
  - TC-FA-TDC-394
  - TC-FA-TDC-395
coverage:
  web: automated
---

# Delete Single: Screening Dialog, Cancel, Esc, Backdrop, lalu Delete Class

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-4 (nama "Bukan bangunan – Kelompok 4") Active dengan Used By 0 dan Last Posted Tax Year kosong; NB-OLD (Inactive) dengan Used By 0 dan Last Posted Tax Year kosong. NB-4 dan NB-OLD adalah target hapus (langkah 24 sampai 37) dan dihapus oleh spec ini. Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` menyeed ulang NB-4 dan NB-OLD yang dihapus. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class lewat API; kemampuan baca jumlah entri Changelog class NB-4 untuk entri Delete (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12); menekan `Esc` dan mengklik backdrop dialog.
- State global yang diubah: tidak ada (class NB-4 dan NB-OLD dipulihkan di hook `after`).

## Test Steps

### TC-FA-TDC-393: Screening dialog Delete single (lolos kedua guard) dari row action Delete

1. Catat baseline jumlah entri Delete Changelog class NB-4
2. Klik tombol `⋯` baris NB-4 lalu `Delete`
3. Verifikasi dialog dengan judul `Delete Tax Depreciation Class`, body bullet `• NB-4 – Bukan bangunan – Kelompok 4` lalu kalimat `This action cannot be undone. Are you sure you want to delete it?`, dan footer tombol `[Cancel]` lalu `[Delete]` bergaya danger

### TC-FA-TDC-396: Cancel pada dialog Delete tidak menghapus class

4. Klik `[Cancel]` pada dialog Delete
5. Verifikasi dialog menutup
6. Verifikasi baris NB-4 tetap ada di tabel
7. Verifikasi tidak ada toast
8. Verifikasi jumlah entri Delete Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log Delete)

### TC-FA-TDC-397: Tombol Esc menutup dialog Delete setara Cancel

9. Klik tombol `⋯` baris NB-4 lalu `Delete`
10. Tekan tombol `Esc`
11. Verifikasi dialog menutup
12. Verifikasi baris NB-4 tetap ada di tabel
13. Verifikasi tidak ada toast
14. Verifikasi jumlah entri Delete Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log Delete)

### TC-FA-TDC-398: Klik backdrop tidak menutup dialog Delete (D-06)

15. Klik tombol `⋯` baris NB-4 lalu `Delete`
16. Klik area gelap di luar dialog (backdrop)
17. Verifikasi dialog Delete tetap terbuka
18. Verifikasi baris NB-4 tetap ada
19. Verifikasi tidak ada toast
20. Tekan `Esc`
21. Verifikasi dialog menutup
22. Verifikasi baris NB-4 tetap ada
23. Verifikasi jumlah entri Delete Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log Delete)

### TC-FA-TDC-394: Delete class yang lolos kedua guard menghapus class secara permanen

24. Klik tombol `⋯` baris NB-4 lalu `Delete`
25. Klik `[Delete]` pada dialog
26. Verifikasi dialog menutup
27. Verifikasi toast sukses `Success, tax depreciation class has been deleted.`
28. Verifikasi baris NB-4 tidak ada di tabel
29. Klik ikon Changelog di toolbar
30. Verifikasi modal Changelog tetap memuat entri-entri lama NB-4
31. Verifikasi jumlah entri Delete Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1 (satu entri Delete baru)
32. Tutup modal Changelog

### TC-FA-TDC-395: Delete class Inactive yang lolos guard

33. Klik tombol `⋯` baris NB-OLD lalu `Delete`
34. Klik `[Delete]` pada dialog
35. Verifikasi dialog menutup
36. Verifikasi toast sukses `Success, tax depreciation class has been deleted.`
37. Verifikasi baris NB-OLD tidak ada di tabel

## Notes

- Spec ini 37 langkah, di atas sekitar 35 langkah. Alasan: satu topik (dialog Delete single dari row action yang sama) dengan urutan screening, batal, lalu aksi yang menghapus data di akhir (prinsip bagian 3). Blok tidak sepenuhnya berdiri sendiri: baseline langkah 1 dipakai pembanding oleh blok TC-FA-TDC-396, 397, 398, dan 394 (langkah 8, 14, 23, 31), dan dialog yang dibuka langkah 2 menjadi pembuka blok TC-FA-TDC-396 (langkah 4 langsung `[Cancel]`). Blok TC-FA-TDC-395 berdiri sendiri; pemecahan lebih lanjut memutus rantai baseline dan dialog tersebut. Pembagian TC lintas spec: dialog blok Guard 1/2 ada di spec 102 dan 103.
- Urutan TC: 393, 396, 397, 398, 394, 395 (aksi yang menghapus data di akhir). Dialog dari langkah 2 dipakai sebagai pembuka TC-FA-TDC-396 (langkah 1 TC: klik `⋯` dan `Delete` yang sama; keadaan identik), sehingga langkah 4 langsung `[Cancel]`.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog, dipakai pembanding langkah 8, 14, 23, dan 31 karena tidak ada aksi yang mengubah log sebelum langkah 25) dan langkah 32 (menutup modal Changelog).
- Absence "tidak ada toast" pada langkah 7, 13, dan 19 diletakkan segera setelah pemicu dengan Verifikasi dialog menutup dan baris yang tetap ada sebagai anchor tabel termuat (8b.2, 8b.11). Baris hilang pada langkah 28 dan 37 memakai toast sukses langkah 27 dan 36 sebagai anchor (8b.2).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - Post Condition TC-FA-TDC-394 (class beserta seluruh versinya terhapus, NB-4 hilang dari pilihan Asset Class, log L-05 di tiga surface) dan TC-FA-TDC-395 ("Class NB-OLD terhapus permanen") tidak punya langkah observasi di luar Expected; tidak diasersi terpisah (S-01). Pengecekan lintas modul ada di spec modul sinkronisasi dan pencatatan log.
  - TC-FA-TDC-394 Expected c ("satu entri Delete baru") dibaca sebagai selisih jumlah entri terhadap baseline (S-12); TC tidak menyebut cara memisahkan entri Delete dari entri lain NB-4.
  - TC-FA-TDC-396, 397, dan 398 menyebut "tidak ada entri log Delete untuk NB-4" tanpa pembanding; spec memakai baseline jumlah entri (langkah 1).
  - TC-FA-TDC-398 langkah 1 memuat klaim "→ dialog Delete terbuka" pada langkah aksi; spec menuliskannya sebagai Verifikasi sendiri (R-02).
