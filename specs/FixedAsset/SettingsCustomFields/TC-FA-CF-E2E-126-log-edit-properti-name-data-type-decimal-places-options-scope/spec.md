---
id: TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope
title: "Log Tiga Surface: Edit Properti Name, Data Type, Decimal Places, Dropdown Options, dan Scope"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-482
  - TC-FA-CF-483
  - TC-FA-CF-484
  - TC-FA-CF-485
  - TC-FA-CF-486
coverage:
  web: automated
---

# Log Tiga Surface: Edit Properti Name, Data Type, Decimal Places, Dropdown Options, dan Scope

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12, Max custom fields per asset name 20) dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diedit: `Storage Capacity` (Numeric, Scope Generator dan Pump), `Empty Metric` (Numeric, Decimal Places 2, tanpa nilai), dan `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`). Hasil rename `Storage Capacity Log {runId}-126` bersuffix.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset). Langkah 43 memulihkan `Empty Metric` ke baseline di antara TC.
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-486: Edit properti Scope mencatat satu baris di tiga surface

1. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Tambahkan chip `Compressor` pada Scope
4. Klik `[Save]`
5. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
6. Buka Modal Changelog tab General dan temukan baris `Storage Capacity`
7. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Storage Capacity`, Field `Scope`, Old Value `Generator, Pump`, New Value `Compressor, Generator, Pump`, Modified By `Sarah J`
8. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
9. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Storage Capacity`
10. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Storage Capacity`, Field `Scope`, Old Value `Generator, Pump`, New Value `Compressor, Generator, Pump`
11. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
12. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Storage Capacity`
13. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Storage Capacity`, Field `Scope`, Old Value `Generator, Pump`, New Value `Compressor, Generator, Pump`, Modified By `Sarah J`
14. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-482: Edit properti Name mencatat satu baris di tiga surface

15. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
16. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
17. Ubah Field Name menjadi `Storage Capacity Log {runId}-126`
18. Klik `[Save]`
19. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
20. Buka Modal Changelog tab General dan temukan baris `Storage Capacity Log {runId}-126`
21. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Storage Capacity Log {runId}-126`, Field `Name`, Old Value `Storage Capacity`, New Value `Storage Capacity Log {runId}-126`, Modified By `Sarah J`
22. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
23. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Storage Capacity Log {runId}-126`
24. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Storage Capacity Log {runId}-126`, Field `Name`, Old Value `Storage Capacity`, New Value `Storage Capacity Log {runId}-126`
25. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
26. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Storage Capacity Log {runId}-126`
27. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Storage Capacity Log {runId}-126`, Field `Name`, Old Value `Storage Capacity`, New Value `Storage Capacity Log {runId}-126`, Modified By `Sarah J`
28. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-484: Edit properti Decimal Places mencatat satu baris di tiga surface

29. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
30. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
31. Pilih Decimal Places `1 (.0)`
32. Klik `[Save]`
33. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
34. Buka Modal Changelog tab General dan temukan baris `Empty Metric`
35. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Empty Metric`, Field `Decimal Places`, Old Value `2`, New Value `1`, Modified By `Sarah J`
36. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
37. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Empty Metric`
38. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Decimal Places`, Old Value `2`, New Value `1`
39. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
40. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Empty Metric`
41. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Decimal Places`, Old Value `2`, New Value `1`, Modified By `Sarah J`
42. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-483: Edit properti Data Type mencatat baris Data Type dan Decimal Places yang ikut berubah

43. Pulihkan baseline Company lewat seed reset Company (`Empty Metric` kembali Numeric dengan Decimal Places 2) lalu muat ulang tabel
44. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
45. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
46. Ganti Data Type menjadi `Text`
47. Klik `[Save]` (field tanpa nilai aset, sehingga tanpa dialog)
48. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
49. Buka Modal Changelog tab General dan temukan baris `Empty Metric`
50. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Empty Metric`, Field `Data Type`, Old Value `Numeric`, New Value `Text`, Modified By `Sarah J`
51. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Empty Metric`, Field `Decimal Places`, Old Value `2`, New Value `—`, Modified By `Sarah J`
52. Verifikasi jumlah entri Changelog tab General bertambah tepat dua dibanding baseline (baris Data Type dan baris Decimal Places; tidak ada baris ganda dan tidak ada baris untuk properti lain yang tidak berubah)
53. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Empty Metric`
54. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Data Type`, Old Value `Numeric`, New Value `Text`
55. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Decimal Places`, Old Value `2`, New Value `—`
56. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat dua dibanding baseline (baris Data Type dan baris Decimal Places; tidak ada baris ganda dan tidak ada baris untuk properti lain yang tidak berubah)
57. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Empty Metric`
58. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Data Type`, Old Value `Numeric`, New Value `Text`, Modified By `Sarah J`
59. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Decimal Places`, Old Value `2`, New Value `—`, Modified By `Sarah J`
60. Verifikasi jumlah entri Activity Log bertambah tepat dua dibanding baseline (baris Data Type dan baris Decimal Places; tidak ada baris ganda dan tidak ada baris untuk properti lain yang tidak berubah)

### TC-FA-CF-485: Edit properti Dropdown Options mencatat satu baris di tiga surface

61. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
62. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
63. Tambahkan opsi `Platinum`
64. Klik `[Save]`
65. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
66. Buka Modal Changelog tab General dan temukan baris `Brand Tier`
67. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Brand Tier`, Field `Dropdown Options`, Old Value `Gold, Silver, Bronze`, New Value `Gold, Silver, Bronze, Platinum`, Modified By `Sarah J`
68. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
69. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Brand Tier`
70. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Brand Tier`, Field `Dropdown Options`, Old Value `Gold, Silver, Bronze`, New Value `Gold, Silver, Bronze, Platinum`
71. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
72. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Brand Tier`
73. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Brand Tier`, Field `Dropdown Options`, Old Value `Gold, Silver, Bronze`, New Value `Gold, Silver, Bronze, Platinum`, Modified By `Sarah J`
74. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 74 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log dan selisih jumlah per surface; 48 langkah, nomor 6 sampai 14, 20 sampai 28, 34 sampai 42, 49 sampai 60, 66 sampai 74) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 26 langkah. Spec dipertahankan karena semua blok berada pada satu kelas harness (pencatatan log tiga surface) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok TC lain kehilangan makna.
- Urutan TC di spec: 486, 482, 484, 483, 485 (bukan urutan nomor). TC-FA-CF-486 memerlukan nama `Storage Capacity` dan Scope `Generator, Pump` sehingga berjalan sebelum TC-FA-CF-482 (rename); TC-FA-CF-484 mengubah Decimal Places `Empty Metric` sehingga langkah 43 memulihkan Decimal Places 2 sebelum TC-FA-CF-483.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 43, langkah 5, 19, 33, 48, dan 65 ("Tunggu aksi selesai" sesudah `[Save]` sebelum Modal Changelog dibuka; S-03, 8b butir 8), baseline di awal tiap TC, dan langkah buka serta temukan baris di tiap surface (R-16).
- Nama hasil rename memakai suffix `{runId}-126` (S-12); Old Value tetap `Storage Capacity` karena nama seed.
- `Verifikasi` jumlah entri ditulis per surface, tepat sesudah `Verifikasi` baris surface itu, terhadap baseline yang dicatat pada langkah awal TC (klausa d TC); pada TC-FA-CF-483 selisihnya dua per surface (baris Data Type dan baris Decimal Places) sesuai klausa d dan e.
- Temuan untuk QA:
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
  - TC-FA-CF-483 klausa d (baris Decimal Places Old `2`, New `—`) dan klausa e (tidak ada baris ganda atau baris untuk properti lain) ditulis sebagai dua baris tepat per surface; TC tidak menyebut urutan kedua baris.
