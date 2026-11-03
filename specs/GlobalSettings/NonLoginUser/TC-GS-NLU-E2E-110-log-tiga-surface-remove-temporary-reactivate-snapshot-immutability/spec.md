---
id: TC-GS-NLU-E2E-110-log-tiga-surface-remove-temporary-reactivate-snapshot-immutability
title: "Log tiga surface: Remove Temporary, Reactivate, snapshot immutability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-402
  - TC-GS-NLU-403
  - TC-GS-NLU-404
  - TC-GS-NLU-405
coverage:
  web: automated
---

# Log tiga surface: Remove Temporary, Reactivate, snapshot immutability

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - `Agus Salim {runId}-110` (TC-GS-NLU-402): First Name `Agus`, Last Name `Salim {runId}-110`, Division `Operations`, Email `agussalim+{runId}-110@qwertysystem.net`, Represented By `Ahmad Fauzi`, Inactive, Temporary-expired dengan Temporary Until 2 hari sebelum hari ini (nilai `[old date]` dalam Date Format `dd/MM/yy`).
  - `Reaktif Satu {runId}-110` (TC-GS-NLU-403): First Name `Reaktif`, Last Name `Satu {runId}-110`, Email `reaktifsatu+{runId}-110@qwertysystem.net`, data lain dan keadaan Temporary-expired sama seperti `Agus Salim {runId}-110`.
  - `Temp Edit {runId}-110` (TC-GS-NLU-404): First Name `Temp`, Last Name `Edit {runId}-110`, Email `tempedit+{runId}-110@qwertysystem.net`, Active, Temporary dengan Temporary Until hari ini ditambah 30 hari.
- Data yang dibuat TC-GS-NLU-405 lewat UI (supaya entri `Create` tercatat): First Name `Snapshot Satu`, Last Name `{runId}-110`, Division `Operations`, Email `snapshotsatu+{runId}-110@qwertysystem.net`, Represented By `Ahmad Fauzi`.
- General Settings: Date Format `dd/MM/yy` (Tabel Data Uji Pre-setup No. 16).
- Baseline log: jumlah entri Activity Log dan System Log aktor dibaca per Action pada langkah awal; kemampuan membaca jumlah entri disediakan tim FE/BE.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-110` yang tersisa.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

1. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor Siti Nurhaliza untuk object Non-Login User per Action `Remove Temporary User`, `Set Temporary User`, `Activate` sebagai baseline Activity Log
2. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User) dan catat jumlah entri per Action `Remove Temporary User`, `Set Temporary User`, `Activate` sebagai baseline System Log aktor

### TC-GS-NLU-402: Log Remove Temporary User saat Reactivate Make Permanent

3. Ketik Search `Agus Salim {runId}-110`, tekan Enter, klik switch Active baris `Agus Salim {runId}-110` (OFF, Temporary-expired)
4. Pilih opsi `Make permanent`
5. Klik `[Reactivate]`
6. Tunggu aksi selesai (dialog Reactivate Temporary User menutup)
7. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
8. Verifikasi Modal Changelog agregat: entri `Remove Temporary User` Field `Temporary Until`, Old Value Temporary Until awal (2 hari sebelum hari ini), New Value `—`
9. Verifikasi Modal Changelog agregat: entri `Activate` Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, dicatat sesudah entri `Remove Temporary User`
10. Tutup Modal Changelog dengan `✕`
11. Ketik Search `Agus Salim {runId}-110`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
12. Verifikasi Tab Changelog Detail: entri `Remove Temporary User` Field `Temporary Until`, Old Value Temporary Until awal (2 hari sebelum hari ini), New Value `—`
13. Verifikasi Tab Changelog Detail: entri `Activate` Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, dicatat sesudah entri `Remove Temporary User`
14. Buka Global Settings > Activity Log lewat sidebar
15. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Remove Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
16. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
17. Verifikasi Activity Log: entri baru memuat Action `Remove Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza serta entri baru Action `Activate` untuk object dan aktor yang sama
18. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
19. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Remove Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
20. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
21. Verifikasi System Log aktor: entri baru memuat Action `Remove Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza serta entri baru Action `Activate` untuk object dan aktor yang sama
22. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-403: Log Set Temporary User saat Reactivate Extend Period

23. Ketik Search `Reaktif Satu {runId}-110`, tekan Enter, klik switch Active baris `Reaktif Satu {runId}-110` (OFF, Temporary-expired)
24. Pilih opsi `Extend period`, pilih tanggal besok
25. Klik `[Reactivate]`
26. Tunggu aksi selesai (dialog Reactivate Temporary User menutup)
27. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
28. Verifikasi Modal Changelog agregat: entri `Set Temporary User` Field `Temporary Until`, Old Value Temporary Until awal (2 hari sebelum hari ini), New Value tanggal besok dalam Date Format `dd/MM/yy`
29. Verifikasi Modal Changelog agregat: entri `Activate` Field `Status`, dicatat sesudah entri `Set Temporary User`
30. Tutup Modal Changelog dengan `✕`
31. Ketik Search `Reaktif Satu {runId}-110`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
32. Verifikasi Tab Changelog Detail: entri `Set Temporary User` Field `Temporary Until`, Old Value Temporary Until awal (2 hari sebelum hari ini), New Value tanggal besok dalam Date Format `dd/MM/yy`
33. Verifikasi Tab Changelog Detail: entri `Activate` Field `Status`, dicatat sesudah entri `Set Temporary User`
34. Buka Global Settings > Activity Log lewat sidebar
35. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Set Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
36. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
37. Verifikasi Activity Log: entri baru memuat Action `Set Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza serta entri baru Action `Activate` untuk object dan aktor yang sama
38. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
39. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Set Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
40. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
41. Verifikasi System Log aktor: entri baru memuat Action `Set Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza serta entri baru Action `Activate` untuk object dan aktor yang sama
42. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-404: Log menghapus centang Temporary User lewat Edit

43. Ketik Search `Temp Edit {runId}-110`, tekan Enter, klik `⋯` baris `Temp Edit {runId}-110` > `Edit`
44. Hapus centang `Set as Temporary User`
45. Klik `[Save]`
46. Tunggu aksi selesai (popup Edit menutup)
47. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
48. Verifikasi Modal Changelog agregat: satu entri `Remove Temporary User` Field `Temporary Until`, Old Value Temporary Until awal (hari ini ditambah 30 hari), New Value `—`
49. Tutup Modal Changelog dengan `✕`
50. Ketik Search `Temp Edit {runId}-110`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
51. Verifikasi Tab Changelog Detail: satu entri `Remove Temporary User` Field `Temporary Until`, Old Value Temporary Until awal (hari ini ditambah 30 hari), New Value `—`
52. Buka Global Settings > Activity Log lewat sidebar
53. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Remove Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
54. Verifikasi Activity Log: entri baru memuat Action `Remove Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza
55. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
56. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Remove Temporary User` bertambah satu dibanding baseline (jumlah baru menjadi baseline berikutnya)
57. Verifikasi System Log aktor: entri baru memuat Action `Remove Temporary User`, object Non-Login User, dan aktor Siti Nurhaliza
58. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar

### TC-GS-NLU-405: Entri log tidak ditulis ulang saat nama berubah dua kali (snapshot immutability)

59. Klik `[+ Non-Login User]`
60. Isi First Name `Snapshot Satu`, Last Name `{runId}-110`, Division `Operations`, Email `snapshotsatu+{runId}-110@qwertysystem.net`
61. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
62. Biarkan checkbox `Stay on this form after submitting` tidak tercentang, klik `[Submit]`
63. Tunggu aksi selesai (popup Create menutup)
64. Ketik Search `Snapshot Satu {runId}-110`, tekan Enter, klik `⋯` baris `Snapshot Satu {runId}-110` > `Edit`
65. Ubah First Name `Snapshot Satu` menjadi `Snapshot Dua`, klik `[Save]`
66. Tunggu aksi selesai (popup Edit menutup)
67. Ketik Search `Snapshot Dua {runId}-110`, tekan Enter, klik `⋯` baris `Snapshot Dua {runId}-110` > `Edit`
68. Ubah First Name menjadi `Snapshot Tiga`, klik `[Save]`
69. Tunggu aksi selesai (popup Edit menutup)
70. Ketik Search `Snapshot Tiga {runId}-110`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
71. Verifikasi Tab Changelog Detail: entri `Edit` pertama tetap `Snapshot Satu` menjadi `Snapshot Dua` (Field `First Name`, Old Value `Snapshot Satu`, New Value `Snapshot Dua`)
72. Verifikasi Tab Changelog Detail: entri `Edit` kedua tetap `Snapshot Dua` menjadi `Snapshot Tiga` (Field `First Name`, Old Value `Snapshot Dua`, New Value `Snapshot Tiga`)
73. Verifikasi Tab Changelog Detail: entri `Create` lama tetap menampilkan New Value `Snapshot Satu {runId}-110`, nama saat itu

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6, 26, 46, 63, 66, 69 (Tunggu aksi selesai), langkah 3, 23, 43 (Search record yang dicari, R-16), serta penutupan modal dan navigasi sidebar di blok baca-log.
- Baseline (S-12): jumlah entri Activity Log dan System Log aktor dibaca per Action dan per aktor sebelum aksi pertama, lalu tiap asersi memakai selisih terhadap baseline terakhir; Changelog memakai nama record bersuffix `{runId}` (baseline nol). Kemampuan membaca jumlah entri dua surface itu disediakan tim FE/BE.
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 73 langkah, dengan 50 langkah berupa blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 prinsip 13 (Smell), sehingga 23 langkah terhitung. Semua blok memeriksa tiga surface log yang sama untuk satu aksi dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Record TC-GS-NLU-405 dibuat lewat UI pada langkah 59 sampai 63 supaya entri `Create` yang diasersi pasti tercatat.
- Temuan untuk QA:
  - TC-GS-NLU-402 dan 403 menyebut dua entri ("lalu entri `Activate`") tanpa menyatakan urutan tampilnya di tabel; spec mengasersi keberadaan kedua entri dan mencatat urutan pencatatannya hanya sebagai keterangan, bukan posisi baris (S-14).
  - TC-GS-NLU-402 sampai 404 menyebut "satu entri dengan Action yang sama" di Activity Log dan System Log aktor tanpa nilai kolom; spec mengasersi Action, object, dan aktor, satu entri per Action.
  - TC-GS-NLU-405 hanya menyebut Tab Changelog Detail; Modal Changelog, Activity Log, dan System Log tidak diasersi karena TC tidak memintanya.
  - Surface Activity Log dan tab System Log Detail aktor tidak dirinci jalur navigasinya di TC (lihat spec 108); spec memakai baseline jumlah entri per Action dan aktor.
