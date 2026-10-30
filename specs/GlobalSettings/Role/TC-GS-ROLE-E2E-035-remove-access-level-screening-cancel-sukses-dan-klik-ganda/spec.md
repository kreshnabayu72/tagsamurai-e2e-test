---
id: TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda
title: "Remove Access Level: Screening Dialog, Cancel, Sukses, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-84
  - TC-GS-ROLE-85
  - TC-GS-ROLE-86
  - TC-GS-ROLE-87
  - TC-GS-ROLE-88
  - TC-GS-ROLE-91
coverage:
  web: automated
---

# Remove Access Level: Screening Dialog, Cancel, Sukses, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Spec tidak berganti akun.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-035`; diubah dan dipulihkan sesuai catatan "Reset Pre-setup per TC" di `tc-role.md`). Given disiapkan hook `before` lewat API:
  - Sari Wulandari (Pre-setup #11, Active): Total Control, dengan baris keenam role CRUD penuh (Given, Tabel Dinamis #1), untuk TC-GS-ROLE-84, 85, dan 86.
  - Dewi Lestari (Pre-setup #3, Staff, Finance): Total Control, Inactive, kehilangan Total Control di TC-GS-ROLE-87.
  - Lukman Hakim (Pre-setup #18, Active): Total Control (Given, Tabel Dinamis #7) untuk TC-GS-ROLE-91.
  - Rahmat Hidayat (Pre-setup #11, Active): Read Only (Given, Tabel Dinamis #4) untuk TC-GS-ROLE-88; punya baris Manage files (R,D) sebagai Pre-setup sebelum di-assign Read Only.
- Pemulihan di hook `after`: Sari Wulandari dan Lukman Hakim kembali ke state kandidat (tanpa access level dan tanpa baris role); Dewi Lestari kembali Total Control, Inactive; Rahmat Hidayat kembali tanpa access level dengan baris Manage files (R,D) seperti Pre-setup #11. Efek pada Modified By dan Last Updated ikut dipulihkan sejauh dapat dipulihkan.
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): mengatur access level dan baris role user Pre-setup lewat API untuk Given dan pemulihan; membaca nilai kolom Users dan jumlah entry Modal Changelog dari UI; hover pada komponen user di dialog.

Tabel Detail, enam Detail yang diperiksa untuk TC-GS-ROLE-86 dan TC-GS-ROLE-88:

| Role |
|---|
| Manage TAG |
| Import data |
| Manage files |
| Manage hardware |
| Manage master reference |
| Manage user and role |

## Test Steps

### Baseline sebelum aksi

1. Buka Tab System
2. Catat nilai kolom Users keenam role sebagai baseline
3. Buka Tab Total Control

### TC-GS-ROLE-84: Screening dialog Remove Total Control

4. Klik `(⋯)` baris Sari Wulandari
5. Klik `Remove`
6. Verifikasi Title dialog `Remove Total Control` tampil
7. Verifikasi body dialog memuat komponen user `• Sari W` (ikon user generik, first name, dan inisial last name)
8. Arahkan kursor ke komponen user `• Sari W`
9. Verifikasi nama lengkap `Sari Wulandari` tampil saat hover
10. Verifikasi teks body `This will remove Total Control from this user. Their individual permissions will be reset and they will have no access assigned. Are you sure you want to remove it?` tampil
11. Verifikasi tombol `[Cancel]` (contrast) dan `[Remove]` (danger) tampil

### TC-GS-ROLE-85: Cancel dialog Remove Total Control

12. Klik `[Cancel]`
13. Verifikasi dialog tertutup
14. Verifikasi tidak ada toast yang tampil
15. Verifikasi baris Sari Wulandari tetap tampil di Tab Total Control
16. Buka Tab System
17. Buka Detail "Manage TAG"
18. Verifikasi baris Sari Wulandari tetap tampil di Detail "Manage TAG" (baris role tetap)
19. Buka Tab Total Control

### TC-GS-ROLE-86: Remove Total Control dari user

20. Klik `(⋯)` baris Sari Wulandari
21. Klik `Remove`
22. Klik `[Remove]`
23. Verifikasi toast sukses `Success, Total Control has been removed.` tampil
24. Verifikasi baris Sari Wulandari tidak ada di Tab Total Control
25. Buka Tab System
26. Verifikasi kolom Users keenam role masing-masing berkurang 1 dari baseline pada langkah 2

Untuk setiap baris Tabel Detail (langkah 27 sampai 30):

27. Buka Tab System
28. Buka Detail `<role>`
29. Ketik Search `Sari Wulandari`, tekan Enter
30. Verifikasi `No results found` tampil (Sari Wulandari tidak ada di Detail `<role>`)

31. Buka Tab Total Control

### TC-GS-ROLE-87: Remove Total Control user Inactive tanpa batasan jumlah Total Control

32. Klik `(⋯)` baris Dewi Lestari
33. Klik `Remove`
34. Klik `[Remove]`
35. Verifikasi tidak ada peringatan jumlah Total Control yang tampil
36. Verifikasi toast sukses `Success, Total Control has been removed.` tampil
37. Verifikasi baris Dewi Lestari tidak ada di Tab Total Control

### TC-GS-ROLE-91: Klik ganda [Remove] dialog Remove Total Control

38. Tunggu toast lama hilang otomatis
39. Buka Modal Changelog Tab Total Control
40. Catat jumlah entry Remove untuk Lukman Hakim sebagai baseline
41. Tutup Modal Changelog
42. Klik `(⋯)` baris Lukman Hakim
43. Klik `Remove`
44. Klik `[Remove]` dua kali cepat
45. Verifikasi satu toast sukses `Success, Total Control has been removed.` tampil
46. Buka Modal Changelog Tab Total Control
47. Verifikasi jumlah entry Remove untuk Lukman Hakim bertambah tepat 1 dari baseline pada langkah 40
48. Tutup Modal Changelog

### TC-GS-ROLE-88: Screening dialog dan Remove Read Only

49. Buka Tab Read Only
50. Klik `(⋯)` baris Rahmat Hidayat
51. Klik `Remove`
52. Verifikasi Title dialog `Remove Read Only` tampil
53. Verifikasi body dialog memuat komponen user `• Rahmat H` (ikon user generik, first name, dan inisial last name)
54. Arahkan kursor ke komponen user `• Rahmat H`
55. Verifikasi nama lengkap `Rahmat Hidayat` tampil saat hover
56. Verifikasi teks body `This will remove Read Only from this user. Their individual permissions will be reset and they will have no access assigned. Are you sure you want to remove it?` tampil
57. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
58. Klik `[Remove]`
59. Verifikasi toast sukses `Success, Read Only has been removed.` tampil
60. Verifikasi baris Rahmat Hidayat tidak ada di Tab Read Only

Untuk setiap baris Tabel Detail (langkah 61 sampai 64):

61. Buka Tab System
62. Buka Detail `<role>`
63. Ketik Search `Rahmat Hidayat`, tekan Enter
64. Verifikasi `No results found` tampil (Rahmat Hidayat tidak ada di Detail `<role>`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional (satu topik aksi, Remove access level Total Control dan Read Only).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (64 langkah nominal, sekitar 104 dengan ekspansi dua perulangan atas enam Detail, langkah 27 sampai 30 dan 61 sampai 64). Alasan: enam TC satu topik aksi (Remove access level) dengan layar dan akun yang sama; ekspansi berasal dari Expected TC-GS-ROLE-86 d dan TC-GS-ROLE-88 c yang mewajibkan memeriksa keenam Detail. Tiap blok TC memakai user target sendiri (Sari Wulandari, Dewi Lestari, Lukman Hakim, Rahmat Hidayat) dengan Given dari hook `before`, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok yang menghapus access level berada di tengah dan akhir sesudah screening dan Cancel (bagian 3 prinsip 5).
- Urutan TC sumber diubah: TC-GS-ROLE-88 (Tab Read Only) dijalankan terakhir karena berbeda tab dan menghapus access level; TC-GS-ROLE-91 sebelum TC-GS-ROLE-88. TC-GS-ROLE-85 memakai dialog yang sama dengan TC-GS-ROLE-84: langkah 1 TC-GS-ROLE-85 ("Klik Remove baris Sari Wulandari") dipenuhi oleh langkah 4 sampai 5, sehingga dialog dibuka sekali untuk screening dan Cancel.
- Langkah penghubung dan pencatatan (bukan dari TC sumber, tanpa awalan `Verifikasi`): membuka Tab System, Detail, Tab Total Control, dan Tab Read Only (langkah 1, 3, 16, 17, 19, 25, 27, 28, 31, 49, 61, 62), mencatat baseline Users (langkah 2), hover (langkah 8 dan 54), Search per Detail (langkah 29 dan 63), menunggu toast lama hilang (langkah 38), serta mencatat baseline dan membuka atau menutup Modal Changelog (langkah 39 sampai 41, 46, 48).
- Langkah 14 (tidak ada toast) didahului langkah 13 (dialog tertutup) sebagai anchor positif bahwa klik `[Cancel]` sudah diproses. Langkah 35 (tidak ada peringatan jumlah Total Control) diletakkan segera sesudah `[Remove]` dan sebelum toast pada langkah 36 (bagian 8b butir 11).
- Langkah 24, 37, dan 60 (baris hilang dari tab) didahului toast sukses sebagai anchor (bagian 8b butir 2). Langkah 30 dan 64 memakai empty state `No results found` hasil Search sebagai anchor absence.
- Perulangan langkah 27 sampai 30 dan 61 sampai 64 memakai Tabel Detail di Prerequisites; parameter tiap iterasi hanya nama role.
- Asersi tambahan di luar kalimat Expected TC (S-03): langkah 18 mengamati "baris role-nya tetap" (Expected TC-GS-ROLE-85 b) lewat Detail "Manage TAG".
- Temuan untuk QA:
  - Post Condition TC-GS-ROLE-86 tanpa langkah observasi dan tidak diasersi: (a) access level Sari Wulandari kosong dan tidak punya baris role (hanya diamati lewat Expected b sampai d), (b) log Remove (Section 5) dan notifikasi ke Sari Wulandari (Section 7).
  - TC-GS-ROLE-84, 85, 86, 87, 88, dan 91 menyebut "Klik (⋯) baris <nama>" tanpa cara menemukan baris bila tab lebih dari satu halaman; mekanisme menemukan baris diputuskan di tahap script.
  - TC-GS-ROLE-85 Expected b ("baris role-nya tetap") tidak menyebut Detail yang diperiksa; spec memakai Detail "Manage TAG".
  - TC-GS-ROLE-86 c ("kolom Users keenam role berkurang 1") tidak menyebut nilai awal; spec mencatat baseline sendiri (langkah 2).
  - TC-GS-ROLE-88 tidak menyebut kondisi baris role Rahmat Hidayat sesudah Remove Read Only selain "hilang dari semua Detail"; baris Manage files (R,D) Pre-setup #11 ikut hilang sehingga spec memulihkannya di hook `after`.
