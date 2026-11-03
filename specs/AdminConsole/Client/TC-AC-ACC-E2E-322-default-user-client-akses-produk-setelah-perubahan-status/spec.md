---
id: TC-AC-ACC-E2E-322-default-user-client-akses-produk-setelah-perubahan-status
title: "Default User Client di Aplikasi Produk: Mode Read-only pada Produk Baru Client Suspended dan Override Dilepas Setelah Auto-Archive lalu Auto-Reactivate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-672
  - TC-AC-ACC-994
coverage:
  web: automated
---

# Default User Client di Aplikasi Produk: Mode Read-only pada Produk Baru Client Suspended dan Override Dilepas Setelah Auto-Archive lalu Auto-Reactivate

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec. Browser A adalah sesi UI aktor ini.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Akun Default User Client yang dipakai (login Browser B, konteks UI kedua kelas c; ditutup sesudah TC): 
  - A-LIF-3 Default User Client `PT Suspend Tanpa Produk`: `clientDefaultUser_automated_ptSuspendTanpaProduk@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_LIF3_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script).
  - A-FX14-1 Default User Client `PT Suspend Arsip Reaktivasi`: `clientDefaultUser_automated_ptSuspendArsip@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_DEFAULT_USER_SUSPEND_ARSIP_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script).
- Fixture (bukan milik spec karena akun Default User terikat nama Client): C-LIF-12 `PT Suspend Tanpa Produk` (Suspended; FAMS Active; SAMS dan SIEM tidak pernah berlangganan; Default User Activated akun A-LIF-3) dan C-FX14-1 `PT Suspend Arsip Reaktivasi` (Suspended; FAMS satu-satunya term Active plan owner Principal; Default User Activated akun A-FX14-1 dengan App Access FAMS). Spec ini mengubah keduanya (SAMS ditambahkan; term FAMS di-Cancel lalu term baru ditambahkan) dan memulihkannya lewat seeding ulang Fixture BE yang dijamin tim FE/BE (idempotent) di hook `before` dan `after` (pengecualian S-06 keputusan 2026-10-30; pernyataan ini juga dicatat di `suite.md`); efeknya (Last Updated, baris Changelog Auto-Archive/Auto-Reactivate) tercatat di sini.
- Kemampuan teknis: kemampuan membaca Modal Changelog Client (Search, ukuran halaman 100) untuk baseline hitungan baris Action `Auto-Archive`, `Auto-Reactivate`, dan `Unsuspend` pada `PT Suspend Arsip Reaktivasi`; konteks UI kedua kelas c (Browser B); login Default User ke portal produk SAMS dan aplikasi FAMS (URL aplikasi produk disediakan tim FE); aksi tulis di aplikasi FAMS. Data Add Subscription TC-AC-ACC-672 (SAMS mode New terotorisasi langsung) dan term FAMS baru TC-AC-ACC-994 (mode New, terotorisasi langsung, Start Date hari ini): Plan dan Duration disediakan tim FE karena TC tidak memberi Data Uji.

## Test Steps

### Produk baru Client Suspended read-only (TC-AC-ACC-672)

1. [Browser A] Buka Admin Console > Client Subscription dan tambah subscription SAMS mode New yang terotorisasi langsung untuk `PT Suspend Tanpa Produk`
2. Tunggu aksi selesai
3. [Browser B] Buka browser kedua dan login sebagai Default User A-LIF-3, muat ulang portal, dan buka SAMS
4. Verifikasi SAMS tampil pada portal A-LIF-3 dan data dapat dilihat
5. [Browser B] Coba menambah atau mengubah data di SAMS
6. Verifikasi aksi tambah/ubah data tidak dapat dilakukan (read-only)
7. Tutup Browser B dan hapus sesi login browser terkait

### Auto-Archive lalu Auto-Reactivate Client Suspended (TC-AC-ACC-994)

8. Klik sub-tab Suspended, ketik Search `PT Suspend Arsip Reaktivasi`, tekan Enter
9. Verifikasi sel FAMS `Active`
10. Klik `[Changelog]` di toolbar List, ketik Search `PT Suspend Arsip Reaktivasi` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
11. Catat jumlah baris dengan Action `Auto-Archive` (A1), `Auto-Reactivate` (R1), dan `Unsuspend` (U1) pada hasil Search (baseline; baris dari run lain dapat sudah ada)
12. Tutup modal Changelog
13. Buka Admin Console > Client Subscription, ketik Search `PT Suspend Arsip Reaktivasi`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
14. Tunggu aksi selesai (Cancel Subscription)
15. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Suspend Arsip Reaktivasi`, tekan Enter, dan buka `⋯` baris itu
16. Verifikasi baris `PT Suspend Arsip Reaktivasi` tampil di sub-tab Archived
17. Verifikasi menu `⋯` memuat `Detail | Edit | Delete`
18. Verifikasi `Unsuspend` tidak ada pada menu
19. Klik sub-tab Suspended, ketik Search `PT Suspend Arsip Reaktivasi`, tekan Enter
20. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (status Suspended dibuang saat Auto-Archive)
21. Tambah term FAMS baru (mode New, terotorisasi langsung, Start Date hari ini) untuk `PT Suspend Arsip Reaktivasi` lewat Client Subscription
22. Tunggu aksi selesai (Add Subscription)
23. Muat ulang Admin Console > Client, klik sub-tab Active, ketik Search `PT Suspend Arsip Reaktivasi`, tekan Enter, dan buka `⋯` baris itu
24. Verifikasi baris `PT Suspend Arsip Reaktivasi` tampil di sub-tab Active
25. Verifikasi menu `⋯` memuat `Detail | Edit | Change Partner | Suspend`
26. Verifikasi `Unsuspend` tidak ada pada menu
27. Klik sub-tab Suspended, ketik Search `PT Suspend Arsip Reaktivasi`, tekan Enter
28. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
29. Klik `[Changelog]` di toolbar List, ketik Search `PT Suspend Arsip Reaktivasi` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
30. Verifikasi Modal Changelog memuat baris Action `Auto-Archive` (Field `Status`, Old Value `Suspended`, New Value `Archived`, Modified By `System`)
31. Verifikasi jumlah baris Action `Auto-Archive` (A2) sama dengan A1 + 1
32. Verifikasi Modal Changelog memuat baris Action `Auto-Reactivate` (Field `Status`, Old Value `Archived`, New Value `Active`, Modified By `System`)
33. Verifikasi jumlah baris Action `Auto-Reactivate` (R2) sama dengan R1 + 1
34. Verifikasi Modal Changelog tidak memuat baris Action `Unsuspend` baru: jumlah baris Action `Unsuspend` (U2) sama dengan U1
35. Ganti akun: login sebagai Default User A-FX14-1, buka produk FAMS, dan lakukan satu aksi tulis (simpan perubahan data)
36. Verifikasi aksi tulis berhasil tanpa penolakan read-only (override read-only App Access tidak berlaku)
37. Keluar dari sesi A-FX14-1 dan login kembali sebagai Total Control (A-01)

## Notes

- Kelas c (konteks UI kedua sebagai objek asersi pada TC-AC-ACC-672) dan sesi berurutan sebagai Default User (TC-AC-ACC-994); kedua TC memakai harness yang sama (Default User Client di aplikasi produk). Jendela Browser B ditutup dan sesi login dihapus di akhir TC-AC-ACC-672 (S-09).
- Absence `tidak ada baris Action Unsuspend baru` memakai baseline hitungan baris pada Search yang sama (langkah 10 dan 11: A1, R1, U1; langkah 12 menutup modal) dan membandingkan hitungan sesudah: A2 = A1 + 1 dan R2 = R1 + 1 sebagai anchor positif, U2 = U1 sebagai absence (bagian 8b butir 2; S-12).
- Spec melewati 35 langkah (37 langkah); alasan: dua TC satu harness (Default User Client di aplikasi produk), data fixture berbeda per TC, langkah tambahan hanya baseline dan hitungan Changelog untuk absence; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): ganti akun dan keluar sesi (langkah 35 dan 37); tutup modal Changelog (langkah 12).
- Langkah penghubung (S-03, R-16): Langkah 14, 22 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-672: Langkah 2 `Muat ulang portal dan buka SAMS` tidak menyebut URL portal Default User; disediakan tim FE.
  - TC-AC-ACC-994: Langkah 9 `buka produk FAMS dan lakukan satu aksi tulis` di aplikasi FAMS di luar Admin Console (label `Manual Only (c)`); aksi tulis konkret tidak dijelaskan, spec memakai `simpan perubahan data` apa adanya.
  - TC-AC-ACC-994: Expected butir (f) `tidak ada baris Action Unsuspend baru` memerlukan baseline; fixture Suspended tidak menyebut riwayat Changelog sebelumnya; spec mencatat baseline hitungan baris (A1, R1, U1) sebelum Cancel Subscription.
