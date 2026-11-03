---
id: TC-AC-PF-E2E-037-capability-tunggal-distributor-create-only-update-only
title: Capability Tunggal Distributor - Create-Only, Update-Only, dan Delete-Only pada Custom Plan Milik Sendiri
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-90
  - TC-AC-PF-91
  - TC-AC-PF-92
coverage:
  web: automated
---

# Capability Tunggal Distributor - Create-Only, Update-Only, dan Delete-Only pada Custom Plan Milik Sendiri

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Create-Only (Distributor) | #12 createOnlyDistributor | `createOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_CO_PASSWORD` | langkah 1 sampai 8 |
| Update-Only (Distributor) | #13 updateOnlyDistributor | `updateOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_UO_PASSWORD` | langkah 9 sampai 17 |
| Delete-Only (Distributor) | #14 deleteOnlyDistributor | `deleteOnlyDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_DO_PASSWORD` | langkah 18 sampai 24 |

- Login di hook `before` spec ini sebagai #12; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (template `Growth` pada Product FAMS), Dataset Plan X (custom Distributor `Plan Distributor Satu` aktif dan `Plan Distributor Arsip` archived tidak pernah dipakai). `Plan Distributor Satu` diedit (Group count menjadi 3) dan `Plan Distributor Arsip` dihapus permanen; pengecualian S-06/S-12 butir A-14 berlaku. Pemulihan Dataset Plan X dijamin fixture backend (disediakan tim FE/BE, idempoten, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 17). Efek di Pre-setup: Last Updated dan entri Changelog Custom Distributor bertambah permanen dan tidak dipulihkan. Versi awal `Plan Distributor Satu` dibaca lewat fixture BE di hook `before` (baseline).
- Data Dinamis (bersuffix per run): custom plan `Paket Distributor Baru {runId}-037` (Product FAMS, Template Growth); dibuang di hook `after` lewat fixture BE (archive lalu Delete).
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk pemulihan Dataset Plan X, penghapusan plan buatan spec, dan membaca versi plan. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: versi `Plan Distributor Satu` dan keberadaan `Plan Distributor Arsip`; suite berjalan serial (`parallel: false`); dipulihkan di hook `after`.

## Test Steps

### Blok Create-Only (Distributor): TC-AC-PF-90

1. Klik tab Custom.
2. Klik `+ Custom Plan`.
3. Pilih Product `FAMS`.
4. Pilih Template `Growth`.
5. Isi Plan Name `Paket Distributor Baru {runId}-037`.
6. Klik `[Submit]`.
7. Verifikasi muncul toast sukses: "Success, custom plan has been created."
8. Verifikasi Plan Detail `Paket Distributor Baru {runId}-037 – v1` terbuka.

### Blok Update-Only (Distributor): TC-AC-PF-91

9. Ganti akun: logout, lalu login sebagai Update-Only (Distributor) (#13).
10. Klik tab Custom.
11. Buka Overlay Row Action pada `Plan Distributor Satu`.
12. Klik `Edit`.
13. Ubah Group count menjadi `3`.
14. Klik `[Save]`.
15. Verifikasi muncul toast sukses: "Success, plan has been updated."
16. Verifikasi versi `Plan Distributor Satu` bertambah satu dari versi awal.
17. Pulihkan Dataset Plan X lewat fixture BE.

### Blok Delete-Only (Distributor): TC-AC-PF-92

18. Ganti akun: logout, lalu login sebagai Delete-Only (Distributor) (#14).
19. Klik tab Custom.
20. Klik sub-tab Archive.
21. Buka Overlay Row Action pada `Plan Distributor Arsip`.
22. Klik `Delete`.
23. Klik `[Delete]` pada dialog `Delete Plan`.
24. Verifikasi muncul toast sukses: "Success, plan has been permanently deleted."

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`); langkah 9 dan 18 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 1, 10, 19, 20 (pindah tab dan sub-tab) dan langkah 17 (pemulihan Dataset Plan X lewat fixture BE, A-6).
- Temuan untuk QA:
  - Judul TC-AC-PF-92 menyebut "meng-archive lalu menghapus", tetapi langkah dan Expected hanya Delete atas plan yang sudah archived; spec mengikuti langkah TC.
  - TC-AC-PF-91 Expected b ("versi bertambah satu") tidak menyebut angka versi; spec memakai versi awal yang dibaca di hook `before`.
  - Post Condition TC-AC-PF-90, 91, dan 92 tanpa langkah observasi tidak diasersi (S-01).
