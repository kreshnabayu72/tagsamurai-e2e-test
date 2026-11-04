---
id: TC-AC-SU-E2E-024-role-matrix-resend-email-row-action-per-aktor
title: "Role Matrix: Row Action Resend Activation Email dan Resend Confirmation Email per Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-71
  - TC-AC-SU-72
  - TC-AC-SU-140
  - TC-AC-SU-152
  - TC-AC-SU-153
coverage:
  web: automated
---

# Role Matrix: Row Action Resend Activation Email dan Resend Confirmation Email per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun aktor: Manage user and role Read saja (U=false, Pre-setup #5) `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD`, `AC_MUR_READ_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-71 | Total Control | Pre-setup #2 |
| TC-AC-SU-71, 72, 140 | Manage user and role (U=true) | Pre-setup #4 |
| TC-AC-SU-71, 152 | Read Only | Pre-setup #3 |
| TC-AC-SU-71, 153 | Manage user and role (U=false) | Pre-setup #5 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-71 | `Sarah Lee` | `Sarah Lee {runId}-024` | `sarahlee+{runId}-024@qwertysystem.net` | Pending Activation |
| TC-AC-SU-71 | `Rina Putri` | `Rina Putri {runId}-024` | `rinaputri+{runId}-024@qwertysystem.net` | Pending Email Confirmation |
| TC-AC-SU-72 | `Dewi Lestari` | `Dewi Lestari {runId}-024` | `dewilestari+{runId}-024@qwertysystem.net` | Total Control; Pending Email Confirmation |
| TC-AC-SU-152, 153 | `Mike Tan` | `Mike Tan {runId}-024` | `miketan+{runId}-024@qwertysystem.net` | Pending Activation |

- Data Pre-setup yang diubah (TC-AC-SU-140, S-06 pengecualian data yang tidak dapat dimiliki spec): akun aktor Manage user and role (U=true, Pre-setup #4) diberi email pending (Pending Email Confirmation) lewat Fixture BE, dan dipulihkan ke keadaan awal di hook `after` dan langkah akhir blok; efek pada Last Updated dan Modified By akun aktor dicatat sebagai efek spec ini.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-71: Resend Email row action, aktor Total Control

1. Ketik Search `{runId}-024`, tekan Enter
2. Klik (⋯) baris `Sarah Lee {runId}-024`
3. Verifikasi Total Control: menu `Sarah Lee {runId}-024` berisi `Resend Activation Email`
4. Tutup menu row action dengan Esc
5. Klik (⋯) baris `Rina Putri {runId}-024`
6. Verifikasi Total Control: menu `Rina Putri {runId}-024` berisi `Resend Confirmation Email`
7. Tutup menu row action dengan Esc

### TC-AC-SU-71, 72, 140: Resend Email row action, aktor Manage user and role (U=true)

8. Logout dari akun aktor saat ini
9. Login sebagai Manage user and role (Update, U=true) (`manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_UPDATE_PASSWORD`)
10. Buka Settings > User lewat sidebar
11. Ketik Search `{runId}-024`, tekan Enter
12. Klik (⋯) baris `Sarah Lee {runId}-024`
13. Verifikasi Manage user and role (U=true): menu `Sarah Lee {runId}-024` berisi `Resend Activation Email`
14. Tutup menu row action dengan Esc
15. Klik (⋯) baris `Rina Putri {runId}-024`
16. Verifikasi Manage user and role (U=true): menu `Rina Putri {runId}-024` berisi `Resend Confirmation Email`
17. Tutup menu row action dengan Esc
18. Klik (⋯) baris `Dewi Lestari {runId}-024`
19. Verifikasi `Resend Confirmation Email` pada menu `Dewi Lestari {runId}-024` tampil dan enabled
20. Tutup menu row action dengan Esc
21. Atur email aktor menjadi Pending Email Confirmation lewat Fixture BE
22. Muat ulang halaman dengan F5
23. Ganti isi kotak search dengan `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
24. Klik (⋯) baris aktor sendiri
25. Verifikasi menu aktor sendiri: `Detail | Resend Confirmation Email`
26. Verifikasi switch Active baris aktor sendiri tetap disabled
27. Tutup menu row action dengan Esc
28. Pulihkan email aktor ke keadaan awal lewat Fixture BE

### TC-AC-SU-71, 152: Resend Email row action, aktor Read Only

29. Logout dari akun aktor saat ini
30. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
31. Buka Settings > User lewat sidebar
32. Ketik Search `{runId}-024`, tekan Enter
33. Klik (⋯) baris `Sarah Lee {runId}-024`
34. Verifikasi Read Only: menu `Sarah Lee {runId}-024` hanya berisi `Detail`
35. Tutup menu row action dengan Esc
36. Klik (⋯) baris `Rina Putri {runId}-024`
37. Verifikasi Read Only: menu `Rina Putri {runId}-024` hanya berisi `Detail`
38. Tutup menu row action dengan Esc
39. Klik (⋯) baris `Mike Tan {runId}-024`
40. Verifikasi row action `Mike Tan {runId}-024` hanya `Detail` (Resend Hidden)
41. Tutup menu row action dengan Esc
42. Buka Detail `Mike Tan {runId}-024` dengan klik Name
43. Verifikasi Breadcrumb `Settings > User > Detail` tampil
44. Verifikasi header Detail tanpa tombol Resend
45. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-71, 153: Resend Email row action, aktor Manage user and role (U=false)

46. Logout dari akun aktor saat ini
47. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
48. Buka Settings > User lewat sidebar
49. Ketik Search `{runId}-024`, tekan Enter
50. Klik (⋯) baris `Sarah Lee {runId}-024`
51. Verifikasi Manage user and role (U=false): menu `Sarah Lee {runId}-024` hanya berisi `Detail`
52. Tutup menu row action dengan Esc
53. Klik (⋯) baris `Rina Putri {runId}-024`
54. Verifikasi Manage user and role (U=false): menu `Rina Putri {runId}-024` hanya berisi `Detail`
55. Tutup menu row action dengan Esc
56. Klik (⋯) baris `Mike Tan {runId}-024`
57. Verifikasi menu `Mike Tan {runId}-024` hanya berisi `Detail` (Resend Hidden)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), semua langkah "Tutup menu row action dengan Esc" (termasuk 4), langkah 10, 31, 48 (buka Settings > User lewat sidebar sesudah login ulang), langkah 21 (pengaturan precondition TC-AC-SU-140), langkah 28 (pemulihan state, S-09), serta langkah kembali ke daftar. Langkah 43 dan 44 (buka Detail dan Breadcrumb `Settings > User > Detail` tampil) adalah langkah penghubung dan anchor positif tambahan (S-03, dasar 8b.2) bagi absence tombol Resend pada langkah 45.
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit; empat akun dipakai berurutan, masing-masing satu kali. Subjudul memetakan langkah ke id TC.
- Ukuran spec (57 langkah, di atas smell sekitar 35 langkah): Role Matrix satu permukaan (row action Resend) dengan empat akun dan pola identik per akun (buka, `Verifikasi`, tutup); tiap blok akun berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Spec ini matriks visibilitas per role (bagian 3a): memuat asersi tampil (Total Control, Manage user and role U=true) dan Hidden (Read Only, Manage user and role U=false) dalam satu spec; `caseType` Positive mengikuti bagian 8.
- Temuan untuk QA:
  - TC-AC-SU-140 mensyaratkan email aktor berstatus Pending Email Confirmation; aktor adalah akun Pre-setup #4, sehingga pengecualian S-06 dipakai lewat Fixture BE (pengecualian untuk TC-140/141 sudah tertulis di `suite.md`).
  - TC-AC-SU-71, 72, 140 memakai nama aktor atau target yang tidak dipetakan ke Pre-setup; spec memakai akun Pre-setup #2, #3, #4, #5.
  - TC-AC-SU-152 dan TC-AC-SU-153 menyebut `Mike Tan` tanpa status; spec men-seed Pending Activation supaya opsi Resend relevan untuk Hidden.
  - Nama user TC (`Sarah Lee`, `Rina Putri`, `Dewi Lestari`, `Mike Tan`) dipakai sebagai nama bersuffix `{runId}-024` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
