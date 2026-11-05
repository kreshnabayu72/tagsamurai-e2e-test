---
id: TC-FA-SU-E2E-434-absence-pencabutan-silent-edit-home-group-tanpa-entri-remove-dan-tanpa-notifikasi
title: "Absence: Pencabutan Silent Group Role dan Role Transaksi akibat Edit Home Group Tanpa Entri Remove di Surface Log dan Tanpa Notifikasi Gita Permata"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1125
coverage:
  web: automated
---

# Absence: Pencabutan Silent Group Role dan Role Transaksi akibat Edit Home Group Tanpa Entri Remove di Surface Log dan Tanpa Notifikasi Gita Permata

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Hook suite dan sesi API aktor dinyatakan di `suite.md`.
- Akun kedua (ganti akun eksplisit di langkah 28): Gita Permata (Pre-setup #20, `Spectra.env.FA_GITA_PASSWORD` sesuai `suite.md`). Gita Permata hanya membuka panel notifikasi dan tidak bertindak.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Pre-setup #51 (`FaUserHGT`, varian `FaUserMain` dengan Home Group tidak dikosongkan). Target: Gita Permata (Home Group Finance & Accounting) dengan Group Role Manage group pada Finance & Accounting, Disposal × Asset Admin (Finance & Accounting), Disposal × Approver (Accounts Payable), dan Damaged × Staff (IT Infrastructure). Seed #51 belum tersedia dan disediakan tim FE/BE; dipulihkan lewat seed API di hook `before`.
- Data uji: Home Group Gita Permata berubah dari Finance & Accounting ke IT Infrastructure; dicabut akibat constraint: Manage group (Finance & Accounting), Disposal × Asset Admin (Finance & Accounting), Disposal × Approver (Accounts Payable).
- Nilai nama pengguna, grup, dan penugasan dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pembacaan jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Gita Permata, Modal Combined Changelog, Tab System Log aktor, dan Activity Log FAMS, pembacaan jumlah entri modal Changelog User > Group Role dan > Transaction Role, serta jumlah notifikasi in-app Gita Permata, semuanya sebelum aksi sebagai baseline (audit trail permanen dan notifikasi: bagian 8b butir 10). Gita Permata memiliki sedikitnya satu notifikasi in-app sebelum aksi sebagai konten pembanding panel notifikasi (seed disediakan tim FE/BE). Entri log dan notifikasi muncul eventual: surface dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Jendela absence notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 31) adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- State global dan pemulihan: Home Group Gita Permata dan seluruh penugasan Group Role dan Role Transaksinya berubah oleh langkah 5. Dipulihkan ke Pre-setup #51 lewat seed API pada langkah 33 dan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1125 (butir c, d, e): pencabutan silent akibat Edit Home Group

1. Catat baseline: jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Gita Permata, Modal Combined Changelog Gita Permata, Tab System Log aktor, dan Activity Log FAMS; jumlah entri modal Changelog User > Group Role dan > Transaction Role Gita Permata; serta jumlah notifikasi in-app Gita Permata
2. Ketik Search `Gita Permata`, tekan Enter
3. Klik ⋯ pada baris Gita Permata lalu `Edit Home Group`
4. Klik node IT Infrastructure lalu `[Select]`
5. Klik `[Revoke]` pada dialog `Role Outside Constraint Will Be Revoked`
6. Verifikasi toast "Success, home group has been updated." tampil
7. Klik Name `Gita Permata`, klik Tab Changelog, lalu muat ulang sampai entri `Edit Home Group` tampil
8. Verifikasi Tab Changelog memuat tepat satu entri `Edit Home Group` baru dibanding baseline untuk aksi ini
9. Verifikasi Tab Changelog tidak memuat entri `Remove` untuk Manage group, Disposal × Asset Admin, maupun Disposal × Approver (jumlah entri `Remove` sama dengan baseline)
10. Buka Modal Combined Changelog Gita Permata, lalu muat ulang sampai entri `Edit Home Group` tampil
11. Verifikasi Modal Combined Changelog memuat tepat satu entri `Edit Home Group` baru dibanding baseline untuk aksi ini
12. Verifikasi Modal Combined Changelog tidak memuat entri `Remove` untuk Manage group, Disposal × Asset Admin, maupun Disposal × Approver (jumlah entri `Remove` sama dengan baseline)
13. Buka Settings > User lewat sidebar, ketik Search `Lina Marlina`, tekan Enter, klik Name `Lina Marlina`, klik Tab System Log, lalu muat ulang sampai entri `Edit Home Group` tampil
14. Verifikasi Tab System Log aktor memuat tepat satu entri `Edit Home Group` baru dibanding baseline untuk aksi ini
15. Verifikasi Tab System Log aktor tidak memuat entri `Remove` untuk Manage group, Disposal × Asset Admin, maupun Disposal × Approver (jumlah entri `Remove` sama dengan baseline)
16. Buka Activity Log FAMS, lalu muat ulang sampai entri `Edit Home Group` tampil
17. Verifikasi Activity Log memuat tepat satu entri `Edit Home Group` baru dibanding baseline untuk aksi ini
18. Verifikasi Activity Log tidak memuat entri `Remove` untuk Manage group, Disposal × Asset Admin, maupun Disposal × Approver (jumlah entri `Remove` sama dengan baseline)
19. Buka Settings > User lewat sidebar, ketik Search `Gita Permata`, tekan Enter, klik Name `Gita Permata`, klik Tab Role, klik Sub-tab Group Role, lalu klik Changelog icon
20. Verifikasi modal Changelog User > Group Role tampil
21. Verifikasi modal Changelog User > Group Role tidak memuat entri baru dari aksi ini, tanpa `Remove` dan tanpa `Remove (via ...)` (jumlah entri sama dengan baseline)
22. Tutup modal Changelog User > Group Role
23. Klik Sub-tab Transaction Role lalu klik Changelog icon
24. Verifikasi modal Changelog User > Transaction Role tampil
25. Verifikasi modal Changelog User > Transaction Role tidak memuat entri baru dari aksi ini, tanpa `Remove` dan tanpa `Remove (via ...)` (jumlah entri sama dengan baseline)
26. Tutup modal Changelog User > Transaction Role
27. Logout
28. Login sebagai Gita Permata
29. Buka panel notifikasi
30. Verifikasi panel notifikasi tampil dan memuat sedikitnya satu notifikasi lain
31. Tunggu 5 detik tanpa memuat ulang halaman
32. Verifikasi Gita Permata tidak menerima notifikasi in-app untuk pencabutan Group Role dan Role Transaksi (jumlah notifikasi sama dengan baseline)
33. Pulihkan Gita Permata ke Pre-setup #51 lewat seed API

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan prinsip 13g: TC-FA-SU-1125 terbelah antara asersi fungsional dan absence. Butir a (toast dan Home Group menjadi IT Infrastructure) dan butir b (Sub-tab Group Role dan Transaction Role tidak lagi memuat penugasan di luar constraint, baris Damaged × Staff tetap) ada di spec 435. Spec ini memuat aksi nyata yang sama (Edit Home Group Gita Permata ke IT Infrastructure dengan `[Revoke]`) dengan baseline sendiri dan mengasersi butir c, d, dan e. Rujukan yang sama ada di `## Notes` spec 435.
- Butir c Expected TC memuat dua klausa per surface (satu entri `Edit Home Group` dan tidak ada entri `Remove`), masing-masing satu `Verifikasi` (S-01): langkah 8 dan 9 (Tab Changelog), 11 dan 12 (Modal Combined Changelog), 14 dan 15 (Tab System Log aktor), 17 dan 18 (Activity Log). Daftar tiga penugasan yang tidak punya entri `Remove` disebut utuh dalam satu `Verifikasi` (S-01). Butir d dipecah per modal: langkah 20 sampai 21 (Group Role) dan 24 sampai 25 (Transaction Role).
- Anchor positif (bagian 8b butir 2, 11): toast sukses langkah 6 membuktikan server menyelesaikan aksi (bagian Expected a yang dipakai sebagai anchor; asersi lengkap butir a ada di spec 435). Pada tiap surface log, entri `Edit Home Group` yang tampil sesudah muat ulang (langkah 8, 11, 14, 17) menjadi anchor untuk asersi tidak ada `Remove` (langkah 9, 12, 15, 18). Pada kedua modal Changelog User, `Verifikasi` modal tampil (langkah 20 dan 24) mendahului asersi jumlah entri. Pada notifikasi, `Verifikasi` panel tampil dan memuat notifikasi lain (langkah 30, R-21) dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 31) mendahului asersi absence (langkah 32).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (baseline, S-12), langkah 2 (Search untuk menemukan baris target, R-16, R-23), langkah 7, 10, 13, 16, 19, 23 (membuka surface), langkah 22 dan 26 (menutup modal), langkah 27 dan 28 (ganti akun eksplisit, S-07; Gita Permata hanya membuka panel notifikasi), langkah 29 (membuka panel), langkah 31 (jendela 5 detik), dan langkah 33 (pemulihan, S-09). Sesudah login Gita Permata, panel notifikasi dibuka tanpa mengandalkan halaman landing akun (S-07).
- Langkah pola baca-log: langkah 7 sampai 26 (buka surface, muat ulang sampai entri tampil, lalu `Verifikasi` kolom log atau jumlah entri). Blok ini tidak dihitung terhadap ambang sekitar 35 langkah; spec ini 33 langkah nominal.
- Panel notifikasi Gita Permata dibuka lewat ganti akun di konteks yang sama (Logout lalu login), bukan lewat konteks browser kedua, seperti spec 403; Lina Marlina tidak bertindak sesudah langkah 26 sehingga tidak ada race antar-sesi (bukan kelas c).
- Temuan untuk QA:
  - TC-FA-SU-1125 Langkah Uji 6 menyebut "Login sebagai Gita Permata di sesi lain"; spec memakai ganti akun eksplisit (langkah 27 dan 28) di konteks yang sama karena panel notifikasi Gita Permata menjadi objek asersi dan konteks UI kedua yang diasersi masuk kelas multi-konteks. Mohon dikonfirmasi.
  - Expected butir e tidak menyebut cara membuktikan panel notifikasi memuat konten lain; spec mensyaratkan Gita Permata memiliki sedikitnya satu notifikasi in-app sebelum aksi (seed disediakan tim FE/BE) sebagai anchor (R-21). Bila seed tidak menyediakannya, langkah 30 gagal.
  - Expected butir c tidak menyebut jumlah baseline entri `Remove`; spec membandingkan jumlah entri `Remove` terhadap baseline per surface (S-12) alih-alih mengasersi nol absolut, karena Gita Permata dapat sudah memiliki entri `Remove` dari run lain.
  - Expected butir c menyebut "masing-masing hanya memuat satu entri `Edit Home Group`" untuk Modal Combined Changelog tanpa menyebut cara membaca Modal Combined Changelog; spec membukanya dari Detail Gita Permata (langkah 10).
  - Expected butir d tidak menyebut surface selain dua modal Changelog User; spec tidak membaca modal Changelog Global Role.
  - Seed Pre-setup #51 (`FaUserHGT`), notifikasi in-app awal Gita Permata, dan kemampuan baca jumlah entri serta jumlah notifikasi disediakan tim FE/BE.
