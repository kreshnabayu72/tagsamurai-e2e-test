---
id: TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required
title: "Log Tiga Surface: Edit Properti Value Type, Global Value, Formula, Placeholder, dan Required"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-487
  - TC-FA-CF-488
  - TC-FA-CF-489
  - TC-FA-CF-490
  - TC-FA-CF-491
coverage:
  web: automated
---

# Log Tiga Surface: Edit Properti Value Type, Global Value, Formula, Placeholder, dan Required

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12, Max custom fields per asset name 20) dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diedit: `Storage Capacity`, `Maintenance Note` (Text, General, bernilai `Checked` pada A1), `Total Cost` (Formula `Purchase Price + 10`), `Voltage Spec` (Text, Scope Generator dan Pump, Global `220V` dan `110V`), dan `Empty Metric` (Numeric, Decimal Places 2, tanpa nilai).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri dan jumlah baris hasil Search nama field tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline sebelum aksi (S-12). Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-491: Edit properti Required mencatat satu baris di tiga surface

1. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Ubah toggle Required ke Yes
4. Klik `[Save]`
5. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
6. Buka Modal Changelog tab General dan temukan baris `Storage Capacity`
7. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Storage Capacity`, Field `Required`, Old Value `No`, New Value `Yes`, Modified By `Sarah J`
8. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
9. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Storage Capacity`
10. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Storage Capacity`, Field `Required`, Old Value `No`, New Value `Yes`
11. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
12. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Storage Capacity`
13. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Storage Capacity`, Field `Required`, Old Value `No`, New Value `Yes`, Modified By `Sarah J`
14. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-490: Edit properti Placeholder mencatat satu baris di tiga surface

15. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
16. Klik row action `⋯` > `Edit` pada baris `Maintenance Note`
17. Isi Placeholder `Write a note`
18. Klik `[Save]`
19. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
20. Buka Modal Changelog tab General dan temukan baris `Maintenance Note`
21. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Maintenance Note`, Field `Placeholder`, Old Value `—`, New Value `Write a note`, Modified By `Sarah J`
22. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
23. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Maintenance Note`
24. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Maintenance Note`, Field `Placeholder`, Old Value `—`, New Value `Write a note`
25. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
26. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Maintenance Note`
27. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Maintenance Note`, Field `Placeholder`, Old Value `—`, New Value `Write a note`, Modified By `Sarah J`
28. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-489: Edit properti Formula mencatat satu baris di tiga surface

29. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
30. Klik row action `⋯` > `Edit` pada baris `Total Cost`
31. Ubah token Formula menjadi `Purchase Price × 2`
32. Klik `[Save]`
33. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
34. Buka Modal Changelog tab General dan temukan baris `Total Cost`
35. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Total Cost`, Field `Formula`, Old Value `[Purchase Price] + 10`, New Value `[Purchase Price] × 2`, Modified By `Sarah J`
36. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
37. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Total Cost`
38. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Total Cost`, Field `Formula`, Old Value `[Purchase Price] + 10`, New Value `[Purchase Price] × 2`
39. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
40. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Total Cost`
41. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Total Cost`, Field `Formula`, Old Value `[Purchase Price] + 10`, New Value `[Purchase Price] × 2`, Modified By `Sarah J`
42. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-488: Edit properti Global Value mencatat satu baris di tiga surface

43. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
44. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
45. Ubah Value `Generator` menjadi `230V`
46. Klik `[Save]`
47. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
48. Buka Modal Changelog tab General dan temukan baris `Voltage Spec`
49. Verifikasi Changelog memuat satu baris dengan Action `Edit`, Field Name `Voltage Spec`, Field `Global Value`, Old Value `Generator: 220V; Pump: 110V`, New Value `Generator: 230V; Pump: 110V`, Modified By `Sarah J`
50. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
51. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Voltage Spec`
52. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Voltage Spec`, Field `Global Value`, Old Value `Generator: 220V; Pump: 110V`, New Value `Generator: 230V; Pump: 110V`
53. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
54. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Voltage Spec`
55. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Voltage Spec`, Field `Global Value`, Old Value `Generator: 220V; Pump: 110V`, New Value `Generator: 230V; Pump: 110V`, Modified By `Sarah J`
56. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-487: Edit properti Value Type mencatat satu baris di tiga surface

57. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Empty Metric` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
58. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
59. Pilih Value Type `Global` dan isi Value `7`
60. Klik `[Save]`
61. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
62. Buka Modal Changelog tab General, ketik Search `Empty Metric`, tekan Enter
63. Verifikasi Changelog memuat satu baris baru dengan Action `Edit`, Field Name `Empty Metric`, Field `Value Type`, Old Value `Specific`, New Value `Global`, Modified By `Sarah J`
64. Verifikasi Changelog memuat satu baris baru dengan Action `Edit`, Field `Global Value`, New Value `7`
65. Verifikasi hasil Search `Empty Metric` pada Changelog bertambah tepat dua baris dibanding baseline (baris Value Type dan baris Global Value; tidak ada baris ganda dan tidak ada baris baru untuk properti lain yang tidak berubah: Data Type, Decimal Places, Scope, Required, dan Placeholder)
66. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Empty Metric`, tekan Enter
67. Verifikasi System Log `Sarah Johnson` memuat satu baris baru dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Value Type`, Old Value `Specific`, New Value `Global`
68. Verifikasi System Log `Sarah Johnson` memuat satu baris baru dengan Action `Edit`, Field `Global Value`, New Value `7`
69. Verifikasi hasil Search `Empty Metric` pada System Log `Sarah Johnson` bertambah tepat dua baris dibanding baseline (baris Value Type dan baris Global Value; tidak ada baris ganda dan tidak ada baris baru untuk properti lain yang tidak berubah: Data Type, Decimal Places, Scope, Required, dan Placeholder)
70. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Empty Metric`, tekan Enter
71. Verifikasi Activity Log memuat satu baris baru dengan Action `Edit`, Object `Custom Fields`, Name `Empty Metric`, Field `Value Type`, Old Value `Specific`, New Value `Global`, Modified By `Sarah J`
72. Verifikasi Activity Log memuat satu baris baru dengan Action `Edit`, Field `Global Value`, New Value `7`
73. Verifikasi hasil Search `Empty Metric` pada Activity Log bertambah tepat dua baris dibanding baseline (baris Value Type dan baris Global Value; tidak ada baris ganda dan tidak ada baris baru untuk properti lain yang tidak berubah: Data Type, Decimal Places, Scope, Required, dan Placeholder)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 73 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log dan selisih jumlah per surface; 48 langkah, nomor 6 sampai 14, 20 sampai 28, 34 sampai 42, 48 sampai 56, 62 sampai 73) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 25 langkah. Spec dipertahankan karena semua blok berada pada satu kelas harness (pencatatan log tiga surface) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok TC lain kehilangan makna.
- Urutan TC di spec: 491, 490, 489, 488, 487; tiap TC mengedit field berbeda sehingga tidak ada ketergantungan state, dan Value Type (TC-FA-CF-487) yang mengubah Global Value `Empty Metric` ditaruh di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline di awal tiap TC, langkah buka serta temukan baris di tiap surface (R-16); selisih jumlah entri diverifikasi per surface sesudah baris log surface itu, terhadap baseline yang dicatat pada langkah awal TC, dan "Tunggu aksi selesai" sebelum surface log dibuka pada tiap TC (langkah 5, 19, 33, 47, dan 61; 8b butir 8; asersi tambahan di luar Expected TC, S-03).
- TC-FA-CF-487 d dan e (langkah 62 sampai 73): baris Value Type dan baris Global Value (New Value `7`) diasersi pada tiap surface; "tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah" ditulis sebagai selisih dua baris pada jumlah baris hasil Search `Empty Metric` terhadap baseline pada tiap surface, dengan kedua baris diasersi lebih dulu pada surface yang sama sebagai anchor (S-12, 8b butir 2); asersi tidak gabungan tiga surface tanpa navigasi.
- Temuan untuk QA:
  - TC-FA-CF-487 d tidak menyebut Old Value, Object, Name, dan Modified By baris `Global Value`; spec hanya mengasersi Action, Field, dan New Value `7` untuk baris itu.
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
