---
id: TC-GS-USER-E2E-168-resilience-tulis-switch-tab-role-5xx-dan-kegagalan-penulisan-log
title: "Resilience Tulis User: Switch Active Tab Role Gagal 5xx, serta Kegagalan Penulisan Log pada Perubahan Permission, Deactivate, dan Resend Activation Email"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-1097
  - TC-GS-USER-1136
  - TC-GS-USER-1135
  - TC-GS-USER-1117
coverage:
  web: automated
---

# Resilience Tulis User: Switch Active Tab Role Gagal 5xx, serta Kegagalan Penulisan Log pada Perubahan Permission, Deactivate, dan Resend Activation Email

## Prerequisites

- Mode: FE+BE (kelas harness b: fault injection; intercept parsial di atas backend nyata untuk TC-GS-USER-1097 dan toggle kegagalan penulisan log di sisi server untuk TC-GS-USER-1136, 1135, dan 1117; bagian 3 prinsip 13 dan bagian 6 konvensi).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai sebagai target aksi dan tidak diubah (S-06). Siti Nurhaliza (No. 2) dipakai sebagai pelaku dan pemilik Tab System Log.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated kecuali disebut lain, Division `Finance`, Access `Fixed Asset`, email `<nama tanpa spasi huruf kecil>+{runId}-168@qwertysystem.net`:
  - `Ahmad Fauzi {runId}-168`: role `Manage TAG` ter-assign (switch Active ON, Update belum tercentang sehingga checkbox Update enabled); target TC-GS-USER-1097 dan TC-GS-USER-1136.
  - `Dewi Lestari {runId}-168`: Active; target TC-GS-USER-1135.
  - `Mike Tan {runId}-168`: Pending Activation; target TC-GS-USER-1117. Activation Email awal memulai cooldown Resend 60 detik pada waktu terbit.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE (TC dan PRD hanya menyebut "endpoint switch Active dibuat gagal 5xx"):
  - Respons update switch Active Tab Role (TC-GS-USER-1097): ditahan dulu supaya posisi optimistic teramati, lalu dijawab 5xx (500) tanpa meneruskan request ke backend saat dilepas.
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Toggle kegagalan penulisan log di sisi server ("penulisan log dibuat gagal sementara"): diaktifkan dan dipulihkan lewat langkah eksplisit; hook `after` memulihkannya sebagai cadangan.
  - Membaca jumlah entri Changelog User dan System Log aktor lewat BE (N dibaca sebelum aksi, 8b butir 10, S-12).
  - Mail-catcher: membaca waktu terbit Activation Email awal dan jumlah email per alamat tujuan (baseline per alamat, R-11).
  - Manipulasi jam: jam server dan jam browser diatur bersama ke nilai absolut dan dipulihkan ke waktu nyata (cooldown Resend dihitung di server dan countdown tooltip berjalan di jam browser).
  - Penanda waktu `T168` dari jam server nyata, jam server dan jam browser sinkron (toleransi 1 menit, S-12).
- Rumus jam (cooldown 60 detik): `T_M` = waktu terbit Activation Email awal `Mike Tan {runId}-168` dibaca dari mail-catcher; jam server dan jam browser diatur bersama ke `T_M` + 60 detik (absolut, bukan geser relatif) supaya cooldown awal berakhir dan `Resend Activation Email` dapat diklik.
- State global yang diubah: toggle kegagalan penulisan log (dipulihkan lewat langkah eksplisit di akhir tiap blok TC) dan jam server dan jam browser (dipulihkan lewat langkah 56 sebelum spec berakhir). Hook `after` memulihkan keduanya sebagai cadangan. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): lepas intercept, pulihkan toggle penulisan log dan jam, hapus ketiga user seed lewat API. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Persiapan

1. Catat penanda waktu T168 (waktu server nyata) sebelum aksi pemicu pertama yang diasersi

### TC-GS-USER-1097: Tab Role, switch gagal 5xx mengembalikan switch dan menampilkan toast error

2. Ketik Search `Ahmad Fauzi {runId}-168`, tekan Enter
3. Klik Name `Ahmad Fauzi {runId}-168` di User List
4. Klik Tab `Role`
5. Pasang intercept pada respons update switch Active Tab Role: tahan respons, lalu jawab 5xx
6. Matikan switch Active baris `Manage TAG`
7. Verifikasi switch Active baris `Manage TAG` menampilkan posisi OFF selama respons ditahan (optimistic)
8. Teruskan jawaban 5xx dengan melepas tahanan respons
9. Verifikasi toast error: "Error, failed to update role."
10. Lepas intercept respons update switch Active Tab Role
11. Verifikasi switch Active baris `Manage TAG` kembali ke posisi sebelum klik (ON)
12. Verifikasi checkbox baris `Manage TAG` enabled

### TC-GS-USER-1136: Tab Role, kegagalan menulis log membatalkan perubahan permission

13. Aktifkan kegagalan penulisan log (kemampuan disediakan tim BE)
14. Catat jumlah entri Changelog User `Ahmad Fauzi {runId}-168` dan jumlah entri System Log aktor Siti Nurhaliza lewat kemampuan baca BE sebagai baseline CL0 dan SL0
15. Centang Update baris `Manage TAG`
16. Verifikasi toast error: "Error, failed to update permissions."
17. Verifikasi checkbox Update baris `Manage TAG` kembali ke nilai sebelum klik (tidak tercentang)
18. Muat ulang halaman (F5)
19. Klik Tab `Role`
20. Verifikasi Update baris `Manage TAG` tidak tercentang (perubahan tidak tersimpan)
21. Verifikasi jumlah entri Changelog User `Ahmad Fauzi {runId}-168` sama dengan CL0 (dibaca lewat BE)
22. Verifikasi jumlah entri System Log aktor Siti Nurhaliza sama dengan SL0 (dibaca lewat BE)
23. Pulihkan penulisan log

### TC-GS-USER-1135: Log Activate/Deactivate ditulis setelah commit, kegagalan log tidak me-rollback toggle

24. Klik menu User di sidebar Global Settings
25. Ketik Search `Dewi Lestari {runId}-168`, tekan Enter
26. Aktifkan kegagalan penulisan log (kemampuan disediakan tim BE)
27. Klik switch Active baris `Dewi Lestari {runId}-168`
28. Klik `[Deactivate]`
29. Verifikasi toast sukses "Success, user has been deactivated."
30. Verifikasi switch Active baris `Dewi Lestari {runId}-168` OFF
31. Klik Name `Dewi Lestari {runId}-168` di User List
32. Verifikasi badge `Inactive` tampil di Header Detail (status tidak di-rollback)
33. Pulihkan penulisan log
34. Klik Tab `Changelog`
35. Muat ulang halaman lalu klik Tab `Changelog` tiap 5 detik sampai baris Action `Deactivate` muncul (batas tunggu 2 menit)
36. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-168`: baris dengan Action `Deactivate`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T168
37. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-168`: tepat 1 baris dengan Action `Deactivate` (tidak duplikat)
38. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari {runId}-168`, tekan Enter; muat ulang halaman tiap 5 detik sampai baris Action `Deactivate` muncul (batas tunggu 2 menit)
39. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Deactivate`, Object `User`, Name `Dewi Lestari {runId}-168`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, bertanggal pada atau sesudah T168
40. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-168` (tidak duplikat)
41. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-168`, tekan Enter; muat ulang halaman tiap 5 detik sampai baris Action `Deactivate` muncul (batas tunggu 2 menit)
42. Verifikasi Activity Log: baris dengan Action `Deactivate`, Object `User`, Name `Dewi Lestari {runId}-168`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T168
43. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-168` (tidak duplikat)

### TC-GS-USER-1117: Penulisan log Resend gagal tidak membatalkan email dan cooldown tetap dimulai

44. Klik menu User di sidebar Global Settings
45. Ketik Search `Mike Tan {runId}-168`, tekan Enter
46. Baca waktu terbit Activation Email awal `Mike Tan {runId}-168` (`T_M`) dari mail-catcher
47. Catat jumlah email ke alamat `miketan+{runId}-168@qwertysystem.net` di mail-catcher sebagai baseline M0
48. Atur jam server dan jam browser bersama ke waktu absolut `T_M` + 60 detik, sehingga cooldown Resend awal berakhir
49. Aktifkan kegagalan penulisan log (kemampuan disediakan tim BE)
50. Klik Name `Mike Tan {runId}-168` di User List
51. Klik `Resend Activation Email`
52. Verifikasi toast sukses "Success, activation email has been sent."
53. Hover tombol `Resend Activation Email`
54. Verifikasi tombol `Resend Activation Email` Disabled dengan tooltip countdown (cooldown dimulai)
55. Verifikasi jumlah email ke alamat `miketan+{runId}-168@qwertysystem.net` di mail-catcher menjadi M0 + 1 (email tetap terkirim)
56. Pulihkan jam server dan jam browser ke waktu nyata
57. Pulihkan penulisan log

## Notes

- Mode: FE+BE (intercept parsial dan toggle kegagalan sisi server, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (57 langkah). Alasan: keempat TC berada di satu kelas harness (b: kegagalan 5xx dan kegagalan penulisan log pada aksi tulis User) dan satu akun aktor; tiap blok TC berdiri sendiri (intercept atau toggle log dipasang dan dipulihkan di dalam blok, user seed sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah TC-GS-USER-1135 (langkah 34 sampai 43) adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) pada tiga surface yang disebut Expected TC.
- Urutan TC sumber diubah: TC-GS-USER-1097 dan TC-GS-USER-1136 dikelompokkan pada Detail Ahmad Fauzi seed yang sama dan Tab Role yang sama (langkah 1 TC-GS-USER-1136 "Klik Name ... buka Tab `Role`" dipenuhi langkah 3 dan 4); kegagalan 1097 mengembalikan switch ke ON sehingga state awal 1136 tidak berubah. TC-GS-USER-1135 dan TC-GS-USER-1117 mengikuti karena memakai user seed berbeda.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (penanda waktu), 2, 25, 45 (Search), 5, 8, 10 (memasang, meneruskan, dan melepas intercept), 13, 26, 49 (mengaktifkan kegagalan penulisan log), 14 (mencatat baseline), 18 dan 19 (muat ulang halaman lalu kembali ke Tab `Role`), 23, 33, 57 (memulihkan penulisan log), 24 dan 44 (kembali ke User List lewat menu User), 31, 34, 50 (membuka Detail dan tab), 35, 38, 41 (membuka surface log dan polling "worker commit" tiap 5 detik, batas 2 menit, bagian 6 konvensi), 46 sampai 48 (membaca `T_M`, baseline email, dan mengatur jam), 53 (hover pemicu tooltip, bagian 8b butir 5), 56 (memulihkan jam sebelum spec berakhir, S-09). Langkah 38 dan 41 memakai pola 138 (membuka Detail `Siti Nurhaliza` atau Activity Log dan Search nama dalam satu langkah).
- Baseline: Changelog User dan System Log aktor pada TC-GS-USER-1136 memakai jumlah entri yang dibaca lewat BE tepat sebelum aksi (CL0 dan SL0; langkah 14) lalu `Verifikasi` jumlah sama setelah anchor positif (toast error pada langkah 16 dan state checkbox pada langkah 17 dan 20); ini asersi jumlah berbaseline, bukan spec absence (kelas g). Pencatatan Deactivate normal tanpa kegagalan log ada di spec 140. Nama user seed bersuffix unik sehingga baseline entri `Deactivate` TC-GS-USER-1135 adalah nol.
- Pembagian TC lintas spec: Toggle Active sukses dan dialog ada di spec 047; Toggle Active gagal 5xx ada di spec 067; auto-save Tab Role sukses di spec 064 dan kegagalan 5xx role lain di spec 068; Resend Activation Email sukses di spec 141 dan gagal 5xx di spec 067.
- Temuan untuk QA:
  - TC-GS-USER-1136, 1135, dan 1117 menulis precondition "penulisan log dibuat gagal" tanpa mekanisme di TC, PRD, atau LLD; spec memakai toggle kegagalan penulisan log yang disediakan tim BE (S-13). Need Confirmation: mekanisme dan lingkup toggle (hanya Changelog, System Log, dan Activity Log, atau semuanya).
  - TC-GS-USER-1136 Expected c ("Tidak ada entri log baru") tidak menyebut surface; spec mengasersi Changelog User target dan System Log aktor lewat baseline BE. Activity Log tidak diasersi pada blok ini. Need Confirmation: surface yang dimaksud.
  - TC-GS-USER-1135 langkah 4 hanya menyebut Tab Changelog dan Tab System Log (aktor), sedangkan Expected b menyebut juga Activity Log; spec membaca ketiganya. Expected b "eventual, bukan instan" tidak memberi batas waktu; spec memakai polling 5 detik dengan batas 2 menit (bagian 6 konvensi). TC tidak menyebut Field, Old Value, dan New Value entri `Deactivate`; spec memakai nilai dari spec 140 (`Status (Global)`, `Active`, `Inactive`).
  - TC-GS-USER-1117 Expected c klausa "bila tetap gagal, ditandai butuh reprocessing manual (`USER-LOGIC-09c`)" tidak punya permukaan UI atau langkah observasi di TC; tidak diasersi. TC juga tidak menyebut cooldown Resend awal setelah Activation Email seed; spec memajukan jam sesuai bagian 6 supaya tombol dapat diklik.
  - TC-GS-USER-1097 menulis "Matikan switch Active baris `Manage TAG`" tanpa menyebut role sudah ter-assign dan berstatus ON; spec men-seed Ahmad Fauzi dengan `Manage TAG` ter-assign (checkbox role yang belum di-assign disabled, TC-GS-USER-1051).
  - TC-GS-USER-1097, 1136, 1135, dan 1117 memakai Ahmad Fauzi, Dewi Lestari, dan Mike Tan Pre-setup; spec memakai seed bersuffix milik spec (S-06, S-12).
