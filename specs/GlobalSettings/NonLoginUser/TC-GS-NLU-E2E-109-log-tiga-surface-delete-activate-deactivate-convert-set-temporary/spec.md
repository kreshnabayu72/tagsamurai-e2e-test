---
id: TC-GS-NLU-E2E-109-log-tiga-surface-delete-activate-deactivate-convert-set-temporary
title: "Log tiga surface: Delete, Activate Deactivate, Convert, Set Temporary"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-398
  - TC-GS-NLU-399
  - TC-GS-NLU-400
  - TC-GS-NLU-401
coverage:
  web: automated
---

# Log tiga surface: Delete, Activate Deactivate, Convert, Set Temporary

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - `Log Dua {runId}-109` (TC-GS-NLU-398): First Name `Log`, Last Name `Dua {runId}-109`, Division `Operations`, Email `logdua+{runId}-109@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active.
  - `Log Tiga {runId}-109` (TC-GS-NLU-399): sama, Last Name `Tiga {runId}-109`, Email `logtiga+{runId}-109@qwertysystem.net`, Active.
  - `Log Empat {runId}-109` (TC-GS-NLU-400): sama, Last Name `Empat {runId}-109`, Email `logempat+{runId}-109@qwertysystem.net`, Active.
- Data yang dibuat TC-GS-NLU-401 lewat UI: First Name `Log Lima`, Last Name `{runId}-109`, Division `Logistics`, Email `loglima+{runId}-109@qwertysystem.net`, Represented By `Ahmad Fauzi`, Set as Temporary User dengan Temporary Until hari ini ditambah 10 hari.
- General Settings: Date Format `dd/MM/yy` (Tabel Data Uji Pre-setup No. 16); nilai `[tanggal +10 hari]` diasersi dalam format itu.
- Baseline log: jumlah entri Activity Log dan System Log aktor dibaca per Action pada langkah awal; kemampuan membaca jumlah entri disediakan tim FE/BE.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-109` yang tersisa (termasuk `Log Lima`) dan Login User hasil Convert `Log Empat`.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

1. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor Siti Nurhaliza untuk object Non-Login User per Action `Delete`, `Deactivate`, `Activate`, `Convert to Login User`, `Create`, `Set Temporary User` sebagai baseline Activity Log
2. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User) dan catat jumlah entri per Action `Delete`, `Deactivate`, `Activate`, `Convert to Login User`, `Create`, `Set Temporary User` sebagai baseline System Log aktor

### TC-GS-NLU-398: Log Delete, Name lama tercatat

3. Ketik Search `Dua {runId}-109`, tekan Enter, klik `⋯` baris `Log Dua {runId}-109` > `Delete`
4. Klik `[Delete]` pada dialog konfirmasi
5. Tunggu aksi selesai (dialog Delete menutup)
6. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
7. Verifikasi Modal Changelog agregat: entri `Delete` Field `Name`, Old Value `Log Dua {runId}-109`, New Value `—`, Modified By `Siti N`
8. Tutup Modal Changelog dengan `✕`
9. Buka Global Settings > Activity Log lewat sidebar
10. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Delete` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
11. Verifikasi Activity Log: entri baru memuat Action `Delete`, object Non-Login User, dan aktor Siti Nurhaliza
12. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
13. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Delete` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
14. Verifikasi System Log aktor: entri baru memuat Action `Delete`, object Non-Login User, dan aktor Siti Nurhaliza
15. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-399: Log Deactivate dan Activate, Status Active dan Inactive

16. Ketik Search `Tiga {runId}-109`, tekan Enter, klik switch Active baris `Log Tiga {runId}-109` (ON)
17. Klik `[Deactivate]` pada dialog konfirmasi
18. Klik switch Active baris `Log Tiga {runId}-109` (OFF)
19. Klik `[Activate]` pada dialog konfirmasi
20. Tunggu aksi selesai (dialog Activate menutup)
21. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
22. Verifikasi Modal Changelog agregat: entri `Deactivate` Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
23. Verifikasi Modal Changelog agregat: entri `Activate` Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
24. Tutup Modal Changelog dengan `✕`
25. Ketik Search `Log Tiga {runId}-109`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
26. Verifikasi Tab Changelog Detail: entri `Deactivate` Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
27. Verifikasi Tab Changelog Detail: entri `Activate` Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
28. Buka Global Settings > Activity Log lewat sidebar
29. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Deactivate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
30. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
31. Verifikasi Activity Log: entri baru memuat Action `Deactivate`, object Non-Login User, dan aktor Siti Nurhaliza serta entri baru Action `Activate` untuk object dan aktor yang sama
32. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
33. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Deactivate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
34. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
35. Verifikasi System Log aktor: entri baru memuat Action `Deactivate`, object Non-Login User, dan aktor Siti Nurhaliza serta entri baru Action `Activate` untuk object dan aktor yang sama
36. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-400: Log Convert to Login User, User Type berubah

37. Ketik Search `Empat {runId}-109`, tekan Enter, klik `⋯` baris `Log Empat {runId}-109` > `Convert to Login User`
38. Klik `[Convert]` pada dialog konfirmasi
39. Tunggu aksi selesai (dialog Convert menutup)
40. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
41. Verifikasi Modal Changelog agregat: entri `Convert to Login User` Field `User Type`, Old Value `Non Login`, New Value `Login (Pending Activation)`, Modified By `Siti N`
42. Verifikasi Modal Changelog agregat: hanya satu entri `Convert to Login User` untuk `Log Empat {runId}-109` (Field `User Type`)
43. Tutup Modal Changelog dengan `✕`
44. Buka sub-tab Login User, ketik Search `Empat {runId}-109`, tekan Enter, klik Name baris `Log Empat {runId}-109` untuk membuka Detail, lalu klik tab `Changelog`
45. Verifikasi Tab Changelog Detail: entri `Convert to Login User` Field `User Type`, Old Value `Non Login`, New Value `Login (Pending Activation)`, Modified By `Siti N`
46. Verifikasi Tab Changelog Detail: hanya satu entri `Convert to Login User` (Field `User Type`)
47. Buka Global Settings > Activity Log lewat sidebar
48. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Convert to Login User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
49. Verifikasi Activity Log: entri baru memuat Action `Convert to Login User`, object Non-Login User, dan aktor Siti Nurhaliza
50. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
51. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Convert to Login User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
52. Verifikasi System Log aktor: entri baru memuat Action `Convert to Login User`, object Non-Login User, dan aktor Siti Nurhaliza
53. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-401: Log Set Temporary User saat Create dengan Temporary Until

54. Klik `[+ Non-Login User]`
55. Isi First Name `Log Lima`, Last Name `{runId}-109`, Division `Logistics`, Email `loglima+{runId}-109@qwertysystem.net`
56. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
57. Centang `Set as Temporary User`, lalu pilih Temporary Until hari ini ditambah 10 hari
58. Biarkan checkbox `Stay on this form after submitting` tidak tercentang, klik `[Submit]`
59. Tunggu aksi selesai (popup Create menutup)
60. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
61. Verifikasi Modal Changelog agregat: entri `Create` Field `Name` untuk `Log Lima {runId}-109`
62. Verifikasi Modal Changelog agregat: entri `Set Temporary User` Field `Temporary Until`, Old Value `—`, New Value hari ini ditambah 10 hari dalam Date Format `dd/MM/yy`
63. Tutup Modal Changelog dengan `✕`
64. Ketik Search `Log Lima {runId}-109`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
65. Verifikasi Tab Changelog Detail: entri `Create` Field `Name` untuk `Log Lima {runId}-109`
66. Verifikasi Tab Changelog Detail: entri `Set Temporary User` Field `Temporary Until`, Old Value `—`, New Value hari ini ditambah 10 hari dalam Date Format `dd/MM/yy`
67. Buka Global Settings > Activity Log lewat sidebar
68. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Create` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
69. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Set Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
70. Verifikasi Activity Log: entri baru memuat Action `Set Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza
71. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
72. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Create` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
73. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Set Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
74. Verifikasi System Log aktor: entri baru memuat Action `Set Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza
75. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5, 20, 39, 59 (Tunggu aksi selesai), langkah 3, 16, 37 (Search record yang dicari, R-16), serta penutupan modal dan navigasi sidebar di blok baca-log.
- Baseline (S-12): jumlah entri Activity Log dan System Log aktor dibaca per Action dan per aktor sebelum aksi pertama, lalu tiap asersi memakai selisih terhadap baseline terakhir; Changelog memakai nama record bersuffix `{runId}` (baseline nol). Kemampuan membaca jumlah entri dua surface itu disediakan tim FE/BE.
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 75 langkah, dengan 58 langkah berupa blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 prinsip 13 (Smell), sehingga 17 langkah terhitung. Semua blok memeriksa tiga surface log yang sama untuk satu aksi dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-NLU-398 menyebut Tab Changelog Detail untuk record yang sudah dihapus; Detail record terhapus tidak dapat dibuka (TC-GS-NLU-452), sehingga spec mengasersi Modal Changelog agregat saja untuk TC itu.
  - TC-GS-NLU-399 dan 401 menyebut "satu entri dengan Action yang sama" di Activity Log dan System Log aktor padahal Changelog memuat dua Action (Deactivate dan Activate; Create dan Set Temporary User); spec mengasersi satu entri per Action.
  - Surface Activity Log dan tab System Log Detail aktor tidak dirinci jalur navigasinya di TC (lihat spec 108); spec memakai baseline jumlah entri per Action dan aktor.
  - TC-GS-NLU-400 menyebut Tab Changelog Detail untuk record yang sudah menjadi Login User; spec membukanya dari Detail Login User di sub-tab Login User (satu thread, TC-GS-NLU-427).
