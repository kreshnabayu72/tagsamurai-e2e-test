---
id: TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas
title: "Role Matrix: Akses Menu dan URL Langsung per Entitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-69
  - TC-AC-CS-71
  - TC-AC-CS-72
  - TC-AC-CS-70
  - TC-AC-CS-73
coverage:
  web: automated
---

# Role Matrix: Akses Menu dan URL Langsung per Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, Total Control, Distributor PT Maju Bersama; Pre-setup #9), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`
  - `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Lestari Wulandari`, Total Control, Partner CV Karya Mandiri; Pre-setup #11), password `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`
  - `noAccessSub_automated_{namaCompany}@qwertysystem.net` (`Toni Hartono`, role tanpa capability Manage allocation, Distributor PT Maju Bersama; Pre-setup #14), password `Spectra.env.AC_SUB_NOACCESS_PASSWORD`
  - `clientDefaultSub_automated_{namaCompany}@qwertysystem.net` (`Sari Dewi`, Default User, entitas Client PT Sejahtera; Pre-setup #15), password `Spectra.env.AC_SUB_CLIENT_DU_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Tabel "Role yang diuji": Total Control Principal (#1), Total Control Distributor (#9), Total Control Partner (#11): item `Client Subscription` Show (TC-AC-CS-69); role tanpa capability Manage allocation Distributor (#14): item Hidden dan URL langsung ditolak (TC-AC-CS-71, TC-AC-CS-72); Default User entitas Client (#15): item Hidden dan URL langsung ditolak (TC-AC-CS-70, TC-AC-CS-73).
- URL langsung yang dipakai TC-AC-CS-72 dan TC-AC-CS-73: `/admin-console/allocation/subscription`.

## Test Steps

### TC-AC-CS-69: Item sidebar Allocation > Client Subscription tampil untuk Principal, Distributor, dan Partner dengan capability

1. Buka menu `Allocation` di sidebar
2. Verifikasi menu induk `Allocation` memuat sub-menu Device Allocation, License Allocation, dan Client Subscription untuk Principal
3. Logout lalu login sbg Role: Total Control (Distributor) `Eko Saputra`
4. Buka menu `Allocation` di sidebar
5. Verifikasi item `Client Subscription` Show untuk Distributor
6. Logout lalu login sbg Role: Total Control (Partner) `Lestari Wulandari`
7. Buka menu `Allocation` di sidebar
8. Verifikasi item `Client Subscription` Show untuk Partner

### TC-AC-CS-71: Item sidebar Client Subscription Hidden untuk role tanpa capability Manage allocation

9. Logout lalu login sbg Role: tanpa akses Manage allocation (Distributor) `Toni Hartono`
10. Buka menu `Allocation` di sidebar
11. Verifikasi sedikitnya satu item sub-menu Allocation lain tampil
12. Verifikasi item `Client Subscription` tidak ada di sidebar
13. Verifikasi role lain tanpa capability Manage allocation tidak punya akses ke menu ini

### TC-AC-CS-72: Akses URL langsung oleh role tanpa capability read

14. Ketik URL `/admin-console/allocation/subscription` langsung di address bar lalu Enter
15. Verifikasi muncul toast error "You don't have permission to do this."
16. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tersembunyi
17. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
18. Verifikasi tidak ada data baris yang tampil

### TC-AC-CS-70: Item sidebar Client Subscription Hidden untuk entitas Client

19. Logout lalu login sbg Role: Default User (entitas Client) `Sari Dewi`
20. Buka menu `Allocation` di sidebar
21. Verifikasi sedikitnya satu item sub-menu Allocation lain tampil
22. Verifikasi item `Client Subscription` tidak ada di sidebar
23. Verifikasi Entity Gate menolak entitas Client (client ❌)

### TC-AC-CS-73: Akses URL langsung oleh entitas Client ditolak

24. Ketik URL `/admin-console/allocation/subscription` langsung di address bar lalu Enter
25. Verifikasi muncul toast error "You don't have permission to do this."
26. Verifikasi tidak ada baris Subscription yang tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok akun karena langkah tiap role berbeda dan ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). Urutan TC: 69, 71, 72, 70, 73 supaya ganti akun satu kali per akun (S-10).
- Verifikasi `sedikitnya satu item sub-menu Allocation lain tampil` adalah anchor positif untuk asersi absence item sidebar (bagian 8b butir 2); TC tidak menulisnya.
- Temuan untuk QA:
  - TC-AC-CS-70 Expected b ("Entity Gate menolak entitas Client (client ❌)") tidak dapat diamati terpisah dari Expected a; spec menuliskannya sebagai Verifikasi sendiri atas hasil yang sama (item tidak tampil) dan Entity Gate tidak punya cara pengamatan lain di UI.
  - TC-AC-CS-71 Expected b ("Role lain tidak punya akses ke menu ini") tidak menyebut role atau cara mengamati; spec menuliskannya sebagai Verifikasi atas akun `Toni Hartono` saja (S-15).
  - TC-AC-CS-72 dan TC-AC-CS-73 mengasersi tampilan (toast dan UI) pada akses URL langsung lewat browser; request langsung tanpa browser ada di spec defense-in-depth (slice lain).
