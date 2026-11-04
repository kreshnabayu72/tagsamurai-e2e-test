---
id: TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role
title: "Resilience Tulis User: Cancel Pending Email Change, Pair dan Unpair TAG, Reset Authenticator, Ganti dan Hapus Foto Avatar, Inline Edit Custom Field, dan Auto-Save Tab Role Gagal 5xx dengan State Dikembalikan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-236
  - TC-GS-USER-351
  - TC-GS-USER-330
  - TC-GS-USER-339
  - TC-GS-USER-342
  - TC-GS-USER-322
  - TC-GS-USER-378
  - TC-GS-USER-320
coverage:
  web: automated
---

# Resilience Tulis User: Cancel Pending Email Change, Pair dan Unpair TAG, Reset Authenticator, Ganti dan Hapus Foto Avatar, Inline Edit Custom Field, dan Auto-Save Tab Role Gagal 5xx dengan State Dikembalikan

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness b: fault injection, bagian 3 prinsip 13 dan bagian 6 konvensi). TC-GS-USER-320 juga memakai simulasi scan TAG pada RFID reader dan diletakkan paling akhir (langkah 76 sampai 84).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Division `Finance` (No. 23), produk `Fixed Asset` (No. 26), Custom Field Blood Type (No. 24), dan John Doe (No. 18, Activated, TAG `TAG-4F7K2XQ9` Verified) untuk TC-GS-USER-322. `TAG-4F7K2XQ9` hanya terpasang pada John Doe sehingga tidak dapat digandakan ke user seed; Unpair digagalkan intercept tanpa meneruskan request ke backend, sehingga TAG, Last Updated, dan Modified By John Doe tidak berubah.
- Berkas foto uji (fixture berkas, disediakan tim FE): `john3.png` (TC-GS-USER-339).
- TAG `TAG-USR-0001` (Tabel Pre-setup No. 25, user, aktif, bebas) hanya dipakai sebagai nilai scan pada TC-GS-USER-320; Pair digagalkan intercept sehingga TAG tidak berubah.
- Data Dinamis, di-seed lewat API di hook `before` (HK1), Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Rina Putri {runId}-068`, Email `rinaputri+{runId}-068@qwertysystem.net`, email pending `rinaputri.new+{runId}-068@qwertysystem.net` (target TC-GS-USER-236).
  - `Dewi Lestari {runId}-068`, Email `dewilestari+{runId}-068@qwertysystem.net`, tanpa TAG (badge `Unverified`), Blood Type `A` (target TC-GS-USER-351 dan TC-GS-USER-320; user tanpa TAG sehingga badge `Unverified`).
  - `John Doe {runId}-068`, Email `johndoe+{runId}-068@qwertysystem.net`, MFA Enrolled, foto profil berkas `john-{runId}-068.png` (target TC-GS-USER-330, 339, dan 342).
  - `Ahmad Fauzi {runId}-068`, Email `ahmadfauzi+{runId}-068@qwertysystem.net`, role `Manage TAG` ter-assign (switch Active ON, Update belum tercentang) sehingga checkbox Update enabled (target TC-GS-USER-378).
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Semua jawaban 5xx (500) diberikan tanpa meneruskan request ke backend, dan tiap intercept dilepas segera setelah toast hasilnya tampil:
  - Respons Cancel Pending Email Change (TC-GS-USER-236).
  - Respons update Custom Field (TC-GS-USER-351).
  - Respons Reset Authenticator (TC-GS-USER-330).
  - Respons ganti foto (TC-GS-USER-339) dan respons hapus foto (TC-GS-USER-342).
  - Respons Unpair TAG (TC-GS-USER-322).
  - Respons Pair TAG dari Detail (TC-GS-USER-320): dijawab 5xx tanpa meneruskan request ke backend sehingga `TAG-USR-0001` tetap bebas.
  - Respons update permission Tab Role (TC-GS-USER-378): ditahan dulu supaya nilai baru (optimistic) teramati, lalu dijawab 5xx saat dilepas.
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Seeding user Activated dengan email pending, MFA Enrolled, foto profil berkas `john-{runId}-068.png`, dan nilai Custom Field Blood Type lewat API.
  - Simulasi RFID reader tersambung dan simulasi scan TAG pada tombol `Scan TAG` (HK7); TC tidak menyebut mekanismenya.
  - Membaca sumber gambar avatar untuk dibandingkan dengan baseline, dan membaca state centang checkbox Tab Role.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah, tanpa mengandalkan setup berhasil penuh): lepas semua intercept; lepas `TAG-USR-0001` bila terpasang (cadangan); hapus lewat API keempat user seed dan berkas `john-{runId}-068.png`; kembalikan sesi ke akun default suite.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-068`, tekan Enter

### TC-GS-USER-236: Cancel Pending Email Change gagal 5xx

2. Pasang intercept pada respons Cancel Pending Email Change: jawab 5xx
3. Klik (⋯) baris `Rina Putri {runId}-068` → `Edit`
4. Klik Button Cancel di samping label pending
5. Klik `[Cancel Change]`
6. Verifikasi toast error: "Error, failed to cancel email change."
7. Lepas intercept respons Cancel Pending Email Change
8. Verifikasi label `Pending email change to rinaputri.new+{runId}-068@qwertysystem.net` tetap tampil
9. Verifikasi Button Cancel di samping label pending tetap tampil
10. Verifikasi dialog Cancel Pending Email Change tetap terbuka
11. Verifikasi tombol `[Cancel Change]` enabled
12. Klik `[Go Back]` pada dialog Cancel Pending Email Change
13. Klik `✕` pada header Popup Edit
14. Verifikasi badge `Pending Email Confirmation` tetap tampil pada baris `Rina Putri {runId}-068` di User List

### TC-GS-USER-351: Inline edit Custom Field gagal server

15. Klik Name `Dewi Lestari {runId}-068` di User List
16. Pasang intercept pada respons update Custom Field: jawab 5xx
17. Hover baris Blood Type, klik icon edit
18. Pilih `O`
19. Klik `[✓ Save]`
20. Verifikasi toast error: "Error, failed to update Blood Type."
21. Lepas intercept respons update Custom Field
22. Verifikasi baris Blood Type tetap Active (mode edit dengan dropdown, `[✓ Save]`, dan `[✕ Cancel]`)
23. Klik `[✕ Cancel]` pada baris Blood Type

### TC-GS-USER-330: Reset Authenticator gagal server

24. Klik menu User di sidebar Global Settings
25. Klik icon Search, ketik `{runId}-068`, tekan Enter
26. Klik Name `John Doe {runId}-068` di User List
27. Pasang intercept pada respons Reset Authenticator: jawab 5xx
28. Klik `Reset Authenticator`
29. Klik `[Reset]`
30. Verifikasi toast error: "Error, failed to reset authenticator for John Doe {runId}-068."
31. Lepas intercept respons Reset Authenticator
32. Verifikasi Badge status authenticator tetap `Enrolled`
33. Verifikasi dialog Reset Authenticator tetap terbuka
34. Verifikasi tombol `[Reset]` enabled
35. Klik `[Cancel]` pada dialog Reset Authenticator

### TC-GS-USER-339: Ganti foto dari Detail gagal server

36. Catat sumber gambar avatar `John Doe {runId}-068` di header Detail sebagai baseline avatar
37. Pasang intercept pada respons ganti foto: jawab 5xx
38. Hover Avatar lalu klik `[Edit]`
39. Pilih file `john3.png`
40. Verifikasi toast error: "Error, failed to update photo."
41. Lepas intercept respons ganti foto
42. Verifikasi sumber gambar avatar sama dengan baseline avatar (foto tidak berubah)

### TC-GS-USER-342: Delete foto dari Detail gagal server

43. Pasang intercept pada respons hapus foto: jawab 5xx
44. Hover Avatar lalu klik `[Delete]`
45. Klik `[Remove]`
46. Verifikasi toast error: "Error, failed to remove photo."
47. Lepas intercept respons hapus foto
48. Verifikasi sumber gambar avatar sama dengan baseline avatar (foto tidak berubah)
49. Verifikasi dialog Remove Photo tetap terbuka
50. Verifikasi tombol `[Remove]` enabled
51. Klik `[Cancel]` pada dialog Remove Photo

### TC-GS-USER-322: Unpair TAG dari Detail gagal server

52. Klik menu User di sidebar Global Settings
53. Klik icon Search, ketik `John Doe`, tekan Enter
54. Klik Name `John Doe` (nama persis, bukan `John Doe {runId}-068`) di User List
55. Pasang intercept pada respons Unpair TAG: jawab 5xx
56. Klik `Unpair`
57. Klik `[Unpair]`
58. Verifikasi toast error: "Error, failed to unpair TAG."
59. Lepas intercept respons Unpair TAG
60. Verifikasi Badge sub-section User TAG tetap `Verified`
61. Verifikasi dialog Unpair TAG tetap terbuka
62. Verifikasi tombol `[Unpair]` enabled
63. Klik `[Cancel]` pada dialog Unpair TAG

### TC-GS-USER-378: Tab Role, auto-save gagal mengembalikan checkbox

64. Klik menu User di sidebar Global Settings
65. Klik icon Search, ketik `{runId}-068`, tekan Enter
66. Klik Name `Ahmad Fauzi {runId}-068` di User List
67. Klik Tab `Role`
68. Catat state checkbox Update baris `Manage TAG` sebagai baseline checkbox
69. Pasang intercept pada respons update permission: tahan respons, lalu jawab 5xx
70. Centang Update baris `Manage TAG`
71. Verifikasi checkbox Update baris `Manage TAG` menampilkan nilai baru (kebalikan baseline checkbox) selama respons ditahan
72. Teruskan jawaban 5xx dengan melepas tahanan respons
73. Verifikasi toast error: "Error, failed to update permissions."
74. Lepas intercept respons update permission
75. Verifikasi checkbox Update baris `Manage TAG` kembali ke state baseline checkbox

### TC-GS-USER-320: Pair TAG dari Detail gagal server

76. Klik menu User di sidebar Global Settings
77. Klik icon Search, ketik `{runId}-068`, tekan Enter
78. Klik Name `Dewi Lestari {runId}-068` di User List
79. Pasang intercept pada respons Pair TAG: jawab 5xx
80. Klik `Scan TAG`
81. Simulasikan scan `TAG-USR-0001`
82. Verifikasi toast error: "Error, failed to pair TAG."
83. Lepas intercept respons Pair TAG
84. Verifikasi Badge tetap `Unverified`

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (84 langkah). Alasan: ketujuh TC berada di satu kelas harness (b, kegagalan 5xx aksi tulis di User List dan User Detail) dan satu akun; tiap blok TC berdiri sendiri (intercept sendiri, dilepas di dalam blok, user seed sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian langkah adalah navigasi antar user dan penutupan dialog konfirmasi.
- Urutan TC sumber diubah dan dikelompokkan per user target supaya Detail tidak dibuka berulang: TC-GS-USER-236 (popup Edit di User List), TC-GS-USER-351 (Detail Dewi Lestari seed), TC-GS-USER-330, 339, dan 342 (Detail John Doe seed), TC-GS-USER-322 (Detail John Doe Pre-setup), TC-GS-USER-378 (Tab Role Ahmad Fauzi seed), lalu TC-GS-USER-320 (Detail Dewi Lestari seed, simulator scan) paling akhir. Tidak ada TC yang menghapus data.
- Pemisahan blok simulator scan (konvensi bagian 3, pemisah nyata hardware berisiko): TC-GS-USER-320 membutuhkan simulator scan TAG pada langkah 81; objek ujinya adalah kegagalan tulis Pair TAG (resilience, kelas b), bukan perangkat scan. Semua blok tanpa hardware diletakkan lebih dulu dan blok simulator di akhir (langkah 76 sampai 84); langkah 76 sampai 78 memulihkan layar dan Detail. State antar blok tidak perlu dipulihkan karena intercept dilepas di dalam blok dan tidak ada data berubah. TC ini tetap di spec resilience ini; butir ini hanya mencatat urutan blok hardware di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search, memasang dan melepas intercept, mencatat baseline avatar dan checkbox, `[Go Back]`, `[Cancel]` yang menutup dialog konfirmasi, `✕` yang menutup Popup Edit (form tidak berubah sehingga tidak memunculkan `Unsaved Changes`), `[✕ Cancel]` yang mengakhiri mode edit inline, dan navigasi ke User List lewat menu User.
- Asersi "foto tidak berubah" (TC-GS-USER-339 dan 342) memakai satu baseline avatar yang dicatat sebelum aksi pertama di Detail John Doe seed; kedua aksi digagalkan intercept sehingga baseline yang sama berlaku untuk keduanya.
- Pembagian TC lintas spec: Cancel Pending Email Change sukses diverifikasi di spec 045, Pair TAG sukses serta Unpair TAG sukses di spec 057, Reset Authenticator sukses di spec 058, ganti dan hapus foto Detail sukses di spec 059, inline edit Custom Field sukses di spec 060, dan auto-save Tab Role sukses di spec 064; spec ini hanya memuat jalur kegagalan.
- Temuan untuk QA:
  - TC-GS-USER-320: berstatus Manual Only (scan RFID) tetapi tetap ditulis (bagian 2 konvensi); precondition "dibuat gagal 5xx" tanpa nama endpoint, spec memicu lewat `Spectra.intercept()` di atas backend nyata dan nama endpoint ditentukan tim FE. Expected b ditulis `Badge tetap Unverified`. Precondition "RFID reader tersambung" disediakan tim FE.
  - TC-GS-USER-236, 322, 330, 339, 342, 351, dan 378 menulis precondition "dibuat gagal 5xx" (TC-GS-USER-236 menambah "mock/proxy") tanpa nama endpoint; spec memicu lewat `Spectra.intercept()` di atas backend nyata dan nama endpoint ditentukan tim FE di tahap script.
  - TC-GS-USER-322 memakai John Doe Pre-setup (TAG `TAG-4F7K2XQ9`) sebagai target aksi tulis; aksi digagalkan intercept tanpa meneruskan request sehingga tidak ada perubahan data. TAG yang sama tidak dapat dipasang pada user seed.
  - TC-GS-USER-236 Expected b ("Label dan pending state tidak berubah") tidak merinci; spec mengasersi label pending, Button Cancel, dan badge `Pending Email Confirmation` di User List.
  - TC-GS-USER-339 dan 342 Expected b ("Foto tidak berubah") tidak menyebut cara mengamatinya; spec membandingkan sumber gambar avatar dengan baseline.
  - TC-GS-USER-351 Expected b ("Baris tetap Active") ambigu antara baris Blood Type tetap dalam mode edit dan user tetap berstatus Active; spec mengikuti arti mode edit (`[✓ Save]` dan `[✕ Cancel]` masih tampil), selaras PRD F-USER-17 (gagal: tetap Active).
  - TC-GS-USER-378 Expected b ("sempat menampilkan nilai baru (optimistic) lalu rollback ke state sebelum klik") tidak menyebut state awal checkbox Update `Manage TAG` dan cara mengamati nilai sementara; spec mencatat state awal sebagai baseline dan menahan respons lewat intercept supaya nilai baru teramati sebelum rollback.
  - TC-GS-USER-378 tidak menyebut role `Manage TAG` sudah ter-assign; checkbox role yang belum di-assign disabled (TC-GS-USER-1051), sehingga spec men-seed Ahmad Fauzi dengan `Manage TAG` ter-assign.
