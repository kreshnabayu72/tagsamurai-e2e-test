---
id: TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total
title: Role Matrix - UI Visibility Total Control Distributor dan Total Control Partner
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-65
  - TC-AC-PF-66
  - TC-AC-PF-67
  - TC-AC-PF-68
  - TC-AC-PF-69
coverage:
  web: automated
---

# Role Matrix - UI Visibility Total Control Distributor dan Total Control Partner

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Total Control (Distributor) | #10 totalControlDistributor | `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_TC_PASSWORD` | langkah 1 sampai 20 |
| Total Control (Partner) | #17 totalControlPartner | `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `AC_PF_PARTNER_TC_PASSWORD` | langkah 21 sampai 34 |

- Login di hook `before` spec ini sebagai #10; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Starter, Growth, Professional, Enterprise, SIEM), Dataset Plan R (default archived `Plan Arsip Lama`, Clients 0), Dataset Plan X (custom Distributor `Plan Distributor Satu` aktif dan `Plan Distributor Arsip` archived tidak pernah dipakai; custom Partner `Plan Partner Satu` aktif). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Total Control (Distributor): TC-AC-PF-65, TC-AC-PF-66, dan TC-AC-PF-67

1. Verifikasi toolbar sub-tab Active tab Default tanpa `+ Default Plan`.
2. Buka Overlay Row Action pada baris Active `Growth`.
3. Verifikasi Overlay Row Action baris Active hanya memuat `Detail` (tanpa `Edit`, `Archive`, `Delete`).
4. Buka Plan Detail `Growth` (klik Plan Name).
5. Verifikasi header `Growth` hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.
6. Kembali ke list lewat Breadcrumb.
7. Klik sub-tab Archive.
8. Buka Overlay Row Action pada baris Archive `Plan Arsip Lama`.
9. Verifikasi Overlay Row Action baris Archive hanya memuat `Detail` (tanpa `Edit`, `Archive`, `Delete`).
10. Verifikasi tab `Global Settings` tidak tampil.
11. Klik tab Custom.
12. Verifikasi toolbar tab Custom memuat `+ Custom Plan`.
13. Buka Overlay Row Action pada baris `Plan Distributor Satu`.
14. Verifikasi baris `Plan Distributor Satu` memuat `Detail`, `Edit`, `Archive`.
15. Buka Plan Detail `Plan Distributor Satu`.
16. Verifikasi header `Plan Distributor Satu` menampilkan ikon Download, button `Edit`, dan button `Archive`.
17. Kembali ke list lewat Breadcrumb.
18. Klik sub-tab Archive.
19. Buka Overlay Row Action pada baris `Plan Distributor Arsip`.
20. Verifikasi baris `Plan Distributor Arsip` memuat `Detail` dan `Delete`.

### Blok Total Control (Partner): TC-AC-PF-68 dan TC-AC-PF-69

21. Ganti akun: logout, lalu login sebagai Total Control (Partner) (#17).
22. Verifikasi toolbar sub-tab Active tab Default tanpa `+ Default Plan`.
23. Buka Overlay Row Action pada baris Active `Growth`.
24. Verifikasi Overlay Row Action baris Active hanya memuat `Detail`.
25. Buka Plan Detail `Growth` (klik Plan Name).
26. Verifikasi header `Growth` hanya menampilkan ikon Download.
27. Kembali ke list lewat Breadcrumb.
28. Verifikasi tab `Global Settings` tidak tampil.
29. Klik tab Custom.
30. Verifikasi toolbar tab Custom memuat `+ Custom Plan`.
31. Buka Overlay Row Action pada baris `Plan Partner Satu`.
32. Verifikasi baris `Plan Partner Satu` memuat `Detail`, `Edit`, `Archive`.
33. Buka Plan Detail `Plan Partner Satu`.
34. Verifikasi header `Plan Partner Satu` menampilkan ikon Download, `Edit`, dan `Archive`.

## Notes

- Spec ditulis per blok role karena Ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); langkah 21 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 6, 17, 27 (kembali ke list), langkah 7, 11, 18, 29 (pindah tab dan sub-tab), dan langkah 4, 15, 25, 33 (membuka Plan Detail yang diasersi langkah berikutnya).
- Urutan TC: TC-AC-PF-67 dan TC-AC-PF-69 disisipkan di antara pengamatan TC-AC-PF-65 dan TC-AC-PF-66 serta TC-AC-PF-68 per permukaan (Default, Custom) agar tiap permukaan dibuka sekali. Overlay Row Action diverifikasi pada satu baris wakil per permukaan; pada sub-tab Archive Default dipakai `Plan Arsip Lama` (Clients 0) karena baris itu menampilkan `Delete` bagi role yang berhak.
- Temuan untuk QA:
  - TC-AC-PF-65 Expected b menyebut "semua baris Active dan Archive" dan TC-AC-PF-68 Expected a "row action hanya Detail"; spec memverifikasi satu baris wakil per permukaan.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
