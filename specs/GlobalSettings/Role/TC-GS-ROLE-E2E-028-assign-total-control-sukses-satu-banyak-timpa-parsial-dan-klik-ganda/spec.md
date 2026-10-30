---
id: TC-GS-ROLE-E2E-028-assign-total-control-sukses-satu-banyak-timpa-parsial-dan-klik-ganda
title: "Assign Total Control: Sukses Satu dan Banyak User, Timpa Baris Parsial, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-58
  - TC-GS-ROLE-59
  - TC-GS-ROLE-61
  - TC-GS-ROLE-63
coverage:
  web: automated
---

# Assign Total Control: Sukses Satu dan Banyak User, Timpa Baris Parsial, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Spec tidak berganti akun; hook `after` tidak perlu mengembalikan sesi.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (user kandidat dan user regular; bukan data baru sehingga tanpa suffix `+{runId}-028`; diubah dan dipulihkan sesuai catatan "Reset Pre-setup per TC" di `tc-role.md`):
  - Sari Wulandari (Pre-setup #11, Active): tanpa access level dan tanpa baris role (TC-GS-ROLE-58).
  - Maya Anggraini (Inactive) dan Rudi Hartono (Pending Activation) (Pre-setup #11): tanpa access level dan tanpa baris role (TC-GS-ROLE-59).
  - Doni Pratama (Pre-setup #10, Staff, IT): Manage TAG (R), Import data (C,R), Manage files (R,D), Manage user and role (R); tanpa baris Manage hardware dan Manage master reference (TC-GS-ROLE-61).
  - Nina Kartika (Pre-setup #11, Active): tanpa access level dan tanpa baris role (TC-GS-ROLE-63).
- Pemulihan: hook `before` memastikan state di atas (Given) dan hook `after` mengembalikan Sari Wulandari, Maya Anggraini, Rudi Hartono, dan Nina Kartika ke state kandidat (tanpa access level dan tanpa baris role) serta Doni Pratama ke baris Pre-setup #10 di atas. Efek pada Modified By dan Last Updated user tersebut ikut dipulihkan.
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): mengatur access level dan baris role user Pre-setup lewat API untuk Given dan pemulihan; membaca nilai kolom Users, Modified By, dan Last Updated dari UI; jam server dan jam browser sinkron (asersi Last Updated memakai waktu aksi dengan toleransi satu menit); format tanggal mengikuti General Settings aktif.

Tabel A, Detail yang diperiksa untuk Sari Wulandari (TC-GS-ROLE-58):

| Role | Kotak centang yang harus checked |
|---|---|
| Manage TAG | Read dan Update |
| Import data | Create dan Read |

Tabel B, Detail yang diperiksa untuk Doni Pratama (TC-GS-ROLE-61):

| Role | Kotak centang yang harus checked | Keterangan |
|---|---|---|
| Manage TAG | Read dan Update | |
| Import data | Create dan Read | |
| Manage files | Read dan Delete | |
| Manage user and role | Create, Read, Update, dan Delete | |
| Manage hardware | Create, Read, Update, dan Delete | baris baru |
| Manage master reference | Create, Read, Update, dan Delete | baris baru |

## Test Steps

### TC-GS-ROLE-58: Assign Total Control ke satu user

1. Buka Tab System
2. Catat nilai kolom Users keenam role sebagai baseline
3. Buka Tab Total Control
4. Klik `[+ Assign]`
5. Centang Sari Wulandari
6. Klik `[Assign]`
7. Verifikasi tidak ada dialog konfirmasi yang tampil
8. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
9. Catat waktu aksi
10. Verifikasi popup Assign Total Control tertutup
11. Verifikasi baris Sari Wulandari tampil di Tab Total Control
12. Verifikasi kolom Modified By baris Sari Wulandari bernilai `Ahmad F`
13. Verifikasi kolom Last Updated baris Sari Wulandari sama dengan waktu pada langkah 9 (toleransi satu menit)
14. Buka Tab System
15. Verifikasi kolom Users keenam role masing-masing bertambah 1 dari baseline pada langkah 2

Untuk setiap baris Tabel A (langkah 16 sampai 18):

16. Buka Detail `<role>`
17. Verifikasi baris Sari Wulandari: kotak centang pada kolom "Kotak centang yang harus checked" checked
18. Buka Tab System

19. Buka Tab Total Control

### TC-GS-ROLE-59: Assign Total Control ke beberapa user sekaligus termasuk Inactive dan Pending Activation

20. Klik `[+ Assign]`
21. Centang Maya Anggraini dan Rudi Hartono
22. Klik `[Assign]`
23. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
24. Verifikasi baris Maya Anggraini tampil di Tab Total Control dengan Status `Inactive`
25. Verifikasi baris Rudi Hartono tampil dengan badge `Pending Activation` di sebelah Name

### TC-GS-ROLE-61: Assign Total Control menimpa baris role parsial yang sudah ada

26. Klik `[+ Assign]`
27. Centang Doni Pratama
28. Klik `[Assign]`
29. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
30. Buka Tab System

Untuk setiap baris Tabel B (langkah 31 sampai 34):

31. Buka Detail `<role>`
32. Verifikasi baris Doni Pratama: kotak centang pada kolom "Kotak centang yang harus checked" checked
33. Verifikasi Detail hanya memuat 1 baris Doni Pratama
34. Buka Tab System

35. Buka Tab Total Control

### TC-GS-ROLE-63: Klik ganda [Assign] Popup Assign Total Control

36. Tunggu toast lama hilang otomatis
37. Buka Modal Changelog Tab Total Control
38. Catat jumlah entry Assign untuk Nina Kartika sebagai baseline
39. Tutup Modal Changelog
40. Klik `[+ Assign]`
41. Centang Nina Kartika
42. Klik `[Assign]` dua kali cepat
43. Verifikasi tombol `[Assign]` masuk state loading atau disabled setelah klik pertama
44. Verifikasi satu toast sukses `Success, Total Control has been assigned.` tampil
45. Buka Modal Changelog Tab Total Control
46. Verifikasi jumlah entry Assign untuk Nina Kartika bertambah tepat 1 dari baseline pada langkah 38
47. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional (satu topik aksi, Assign Total Control, pada layar dan akun yang sama).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (47 langkah nominal, sekitar 70 dengan ekspansi perulangan langkah 16 sampai 18 dan 31 sampai 34). Alasan: empat TC berbagi topik aksi, layar, dan akun yang sama (Assign Total Control dari Tab Total Control); tiap blok TC memakai user target sendiri dan dimulai dari Tab Total Control, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ekspansi berasal dari kewajiban memeriksa Detail enam role pada Expected TC-GS-ROLE-61 (dan dua Detail pada TC-GS-ROLE-58).
- Langkah penghubung dan pencatatan (bukan dari TC sumber, tanpa awalan `Verifikasi`): membuka Tab System dan Tab Total Control (langkah 1, 3, 14, 18, 19, 30, 34, 35), mencatat baseline Users (langkah 2), mencatat waktu aksi (langkah 9), menunggu toast lama hilang (langkah 36), serta membuka, mencatat baseline, dan menutup Modal Changelog (langkah 37 sampai 39, 45, 47). Baseline Users dan baseline jumlah entry memenuhi S-12 (dicatat sebelum aksi pemicu).
- Langkah 7 (tidak ada dialog konfirmasi) diletakkan sesudah klik `[Assign]` dan sebelum toast pada langkah 8, sesuai bagian 8b butir 11; toast menjadi anchor positif bahwa assign selesai tanpa dialog.
- Langkah 36: toast sukses TC sebelumnya ditunggu hilang sebelum langkah 44 menghitung "satu toast" (bagian 8b butir 8c).
- Perulangan langkah 16 sampai 18 memakai Tabel A dan langkah 31 sampai 34 memakai Tabel B di Prerequisites; parameter tiap iterasi hanya role dan kotak centang pada tabel.
- Post Condition tanpa langkah observasi tidak diasersi; lihat "Temuan untuk QA".
- Maya Anggraini dan Rudi Hartono (Tabel Dinamis #2) diassign di spec ini lalu dipulihkan ke state kandidat di hook `after`; spec lain yang membutuhkannya sebagai Total Control menyiapkan Given sendiri.
- Temuan untuk QA:
  - TC-GS-ROLE-58, TC-GS-ROLE-59, TC-GS-ROLE-61, dan TC-GS-ROLE-63 menyebut "Centang <nama>" dan "amati baris <nama>" tanpa cara menemukan baris bila picker atau Detail lebih dari satu halaman (pool picker dan Detail berisi lebih dari 10 baris menurut Pre-setup #11 dan #17); spec mengikuti TC dan tidak menambahkan langkah Search atau pagination, sehingga mekanisme menemukan baris diputuskan di tahap script.
  - Post Condition TC-GS-ROLE-58 tanpa langkah observasi dan tidak diasersi: (a) access level Sari Wulandari = Total Control dan baris keenam role CRUD penuh sesuai kolom berlaku (hanya dua Detail yang diamati lewat Expected e dan f), (b) log Assign tercatat (Section 5), (c) sidebar Global Settings Sari Wulandari berubah (Section 7).
  - Expected TC-GS-ROLE-58 d ("kolom Users keenam role bertambah 1") tidak menyebut nilai awal; spec mencatat baseline sendiri (langkah 2).
