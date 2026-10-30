---
id: TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role
title: "Resilience Tulis User: Cancel Pending Email Change, Pair dan Unpair TAG, Reset Authenticator, Ganti dan Hapus Foto Avatar, Inline Edit Custom Field, dan Auto-Save Tab Role Gagal 5xx dengan State Dikembalikan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-236
  - TC-GS-USER-320
  - TC-GS-USER-351
  - TC-GS-USER-330
  - TC-GS-USER-339
  - TC-GS-USER-342
  - TC-GS-USER-322
  - TC-GS-USER-378
coverage:
  web: automated
---

# Resilience Tulis User: Cancel Pending Email Change, Pair dan Unpair TAG, Reset Authenticator, Ganti dan Hapus Foto Avatar, Inline Edit Custom Field, dan Auto-Save Tab Role Gagal 5xx dengan State Dikembalikan

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness b: fault injection, bagian 3 prinsip 13 dan bagian 6 konvensi).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Division `Finance` (No. 23), produk `Fixed Asset` (No. 26), Custom Field Blood Type (No. 24), TAG `TAG-USR-0001` (user, aktif, bebas; No. 25), dan John Doe (No. 18, Activated, TAG `TAG-4F7K2XQ9` Verified) untuk TC-GS-USER-322. `TAG-4F7K2XQ9` hanya terpasang pada John Doe sehingga tidak dapat digandakan ke user seed; Unpair digagalkan intercept tanpa meneruskan request ke backend, sehingga TAG, Last Updated, dan Modified By John Doe tidak berubah.
- Berkas foto uji (fixture berkas, disediakan tim FE): `john3.png` (TC-GS-USER-339).
- Data Dinamis, di-seed lewat API di hook `before` (HK1), Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Rina Putri {runId}-068`, Email `rinaputri+{runId}-068@qwertysystem.net`, email pending `rinaputri.new+{runId}-068@qwertysystem.net` (target TC-GS-USER-236).
  - `Dewi Lestari {runId}-068`, Email `dewilestari+{runId}-068@qwertysystem.net`, tanpa TAG (badge `Unverified`), Blood Type `A` (target TC-GS-USER-320 dan 351).
  - `John Doe {runId}-068`, Email `johndoe+{runId}-068@qwertysystem.net`, MFA Enrolled, foto profil berkas `john-{runId}-068.png` (target TC-GS-USER-330, 339, dan 342).
  - `Ahmad Fauzi {runId}-068`, Email `ahmadfauzi+{runId}-068@qwertysystem.net`, tanpa assignment role `Manage TAG` (target TC-GS-USER-378).
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Semua jawaban 5xx (500) diberikan tanpa meneruskan request ke backend, dan tiap intercept dilepas segera setelah toast hasilnya tampil:
  - Respons Cancel Pending Email Change (TC-GS-USER-236).
  - Respons Pair TAG (TC-GS-USER-320).
  - Respons update Custom Field (TC-GS-USER-351).
  - Respons Reset Authenticator (TC-GS-USER-330).
  - Respons ganti foto (TC-GS-USER-339) dan respons hapus foto (TC-GS-USER-342).
  - Respons Unpair TAG (TC-GS-USER-322).
  - Respons update permission Tab Role (TC-GS-USER-378).
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Seeding user Activated dengan email pending, MFA Enrolled, foto profil berkas `john-{runId}-068.png`, dan nilai Custom Field Blood Type lewat API.
  - Simulasi RFID reader tersambung dan simulasi scan TAG `TAG-USR-0001` pada tombol `Scan TAG` (HK7); TC-GS-USER-320 berstatus Manual Only di TC.
  - Membaca sumber gambar avatar untuk dibandingkan dengan baseline, dan membaca state centang checkbox Tab Role.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah, tanpa mengandalkan setup berhasil penuh): lepas semua intercept; hapus lewat API keempat user seed dan berkas `john-{runId}-068.png`; kembalikan sesi ke akun default suite.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `{runId}-068`, tekan Enter

### TC-GS-USER-236: Cancel Pending Email Change gagal 5xx

3. Pasang intercept pada respons Cancel Pending Email Change: jawab 5xx
4. Klik (⋯) baris `Rina Putri {runId}-068` → `Edit`
5. Klik Button Cancel di samping label pending
6. Klik `[Cancel Change]`
7. Verifikasi toast error: "Error, failed to cancel email change."
8. Lepas intercept respons Cancel Pending Email Change
9. Verifikasi label `Pending email change to rinaputri.new+{runId}-068@qwertysystem.net` tetap tampil
10. Verifikasi Button Cancel di samping label pending tetap tampil
11. Klik `[Go Back]` pada dialog Cancel Pending Email Change
12. Klik `✕` pada header Popup Edit
13. Verifikasi badge `Pending Email Confirmation` tetap tampil pada baris `Rina Putri {runId}-068` di User List

### TC-GS-USER-320: Pair TAG dari Detail gagal server

14. Klik Name `Dewi Lestari {runId}-068` di User List
15. Pasang intercept pada respons Pair TAG: jawab 5xx
16. Klik `Scan TAG` pada sub-section User TAG
17. Scan `TAG-USR-0001` pada RFID reader (simulasi)
18. Verifikasi toast error: "Error, failed to pair TAG."
19. Lepas intercept respons Pair TAG
20. Verifikasi Badge sub-section User TAG tetap `Unverified`

### TC-GS-USER-351: Inline edit Custom Field gagal server

21. Pasang intercept pada respons update Custom Field: jawab 5xx
22. Hover baris Blood Type, klik icon edit
23. Pilih `O`
24. Klik `[✓ Save]`
25. Verifikasi toast error: "Error, failed to update Blood Type."
26. Lepas intercept respons update Custom Field
27. Verifikasi baris Blood Type tetap Active (mode edit dengan dropdown, `[✓ Save]`, dan `[✕ Cancel]`)
28. Klik `[✕ Cancel]` pada baris Blood Type

### TC-GS-USER-330: Reset Authenticator gagal server

29. Klik menu User di sidebar Global Settings
30. Klik icon Search, ketik `{runId}-068`, tekan Enter
31. Klik Name `John Doe {runId}-068` di User List
32. Pasang intercept pada respons Reset Authenticator: jawab 5xx
33. Klik `Reset Authenticator`
34. Klik `[Reset]`
35. Verifikasi toast error: "Error, failed to reset authenticator for John Doe {runId}-068."
36. Lepas intercept respons Reset Authenticator
37. Verifikasi Badge status authenticator tetap `Enrolled`
38. Klik `[Cancel]` pada dialog Reset Authenticator

### TC-GS-USER-339: Ganti foto dari Detail gagal server

39. Catat sumber gambar avatar `John Doe {runId}-068` di header Detail sebagai baseline avatar
40. Pasang intercept pada respons ganti foto: jawab 5xx
41. Hover Avatar lalu klik `[Edit]`
42. Pilih file `john3.png`
43. Verifikasi toast error: "Error, failed to update photo."
44. Lepas intercept respons ganti foto
45. Verifikasi sumber gambar avatar sama dengan baseline avatar (foto tidak berubah)

### TC-GS-USER-342: Delete foto dari Detail gagal server

46. Pasang intercept pada respons hapus foto: jawab 5xx
47. Hover Avatar lalu klik `[Delete]`
48. Klik `[Remove]`
49. Verifikasi toast error: "Error, failed to remove photo."
50. Lepas intercept respons hapus foto
51. Verifikasi sumber gambar avatar sama dengan baseline avatar (foto tidak berubah)
52. Klik `[Cancel]` pada dialog Remove Photo

### TC-GS-USER-322: Unpair TAG dari Detail gagal server

53. Klik menu User di sidebar Global Settings
54. Klik icon Search, ketik `John Doe`, tekan Enter
55. Klik Name `John Doe` di User List
56. Pasang intercept pada respons Unpair TAG: jawab 5xx
57. Klik `Unpair`
58. Klik `[Unpair]`
59. Verifikasi toast error: "Error, failed to unpair TAG."
60. Lepas intercept respons Unpair TAG
61. Verifikasi Badge sub-section User TAG tetap `Verified`
62. Klik `[Cancel]` pada dialog Unpair TAG

### TC-GS-USER-378: Tab Role, auto-save gagal mengembalikan checkbox

63. Klik menu User di sidebar Global Settings
64. Klik icon Search, ketik `{runId}-068`, tekan Enter
65. Klik Name `Ahmad Fauzi {runId}-068` di User List
66. Klik Tab `Role`
67. Catat state checkbox Update baris `Manage TAG` sebagai baseline checkbox
68. Pasang intercept pada respons update permission: jawab 5xx
69. Centang Update baris `Manage TAG`
70. Verifikasi toast error: "Error, failed to update permissions."
71. Lepas intercept respons update permission
72. Verifikasi checkbox Update baris `Manage TAG` kembali ke state baseline checkbox

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (72 langkah). Alasan: kedelapan TC berada di satu kelas harness (b, kegagalan 5xx aksi tulis di User List dan User Detail) dan satu akun; tiap blok TC berdiri sendiri (intercept sendiri, dilepas di dalam blok, user seed sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian langkah adalah navigasi antar user dan penutupan dialog konfirmasi.
- Urutan TC sumber diubah dan dikelompokkan per user target supaya Detail tidak dibuka berulang: TC-GS-USER-236 (popup Edit di User List), TC-GS-USER-320 dan 351 (Detail Dewi Lestari seed), TC-GS-USER-330, 339, dan 342 (Detail John Doe seed), TC-GS-USER-322 (Detail John Doe Pre-setup), TC-GS-USER-378 (Tab Role Ahmad Fauzi seed). Tidak ada TC yang menghapus data.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan layar, Search, memasang dan melepas intercept, mencatat baseline avatar dan checkbox, `[Go Back]`, `[Cancel]` yang menutup dialog konfirmasi, `✕` yang menutup Popup Edit (form tidak berubah sehingga tidak memunculkan `Unsaved Changes`), `[✕ Cancel]` yang mengakhiri mode edit inline, dan navigasi ke User List lewat menu User.
- Asersi "foto tidak berubah" (TC-GS-USER-339 dan 342) memakai satu baseline avatar yang dicatat sebelum aksi pertama di Detail John Doe seed; kedua aksi digagalkan intercept sehingga baseline yang sama berlaku untuk keduanya.
- Pembagian TC lintas spec: Cancel Pending Email Change sukses diverifikasi di spec 045, Pair dan Unpair TAG sukses di spec 057, Reset Authenticator sukses di spec 058, ganti dan hapus foto Detail sukses di spec 059, inline edit Custom Field sukses di spec 060, dan auto-save Tab Role sukses di spec 064; spec ini hanya memuat jalur kegagalan.
- Temuan untuk QA:
  - TC-GS-USER-236, 320, 322, 330, 339, 342, 351, dan 378 menulis precondition "dibuat gagal 5xx" (TC-GS-USER-236 menambah "mock/proxy") tanpa nama endpoint; spec memicu lewat `Spectra.intercept()` di atas backend nyata dan nama endpoint ditentukan tim FE di tahap script.
  - TC-GS-USER-320 berstatus Manual Only (scan RFID) tetapi tetap ditulis (bagian 2 konvensi); simulasi RFID reader dan scan TAG tidak punya mekanisme di TC, PRD, atau LLD dan disediakan tim FE/BE.
  - TC-GS-USER-322 memakai John Doe Pre-setup (TAG `TAG-4F7K2XQ9`) sebagai target aksi tulis; aksi digagalkan intercept tanpa meneruskan request sehingga tidak ada perubahan data. TAG yang sama tidak dapat dipasang pada user seed.
  - TC-GS-USER-236, 322, 330, dan 342 tidak menyebut apakah dialog konfirmasi tetap terbuka setelah kegagalan; spec mengikuti error-handling-convention bagian 2 (dialog tetap terbuka pada 5xx) dan menutupnya dengan `[Go Back]` atau `[Cancel]`.
  - TC-GS-USER-236 Expected b ("Label dan pending state tidak berubah") tidak merinci; spec mengasersi label pending, Button Cancel, dan badge `Pending Email Confirmation` di User List.
  - TC-GS-USER-339 dan 342 Expected b ("Foto tidak berubah") tidak menyebut cara mengamatinya; spec membandingkan sumber gambar avatar dengan baseline.
  - TC-GS-USER-351 Expected b ("Baris tetap Active") ambigu antara baris Blood Type tetap dalam mode edit dan user tetap berstatus Active; spec mengikuti arti mode edit (`[✓ Save]` dan `[✕ Cancel]` masih tampil), selaras PRD F-USER-17 (gagal: tetap Active).
  - TC-GS-USER-378 Expected b ("Checkbox kembali ke state sebelumnya") tidak menyebut state awal checkbox Update `Manage TAG` untuk Ahmad Fauzi; spec mencatat state itu sebagai baseline sebelum aksi.
