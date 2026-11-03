---
id: TC-AC-PF-E2E-025-konkurensi-capability-dicabut-dan-entitas-suspended-saat-form-dialog-terbuka
title: "Konkurensi: Capability Update Dicabut Saat Form Edit Terbuka dan Entitas Distributor Suspended Saat Dialog Archive Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-567
  - TC-AC-PF-79
coverage:
  web: automated
---

# Konkurensi: Capability Update Dicabut Saat Form Edit Terbuka dan Entitas Distributor Suspended Saat Dialog Archive Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (sesi A TC-AC-PF-567): Update-Only Principal `updateOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #4; Manage plans & licensing: Read dan Update; Group Role Manage active client CRUD), password dari `Spectra.env.AC_PF_UO_PASSWORD`. Akun pengamat sesi B TC-AC-PF-567: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (login pada langkah 9). Akun sesi A TC-AC-PF-79: Total Control Distributor `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10; entitas Distributor Active), password dari `Spectra.env.AC_PF_DIST_TC_PASSWORD` (login pada langkah 19). Pelaku sesi B yang hanya memicu perubahan state (mencabut capability, mengubah status entitas) memakai sesi API; akunnya tidak tertulis di TC dan disediakan tim FE. Kelas harness: c multi-konteks (sesi B diamati sebagai ganti akun eksplisit) untuk TC-AC-PF-567 dan TC-AC-PF-79; TC-AC-PF-79 sekaligus kelas h state tenant (status entitas Distributor Suspended).
- Login aktor pertama di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Ganti akun ditulis eksplisit pada langkah 8, 9, 18, dan 19; hook `after` mengembalikan sesi ke akun default suite.
- Data milik spec (hook `before`, dibuat lewat fixture BE, dibersihkan di hook `after`): custom plan Principal aktif `Paket Capability {runId}-025` (FAMS, Paid, v1, Group count awal `3`, tanpa subscription) dan custom plan Distributor aktif `Plan Distributor Satu {runId}-025` (milik Distributor #10, tidak dipakai subscription penahan; bentuk Dataset Plan X). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk ketiga akun; spec ini tidak mengubahnya.
- Kemampuan teknis: sesi API aktor untuk mencabut capability Update akun #4 di Settings > Role & Permission (langkah 2) dan mengubah status entitas Distributor menjadi Suspended (langkah 21), tanpa endpoint karangan (S-13, R-20); fixture BE (pemulihan capability dan status entitas, pembuatan plan) disediakan tim FE/BE (lihat `suite.md`).
- State global: capability akun #4 dan status entitas Distributor #10 diubah spec ini dan dipulihkan lewat fixture BE pada langkah 17 dan 30 serta di hook `after`; suite berjalan serial. Entri Changelog bersifat permanen.
- Env var: `Spectra.env.AC_PF_UO_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`, dan `Spectra.env.AC_PF_DIST_TC_PASSWORD`; nama `AC_PF_UO_PASSWORD` dan `AC_PF_DIST_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-567: Capability Update dicabut saat form Edit terbuka: Save ditolak dengan toast akses ditolak baku

1. Sesi A: klik tab Custom, ketik Search `Paket Capability {runId}-025`, tekan Enter, buka Overlay Row Action `Paket Capability {runId}-025`, klik `Edit`, ubah Group count `3` menjadi `25`
2. Sesi B (sesi API): cabut capability Update akun sesi A hingga perubahan tersimpan
3. Sesi A: klik `[Save]`
4. Verifikasi sesi A menampilkan toast error: "You don't have permission to do this."
5. Sesi A: klik segmen Breadcrumb `Plans & Features`
6. Verifikasi sesi A menampilkan dialog `Unsaved Changes`
7. Sesi A: klik `[Leave]`
8. Ganti akun: Logout dari akun Update-Only Principal
9. Login sebagai Total Control Principal (sesi B)
10. Sesi B: klik menu Plans & Licensing > Plans & Features di sidebar, klik tab Custom, ketik Search `Paket Capability {runId}-025`, tekan Enter
11. Verifikasi kolom Version `Paket Capability {runId}-025` tetap `v1`
12. Sesi B: klik ikon Changelog pada toolbar tab Custom
13. Verifikasi modal Changelog Custom tampil dengan sedikitnya satu entri
14. Verifikasi tidak ada entri Edit baru untuk `Paket Capability {runId}-025`
15. Tutup modal Changelog lewat `✕`
16. Sesi B: klik `(←)` pada kotak Search
17. Pulihkan capability Update akun #4 lewat fixture BE hingga tersimpan

### TC-AC-PF-79: Entitas Distributor menjadi Suspended saat halaman terbuka: Confirm Archive ditolak dengan toast baku dan plan tetap Active

18. Ganti akun: Logout dari akun Total Control Principal
19. Login sebagai Total Control Distributor (sesi A)
20. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, klik tab Custom, buka Overlay Row Action `Plan Distributor Satu {runId}-025`, klik `Archive` sehingga dialog `Archive Plan` terbuka
21. Sesi B (sesi API): ubah status entitas Distributor menjadi Suspended hingga perubahan tersimpan
22. Sesi A: klik `[Archive]`
23. Verifikasi sesi A menampilkan toast error: "Changes can't be saved while this workspace is suspended or expired."
24. Sesi A: muat ulang halaman dengan F5
25. Verifikasi `Plan Distributor Satu {runId}-025` tetap tampil di tab Custom sub-tab Active
26. Sesi A: klik ikon Changelog pada toolbar tab Custom
27. Verifikasi modal Changelog Custom tampil dengan sedikitnya satu entri
28. Verifikasi tidak ada entri Archive untuk `Plan Distributor Satu {runId}-025`
29. Tutup modal Changelog lewat `✕`
30. Pulihkan status entitas Distributor menjadi Active lewat fixture BE hingga tersimpan

## Notes

- P-1: asersi absence entri Changelog pada langkah 14 dan 28 bergantung pada state dua sesi yang baru dibangun langkah sebelumnya (form Edit dan dialog Archive terbuka sebelum capability dicabut dan entitas di-suspend); baseline berupa nama plan bersuffix (baseline nol) dengan anchor positif langkah 13 dan 27 (S-05, S-12, bagian 8b butir 2).
- Langkah penghubung (S-03): klik tab Custom, klik menu sidebar, dan Search pada langkah 1, 10, dan 20 mengarahkan layar ke tab yang disyaratkan precondition TC dan menemukan baris target (R-16); langkah 5 sampai 7 menutup form Edit yang dirty setelah Save ditolak (S-08); langkah 8 dan 9 serta 18 dan 19 adalah ganti akun eksplisit (S-07); langkah 15, 16, dan 29 menutup modal dan Search; langkah 17 dan 30 memulihkan state global (S-09, R-08); langkah 24 memuat ulang halaman sesuai langkah TC.
- Plan uji memakai nama bersuffix (S-12) sebagai ganti `Growth Tier` (Dataset Plan A) dan `Plan Distributor Satu` (Dataset Plan X) agar data milik spec (S-06); TC-AC-PF-567 mengubah plan milik spec, bukan Pre-setup.
- Kelas c dan h digabung dalam satu spec karena keduanya satu topik (perubahan state oleh sesi lain saat form atau dialog tulis terbuka, hasil Save atau Confirm ditolak server dengan toast baku) dan memakai pola sesi A UI serta sesi B API yang sama; tiap blok memakai plan dan akun sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-AC-PF-597 dan TC-AC-PF-599 ada di spec 017.
- Temuan untuk QA:
  - TC-AC-PF-567 dan TC-AC-PF-79: sesi B pada TC menunjuk aktor lain ("cabut capability ... di Settings > Role & Permission", "ubah status entitas Distributor menjadi Suspended") tanpa akun, UI, atau mekanisme; spec memakai sesi API dengan kemampuan "disediakan tim FE" tanpa endpoint karangan. Pada TC-AC-PF-79 Pre-setup #10 hanya menyebut Principal sebagai sesi B tanpa email.
  - TC-AC-PF-567: Expected b "tidak memuat entri baru" tidak menyebut jumlah awal; spec mengasersi tidak adanya entri Edit baru untuk plan bersuffix.
  - TC-AC-PF-567: Save ditolak membiarkan form dirty tanpa langkah penutup di TC; spec menutup form lewat klik segmen Breadcrumb `Plans & Features` dan `[Leave]` dengan asumsi form tetap terbuka sesudah toast error.
