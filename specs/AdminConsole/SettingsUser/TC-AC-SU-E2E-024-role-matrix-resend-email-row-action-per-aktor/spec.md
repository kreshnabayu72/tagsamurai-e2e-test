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
10. Ketik Search `{runId}-024`, tekan Enter
11. Klik (⋯) baris `Sarah Lee {runId}-024`
12. Verifikasi Manage user and role (U=true): menu `Sarah Lee {runId}-024` berisi `Resend Activation Email`
13. Tutup menu row action dengan Esc
14. Klik (⋯) baris `Rina Putri {runId}-024`
15. Verifikasi Manage user and role (U=true): menu `Rina Putri {runId}-024` berisi `Resend Confirmation Email`
16. Tutup menu row action dengan Esc
17. Klik (⋯) baris `Dewi Lestari {runId}-024`
18. Verifikasi `Resend Confirmation Email` pada menu `Dewi Lestari {runId}-024` tampil dan enabled
19. Tutup menu row action dengan Esc
20. Atur email aktor menjadi Pending Email Confirmation lewat Fixture BE
21. Muat ulang halaman dengan F5
22. Ketik Search `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
23. Klik (⋯) baris aktor sendiri
24. Verifikasi menu aktor sendiri: `Detail | Resend Confirmation Email`
25. Verifikasi switch Active baris aktor sendiri tetap disabled
26. Tutup menu row action dengan Esc
27. Pulihkan email aktor ke keadaan awal lewat Fixture BE

### TC-AC-SU-71, 152: Resend Email row action, aktor Read Only

28. Logout dari akun aktor saat ini
29. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
30. Ketik Search `{runId}-024`, tekan Enter
31. Klik (⋯) baris `Sarah Lee {runId}-024`
32. Verifikasi Read Only: menu `Sarah Lee {runId}-024` hanya berisi `Detail`
33. Tutup menu row action dengan Esc
34. Klik (⋯) baris `Rina Putri {runId}-024`
35. Verifikasi Read Only: menu `Rina Putri {runId}-024` hanya berisi `Detail`
36. Tutup menu row action dengan Esc
37. Klik (⋯) baris `Mike Tan {runId}-024`
38. Verifikasi row action `Mike Tan {runId}-024` hanya `Detail` (Resend Hidden)
39. Tutup menu row action dengan Esc
40. Buka Detail `Mike Tan {runId}-024` dengan klik Name
41. Verifikasi Breadcrumb Detail tampil
42. Verifikasi header Detail tanpa tombol Resend
43. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-71, 153: Resend Email row action, aktor Manage user and role (U=false)

44. Logout dari akun aktor saat ini
45. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
46. Ketik Search `{runId}-024`, tekan Enter
47. Klik (⋯) baris `Sarah Lee {runId}-024`
48. Verifikasi Manage user and role (U=false): menu `Sarah Lee {runId}-024` hanya berisi `Detail`
49. Tutup menu row action dengan Esc
50. Klik (⋯) baris `Rina Putri {runId}-024`
51. Verifikasi Manage user and role (U=false): menu `Rina Putri {runId}-024` hanya berisi `Detail`
52. Tutup menu row action dengan Esc
53. Klik (⋯) baris `Mike Tan {runId}-024`
54. Verifikasi menu `Mike Tan {runId}-024` hanya berisi `Detail` (Resend Hidden)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), semua langkah "Tutup menu row action dengan Esc" (termasuk 4), langkah 20 (pengaturan precondition TC-AC-SU-140), langkah 27 (pemulihan state, S-09), serta langkah kembali ke daftar. Langkah 40 dan 41 (buka Detail dan Breadcrumb Detail tampil) adalah langkah penghubung dan anchor positif tambahan (S-03, dasar 8b.2) bagi absence tombol Resend pada langkah 42.
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit; empat akun dipakai berurutan, masing-masing satu kali. Subjudul memetakan langkah ke id TC.
- Ukuran spec (54 langkah, di atas smell sekitar 35 langkah): Role Matrix satu permukaan (row action Resend) dengan empat akun dan pola identik per akun (buka, `Verifikasi`, tutup); tiap blok akun berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-140 mensyaratkan email aktor berstatus Pending Email Confirmation; aktor adalah akun Pre-setup #4, sehingga pengecualian S-06 dipakai lewat Fixture BE (pengecualian untuk TC-140/141 sudah tertulis di `suite.md`).
  - TC-AC-SU-71, 72, 140 memakai nama aktor atau target yang tidak dipetakan ke Pre-setup; spec memakai akun Pre-setup #2, #3, #4, #5.
  - TC-AC-SU-152 dan TC-AC-SU-153 menyebut `Mike Tan` tanpa status; spec men-seed Pending Activation supaya opsi Resend relevan untuk Hidden.
  - Nama user TC (`Sarah Lee`, `Rina Putri`, `Dewi Lestari`, `Mike Tan`) dipakai sebagai nama bersuffix `{runId}-024` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
