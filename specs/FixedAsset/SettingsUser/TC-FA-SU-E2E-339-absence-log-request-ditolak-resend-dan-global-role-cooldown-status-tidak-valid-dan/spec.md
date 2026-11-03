---
id: TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan
title: "Absence Log Request Ditolak: Resend dan Global Role: Cooldown, Status Tidak Valid, dan Switch OFF"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-146
  - TC-FA-SU-148
  - TC-FA-SU-171
  - TC-FA-SU-183
  - TC-FA-SU-1004
coverage:
  web: automated
---

# Absence Log Request Ditolak: Resend dan Global Role: Cooldown, Status Tidak Valid, dan Switch OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 30 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23). Target: Hana Kusuma (Pending Activation), Gita Permata (Activated, Global Role Manage accounting dengan Create dan Read tercentang), Ahmad Dahlan (Default User, Pre-setup #2), Lina Marlina (Total Control), dan Qori Akbar (akun sendiri).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Jam server dan jam browser dibekukan bersama pada langkah 1 dan hanya digeser ke nilai absolut (T0+59 pada langkah 4, T0+60 pada langkah 19, T1+59 pada langkah 21); T0 dan T1 dibaca dari waktu terbit Resend Activation Email lewat API seeding (kemampuan disediakan tim FE/BE); cooldown Resend 60 detik dipenuhi dengan mengatur jam, bukan menunggu (R-10, 8b.3). Jam dipulihkan di hook `after`. Baseline log diambil sesudah entri Resend pertama tampil dan sebelum permintaan langsung. Precondition d TC-FA-SU-146 dan 148 (cooldown belum berjalan) dipenuhi di hook `before` dengan jam yang sama.
- State global dan pemulihan: jam server dan jam browser dibekukan pada langkah 1, digeser pada langkah 4, 19, dan 21, lalu dipulihkan di hook `after`; cooldown Resend Hana Kusuma dibersihkan lewat jam di hook `after`; switch dan nilai CRUD Gita Permata dipulihkan lewat seed API. Efek pada Pre-setup: Last Updated dan Modified By Hana Kusuma dan Gita Permata berubah dan entri log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-146: Permintaan langsung Resend dalam masa cooldown

1. Bekukan jam server dan jam browser pada waktu tetap, lalu kirim Resend Activation Email untuk Hana Kusuma lewat UI (klik `⋯` pada baris Hana Kusuma lalu Resend Activation Email)
2. Baca T0 dari waktu terbit Resend Activation Email Hana Kusuma lewat API seeding
3. Muat ulang surface sampai entri `Resend Activation Email` tampil, lalu catat jumlah entri log pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log sebagai baseline (sesudah pengiriman pertama)
4. Setel jam server dan jam browser ke T0+59 detik
5. Dalam 60 detik kirim permintaan langsung ke API Resend Activation Email untuk Hana Kusuma memakai klien HTTP dengan token sesi Lina Marlina
6. Verifikasi anchor: server menolak permintaan dengan status 429
7. Verifikasi tidak ada entri log baru pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-148: Permintaan langsung Resend pada status tidak valid

8. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
9. Kirim permintaan langsung ke API Resend Activation Email untuk Gita Permata (Activated) memakai klien HTTP dengan token sesi Lina Marlina
10. Verifikasi anchor: server menolak permintaan dengan status 409
11. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-171: Checkbox C/R/U/D ditolak server saat switch Global Role OFF

12. Ketik Search `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
13. Matikan switch Manage accounting
14. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline (sesudah switch dimatikan)
15. Kirim permintaan langsung ke API ubah Update pada role Manage accounting Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
16. Verifikasi anchor: server menolak permintaan ubah Update pada role yang OFF
17. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
18. Pulihkan switch dan nilai CRUD Manage accounting Gita Permata (Create dan Read tercentang, Update dan Delete tidak) lewat seed API

### TC-FA-SU-1004: Permintaan langsung Resend: cooldown 429 dan status tidak valid 409

19. Setel jam server dan jam browser ke T0+60 detik sehingga cooldown Resend Hana Kusuma tidak berjalan
20. Kirim Resend Activation Email untuk Hana Kusuma lewat UI
21. Baca T1 dari waktu terbit Resend Activation Email terbaru Hana Kusuma lewat API seeding, lalu setel jam server dan jam browser ke T1+59 detik
22. Muat ulang surface sampai entri `Resend Activation Email` tampil, lalu catat jumlah entri log pada Tab Changelog Hana Kusuma dan Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline (sesudah pengiriman pertama)
23. Kirim permintaan langsung ke API Resend Activation Email untuk Hana Kusuma dalam masa cooldown memakai klien HTTP dengan token sesi Lina Marlina
24. Verifikasi anchor: Resend dalam masa cooldown ditolak dengan status 429
25. Kirim permintaan langsung ke API Resend Activation Email untuk Gita Permata (Activated) memakai klien HTTP dengan token sesi Lina Marlina
26. Verifikasi anchor: Resend Activation untuk pengguna Activated ditolak dengan status 409
27. Kirim permintaan langsung ke API Resend Confirmation Email untuk Gita Permata (tanpa email pending) memakai klien HTTP dengan token sesi Lina Marlina
28. Verifikasi anchor: Resend Confirmation untuk pengguna tanpa email pending ditolak dengan status 409
29. Verifikasi tidak ada entri log baru pada Tab Changelog Hana Kusuma dan Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-183: Permintaan langsung ubah Global Role Default User, diri sendiri, atau target tier

30. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
31. Catat jumlah entri log pada Tab Changelog Ahmad Dahlan, Qori Akbar, dan Lina Marlina, Tab System Log aktor, dan Activity Log sebagai baseline
32. Kirim permintaan langsung ke API ubah switch Global Role untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Qori Akbar
33. Verifikasi anchor: server menolak permintaan dengan status 403
34. Kirim permintaan langsung ke API ubah switch Global Role untuk akun sendiri (Qori Akbar) memakai klien HTTP dengan token sesi Qori Akbar
35. Verifikasi anchor: server menolak permintaan dengan status 403
36. Kirim permintaan langsung ke API ubah switch Global Role untuk Lina Marlina (Total Control) memakai klien HTTP dengan token sesi Qori Akbar
37. Verifikasi anchor: server menolak permintaan dengan status 403
38. Verifikasi tidak ada entri log baru pada Tab Changelog Ahmad Dahlan, Qori Akbar, dan Lina Marlina, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-146, 148, 171, 183, dan 1004 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 324. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Urutan TC sumber diubah (TC-FA-SU-146, 148, 171, 1004, 183) supaya ganti akun ke Qori Akbar hanya satu kali. TC-FA-SU-188 ada di spec 324 saja karena Expected-nya tidak memuat klausa log.
- Baseline TC-FA-SU-146 dan 1004 dicatat sesudah pengiriman Resend lewat UI karena pengiriman pertama itu sah menghasilkan entri log; hanya permintaan langsung yang ditolak diasersi tidak menambah entri.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 3, 8, 12, 14, 18, 19, 22, 31; langkah 2, 4, dan 21 adalah pembacaan T0/T1 dan penyetelan jam (R-10); langkah 1 membekukan jam sekaligus mengirim Resend (S-03).
- Ganti akun eksplisit (S-07): langkah 30.
- Spec ini 38 langkah (di atas smell 35 langkah). Alasan: seluruh blok satu kelas harness (absence, kelas g) dan satu topik (permintaan langsung ditolak), tiap blok berdiri sendiri; tambahan tiga langkah berasal dari pembekuan jam dan pembacaan T0/T1 (R-10).
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - TC-FA-SU-171 dan 1004 tidak menyebut pengguna target Global Role dan Resend Confirmation; spec memakai Gita Permata (sama dengan spec 324).
  - Email dan password Qori Akbar (#4) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
