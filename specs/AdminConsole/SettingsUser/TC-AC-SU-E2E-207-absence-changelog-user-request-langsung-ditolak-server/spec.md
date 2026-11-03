---
id: TC-AC-SU-E2E-207-absence-changelog-user-request-langsung-ditolak-server
title: "Absence Changelog: User untuk Request Langsung yang Ditolak Server pada Mutasi Default User, Role Diri Sendiri, Edit Role Target Total Control, Group Role tanpa Assignment, Cooldown Resend, dan Deactivate Target Total Control"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-615
  - TC-AC-SU-616
  - TC-AC-SU-617
  - TC-AC-SU-620
  - TC-AC-SU-621
  - TC-AC-SU-665
coverage:
  web: automated
---

# Absence Changelog: User untuk Request Langsung yang Ditolak Server pada Mutasi Default User, Role Diri Sendiri, Edit Role Target Total Control, Group Role tanpa Assignment, Cooldown Resend, dan Deactivate Target Total Control

## Prerequisites

- Mode: FE+BE.
- Akun UI aktor (pengamat Popup Changelog: User dan pelaku Resend pertama TC-621): Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun UI di tengah spec; hook `after` memulihkan sesi ke akun default suite.
- Sesi API tiap aktor request (login API password; token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE):

| Blok | Aktor request | Akun | Password |
|---|---|---|---|
| TC-615, TC-620, TC-621 | Total Control | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-616, TC-617, TC-665 | Manage user and role (Update) | `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_MUR_UPDATE_PASSWORD` |

- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12). Data Pre-setup bersama tidak diubah. Data milik spec (target yang request-nya ditolak server):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Dewi Lestari {runId}-207A` | `dewilestari+{runId}-207a@qwertysystem.net` | Activated, Active, bertier Total Control (TC-617) |
| U2 | `Dewi Lestari {runId}-207B` | `dewilestari+{runId}-207b@qwertysystem.net` | Activated, Active, bertier Total Control (TC-665) |
| U3 | `Mike Tan {runId}-207C` | `miketan+{runId}-207c@qwertysystem.net` | Activated, tanpa tier, "Manage partner" tanpa group assignment (TC-620) |
| U4 | `Sarah Lee {runId}-207D` | `sarahlee+{runId}-207d@qwertysystem.net` | Pending Activation, di luar cooldown Resend (TC-621) |
| Pre-setup | Default User Principal (#1) target TC-615; akun Manage user and role (Update) (#4) target TC-616 | - | hanya dibaca (request ditolak, state tidak diubah); tidak dapat dimiliki spec |

- Baseline: Changelog: User adalah audit trail permanen, sehingga total entri tidak diasersi sebagai angka absolut. Tiap blok mencatat jumlah entri sendiri sebelum request (N1 sampai N6; TC-621 memakai baseline B6 sebelum Resend pertama dan N6 sesudahnya) dan mengasersi jumlah entri sama dengan baseline itu (S-12).
- Kemampuan teknis (pemicu kelas a, P-5 butir a): klien HTTP yang mengirim request langsung ke server atas nama aktor tiap blok; pola request (path dan body) disediakan tim FE/BE tanpa endpoint karangan di spec; kemampuan membaca jumlah entri Changelog: User sebelum dan sesudah request (disediakan tim FE/BE, bagian 8b butir 10); jam server dan jam browser dapat dibekukan dan dipulihkan (TC-621). Tanpa intercept dan tanpa mail-catcher.
- Waktu TC-621: acuan T dibaca dari waktu terbit entri Resend pertama lewat API seeding (bukan perkiraan dari jam hook). Jam server dan jam browser dibekukan pada T + 10 detik sehingga request Resend kedua berada dalam jendela cooldown 60 detik; margin terhadap batas = 60 detik - 10 detik = 50 detik. Baseline B6 dicatat sebelum Resend pertama dan N6 dicatat sesudah entri Resend pertama terbaca (langkah 34), keduanya sebelum jam dibekukan.
- State global yang diubah spec: jam server dan jam browser (hanya TC-621); dipulihkan pada langkah 39 dan di hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Langkah "Tunggu aksi selesai" pada TC-621 memakai polling tiap 5 detik sampai jumlah entri Changelog: User naik 1 dari baseline B6, batas tunggu 30 detik (entri Resend ditulis di background).
- Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-615: Mutasi Default User
1. Catat jumlah entri Changelog: User lewat kemampuan baca sebagai N1
2. Kirim request langsung untuk menonaktifkan Default User Principal atas nama aktor Total Control
3. Verifikasi respons server berupa penolakan (bukan 2xx)
4. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
5. Verifikasi Popup Changelog: User menampilkan sedikitnya satu baris entri
6. Verifikasi jumlah entri Changelog: User (dibaca lewat kemampuan baca) sama dengan N1 (tidak dicatat)
### TC-AC-SU-616: Mutasi role diri sendiri
7. Tutup popup, lalu catat jumlah entri Changelog: User lewat kemampuan baca sebagai N2
8. Kirim request langsung untuk mematikan role "Manage user and role" pada akun aktor sendiri atas nama aktor Manage user and role (Update)
9. Verifikasi respons server berupa penolakan (bukan 2xx)
10. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
11. Verifikasi Popup Changelog: User menampilkan sedikitnya satu baris entri
12. Verifikasi jumlah entri Changelog: User (dibaca lewat kemampuan baca) sama dengan N2 (tidak dicatat)
### TC-AC-SU-617: Edit role target Total Control
13. Tutup popup, lalu catat jumlah entri Changelog: User lewat kemampuan baca sebagai N3
14. Kirim request langsung untuk mengedit CRUD role U1 (`Dewi Lestari {runId}-207A`) atas nama aktor Manage user and role (Update)
15. Verifikasi respons server berupa penolakan (bukan 2xx)
16. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
17. Verifikasi Popup Changelog: User menampilkan sedikitnya satu baris entri
18. Verifikasi jumlah entri Changelog: User (dibaca lewat kemampuan baca) sama dengan N3 (tidak ada entri baru)
### TC-AC-SU-665: Deactivate target Total Control
19. Tutup popup, lalu catat jumlah entri Changelog: User lewat kemampuan baca sebagai N4
20. Kirim request langsung untuk menonaktifkan U2 (`Dewi Lestari {runId}-207B`) atas nama aktor Manage user and role (Update, U=true)
21. Verifikasi respons server berupa penolakan (bukan 2xx)
22. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
23. Verifikasi Popup Changelog: User menampilkan sedikitnya satu baris entri
24. Verifikasi jumlah entri Changelog: User (dibaca lewat kemampuan baca) sama dengan N4 (tidak ada entri baru)
### TC-AC-SU-620: Flag aktif Group Role tanpa assignment
25. Tutup popup, lalu catat jumlah entri Changelog: User lewat kemampuan baca sebagai N5
26. Kirim request langsung yang mengirim flag aktif untuk "Manage partner" U3 (`Mike Tan {runId}-207C`) tanpa group assignment atas nama aktor Total Control
27. Verifikasi respons server berupa penolakan hak akses (bukan 2xx)
28. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
29. Verifikasi Popup Changelog: User menampilkan sedikitnya satu baris entri
30. Verifikasi jumlah entri Changelog: User (dibaca lewat kemampuan baca) sama dengan N5 (tidak dicatat entri log)
### TC-AC-SU-621: Cooldown Resend ditegakkan server
31. Tutup popup, ketik Search `Sarah Lee {runId}-207D`, tekan Enter
32. Catat jumlah entri Changelog: User lewat kemampuan baca sebagai baseline B6 (sebelum Resend pertama)
33. Buka row action (⋯) baris U4, lalu klik Resend Activation Email
34. Tunggu aksi selesai: baca jumlah entri Changelog: User lewat kemampuan baca tiap 5 detik sampai jumlah naik 1 dari B6 (batas tunggu 30 detik), lalu catat jumlah itu sebagai N6 (entri Resend pertama sudah termasuk)
35. Catat T dari waktu terbit entri Resend pertama lewat API seeding
36. Bekukan jam server dan jam browser pada T + 10 detik
37. Kirim request langsung Resend Activation Email kedua untuk U4 atas nama aktor Total Control
38. Verifikasi respons server berupa penolakan (bukan 2xx)
39. Pulihkan jam server dan jam browser
40. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
41. Verifikasi Popup Changelog: User menampilkan sedikitnya satu baris entri
42. Verifikasi jumlah entri Changelog: User (dibaca lewat kemampuan baca) sama dengan N6 (tidak dicatat)
43. Tutup popup, lalu klik `(←)` pada kotak Search

## Notes

- P-5 butir (a): spec absence (kelas g) memuat pemicu request langsung kelas a (dan pembekuan jam pada TC-621) yang hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji. Tiap TC punya baseline sendiri (N1 sampai N6); data target milik spec kecuali target Pre-setup TC-615 dan TC-616 yang hanya dibaca (S-06).
- Pembagian TC lintas spec (S-05): TC-615, TC-616, dan TC-617 juga ada di `sourceTc` spec 182; TC-620, TC-621, dan TC-665 juga ada di `sourceTc` spec 183. Spec 182 dan 183 mengasersi respons server, state data, dan (TC-621) state tombol cooldown; spec ini hanya mengasersi klausa "tidak dicatat di Changelog: User" dengan aksi nyata dan baseline sendiri.
- Request langsung mengikuti bagian 8b butir 1: asersi pada request hanya respons server (bukan 2xx). Toast, refresh UI, state switch, dan state tombol yang disebut Expected TC (TC-615 `"Default User cannot be modified."`; TC-616 `"You can't manage your own account from here."`; TC-617 dan TC-665 `"You don't have permission to edit."`; TC-620 `"You don't have permission to do this."`) tidak diasersi di spec ini; asersi state data dan perilaku FE ada di spec 182, 183, dan spec jalur UI.
- Anchor absence (bagian 8b butir 2): pemicu tiap blok menyentuh entitas yang berbeda sehingga anchor memakai respons penolakan server pada langkah sebelumnya, sedikitnya satu baris entri di Popup Changelog: User, dan jumlah entri terhadap baseline sebagai surface agregat.
- Urutan blok: TC-615, TC-616, TC-617, TC-665, TC-620, TC-621. TC-621 di akhir karena satu-satunya blok yang membekukan jam dan memakai UI untuk aksi pertama; blok request langsung lain tidak bergantung pada jam (S-10).
- Langkah penghubung tanpa Verifikasi (S-03): pencatatan baseline, menutup popup, Search baris target Resend (langkah 31, R-16), polling "Tunggu aksi selesai" (langkah 34, batas 30 detik), pencatatan T (langkah 35), pembekuan dan pemulihan jam, serta mengosongkan Search (langkah 43).
- Spec ini 43 langkah (di atas smell 35 langkah): enam blok seluruhnya satu kelas harness (absence kelas g, satu surface Popup Changelog: User) dan berdiri sendiri dengan baseline masing-masing; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log berpola (buka Popup Changelog: User, Verifikasi anchor, Verifikasi jumlah) 18 langkah tidak dihitung ke smell.
- Temuan untuk QA:
  - Expected TC-615, TC-616, TC-620, dan TC-621 menyebut "tidak dicatat" tanpa cara membaca jumlah entri; spec memakai kemampuan baca jumlah entri Changelog: User yang disediakan tim FE/BE (bagian 8b butir 10).
  - TC memberi precondition login sebagai aktor request (Manage user and role atau Total Control); spec memakai sesi UI Total Control hanya sebagai pengamat Popup Changelog: User dan sesi API aktor TC sebagai pengirim request.
  - TC-615 dan TC-616 memakai target Pre-setup (Default User dan akun Manage user and role) yang tidak dapat dimiliki spec; targetnya hanya dibaca.
  - TC-665 menyebut aktor "sebagai `Mike Tan`" tanpa pernyataan tegas; spec memakai akun Pre-setup #4 sebagai aktor dan user bersuffix sebagai target.
  - Expected TC-620 dan TC-621 tidak menyebut status HTTP penolakan; spec mengasersi respons bukan 2xx.
  - TC memakai nama literal (`Dewi Lestari`, `Mike Tan`, `Sarah Lee`); spec memakai nama bersuffix (S-12).
