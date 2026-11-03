---
id: TC-AC-CS-E2E-131-notifikasi-in-app-approver
title: "Notifikasi In-App: Approver"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-488
  - TC-AC-CS-489
  - TC-AC-CS-492
  - TC-AC-CS-570
  - TC-AC-CS-493
coverage:
  web: automated
---

# Notifikasi In-App: Approver

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, approver pool PT Maju Bersama), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit) dan pemicu lewat sesi API:

| Pre-setup | Email | Peran | Env password |
|---|---|---|---|
| #6 | `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`) | Create-Only Distributor, requester biasa; sesi API pemicu dan akun ganti akun langkah 33 | `Spectra.env.AC_SUB_CREATE_PASSWORD` |
| #5 | `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`) | Group Manager, sesi API pemicu langkah 29 | `Spectra.env.AC_SUB_GM_PASSWORD` |
| #1 | `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`) | Total Control Principal, sesi API pemicu langkah 29 | `Spectra.env.AC_SUB_TC_PASSWORD` |

Hook `after` mengembalikan sesi UI ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed milik spec, dibuat lewat sesi API aktor `Fajar Nugroho` di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-131`), dengan jumlah notifikasi dibaca sebagai baseline sebelum pemicu:
  1. TC-AC-CS-488 dan TC-AC-CS-570: pengajuan Add Subscription SAMS Waiting for Approval `P1` untuk Client `Client Notif P1+{runId}-131`, alias Subscription ID `P1` (dibaca lewat seeding API; Data Dinamis #3; notifikasi "Subscription needs approval" Unread untuk `Eko Saputra`).
  2. TC-AC-CS-489: Client `Client Notif Edit+{runId}-131` dengan term Pending SIEM milik spec (alias Subscription ID `P-Edit`, dibaca lewat seeding API) yang diedit oleh `Fajar Nugroho` dengan toggle ON sehingga kembali Waiting for Approval (Dependensi TC-AC-CS-224).
  3. TC-AC-CS-492: Client `Client Notif Cancel+{runId}-131` dengan pengajuan Waiting for Approval FAMS milik spec (alias Subscription ID `P-Cancel`, dibaca lewat seeding API) yang di-Cancel Request oleh `Fajar Nugroho` (Dependensi TC-AC-CS-272).
  4. TC-AC-CS-493: kejadian Cancel Subscription, Cancel Request term Pending (requester, Group Manager, dan Total Control), Scheduled Flip Auto-Cancel, dan term yang langsung terotorisasi (Dependensi TC-AC-CS-262, 274, 290, 143) dipicu oleh langkah 29 setelah baseline jumlah notifikasi `Eko Saputra` dan `Fajar Nugroho` dicatat di langkah 28.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor; membaca jumlah notifikasi in-app per akun; memicu job Scheduled Flip Auto-Cancel lewat kueri fixture status job (batas tunggu 2 menit, tanpa menggeser jam di spec ini); endpoint tulis tidak tertulis di TC, PRD, atau LLD (S-13).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-488: Notifikasi pengajuan baru ke approver pool

1. Buka dropdown notifikasi approver `Eko Saputra`
2. Verifikasi notifikasi dengan Title "Subscription needs approval" dan Body "[Subscription ID P1] · SAMS · Client Notif P1+{runId}-131" tampil
3. Verifikasi notifikasi itu bersifat actionable (memuat tombol `[Detail]`)
4. Klik notifikasi
5. Verifikasi halaman Approvals > Client Subscription terbuka

### TC-AC-CS-489: Notifikasi saat Edit mengembalikan term Pending ke Waiting for Approval

6. Buka dropdown notifikasi approver `Eko Saputra`
7. Verifikasi notifikasi actionable "Subscription needs approval" dengan Body "[Subscription ID P-Edit] · SIEM · Client Notif Edit+{runId}-131" baru terkirim

### TC-AC-CS-492: Notifikasi Cancel Request oleh requester ke approver pool

8. Verifikasi notifikasi view-only "Subscription request canceled" dengan Body "[Subscription ID P-Cancel] · FAMS · Client Notif Cancel+{runId}-131" tampil pada dropdown yang sama
9. Verifikasi notifikasi itu hanya memuat tombol `[Mark as Read]`
10. Tutup dropdown notifikasi

### TC-AC-CS-570: Notifikasi actionable memuat tombol Detail tanpa Mark as Read dan tetap Unread sampai keputusan diambil

11. Buka dropdown notifikasi approver `Eko Saputra`
12. Verifikasi notifikasi "Subscription needs approval" `P1` memuat tombol `[Detail]` dan tidak memuat tombol `[Mark as Read]`
13. Catat hitungan badge notifikasi
14. Klik tombol `[Detail]` pada notifikasi `P1`
15. Verifikasi halaman Approvals > Client Subscription terbuka
16. Buka dropdown notifikasi approver `Eko Saputra`
17. Verifikasi notifikasi `P1` tetap Unread dan badge hitungan tidak berkurang dari yang dicatat
18. Klik menu `Client Subscription` di sidebar (keluar dari Approvals tanpa keputusan)
19. Buka dropdown notifikasi approver `Eko Saputra`
20. Verifikasi notifikasi `P1` tetap Unread
21. Buka Approvals > Client Subscription
22. Ketik Search `Client Notif P1+{runId}-131`, tekan Enter
23. Pilih pengajuan `P1`, pilih radio Approve, klik `[Submit Decision]`, konfirmasi dialog
24. Tunggu aksi selesai (dialog/modal tertutup)
25. Buka dropdown notifikasi approver `Eko Saputra`
26. Verifikasi notifikasi `P1` berstatus Read otomatis

### TC-AC-CS-493: Aksi tanpa notifikasi

27. Tutup dropdown notifikasi
28. Catat baseline jumlah notifikasi `Eko Saputra` dan `Fajar Nugroho` (kemampuan baca jumlah)
29. Picu lewat sesi API aktor hingga seluruh kejadian tersimpan: Cancel Subscription term seed; Cancel Request term Pending seed oleh requester `Fajar Nugroho`, oleh Group Manager `Dewi Anggraini`, dan oleh Total Control `Hendra Wijaya`; Scheduled Flip Auto-Cancel; dan Add, Renew, Convert, Activate Trial yang langsung terotorisasi
30. Buka dropdown notifikasi approver `Eko Saputra`
31. Verifikasi jumlah notifikasi sama dengan baseline sehingga tidak ada notifikasi untuk Cancel Subscription, pembatalan term Pending oleh requester, Group Manager, atau Total Control, Scheduled Flip Auto-Cancel, maupun Add, Renew, Convert, atau Activate Trial yang langsung terotorisasi
32. Logout
33. Login sebagai Create-Only `Fajar Nugroho`
34. Buka dropdown notifikasi requester `Fajar Nugroho`
35. Verifikasi jumlah notifikasi sama dengan baseline sehingga tidak ada notifikasi untuk kelima kejadian itu

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-490, 491, 571, dan 494 (notifikasi requester dan multi-role) ada di spec 132.
- Urutan TC berbeda dari sumber (488, 489, 492, 493, 570): TC-AC-CS-493 dijalankan terakhir karena memuat ganti akun dan kejadian pemicu yang tidak boleh mengubah isi dropdown TC lain; TC-AC-CS-489 dan TC-AC-CS-492 dibaca pada dropdown yang sama dengan TC-AC-CS-488 untuk mengurangi pembukaan dropdown.
- Langkah penghubung (S-03): langkah 10, 27 (menutup dropdown), langkah 18 (keluar dari Approvals tanpa keputusan), langkah 13 (mencatat badge), langkah 16 (membuka ulang dropdown karena `[Detail]` berpindah halaman), langkah 22 (Search untuk menemukan pengajuan target, R-16), langkah 24 (menunggu keputusan selesai), langkah 28 (mencatat baseline), dan langkah 32 (Logout sebagai bagian ganti akun, S-07).
- Verifikasi absence pada langkah 31 dan 35: surface agregat berupa jumlah notifikasi sebelum dan sesudah memakai baseline langkah 28 (bagian 8b butir 2); daftar kejadian yang sama-sama tidak menghasilkan notifikasi disebut utuh dalam satu `Verifikasi` (S-01).
- Aksi pemicu pelaku lain lewat sesi API bukan konteks UI kedua; `P-2` tidak dipakai. Karena semua pemicu ada di hook `before`, data seed dirujuk lewat fixture.
- Temuan untuk QA:
  - TC-AC-CS-489, 490, 492, 570 memakai record Pre-setup bersama (`SUBS-20260819-00001`, `SUBS-20260819-00006`) yang berubah statusnya oleh TC lain (diedit, dibatalkan, disetujui); spec memakai record milik spec sehingga Body notifikasi memuat Subscription ID dan nama Client seed, bukan nilai literal TC (S-06).
  - TC-AC-CS-488 Expected a menyebut Body "[Subscription ID] · SAMS · Client Tanpa Subscription"; spec memakai Client seed bersuffix.
  - TC-AC-CS-493 langkah 2 mengharuskan akun requester `Fajar Nugroho`, sedangkan akun aktor spec memakai Distributor; ganti akun ditulis di langkah 32 sampai 33.
  - TC-AC-CS-493 menyebut "Scheduled Flip Auto-Cancel" sebagai kejadian tanpa notifikasi tetapi tidak menyebut cara memicunya; spec memakai kueri fixture status job (disediakan tim FE/BE).
  - TC-AC-CS-570 Expected b menyebut "badge hitungan" tanpa menyebut elemen badge; spec mengasersi hitungan badge notifikasi pada ikon dropdown.
