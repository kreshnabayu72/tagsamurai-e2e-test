---
id: TC-AC-SU-E2E-021-role-matrix-tab-role-global-role-per-aktor-dan-target
title: "Role Matrix: Tab Role Global Role, Aktor Manage user and role (Update) per Target"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-62
coverage:
  web: automated
---

# Role Matrix: Tab Role Global Role, Aktor Manage user and role (Update) per Target

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Manage user and role (Update, U=true); halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-62 | Manage user and role (U=true) | Pre-setup #4 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-62 | `Rudi Hartono` | `Rudi Hartono {runId}-021` | `rudihartono+{runId}-021@qwertysystem.net` | tanpa tingkat akses (kosong) |
| TC-AC-SU-62 | `Dewi Lestari` | `Dewi Lestari {runId}-021` | `dewilestari+{runId}-021@qwertysystem.net` | Total Control |
| TC-AC-SU-62 | `Dedi Kurnia` | `Dedi Kurnia {runId}-021` | `dedikurnia+{runId}-021@qwertysystem.net` | Group Manager |

- Baris Default User (Pre-setup #1) dan baris aktor sendiri dicari lewat Search atas email akun masing-masing; keduanya tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-62: Tab Role Global Role, aktor Manage user and role (Update) per target

1. Ketik Search `Rudi Hartono {runId}-021`, tekan Enter
2. Klik Name `Rudi Hartono {runId}-021`
3. Hover switch dan checkbox C/U/D baris `Manage group` pada sub-tab Global Role
4. Verifikasi `Rudi Hartono {runId}-021`: switch dan C/U/D enabled
5. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
6. Ganti isi kotak search dengan `Dewi Lestari {runId}-021`, tekan Enter
7. Klik Name `Dewi Lestari {runId}-021`
8. Hover switch baris `Manage group` pada sub-tab Global Role
9. Verifikasi `Dewi Lestari {runId}-021`: switch tampil namun disabled dengan tooltip `You don't have permission to edit.`
10. Hover checkbox C baris `Manage group` pada sub-tab Global Role
11. Verifikasi `Dewi Lestari {runId}-021`: checkbox C tampil namun disabled dengan tooltip `You don't have permission to edit.`
12. Hover checkbox U baris `Manage group` pada sub-tab Global Role
13. Verifikasi `Dewi Lestari {runId}-021`: checkbox U tampil namun disabled dengan tooltip `You don't have permission to edit.`
14. Hover checkbox D baris `Manage group` pada sub-tab Global Role
15. Verifikasi `Dewi Lestari {runId}-021`: checkbox D tampil namun disabled dengan tooltip `You don't have permission to edit.`
16. Verifikasi banner `This user has Total Control access.`
17. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
18. Ganti isi kotak search dengan `Dedi Kurnia {runId}-021`, tekan Enter
19. Klik Name `Dedi Kurnia {runId}-021`
20. Hover switch dan checkbox C/U/D baris `Manage group` pada sub-tab Global Role
21. Verifikasi `Dedi Kurnia {runId}-021`: switch dan C/U/D Global Role enabled
22. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
23. Ganti isi kotak search dengan `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
24. Klik Name baris aktor sendiri
25. Hover switch baris `Manage group` pada sub-tab Global Role
26. Verifikasi aktor sendiri: switch tampil namun disabled dengan tooltip `You can't manage your own account from here.`
27. Hover checkbox C baris `Manage group` pada sub-tab Global Role
28. Verifikasi aktor sendiri: checkbox C tampil namun disabled dengan tooltip `You can't manage your own account from here.`
29. Hover checkbox U baris `Manage group` pada sub-tab Global Role
30. Verifikasi aktor sendiri: checkbox U tampil namun disabled dengan tooltip `You can't manage your own account from here.`
31. Hover checkbox D baris `Manage group` pada sub-tab Global Role
32. Verifikasi aktor sendiri: checkbox D tampil namun disabled dengan tooltip `You can't manage your own account from here.`
33. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
34. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
35. Klik Name baris Default User
36. Verifikasi Default User: semua switch ON dan semua CRUD checked
37. Hover switch baris `Manage group` pada sub-tab Global Role
38. Verifikasi Default User: switch tampil namun disabled dengan tooltip `Default User cannot be modified.`
39. Hover checkbox C baris `Manage group` pada sub-tab Global Role
40. Verifikasi Default User: checkbox C tampil namun disabled dengan tooltip `Default User cannot be modified.`
41. Hover checkbox U baris `Manage group` pada sub-tab Global Role
42. Verifikasi Default User: checkbox U tampil namun disabled dengan tooltip `Default User cannot be modified.`
43. Hover checkbox D baris `Manage group` pada sub-tab Global Role
44. Verifikasi Default User: checkbox D tampil namun disabled dengan tooltip `Default User cannot be modified.`
45. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
46. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), semua langkah kembali ke daftar lewat Breadcrumb, langkah 46 (reset Search). Layar awal dibuka hook `beforeEach` suite; sub-tab Global Role aktif secara default pada Tab Role.
- Spec ini matriks visibilitas per target (bagian 3a): memuat asersi enabled (target tanpa tingkat akses dan Group Manager) dan disabled (target Total Control, aktor sendiri, Default User) dalam satu spec; polaritas campuran disengaja karena TC-AC-SU-62 menguji satu matriks; `caseType` Positive mengikuti bagian 8.
- Ukuran spec (46 langkah, di atas smell sekitar 35 langkah): satu TC pada satu akun dengan lima target; untuk target disabled (Total Control, aktor sendiri, Default User) tiap elemen (switch, checkbox C, U, D) di-hover satu per satu dan tooltipnya diasersi sebelum hover berikutnya (bagian 8b butir 5), sehingga tiap target menjadi delapan langkah; tiap target berdiri sendiri (mulai dan berakhir di User List).
- Pembagian TC Role Matrix Tab Role: TC-AC-SU-62 di spec ini, TC-AC-SU-63 dan 64 di spec 201, TC-AC-SU-65 di spec 202. Tiap spec memakai akun dan data seed sendiri.
- Temuan untuk QA:
  - TC-AC-SU-62 memakai nama aktor `Mike Tan`, `Fajar Nugroho` yang tidak dipetakan ke Pre-setup; spec memakai akun Pre-setup #4.
  - TC-AC-SU-62: baris yang dihover adalah `Manage group` (TC menyebut baris `Manage group` hanya pada langkah 2); target diasumsikan memiliki baris itu pada sub-tab Global Role.
  - TC-AC-SU-62 menyebut Group Role `Rudi Hartono` "kosong"; spec men-seed `Rudi Hartono` tanpa tingkat akses.
  - Nama user TC (`Rudi Hartono`, `Dewi Lestari`, `Dedi Kurnia`) dipakai sebagai nama bersuffix `{runId}-021` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
