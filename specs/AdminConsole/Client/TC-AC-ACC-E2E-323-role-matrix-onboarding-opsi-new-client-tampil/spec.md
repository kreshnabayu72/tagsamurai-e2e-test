---
id: TC-AC-ACC-E2E-323-role-matrix-onboarding-opsi-new-client-tampil
title: "Role Matrix: Opsi + New Client pada Field Client Form Add Subscription Tampil untuk Total Control, Active-Create + Allocation, dan Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-924
  - TC-AC-ACC-439
  - TC-AC-ACC-988
coverage:
  web: automated
---

# Role Matrix: Opsi + New Client pada Field Client Form Add Subscription Tampil untuk Total Control, Active-Create + Allocation, dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (Role Matrix positif; akun aktor pertama Total Control login di hook `before` spec ini, dua role berikutnya lewat ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`); halaman Admin Console > Client dibuka hook `beforeEach` suite):
  - Total Control (Principal) A-01: `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-AC-ACC-924).
  - Active-Create + Allocation A-AST-6 (Manage active client: Create + Read; Manage allocation: Create + Read, exact-match Area Jakarta): `activeCreateAllocationJakarta_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_ACTIVE_CREATE_ALLOC_JAKARTA_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-439).
  - Group Manager A-03 (Principal, scope Area Jakarta + seluruh descendant): `groupManagerJakarta_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_GM_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-988).
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Tidak ada data yang dibuat; form Add Subscription hanya dibuka dan field Client dibaca. Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Total Control (TC-AC-ACC-924)

1. Buka Admin Console > Client Subscription, klik `[+ Subscription]`, pilih Subscription Type `New`, dan buka field Client
2. Verifikasi opsi `+ New Client` tampil di field Client bersama daftar Client existing

### Active-Create + Allocation (TC-AC-ACC-439)

3. Ganti akun: logout, lalu login sebagai Active-Create + Allocation A-AST-6
4. Buka Admin Console > Client Subscription, klik `[+ Subscription]`, pilih Subscription Type `New`, dan buka field Client
5. Verifikasi opsi `+ New Client` tampil di field Client bersama daftar Client existing

### Group Manager (TC-AC-ACC-988)

6. Ganti akun: logout, lalu login sebagai Group Manager A-03
7. Buka Admin Console > Client Subscription, klik `[+ Subscription]`, pilih Subscription Type `New`, dan buka field Client
8. Verifikasi opsi `+ New Client` tampil di field Client bersama daftar Client existing
9. Logout, lalu login kembali sebagai Total Control (A-01)

## Notes

- Spec Role Matrix ditulis per blok role (bagian 3a): langkah tiap role identik tetapi ganti akun menuntut Step eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (S-03, S-07): ganti akun dan logout akhir mengembalikan sesi.
- Temuan untuk QA
  - TC-AC-ACC-924 dan TC-AC-ACC-988 menulis `Pilih mode New`, sedangkan TC-AC-ACC-439 menulis `Klik [+ Subscription], Pilih Subscription Type New`; spec memakai satu urutan dari TC-AC-ACC-439 untuk ketiga role.
