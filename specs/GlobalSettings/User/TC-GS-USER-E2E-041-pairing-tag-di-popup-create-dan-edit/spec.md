---
id: TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit
title: "Pairing TAG di Popup Create dan Edit: Scan Ditolak, Scan Valid Verified, Unpair, Cancel Unpair, dan Re-pair"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-131
  - TC-GS-USER-132
  - TC-GS-USER-133
  - TC-GS-USER-134
  - TC-GS-USER-135
  - TC-GS-USER-136
  - TC-GS-USER-209
  - TC-GS-USER-210
  - TC-GS-USER-211
coverage:
  web: automated
---

# Pairing TAG di Popup Create dan Edit: Scan Ditolak, Scan Valid Verified, Unpair, Cancel Unpair, dan Re-pair

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Client: PT Maju Bersama, plan Growth (Tabel Data Uji Pre-setup No. 26), sehingga field `User TAG` dirender.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 25 dan No. 18):
  - `TAG-USR-0001` (TAG user, aktif, bebas; hook `before` memastikan tidak terpasang ke user mana pun), `TAG-4F7K2XQ9` (terpasang ke John Doe), `TAG-OBJ-0001` (object TAG), `TAG-NEW-0001` (belum diaktivasi).
  - `TAG-EXT-9999` bukan produk TAG Samurai (tidak terdaftar di TAG Registry).
  - John Doe (No. 18): Activated, TAG `TAG-4F7K2XQ9`. John Doe diedit spec ini (unpair lalu re-pair `TAG-USR-0001`) karena TC mengunci TAG dan user ini (S-06); hook `after` memulihkan pairing `TAG-4F7K2XQ9` ke John Doe dan membebaskan `TAG-USR-0001`. Efek yang tidak dapat dipulihkan: kolom Last Update dan Modified By baris John Doe berubah.
- Pemulihan pairing John Doe merujuk fixture pemulihan di `suite.md` ("Pemulihan data Pre-setup yang ditulis spec").
- Data Dinamis: First Name `Pairing` dan Last Name `Tester {runId}-041` (nama gabungan `Pairing Tester {runId}-041`; hanya diketik di Popup Create, tidak pernah di-submit; tidak ada data tercipta).
- Kemampuan teknis (disediakan tim FE/BE):
  - Simulasi scan TAG: perangkat RFID reader dianggap tersambung dan ID TAG disuntikkan ke aplikasi seolah-olah dipindai (`TAG-NEW-0001`, `TAG-4F7K2XQ9`, `TAG-OBJ-0001`, `TAG-EXT-9999`, `TAG-USR-0001`); simulasi menahan hasil scan sampai langkah "Scan ..." dijalankan sehingga indikator loading tombol `Scan TAG` teramati.
  - Pemulihan pairing John Doe di hook `after` lewat API (nama endpoint ditentukan tim FE di tahap script).
  - Setup Column User List: kolom `TAG` ditampilkan lewat modal Setup Column pada langkah spec dan disembunyikan lagi; hook `after` mengembalikan kolom ke default.
- State global: pairing John Doe, preferensi kolom User List. Suite berjalan serial (`parallel: false`, lihat `suite.md`); dipulihkan di hook `after`.

## Test Steps

### Pembukaan Popup Create

1. Klik `[+ User]` di Table Tools

### TC-GS-USER-131: Scan TAG-NEW-0001 (belum diaktivasi) ditolak

2. Klik `Scan TAG`
3. Scan `TAG-NEW-0001`
4. Verifikasi toast error: "This TAG hasn't been activated yet. Please contact Admin."
5. Verifikasi badge tetap `Unverified` (warning)
6. Verifikasi button `Unpair` tidak muncul
7. Tunggu toast hilang

### TC-GS-USER-132: Scan TAG-4F7K2XQ9 (sudah dipasang ke John Doe) ditolak

8. Klik `Scan TAG`
9. Scan `TAG-4F7K2XQ9`
10. Verifikasi toast error: "Error, RFID TAG is already paired to another user."
11. Verifikasi badge tetap `Unverified` (warning)
12. Verifikasi button `Unpair` tidak muncul
13. Tunggu toast hilang

### TC-GS-USER-133: Scan TAG-OBJ-0001 (object TAG) ditolak

14. Klik `Scan TAG`
15. Scan `TAG-OBJ-0001`
16. Verifikasi toast error: "Error, the scanned TAG is object TAG."
17. Verifikasi badge tetap `Unverified` (warning)
18. Verifikasi button `Unpair` tidak muncul
19. Tunggu toast hilang

### TC-GS-USER-134: Urutan cek TAG, belum diaktivasi dilaporkan lebih dulu

20. Klik `Scan TAG`
21. Scan `TAG-EXT-9999`
22. Verifikasi toast error: "This TAG hasn't been activated yet. Please contact Admin."
23. Verifikasi hanya satu toast error yang tampil (bukan dua cek)
24. Tunggu toast hilang

### TC-GS-USER-135: Scan TAG valid mengubah badge jadi Verified dan memunculkan Unpair

25. Klik `Scan TAG`
26. Verifikasi tombol `Scan TAG` menampilkan loading indicator selama scan berlangsung
27. Scan `TAG-USR-0001`
28. Verifikasi badge `Verified` (success)
29. Verifikasi tombol `Scan TAG` tampil
30. Verifikasi button `Unpair` tampil
31. Verifikasi susunan satu baris dari kiri ke kanan: tombol `Scan TAG`, badge `Verified` (success) di kanan tombol, lalu `Unpair`
32. Verifikasi belum ada toast

### TC-GS-USER-136: Unpair TAG yang baru di-scan di form mengembalikan badge Unverified

33. Isi First Name `Pairing` dan Last Name `Tester {runId}-041`
34. Klik `Unpair`
35. Verifikasi dialog Title `Unpair TAG`
36. Verifikasi body dialog memuat bullet nama sesuai First Name dan Last Name yang diisi (`Pairing Tester {runId}-041`)
37. Verifikasi body dialog memuat `This will unpair the TAG from this user.` dan `Are you sure you want to unpair it?`
38. Verifikasi dialog memuat tombol `[Cancel]` dan `[Unpair]`
39. Klik `[Unpair]` pada dialog
40. Verifikasi badge kembali `Unverified` (warning) di kanan tombol `Scan TAG`
41. Verifikasi button `Unpair` tidak muncul
42. Klik `✕` pada header Popup Create
43. Verifikasi dialog `Unsaved Changes`
44. Klik `[Leave]`

### TC-GS-USER-210 dan TC-GS-USER-209: Edit John Doe, Cancel Unpair lalu Unpair tersimpan saat Save

45. Klik icon Search, ketik `John Doe`, tekan Enter
46. Klik header kolom Column Visibility (⋯) → `Setup Column...`, centang kolom `TAG`, klik `[Save]`
47. Klik (⋯) baris John Doe → `Edit`
48. Klik `Unpair`
49. Klik `[Cancel]` pada dialog
50. Verifikasi badge tetap `Verified`
51. Verifikasi TAG `TAG-4F7K2XQ9` tetap tampil
52. Klik `Unpair`
53. Klik `[Unpair]` pada dialog
54. Verifikasi badge `Unverified` setelah dialog
55. Klik `[Save]`
56. Verifikasi toast sukses: "Success, user has been updated."
57. Verifikasi hanya satu toast yang tampil (tanpa toast unpair terpisah)
58. Verifikasi kolom TAG baris John Doe bernilai `—`

### TC-GS-USER-211: Re-pair TAG lain lalu Save

59. Klik (⋯) baris John Doe → `Edit`
60. Klik `Scan TAG`
61. Scan `TAG-USR-0001`
62. Verifikasi badge `Verified`
63. Verifikasi TAG `TAG-USR-0001` tampil
64. Klik `[Save]`
65. Verifikasi toast sukses: "Success, user has been updated."
66. Klik header kolom Column Visibility (⋯) → `Setup Column...`, hilangkan centang kolom `TAG`, klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness d (simulasi scan TAG); seluruh TC di spec ini memakai harness yang sama.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (66 langkah) karena sembilan TC berada di satu kelas harness (pairing TAG dengan simulasi scan); blok Create (TC-GS-USER-131 sampai 136) memakai satu pembukaan Popup Create dan blok Edit (TC-GS-USER-210, 209, 211) memakai pembukaan Popup Edit sendiri, sehingga tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-210 mendahului TC-GS-USER-209 dalam satu pembukaan Popup Edit (Cancel Unpair, lalu Unpair dikonfirmasi dan di-Save), karena aksi Unpair TC-GS-USER-209 menghapus TAG yang dibutuhkan TC-GS-USER-210. TC-GS-USER-211 berada sesudah TC-GS-USER-209 karena John Doe sudah tidak memegang TAG. Blok Create mendahului blok Edit karena TC-GS-USER-132 mengasersi `TAG-4F7K2XQ9` masih terpasang ke John Doe.
- TC-GS-USER-136 langkah 2 (scan `TAG-USR-0001`) dipenuhi oleh scan TC-GS-USER-135 pada Popup Create yang sama (langkah 27).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (pembukaan), 7, 13, 19, 24 (menunggu toast hilang agar asersi toast berikutnya tidak tercampur), 33 (mengisi First Name dan Last Name agar bullet nama dialog Unpair terisi), 42 sampai 44 (menutup Popup Create dirty lewat `✕`, dialog `Unsaved Changes`, `[Leave]`, S-08), 45 (Search John Doe), 46 dan 66 (menampilkan dan menyembunyikan kolom `TAG` yang default tersembunyi).
- Popup Create hanya berisi First Name, Last Name, dan TAG yang di-stage; tidak ada submit, sehingga tidak ada user baru tercipta.
- Langkah 5, 11, 17 menjadi anchor positif untuk absence `Unpair` (langkah 6, 12, 18): badge `Unverified` dan tombol `Scan TAG` tampil di surface yang sama.
- Temuan untuk QA:
  - TC-GS-USER-131 sampai 136 berstatus `Manual Only` di TC (butuh RFID reader); spec memintanya dijalankan lewat simulasi scan yang disediakan tim FE/BE.
  - TC-GS-USER-136 tidak mengisi nama pada Popup Create sedangkan Expected a menyebut "body bullet nama"; Form Create hanya punya First Name dan Last Name (tidak ada field Name; langkah spec sebelumnya menulis "Isi Name"); spec mengisi First Name `Pairing` dan Last Name `Tester {runId}-041` sebelum Unpair, dan bullet nama dialog diasumsikan menampilkan nama gabungan keduanya (format bullet tidak disebut TC).
  - TC-GS-USER-209 Post Condition "TAG-4F7K2XQ9 tersedia lagi di TAG Registry" tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-USER-209 menyebut kolom TAG John Doe `—` padahal kolom curated `TAG` default tersembunyi (TC-GS-USER-1); spec menampilkannya lewat Setup Column.
  - TC-GS-USER-209 mengubah John Doe (Pre-setup No. 18) dan TC-GS-USER-211 memasang `TAG-USR-0001`; tidak ada user Pre-setup lain yang memegang `TAG-4F7K2XQ9`, sehingga pemulihan di `after` disediakan tim FE/BE.
  - TC-GS-USER-131 sampai 133 menyebut "Button `Unpair` tidak muncul" tanpa menyebut keadaan awal sebelum scan; spec mengasersinya sesudah scan ditolak.
- REVIEW C19 diterima (2026-11-03): langkah 23 dan 57 menghitung toast dari aksi yang sama dengan toast yang baru diverifikasi satu langkah sebelumnya; tidak ada toast lama yang tersisa, dan langkah "Tunggu toast lama hilang" justru membuat toast yang dihitung ikut hilang sebelum diasersi.
