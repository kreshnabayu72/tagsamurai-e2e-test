---
id: TC-FA-FAAC-E2E-023-role-matrix-visibilitas-detail-edit-manage-create-update-delete
title: "Role Matrix: Visibilitas Elemen Detail Mode Edit untuk Manage Accounting (Read, Create), (Read, Update), dan (Read, Delete)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-65
  - TC-FA-FAAC-66
  - TC-FA-FAAC-67
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Detail Mode Edit untuk Manage Accounting (Read, Create), (Read, Update), dan (Read, Delete)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Create)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Create) | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RC_PASSWORD` | TC-FA-FAAC-65 |
| Manage accounting (Read, Update) | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RU_PASSWORD` | TC-FA-FAAC-66 |
| Manage accounting (Read, Delete) | `manageAccountingReadDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RD_PASSWORD` | TC-FA-FAAC-67 |

- Env var: `FA_AC_MA_RC_PASSWORD`, `FA_AC_MA_RU_PASSWORD`, `FA_AC_MA_RD_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Asset Class HEAVY-EQ memiliki versi Scheduled dengan Effective From bulan berjalan + 2 (M+2, format MMM yyyy; seed Scheduled relatif tanggal run, fixture disediakan tim FE/BE) dan Asset Name ter-assign Excavator PC200 dan Wheel Loader (Pre-setup seed, NC-16). Dibaca, tidak diubah. Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: ganti akun (logout lalu login), hover pada field dan membaca tooltip, membuka dropdown Select akun, centang baris tabel Asset Names.

## Test Steps

### TC-FA-FAAC-65

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik Class Code HEAVY-EQ untuk membuka Detail mode Edit
3. Verifikasi tab General, Depreciation, Accounts, dan Asset Names serta Alert versi Scheduled "Next version starts <M+2 dalam format MMM yyyy>.": Show
4. Verifikasi Button [Cancel scheduled version] pada Alert: Hidden
5. Arahkan kursor ke field Class Name pada tab General
6. Verifikasi tooltip "You don't have permission to edit." tampil
7. Verifikasi field halaman Detail mode Edit tetap tampil (visible) namun berstatus Disabled
8. Verifikasi Button [Save] dan [Clear Field]: Hidden
9. Klik tab Accounts, lalu klik Select akun Asset Cost
10. Verifikasi Select akun tidak dapat dibuka karena Disabled sehingga shortcut "+ Create account" tidak tersedia
11. Klik tab Asset Names
12. Verifikasi tabel Asset Names tampil dengan baris Wheel Loader
13. Verifikasi tab Asset Names: Button [+ Assign Asset Names], row action Move dan Unassign, bulk Move to another asset class dan Unassign: Hidden

### TC-FA-FAAC-66

14. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Update)
15. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
16. Ketik Search `HEAVY-EQ`, tekan Enter
17. Klik Class Code HEAVY-EQ untuk membuka Detail mode Edit
18. Verifikasi tab General, Depreciation, Accounts, dan Asset Names serta Alert versi Scheduled "Next version starts <M+2 dalam format MMM yyyy>.": Show
19. Verifikasi Button [Cancel scheduled version] pada Alert: Show
20. Verifikasi field halaman Detail mode Edit: Show dan dapat diubah
21. Verifikasi Button [Save] dan [Clear Field]: Show
22. Klik tab Accounts, lalu klik Select akun Asset Cost
23. Verifikasi pada Select akun (Asset Cost), shortcut "+ Create account": Hidden
24. Tutup dropdown Select akun (Esc)
25. Klik tab Asset Names
26. Centang baris Wheel Loader
27. Klik tombol ⋯ pada baris Wheel Loader
28. Verifikasi tab Asset Names: Button [+ Assign Asset Names], row action Move dan Unassign, bulk Move to another asset class dan Unassign: Show
29. Tutup menu baris dan hapus centang baris Wheel Loader

### TC-FA-FAAC-67

30. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Delete)
31. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
32. Ketik Search `HEAVY-EQ`, tekan Enter
33. Klik Class Code HEAVY-EQ untuk membuka Detail mode Edit
34. Verifikasi tab General, Depreciation, Accounts, dan Asset Names serta Alert versi Scheduled "Next version starts <M+2 dalam format MMM yyyy>.": Show
35. Verifikasi Button [Cancel scheduled version] pada Alert: Hidden
36. Arahkan kursor ke field Class Name pada tab General
37. Verifikasi tooltip "You don't have permission to edit." tampil
38. Verifikasi field halaman Detail mode Edit tetap tampil (visible) namun berstatus Disabled
39. Verifikasi Button [Save] dan [Clear Field]: Hidden
40. Klik tab Accounts, lalu klik Select akun Asset Cost
41. Verifikasi Select akun tidak dapat dibuka karena Disabled sehingga shortcut "+ Create account" tidak tersedia
42. Klik tab Asset Names
43. Verifikasi tabel Asset Names tampil dengan baris Wheel Loader
44. Verifikasi tab Asset Names: Button [+ Assign Asset Names], row action Move dan Unassign, bulk Move to another asset class dan Unassign: Hidden

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec ini melewati sekitar 35 langkah. Alasan: ketiga blok satu kelas (Role Matrix) dan satu topik (visibilitas elemen Detail mode Edit per role), tiap blok role berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected tiap TC memuat enam klausa yang masing-masing wajib punya `Verifikasi` sendiri (S-01).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 29 (menutup menu dan menghapus centang agar state tidak terbawa, S-09), langkah 14 dan 30 (ganti akun), langkah 15 dan 31 (membuka tab Asset Class sesudah login ulang, S-07).
- Search `HEAVY-EQ` (langkah 1, 16, dan 32) mendahului aksi pada baris HEAVY-EQ karena baris itu tidak dijamin berada di halaman 1 (R-16).
- Asersi Hidden dan Disabled didahului asersi Show elemen halaman yang sama pada langkah pertama tiap blok sebagai anchor positif permukaan (bagian 8b butir 2); untuk baris tab Asset Names role tanpa hak tulis, `Verifikasi` baris Wheel Loader tampil adalah anchor bagi asersi Hidden.
- Langkah TC "Buka Select akun Asset Cost bila field dapat diubah" ditulis deterministik: role yang dapat mengubah field membuka dropdown dan diasersi shortcutnya; role lain mencoba mengklik Select dan mengasersi tidak dapat dibuka.
- Temuan untuk QA:
  - TC tidak menyebut field mana yang di-hover untuk tooltip "You don't have permission to edit." pada role tanpa hak ubah; spec memakai field Class Name.
  - TC tidak menyebut cara menampilkan bulk action tab Asset Names; spec mencentang baris Wheel Loader untuk memunculkan bulk Move to another asset class dan Unassign pada role yang memiliki kolom checkbox, dan menambah klik tombol ⋯ baris yang sama untuk membaca row action.
