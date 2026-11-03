---
id: TC-AC-RP-E2E-108-konsumen-allocation-remove-approver-toggle-tidak-retroaktif
title: "Modul Konsumen Allocation: Remove Approver Seketika, Toggle Tidak Retroaktif, dan Allocator Di-deactivate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-362
  - TC-AC-RP-363
  - TC-AC-RP-364
coverage:
  web: automated
---

# Modul Konsumen Allocation: Remove Approver Seketika, Toggle Tidak Retroaktif, dan Allocator Di-deactivate

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor ganti akun eksplisit (S-07): Standard `Dewi Anggreni` (Additional Approver `Manage allocation` `Region Jawa`) pada langkah 5 dan 30; Group Manager `Fajar Nugroho` (Pre-setup #6, `Spectra.env.AC_RP_GM_PASSWORD`) pada langkah 10; Standard `John Dohan` (Group Role `Manage allocation` `Region Jawa`) pada langkah 22; kembali ke `Siti Nurhaliza` pada langkah 13, 26. Email dan password `Dewi Anggreni` dan `John Dohan` tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12, #14, #15, #17 (approver `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`; toggle `Region Jawa` ON), dan #26 (Approvals, Device Allocation, Settings > User).
- Data Dinamis (Tabel Data Uji Dinamis #7): allocation A `Waiting for Approval` milik `John Dohan` di `Region Jawa` (toggle ON) dan allocation B yang sudah disetujui `Dewi Anggreni` sebelum approver dihapus (dipakai langkah 8), keduanya dibuat di hook `before` lewat seeding API (kemampuan disediakan tim BE/FE), identitas unik per run dengan suffix `+{runId}-108`; dibersihkan di hook `after`. Allocation baru yang dibuat langkah 23 (milik `John Dohan`) dibersihkan lewat kemampuan reset yang disediakan tim FE/BE pada langkah 25 dan di hook `after`.
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`, `AC_RP_GM_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-362: Remove Additional Approver mencabut hak approve seketika

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Region Jawa`, lalu Remove approver `Dewi Anggreni`: klik `⋯` baris `Dewi Anggreni`, klik `Remove`, lalu klik `[Remove]`
4. Tunggu aksi selesai (approver `Dewi Anggreni` terhapus)
5. Ganti akun: logout, lalu login sebagai `Dewi Anggreni`
6. Buka Approvals > Device Allocation lalu buka allocation A
7. Verifikasi `Dewi Anggreni` tidak lagi dapat Approve/Reject allocation A
8. Buka allocation B yang sudah disetujui sebelumnya
9. Verifikasi approval yang sudah dibuat sebelumnya pada allocation B tetap sah
10. Ganti akun: logout, lalu login sebagai Group Manager `Fajar Nugroho` (`Spectra.env.AC_RP_GM_PASSWORD`)
11. Buka Approvals > Device Allocation lalu buka allocation A
12. Verifikasi GM tetap dapat menyelesaikan allocation A (Approve/Reject tersedia)
13. Ganti akun: logout, lalu login sebagai Total Control `Siti Nurhaliza` (`Spectra.env.AC_RP_TC_PASSWORD`)
14. Buka Approvals > Device Allocation lalu buka allocation A
15. Verifikasi Total Control tetap dapat menyelesaikan allocation A (Approve/Reject tersedia)
16. Pulihkan baseline: `Dewi Anggreni` kembali menjadi approver `Manage allocation` `Region Jawa`

### TC-AC-RP-363: Perubahan toggle tidak retroaktif

17. Buka halaman `Settings > Role & Permission`, klik tab `System`, lalu pada section Group Role klik `⋯` pada baris `Manage allocation` dan klik `Detail`
18. Klik node `Region Jawa`, lalu ubah toggle ke OFF
19. Tunggu aksi selesai (toggle `Region Jawa` OFF tersimpan)
20. Buka Approvals > Device Allocation
21. Verifikasi allocation A tetap `Waiting for Approval`
22. Ganti akun: logout, lalu login sebagai `John Dohan`
23. Buat allocation baru ke entitas di `Region Jawa`
24. Verifikasi allocation baru langsung dieksekusi
25. Pulihkan baseline: allocation baru dari langkah 23 dibersihkan
26. Ganti akun: logout, lalu login kembali sebagai Total Control `Siti Nurhaliza` (`Spectra.env.AC_RP_TC_PASSWORD`)
27. Pulihkan baseline: toggle `Manage allocation` `Region Jawa` kembali ON

### TC-AC-RP-364: Allocator di-deactivate saat Waiting for Approval

28. Nonaktifkan `John Dohan` di Settings > User
29. Tunggu aksi selesai (`John Dohan` nonaktif)
30. Ganti akun: logout, lalu login sebagai approver `Dewi Anggreni`
31. Buka Approvals > Device Allocation lalu buka allocation A
32. Approve allocation A
33. Verifikasi Approve dapat dilakukan
34. Verifikasi chain approval tetap berjalan
35. Pulihkan baseline: `John Dohan` diaktifkan kembali

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 16, 25, 27, dan 35 (pemulihan baseline tanpa `Verifikasi`; langkah 25 membersihkan allocation yang dibuat langkah 23); langkah "Tunggu aksi selesai" sebelum ganti akun atau pindah surface (bagian 8b butir 8).
- Penyimpangan urutan (S-10): ganti akun terjadi lebih dari sekali karena aktor TC-AC-RP-362 sampai TC-AC-RP-364 berbeda (Total Control, approver, GM, allocator); urutan TC sumber dipertahankan.
- Temuan untuk QA:
  - Email dan password akun Standard yang menjadi aktor (`Dewi Anggreni`, `John Dohan`) tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Data pembuatan allocation (jenis perangkat, stok, dan entitas tujuan di group yang disebut) tidak ditulis di TC; spec menulis "entitas di group X" apa adanya dan menyatakan data itu disediakan tim FE (S-11, S-13).
  - TC-AC-RP-362 Expected "approval yang sudah dibuat sebelumnya tetap sah" tidak punya precondition yang menyiapkan approval itu; spec menyiapkan allocation B yang sudah disetujui `Dewi Anggreni` lewat seeding dan mengasersi approval itu tetap sah (penambahan precondition, dicatat di sini; S-03 dan S-15).
  - TC-AC-RP-362 Expected "GM/TC tetap dapat menyelesaikan" dibaca sebagai kedua peran; spec memeriksa keduanya tanpa menyelesaikan allocation A supaya allocation A tetap tersedia untuk TC-AC-RP-363 dan TC-AC-RP-364.
  - TC-AC-RP-363 Expected "allocation baru setelah OFF langsung dieksekusi" tidak menyebut pembuatnya; Total Control selalu bypass sehingga spec memakai `John Dohan` (bukan bypass) sebagai pembuat allocation baru.
  - TC-AC-RP-364 Expected "chain tetap berjalan" tidak menyebut keadaan yang diamati; spec mengasersi kalimat itu apa adanya.
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
