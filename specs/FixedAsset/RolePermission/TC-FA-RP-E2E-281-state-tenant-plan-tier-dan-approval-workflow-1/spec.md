---
id: TC-FA-RP-E2E-281-state-tenant-plan-tier-dan-approval-workflow-1
title: "State tenant: plan tier dan Approval Workflow (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-990
  - TC-FA-RP-991
  - TC-FA-RP-992
  - TC-FA-RP-993
coverage:
  web: automated
---

# State tenant: plan tier dan Approval Workflow (1/2)

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

### TC-FA-RP-990: Plan Starter tanpa Approval Workflow, konfigurasi approval tetap dapat disimpan tanpa error

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Approver
3. Centang Pandu Wijaya
4. Klik `[Assign]`
5. Verifikasi muncul toast sukses: `Success, Approver has been assigned.`
6. Aktifkan toggle `Require Approval for Disposal`
7. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
8. Verifikasi toggle tersimpan ON
9. Verifikasi menu `Role & Permission` tampil dan tidak Disabled
10. Verifikasi tidak ada chip `Upgrade` pada menu `Role & Permission`
11. Ganti akun: logout, lalu login sebagai Total Control pada `Client Growth` dengan `Spectra.env.FA_GROWTH_TC_PASSWORD`
12. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`

### TC-FA-RP-991: Plan Growth tanpa Approval Workflow, konfigurasi approval tetap dapat disimpan tanpa error

13. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
14. Klik `[+ Assign]` pada section Approver
15. Centang Pandu Wijaya
16. Klik `[Assign]`
17. Verifikasi muncul toast sukses: `Success, Approver has been assigned.`
18. Aktifkan toggle `Require Approval for Disposal`
19. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
20. Verifikasi toggle tersimpan ON
21. Verifikasi menu `Role & Permission` tampil dan tidak Disabled
22. Verifikasi tidak ada chip `Upgrade` pada menu `Role & Permission`
23. Ganti akun: logout, lalu login sebagai Total Control pada `Client Professional` dengan `Spectra.env.FA_PROFESSIONAL_TC_PASSWORD`
24. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`

### TC-FA-RP-992: Plan Professional dengan Approval Workflow Full, konfigurasi approval tersimpan normal

25. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
26. Aktifkan toggle `Require Approval for Disposal`
27. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
28. Verifikasi toggle ON
29. Ganti akun: logout, lalu login sebagai Total Control pada `Client Enterprise` dengan `Spectra.env.FA_ENTERPRISE_TC_PASSWORD`
30. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`

### TC-FA-RP-993: Plan Enterprise dengan Approval Workflow Full, konfigurasi approval tersimpan normal

31. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
32. Aktifkan toggle `Require Approval for Disposal`
33. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
34. Verifikasi toggle ON

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-990, 991, 992, 993).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): ganti akun dan membuka halaman (tiga kali, satu per client berikutnya); membuka Tab `Transaction Role`, node, dan sub-tab; memilih Approver pada popup Assign.
- Spec ini memuat empat plan secara berurutan dengan tiga kali ganti akun; TC-FA-RP-994 (Assign Total Control pada keempat plan) ada di spec 317.
- Seeding awal tiap client: `IT Infrastructure` sub-tab `Disposal` tanpa Approver dan Require Approval Off; Ahmad Fauzi tanpa tingkat akses.
- Temuan untuk QA:
  - Akun Total Control pada `Client Starter`, `Client Growth`, `Client Professional`, dan `Client Enterprise` tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - TC-FA-RP-990 dan TC-FA-RP-991 meng-Assign Approver Pandu Wijaya pada `IT Infrastructure` sub-tab `Disposal`, sedangkan Pre-setup #19 yang menjadi Precondition sudah memuat Pandu Wijaya sebagai Approver di node dan sub-tab itu; spec membuat node tanpa Approver lewat seeding agar langkah Assign bermakna.
  - TC-FA-RP-992 dan TC-FA-RP-993 mengaktifkan toggle tanpa langkah Assign Approver; spec mengikuti TC dan memakai Approver Pandu Wijaya yang sudah ada dari Pre-setup #19 pada client itu (kondisi awal berbeda dari TC-FA-RP-990 dan 991).
