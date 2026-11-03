---
id: TC-AC-PF-E2E-108-push-update-kepemilikan-principal-dan-distributor
title: "Push Update: Kepemilikan Principal dan Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-273
  - TC-AC-PF-274
coverage:
  web: automated
---

# Push Update: Kepemilikan Principal dan Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Ganti akun ke Distributor ada di langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Akun kedua: Total Control Distributor `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10; entitas Distributor Active), password dari `Spectra.env.AC_PF_DIST_TC_PASSWORD` (nama env diusulkan, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features). Akun pertama (Principal) login di hook; Distributor login lewat langkah ganti akun.
- Data Pre-setup: Dataset Plan D (Pre-setup #24): default `Growth` v5 dengan client eligible `PT Wahana Nusantara` (Active v1, delta upgrade); Dataset Plan P (Pre-setup #28): custom plan `Plan Distributor Satu` dengan client eligible dalam jaringan Distributor. Dataset hanya dibaca; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan D dan Dataset Plan P) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data (seluruh blok hanya membaca). Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-273: Kepemilikan Push Update default plan: Principal saja

1. Buka tab Default sub-tab Active pada Plans List
2. Buka Plan Detail `Growth`
3. Klik Tab Assigned Clients
4. Buka Overlay Row Action `PT Wahana Nusantara`
5. Verifikasi Principal: Overlay Row Action memuat `Detail` dan `Push Update`
6. Tutup Overlay Row Action
7. Logout dari akun Principal (ganti akun)
8. Login sebagai `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` dengan password dari `Spectra.env.AC_PF_DIST_TC_PASSWORD`
9. Buka tab Default sub-tab Active pada Plans List
10. Buka Plan Detail `Growth`
11. Klik Tab Assigned Clients
12. Buka Overlay Row Action `PT Wahana Nusantara`
13. Verifikasi Distributor: Overlay Row Action hanya memuat `Detail`
14. Tutup Overlay Row Action

### TC-AC-PF-274: Kepemilikan Push Update custom plan: Distributor pemilik dapat Push Update client miliknya

15. Buka tab Custom sub-tab Active pada Plans List
16. Buka Plan Detail `Plan Distributor Satu`
17. Klik Tab Assigned Clients
18. Buka Overlay Row Action pada client Outdated eligible `Plan Distributor Satu`
19. Verifikasi Overlay Row Action memuat `Detail` dan `Push Update`
20. Tutup Overlay Row Action

## Notes

- Langkah ganti akun (S-07): `Logout` lalu login sebagai Distributor ditulis eksplisit pada TC-AC-PF-273; akun Distributor dipakai juga oleh TC-AC-PF-274.
- Alasan satu spec per blok role: langkah tiap akun berbeda, sehingga ditulis per blok role (bagian 3a).
- Temuan untuk QA: TC-AC-PF-274 Langkah 3 menyebut "client Outdated eligible" tanpa nama client; Dataset Plan P hanya menyebut `Plan Distributor Satu` dengan client eligible dalam jaringan Distributor. Nama client perlu dilengkapi.
- Temuan untuk QA: nama env password akun Distributor tidak terdaftar di TC; `AC_PF_DIST_TC_PASSWORD` adalah usulan tim FE.
