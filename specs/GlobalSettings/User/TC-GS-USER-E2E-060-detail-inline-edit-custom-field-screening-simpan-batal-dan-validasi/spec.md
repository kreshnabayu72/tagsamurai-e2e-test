---
id: TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi
title: "User Detail: Section Custom Fields (Screening, Collapse, Format Phone, Inline Edit Simpan, Batal, Multi-aktif, Validasi Required dan Min. 4 Characters, Saving State, Akun Sendiri, dan Holder Update-Only)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-344
  - TC-GS-USER-345
  - TC-GS-USER-346
  - TC-GS-USER-347
  - TC-GS-USER-348
  - TC-GS-USER-349
  - TC-GS-USER-350
  - TC-GS-USER-352
  - TC-GS-USER-354
  - TC-GS-USER-355
  - TC-GS-USER-1077
coverage:
  web: automated
---

# User Detail: Section Custom Fields (Screening, Collapse, Format Phone, Inline Edit Simpan, Batal, Multi-aktif, Validasi Required dan Min. 4 Characters, Saving State, Akun Sendiri, dan Holder Update-Only)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk menahan respons update field pada TC-GS-USER-352).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`. Akun kedua (ganti akun eksplisit di TC-GS-USER-355): Manage user and role Update-Only (Bayu Saputra) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 6; kredensial `Spectra.env.GS_UPDATE_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` dan `GS_UPDATE_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 24): Custom Field aktif Blood Type (Dropdown A/B/O/AB), Skills (Multi-Dropdown Excel/SQL), dan Emergency Phone (Phone; Required aktif untuk TC-GS-USER-349 dan 344, TC lain dijalankan saat Required nonaktif). Definisi Custom Field dibaca dan tidak diubah; hanya status Required Emergency Phone yang diatur (lihat State global). Akun aktor Siti Nurhaliza (No. 2) diubah Blood Type-nya di TC-GS-USER-354 (target Edit-nya adalah akun sendiri, sehingga tidak dapat diganti user seed tanpa ganti akun); nilai awal dicatat di hook `before` dan dipulihkan di hook `after`; Last Updated dan Modified By Siti Nurhaliza tidak dapat dipulihkan dan berubah.
- Data Dinamis, di-seed lewat API di hook `before` (HK1), Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Dewi Lestari {runId}-060`, Email `dewilestari+{runId}-060@qwertysystem.net`: Blood Type `A`, Skills kosong, Emergency Phone kosong (Required, dikosongkan lewat API seeding) (TC-GS-USER-344, 345, 350, 347, 348, 346, 352, dan 355).
  - `Dewi Lestari B {runId}-060`, Email `dewilestarib+{runId}-060@qwertysystem.net`: Blood Type `A`, Skills kosong, Emergency Phone tersimpan dengan Country Code `🇮🇩 +62` dan Number `81234567890` (TC-GS-USER-1077 dan 349).
- Kemampuan teknis, disediakan tim FE:
  - Seeding nilai Custom Field (termasuk Emergency Phone Required yang kosong) pada user seed lewat API, dan membaca serta memulihkan Blood Type akun Siti Nurhaliza.
  - Intercept (`Spectra.intercept()`) menahan respons update field pada TC-GS-USER-352; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Intercept dilepas segera setelah state saving diamati.
- State global yang diubah: status Required Custom Field `Emergency Phone`: aktif untuk TC-GS-USER-349 (langkah 6 sampai 13) dan TC-GS-USER-344 (langkah 16 sampai 25), nonaktif untuk TC lain sesuai Tabel Pre-setup No. 24. Status dinyalakan dan dimatikan oleh langkah penghubung eksplisit (langkah 6, 14, 16, dan 26) lewat kemampuan fixture yang disediakan tim FE/BE (bukan aksi UI), dan hook `before` mencatat status awal. Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya. TC-GS-USER-344 Expected d mengharapkan alert `⚠ "Emergency phone is required."` yang hanya muncul bila Required aktif, sehingga Required dinyalakan untuk TC itu, berbeda dari Pre-setup No. 24 (lihat Notes, Temuan untuk QA). Hook `after` (tetap berjalan walau spec gagal di tengah) melepas intercept, memulihkan Blood Type Siti Nurhaliza, menghapus dua user seed, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-1077: Section Custom Fields menampilkan nilai Phone terisi sebagai [+CountryCode] [Number]

3. Klik Name `Dewi Lestari B {runId}-060` di User List
4. Verifikasi baris Emergency Phone menampilkan `Emergency Phone: +62 81234567890` (Country Code dan Number dipisah satu spasi)
5. Verifikasi baris Emergency Phone tidak menampilkan nilai tanpa spasi `+6281234567890`

### TC-GS-USER-349: Inline edit Custom Field Required dikosongkan lalu Save ditolak

6. Nyalakan status Required Custom Field `Emergency Phone` (fixture FE/BE, bukan aksi UI)
7. Hover baris Emergency Phone, klik icon edit
8. Kosongkan isian Number Emergency Phone
9. Klik `[✓ Save]`
10. Verifikasi inline error `Emergency phone must not be empty`
11. Verifikasi baris Emergency Phone tetap Active
12. Klik `[✕ Cancel]` pada baris Emergency Phone
13. Verifikasi Display `Emergency Phone: +62 81234567890` (nilai tersimpan tidak berubah)
14. Matikan status Required Custom Field `Emergency Phone` (fixture FE/BE, bukan aksi UI)

### TC-GS-USER-344: Screening Section Custom Fields

15. Kembali ke User List dengan klik Back
16. Nyalakan status Required Custom Field `Emergency Phone` (fixture FE/BE, bukan aksi UI)
17. Klik Name `Dewi Lestari {runId}-060` di User List
18. Verifikasi Section Custom Fields collapsible dengan grid 2 kolom `Label: Value`
19. Verifikasi `Blood Type: A`
20. Verifikasi `Skills: —`
21. Verifikasi icon edit baris Skills tidak tampil
22. Verifikasi baris Emergency Phone menampilkan alert `⚠ "Emergency phone is required."` menggantikan `—`
23. Verifikasi icon edit baris Emergency Phone langsung tampil
24. Hover baris Skills
25. Verifikasi icon edit baris Skills tampil
26. Matikan status Required Custom Field `Emergency Phone` (fixture FE/BE, bukan aksi UI)

### TC-GS-USER-345: Section Custom Fields dapat di-collapse dan di-expand

27. Klik header Section Custom Fields
28. Verifikasi Section Custom Fields tertutup
29. Klik header Section Custom Fields lagi
30. Verifikasi Section Custom Fields terbuka kembali

### TC-GS-USER-350: Inline edit Custom Field melanggar rule Data Type ditolak

31. Klik icon edit baris Emergency Phone
32. Ketik `081` pada isian Number Emergency Phone
33. Klik `[✓ Save]`
34. Verifikasi inline error `Min. 4 characters`
35. Verifikasi baris Emergency Phone tetap Active
36. Klik `[✕ Cancel]` pada baris Emergency Phone

### TC-GS-USER-347: Inline edit Custom Field [✕ Cancel] mengembalikan nilai lama tanpa request

37. Hover baris Blood Type, klik icon edit
38. Pilih `B`
39. Klik `[✕ Cancel]` pada baris Blood Type
40. Verifikasi Display kembali `Blood Type: A`
41. Verifikasi tidak ada toast

### TC-GS-USER-348: Inline edit beberapa Custom Field aktif bersamaan secara independen

42. Hover baris Blood Type, klik icon edit
43. Hover baris Skills, klik icon edit
44. Verifikasi baris Blood Type dan baris Skills Active bersamaan
45. Pilih `Excel` pada Skills
46. Klik `[✓ Save]` pada baris Skills
47. Tunggu aksi selesai (baris Skills kembali Display)
48. Verifikasi baris Blood Type masih Active
49. Klik `[✕ Cancel]` pada baris Blood Type

### TC-GS-USER-346: Inline edit Custom Field sukses

50. Hover baris Blood Type, klik icon Edit2Line
51. Verifikasi baris Blood Type Active dengan dropdown, `[✓ Save]`, dan `[✕ Cancel]`
52. Pilih `O`
53. Klik `[✓ Save]`
54. Verifikasi toast sukses: "Success, Blood Type has been updated."
55. Verifikasi Display `Blood Type: O`

### TC-GS-USER-352: Inline edit Custom Field, saving state menonaktifkan widget

56. Pasang intercept pada respons update field: tahan respons
57. Hover baris Blood Type, klik icon edit
58. Pilih `AB`
59. Klik `[✓ Save]`
60. Verifikasi widget baris Blood Type disabled selama saving
61. Verifikasi icon baris Blood Type disabled selama saving
62. Lepas intercept respons update field sehingga respons diteruskan
63. Tunggu aksi selesai (baris Blood Type kembali Display)

### TC-GS-USER-354: Inline edit Custom Field akun sendiri enabled

64. Kembali ke User List dengan klik Back
65. Klik Name `Siti Nurhaliza` di User List
66. Hover baris Blood Type
67. Verifikasi icon edit tampil dan enabled
68. Klik icon edit
69. Pilih nilai Blood Type yang berbeda dari nilai awal akun yang dicatat di hook `before`
70. Klik `[✓ Save]`
71. Verifikasi Display Blood Type menampilkan nilai baru yang tersimpan

### TC-GS-USER-355: Inline edit Custom Field sukses oleh holder Update-Only terhadap target Normal

72. Logout dari akun Total Control, lalu login sebagai Bayu Saputra (Manage user and role Update-Only: R+U) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.GS_UPDATE_PASSWORD`
73. Buka Global Settings > User > User List (sub-tab Login User)
74. Pilih 100 baris per halaman pada Pagination
75. Klik Name `Dewi Lestari {runId}-060` di User List
76. Hover baris Blood Type, klik icon edit
77. Pilih `B`
78. Klik `[✓ Save]`
79. Verifikasi toast sukses: "Success, Blood Type has been updated."

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (79 langkah). Alasan: seluruh blok satu kelas (fungsional) dan satu layar (Section Custom Fields di User Detail); pembukaan Detail dan ganti akun dipakai bersama; tiap blok mengubah satu baris Custom Field sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-1077 dan 349 (user `Dewi Lestari B {runId}-060` dengan Emergency Phone terisi) dikerjakan di awal supaya Detail user itu dibuka satu kali; screening (TC-GS-USER-344, 345) di awal user `Dewi Lestari {runId}-060` sebelum aksi edit; validasi diblokir (TC-GS-USER-350) sebelum aksi sukses; TC-GS-USER-347 sebelum TC-GS-USER-348 dan 346 supaya Blood Type masih `A`; TC-GS-USER-354 dan 355 (ganti akun) paling akhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6, 14, 16, dan 26 (menyalakan dan mematikan Required `Emergency Phone` lewat kemampuan tim FE/BE, bukan aksi UI), pembukaan layar, Back ke User List, `[✕ Cancel]` setelah inline error dan setelah TC-GS-USER-348, pasang dan lepas intercept, "Tunggu aksi selesai", dan ganti akun ke Bayu Saputra. Langkah Hover baris sebelum klik icon edit menyatakan cara icon edit tampil.
- TC-GS-USER-349: `[✕ Cancel]` dan `Verifikasi` Display `Emergency Phone: +62 81234567890` menyatakan "nilai tersimpan tidak berubah" (Expected b).
- Nilai TC-GS-USER-352 diubah dari `O` ke `AB` karena `Blood Type` sudah `O` setelah TC-GS-USER-346; TC tidak menyebut precondition nilai awal.
- Alert `⚠ "Emergency phone is required."` ditulis persis seperti Expected TC, termasuk tanda kutip ganda.
- Temuan untuk QA:
  - TC-GS-USER-344: precondition c dan Expected d mengharapkan alert `⚠ "Emergency phone is required."` pada Emergency Phone kosong (Required), sedangkan Tabel Pre-setup No. 24 menyatakan Required hanya aktif untuk TC-GS-USER-158 dan 349. Spec mengikuti TC (langkah 22 tetap) dan menyalakan Required sebelum TC ini (langkah 16; keputusan: TC-GS-USER-344 masuk Required aktif); Pre-setup No. 24 perlu disesuaikan tim TC.
  - TC-GS-USER-344 dan 349: Emergency Phone kosong (344) dan terisi `081234567890` (349) pada Dewi Lestari yang sama; Tabel Pre-setup menyebut Emergency Phone kosong. Spec memakai dua user seed (`Dewi Lestari {runId}-060` kosong dan `Dewi Lestari B {runId}-060` terisi).
  - TC-GS-USER-349 dan 1077: nilai Emergency Phone `081234567890` (349) dan Country Code `+62` dengan Number `81234567890` (1077) berbeda representasi (angka 0 di depan); spec memakai satu user seed (`+62 81234567890`) untuk keduanya.
  - TC-GS-USER-354: precondition tidak menyebut nilai awal Blood Type akun sendiri maupun nilai yang dipilih; spec memilih nilai berbeda dari nilai awal dan memulihkannya di hook `after`.
  - TC-GS-USER-354: Tipe tertulis Negative, padahal Expected adalah aksi berhasil.
  - TC-GS-USER-352: precondition "Response update field ditahan" tidak menyebut cara menahan respons; disediakan tim FE lewat intercept.
  - TC-GS-USER-347: judul menyebut "tanpa request", tetapi Expected tidak mengasersi request; spec hanya mengasersi Display `Blood Type: A` dan tidak ada toast.
  - TC-GS-USER-348: langkah 4 "Save Skills saja" tidak menyebut nilai Skills; spec memakai `Excel`.
  - TC-GS-USER-355: Expected hanya menyebut toast; spec tidak menambah asersi Display.
  - TC-GS-USER-350: Number `081` (3 karakter) menghasilkan `Min. 4 characters`; aturan Min. 4 characters terhadap Number berikut kode negara tidak dijelaskan di TC.
