---
id: TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off
title: "Defense-in-depth Resend dan Global Role: Cooldown, Status Tidak Valid, dan Switch OFF"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-146
  - TC-FA-SU-148
  - TC-FA-SU-171
  - TC-FA-SU-183
  - TC-FA-SU-188
  - TC-FA-SU-1004
coverage:
  web: automated
---

# Defense-in-depth Resend dan Global Role: Cooldown, Status Tidak Valid, dan Switch OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 37 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23). Target: Hana Kusuma (Pending Activation), Gita Permata (Activated, Global Role Manage accounting dengan Create dan Read tercentang), Nanda Pratama (Global Role Manage global user & role OFF, Group Role Manage user & role pada Finance & Accounting), Ahmad Dahlan (Default User, Pre-setup #2), Lina Marlina (Total Control), Qori Akbar (akun sendiri).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Mail-catcher dengan baseline jumlah email per alamat (R-11, S-12) untuk Hana Kusuma dan Gita Permata (disediakan tim FE).
- Jam server dan jam browser dibekukan bersama pada langkah 1 dan hanya digeser ke nilai absolut (T0+59 pada langkah 4, T0+60 pada langkah 26, T1+59 pada langkah 28); T0 dan T1 dibaca dari waktu terbit Resend Activation Email lewat API seeding (kemampuan disediakan tim FE/BE); cooldown Resend 60 detik dipenuhi dengan mengatur jam, bukan menunggu (R-10, 8b.3). Jam dipulihkan di hook `after`. Precondition d TC-FA-SU-146 dan 148 (cooldown belum berjalan) dipenuhi di hook `before` dengan jam yang sama.
- State global dan pemulihan: jam server dan jam browser dibekukan pada langkah 1, digeser pada langkah 4, 26, dan 28, lalu dipulihkan di hook `after`; Hana Kusuma menerima email Resend aktivasi (pengiriman UI pada TC-FA-SU-146 dan 1004) dan cooldown Resend-nya dibersihkan lewat jam di hook `after`; switch dan nilai CRUD Gita Permata serta switch Nanda Pratama dipulihkan lewat seed API. Efek pada Pre-setup: Last Updated dan Modified By Gita Permata, Nanda Pratama, dan Hana Kusuma berubah dan entri log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-146: Permintaan langsung Resend dalam masa cooldown

1. Bekukan jam server dan jam browser pada waktu tetap, lalu kirim Resend Activation Email untuk Hana Kusuma lewat UI (klik `⋯` pada baris Hana Kusuma lalu Resend Activation Email)
2. Baca T0 dari waktu terbit Resend Activation Email Hana Kusuma lewat API seeding
3. Catat jumlah email yang diterima Hana Kusuma di mail-catcher sebagai baseline
4. Setel jam server dan jam browser ke T0+59 detik
5. Dalam 60 detik kirim permintaan langsung ke API Resend Activation Email untuk Hana Kusuma memakai klien HTTP dengan token sesi Lina Marlina
6. Verifikasi server menolak permintaan dengan status 429
7. Verifikasi tidak ada email kedua terkirim ke Hana Kusuma: jumlah email sama dengan baseline

### TC-FA-SU-148: Permintaan langsung Resend pada status tidak valid

8. Catat jumlah email yang diterima Gita Permata di mail-catcher sebagai baseline
9. Kirim permintaan langsung ke API Resend Activation Email untuk Gita Permata (Activated) memakai klien HTTP dengan token sesi Lina Marlina
10. Verifikasi server menolak permintaan Resend Activation untuk Gita Permata (Activated) dengan status 409
11. Verifikasi tidak ada email terkirim ke Gita Permata: jumlah email sama dengan baseline

### TC-FA-SU-171: Checkbox C/R/U/D ditolak server saat switch Global Role OFF

12. Ketik Search `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
13. Matikan switch Manage accounting
14. Kirim permintaan langsung ke API ubah Update pada role Manage accounting Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
15. Verifikasi server menolak permintaan ubah Update pada role yang OFF
16. Verifikasi nilai CRUD tersimpan Manage accounting Gita Permata tidak berubah (dibaca lewat API)
17. Pulihkan switch dan nilai CRUD Manage accounting Gita Permata (Create dan Read tercentang, Update dan Delete tidak) lewat seed API

### TC-FA-SU-188: Penambahan grup ke Group Role Manage user & role ditolak saat Global Role Manage global user & role aktif

18. Kembali ke User List, ketik Search `Nanda`, tekan Enter, klik nama Nanda Pratama, lalu buka Tab Role > Sub-tab Global Role
19. Nyalakan switch Global Role Manage global user & role
20. Kirim permintaan langsung ke API tambah grup pada Group Role Manage user & role Nanda Pratama memakai klien HTTP dengan token sesi Lina Marlina
21. Verifikasi server menolak permintaan penambahan grup sebagai tidak eligible
22. Buka Sub-tab Group Role
23. Verifikasi baris Group Role Manage user & role tidak dirender pada Sub-tab Group Role Nanda Pratama
24. Verifikasi tidak ada penugasan grup baru pada Group Role Manage user & role Nanda Pratama (dibaca lewat API)
25. Pulihkan switch Global Role Manage global user & role Nanda Pratama ke OFF lewat seed API

### TC-FA-SU-1004: Permintaan langsung Resend: cooldown 429 dan status tidak valid 409

26. Setel jam server dan jam browser ke T0+60 detik sehingga cooldown Resend Hana Kusuma tidak berjalan
27. Kirim Resend Activation Email untuk Hana Kusuma lewat UI
28. Baca T1 dari waktu terbit Resend Activation Email terbaru Hana Kusuma lewat API seeding, lalu setel jam server dan jam browser ke T1+59 detik
29. Catat jumlah email yang diterima Hana Kusuma dan Gita Permata di mail-catcher sebagai baseline
30. Kirim permintaan langsung ke API Resend Activation Email untuk Hana Kusuma dalam masa cooldown memakai klien HTTP dengan token sesi Lina Marlina
31. Verifikasi Resend dalam masa cooldown ditolak dengan status 429
32. Kirim permintaan langsung ke API Resend Activation Email untuk Gita Permata (Activated) memakai klien HTTP dengan token sesi Lina Marlina
33. Verifikasi Resend Activation untuk pengguna Activated ditolak dengan status 409
34. Kirim permintaan langsung ke API Resend Confirmation Email untuk Gita Permata (tanpa email pending) memakai klien HTTP dengan token sesi Lina Marlina
35. Verifikasi Resend Confirmation untuk pengguna tanpa email pending ditolak dengan status 409
36. Verifikasi tidak ada email kedua terkirim ke Hana Kusuma dan tidak ada email terkirim ke Gita Permata: jumlah email sama dengan baseline

### TC-FA-SU-183: Permintaan langsung ubah Global Role Default User, diri sendiri, atau target tier

37. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
38. Kirim permintaan langsung ke API ubah switch Global Role untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Qori Akbar
39. Verifikasi server menolak permintaan dengan status 403
40. Kirim permintaan langsung ke API ubah switch Global Role untuk akun sendiri (Qori Akbar) memakai klien HTTP dengan token sesi Qori Akbar
41. Verifikasi server menolak permintaan dengan status 403
42. Kirim permintaan langsung ke API ubah switch Global Role untuk Lina Marlina (Total Control) memakai klien HTTP dengan token sesi Qori Akbar
43. Verifikasi server menolak permintaan dengan status 403
44. Verifikasi nilai Global Role Ahmad Dahlan, Qori Akbar, dan Lina Marlina tidak berubah (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-146, 148, 171, 183, 188, dan 1004 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-146, 148, 171, 183, dan 1004 diasersi di spec 339 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Urutan TC sumber diubah (TC-FA-SU-146, 148, 171, 188, 1004, 183) supaya ganti akun ke Qori Akbar hanya satu kali.
- Email yang tidak terkirim adalah state data (R-11), bukan entri log; diasersi di spec ini dengan baseline per alamat.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 2, 3, 4, 8, 12, 17, 18, 25, 26, 28, 29. Langkah 1 membekukan jam sekaligus mengirim Resend (S-03); langkah 2, 4, 26, dan 28 adalah pembacaan T0/T1 dan penyetelan jam (R-10).
- Ganti akun eksplisit (S-07): langkah 37.
- Spec ini 44 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu kelas harness (defense-in-depth, kelas a) dan satu topik (permintaan langsung Resend dan Global Role yang ditolak), tiap blok berdiri sendiri dengan target sendiri dan hanya sebagian memakai langkah pemulihan; TC-FA-SU-1004 sengaja diperlakukan utuh walau tumpang tindih dengan TC-FA-SU-146 dan 148.
- Temuan untuk QA:
  - TC-FA-SU-1004 tumpang tindih dengan TC-FA-SU-146 dan 148 (cooldown 429 dan status tidak valid 409); semuanya ditulis sebagai blok sendiri karena satu TC tepat satu spec.
  - TC-FA-SU-171 tidak menyebut pengguna target; spec memakai Gita Permata (Manage accounting, Pre-setup #23). Expected a TC-FA-SU-171 tidak menyebut kode status.
  - TC-FA-SU-1004 menyebut "Resend Confirmation untuk pengguna tanpa email pending" tanpa menyebut penggunanya; spec memakai Gita Permata.
  - TC-FA-SU-188 tidak menyebut kode status; Expected b (baris Group Role tidak dirender) diasersi lewat Sub-tab Group Role.
  - Email dan password Qori Akbar (#4) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
