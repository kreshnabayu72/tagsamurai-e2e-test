---
id: TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target
title: "Role Matrix: Kontrol Baris User List untuk Aktor Manage user and role (Full CRUD) per Target (Normal, Holder Biasa, Default User, Self, Tier Total Control, Tier Read Only)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-54
  - TC-GS-USER-55
  - TC-GS-USER-56
  - TC-GS-USER-57
  - TC-GS-USER-58
  - TC-GS-USER-59
coverage:
  web: automated
---

# Role Matrix: Kontrol Baris User List untuk Aktor Manage user and role (Full CRUD) per Target (Normal, Holder Biasa, Default User, Self, Tier Total Control, Tier Read Only)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (satu role):

| Role | Akun | Nama user | Env var password |
|---|---|---|---|
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` | Fajar Nugroho (Tabel Pre-setup No. 4) | `Spectra.env.GS_FULLCRUD_PASSWORD` |

- Login akun Full CRUD (aktor pertama dan satu-satunya spec) dilakukan di hook `before`; tidak ada langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_FULLCRUD_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): target Normal Dewi Lestari (No. 12), target Holder biasa Ahmad Fauzi (No. 13, holder Manage user and role non-tier), target Default User Hendra Gunawan (No. 1), target Self Fajar Nugroho (No. 4, akun yang login), target Tier Total Control Andi Wijaya (No. 10), target Tier Read Only Doni Pratama (No. 11). Data Dinamis: tidak ada.
- Kemampuan teknis: hover elemen (checkbox, switch, opsi overlay) dan membaca tooltip; membaca state enabled atau disabled; menekan Esc.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-54: Kontrol baris target Normal untuk aktor Full CRUD

3. Verifikasi checkbox baris Dewi Lestari enabled
4. Verifikasi switch Active baris Dewi Lestari enabled
5. Klik (⋯) pada baris Dewi Lestari
6. Verifikasi overlay memuat opsi `Detail` | `Edit` | `Delete` enabled
7. Tutup overlay dengan menekan Esc

### TC-GS-USER-55: Kontrol baris target Holder biasa untuk aktor Full CRUD

8. Verifikasi checkbox baris Ahmad Fauzi enabled
9. Verifikasi switch Active baris Ahmad Fauzi enabled
10. Klik (⋯) pada baris Ahmad Fauzi
11. Verifikasi overlay memuat opsi `Detail` | `Edit` | `Delete` enabled
12. Tutup overlay dengan menekan Esc

### TC-GS-USER-56: Kontrol baris target Default User untuk aktor Full CRUD

13. Arahkan kursor ke checkbox baris Hendra Gunawan
14. Verifikasi checkbox baris Hendra Gunawan tampil namun disabled
15. Verifikasi tooltip `Default User cannot be modified.`
16. Arahkan kursor ke switch Active baris Hendra Gunawan
17. Verifikasi switch Active baris Hendra Gunawan tampil namun disabled
18. Verifikasi tooltip `Default User cannot be modified.`
19. Klik (⋯) pada baris Hendra Gunawan
20. Verifikasi opsi `Detail` enabled di overlay
21. Arahkan kursor ke opsi `Edit`
22. Verifikasi opsi `Edit` tampil namun disabled
23. Verifikasi tooltip `You don't have permission to edit.`
24. Arahkan kursor ke opsi `Delete`
25. Verifikasi opsi `Delete` tampil namun disabled
26. Verifikasi tooltip `Default User cannot be modified.`
27. Tutup overlay dengan menekan Esc

### TC-GS-USER-57: Kontrol baris target Self untuk aktor Full CRUD

28. Arahkan kursor ke checkbox baris Fajar Nugroho (akun sendiri)
29. Verifikasi checkbox baris Fajar Nugroho tampil namun disabled
30. Verifikasi tooltip `You can't manage your own account from here.`
31. Arahkan kursor ke switch Active baris Fajar Nugroho
32. Verifikasi switch Active baris Fajar Nugroho tampil namun disabled
33. Verifikasi tooltip `You can't manage your own account from here.`
34. Klik (⋯) pada baris Fajar Nugroho
35. Verifikasi opsi `Detail` dan `Edit` enabled di overlay
36. Arahkan kursor ke opsi `Delete`
37. Verifikasi opsi `Delete` tampil namun disabled
38. Verifikasi tooltip `You can't manage your own account from here.`
39. Tutup overlay dengan menekan Esc

### TC-GS-USER-58: Kontrol baris target Tier Total Control untuk aktor Full CRUD

40. Verifikasi baris Andi Wijaya tampil di tabel
41. Arahkan kursor ke checkbox baris Andi Wijaya
42. Verifikasi checkbox baris Andi Wijaya tampil namun disabled
43. Verifikasi tooltip `You don't have permission to edit.`
44. Arahkan kursor ke switch Active baris Andi Wijaya
45. Verifikasi switch Active baris Andi Wijaya tampil namun disabled
46. Verifikasi tooltip `You don't have permission to edit.`
47. Klik (⋯) pada baris Andi Wijaya
48. Verifikasi opsi `Detail` enabled di overlay
49. Arahkan kursor ke opsi `Edit`
50. Verifikasi opsi `Edit` tampil namun disabled
51. Verifikasi tooltip `You don't have permission to edit.`
52. Arahkan kursor ke opsi `Delete`
53. Verifikasi opsi `Delete` tampil namun disabled
54. Verifikasi tooltip `You don't have permission to edit.`
55. Tutup overlay dengan menekan Esc

### TC-GS-USER-59: Kontrol baris target Tier Read Only untuk aktor Full CRUD

56. Verifikasi baris Doni Pratama tampil di tabel
57. Arahkan kursor ke checkbox baris Doni Pratama
58. Verifikasi checkbox baris Doni Pratama tampil namun disabled
59. Verifikasi tooltip `You don't have permission to edit.`
60. Arahkan kursor ke switch Active baris Doni Pratama
61. Verifikasi switch Active baris Doni Pratama tampil namun disabled
62. Verifikasi tooltip `You don't have permission to edit.`
63. Klik (⋯) pada baris Doni Pratama
64. Verifikasi opsi `Detail` enabled di overlay
65. Arahkan kursor ke opsi `Edit`
66. Verifikasi opsi `Edit` tampil namun disabled
67. Verifikasi tooltip `You don't have permission to edit.`
68. Arahkan kursor ke opsi `Delete`
69. Verifikasi opsi `Delete` tampil namun disabled
70. Verifikasi tooltip `You don't have permission to edit.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi): satu role (Manage user and role Full CRUD) dengan enam target yang berbeda hasilnya; target Normal dan Holder biasa tidak ikut terlarang, sedangkan Default User, Self, dan target bertier terlindungi.
- Spec melewati sekitar 35 langkah (70 langkah) karena keenam blok satu kelas (kontrol baris, baca saja tanpa aksi yang mengubah data), satu akun, dan berbagi satu pembukaan List. Setiap elemen disabled butuh tiga langkah (hover, state, tooltip) dan keempat target terlindungi masing-masing punya tiga sampai empat elemen disabled; tiap blok TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (memilih 100 baris per halaman, supaya semua baris target tampil tanpa Search), serta langkah 7, 12, 27, 39, dan 55 (menutup overlay row action sebelum TC berikutnya).
- Langkah "Cari baris X" pada TC sumber dipenuhi dengan menemukan baris Name X di halaman 100 baris; langkah "Hover elemen yang disabled" pada TC-GS-USER-54 dan TC-GS-USER-55 tidak dijalankan karena tidak ada elemen disabled pada baris itu.
- Langkah 40 dan 56 (baris tampil di tabel) adalah Expected d TC-GS-USER-58 dan TC-GS-USER-59 ("baris tetap tampil, tidak disembunyikan"); keduanya diletakkan sebelum hover supaya baris dipastikan ada sebelum diamati.
- Temuan untuk QA:
  - TC-GS-USER-57 langkah 1 berbunyi "Cari baris baris akun sendiri" (kata ganda); spec memakai baris Fajar Nugroho (akun yang login).
  - TC-GS-USER-56 Expected c menyatakan `Edit` disabled dengan tooltip `You don't have permission to edit.` untuk Default User, sedangkan TC-GS-USER-50 (aktor Total Control) menyatakan `Edit` enabled; spec mengikuti masing-masing TC.
