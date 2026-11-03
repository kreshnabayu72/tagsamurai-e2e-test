---
id: TC-FA-RP-E2E-317-state-tenant-plan-tier-dan-approval-workflow-2
title: "State tenant: plan tier dan Approval Workflow (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-994
coverage:
  web: automated
---

# State tenant: plan tier dan Approval Workflow (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client per plan (Pre-setup #30), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA): `Spectra.env.FA_STARTER_TC_PASSWORD` (Starter), `Spectra.env.FA_GROWTH_TC_PASSWORD` (Growth), `Spectra.env.FA_PROFESSIONAL_TC_PASSWORD` (Professional), `Spectra.env.FA_ENTERPRISE_TC_PASSWORD` (Enterprise). Login akun pertama di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pergantian ke client berikutnya memakai langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #30 (`Client Starter`, `Client Growth` dengan Approval Workflow None; `Client Professional`, `Client Enterprise` dengan Approval Workflow Full; masing-masing dengan Total Control), #18, dan #19 (Pandu Wijaya sebagai kandidat Approver; Require Approval Off di semua node).
- Kemampuan teknis: seeding status awal tiap client (lihat seeding di bawah). Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): status tingkat akses, baris peran, nilai Require Approval, dan aturan persetujuan dibaca untuk Expected "tidak ada perubahan data" atau nilai akhir.
- State global: spec tidak mengubah plan atau status client; hanya nilai Require Approval dan penugasan di tiap client yang dipulihkan di hook `after`.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-994: Modul inti Role & Permission tersedia identik di seluruh plan

1. Klik `[+ Assign]` di Tab Total Control
2. Centang Ahmad Fauzi
3. Klik `[Assign]`
4. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.` pada `Client Starter`
5. Verifikasi tidak ada gating atau upsell pada `Client Starter`: tidak ada chip `Upgrade` pada menu `Role & Permission`
6. Ganti akun: logout, lalu login sebagai Total Control pada `Client Growth` dengan `Spectra.env.FA_GROWTH_TC_PASSWORD`
7. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`
8. Klik `[+ Assign]` di Tab Total Control
9. Centang Ahmad Fauzi
10. Klik `[Assign]`
11. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.` pada `Client Growth`
12. Verifikasi tidak ada gating atau upsell pada `Client Growth`: tidak ada chip `Upgrade` pada menu `Role & Permission`
13. Ganti akun: logout, lalu login sebagai Total Control pada `Client Professional` dengan `Spectra.env.FA_PROFESSIONAL_TC_PASSWORD`
14. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`
15. Klik `[+ Assign]` di Tab Total Control
16. Centang Ahmad Fauzi
17. Klik `[Assign]`
18. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.` pada `Client Professional`
19. Verifikasi tidak ada gating atau upsell pada `Client Professional`: tidak ada chip `Upgrade` pada menu `Role & Permission`
20. Ganti akun: logout, lalu login sebagai Total Control pada `Client Enterprise` dengan `Spectra.env.FA_ENTERPRISE_TC_PASSWORD`
21. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`
22. Klik `[+ Assign]` di Tab Total Control
23. Centang Ahmad Fauzi
24. Klik `[Assign]`
25. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.` pada `Client Enterprise`
26. Verifikasi tidak ada gating atau upsell pada `Client Enterprise`: tidak ada chip `Upgrade` pada menu `Role & Permission`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-994).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): ganti akun dan membuka halaman (tiga kali, satu per client berikutnya); memilih Ahmad Fauzi pada popup Assign.
- Pembagian TC lintas spec: TC-FA-RP-990 sampai TC-FA-RP-993 (konfigurasi approval per plan) ada di spec 281. Spec ini memuat satu TC yang berjalan pada keempat client, sehingga tiga kali ganti akun tidak dapat dihindari.
- Seeding awal tiap client: Ahmad Fauzi tanpa tingkat akses; Total Control Ahmad Fauzi dilepas lewat seeding di hook `after`.
- Temuan untuk QA:
  - Akun Total Control pada `Client Starter`, `Client Growth`, `Client Professional`, dan `Client Enterprise` tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - Expected TC-FA-RP-994 "tanpa gating atau upsell" tidak menyebut elemen yang diamati; spec mengamati chip `Upgrade` pada menu `Role & Permission` (selaras dengan TC-FA-RP-990).
