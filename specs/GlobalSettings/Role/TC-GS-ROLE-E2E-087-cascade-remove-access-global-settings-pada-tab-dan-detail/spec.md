---
id: TC-GS-ROLE-E2E-087-cascade-remove-access-global-settings-pada-tab-dan-detail
title: "Cascade Remove Access Global Settings pada Tab dan Detail Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-233
  - TC-GS-ROLE-234
  - TC-GS-ROLE-291
coverage:
  web: automated
---

# Cascade Remove Access Global Settings pada Tab dan Detail Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah (Given dipasang lewat API di hook `before`; pemulihan di hook `after`, tanpa berasumsi langkah spec berhasil penuh):
  - Pandu Wijaya (Pre-setup #18, kandidat sekali pakai, Active): di-assign Total Control oleh Ahmad Fauzi lewat API sebelum TC-GS-ROLE-233 (precondition b TC), dengan Access Global Settings.
  - Agus Salim (Pre-setup #9, Dynamic #18): punya baris Manage TAG dan tanpa access level (precondition b TC-GS-ROLE-234), dengan Access Global Settings.
  - Rahmat Hidayat (Pre-setup #11, Dynamic #4): di-assign Read Only kembali lewat API (precondition b TC-GS-ROLE-291), dengan Access Global Settings.
  - Ketiga user juga memiliki Access produk lain (mis. `Fixed Asset`; disediakan tim FE) supaya Edit User yang mencabut Global Settings tidak ditolak `Access must not be empty` (USER V-15).
  - Pemulihan di hook `after`: Access Global Settings dicentang kembali untuk ketiganya; Pandu Wijaya tanpa access level; Agus Salim tanpa baris role (Pre-setup #9); Rahmat Hidayat tanpa access level dengan baris Manage files Read dan Delete (Pre-setup #11). Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, System Log, serta notifikasi (bersifat immutable).
- Tabel "Role" (keenam role Tab System): `Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`.
- Kemampuan teknis: seeding dan pemulihan access level, baris role, dan Access User lewat API (sesi API aktor Total Control); membaca jumlah notifikasi bertipe Role & Permission milik Pandu Wijaya tanpa login sebagai Pandu Wijaya (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD); membaca jumlah total entri Modal Changelog; membaca hasil Search Activity Log dan Tab System Log.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-233: Remove Access Global Settings untuk user Total Control

1. Buka Tab System, catat nilai kolom Users tiap role pada tabel "Role" sebagai baseline Users
2. Buka Modal Changelog Tab System, catat jumlah total entri sebagai baseline Changelog Tab System, tutup modal
3. Buka Tab Total Control, buka Modal Changelog, catat jumlah total entri sebagai baseline Changelog Tab Total Control, tutup modal
4. Buka Global Settings > Activity Log, ketik Search `Pandu Wijaya`, tekan Enter, catat jumlah entri hasil Search sebagai baseline Activity Log
5. Buka Global Settings > User > Detail Ahmad Fauzi > Tab System Log, ketik Search `Pandu Wijaya`, tekan Enter, catat jumlah entri hasil Search sebagai baseline System Log
6. Catat jumlah notifikasi Role & Permission milik Pandu Wijaya sebagai baseline notifikasi
7. Buka Global Settings > User, ketik Search `Pandu Wijaya`, tekan Enter
8. Klik `⋯` pada baris Pandu Wijaya, pilih `Edit`
9. Uncheck Access `Global Settings`
10. Klik `[Save]`
11. Klik `[Remove]` pada dialog
12. Tunggu aksi selesai
13. Buka Role & Permission > Tab Total Control, ketik Search `Pandu Wijaya`, tekan Enter
14. Verifikasi empty state `No results found` tampil di Tab Total Control
15. Untuk setiap role pada tabel "Role", lakukan langkah 16 dan 17
16. Buka Detail role tersebut dari Tab System, ketik Search `Pandu Wijaya`, tekan Enter
17. Verifikasi empty state `No results found` tampil di Detail role tersebut
18. Buka Tab Total Control, buka Modal Changelog
19. Verifikasi jumlah total entri Changelog Tab Total Control sama dengan baseline langkah 3 ditambah 1
20. Verifikasi entri baru teratas: Action `Remove`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`
21. Tutup Modal Changelog
22. Buka Tab System
23. Untuk setiap role pada tabel "Role", Verifikasi kolom Users role tersebut sama dengan baseline langkah 1 dikurangi 1
24. Buka Modal Changelog Tab System
25. Verifikasi jumlah total entri Changelog Tab System sama dengan baseline langkah 2 (tidak ada entri Remove per-role untuk Pandu Wijaya)
26. Tutup Modal Changelog
27. Buka Global Settings > Activity Log, ketik Search `Pandu Wijaya`, tekan Enter
28. Verifikasi jumlah entri hasil Search sama dengan baseline langkah 4 ditambah 2
29. Verifikasi 1 entri modul Role & Permission: Action `Remove`, Object `Total Control`, Name `Pandu Wijaya`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`
30. Verifikasi entri Remove Access milik modul User untuk `Pandu Wijaya` tampil di samping entri langkah 29
31. Buka Global Settings > User > Detail Ahmad Fauzi > Tab System Log, ketik Search `Pandu Wijaya`, tekan Enter
32. Verifikasi jumlah entri hasil Search sama dengan baseline langkah 5 ditambah 2
33. Verifikasi 1 entri modul Role & Permission: Action `Remove`, Object `Total Control`, Name `Pandu Wijaya`, Field `Access Level`, Old Value `Total Control`, New Value `—`
34. Verifikasi entri Remove Access milik modul User untuk `Pandu Wijaya` tampil di samping entri langkah 33
35. Verifikasi jumlah notifikasi Role & Permission milik Pandu Wijaya sama dengan baseline langkah 6

### TC-GS-ROLE-234: Remove Access Global Settings untuk user tanpa access level

36. Buka Role & Permission > Tab System, buka Modal Changelog, catat jumlah total entri sebagai baseline Changelog Tab System, tutup modal
37. Buka Global Settings > User, ketik Search `Agus Salim`, tekan Enter
38. Klik `⋯` pada baris Agus Salim, pilih `Edit`
39. Uncheck Access `Global Settings`
40. Klik `[Save]`
41. Klik `[Remove]` pada dialog
42. Tunggu aksi selesai
43. Buka Role & Permission > Tab System > Detail "Manage TAG", ketik Search `Agus Salim`, tekan Enter
44. Verifikasi empty state `No results found` tampil di Detail "Manage TAG"
45. Buka Tab System, buka Modal Changelog
46. Verifikasi jumlah total entri Changelog Tab System sama dengan baseline langkah 36 (tidak ada entri untuk kejadian ini)
47. Tutup Modal Changelog

### TC-GS-ROLE-291: Remove Access Global Settings untuk user Read Only

48. Buka Role & Permission > Tab Read Only, buka Modal Changelog, catat jumlah total entri sebagai baseline Changelog Tab Read Only, tutup modal
49. Buka Global Settings > Activity Log, ketik Search `Rahmat Hidayat`, tekan Enter, catat jumlah entri hasil Search sebagai baseline Activity Log
50. Buka Global Settings > User > Detail Ahmad Fauzi > Tab System Log, ketik Search `Rahmat Hidayat`, tekan Enter, catat jumlah entri hasil Search sebagai baseline System Log
51. Buka Global Settings > User, ketik Search `Rahmat Hidayat`, tekan Enter
52. Klik `⋯` pada baris Rahmat Hidayat, pilih `Edit`
53. Uncheck Access `Global Settings`
54. Klik `[Save]`
55. Klik `[Remove]` pada dialog
56. Tunggu aksi selesai
57. Buka Role & Permission > Tab Read Only, ketik Search `Rahmat Hidayat`, tekan Enter
58. Verifikasi empty state `No results found` tampil di Tab Read Only
59. Untuk setiap role pada tabel "Role", lakukan langkah 60 dan 61
60. Buka Detail role tersebut dari Tab System, ketik Search `Rahmat Hidayat`, tekan Enter
61. Verifikasi empty state `No results found` tampil di Detail role tersebut
62. Buka Tab Read Only, buka Modal Changelog
63. Verifikasi jumlah total entri Changelog Tab Read Only sama dengan baseline langkah 48 ditambah 1
64. Verifikasi entri baru teratas: Action `Remove`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Ahmad F`
65. Tutup Modal Changelog
66. Buka Global Settings > Activity Log, ketik Search `Rahmat Hidayat`, tekan Enter
67. Verifikasi jumlah entri hasil Search sama dengan baseline langkah 49 ditambah 2
68. Verifikasi 1 entri modul Role & Permission: Action `Remove`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Ahmad F`
69. Verifikasi entri Remove Access milik modul User untuk `Rahmat Hidayat` tampil di samping entri langkah 68
70. Buka Global Settings > User > Detail Ahmad Fauzi > Tab System Log, ketik Search `Rahmat Hidayat`, tekan Enter
71. Verifikasi jumlah entri hasil Search sama dengan baseline langkah 50 ditambah 2
72. Verifikasi 1 entri modul Role & Permission: Action `Remove`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `Read Only`, New Value `—`
73. Verifikasi entri Remove Access milik modul User untuk `Rahmat Hidayat` tampil di samping entri langkah 72

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Spec melewati sekitar 35 langkah (73 langkah nominal; ekspansi tiga perulangan atas enam role menambah 25 langkah, sehingga 98 langkah). Alasan: tiga blok memakai satu topik (cascade Remove Access Global Settings dari modul User), satu kelas harness (fungsional), dan tiap blok berdiri sendiri dengan user, baseline, dan state sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Panjang berasal dari baseline jumlah entri (S-12) dan tiga permukaan observasi log per TC, bukan dari beberapa kelas harness.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengikuti TC sumber; ketiga TC memakai user yang berbeda sehingga tidak ada ketergantungan data.
- Langkah 15 sampai 17 dan 59 sampai 61 adalah perulangan atas enam baris tabel "Role" (langkah yang diulang: 16 dan 17, 60 dan 61); langkah 23 adalah perulangan satu `Verifikasi` per role atas tabel yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): mencatat baseline (langkah 1 sampai 6, 36, 48 sampai 50); Search user target di modul User (langkah 7, 37, 51); "Tunggu aksi selesai" (langkah 12, 42, 56); membuka dan menutup Modal Changelog (langkah 18, 21, 24, 26, 45, 47, 62, 65); membuka Detail role dan permukaan log.
- Urutan Expected TC-GS-ROLE-233 mengikuti permukaan yang dikunjungi: a (langkah 14 sampai 17), b (langkah 19 dan 20), c (langkah 23), e (langkah 25), f (langkah 28 sampai 30), g (langkah 32 sampai 34), lalu d (langkah 35). Absence tabel (langkah 14, 17, 44, 58, 61) memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2).
- "Entri baru teratas" pada langkah 20 dan 64 berarti entri teratas Modal Changelog (urutan default terbaru) sesudah jumlah entri bertambah tepat 1 dari baseline. Entri log pada langkah 29 sampai 34 dan 68 sampai 73 dikenali lewat Search nama user target; jumlah entri dibandingkan dengan baseline hasil Search yang sama.
- Langkah 30, 34, 69, dan 73 memverifikasi klausa "di samping entry Remove Access milik modul User" pada Expected f dan g TC-GS-ROLE-233 serta Expected c dan d TC-GS-ROLE-291; TC tidak menyebut kolom entri Remove Access sehingga hanya keberadaannya yang diasersi.
- Langkah 35 (Pandu Wijaya tidak menerima notifikasi) memakai pembacaan jumlah notifikasi lewat kemampuan teknis tim FE/BE dengan baseline langkah 6; spec tidak membuka sesi UI Pandu Wijaya karena TC tidak menyediakan langkah observasi notifikasi.
- Temuan untuk QA:
  - Pre-setup #18 dan #11 mencatat user target hanya ber-Access Global Settings; mencabut satu-satunya Access ditolak (`Access must not be empty`, USER V-15). Spec menambahkan Access produk lain sebagai Given untuk ketiga user.
  - TC-GS-ROLE-233 Expected d tidak punya langkah observasi di Langkah Uji; spec mengasersinya lewat pembacaan notifikasi (kemampuan tim FE/BE tanpa endpoint di TC, PRD, dan LLD).
  - TC-GS-ROLE-233 langkah 1 sampai 3, TC-GS-ROLE-234 langkah 1, dan TC-GS-ROLE-291 langkah 1 ("Lakukan Remove Access Global Settings") tidak merinci alur di modul User; spec memakai Edit User, uncheck `Global Settings`, `[Save]`, lalu `[Remove]` pada dialog (USER TC-GS-USER-224).
  - TC-GS-ROLE-233 Expected f dan g serta TC-GS-ROLE-291 Expected c dan d tidak menyebut kolom entri Remove Access milik modul User.
  - TC-GS-ROLE-234 Expected b menyebut "Changelog Role & Permission"; Langkah Uji 2 menyebut Changelog Tab System, sehingga spec memeriksa Changelog Tab System.
