---
id: TC-AC-SU-E2E-026-aktor-read-only-kontrol-baca-tabel-dan-tab-detail
title: "Aktor Read Only: Kontrol Baca Tabel, Seluruh Tab Detail User, Tab Responsibilities, Tab Changelog, dan Prioritas Tooltip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-75
  - TC-AC-SU-76
  - TC-AC-SU-80
  - TC-AC-SU-367
  - TC-AC-SU-403
coverage:
  web: automated
---

# Aktor Read Only: Kontrol Baca Tabel, Seluruh Tab Detail User, Tab Responsibilities, Tab Changelog, dan Prioritas Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-76 | `John Doe` | `John Doe {runId}-026` | `johndoe+{runId}-026@qwertysystem.net` | Activated, Active |
| TC-AC-SU-367, 403 | `Jane Smith` | `Jane Smith {runId}-026` | `janesmith+{runId}-026@qwertysystem.net` | sedikitnya satu Pending Approval (Tab Responsibilities terisi) dan sedikitnya satu entri Changelog |

- Data user lain di entitas (Pre-setup, lebih dari 10 baris) dipakai TC-AC-SU-75 untuk pagination next. Baris Default User (Pre-setup #1) dicari lewat Search atas emailnya. Seeding Pending Approval dan entri Changelog lewat Fixture BE (mekanisme tidak disebut TC; disediakan tim FE/BE).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-75: Kontrol baca tabel tetap aktif untuk Read Only

1. Klik icon Search
2. Verifikasi icon Search tampil dan berfungsi (input Search terbuka)
3. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
4. Klik icon Filter
5. Verifikasi icon Filter tampil dan berfungsi (Filter Panel terbuka)
6. Klik icon Filter lagi untuk menutup Filter Panel
7. Klik header kolom Name
8. Verifikasi Sort pada kolom Name tampil dan berfungsi
9. Klik header (⋯) Column Visibility
10. Verifikasi Column Visibility tampil dan berfungsi (overlay terbuka)
11. Tutup overlay Column Visibility dengan Esc
12. Klik pagination next
13. Verifikasi Pagination tampil dan berfungsi (halaman 2 terbuka)
14. Verifikasi icon Download dan icon Changelog tampil
15. Klik (⋯) satu baris
16. Verifikasi row action (⋯) tampil dengan opsi `Detail`
17. Tutup menu row action dengan Esc

### TC-AC-SU-76: Seluruh tab Detail User tampil untuk Read Only

18. Ketik Search `John Doe {runId}-026`, tekan Enter
19. Klik Name `John Doe {runId}-026`
20. Klik Tab `Role`
21. Verifikasi Tab `Role` tampil dan terbuka
22. Klik Tab `Responsibilities (N)`
23. Verifikasi Tab `Responsibilities (N)` tampil dan terbuka
24. Klik Tab `Changelog`
25. Verifikasi Tab `Changelog` tampil dan terbuka
26. Klik Tab `System Log`
27. Verifikasi Tab `System Log` tampil dan terbuka
28. Klik Tab `User Log`
29. Verifikasi Tab `User Log` tampil dan terbuka
30. Verifikasi tidak ada state disabled pada tab
31. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-80: Prioritas tooltip aktor Read Only terhadap baris Default User

32. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
33. Hover switch Active baris Default User
34. Verifikasi switch Active baris Default User tetap tampil (visible) ON namun disabled
35. Verifikasi tampil satu tooltip `Read Only access cannot modify data.`
36. Verifikasi tooltip `Default User cannot be modified.` tidak tampil

### TC-AC-SU-367: Tab Responsibilities tetap tampil untuk aktor Read Only

37. Ganti isi kotak search dengan `Jane Smith {runId}-026`, tekan Enter
38. Klik Name `Jane Smith {runId}-026`
39. Klik Tab `Responsibilities (N)`
40. Verifikasi Tab `Responsibilities (N)` tampil dan tabel terisi
41. Verifikasi toolbar Search, Filter, dan Download aktif
42. Verifikasi tidak ada kontrol Disabled di tab ini

### TC-AC-SU-403: Tab Changelog dapat dibuka aktor Read Only

43. Klik Tab `Changelog`
44. Verifikasi Tab Changelog tampil dengan data
45. Verifikasi Search, Filter, dan Download aktif

## Notes

- Langkah penghubung (S-03): langkah 3, 6, 11, dan 17 (reset kontrol yang dibuka, S-09), langkah 31 (kembali ke daftar); Search untuk menemukan baris target adalah penghubung (R-16). Layar awal dibuka hook `beforeEach` suite.
- Ukuran spec (45 langkah, di atas smell sekitar 35 langkah): satu akun (Read Only) pada satu halaman; lima blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna) dengan tiap kontrol atau tab diasersi setelah aksinya (S-01).
- Temuan untuk QA:
  - TC-AC-SU-75 butir a menyebut Download dan Changelog "tampil dan berfungsi" tetapi langkah TC tidak mengklik keduanya; spec mengasersi Download dan Changelog tampil dan tidak menjalankannya.
  - TC-AC-SU-367 dan TC-AC-SU-403 mensyaratkan Pending Approval dan entri Changelog pada `Jane Smith` tanpa cara membuatnya; disediakan tim FE/BE.
  - Label tab `Responsibilities (N)` ditulis dengan placeholder `N` sesuai TC (nilai N tidak diasersi di spec ini).
  - Nama user TC (`John Doe`, `Jane Smith`) dipakai sebagai nama bersuffix `{runId}-026` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
