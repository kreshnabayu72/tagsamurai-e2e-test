---
id: TC-AC-PF-E2E-029-role-matrix-ui-visibility-principal-total-control-dan
title: Role Matrix - UI Visibility Principal Total Control dan Default User
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-57
  - TC-AC-PF-58
  - TC-AC-PF-59
  - TC-AC-PF-78
coverage:
  web: automated
---

# Role Matrix - UI Visibility Principal Total Control dan Default User

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Total Control (Principal) | #1 totalControlPrincipal | `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_TC_PASSWORD` | langkah 1 sampai 30 |
| Default User (Principal) | #6 defaultUserPrincipal | `defaultUserPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DU_PASSWORD` | langkah 31 sampai 37 |

- Login di hook `before` spec ini sebagai #1; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Starter, Growth, Professional, Enterprise, SIEM; default archived `Growth Plus (old)` dengan Clients historis 31; custom Principal aktif `Growth Tier`; custom Principal archived `Enterprise Reseller` dengan Clients 6), Dataset Plan R (default archived `Plan Arsip Lama` dengan Clients 0), Dataset Plan C (custom archived `Arsip Custom Satu` dengan Clients 0). Spec hanya membaca data ini dan tidak mengubahnya; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Total Control (Principal): TC-AC-PF-57, TC-AC-PF-58, dan TC-AC-PF-78

1. Verifikasi toolbar sub-tab Active tab Default memuat `+ Default Plan`.
2. Buka Overlay Row Action pada baris Active `Growth`.
3. Verifikasi Overlay Row Action baris Active memuat `Detail`, `Edit`, `Archive`.
4. Verifikasi modul ini tidak menyediakan kontrol untuk men-suspend entitas Principal pada toolbar dan Overlay Row Action.
5. Buka Plan Detail `Growth` (klik Plan Name).
6. Verifikasi header `Growth` menampilkan ikon Download, button `Edit`, dan button `Archive`.
7. Kembali ke list lewat Breadcrumb.
8. Klik sub-tab Archive.
9. Verifikasi toolbar tab Default Archive tanpa `+ Default Plan`.
10. Buka Overlay Row Action pada `Growth Plus (old)` (Clients > 0).
11. Verifikasi Overlay Row Action `Growth Plus (old)` hanya memuat `Detail`.
12. Buka Overlay Row Action pada `Plan Arsip Lama` (Clients 0).
13. Verifikasi Overlay Row Action `Plan Arsip Lama` memuat `Detail` dan `Delete`.
14. Buka Plan Detail `Growth Plus (old)`.
15. Verifikasi header `Growth Plus (old)` hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.
16. Kembali ke list lewat Breadcrumb.
17. Klik tab Custom.
18. Verifikasi toolbar tab Custom Active memuat `+ Custom Plan`.
19. Buka Overlay Row Action pada baris Active `Growth Tier`.
20. Verifikasi Overlay Row Action baris Active memuat `Detail`, `Edit`, `Archive`.
21. Buka Plan Detail `Growth Tier`.
22. Verifikasi header `Growth Tier` menampilkan ikon Download, button `Edit`, dan button `Archive`.
23. Kembali ke list lewat Breadcrumb.
24. Klik sub-tab Archive.
25. Buka Overlay Row Action pada `Enterprise Reseller` (Clients > 0).
26. Verifikasi Overlay Row Action `Enterprise Reseller` hanya memuat `Detail`.
27. Buka Overlay Row Action pada `Arsip Custom Satu` (Clients 0).
28. Verifikasi Overlay Row Action `Arsip Custom Satu` memuat `Detail` dan `Delete`.
29. Klik tab Global Settings.
30. Verifikasi tab Global Settings tampil dengan Card, ikon Changelog, `[Clear Field]`, dan `[Save]`.

### Blok Default User (Principal): TC-AC-PF-59

31. Ganti akun: logout, lalu login sebagai Default User (Principal) (#6).
32. Verifikasi toolbar sub-tab Active tab Default memuat `+ Default Plan`.
33. Buka Overlay Row Action pada baris Active `Growth`.
34. Verifikasi Overlay Row Action baris Active memuat `Detail`, `Edit`, `Archive`.
35. Klik tab Global Settings.
36. Verifikasi tab `Global Settings` tampil dan terbuka.
37. Verifikasi `[Save]` tampil.

## Notes

- Langkah penghubung (S-03): langkah 7, 16, 23 (kembali ke list), langkah 8, 17, 24 (pindah tab dan sub-tab), dan langkah 31 (Ganti akun eksplisit, S-07). Langkah 5, 14, 21, 29, dan 35 membuka halaman yang diasersi langkah berikutnya.
- Urutan TC: langkah TC-AC-PF-57, TC-AC-PF-58, dan TC-AC-PF-78 disisipkan berurutan per permukaan (Default Active, Default Archive, Custom Active, Custom Archive, Global Settings) agar tiap permukaan dibuka sekali. Verifikasi TC-AC-PF-78 Expected a (toolbar `+ Default Plan` dan Overlay Row Action `Detail`, `Edit`, `Archive`) identik dengan TC-AC-PF-57 Expected a, sehingga langkah 1 dan 3 memenuhi keduanya.
- Alasan melewati sekitar 35 langkah: seluruh blok berkelas Role Matrix visibilitas satu halaman dengan dataset yang sama, dan tiap blok role berdiri sendiri; kegagalan satu permukaan tidak membuat permukaan lain kehilangan makna. Elemen yang diverifikasi dihitung per klausa (S-01) dan tiap permukaan tabel (Default Active, Default Archive, Custom Active, Custom Archive) memerlukan pembukaan Overlay Row Action sendiri.
- Temuan untuk QA:
  - TC-AC-PF-78 langkah 2 ("Cari opsi mengubah status entitas Principal dari modul ini") tidak menyebut lokasi pencarian; spec memverifikasi bahwa toolbar dan Overlay Row Action tidak memuat kontrol itu (langkah 4).
  - TC-AC-PF-57 Expected b dan d menulis "plan yang dirujuk subscription non-Deleted (Clients > 0)" tanpa menyebut baris data tertentu; spec memakai `Growth Plus (old)` (Clients historis 31, Dataset Plan A) dan `Enterprise Reseller` (Clients 6) sebagai wakil.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
