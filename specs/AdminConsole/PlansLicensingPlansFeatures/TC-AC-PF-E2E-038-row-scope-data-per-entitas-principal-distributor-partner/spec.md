---
id: TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner
title: Row Scope Data per Entitas - Principal, Distributor, dan Partner
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-93
  - TC-AC-PF-94
  - TC-AC-PF-95
  - TC-AC-PF-96
  - TC-AC-PF-97
  - TC-AC-PF-98
coverage:
  web: automated
---

# Row Scope Data per Entitas - Principal, Distributor, dan Partner

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Total Control (Principal) | #1 totalControlPrincipal | `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_TC_PASSWORD` | langkah 1 sampai 7 |
| Total Control (Distributor) | #10 totalControlDistributor | `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_TC_PASSWORD` | langkah 8 sampai 25 |
| Total Control (Partner) | #17 totalControlPartner | `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `AC_PF_PARTNER_TC_PASSWORD` | langkah 26 sampai 34 |

- Login di hook `before` spec ini sebagai #1; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan X (Principal `Plan Principal Satu` aktif dan `Plan Principal Arsip` archived; Distributor `Plan Distributor Satu` aktif dan `Plan Distributor Arsip` archived tidak pernah dipakai; Partner `Plan Partner Satu` aktif), Dataset Plan A (default aktif Starter, Growth, Professional, Enterprise, SIEM; default archived `Growth Plus (old)`), Dataset Plan D (`Growth` v5 dengan 9 client; hanya 2 client berada di jaringan Distributor aktor), dan `Plan Distributor Satu` dengan 3 client (2 dalam jaringan Distributor, 1 di luar jaringan). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Total Control (Principal): TC-AC-PF-93

1. Klik tab Custom.
2. Verifikasi baris `Plan Principal Satu` tampil.
3. Verifikasi `Plan Distributor Satu` dan `Plan Partner Satu` tidak tampil di tabel.
4. Ketik Search `Distributor`, tekan Enter.
5. Verifikasi empty state "No results found".
6. Ganti isi kotak search dengan `Partner`, tekan Enter.
7. Verifikasi empty state "No results found".

### Blok Total Control (Distributor): TC-AC-PF-96, TC-AC-PF-97, TC-AC-PF-94, dan TC-AC-PF-98

8. Ganti akun: logout, lalu login sebagai Total Control (Distributor) (#10).
9. Verifikasi tab Default sub-tab Active memuat `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`.
10. Klik sub-tab Archive.
11. Verifikasi tab Default sub-tab Archive memuat `Growth Plus (old)`.
12. Buka Overlay Row Action pada `Growth Plus (old)`.
13. Verifikasi Overlay Row Action hanya memuat `Detail` (tanpa kontrol tulis).
14. Klik sub-tab Active.
15. Buka Plan Detail `Growth` (klik Plan Name).
16. Klik Tab Assigned Clients.
17. Verifikasi tab menampilkan kesembilan client pemakai plan (platform-level, tanpa isolasi jaringan).
18. Kembali ke list lewat Breadcrumb.
19. Klik tab Custom.
20. Verifikasi baris `Plan Distributor Satu` tampil.
21. Verifikasi `Plan Principal Satu` dan `Plan Partner Satu` tidak tampil di tabel.
22. Buka Plan Detail `Plan Distributor Satu`.
23. Klik Tab Assigned Clients.
24. Verifikasi tab hanya menampilkan 2 client dalam jaringan Distributor (entity-scoped).
25. Verifikasi client di luar jaringan Distributor tidak tampil.

### Blok Total Control (Partner): TC-AC-PF-96 dan TC-AC-PF-95

26. Ganti akun: logout, lalu login sebagai Total Control (Partner) (#17).
27. Verifikasi tab Default sub-tab Active memuat `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`.
28. Klik sub-tab Archive.
29. Verifikasi tab Default sub-tab Archive memuat `Growth Plus (old)`.
30. Buka Overlay Row Action pada `Growth Plus (old)`.
31. Verifikasi Overlay Row Action hanya memuat `Detail` (tanpa kontrol tulis).
32. Klik tab Custom.
33. Verifikasi baris `Plan Partner Satu` tampil.
34. Verifikasi `Plan Principal Satu` dan `Plan Distributor Satu` tidak tampil di tabel.

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`); langkah 8 dan 26 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 1, 10, 14, 19, 28, 32 (pindah tab dan sub-tab), langkah 15, 16, 22, 23 (membuka Plan Detail dan Tab Assigned Clients), langkah 18 (kembali ke list). Langkah 4 dan 6 (Search) adalah pemicu Expected TC-AC-PF-93 b dan bukan langkah penghubung.
- Urutan TC: TC-AC-PF-96 diverifikasi di awal tiap blok Distributor dan Partner karena akun yang baru login mendarat di tab Default. Pada blok Distributor, TC-AC-PF-97 (langkah 14 sampai 17) dijalankan sebelum TC-AC-PF-94 (langkah 19 sampai 21) dan TC-AC-PF-98 (langkah 22 sampai 25) agar permukaan Default lalu Custom dibuka sekali.
- Langkah 2 adalah anchor positif untuk langkah 3; langkah 20 untuk langkah 21; langkah 33 untuk langkah 34; langkah 24 untuk langkah 25.
- Temuan untuk QA:
  - TC-AC-PF-97 dan TC-AC-PF-98 menyebut jumlah client dalam jaringan Distributor (2 dari 9 pada `Growth`; 2 dari 3 pada `Plan Distributor Satu`) tetapi Dataset Plan D dan Dataset Plan P tidak merinci nama client yang berada di dalam atau di luar jaringan. Nama client "disediakan tim FE/BE".
  - TC-AC-PF-96 Expected b ("tidak ada kontrol tulis pada baris") tidak menyebut baris yang diamati; spec memverifikasi Overlay Row Action `Growth Plus (old)` (langkah 12, 13, 30, 31).
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
