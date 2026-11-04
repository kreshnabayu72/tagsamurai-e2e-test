---
id: TC-GS-USER-E2E-162-tab-role-switch-off-on-inactive-retained-dan-tooltip-checkbox
title: "User Detail Tab Role: Tooltip Checkbox Baris Switch OFF, Column Visibility Kolom Active, Switch OFF Menyimpan Inactive-Retained, dan Switch ON Memulihkan Nilai Tersimpan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1106
  - TC-GS-USER-1100
  - TC-GS-USER-1092
  - TC-GS-USER-1093
coverage:
  web: automated
---

# User Detail Tab Role: Tooltip Checkbox Baris Switch OFF, Column Visibility Kolom Active, Switch OFF Menyimpan Inactive-Retained, dan Switch ON Memulihkan Nilai Tersimpan

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after`: `Ahmad Fauzi {runId}-162` (padanan Ahmad Fauzi, Tabel Pre-setup No. 13), email `ahmadfauzi+{runId}-162@qwertysystem.net`, Activated, dengan kondisi:
  - baris `Manage TAG` Active dengan Read dan Update tercentang (TC-GS-USER-1092 dan 1093);
  - baris `Manage files` belum pernah di-assign (switch OFF) (TC-GS-USER-1106);
  - baris `Manage master reference` inactive-retained (TC-GS-USER-1106).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): seeding user dengan assignment role Active dan inactive-retained serta nilai CRUD lewat API; membaca jumlah Users role `Manage TAG` (n) lewat BE tepat sebelum aksi TC-GS-USER-1092 (audit trail dan hitungan bersama, 8b butir 10); menghitung request tulis yang terkirim saat klik checkbox disabled (intercept); hover elemen disabled untuk membaca tooltip.
- State global yang diubah: keanggotaan role `Manage TAG` (berkurang satu lalu pulih pada TC-GS-USER-1092 dan 1093). Suite berjalan serial. Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): hapus user seed sehingga keanggotaan role pulih.

## Test Steps

### TC-GS-USER-1106: Checkbox baris switch OFF disabled dengan tooltip `Turn on this role first.`

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-162`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-162` di User List
3. Klik Tab `Role`
4. Hover checkbox Delete baris `Manage files`
5. Verifikasi checkbox Delete baris `Manage files` tampil namun disabled dengan tooltip `"Turn on this role first."`
6. Verifikasi checkbox Delete baris `Manage files` tidak tercentang
7. Hover checkbox Update baris `Manage master reference`
8. Verifikasi checkbox Update baris `Manage master reference` tampil namun disabled dengan tooltip `"Turn on this role first."`
9. Verifikasi checkbox Update baris `Manage master reference` tidak tercentang
10. Klik checkbox Delete baris `Manage files`
11. Verifikasi state checkbox Delete baris `Manage files` tidak berubah (tetap kosong dan disabled)
12. Verifikasi tidak ada request tulis yang terkirim saat klik checkbox
13. Nyalakan switch Active baris `Manage files`
14. Verifikasi checkbox Delete baris `Manage files` enabled
15. Hover checkbox Delete baris `Manage files`
16. Verifikasi tooltip `"Turn on this role first."` tidak tampil

### TC-GS-USER-1100: Column Visibility hide kolom Active lalu unhide

17. Catat posisi switch Active keenam baris sebagai S0
18. Klik header `(⋯)`
19. Uncheck `Active`
20. Verifikasi kolom `Role Name` tampil
21. Verifikasi kolom `Active` hilang
22. Check `Active` lagi
23. Verifikasi kolom `Active` tampil kembali di posisi paling kiri
24. Verifikasi posisi switch Active keenam baris sama dengan S0
25. Tekan Esc untuk menutup Column Visibility

### TC-GS-USER-1092: Switch OFF menyimpan role sebagai inactive-retained

26. Catat jumlah Users role `Manage TAG` di Role & Permission sebagai n (lewat kemampuan baca BE)
27. Matikan switch Active baris `Manage TAG`
28. Verifikasi toast sukses "Success, role has been updated."
29. Verifikasi tidak ada dialog konfirmasi
30. Verifikasi switch Active baris `Manage TAG` OFF
31. Verifikasi seluruh checkbox baris `Manage TAG` disabled
32. Buka Global Settings > Role & Permission > System
33. Verifikasi kolom Users `Manage TAG` sama dengan n - 1
34. Klik icon Search, ketik `Manage TAG`, tekan Enter
35. Klik Name `Manage TAG` untuk membuka Detail role
36. Verifikasi Detail `Manage TAG` memuat sedikitnya satu baris user lain (selain `Ahmad Fauzi {runId}-162`)
37. Klik icon Search, ketik `Ahmad Fauzi {runId}-162`, tekan Enter
38. Verifikasi empty state `No results found` tampil
39. Verifikasi `Ahmad Fauzi {runId}-162` tidak tampil di Detail `Manage TAG`

### TC-GS-USER-1093: Switch ON memulihkan role inactive-retained dengan nilai tersimpan tanpa popup

40. Klik menu User di sidebar Global Settings
41. Klik icon Search, ketik `Ahmad Fauzi {runId}-162`, tekan Enter
42. Klik Name `Ahmad Fauzi {runId}-162` di User List
43. Klik Tab `Role`
44. Nyalakan switch Active baris `Manage TAG`
45. Verifikasi toast sukses "Success, role has been updated."
46. Verifikasi tidak ada popup atau dialog
47. Verifikasi switch Active baris `Manage TAG` ON
48. Verifikasi checkbox Read baris `Manage TAG` tercentang dan disabled
49. Verifikasi checkbox Update baris `Manage TAG` tercentang
50. Buka Global Settings > Role & Permission > System
51. Klik icon Search, ketik `Manage TAG`, tekan Enter
52. Klik Name `Manage TAG` untuk membuka Detail role
53. Klik icon Search, ketik `Ahmad Fauzi {runId}-162`, tekan Enter
54. Verifikasi `Ahmad Fauzi {runId}-162` tampil di Detail `Manage TAG` dengan Read dan Update tercentang

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (54 langkah) karena empat TC berada di satu kelas harness (fungsional, aksi tulis pada user milik spec), satu aktor, dan satu layar utama (Tab Role User Detail). Blok TC-GS-USER-1106 dan TC-GS-USER-1100 berdiri sendiri; TC-GS-USER-1093 sengaja memakai state hasil TC-GS-USER-1092 pada user seed yang sama (S-04), sehingga langkah itu berurutan dan tidak bisa dibalik. Banyak langkah berasal dari satu `Verifikasi` per klausa Expected (S-01).
- Urutan TC sumber diubah: TC-GS-USER-1106 dan TC-GS-USER-1100 (UI Only, tooltip dan Column Visibility) mendahului TC-GS-USER-1092 dan TC-GS-USER-1093 (aksi tulis) sesuai bagian 3; TC-GS-USER-1092 mendahului TC-GS-USER-1093 karena precondition TC-GS-USER-1093 adalah hasil TC-GS-USER-1092 (S-04). Langkah 1 sampai 3 TC-GS-USER-1100 dipenuhi langkah 2 sampai 3.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 37, 41, dan 53 (Search nama target sebelum Klik Name, R-16), 34 dan 51 (Search role `Manage TAG`), 17 (mencatat posisi switch), 25 (menutup Column Visibility), 26 (mencatat n), 32 dan 50 (membuka Role & Permission), 40 (kembali ke User List).
- Pemulihan Column Visibility (bagian 8b butir 13): langkah 22 mengembalikan kolom `Active` pada TC yang sama; Column Visibility Tab Role tidak memiliki `[Save]`.
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC, hanya sebagai anchor): langkah 20 (kolom `Role Name` tampil, anchor untuk "kolom `Active` hilang"); langkah 28 (toast sukses menjadi anchor untuk langkah 29, absence dialog); langkah 45 (anchor untuk langkah 46); langkah 36 (Detail `Manage TAG` memuat sedikitnya satu baris user lain, anchor positif sebelum Search pada langkah 37; mengandaikan role `Manage TAG` masih punya anggota lain sesudah `Ahmad Fauzi {runId}-162` dinonaktifkan) dan langkah 38 (empty state `No results found`, anchor untuk asersi absence pada langkah 39).
- TC-GS-USER-1106 Expected c ("tooltip hilang") diasersi pada langkah 15 sampai 16 setelah langkah 14 (checkbox enabled) yang menjadi anchor.
- Temuan untuk QA:
  - TC-GS-USER-1100 Expected b ("Selama kolom Active hidden, nilai switch tidak berubah") tidak mungkin diamati selama kolom tersembunyi; spec membandingkan posisi switch sebelum hide (S0, langkah 17) dengan sesudah unhide (langkah 24).
  - TC-GS-USER-1092 langkah 4 dan 5 tidak menyebut surface Detail role (halaman Detail `Manage TAG` di Role & Permission) maupun cara mencari user; spec mencari lewat Search dan mengasersi empty state.
  - TC-GS-USER-1106 Expected a menulis checkbox `Manage master reference` inactive-retained "tidak tercentang" walau nilai tersimpan ada; spec mengikuti TC.
  - TC-GS-USER-1106 langkah 4 "Klik salah satu checkbox itu" tidak menyebut checkbox mana; spec memilih Delete baris `Manage files`.
  - TC-GS-USER-1093 (P-10): precondition menyebut "hasil TC-GS-USER-1092"; spec membangunnya berurutan pada user seed yang sama.
  - TC-GS-USER-1092 Post Condition ("baris Manage TAG inactive-retained") tanpa langkah observasi tersendiri; diverifikasi sebagian lewat langkah 47 sampai 49.
  - TC-GS-USER-1106, 1100, 1092, 1093 memakai user Pre-setup (Ahmad Fauzi); spec memakai seed milik spec (S-06).
