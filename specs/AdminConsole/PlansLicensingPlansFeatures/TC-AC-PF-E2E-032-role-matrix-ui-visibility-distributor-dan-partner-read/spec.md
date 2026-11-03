---
id: TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read
title: Role Matrix - UI Visibility Distributor dan Partner Read Only, Create-Only, Update-Only, dan Delete-Only
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-70
  - TC-AC-PF-71
  - TC-AC-PF-72
  - TC-AC-PF-73
  - TC-AC-PF-74
coverage:
  web: automated
---

# Role Matrix - UI Visibility Distributor dan Partner Read Only, Create-Only, Update-Only, dan Delete-Only

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Read Only (Distributor) | #11 readOnlyDistributor | `readOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_RO_PASSWORD` | langkah 1 sampai 12 |
| Read Only (Partner) | #18 readOnlyPartner | `readOnlyPartner_automated_{namaCompany}@qwertysystem.net` | `AC_PF_PARTNER_RO_PASSWORD` | langkah 13 sampai 25 |
| Create-Only (Distributor) | #12 createOnlyDistributor | `createOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_CO_PASSWORD` | langkah 26 sampai 33 |
| Update-Only (Distributor) | #13 updateOnlyDistributor | `updateOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_UO_PASSWORD` | langkah 34 sampai 41 |
| Delete-Only (Distributor) | #14 deleteOnlyDistributor | `deleteOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_DO_PASSWORD` | langkah 42 sampai 49 |

- Login di hook `before` spec ini sebagai #11; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Starter, Growth, Professional, Enterprise, SIEM), Dataset Plan X (custom Distributor `Plan Distributor Satu` aktif dan `Plan Distributor Arsip` archived tidak pernah dipakai; custom Partner `Plan Partner Satu` aktif). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Read Only (Distributor): TC-AC-PF-70

1. Verifikasi toolbar sub-tab Active tab Default tanpa `+ Default Plan`.
2. Buka Overlay Row Action pada baris Active `Growth`.
3. Verifikasi Overlay Row Action hanya `Detail`.
4. Buka Plan Detail `Growth` (klik Plan Name).
5. Verifikasi header hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.
6. Kembali ke list lewat Breadcrumb.
7. Klik tab Custom.
8. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
9. Buka Overlay Row Action pada baris `Plan Distributor Satu`.
10. Verifikasi Overlay Row Action hanya `Detail`.
11. Buka Plan Detail `Plan Distributor Satu`.
12. Verifikasi header hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.

### Blok Read Only (Partner): TC-AC-PF-71

13. Ganti akun: logout, lalu login sebagai Read Only (Partner) (#18).
14. Verifikasi toolbar sub-tab Active tab Default tanpa `+ Default Plan`.
15. Buka Overlay Row Action pada baris Active `Growth`.
16. Verifikasi Overlay Row Action hanya `Detail`.
17. Buka Plan Detail `Growth` (klik Plan Name).
18. Verifikasi header hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.
19. Kembali ke list lewat Breadcrumb.
20. Klik tab Custom.
21. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
22. Buka Overlay Row Action pada baris `Plan Partner Satu`.
23. Verifikasi Overlay Row Action hanya `Detail`.
24. Buka Plan Detail `Plan Partner Satu`.
25. Verifikasi header hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.

### Blok Create-Only (Distributor): TC-AC-PF-72

26. Ganti akun: logout, lalu login sebagai Create-Only (Distributor) (#12).
27. Klik tab Custom.
28. Verifikasi toolbar tab Custom memuat `+ Custom Plan`.
29. Buka Overlay Row Action pada baris Active `Plan Distributor Satu`.
30. Verifikasi Overlay Row Action `Plan Distributor Satu` hanya `Detail`.
31. Klik sub-tab Archive.
32. Buka Overlay Row Action pada baris `Plan Distributor Arsip`.
33. Verifikasi Overlay Row Action `Plan Distributor Arsip` hanya `Detail`.

### Blok Update-Only (Distributor): TC-AC-PF-73

34. Ganti akun: logout, lalu login sebagai Update-Only (Distributor) (#13).
35. Klik tab Custom.
36. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
37. Buka Overlay Row Action pada baris Active `Plan Distributor Satu`.
38. Verifikasi Overlay Row Action `Plan Distributor Satu` memuat `Detail` dan `Edit` tanpa `Archive`.
39. Klik sub-tab Archive.
40. Buka Overlay Row Action pada baris `Plan Distributor Arsip`.
41. Verifikasi Overlay Row Action `Plan Distributor Arsip` hanya `Detail`.

### Blok Delete-Only (Distributor): TC-AC-PF-74

42. Ganti akun: logout, lalu login sebagai Delete-Only (Distributor) (#14).
43. Klik tab Custom.
44. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
45. Buka Overlay Row Action pada baris Active `Plan Distributor Satu`.
46. Verifikasi Overlay Row Action `Plan Distributor Satu` memuat `Detail` dan `Archive` tanpa `Edit`.
47. Klik sub-tab Archive.
48. Buka Overlay Row Action pada baris `Plan Distributor Arsip`.
49. Verifikasi Overlay Row Action `Plan Distributor Arsip` memuat `Delete`.

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`) dan langkah tiap role berbeda (capability berbeda menghasilkan hasil Hidden berbeda). Langkah 13, 26, 34, dan 42 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 6 dan 19 (kembali ke list), langkah 7, 20, 27, 31, 35, 39, 43, dan 47 (pindah tab dan sub-tab), dan langkah 4, 11, 17, 24 (membuka Plan Detail yang diasersi langkah berikutnya).
- Alasan melewati sekitar 35 langkah: seluruh blok berkelas Role Matrix visibilitas satu halaman dengan dataset yang sama dan tiap blok role berdiri sendiri; kegagalan satu blok tidak membuat blok role lain kehilangan makna. Lima role memerlukan lima Step Ganti akun dan pembukaan Overlay Row Action pada permukaan Custom Active dan Custom Archive per role.
- Temuan untuk QA:
  - TC-AC-PF-70 dan TC-AC-PF-71 Expected b ("Overlay Row Action hanya Detail") tidak menyebut sub-tab; spec memverifikasinya pada sub-tab Active tab Default dan tab Custom.
  - TC-AC-PF-74 Expected b menyebut "plan archived tidak pernah dipakai memuat Delete" tanpa menyebut opsi lain pada baris itu; spec memverifikasi `Delete` saja (langkah 49) dan tidak mengasersi kombinasi dengan `Detail`.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
