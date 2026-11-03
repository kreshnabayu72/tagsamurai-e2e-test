---
id: TC-GS-NLU-E2E-108-log-tiga-surface-create-edit-per-field-represented-by
title: "Log tiga surface: Create, Edit per field, Represented By, Photo"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-394
  - TC-GS-NLU-395
  - TC-GS-NLU-396
  - TC-GS-NLU-397
coverage:
  web: automated
---

# Log tiga surface: Create, Edit per field, Represented By, Photo

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - `Log Enam {runId}-108` (TC-GS-NLU-395): First Name `Log`, Last Name `Enam {runId}-108`, Position `Driver`, Division `Operations`, Employee ID `LOG-108-{runId}-A`, Email `logenam+{runId}-108@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active.
  - `Log Rep {runId}-108` (TC-GS-NLU-396): First Name `Log`, Last Name `Rep {runId}-108`, Division `Operations`, Email `logrep+{runId}-108@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active.
  - `Log Foto {runId}-108` (TC-GS-NLU-397): First Name `Log`, Last Name `Foto {runId}-108`, Division `Operations`, Email `logfoto+{runId}-108@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active, dengan foto awal `fixtures/sampleImage.png`.
- Data yang dibuat TC-GS-NLU-394 lewat UI: First Name `Log Satu`, Last Name `{runId}-108`, Division `Logistics`, Email `logsatu+{runId}-108@qwertysystem.net`, Represented By `Ahmad Fauzi`.
- Nilai perubahan TC-GS-NLU-395: First Name `Logu`, Last Name `Enamu {runId}-108`, Position `Manager`, Division `Logistics`, Employee ID `LOG-108-{runId}-B`, Email `logenamu+{runId}-108@qwertysystem.net`. Foto pengganti TC-GS-NLU-397: berkas gambar uji lain yang berbeda dari foto awal (disediakan tim FE).
- Baseline log: jumlah entri Activity Log dan System Log aktor dibaca per Action `Create` dan `Edit` pada langkah awal; kemampuan membaca jumlah entri disediakan tim FE/BE.
- Kemampuan teknis: unggah berkas pada avatar, membaca jumlah entri Activity Log dan System Log aktor.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-108` yang tersisa (termasuk `Log Satu`).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` (dirujuk sebagai `Fixture.nonLoginUser.<key>`) untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

1. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor Siti Nurhaliza untuk object Non-Login User per Action `Create`, `Edit` sebagai baseline Activity Log
2. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User) dan catat jumlah entri per Action `Create`, `Edit` sebagai baseline System Log aktor

### TC-GS-NLU-394: Log Create, Name tercatat di tiga surface

3. Klik `[+ Non-Login User]`
4. Isi First Name `Log Satu`, Last Name `{runId}-108`, Division `Logistics`, Email `logsatu+{runId}-108@qwertysystem.net`
5. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
6. Biarkan checkbox `Stay on this form after submitting` tidak tercentang, klik `[Submit]`
7. Tunggu aksi selesai (popup Create menutup)
8. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
9. Verifikasi Modal Changelog agregat: entri `Create` untuk `Log Satu {runId}-108` berada di baris teratas
10. Verifikasi Modal Changelog agregat: entri `Create` Field `Name`, Old Value `—`, New Value `Log Satu {runId}-108`, Modified By `Siti N`
11. Tutup Modal Changelog dengan `✕`
12. Ketik Search `Log Satu {runId}-108`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
13. Verifikasi Tab Changelog Detail: entri `Create` untuk `Log Satu {runId}-108` berada di baris teratas
14. Verifikasi Tab Changelog Detail: entri `Create` Field `Name`, Old Value `—`, New Value `Log Satu {runId}-108`, Modified By `Siti N`
15. Buka Global Settings > Activity Log lewat sidebar
16. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Create` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
17. Verifikasi Activity Log: entri baru memuat Action `Create`, object Non-Login User, dan aktor Siti Nurhaliza
18. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
19. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Create` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
20. Verifikasi System Log aktor: entri baru memuat Action `Create`, object Non-Login User, dan aktor Siti Nurhaliza
21. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-395: Log Edit, satu entri per field yang berubah

22. Ketik Search `Enam {runId}-108`, tekan Enter, klik `⋯` baris `Log Enam {runId}-108` > `Edit`
23. Ubah First Name menjadi `Logu`, Last Name menjadi `Enamu {runId}-108`, Position menjadi `Manager`, Division menjadi `Logistics`, Employee ID menjadi `LOG-108-{runId}-B`, Email menjadi `logenamu+{runId}-108@qwertysystem.net`
24. Klik `[Save]`
25. Tunggu aksi selesai (popup Edit menutup)
26. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
27. Verifikasi Modal Changelog agregat: entri `Edit` Field `First Name`, Old Value `Log`, New Value `Logu`
28. Verifikasi Modal Changelog agregat: entri `Edit` Field `Last Name`, Old Value `Enam {runId}-108`, New Value `Enamu {runId}-108`
29. Verifikasi Modal Changelog agregat: entri `Edit` Field `Position`, Old Value `Driver`, New Value `Manager`
30. Verifikasi Modal Changelog agregat: entri `Edit` Field `Division`, Old Value `Operations`, New Value `Logistics`
31. Verifikasi Modal Changelog agregat: entri `Edit` Field `Employee ID`, Old Value `LOG-108-{runId}-A`, New Value `LOG-108-{runId}-B`
32. Verifikasi Modal Changelog agregat: entri `Edit` Field `Email`, Old Value `logenam+{runId}-108@qwertysystem.net`, New Value `logenamu+{runId}-108@qwertysystem.net`
33. Verifikasi Modal Changelog agregat: tepat enam entri `Edit` baru untuk `Log Enam {runId}-108`, tanpa entri ganda dan tanpa entri untuk field yang tidak berubah
34. Tutup Modal Changelog dengan `✕`
35. Ketik Search `Enamu {runId}-108`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
36. Verifikasi Tab Changelog Detail: entri `Edit` Field `First Name`, Old Value `Log`, New Value `Logu`
37. Verifikasi Tab Changelog Detail: entri `Edit` Field `Last Name`, Old Value `Enam {runId}-108`, New Value `Enamu {runId}-108`
38. Verifikasi Tab Changelog Detail: entri `Edit` Field `Position`, Old Value `Driver`, New Value `Manager`
39. Verifikasi Tab Changelog Detail: entri `Edit` Field `Division`, Old Value `Operations`, New Value `Logistics`
40. Verifikasi Tab Changelog Detail: entri `Edit` Field `Employee ID`, Old Value `LOG-108-{runId}-A`, New Value `LOG-108-{runId}-B`
41. Verifikasi Tab Changelog Detail: entri `Edit` Field `Email`, Old Value `logenam+{runId}-108@qwertysystem.net`, New Value `logenamu+{runId}-108@qwertysystem.net`
42. Verifikasi Tab Changelog Detail: tepat enam entri `Edit`, tanpa entri ganda dan tanpa entri untuk field yang tidak berubah
43. Buka Global Settings > Activity Log lewat sidebar
44. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah enam dibanding baseline (jumlah baru menjadi baseline berikutnya)
45. Verifikasi Activity Log: enam entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza, satu per Field dengan Old Value dan New Value yang sama seperti di Changelog
46. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
47. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah enam dibanding baseline (jumlah baru menjadi baseline berikutnya)
48. Verifikasi System Log aktor: enam entri baru memuat Action `Edit` dan object Non-Login User, satu per Field dengan Old Value dan New Value yang sama seperti di Changelog
49. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar
50. Ketik Search `Rep {runId}-108`, tekan Enter, klik Name baris `Log Rep {runId}-108` untuk membuka Detail, lalu klik tab `Changelog`
51. Verifikasi kolom header tabel Tab Changelog Detail `Log Rep {runId}-108` tampil
52. Verifikasi Tab Changelog Detail `Log Rep {runId}-108` tidak memuat entri `Edit` (entri milik record lain tidak ikut tercatat)
53. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-396: Log Edit Represented By, nama Login User lama dan baru

54. Ketik Search `Rep {runId}-108`, tekan Enter, klik `⋯` baris `Log Rep {runId}-108` > `Edit`
55. Ganti Represented By dari `Ahmad Fauzi` ke `Dewi Anggraini` lewat popup Select User
56. Klik `[Save]`
57. Tunggu aksi selesai (popup Edit menutup)
58. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
59. Verifikasi Modal Changelog agregat: entri `Edit` Field `Represented By`, Old Value `Ahmad Fauzi`, New Value `Dewi Anggraini`
60. Tutup Modal Changelog dengan `✕`
61. Ketik Search `Rep {runId}-108`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
62. Verifikasi Tab Changelog Detail: entri `Edit` Field `Represented By`, Old Value `Ahmad Fauzi`, New Value `Dewi Anggraini`
63. Buka Global Settings > Activity Log lewat sidebar
64. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
65. Verifikasi Activity Log: entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza
66. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
67. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
68. Verifikasi System Log aktor: entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza
69. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-397: Log Edit Photo tercatat tanpa nilai teks

70. Ketik Search `Foto {runId}-108`, tekan Enter, klik `⋯` baris `Log Foto {runId}-108` > `Edit`
71. Ganti foto dengan berkas gambar uji lain pada avatar
72. Klik `[Save]`
73. Tunggu aksi selesai (popup Edit menutup)
74. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
75. Verifikasi Modal Changelog agregat: entri `Edit` Field `Photo`, Old Value `—`, New Value `—`
76. Tutup Modal Changelog dengan `✕`
77. Ketik Search `Foto {runId}-108`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
78. Verifikasi Tab Changelog Detail: entri `Edit` Field `Photo`, Old Value `—`, New Value `—`
79. Buka Global Settings > Activity Log lewat sidebar
80. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
81. Verifikasi Activity Log: entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza
82. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
83. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
84. Verifikasi System Log aktor: entri baru memuat Action `Edit`, object Non-Login User, dan aktor Siti Nurhaliza
85. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7, 25, 57, 73 (Tunggu aksi selesai), langkah 22, 54, 70 (Search record yang dicari sebelum membuka menu `⋯`, R-16), serta penutupan modal dan navigasi sidebar di blok baca-log.
- Baseline (S-12): jumlah entri Activity Log dan System Log aktor dibaca per Action dan per aktor pada dua langkah awal, lalu tiap asersi memakai selisih terhadap baseline terakhir; Changelog memakai nama record bersuffix `{runId}-108` (baseline nol).
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 85 langkah, dengan 68 langkah berupa blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 prinsip 13 (Smell), sehingga 17 langkah terhitung. Semua blok memeriksa tiga surface log yang sama untuk satu aksi dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-GS-NLU-395 Expected d (entri milik record lain tidak ikut tercatat) diasersi pada Tab Changelog Detail `Log Rep {runId}-108`, record lain yang tidak diubah pada saat itu.
- Modified By hanya diasersi pada TC-GS-NLU-394 (satu-satunya yang menyebutnya); TC-GS-NLU-395 sampai 397 tidak menyebutnya sehingga asersi itu tidak ditulis (S-03).
- Temuan untuk QA:
  - TC-GS-NLU-394 sampai 397 menyebut surface Activity Log dan tab System Log Detail aktor tanpa menyebut jalur navigasi, filter, atau cara membaca entri; spec memakai baseline jumlah entri per Action dan aktor (kemampuan disediakan tim FE/BE) dan jalur Global Settings > Activity Log serta tab `System Log` pada Detail aktor.
  - Expected b dan c TC-GS-NLU-394, 396, dan 397 hanya menyebut "satu entri dengan Action yang sama" tanpa nilai kolom; spec mengasersi Action, object Non-Login User, dan aktor.
  - TC-GS-NLU-397 tidak menyebut berkas foto pengganti; spec memakai berkas gambar uji lain (disediakan tim FE).
  - Kolom Date entri log tidak diasersi karena TC tidak memintanya.
