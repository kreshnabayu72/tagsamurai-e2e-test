---
id: TC-FA-SU-E2E-066-group-manager-save-0-grup-auto-revert-beberapa-grup-dan-auto-revert-tier-dari-popup
title: "Group Manager: Save 0 Grup, Auto-Revert Beberapa Grup, dan Auto-Revert Tier dari Popup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-215
  - TC-FA-SU-216
  - TC-FA-SU-217
coverage:
  web: automated
---

# Group Manager: Save 0 Grup, Auto-Revert Beberapa Grup, dan Auto-Revert Tier dari Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah terakhir): Group Manager Oscar Pranata (Pre-setup #9), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_GM_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Oscar Pranata, Group Manager IT Infrastructure dan Accounts Payable dengan Group Role `Manage group` penuh pada kedua grup (Pre-setup #9; "role penopang" pada TC adalah `Manage group`); Lina Marlina, Total Control (Pre-setup #1 dan #23), target TC-FA-SU-217.
- Data uji: Save dengan 0 grup (TC-FA-SU-215 dan 216) dan satu centang CRUD diubah pada popup Assign Group Role Lina Marlina (TC-FA-SU-217).
- Kemampuan teknis: seed API untuk memulihkan status Group Manager dan penugasan Oscar Pranata serta tier Total Control Lina Marlina (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target dan jumlah notifikasi in-app Oscar Pranata sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager dan penugasan Oscar Pranata, serta tier Total Control Lina Marlina (akun aktor default suite); dipulihkan ke Pre-setup #1, #9, dan #23 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-215: Save dengan 0 grup pada target Group Manager: dialog Auto-Revert D-05c sebelum penugasan dilepas

1. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role role penopang Manage group
2. Klik `[Clear Field]` lalu klik `[Save]`
3. Verifikasi dialog Title `Remove Group Manager` tampil sebelum penyimpanan
4. Klik `[Remove]`
5. Verifikasi seluruh penugasan grup role penopang Oscar terlepas (kolom Group baris Manage group menjadi `—`)
6. Verifikasi status Group Manager Oscar terlepas (banner Group Manager hilang)
7. Pulihkan status Group Manager dan penugasan Oscar Pranata ke Pre-setup #9 lewat seed API

### TC-FA-SU-216: Auto-Revert lebih dari satu grup Group Manager dalam satu edit: satu dialog D-05d dan satu toast T-06c

8. Catat jumlah entri `Auto-Revert` Oscar Pranata pada Tab Changelog serta jumlah notifikasi in-app Oscar Pranata sebagai baseline
9. Buka ulang Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role role penopang Manage group yang menopang dua grup Group Manager
10. Klik `[Clear Field]` lalu klik `[Save]`
11. Verifikasi satu dialog Title `Remove Group Manager` dengan Body bullet `• Oscar Pranata`, kalimat `This change will remove Group Manager status for these groups:` diikuti bullet IT Infrastructure dan Accounts Payable, lalu `Are you sure you want to remove it?`
12. Tunggu toast lama hilang otomatis
13. Klik `[Remove]`
14. Verifikasi satu toast "Success, permissions have been updated. Oscar Pranata is no longer Group Manager."
15. Buka Tab Changelog, Search `Oscar Pranata`, tekan Enter, lalu muat ulang sampai entri tampil
16. Verifikasi satu entri `Auto-Revert` per grup (IT Infrastructure dan Accounts Payable), dua entri bertambah dibanding baseline pada Tab Changelog
17. Pulihkan status Group Manager dan penugasan Oscar Pranata ke Pre-setup #9 lewat seed API

### TC-FA-SU-217: Auto-Revert target Total Control atau Read Only dari popup Assign Group Role: dialog tier dan banner hilang

18. Buka Detail Lina Marlina > Tab Role > Sub-tab Group Role
19. Buka popup Assign Group Role lalu ubah satu centang CRUD pada satu baris grup
20. Klik `[Save]`
21. Verifikasi dialog Title `Remove Total Control`
22. Klik `[Remove]`
23. Verifikasi tingkat akses Lina Marlina kosong dan banner tier hilang
24. Verifikasi toast "Success, permissions have been updated. Lina Marlina is no longer Total Control."
25. Pulihkan tier Total Control Lina Marlina ke Pre-setup #1 dan #23 lewat seed API
26. Logout lalu login sebagai Group Manager Oscar Pranata
27. Buka panel notifikasi
28. Verifikasi notifikasi in-app view-only tetap satu per grup (dua notifikasi baru dibanding baseline)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan, kecuali asersi notifikasi TC-FA-SU-216 butir c yang diletakkan pada langkah terakhir spec agar satu kali ganti akun cukup; baseline notifikasi dicatat sebelum TC-FA-SU-216 sehingga notifikasi TC-FA-SU-215 tidak ikut terhitung.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7, 8, 12, 17 dan 25. Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #1, #9, dan #23 (S-06, S-09).
- Langkah pola baca-log: langkah 15 dan 16. Search `Oscar Pranata` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16). Langkah terakhir spec mengganti akun ke Group Manager Oscar Pranata (ganti akun eksplisit, S-07).
- Temuan untuk QA:
  - TC-FA-SU-217 butir a menyebut "target Read Only memunculkan `Remove Read Only`", tetapi Data Uji dan langkah hanya memuat Lina Marlina (Total Control); klausa Read Only tidak punya langkah dan tidak diasersi.
  - TC-FA-SU-217 langkah 2 ("ubah centang") tidak menyebut role, grup, dan centang yang diubah agar pola Total Control menyimpang; spec memakai satu centang CRUD pada satu baris grup.
  - TC-FA-SU-217 butir b menyebut "toast T-06a mengikuti tier"; spec memakai copy template Catatan TC `Success, permissions have been updated. [User] is no longer [Tier].`.
  - TC-FA-SU-215 tidak menyebut Expected untuk log dan notifikasi (hanya Post Condition tanpa langkah observasi); Post Condition TC-FA-SU-215 dan 217 tidak diasersi.
  - TC-FA-SU-216 butir c ("notifikasi tetap satu per grup") tidak menyebut cara menghitung notifikasi; spec memakai baseline jumlah notifikasi dan panel notifikasi Oscar Pranata.
