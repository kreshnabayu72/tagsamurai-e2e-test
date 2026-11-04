---
id: TC-FA-TDC-E2E-107-resilience-bulk-deactivate-dan-activate-5xx-timeout
title: "Resilience Bulk Deactivate dan Bulk Activate: Gagal 5xx dan Timeout"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-481
  - TC-FA-TDC-482
  - TC-FA-TDC-483
coverage:
  web: automated
---

# Resilience Bulk Deactivate dan Bulk Activate: Gagal 5xx dan Timeout

## Prerequisites

- Mode: FE+BE. Respons request bulk Deactivate dan bulk Activate dipaksa gagal lewat `Spectra.intercept()` di atas backend nyata; asersi atas status toggle tersimpan memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data milik spec (disediakan tim FE; class di luar Example Data disediakan lewat seed API): class NB-3 dan NB-4 Active dengan Used By 0 (target bulk Deactivate, TC-FA-TDC-481 dan 482), serta class NB-OLD dan NB-OLD2 berstatus Inactive dengan Used By 0 (target bulk Activate, TC-FA-TDC-483). Tabel berisi tidak lebih dari 10 class dalam satu halaman Pagination, sehingga baris target tidak dicari lewat Search. Semua request gagal, sehingga tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` atas request bulk Deactivate dan bulk Activate (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk (a) mengembalikan respons 500 satu kali, dan (b) menahan request tanpa respons sampai timeout satu kali; intercept lepas otomatis sesudah satu respons atau timeout (S-09). Seed dan pemulihan class lewat API (disediakan tim FE/BE, lihat `suite.md`).
- State global yang diubah: hanya intercept jaringan pada sesi browser; dilepas di hook `after` sebagai cadangan.

## Test Steps

### TC-FA-TDC-481: Bulk Deactivate gagal 5xx: dialog dan seleksi dipertahankan

1. Aktifkan intercept network: request bulk Deactivate dijawab 500 satu kali
2. Centang checkbox baris NB-3 dan NB-4
3. Klik `Deactivate` pada Bulk Action Bar
4. Klik `[Deactivate]` pada dialog konfirmasi
5. Verifikasi toast error `Error, failed to deactivate tax depreciation class.` tampil
6. Verifikasi toast error tidak hilang otomatis
7. Verifikasi seleksi dan Bulk Action Bar dipertahankan
8. Verifikasi dialog konfirmasi tetap terbuka
9. Verifikasi tombol `[Deactivate]` enabled untuk percobaan ulang
10. Verifikasi toggle `Active` NB-3 dan NB-4 tetap On pada nilai tersimpan
11. Tutup toast error
12. Klik `[Cancel]` pada dialog konfirmasi
13. Hilangkan centang checkbox baris NB-3 dan NB-4

### TC-FA-TDC-482: Bulk Deactivate gagal timeout: dialog dan seleksi dipertahankan

14. Aktifkan intercept network: request bulk Deactivate ditahan tanpa respons sampai timeout
15. Centang checkbox baris NB-3 dan NB-4
16. Klik `Deactivate` pada Bulk Action Bar
17. Klik `[Deactivate]` pada dialog konfirmasi
18. Tunggu sampai timeout
19. Verifikasi toast error `Connection problem. Please try again.` tampil tanpa tombol aksi
20. Verifikasi seleksi dan Bulk Action Bar dipertahankan
21. Verifikasi dialog konfirmasi tetap terbuka
22. Verifikasi tombol `[Deactivate]` enabled untuk percobaan ulang
23. Verifikasi toggle `Active` NB-3 dan NB-4 tetap On pada nilai tersimpan
24. Tutup toast error
25. Klik `[Cancel]` pada dialog konfirmasi
26. Hilangkan centang checkbox baris NB-3 dan NB-4

### TC-FA-TDC-483: Bulk Activate gagal 5xx: dialog dan seleksi dipertahankan

27. Aktifkan intercept network: request bulk Activate dijawab 500 satu kali
28. Centang checkbox baris NB-OLD dan NB-OLD2
29. Klik `Activate` pada Bulk Action Bar
30. Klik `[Activate]` pada dialog konfirmasi
31. Verifikasi toast error `Error, failed to activate tax depreciation class.` tampil
32. Verifikasi toast error tidak hilang otomatis
33. Verifikasi seleksi dan Bulk Action Bar dipertahankan
34. Verifikasi dialog konfirmasi tetap terbuka
35. Verifikasi tombol `[Activate]` enabled untuk percobaan ulang
36. Verifikasi toggle `Active` NB-OLD dan NB-OLD2 tetap Off pada nilai tersimpan
37. Klik `[Cancel]` pada dialog konfirmasi
38. Hilangkan centang checkbox baris NB-OLD dan NB-OLD2

## Notes

- Spec ini 38 langkah, di atas sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection pada aksi bulk) dan berdiri sendiri; tiap blok memuat asersi yang masing-masing satu klausa (S-01), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Bulk Activate timeout, Bulk Delete, dan retry Delete ada di spec 108.
- Langkah penghubung (S-03): langkah 11 dan 24 (menutup toast error persisten agar toast berikutnya tidak tertukar, R-12), langkah 12, 25, dan 37 (menutup dialog yang tetap terbuka), serta langkah 13, 26, dan 38 (menghilangkan seleksi yang dipertahankan, S-09).
- Intercept memakai pola satu kali dan lepas otomatis sehingga tidak ada intercept yang tertinggal setelah pemicu selesai (S-09); langkah 18 menunggu timeout yang disimulasikan intercept.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - Class NB-OLD2 (TC-FA-TDC-483, 484) tidak ada di Example Data PRD; spec menyebutnya sebagai class tambahan yang di-seed lewat API.
  - TC-FA-TDC-482 tidak menyebut durasi timeout dan cara intercept menahan request; spec menuliskannya sebagai kemampuan `Spectra.intercept()` tanpa mengarang endpoint (S-13).
