---
id: TC-AC-RP-E2E-134-sinkron-pindah-entitas-antar-group-dan-wewenang-gm
title: "Sinkronisasi Settings > Group: Pemindahan Entitas Antar Group Menyesuaikan Wewenang Group Manager Tanpa Perubahan Penugasan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-353
coverage:
  web: automated
---

# Sinkronisasi Settings > Group: Pemindahan Entitas Antar Group Menyesuaikan Wewenang Group Manager Tanpa Perubahan Penugasan

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor ganti akun eksplisit (S-07): Standard `John Dohan` (GM `Region Jawa`) pada langkah 9, Group Manager `Fajar Nugroho` (`groupManagerRP_automated_{namaCompany}@qwertysystem.net`, Pre-setup #6, `Spectra.env.AC_RP_GM_PASSWORD`) pada langkah 13, Standard `Alex Tan` (GM `Sumatera`) pada langkah 16, lalu kembali ke `Siti Nurhaliza` pada langkah 19. Email dan password `John Dohan` dan `Alex Tan` tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (user Standard `Alex Tan`, `John Dohan`), #14 (penugasan GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`), #16 (`Distributor Jakarta` di `Jakarta`, `Distributor Jawa Timur` di `Surabaya`), dan #26 (menu Distributor dan Settings > Group).
- Data Dinamis (Tabel Data Uji Dinamis #4 dan #6): penugasan GM `Alex Tan` di `Sumatera` dan `John Dohan` di `Region Jawa` dibuat oleh langkah 2 dan 3 (keduanya belum menjadi GM pada awal spec); dipulihkan lewat langkah 26.
- Target pemindahan `Distributor Jawa Timur` dari `Surabaya` ke `Sumatera` adalah entitas Pre-setup (S-06); dipulihkan ke `Surabaya` lewat langkah 26.
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Kemampuan teknis: modal Changelog Tab Group Manager (Table Tools) untuk baseline jumlah entri (langkah 6); jumlah dibaca sebelum aksi karena Changelog adalah audit trail permanen (S-12).
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`, `AC_RP_GM_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-353: Entitas dipindah group menyesuaikan wewenang GM tanpa perubahan penugasan

1. Klik tab `Group Manager`
2. Assign Group Manager `Alex Tan` ke group `Sumatera`: klik `+ Assign`, pilih Group `Sumatera`, centang `Alex Tan`, lalu klik `[Assign]`
3. Assign Group Manager `John Dohan` ke group `Region Jawa`: klik `+ Assign`, pilih Group `Region Jawa`, centang `John Dohan`, lalu klik `[Assign]`
4. Tunggu aksi selesai (kedua penugasan tersimpan)
5. Buka modal Changelog Tab Group Manager lewat Table Tools
6. Catat jumlah entri Changelog sebagai baseline
7. Tutup modal Changelog
8. Pindahkan `Distributor Jawa Timur` ke group `Sumatera` di Settings > Group
9. Ganti akun: logout, lalu login sebagai `John Dohan` (GM `Region Jawa`, bukan GM `Sumatera`)
10. Buka menu Distributor
11. Verifikasi `Distributor Jakarta` tampil
12. Verifikasi `John Dohan` tidak lagi melihat `Distributor Jawa Timur`
13. Ganti akun: logout, lalu login sebagai `Fajar Nugroho` (GM `Region Jawa` dan `Sumatera`; `Spectra.env.AC_RP_GM_PASSWORD`)
14. Buka menu Distributor
15. Verifikasi `Fajar Nugroho` tetap melihat `Distributor Jawa Timur` melalui penugasan GM `Sumatera` (union akses dua group)
16. Ganti akun: logout, lalu login sebagai `Alex Tan` (GM `Sumatera`)
17. Buka menu Distributor
18. Verifikasi `Alex Tan` melihat `Distributor Jawa Timur` dengan CRUD penuh
19. Ganti akun: logout, lalu login kembali sebagai `Siti Nurhaliza` (`Spectra.env.AC_RP_TC_PASSWORD`)
20. Buka halaman `Settings > Role & Permission`, lalu klik tab `Group Manager`
21. Verifikasi penugasan GM `Alex Tan` — `Sumatera` tetap ada
22. Verifikasi penugasan GM `John Dohan` — `Region Jawa` tetap ada
23. Buka modal Changelog Tab Group Manager lewat Table Tools
24. Verifikasi jumlah entri Changelog sama dengan baseline langkah 6 (tidak ada log khusus atas pemindahan entitas)
25. Tutup modal Changelog
26. Pulihkan baseline: penugasan GM `Alex Tan` dan `John Dohan` dilepas dan `Distributor Jawa Timur` dikembalikan ke group `Surabaya`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 6 (baseline jumlah entri Changelog, S-12), langkah 26 (pemulihan baseline), dan langkah "Tunggu aksi selesai" (bagian 8b butir 8) sebelum membaca baseline.
- Pembanding absence (bagian 8b butir 2): `Distributor Jakarta` tampil pada menu Distributor sebelum asersi `Distributor Jawa Timur` tidak terlihat oleh `John Dohan`.
- P-1: asersi "tidak ada log" pada bagian akhir Expected d ditulis di spec ini sebagai `Verifikasi` berbaseline karena konteksnya bergantung pada state berat yang baru dibangun: dua penugasan GM baru lewat tiga akun dan pemindahan entitas tidak dapat dibangun ulang di spec absence tanpa mengulang seluruh alur; tidak ada spec absence (kelas g) yang memuat aksi nyata untuk TC ini (S-05). Surface: modal Changelog Tab Group Manager; baseline jumlah entri sebelum pemindahan.
- Temuan untuk QA:
  - TC-AC-RP-353 Expected d "tidak ada log atau notifikasi khusus": notifikasi in-app tidak diasersi karena pengiriman menunggu Admin Console > Notification (TC notifikasi `[DEFERRED]`); hanya log Changelog Tab Group Manager yang diasersi dan TC tidak menyebut surface log.
  - TC-AC-RP-353 Expected c "CRUD penuh" tidak menyebut penanda pengamatan pada menu Distributor; spec memakai teks Expected apa adanya.
  - Email dan password `John Dohan` dan `Alex Tan` sebagai aktor login tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - TC-AC-RP-353 tidak menyebut toast hasil Assign GM dan pemindahan entitas; spec tidak mengasersinya.
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
