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
- Data Pre-setup (Tabel Data Uji Pre-setup No. 24): Custom Field aktif Blood Type (Dropdown A/B/O/AB), Skills (Multi-Dropdown Excel/SQL), dan Emergency Phone (Phone, Required), dibaca dan tidak diubah. Akun aktor Siti Nurhaliza (No. 2) diubah Blood Type-nya di TC-GS-USER-354 (target Edit-nya adalah akun sendiri, sehingga tidak dapat diganti user seed tanpa ganti akun); nilai awal dicatat di hook `before` dan dipulihkan di hook `after`; Last Updated dan Modified By Siti Nurhaliza tidak dapat dipulihkan dan berubah.
- Data Dinamis, di-seed lewat API di hook `before` (HK1), Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Dewi Lestari {runId}-060`, Email `dewilestari+{runId}-060@qwertysystem.net`: Blood Type `A`, Skills kosong, Emergency Phone kosong (Required, dikosongkan lewat API seeding) (TC-GS-USER-344, 345, 350, 347, 348, 346, 352, dan 355).
  - `Dewi Lestari B {runId}-060`, Email `dewilestarib+{runId}-060@qwertysystem.net`: Blood Type `A`, Skills kosong, Emergency Phone tersimpan dengan Country Code `🇮🇩 +62` dan Number `81234567890` (TC-GS-USER-1077 dan 349).
- Kemampuan teknis, disediakan tim FE:
  - Seeding nilai Custom Field (termasuk Emergency Phone Required yang kosong) pada user seed lewat API, dan membaca serta memulihkan Blood Type akun Siti Nurhaliza.
  - Intercept (`Spectra.intercept()`) menahan respons update field pada TC-GS-USER-352; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Intercept dilepas segera setelah state saving diamati.
- State global yang diubah: tidak ada. Hook `after` (tetap berjalan walau spec gagal di tengah) melepas intercept, memulihkan Blood Type Siti Nurhaliza, menghapus dua user seed, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-1077: Section Custom Fields menampilkan nilai Phone terisi sebagai [+CountryCode] [Number]

3. Klik Name `Dewi Lestari B {runId}-060` di User List
4. Verifikasi baris Emergency Phone menampilkan `Emergency Phone: +62 81234567890` (Country Code dan Number dipisah satu spasi)
5. Verifikasi baris Emergency Phone tidak menampilkan nilai tanpa spasi `+6281234567890`

### TC-GS-USER-349: Inline edit Custom Field Required dikosongkan lalu Save ditolak

6. Hover baris Emergency Phone, klik icon edit
7. Kosongkan isian Number Emergency Phone
8. Klik `[✓ Save]`
9. Verifikasi inline error `Emergency phone must not be empty`
10. Verifikasi baris Emergency Phone tetap Active
11. Klik `[✕ Cancel]` pada baris Emergency Phone
12. Verifikasi Display `Emergency Phone: +62 81234567890` (nilai tersimpan tidak berubah)

### TC-GS-USER-344: Screening Section Custom Fields

13. Kembali ke User List dengan klik Back
14. Klik Name `Dewi Lestari {runId}-060` di User List
15. Verifikasi Section Custom Fields collapsible dengan grid 2 kolom `Label: Value`
16. Verifikasi `Blood Type: A`
17. Verifikasi `Skills: —`
18. Verifikasi icon edit baris Skills tidak tampil
19. Verifikasi baris Emergency Phone menampilkan alert `⚠ "Emergency phone is required."` menggantikan `—`
20. Verifikasi icon edit baris Emergency Phone langsung tampil
21. Hover baris Skills
22. Verifikasi icon edit baris Skills tampil

### TC-GS-USER-345: Section Custom Fields dapat di-collapse dan di-expand

23. Klik header Section Custom Fields
24. Verifikasi Section Custom Fields tertutup
25. Klik header Section Custom Fields lagi
26. Verifikasi Section Custom Fields terbuka kembali

### TC-GS-USER-350: Inline edit Custom Field melanggar rule Data Type ditolak

27. Klik icon edit baris Emergency Phone
28. Ketik `081` pada isian Number Emergency Phone
29. Klik `[✓ Save]`
30. Verifikasi inline error `Min. 4 characters`
31. Verifikasi baris Emergency Phone tetap Active
32. Klik `[✕ Cancel]` pada baris Emergency Phone

### TC-GS-USER-347: Inline edit Custom Field [✕ Cancel] mengembalikan nilai lama tanpa request

33. Hover baris Blood Type, klik icon edit
34. Pilih `B`
35. Klik `[✕ Cancel]` pada baris Blood Type
36. Verifikasi Display kembali `Blood Type: A`
37. Verifikasi tidak ada toast

### TC-GS-USER-348: Inline edit beberapa Custom Field aktif bersamaan secara independen

38. Hover baris Blood Type, klik icon edit
39. Hover baris Skills, klik icon edit
40. Verifikasi baris Blood Type dan baris Skills Active bersamaan
41. Pilih `Excel` pada Skills
42. Klik `[✓ Save]` pada baris Skills
43. Tunggu aksi selesai (baris Skills kembali Display)
44. Verifikasi baris Blood Type masih Active
45. Klik `[✕ Cancel]` pada baris Blood Type

### TC-GS-USER-346: Inline edit Custom Field sukses

46. Hover baris Blood Type, klik icon Edit2Line
47. Verifikasi baris Blood Type Active dengan dropdown, `[✓ Save]`, dan `[✕ Cancel]`
48. Pilih `O`
49. Klik `[✓ Save]`
50. Verifikasi toast sukses: "Success, Blood Type has been updated."
51. Verifikasi Display `Blood Type: O`

### TC-GS-USER-352: Inline edit Custom Field, saving state menonaktifkan widget

52. Pasang intercept pada respons update field: tahan respons
53. Hover baris Blood Type, klik icon edit
54. Pilih `AB`
55. Klik `[✓ Save]`
56. Verifikasi widget baris Blood Type disabled selama saving
57. Verifikasi icon baris Blood Type disabled selama saving
58. Lepas intercept respons update field sehingga respons diteruskan
59. Tunggu aksi selesai (baris Blood Type kembali Display)

### TC-GS-USER-354: Inline edit Custom Field akun sendiri enabled

60. Kembali ke User List dengan klik Back
61. Klik Name `Siti Nurhaliza` di User List
62. Hover baris Blood Type
63. Verifikasi icon edit tampil dan enabled
64. Klik icon edit
65. Pilih nilai Blood Type yang berbeda dari nilai awal akun yang dicatat di hook `before`
66. Klik `[✓ Save]`
67. Verifikasi Display Blood Type menampilkan nilai baru yang tersimpan

### TC-GS-USER-355: Inline edit Custom Field sukses oleh holder Update-Only terhadap target Normal

68. Logout dari akun Total Control, lalu login sebagai Bayu Saputra (Manage user and role Update-Only: R+U) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.GS_UPDATE_PASSWORD`
69. Buka Global Settings > User > User List (sub-tab Login User)
70. Pilih 100 baris per halaman pada Pagination
71. Klik Name `Dewi Lestari {runId}-060` di User List
72. Hover baris Blood Type, klik icon edit
73. Pilih `B`
74. Klik `[✓ Save]`
75. Verifikasi toast sukses: "Success, Blood Type has been updated."

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (75 langkah). Alasan: seluruh blok satu kelas (fungsional) dan satu layar (Section Custom Fields di User Detail); pembukaan Detail dan ganti akun dipakai bersama; tiap blok mengubah satu baris Custom Field sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-1077 dan 349 (user `Dewi Lestari B {runId}-060` dengan Emergency Phone terisi) dikerjakan di awal supaya Detail user itu dibuka satu kali; screening (TC-GS-USER-344, 345) di awal user `Dewi Lestari {runId}-060` sebelum aksi edit; validasi diblokir (TC-GS-USER-350) sebelum aksi sukses; TC-GS-USER-347 sebelum TC-GS-USER-348 dan 346 supaya Blood Type masih `A`; TC-GS-USER-354 dan 355 (ganti akun) paling akhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): pembukaan layar, Back ke User List, `[✕ Cancel]` setelah inline error dan setelah TC-GS-USER-348, pasang dan lepas intercept, "Tunggu aksi selesai", dan ganti akun ke Bayu Saputra. Langkah Hover baris sebelum klik icon edit menyatakan cara icon edit tampil.
- TC-GS-USER-349: `[✕ Cancel]` dan `Verifikasi` Display `Emergency Phone: +62 81234567890` menyatakan "nilai tersimpan tidak berubah" (Expected b).
- Nilai TC-GS-USER-352 diubah dari `O` ke `AB` karena `Blood Type` sudah `O` setelah TC-GS-USER-346; TC tidak menyebut precondition nilai awal.
- Alert `⚠ "Emergency phone is required."` ditulis persis seperti Expected TC, termasuk tanda kutip ganda.
- Temuan untuk QA:
  - TC-GS-USER-344 dan 349: Emergency Phone kosong (344) dan terisi `081234567890` (349) pada Dewi Lestari yang sama; Tabel Pre-setup menyebut Emergency Phone kosong. Spec memakai dua user seed (`Dewi Lestari {runId}-060` kosong dan `Dewi Lestari B {runId}-060` terisi).
  - TC-GS-USER-349 dan 1077: nilai Emergency Phone `081234567890` (349) dan Country Code `+62` dengan Number `81234567890` (1077) berbeda representasi (angka 0 di depan); spec memakai satu user seed (`+62 81234567890`) untuk keduanya.
  - TC-GS-USER-354: precondition tidak menyebut nilai awal Blood Type akun sendiri maupun nilai yang dipilih; spec memilih nilai berbeda dari nilai awal dan memulihkannya di hook `after`.
  - TC-GS-USER-354: Tipe tertulis Negative, padahal Expected adalah aksi berhasil.
  - TC-GS-USER-352: precondition "Response update field ditahan" tidak menyebut cara menahan respons; disediakan tim FE lewat intercept.
  - TC-GS-USER-347: judul menyebut "tanpa request", tetapi Expected tidak mengasersi request; spec hanya mengasersi Display `Blood Type: A` dan tidak ada toast.
  - TC-GS-USER-348: langkah 4 "Save Skills saja" tidak menyebut nilai Skills; spec memakai `Excel`.
  - TC-GS-USER-355: Expected hanya menyebut toast; spec tidak menambah asersi Display.
  - TC-GS-USER-350: Number `081` (3 karakter) menghasilkan `Min. 4 characters`; aturan Min. 4 characters terhadap Number berikut kode negara tidak dijelaskan di TC.
