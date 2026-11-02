---
id: TC-AC-CS-E2E-017-role-matrix-visibilitas-elemen-role-principal-dan-group-manager
title: "Role Matrix: Visibilitas Elemen Role Principal dan Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-74
  - TC-AC-CS-30
  - TC-AC-CS-75
  - TC-AC-CS-76
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Role Principal dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `readOnlySub_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`, Read Only, Principal PT ABC; Pre-setup #3), password `Spectra.env.AC_SUB_RO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`
  - `defaultUserSub_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, Principal PT ABC; Pre-setup #2), password `Spectra.env.AC_SUB_DU_PASSWORD`
  - `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Group Manager scope Group `Jawa`, Distributor PT Maju Bersama; Pre-setup #5), password `Spectra.env.AC_SUB_GM_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Tabel "Role yang diuji": Read Only Principal (#3), Total Control Principal (#1), Default User Principal (#2), Group Manager scope Group `Jawa` (#5).
- Data Pre-setup baca-saja: #61 `SUBS-20260101-00001` (Active, PT Sejahtera, Plan Owner PT Maju Bersama), #60 `SUBS-20260810-00001` (Trial Active, PT Sejahtera, Plan Owner PT ABC); Client dalam scope Group `Jawa` dan satu Client di luar scope disediakan Pre-setup #5 dan #35 (nama Client tidak disebut TC selain `Percetakan Mega` pada Group `Jawa`).

## Test Steps

### TC-AC-CS-74: Visibilitas elemen untuk Read Only

1. Verifikasi Search, Filter, Download, dan Changelog Show di toolbar
2. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Hidden
3. Klik ikon Changelog
4. Tutup modal Changelog lewat `✕`
5. Klik ikon Download
6. Verifikasi menu Download terbuka
7. Ketik Search `SUBS-20260101-00001`, tekan Enter
8. Klik ikon `⋯` pada baris `SUBS-20260101-00001`
9. Verifikasi menu row action hanya berisi Detail dan Subscription Log (Renew, Convert, Edit, Cancel Request, Resubmit, Cancel Subscription Hidden)
10. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
11. Klik ikon `⋯` pada baris Trial
12. Verifikasi baris Trial tampil dan menu row action hanya berisi Detail dan Subscription Log

### TC-AC-CS-30: Row action Detail membuka Subscription Detail

13. Ganti isi kotak search dengan `SUBS-20260101-00001`, tekan Enter
14. Klik ikon `⋯` pada baris `SUBS-20260101-00001`
15. Verifikasi menu row action Read Only berisi tepat dua item: Detail, Subscription Log
16. Klik `Detail`
17. Verifikasi halaman Subscription Detail untuk `SUBS-20260101-00001` terbuka
18. Verifikasi halaman Subscription Detail bersifat read-only
19. Klik segmen `Client Subscription` pada Breadcrumb

### TC-AC-CS-75: Visibilitas elemen untuk Total Control dan Default User (Total Control)

20. Logout lalu login sbg Role: Total Control (Principal) `Hendra Wijaya`
21. Buka menu `Allocation > Client Subscription`
22. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Show
23. Verifikasi Search, Filter, Download, Changelog, dan tombol `⋯` pada header kolom Actions Show
24. Ketik Search `SUBS-20260101-00001`, tekan Enter
25. Klik ikon `⋯` pada baris `SUBS-20260101-00001`
26. Verifikasi menu row action baris Active berisi Detail, Subscription Log, Renew (enabled), dan Cancel Subscription
27. Verifikasi Edit, Cancel Request, dan Resubmit tidak ada pada baris Active
28. Klik `Renew`
29. Verifikasi dialog blok V-27 tampil karena Client punya trial Active untuk Product yang sama (ACCS-LOGIC-08d)
30. Tutup dialog blok V-27
31. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
32. Klik ikon `⋯` pada baris Trial Active
33. Verifikasi menu row action baris Trial Active berisi Detail, Subscription Log, dan Convert

### TC-AC-CS-75: Visibilitas elemen untuk Total Control dan Default User (Default User)

34. Logout lalu login sbg Role: Default User (Principal) `Budi Santoso`
35. Buka menu `Allocation > Client Subscription`
36. Verifikasi tampilan elemen identik dengan Total Control: `[+ Subscription]` dan `[+ Activate Trial]` Show
37. Verifikasi Search, Filter, Download, Changelog, dan tombol `⋯` pada header kolom Actions Show
38. Ketik Search `SUBS-20260101-00001`, tekan Enter
39. Klik ikon `⋯` pada baris `SUBS-20260101-00001`
40. Verifikasi menu row action baris Active identik dengan Total Control: Detail, Subscription Log, Renew, dan Cancel Subscription tanpa Edit, Cancel Request, maupun Resubmit
41. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
42. Klik ikon `⋯` pada baris Trial Active
43. Verifikasi menu row action baris Trial Active identik dengan Total Control: Detail, Subscription Log, dan Convert

### TC-AC-CS-76: Visibilitas elemen untuk Group Manager dalam scope group

44. Logout lalu login sbg Role: Group Manager (Distributor, scoped) `Dewi Anggraini`
45. Buka menu `Allocation > Client Subscription`
46. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Show
47. Verifikasi Search, Filter, Download, Changelog, dan tombol `⋯` pada header kolom Actions Show
48. Ketik Search `Percetakan Mega`, tekan Enter
49. Klik ikon `⋯` pada baris Client dalam scope Group `Jawa`
50. Verifikasi menu row action baris dalam scope menampilkan Detail, Subscription Log, dan aksi sesuai status baris
51. Ganti isi kotak search dengan nama Client di luar scope Group `Jawa`, tekan Enter
52. Verifikasi EmptyState "No results found" tampil dan baris Client di luar scope group tidak tampil
53. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). TC-AC-CS-75 ditulis dalam dua blok (Total Control, Default User) dan Notes menyebut alasannya sama. Urutan TC: 74, 30, 75, 76 dengan role sesuai akun login berurutan (S-10).
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search, tutup modal Changelog, tutup dialog blok V-27, dan klik segmen `Client Subscription` pada Breadcrumb. Klik ikon Changelog dan Download pada TC-AC-CS-74 membuktikan keduanya dapat dibuka.
- Verifikasi di awal TC-AC-CS-74 (Search, Filter, Download, Changelog Show) mendahului Verifikasi `Hidden` sebagai anchor absence (bagian 8b butir 2).
- Spec ini 53 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (visibilitas elemen List per role); tiap role mengulang pengamatan yang sama pada surface yang sama sehingga langkah per role tidak dapat dilebur.
- Temuan untuk QA:
  - TC-AC-CS-76 tidak menyebut Subscription ID, nama Client dalam scope, dan nama Client di luar scope; spec memakai Client `Percetakan Mega` (Group `Jawa`, Pre-setup #35 pada TC-AC-CS-585) dan menulis nama Client di luar scope sebagai disediakan dari Pre-setup (S-11).
  - TC-AC-CS-75 Expected a menyebut klik `Renew` membuka dialog blok V-27 tanpa menyebut teks dialog; spec hanya mengasersi dialog blok tampil dan menutupnya.
  - TC-AC-CS-75 Expected c ("Edit, Cancel Request, dan Resubmit hanya muncul pada baris milik aktor sebagai requester") tidak menyebut baris milik aktor; spec mengasersi ketiganya tidak ada pada baris yang bukan milik aktor.
