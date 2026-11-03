---
id: TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan
title: "Bulk Activate dan Deactivate: Dialog Satu Daftar dan Dua Kelompok, Baris yang Di-skip, Toast Ringkasan, Collapse ke Dialog Single, Cancel, dan Reset Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-291
  - TC-GS-USER-292
  - TC-GS-USER-293
  - TC-GS-USER-295
  - TC-GS-USER-296
  - TC-GS-USER-297
  - TC-GS-USER-298
  - TC-GS-USER-1027
  - TC-GS-USER-1035
  - TC-GS-USER-1036
  - TC-GS-USER-304
coverage:
  web: automated
---

# Bulk Activate dan Deactivate: Dialog Satu Daftar dan Dua Kelompok, Baris yang Di-skip, Toast Ringkasan, Collapse ke Dialog Single, Cancel, dan Reset Seleksi

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22) tidak dipakai sebagai target aksi dan tidak diubah.
- Data Dinamis, 16 user milik spec, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated, Division `Finance`, Access `Fixed Asset`, email `<name tanpa spasi huruf kecil>+{runId}-054@qwertysystem.net`:
  - Inactive manual (dapat diaktifkan), 12 user: `Jane Smith {runId}-054` (J1), `Ahmad Fauzi {runId}-054` (A1), `Jane Smith Dua {runId}-054` (J2), `Jane Smith Tiga {runId}-054` (J3), `Jane Smith Empat {runId}-054` (J4), `Jane Smith Lima {runId}-054` (J5), `Nonaktif 01 {runId}-054` sampai `Nonaktif 06 {runId}-054`.
  - Temporary-expired, Inactive: `Budi Hartono {runId}-054` (B1).
  - Active: `Dewi Lestari {runId}-054` (D1), `Dewi Lestari Dua {runId}-054` (D2), dan `Joko Susilo {runId}-054` (K; approver pada 2 approval yang menunggu dan memegang aset Borrowed, HK8; seeding approval in-flight dan aset Borrowed disediakan tim FE/BE).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus 16 user seed lewat API, bersihkan seleksi, kosongkan Search, tutup dialog.
- Kemampuan teknis: membaca isi dialog yang scrollable (12 nama); mengatur ukuran halaman 25 baris.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-054`, tekan Enter
2. Atur ukuran halaman menjadi 25 baris

### TC-GS-USER-291: Bulk Activate tanpa baris skip, dialog Activate Users satu daftar memuat seluruh nama tanpa diringkas

3. Centang 12 baris Inactive: `Jane Smith {runId}-054`, `Ahmad Fauzi {runId}-054`, `Jane Smith Dua {runId}-054`, `Jane Smith Tiga {runId}-054`, `Jane Smith Empat {runId}-054`, `Jane Smith Lima {runId}-054`, dan `Nonaktif 01 {runId}-054` sampai `Nonaktif 06 {runId}-054`
4. Klik `Bulk Action` lalu opsi `Activate`
5. Verifikasi Title dialog `Activate Users`
6. Verifikasi satu daftar bullet memuat 12 nama lengkap (tidak diringkas, tanpa dua kelompok): `Jane Smith {runId}-054`, `Ahmad Fauzi {runId}-054`, `Jane Smith Dua {runId}-054`, `Jane Smith Tiga {runId}-054`, `Jane Smith Empat {runId}-054`, `Jane Smith Lima {runId}-054`, `Nonaktif 01 {runId}-054` sampai `Nonaktif 06 {runId}-054`
7. Verifikasi body scrollable
8. Verifikasi body memuat `They will be activated across all products. Are you sure you want to activate them?`
9. Verifikasi tombol `[Cancel]` dan `[Activate]`
10. Klik `[Cancel]`
11. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-295: Bulk Activate 1 baris collapse ke dialog single

12. Centang baris `Jane Smith {runId}-054`
13. Klik `Bulk Action` lalu opsi `Activate`
14. Verifikasi dialog single memuat bullet `• Jane Smith {runId}-054`
15. Verifikasi dialog single memuat `This will activate user across all products. Are you sure you want to activate it?`
16. Klik `[Cancel]`
17. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-297: Bulk Deactivate 1 baris collapse ke dialog single

18. Centang baris `Dewi Lestari {runId}-054`
19. Klik `Bulk Action` lalu opsi `Deactivate`
20. Verifikasi Title dialog `Deactivate User`
21. Verifikasi body memuat bullet `• Dewi Lestari {runId}-054`
22. Verifikasi body memuat `This will deactivate user across all products. This user will be immediately logged out.`
23. Verifikasi body memuat `Are you sure you want to deactivate it?`
24. Verifikasi tombol `[Cancel]` dan `[Deactivate]`
25. Klik `[Cancel]`
26. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-298: Bulk dialog [Cancel] tidak mereset seleksi

27. Centang baris `Dewi Lestari {runId}-054` dan `Dewi Lestari Dua {runId}-054` (Active)
28. Klik `Bulk Action` lalu opsi `Deactivate`
29. Klik `[Cancel]`
30. Verifikasi dialog tertutup
31. Verifikasi 2 baris tetap tercentang
32. Verifikasi bar tetap tampil
33. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-1027: Bulk Activate dialog [Cancel] tidak mengaktifkan dan tidak mereset seleksi

34. Centang baris `Jane Smith {runId}-054` dan `Ahmad Fauzi {runId}-054` (Inactive)
35. Klik `Bulk Action` lalu opsi `Activate`
36. Klik `[Cancel]`
37. Verifikasi dialog tertutup
38. Verifikasi tidak ada toast
39. Verifikasi switch Active baris `Jane Smith {runId}-054` dan `Ahmad Fauzi {runId}-054` tetap OFF
40. Verifikasi kedua baris tetap tercentang
41. Verifikasi bar tetap tampil
42. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-292: Bulk Activate semua eligible sukses

43. Centang baris `Jane Smith {runId}-054` dan `Ahmad Fauzi {runId}-054` (Inactive)
44. Klik `Bulk Action` lalu opsi `Activate`
45. Klik `[Activate]`
46. Verifikasi toast sukses "Success, user has been activated."
47. Verifikasi switch Active baris `Jane Smith {runId}-054` dan `Ahmad Fauzi {runId}-054` ON
48. Verifikasi bar hilang
49. Verifikasi seleksi reset (kedua baris tidak tercentang)

### TC-GS-USER-293: Bulk Activate dengan baris Temporary-expired, baris itu di-skip dan toast ringkasan

50. Centang baris `Jane Smith Dua {runId}-054` dan `Budi Hartono {runId}-054` (Temporary-expired)
51. Klik `Bulk Action` lalu opsi `Activate`
52. Verifikasi Title dialog `Activate Users`
53. Verifikasi kelompok `The following will be activated across all products:` memuat bullet `• Jane Smith Dua {runId}-054`
54. Verifikasi kelompok `The following will be skipped (already active or temporary period ended):` memuat bullet `• Budi Hartono {runId}-054`
55. Verifikasi dialog ditutup `Are you sure you want to continue?`
56. Verifikasi tombol `[Cancel]` dan `[Continue]`
57. Klik `[Continue]`
58. Verifikasi toast "Success, user has been activated. Some items were skipped."
59. Verifikasi dialog `Reactivate Temporary User` tidak muncul
60. Verifikasi switch Active baris `Jane Smith Dua {runId}-054` ON
61. Verifikasi switch Active baris `Budi Hartono {runId}-054` tetap OFF

### TC-GS-USER-304: Setelah bulk action sukses, bar hilang dan seleksi reset termasuk baris yang di-skip

62. Centang baris `Jane Smith Tiga {runId}-054` dan `Budi Hartono {runId}-054`
63. Klik `Bulk Action` lalu opsi `Activate`
64. Klik `[Continue]`
65. Verifikasi bar hilang
66. Verifikasi kedua baris tidak tercentang (termasuk `Budi Hartono {runId}-054` yang di-skip)

### TC-GS-USER-1036: Bulk Activate dengan baris yang sudah Active, baris di-skip dan toast ringkasan

67. Centang baris `Dewi Lestari {runId}-054` (Active) dan `Jane Smith Empat {runId}-054` (Inactive)
68. Klik `Bulk Action` lalu opsi `Activate`
69. Verifikasi Title dialog `Activate Users`
70. Verifikasi kelompok `The following will be activated across all products:` memuat bullet `• Jane Smith Empat {runId}-054`
71. Verifikasi kelompok `The following will be skipped (already active or temporary period ended):` memuat bullet `• Dewi Lestari {runId}-054`
72. Verifikasi dialog ditutup `Are you sure you want to continue?`
73. Verifikasi tombol `[Cancel]` dan `[Continue]`
74. Klik `[Continue]`
75. Verifikasi toast "Success, user has been activated. Some items were skipped."
76. Verifikasi switch Active baris `Jane Smith Empat {runId}-054` ON
77. Verifikasi switch Active baris `Dewi Lestari {runId}-054` tetap ON

### TC-GS-USER-1035: Bulk Deactivate dengan baris yang sudah Inactive, baris di-skip dan toast ringkasan

78. Centang baris `Dewi Lestari {runId}-054` (Active) dan `Jane Smith Lima {runId}-054` (Inactive)
79. Klik `Bulk Action` lalu opsi `Deactivate`
80. Verifikasi Title dialog `Deactivate Users`
81. Verifikasi kelompok `The following will be deactivated across all products:` memuat bullet `• Dewi Lestari {runId}-054`
82. Verifikasi kelompok `The following will be skipped (already inactive):` memuat bullet `• Jane Smith Lima {runId}-054`
83. Verifikasi dialog ditutup `Are you sure you want to continue?`
84. Verifikasi tombol `[Cancel]` dan `[Continue]`
85. Klik `[Continue]`
86. Verifikasi toast "Success, user has been deactivated. Some items were skipped."
87. Verifikasi switch Active baris `Dewi Lestari {runId}-054` OFF
88. Verifikasi switch Active baris `Jane Smith Lima {runId}-054` tetap OFF

### TC-GS-USER-296: Bulk Deactivate tanpa baris skip, dialog Deactivate Users satu daftar dan hasil

89. Centang baris `Dewi Lestari Dua {runId}-054` dan `Joko Susilo {runId}-054`
90. Klik `Bulk Action` lalu opsi `Deactivate`
91. Verifikasi Title dialog `Deactivate Users`
92. Verifikasi satu daftar bullet `Dewi Lestari Dua {runId}-054` dan `Joko Susilo {runId}-054` (tanpa dua kelompok)
93. Verifikasi body memuat peringatan aset aktif `Joko Susilo {runId}-054 is currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under this user until manually transferred or returned.` (nama pada `[User Name]` diganti nama user)
94. Verifikasi body memuat baris approval in-flight `Pending approvals of this user will be reassigned to other approvers.`
95. Verifikasi body memuat `These users will be immediately logged out.`
96. Verifikasi body memuat `They will be deactivated across all products. Are you sure you want to deactivate them?`
97. Klik `[Deactivate]`
98. Verifikasi toast sukses "Success, user has been deactivated."
99. Verifikasi switch Active baris `Dewi Lestari Dua {runId}-054` dan `Joko Susilo {runId}-054` OFF

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (99 langkah) karena sebelas TC Bulk Activate dan Deactivate berada di satu kelas harness (fungsional), satu aksi (Bulk Action Activate/Deactivate), dan satu layar (User List dengan Search `{runId}-054`). Tiap blok berdiri sendiri pada seed sendiri (satu pasang atau satu kelompok user per TC), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah `Verifikasi` isi dialog yang diwajibkan S-01 (teks tiap kelompok, ditutup, tombol).
- Urutan TC sumber diubah: screening dan Cancel (TC-GS-USER-291, 295, 297, 298, 1027) di awal, lalu aksi sukses (TC-GS-USER-292, 293, 304, 1036, 1035, 296; bagian 3 prinsip 3). TC-GS-USER-1036 mendahului TC-GS-USER-1035 karena Dewi Lestari (Active) tetap Active pada TC-GS-USER-1036 dan dinonaktifkan pada TC-GS-USER-1035; TC-GS-USER-296 paling akhir karena menonaktifkan seed milik TC itu saja (`Dewi Lestari Dua`, `Joko Susilo`).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 dan 2 (Search dan ukuran halaman 25 baris supaya 16 baris seed tampil dalam satu halaman), 11, 17, 26, 33, 42 (membersihkan seleksi dengan icon `×`, S-09), 10, 16, 25 (menutup dialog dengan `[Cancel]` setelah screening).
- Langkah 59 ("dialog Reactivate Temporary tidak muncul", Expected TC-GS-USER-293 butir b) didahului toast pada langkah 58 sebagai pembanding bahwa dialog hasil sudah tampil dan ditutup (bagian 8b butir 2). Tidak ada asersi tambahan di luar Expected TC.
- Seed `Dewi Lestari Dua {runId}-054` ditambahkan karena Dewi Lestari dinonaktifkan di dua TC (TC-GS-USER-1035 dan TC-GS-USER-296) dan Joko Susilo hanya dinonaktifkan di TC-GS-USER-296. Seed Inactive dibuat 12 user karena TC-GS-USER-291 mensyaratkan 12 nama; enam di antaranya (`Jane Smith`, `Ahmad Fauzi`, `Jane Smith Dua` sampai `Lima`) dipakai pula oleh TC lain, yang dilakukan sesudah TC-GS-USER-291.
- Pembagian TC: Bulk Delete diverifikasi di spec 055; kegagalan server pada Bulk Activate dan Deactivate (5xx, sebagian gagal) diverifikasi di spec lain; log Bulk Activate dan Deactivate diverifikasi di spec pencatatan log.
- Temuan untuk QA:
  - TC-GS-USER-296 butir a menyebut peringatan aset aktif dan approval "hanya bila berlaku"; spec mengasersi peringatan aset aktif dan approval untuk Joko Susilo (memegang aset Borrowed dan approver) dan tidak mengasersi ketiadaannya pada Dewi Lestari Dua.
  - TC-GS-USER-295 butir tidak menyebut Title dialog single Activate; spec tidak mengasersi Title.
  - TC-GS-USER-291 tidak menyebut urutan nama dalam daftar bullet atau batas tinggi scroll; spec mengasersi 12 nama tanpa urutan dan body scrollable.
  - TC-GS-USER-293 butir b ("Dialog Reactivate Temporary tidak muncul") tidak menyebut kapan diamati (sebelum atau sesudah `[Continue]`); spec mengasersinya sesudah `[Continue]`.
  - TC-GS-USER-298 tidak menyebut dua baris Active yang dicentang; spec memakai `Dewi Lestari` dan `Dewi Lestari Dua`.
  - TC memakai Dewi Lestari, Jane Smith, Ahmad Fauzi, Joko Susilo, dan Budi Hartono Pre-setup sebagai target aksi tulis; spec memakai seed milik spec.
  - TC-GS-USER-292, 293, 296, 1035, 1036, dan 304 tanpa Post Condition; TC-GS-USER-291, 295, 297, 298, dan 1027 tanpa Post Condition.
