---
id: TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only
title: Role Matrix - UI Visibility Principal Read Only, Create-Only, Update-Only, dan Delete-Only
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-60
  - TC-AC-PF-61
  - TC-AC-PF-62
  - TC-AC-PF-63
  - TC-AC-PF-64
coverage:
  web: automated
---

# Role Matrix - UI Visibility Principal Read Only, Create-Only, Update-Only, dan Delete-Only

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Read Only (Principal) | #2 readOnlyPrincipal | `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_RO_PASSWORD` | langkah 1 sampai 21 |
| Create-Only (Principal) | #3 createOnlyPrincipal | `createOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_CO_PASSWORD` | langkah 22 sampai 28 |
| Update-Only (Principal) | #4 updateOnlyPrincipal | `updateOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_UO_PASSWORD` | langkah 29 sampai 37 |
| Delete-Only (Principal) | #5 deleteOnlyPrincipal | `deleteOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DO_PASSWORD` | langkah 38 sampai 45 |

- Login di hook `before` spec ini sebagai #2; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Growth dan lainnya; default archived `Growth Plus (old)`; custom aktif `Growth Tier`; custom archived `Enterprise Reseller`), Dataset Plan R (default archived `Plan Arsip Lama`, Clients 0), Dataset Plan D (plan `Growth` dengan client `PT Wahana Nusantara` pada Tab Assigned Clients; aktor #2 membaca baris itu tanpa mengubahnya). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Read Only (Principal): TC-AC-PF-60 dan TC-AC-PF-61

1. Verifikasi toolbar sub-tab Active tab Default tanpa `+ Default Plan`.
2. Buka Overlay Row Action pada baris Active `Growth`.
3. Verifikasi Overlay Row Action baris Active hanya memuat `Detail`.
4. Buka Plan Detail `Growth` (klik Plan Name).
5. Verifikasi header memuat ikon Download saja; `Edit` dan `Archive` Hidden.
6. Klik Tab Assigned Clients.
7. Buka Overlay Row Action pada baris client `PT Wahana Nusantara`.
8. Verifikasi row action baris hanya `Detail`; `Push Update` Hidden.
9. Kembali ke list lewat Breadcrumb.
10. Verifikasi tab `Global Settings` tidak tampil pada deretan tab di atas tabel list.
11. Klik sub-tab Archive.
12. Buka Overlay Row Action pada baris Archive `Growth Plus (old)`.
13. Verifikasi Overlay Row Action baris Archive hanya memuat `Detail`.
14. Klik tab Custom.
15. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
16. Buka Overlay Row Action pada baris Active `Growth Tier`.
17. Verifikasi Overlay Row Action baris Active hanya memuat `Detail`.
18. Klik sub-tab Archive.
19. Buka Overlay Row Action pada baris Archive `Enterprise Reseller`.
20. Verifikasi Overlay Row Action baris Archive hanya memuat `Detail`.
21. Verifikasi ikon Search, Filter, Download, Changelog tampil dan aktif.

### Blok Create-Only (Principal): TC-AC-PF-62

22. Ganti akun: logout, lalu login sebagai Create-Only (Principal) (#3).
23. Verifikasi toolbar sub-tab Active tab Default memuat `+ Default Plan`.
24. Buka Overlay Row Action pada baris Active `Growth`.
25. Verifikasi Overlay Row Action hanya memuat `Detail`.
26. Klik tab Custom.
27. Verifikasi toolbar tab Custom memuat `+ Custom Plan`.
28. Verifikasi tab `Global Settings` tidak tampil.

### Blok Update-Only (Principal): TC-AC-PF-63

29. Ganti akun: logout, lalu login sebagai Update-Only (Principal) (#4).
30. Verifikasi toolbar sub-tab Active tab Default tanpa `+ Default Plan`.
31. Buka Overlay Row Action pada baris Active `Growth`.
32. Verifikasi Overlay Row Action memuat `Detail` dan `Edit` tanpa `Archive`.
33. Klik tab Custom.
34. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
35. Buka Overlay Row Action pada baris Active `Growth Tier`.
36. Verifikasi Overlay Row Action memuat `Detail` dan `Edit` tanpa `Archive`.
37. Verifikasi tab `Global Settings` tampil.

### Blok Delete-Only (Principal): TC-AC-PF-64

38. Ganti akun: logout, lalu login sebagai Delete-Only (Principal) (#5).
39. Verifikasi toolbar sub-tab Active tab Default tanpa tombol create.
40. Buka Overlay Row Action pada baris Active `Growth`.
41. Verifikasi Overlay Row Action baris Active memuat `Detail` dan `Archive` tanpa `Edit`.
42. Klik sub-tab Archive.
43. Buka Overlay Row Action pada plan archived yang tidak pernah dipakai `Plan Arsip Lama`.
44. Verifikasi Overlay Row Action `Plan Arsip Lama` memuat `Detail` dan `Delete`.
45. Verifikasi tab `Global Settings` tidak tampil.

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`) dan langkah tiap role berbeda (capability berbeda menghasilkan hasil Hidden berbeda). Langkah 22, 29, dan 38 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 4 sampai 9 menyisipkan TC-AC-PF-61 di tengah pengamatan TC-AC-PF-60 agar Plan Detail dan Tab Assigned Clients dibuka sekali; langkah 11, 14, 18, 26, 33, 42 (pindah tab dan sub-tab).
- Urutan TC: Verifikasi TC-AC-PF-61 Expected c (tab `Global Settings` tidak tampil) ada di langkah 10, sesudah kembali ke list, karena TC menyebut "deretan tab di atas tabel list". Overlay Row Action diverifikasi pada satu baris wakil per permukaan (Default Active, Default Archive, Custom Active, Custom Archive).
- Alasan melewati sekitar 35 langkah: seluruh blok berkelas Role Matrix visibilitas satu halaman dengan dataset yang sama dan tiap blok role berdiri sendiri; kegagalan satu blok tidak membuat blok role lain kehilangan makna. Elemen yang diverifikasi dihitung per klausa (S-01) dan tiap permukaan tabel memerlukan pembukaan Overlay Row Action sendiri.
- Temuan untuk QA:
  - TC-AC-PF-61 precondition menyebut Dataset Plan D untuk Assigned Clients, tetapi Pre-setup #2 (`readOnlyPrincipal`) tidak mencantumkan Group Role Manage active client; Expected b hanya menyebut "baris" tanpa nama client. Spec memakai `PT Wahana Nusantara` (Dataset Plan D) sebagai baris wakil.
  - TC-AC-PF-60 Expected b menyebut "semua baris Active dan Archive"; spec memverifikasi satu baris per permukaan (langkah 3, 13, 17, 20).
  - TC-AC-PF-62 dan 63 langkah 2 hanya menyebut "baris Active" tanpa tab; spec memverifikasinya pada tab Default (langkah 24, 31) dan, untuk TC-AC-PF-63, juga pada tab Custom (langkah 35).
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
