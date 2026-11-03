---
id: TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate
title: "Log Tiga Surface: Create, Activate, Deactivate, dan Bulk Activate-Deactivate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-480
  - TC-FA-CF-481
  - TC-FA-CF-492
  - TC-FA-CF-493
  - TC-FA-CF-497
  - TC-FA-CF-498
coverage:
  web: automated
---

# Log Tiga Surface: Create, Activate, Deactivate, dan Bulk Activate-Deactivate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`.
- Data Dinamis: field `Log Create {runId}-124` (Text, Scope General) dan `Log Config {runId}-124` (Numeric, Decimal Places 2, Required Yes, Scope Specific `Pump`). Field baseline yang diubah statusnya: `Depreciated Ratio` (Inactive) dan `Asset Serial Tag` (Active).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log, serta Search nama field pada ketiganya, untuk baseline dan perbandingan; jumlah baris hasil Search nama field Pre-setup (`Depreciated Ratio`, `Asset Serial Tag`) tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline sebelum aksi (S-12). Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset). Langkah 41 memulihkan status Active kedua field baseline di antara TC.
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-480: Create mencatat satu baris Name di tiga surface

1. Klik `[+ Custom Field]`, isi Field Name `Log Create {runId}-124`, pilih Data Type `Text` dan Scope `General`, lalu klik `[Submit]`
2. Tunggu aksi selesai (dialog tertutup atau field kembali kosong dan tabel dimuat ulang)
3. Buka Modal Changelog tab General, ketik Search `Log Create {runId}-124`, tekan Enter
4. Verifikasi Changelog memuat satu baris dengan Action `Create`, Field Name `Log Create {runId}-124`, Field `Name`, Old Value `—`, New Value `Log Create {runId}-124`, Modified By `Sarah J`
5. Verifikasi hasil Search `Log Create {runId}-124` pada Changelog hanya memuat satu baris (nama bersuffix unik, baseline nol; tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
6. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Log Create {runId}-124`, tekan Enter
7. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Create`, Object `Custom Fields`, Name `Log Create {runId}-124`, Field `Name`, Old Value `—`, New Value `Log Create {runId}-124`
8. Verifikasi hasil Search `Log Create {runId}-124` pada System Log `Sarah Johnson` hanya memuat satu baris (nama bersuffix unik, baseline nol; tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
9. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Log Create {runId}-124`, tekan Enter
10. Verifikasi Activity Log memuat satu baris dengan Action `Create`, Object `Custom Fields`, Name `Log Create {runId}-124`, Field `Name`, Old Value `—`, New Value `Log Create {runId}-124`, Modified By `Sarah J`
11. Verifikasi hasil Search `Log Create {runId}-124` pada Activity Log hanya memuat satu baris (nama bersuffix unik, baseline nol; tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-481: Create tidak mencatat baris untuk konfigurasi awal selain Name

12. Klik `[+ Custom Field]`, isi Field Name `Log Config {runId}-124`, pilih Data Type `Numeric`, Decimal Places 2, Required Yes, dan Scope `Specific Asset Name` dengan `Pump`, lalu klik `[Submit]`
13. Tunggu aksi selesai (dialog tertutup atau field kembali kosong dan tabel dimuat ulang)
14. Buka Modal Changelog tab General, ketik Search `Log Config {runId}-124`, tekan Enter
15. Verifikasi Changelog memuat satu baris Action `Create` dengan Field `Name` untuk `Log Config {runId}-124`
16. Verifikasi hasil Search `Log Config {runId}-124` pada Changelog hanya memuat satu baris (nama bersuffix unik, baseline nol; tidak ada baris untuk Data Type, Decimal Places, Scope, Required, maupun Active)

### TC-FA-CF-492: Activate mencatat baris Active Inactive ke Active di tiga surface

17. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Depreciated Ratio` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
18. Geser switch Active baris `Depreciated Ratio` ke ON lalu klik `[Activate]` pada dialog
19. Tunggu aksi selesai (dialog tertutup atau field kembali kosong dan tabel dimuat ulang)
20. Buka Modal Changelog tab General, ketik Search `Depreciated Ratio`, tekan Enter
21. Verifikasi Changelog memuat satu baris baru dengan Action `Activate`, Field Name `Depreciated Ratio`, Field `Active`, Old Value `Inactive`, New Value `Active`, Modified By `Sarah J`
22. Verifikasi hasil Search `Depreciated Ratio` pada Changelog bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris baru untuk properti yang tidak berubah)
23. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Depreciated Ratio`, tekan Enter
24. Verifikasi System Log `Sarah Johnson` memuat satu baris baru dengan Action `Activate`, Object `Custom Fields`, Name `Depreciated Ratio`, Field `Active`, Old Value `Inactive`, New Value `Active`
25. Verifikasi hasil Search `Depreciated Ratio` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris baru untuk properti yang tidak berubah)
26. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Depreciated Ratio`, tekan Enter
27. Verifikasi Activity Log memuat satu baris baru dengan Action `Activate`, Object `Custom Fields`, Name `Depreciated Ratio`, Field `Active`, Old Value `Inactive`, New Value `Active`, Modified By `Sarah J`
28. Verifikasi hasil Search `Depreciated Ratio` pada Activity Log bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris baru untuk properti yang tidak berubah)

### TC-FA-CF-493: Deactivate mencatat baris Active Active ke Inactive di tiga surface

29. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Asset Serial Tag` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
30. Geser switch Active baris `Asset Serial Tag` ke OFF lalu klik `[Deactivate]` pada dialog
31. Tunggu aksi selesai (dialog tertutup atau field kembali kosong dan tabel dimuat ulang)
32. Buka Modal Changelog tab General, ketik Search `Asset Serial Tag`, tekan Enter
33. Verifikasi Changelog memuat satu baris baru dengan Action `Deactivate`, Field Name `Asset Serial Tag`, Field `Active`, Old Value `Active`, New Value `Inactive`, Modified By `Sarah J`
34. Verifikasi hasil Search `Asset Serial Tag` pada Changelog bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris baru untuk properti yang tidak berubah)
35. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Asset Serial Tag`, tekan Enter
36. Verifikasi System Log `Sarah Johnson` memuat satu baris baru dengan Action `Deactivate`, Object `Custom Fields`, Name `Asset Serial Tag`, Field `Active`, Old Value `Active`, New Value `Inactive`
37. Verifikasi hasil Search `Asset Serial Tag` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris baru untuk properti yang tidak berubah)
38. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Asset Serial Tag`, tekan Enter
39. Verifikasi Activity Log memuat satu baris baru dengan Action `Deactivate`, Object `Custom Fields`, Name `Asset Serial Tag`, Field `Active`, Old Value `Active`, New Value `Inactive`, Modified By `Sarah J`
40. Verifikasi hasil Search `Asset Serial Tag` pada Activity Log bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris baru untuk properti yang tidak berubah)

### TC-FA-CF-497: Bulk Activate mencatat satu baris per field yang berubah

41. Pulihkan status baseline lewat seed reset Company (`Depreciated Ratio` Inactive dan `Asset Serial Tag` Active) lalu muat ulang tabel
42. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Depreciated Ratio` lalu `Asset Serial Tag` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
43. Centang baris `Depreciated Ratio` (Inactive) dan `Asset Serial Tag` (Active)
44. Jalankan Bulk Activate lewat Bulk Action Bar
45. Tunggu aksi selesai (dialog tertutup atau field kembali kosong dan tabel dimuat ulang)
46. Buka Modal Changelog tab General, ketik Search `Depreciated Ratio`, tekan Enter
47. Verifikasi hasil Search `Depreciated Ratio` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Activate` untuk `Depreciated Ratio`)
48. Ganti isi kotak search dengan `Asset Serial Tag`, tekan Enter
49. Verifikasi hasil Search `Asset Serial Tag` pada Changelog sama dengan baseline (tidak ada baris baru untuk `Asset Serial Tag` yang dilewati)
50. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Depreciated Ratio`, tekan Enter
51. Verifikasi hasil Search `Depreciated Ratio` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Activate` untuk `Depreciated Ratio`)
52. Ganti isi kotak search dengan `Asset Serial Tag`, tekan Enter
53. Verifikasi hasil Search `Asset Serial Tag` pada System Log `Sarah Johnson` sama dengan baseline (tidak ada baris baru untuk `Asset Serial Tag` yang dilewati)
54. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Depreciated Ratio`, tekan Enter
55. Verifikasi hasil Search `Depreciated Ratio` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Activate` untuk `Depreciated Ratio`)
56. Ganti isi kotak search dengan `Asset Serial Tag`, tekan Enter
57. Verifikasi hasil Search `Asset Serial Tag` pada Activity Log sama dengan baseline (tidak ada baris baru untuk `Asset Serial Tag` yang dilewati)

### TC-FA-CF-498: Bulk Deactivate mencatat satu baris per field yang berubah

58. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Depreciated Ratio` lalu `Asset Serial Tag` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
59. Centang baris `Depreciated Ratio` dan `Asset Serial Tag` (keduanya Active)
60. Jalankan Bulk Deactivate lewat Bulk Action Bar
61. Tunggu aksi selesai (dialog tertutup atau field kembali kosong dan tabel dimuat ulang)
62. Buka Modal Changelog tab General, ketik Search `Depreciated Ratio`, tekan Enter
63. Verifikasi hasil Search `Depreciated Ratio` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Deactivate` dengan Old Value `Active` dan New Value `Inactive`)
64. Ganti isi kotak search dengan `Asset Serial Tag`, tekan Enter
65. Verifikasi hasil Search `Asset Serial Tag` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Deactivate` dengan Old Value `Active` dan New Value `Inactive`)
66. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Depreciated Ratio`, tekan Enter
67. Verifikasi hasil Search `Depreciated Ratio` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Deactivate` dengan Old Value `Active` dan New Value `Inactive`)
68. Ganti isi kotak search dengan `Asset Serial Tag`, tekan Enter
69. Verifikasi hasil Search `Asset Serial Tag` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Deactivate` dengan Old Value `Active` dan New Value `Inactive`)
70. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Depreciated Ratio`, tekan Enter
71. Verifikasi hasil Search `Depreciated Ratio` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Deactivate` dengan Old Value `Active` dan New Value `Inactive`)
72. Ganti isi kotak search dengan `Asset Serial Tag`, tekan Enter
73. Verifikasi hasil Search `Asset Serial Tag` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Deactivate` dengan Old Value `Active` dan New Value `Inactive`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 73 langkah bernomor; langkah blok baca-log berpola (buka surface dengan Search nama field, `Verifikasi` baris log, `Verifikasi` selisih jumlah; 54 langkah, nomor 3 sampai 11, 14 sampai 16, 20 sampai 28, 32 sampai 40, 46 sampai 57, 62 sampai 73) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 19 langkah. Spec dipertahankan karena semua blok berada pada satu kelas harness (pencatatan log tiga surface) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok TC lain kehilangan makna.
- Urutan TC di spec: 480, 481, 492, 493, 497, 498 (urutan TC). Langkah 41 memulihkan status baseline karena TC-FA-CF-492 dan TC-FA-CF-493 mengubahnya dan TC-FA-CF-497 mensyaratkan `Depreciated Ratio` Inactive dan `Asset Serial Tag` Active.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 41 (pemulihan baseline), langkah "Tunggu aksi selesai" sebelum membuka surface log (8b butir 8), langkah baseline (S-12) di awal TC-FA-CF-492, 493, 497, dan 498, serta langkah buka surface log dengan Search nama field dan ganti isi kotak search (R-16).
- Satu `Verifikasi` per klausa dan per surface (S-01): isi kolom baris log dan selisih jumlah baris ditulis terpisah di tiap surface. Nama field Pre-setup (`Depreciated Ratio`, `Asset Serial Tag`) tidak unik pada audit trail permanen, sehingga "baris baru" dibuktikan dengan selisih jumlah baris hasil Search nama field terhadap baseline sebelum aksi (TC-FA-CF-492, 493, 497, 498; S-12), bukan dengan posisi atau jumlah absolut. Baseline dicatat dengan Search nama field yang sama sebelum aksi.
- TC-FA-CF-480 dan 481 memakai nama field bersuffix unik `{runId}-124` sehingga baseline nol dan tidak ada langkah pencatatan baseline; hasil Search nama itu diasersi "hanya memuat satu baris" (S-12, nama unik).
- Asersi "tidak ada baris" TC-FA-CF-481, 497 b, dan 498 ditulis sebagai selisih jumlah terhadap baseline pada hasil Search yang sama dengan baris positif yang diasersi lebih dulu di surface itu (anchor, 8b butir 2); ini bukan spec absence karena aksi TC nyata di spec ini.
- Seed pemulihan baseline (langkah 41) tidak menghapus audit trail permanen; baseline TC-FA-CF-497 dicatat sesudah pemulihan sehingga selisihnya hanya berasal dari aksi TC itu.
- Temuan untuk QA:
  - TC-FA-CF-497 dan TC-FA-CF-498 tidak menyebut label tombol konfirmasi Bulk Activate dan Bulk Deactivate; spec menulis "Jalankan Bulk Activate" dan "Jalankan Bulk Deactivate" lewat Bulk Action Bar persis seperti TC.
  - TC-FA-CF-498 "Centang dua field Active" tidak menyebut field mana; spec memakai `Depreciated Ratio` (Active sesudah TC-FA-CF-497) dan `Asset Serial Tag`.
  - TC-FA-CF-497 tidak menyebut Field, Old Value, dan New Value baris Activate; spec hanya mengasersi Action `Activate` melalui selisih jumlah baris.
  - Email akun Total Control Company Alpha mengikuti pola Pre-setup #1; env var `FA_TC_PASSWORD` disediakan tim FE.
