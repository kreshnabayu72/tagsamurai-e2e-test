---
id: TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval
title: "Modul Konsumen Allocation: Toggle ON dan OFF, Bypass GM dan Total Control, serta Additional Approver"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-357
  - TC-AC-RP-358
  - TC-AC-RP-359
  - TC-AC-RP-360
  - TC-AC-RP-361
coverage:
  web: automated
---

# Modul Konsumen Allocation: Toggle ON dan OFF, Bypass GM dan Total Control, serta Additional Approver

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Standard `John Dohan` (Group Role `Manage allocation` di `Region Jawa` dan `Sumatera` C/R; Pre-setup #15). Email dan password tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor ganti akun eksplisit (S-07): Group Manager `Fajar Nugroho` (Pre-setup #6, `Spectra.env.AC_RP_GM_PASSWORD`) pada langkah 6; Total Control `Siti Nurhaliza` (Pre-setup #1, `Spectra.env.AC_RP_TC_PASSWORD`) pada langkah 11; Standard `Dewi Anggreni` (Group Role `Manage allocation` `Region Jawa` C/R dan Additional Approver `Manage allocation` `Region Jawa`; Pre-setup #15 dan #17; email dan password disediakan tim FE) pada langkah 15. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12, #14 (GM `Fajar Nugroho` `Region Jawa` dan `Sumatera`), #15 (penugasan Group Role `Manage allocation`), #16 (entitas member group), #17 (approver `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`; toggle `Region Jawa` ON, `Sumatera` OFF tersimpan), dan #26 (Device Allocation dan Approvals).
- Data Dinamis (Tabel Data Uji Dinamis #7, TC-AC-RP-361): allocation `Waiting for Approval` milik `John Dohan` di `Region Jawa` (toggle ON) dibuat di hook `before` lewat seeding API (kemampuan disediakan tim BE/FE), identitas unik per run dengan suffix `+{runId}-107`; dipakai pada langkah 21. Allocation yang dibuat langkah spec dibersihkan di hook `after`.
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_GM_PASSWORD`, `AC_RP_TC_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-357: Toggle Manage allocation ON membuat allocation masuk Waiting for Approval

1. Buka menu Device Allocation
2. Buat allocation Hardware ke entitas di group `Region Jawa`
3. Verifikasi allocation berstatus `Waiting for Approval`

### TC-AC-RP-358: Toggle OFF membuat allocation langsung dieksekusi

4. Buat allocation Hardware ke entitas di group `Sumatera`
5. Verifikasi allocation langsung dieksekusi tanpa review

### TC-AC-RP-359: GM dan Total Control bypass approval

6. Ganti akun: logout, lalu login sebagai Group Manager `Region Jawa` `Fajar Nugroho` (`Spectra.env.AC_RP_GM_PASSWORD`)
7. Buka menu Device Allocation
8. Buat allocation ke entitas di `Jakarta` (descendant `Region Jawa`)
9. Verifikasi allocation GM langsung selesai tanpa `Waiting for Approval`
10. Verifikasi log "Auto-approved — allocator is Group Manager" pada allocation GM
11. Ganti akun: logout, lalu login sebagai Total Control `Siti Nurhaliza` (`Spectra.env.AC_RP_TC_PASSWORD`)
12. Buka menu Device Allocation
13. Buat allocation ke entitas di `Region Jawa`
14. Verifikasi allocation Total Control langsung selesai tanpa `Waiting for Approval`

### TC-AC-RP-360: Additional Approver bukan bypass dan tidak dapat menyetujui miliknya sendiri

15. Ganti akun: logout, lalu login sebagai Additional Approver `Manage allocation` `Region Jawa` dengan Group Role `Manage allocation` `Dewi Anggreni`
16. Buka menu Device Allocation
17. Buat allocation ke entitas di `Region Jawa`
18. Buka Approvals > Device Allocation
19. Verifikasi allocation masuk `Waiting for Approval`
20. Verifikasi `Dewi Anggreni` tidak dapat Approve/Reject allocation miliknya sendiri

### TC-AC-RP-361: Additional Approver dapat menyetujui allocation orang lain

21. Buka allocation milik `John Dohan` di Approvals > Device Allocation
22. Klik Approve
23. Verifikasi allocation berstatus `Approved`
24. Pulihkan baseline: data Pre-setup dan Data Dinamis yang diubah dikembalikan lewat kemampuan reset FE/BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC-AC-RP-359 (GM lalu Total Control) dan TC-AC-RP-360 dan TC-AC-RP-361 (`Dewi Anggreni`) diurutkan menurut akun supaya tiap akun diganti satu kali (S-07); urutan antar-TC lain mengikuti sumber.
- Langkah penghubung (S-03, S-09): langkah 24 (pemulihan baseline tanpa `Verifikasi`).
- Temuan untuk QA:
  - Email dan password akun Standard yang menjadi aktor (`John Dohan`, `Dewi Anggreni`) tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Data pembuatan allocation (jenis perangkat, stok, dan entitas tujuan di group yang disebut) tidak ditulis di TC; spec menulis "entitas di group X" apa adanya dan menyatakan data itu disediakan tim FE (S-11, S-13).
  - TC-AC-RP-358 mensyaratkan toggle `Sumatera` OFF; Pre-setup #17 menyebut `Sumatera` OFF tersimpan sehingga tidak perlu diatur ulang oleh spec.
  - TC-AC-RP-359 Expected "Kedua allocation langsung selesai" tidak menyebut status akhir; spec mengasersi "tanpa `Waiting for Approval`". Log "Auto-approved — allocator is Group Manager" hanya diasersi pada allocation GM sesuai Expected.
  - TC-AC-RP-360 Expected "tidak dapat Approve/Reject" tidak menyebut bentuk keadaan (aksi Hidden atau Disabled); spec mengasersi apa adanya.
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
