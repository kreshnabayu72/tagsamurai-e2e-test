---
id: TC-AC-CS-E2E-132-notifikasi-in-app-requester-dan-multi-role
title: "Notifikasi In-App: Requester dan Multi-role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-490
  - TC-AC-CS-491
  - TC-AC-CS-571
  - TC-AC-CS-494
coverage:
  web: automated
---

# Notifikasi In-App: Requester dan Multi-role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, requester), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit): Multi-role Distributor (Pre-setup #95) `multiRoleDistSub_automated_{namaCompany}@qwertysystem.net` (`Sinta Maharani`; Total Control sekaligus Additional Approver Manage allocation dan Group Manager scope group `Jawa` pada PT Maju Bersama), password `Spectra.env.AC_SUB_MULTIROLE_PASSWORD`.
- Akun pemicu lewat sesi API (bukan sesi UI): Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, approver), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- State global: toggle Require Approval for Allocation PT Maju Bersama diatur ON oleh fixture backend yang disediakan tim FE/BE di hook `before` (supaya pengajuan `Fajar Nugroho` berstatus Waiting for Approval) dan dipulihkan ke nilai awal di hook `after` (S-06, pengecualian 2026-10-30). Suite berjalan serial.
- Data seed milik spec, dibuat lewat sesi API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-132`): pengajuan `A1` (Client `Client Notif A1+{runId}-132`, FAMS) yang disetujui `Eko Saputra` (Dependensi TC-AC-CS-297; notifikasi "Subscription approved" Unread untuk `Fajar Nugroho`); pengajuan `R1` (Client `Client Notif R1+{runId}-132`, FAMS) yang ditolak `Eko Saputra` (Dependensi TC-AC-CS-302); pengajuan `M1` baru dikirim `Fajar Nugroho` dan belum diputuskan (Data Dinamis #3; Dependensi TC-AC-CS-147; tidak ada notifikasi lain untuk `Sinta Maharani` pada event itu sebelum dibaca, baseline nol karena nama bersuffix unik).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor; pengaturan toggle Require Approval; endpoint tulis tidak tertulis di TC, PRD, atau LLD (S-13).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-490: Notifikasi Approve ke requester

1. Buka dropdown notifikasi requester `Fajar Nugroho`
2. Verifikasi notifikasi view-only "Subscription approved" dengan Body "[Subscription ID A1] · FAMS · Client Notif A1+{runId}-132" tampil
3. Verifikasi notifikasi itu hanya memuat tombol `[Mark as Read]` tanpa tombol navigasi aksi

### TC-AC-CS-491: Notifikasi Reject ke requester

4. Verifikasi notifikasi view-only "Subscription rejected" dengan Body "[Subscription ID R1] · FAMS · Client Notif R1+{runId}-132" tampil pada dropdown yang sama
5. Verifikasi notifikasi itu hanya memuat tombol `[Mark as Read]`

### TC-AC-CS-571: Notifikasi view-only, klik area item tidak mengubah status dan hanya Mark as Read yang mengubah

6. Verifikasi notifikasi "Subscription approved" `A1` Unread hanya memuat tombol `[Mark as Read]`
7. Klik area judul notifikasi `A1` (bukan tombol)
8. Tutup dropdown notifikasi
9. Buka dropdown notifikasi requester `Fajar Nugroho`
10. Verifikasi notifikasi `A1` tetap Unread
11. Verifikasi tombol `[Mark as Read]` pada notifikasi `A1` tetap ada
12. Klik tombol `[Mark as Read]` pada notifikasi `A1`
13. Verifikasi notifikasi `A1` berstatus Read

### TC-AC-CS-494: Pengguna dengan beberapa role hanya menerima satu notifikasi per event

14. Logout
15. Login sebagai Multi-role `Sinta Maharani`
16. Buka dropdown notifikasi `Sinta Maharani`
17. Verifikasi tepat satu notifikasi "Subscription needs approval" untuk pengajuan `M1`
18. Verifikasi notifikasi itu memakai varian `action_tier` tertinggi (actionable, memuat tombol `[Detail]`)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-488, 489, 492, 493, dan 570 (notifikasi approver) ada di spec 131.
- Langkah penghubung (S-03): langkah 8 (menutup dropdown) dan langkah 14 (Logout sebagai bagian ganti akun, S-07).
- Aksi pemicu pelaku lain (approver, pengajuan) lewat sesi API di hook `before`; bukan konteks UI kedua, `P-2` tidak dipakai. Ganti akun ke `Sinta Maharani` eksplisit di langkah 14 sampai 15 karena akun pertama login di hook `before`.
- Temuan untuk QA:
  - TC-AC-CS-490 dan 491 memakai record Pre-setup bersama (`SUBS-20260819-00001`, `SUBS-20260819-00003`) yang statusnya berubah oleh TC lain; spec memakai record milik spec sehingga Body notifikasi memuat Subscription ID dan nama Client seed, bukan nilai literal TC (S-06).
  - TC-AC-CS-490 dan 491 tidak menyebut precondition "Pengajuan disetujui/ditolak approver" dengan akun approver; spec memakai `Eko Saputra` (Pre-setup #9) sebagai pelaku lewat sesi API.
  - TC-AC-CS-494 Expected a ("tepat satu notifikasi") dan b tidak menyebut cara mengetahui varian `action_tier` selain tombol yang tampil; spec mengasersi tombol `[Detail]`.
  - TC-AC-CS-571 langkah 2 menyebut "buka dropdown lagi" tanpa menyebut cara menutupnya; spec menutup dropdown di langkah 8.
