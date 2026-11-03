---
id: TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1
title: "Absence log: aksi ditolak karena state tenant (1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-973
  - TC-FA-RP-974
  - TC-FA-RP-975
  - TC-FA-RP-976
  - TC-FA-RP-977
  - TC-FA-RP-978
coverage:
  web: automated
---

# Absence log: aksi ditolak karena state tenant (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #25 (`Client Suspended`), #15 (Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata), #36 (baris Budi Santoso di Tab Total Control, TC-FA-RP-974), #39 (Detail Role `Manage accounting` dan `Manage Open API` terisi; Citra Lestari dengan Create tercentang; Dimas Pranata pada `Manage Open API`), #18, dan #19. Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: kemampuan baca jumlah entri (disediakan tim FE/BE, tanpa endpoint karangan, bagian 8b butir 10) untuk Changelog surface terkait, System Log aktor, dan Activity Log; baseline dicatat per TC sebelum aksi pemicu dan asersi memakai perbandingan dengan baseline, bukan angka absolut (S-12).
- State global: status `Client Suspended` tidak diubah; spec tidak mengubah data karena semua aksi ditolak.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-973: Client Suspended menolak Assign Total Control, tidak ada entri log

1. Catat baseline jumlah entri Changelog Tab Total Control, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
2. Klik `[+ Assign]` di Tab Total Control
3. Centang Dimas Pranata
4. Klik `[Assign]`
5. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
6. Verifikasi jumlah entri Changelog Tab Total Control, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
7. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-974: Client Suspended menolak Remove Total Control, tidak ada entri log

8. Tunggu toast lama hilang otomatis
9. Catat baseline jumlah entri Changelog Tab Total Control, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
10. Klik `[⋯]` baris Budi Santoso lalu `Remove`
11. Klik `[Remove]`
12. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
13. Verifikasi jumlah entri Changelog Tab Total Control, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
14. Klik `[Cancel]` pada dialog Remove

### TC-FA-RP-975: Client Suspended menolak Assign Group Manager, tidak ada entri log

15. Tunggu toast lama hilang otomatis
16. Klik Tab `Group Manager`
17. Catat baseline jumlah entri Changelog Tab Group Manager, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
18. Klik `[+ Assign]` di Tab Group Manager
19. Pilih group `Data Center`, centang Ahmad Fauzi
20. Klik `[Assign]`
21. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
22. Verifikasi jumlah entri Changelog Tab Group Manager, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
23. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-976: Client Suspended menolak Assign User ke Role, tidak ada entri log

24. Tunggu toast lama hilang otomatis
25. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
26. Catat baseline jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
27. Klik `[+ Assign]`
28. Centang Ahmad Fauzi
29. Klik `[Assign]`
30. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
31. Verifikasi jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
32. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-977: Client Suspended menolak Edit CRUD, tidak ada entri log

33. Tunggu toast lama hilang otomatis
34. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
35. Catat baseline jumlah entri Changelog Detail Role `Manage accounting`, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
36. Hapus centang Create pada baris Citra Lestari
37. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
38. Verifikasi jumlah entri Changelog Detail Role `Manage accounting`, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-978: Client Suspended menolak Remove baris peran, tidak ada entri log

39. Tunggu toast lama hilang otomatis
40. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
41. Catat baseline jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
42. Klik `[⋯]` baris Dimas Pranata lalu `Remove`
43. Klik `[Remove]`
44. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
45. Verifikasi jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
46. Klik `[Cancel]` pada dialog Remove

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-973 sampai TC-FA-RP-978).
- Kelas g (absence log): tiap TC punya aksi pemicu nyata, baseline sendiri (S-12), dan anchor positif sebelum asersi absence (bagian 8b butir 2). Pemicu berkelas lain (state tenant, permintaan langsung, dua sesi) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5` butir a). Anchor positif tiap blok adalah toast penolakan `Changes can't be saved while this workspace is suspended or expired.`.
- Pembagian TC lintas spec: klausa "tidak ada entri log" pada Expected c TC-FA-RP-973 sampai TC-FA-RP-978 diasersi di spec ini dengan aksi nyata dan baseline sendiri; klausa toast, state kontrol, dan tidak ada perubahan data diasersi di spec 278 (TC-FA-RP-973 sampai 977) dan spec 279 (TC-FA-RP-978). Id TC tetap di `sourceTc` spec asal dan spec ini (S-05).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): pencatatan baseline jumlah entri; "Tunggu toast lama hilang otomatis" sebelum tiap toast baku yang sama diasersi lagi (R-12); membuka tab dan Detail Role; memilih group dan mencentang kandidat; menutup popup dan dialog dengan `[Cancel]` (S-09).
- Spec melewati sekitar 35 langkah (46 langkah). Semua blok satu kelas harness (absence log) pada akun dan tenant yang sama; tiap TC punya aksi, baseline, dan anchor sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Akun Total Control pada `Client Suspended` tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - Expected c TC-FA-RP-973 sampai TC-FA-RP-978 menyebut "entri log" tanpa surface; spec membandingkan Changelog surface yang disentuh aksi, System Log aktor, dan Activity Log terhadap baseline.
  - TC tidak menyebut apakah popup atau dialog tetap terbuka setelah penolakan; spec menutupnya dengan `[Cancel]` mengikuti pola penolakan lain di TC.
