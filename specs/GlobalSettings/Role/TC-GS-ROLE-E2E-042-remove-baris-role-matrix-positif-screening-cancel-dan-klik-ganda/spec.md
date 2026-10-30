---
id: TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda
title: "Role Matrix: Remove Baris Role Positif (Screening, Cancel, Konfirmasi, dan Klik Ganda)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-110
  - TC-GS-ROLE-111
  - TC-GS-ROLE-112
  - TC-GS-ROLE-113
  - TC-GS-ROLE-119
coverage:
  web: automated
---

# Role Matrix: Remove Baris Role Positif (Screening, Cancel, Konfirmasi, dan Klik Ganda)

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Karena spec berakhir di akun Hendra Wijaya, hook `after` mengembalikan sesi ke akun default suite (Ahmad Fauzi).
- Langkah tiap role berbeda, sehingga spec ditulis per blok role (Total Control untuk TC-GS-ROLE-110, 111, 112, 119; Manage user and role C/R/U/D untuk TC-GS-ROLE-113), bukan perulangan.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-110, TC-GS-ROLE-111, TC-GS-ROLE-112, TC-GS-ROLE-119 | Total Control | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-113 | Manage user and role C/R/U/D | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` |

- Env baru yang harus didaftarkan di `executionConfig.environmentVariables` dan `.env.example`: `GS_ROLE_MANAGE_CRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup #10: Doni Pratama (Staff, IT; bukan Total Control atau Read Only) punya baris Manage TAG (Read) dan Manage files (Read, Delete). Target TC-GS-ROLE-110, 111, dan 112.
- Data Given (disiapkan di hook `before` lewat seeding API, kemampuan disediakan tim FE/BE; dipakai sebagai precondition TC): Nina Kartika (Pre-setup #11) memiliki baris `Manage files` (target TC-GS-ROLE-113) dan Wawan Setiawan (Pre-setup #11) memiliki baris `Manage hardware` (target TC-GS-ROLE-119); keduanya bukan Total Control atau Read Only.
- Data yang diubah spec: baris `Manage TAG` Doni Pratama dihapus (TC-GS-ROLE-112), baris `Manage files` Nina Kartika dihapus (TC-GS-ROLE-113), dan baris `Manage hardware` Wawan Setiawan dihapus (TC-GS-ROLE-119). Hook `after` memulihkan baris `Manage TAG` Doni Pratama (Read) ke kondisi Pre-setup #10 lewat seeding API; Nina Kartika dan Wawan Setiawan kembali ke kondisi kandidat Pre-setup #11 (tanpa baris role) sehingga tidak perlu pemulihan lain.
- Kemampuan teknis: klik ganda cepat pada `[Remove]` (dua klik berurutan tanpa jeda yang disengaja); hover pada komponen user di dialog; baseline entry Changelog dibaca dari Modal Changelog; Logout dan login ulang di browser yang sama.
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-110: Screening overlay row action dan dialog Remove baris target biasa

1. Klik Role Name `Manage TAG`
2. Klik `(⋯)` baris Doni Pratama
3. Verifikasi overlay hanya berisi `Remove` dengan icon DeleteBin6Line severity danger
4. Klik `Remove`
5. Verifikasi title dialog "Remove Access"
6. Verifikasi body dialog memuat komponen user (ikon user generik dan "Doni P")
7. Arahkan kursor ke komponen user "Doni P"
8. Verifikasi tooltip menampilkan nama lengkap "Doni Pratama"
9. Verifikasi body dialog memuat teks "This will remove Manage TAG access from this user. Are you sure you want to remove it?"
10. Verifikasi tombol `[Cancel]` (contrast) dan `[Remove]` (danger) tampil
11. Klik `[Cancel]`

### TC-GS-ROLE-111: Cancel dialog Remove baris target biasa

12. Klik `(⋯)` baris Doni Pratama
13. Klik `Remove`
14. Klik `[Cancel]`
15. Verifikasi tidak ada toast
16. Verifikasi dialog tertutup
17. Verifikasi baris Doni Pratama tetap ada

### TC-GS-ROLE-112: Remove baris role target biasa oleh Total Control

18. Klik segmen `System` pada breadcrumb untuk membuka Tab System
19. Catat jumlah Users baris `Manage TAG` di Tab System (N112)
20. Klik Role Name `Manage TAG`
21. Klik `(⋯)` baris Doni Pratama
22. Klik `Remove`
23. Klik `[Remove]`
24. Verifikasi toast sukses "Success, user has been removed."
25. Verifikasi baris Doni Pratama hilang dari Detail `Manage TAG`
26. Klik segmen `System` pada breadcrumb untuk membuka Tab System
27. Verifikasi Users baris `Manage TAG` sama dengan N112 dikurangi 1
28. Klik Role Name `Manage files`
29. Verifikasi baris Doni Pratama di Detail `Manage files` tetap ada

### TC-GS-ROLE-119: Klik ganda [Remove] dialog Remove baris role

30. Klik segmen `System` pada breadcrumb untuk membuka Tab System
31. Klik Role Name `Manage hardware`
32. Klik `Changelog`
33. Catat jumlah entry Remove untuk Wawan Setiawan di Modal Changelog `Manage hardware` (K119)
34. Tutup Modal Changelog dengan `✕`
35. Tunggu toast lama hilang otomatis
36. Klik `(⋯)` baris Wawan Setiawan
37. Klik `Remove`
38. Klik `[Remove]` dua kali cepat
39. Verifikasi satu toast sukses "Success, user has been removed."
40. Klik `Changelog`
41. Verifikasi Modal Changelog `Manage hardware` tampil
42. Verifikasi jumlah entry Remove untuk Wawan Setiawan sama dengan K119 ditambah 1 (tepat 1 entry baru)
43. Tutup Modal Changelog dengan `✕`

### TC-GS-ROLE-113: Manage user and role dengan Update menghapus baris role

44. Logout, lalu login sebagai Manage user and role C/R/U/D (Hendra Wijaya)
45. Buka Global Settings > Role & Permission > Tab System
46. Klik Role Name `Manage files`
47. Klik `(⋯)` baris Nina Kartika
48. Klik `Remove`
49. Klik `[Remove]`
50. Verifikasi toast sukses "Success, user has been removed."
51. Verifikasi baris Nina Kartika hilang dari Detail `Manage files`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Spec Role Matrix positif (bagian 3a konvensi): aksi Remove baris role berhasil untuk Total Control dan Manage user and role dengan Update. Kombinasi role lain tanpa TC sumber tidak ditambahkan.
- Spec melewati sekitar 35 langkah (51 langkah) karena kelima TC berada di satu kelas harness (fungsional, Remove baris pada Detail) dengan role matrix yang sama; tiap blok TC memakai user target dan Detail sendiri (Doni Pratama, Wawan Setiawan, Nina Kartika) dan dimulai dari Tab System, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok Hendra Wijaya terakhir karena berganti akun.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup dialog dengan `[Cancel]` (langkah 11), membuka Tab System lewat breadcrumb (langkah 18, 26, 30), mencatat baseline Users dan Changelog (langkah 19 dan 32 sampai 34), menutup Modal Changelog (langkah 43), menunggu toast lama hilang (langkah 35), serta Logout dan login ke akun berikutnya (langkah 44 dan 45).
- Urutan TC sumber diubah: TC-GS-ROLE-119 dijalankan sebelum TC-GS-ROLE-113 karena TC-GS-ROLE-113 memakai akun Hendra Wijaya sehingga ditaruh terakhir (satu kali ganti akun). Remove yang berhasil (TC-GS-ROLE-112, 119, 113) dijalankan sesudah Screening dan Cancel (TC-GS-ROLE-110 dan 111) karena aksi yang menghapus baris ditaruh sesudah kasus yang masih membutuhkan baris Doni Pratama (prinsip 5 bagian 3).
- Langkah 15 (tidak ada toast) diletakkan segera sesudah pemicu `[Cancel]` (butir 11 bagian 8b). Langkah 25 (baris hilang) memakai toast sukses langkah 24 sebagai anchor.
- Asersi tepat 1 entry Remove di Changelog (langkah 42) memakai baseline jumlah entry (langkah 33) dan didahului langkah 41 sebagai anchor bahwa modal sudah termuat.
- Temuan untuk QA:
  - TC-GS-ROLE-112 Post Condition (log Remove Field Access, menu TAG Doni Pratama hidden pada request berikutnya) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-ROLE-110, TC-GS-ROLE-111, TC-GS-ROLE-113, dan TC-GS-ROLE-119 tidak punya Post Condition.
  - TC-GS-ROLE-119 Expected b ("tepat 1 entry Remove") tidak menyebut cara menyaring entry per user atau jumlah awal; spec menghitung entry Remove yang menyebut Wawan Setiawan dengan baseline sebelum aksi.
  - TC-GS-ROLE-113 dan TC-GS-ROLE-119 menyebut baris target Nina Kartika dan Wawan Setiawan tanpa precondition baris role; spec menyiapkannya sebagai Given lewat seeding API.
