---
id: TC-FA-TDC-E2E-108-resilience-bulk-activate-delete-5xx-timeout-dan-retry-delete
title: "Resilience Bulk Activate dan Bulk Delete: Timeout, Gagal 5xx, dan Retry Delete"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-484
  - TC-FA-TDC-485
  - TC-FA-TDC-486
  - TC-FA-TDC-901
sourceRules: ["§7.3#b1", "§9.6#p1", "R-04", "R-06", "F-FATDC-06.k6", "S-07a", "L-05"]
smoke: []
dependsOn: []
trace:
  "§7.3#b1": [7, 9, 22, 33, 35]
  "§9.6#p1": [7, 8, 10, 21, 23, 33, 34, 36]
  "R-04": 11
  "R-06": [19, 24, 37, 43, 47]
  "F-FATDC-06.k6": 45
  "S-07a": 46
  "L-05": 49
anchor: [20]
coverage:
  web: automated
---

# Resilience Bulk Activate dan Bulk Delete: Timeout, Gagal 5xx, dan Retry Delete

## Prerequisites

- Mode: FE+BE. Respons request bulk Activate, bulk Delete, dan Delete dipaksa gagal lewat `Spectra.intercept()` di atas backend nyata; asersi atas status toggle, baris yang dipertahankan, dan entri Changelog memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data milik spec (disediakan tim FE; class di luar Example Data disediakan lewat seed API): class NB-OLD dan NB-OLD2 berstatus Inactive dengan Used By 0 (target bulk Activate yang gagal, TC-FA-TDC-484); class NB-3 dan NB-4 dengan Used By 0 dan Last Posted Tax Year kosong (target bulk Delete yang gagal, TC-FA-TDC-485 dan 486; NB-4 juga target Delete single TC-FA-TDC-901 yang berhasil pada percobaan kedua dan menghapus NB-4). Tabel berisi tidak lebih dari 10 class dalam satu halaman Pagination, sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` menyeed ulang NB-4 yang dihapus. Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` atas request bulk Activate, bulk Delete, dan Delete (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk (a) mengembalikan respons 500 satu kali, lalu meneruskan request berikutnya ke backend, dan (b) menahan request tanpa respons sampai timeout satu kali; intercept lepas otomatis sesudah satu respons atau timeout (S-09). Kemampuan baca jumlah entri Delete Changelog class NB-4 (disediakan tim FE/BE; baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12). Seed dan pemulihan class lewat API (disediakan tim FE/BE, lihat `suite.md`).
- State global yang diubah: intercept jaringan pada sesi browser (dilepas di hook `after` sebagai cadangan); NB-4 dihapus pada blok TC-FA-TDC-901 (di-seed ulang di hook `after`).

## Test Steps

### TC-FA-TDC-484: Bulk Activate gagal timeout: dialog dan seleksi dipertahankan

1. Catat baseline jumlah entri Delete Changelog class NB-4
2. Aktifkan intercept network: request bulk Activate ditahan tanpa respons sampai timeout
3. Centang checkbox baris NB-OLD dan NB-OLD2
4. Klik `Activate` pada Bulk Action Bar
5. Klik `[Activate]` pada dialog konfirmasi
6. Tunggu sampai timeout
7. Verifikasi toast error `Connection problem. Please try again.` tampil tanpa tombol aksi
8. Verifikasi seleksi dan Bulk Action Bar dipertahankan
9. Verifikasi dialog konfirmasi tetap terbuka
10. Verifikasi tombol `[Activate]` enabled untuk percobaan ulang
11. Verifikasi toggle `Active` NB-OLD dan NB-OLD2 tetap Off pada nilai tersimpan
12. Tutup toast error
13. Klik `[Cancel]` pada dialog konfirmasi
14. Hilangkan centang checkbox baris NB-OLD dan NB-OLD2

### TC-FA-TDC-485: Bulk Delete gagal 5xx: dialog dan seleksi dipertahankan

15. Aktifkan intercept network: request bulk Delete dijawab 500 satu kali
16. Centang checkbox baris NB-3 dan NB-4
17. Klik `Delete` pada Bulk Action Bar
18. Klik `[Delete]` pada dialog konfirmasi
19. Verifikasi toast error `Error, failed to delete tax depreciation class.` tampil
20. Verifikasi toast error tidak hilang otomatis
21. Verifikasi seleksi dan Bulk Action Bar dipertahankan
22. Verifikasi dialog konfirmasi tetap terbuka
23. Verifikasi tombol `[Delete]` enabled untuk percobaan ulang
24. Verifikasi baris NB-3 dan NB-4 tetap ada di tabel
25. Tutup toast error
26. Klik `[Cancel]` pada dialog konfirmasi
27. Hilangkan centang checkbox baris NB-3 dan NB-4

### TC-FA-TDC-486: Bulk Delete gagal timeout: dialog dan seleksi dipertahankan

28. Aktifkan intercept network: request bulk Delete ditahan tanpa respons sampai timeout
29. Centang checkbox baris NB-3 dan NB-4
30. Klik `Delete` pada Bulk Action Bar
31. Klik `[Delete]` pada dialog konfirmasi
32. Tunggu sampai timeout
33. Verifikasi toast error `Connection problem. Please try again.` tampil tanpa tombol aksi
34. Verifikasi seleksi dan Bulk Action Bar dipertahankan
35. Verifikasi dialog konfirmasi tetap terbuka
36. Verifikasi tombol `[Delete]` enabled untuk percobaan ulang
37. Verifikasi baris NB-3 dan NB-4 tetap ada di tabel
38. Tutup toast error
39. Klik `[Cancel]` pada dialog konfirmasi
40. Hilangkan centang checkbox baris NB-3 dan NB-4

### TC-FA-TDC-901: Retry Delete setelah 5xx berhasil tanpa duplikasi log

41. Aktifkan intercept network: request Delete dijawab 500 satu kali
42. Klik tombol `⋯` baris NB-4, `Delete`, lalu `[Delete]` (gagal)
43. Verifikasi toast error `Error, failed to delete tax depreciation class.` tampil
44. Klik `[Delete]` lagi pada dialog yang tetap terbuka
45. Verifikasi dialog menutup
46. Verifikasi baris NB-4 tidak ada di tabel
47. Verifikasi toast sukses `Success, tax depreciation class has been deleted.` tampil
48. Klik ikon Changelog di toolbar
49. Verifikasi jumlah entri Delete Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1
50. Tutup modal Changelog

## Notes

- Spec ini 50 langkah, di atas sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection pada aksi bulk dan Delete) dan berdiri sendiri; tiap blok memuat asersi yang masing-masing satu klausa (S-01), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan menaruh aksi yang menghapus data (TC-FA-TDC-901) di akhir. Bulk Deactivate, Bulk Activate 5xx, dan kegagalan single ada di spec 105, 106, dan 107.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog yang dibandingkan pada langkah 49; tidak ada Delete yang berhasil sebelum langkah 44), langkah 12, 25, dan 38 (menutup toast error persisten, R-12), langkah 13, 26, dan 39 (menutup dialog yang tetap terbuka), langkah 14, 27, dan 40 (menghilangkan seleksi yang dipertahankan, S-09), serta langkah 50 (menutup modal Changelog).
- Pada TC-FA-TDC-901 Expected TC memakai penomoran lokal ("Langkah 2", "Langkah 3"); spec memetakannya ke langkah 43 dan langkah 45 sampai 47 (R-04).
- Absence baris hilang pada langkah 46 memakai toast sukses langkah 47 sebagai anchor; urutan state mendahulukan penutupan dialog (8b.2, 8b.5).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - Class NB-OLD2 tidak ada di Example Data PRD; spec menyebutnya sebagai class tambahan yang di-seed lewat API.
  - TC-FA-TDC-484 dan 486 tidak menyebut durasi timeout dan cara intercept menahan request; spec menuliskannya sebagai kemampuan `Spectra.intercept()` tanpa mengarang endpoint (S-13).
  - TC-FA-TDC-901 Expected c ("tepat satu entri Delete untuk NB-4") dibaca sebagai selisih terhadap baseline (S-12).
