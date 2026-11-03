---
id: TC-FA-SU-E2E-094-dialog-gabungan-beberapa-grup-group-manager-kunci-baris-notifikasi-dan-aktor-manage
title: "Dialog Gabungan Beberapa Grup Group Manager, Kunci Baris, dan Notifikasi Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-297
  - TC-FA-SU-298
  - TC-FA-SU-319
coverage:
  web: automated
---

# Dialog Gabungan Beberapa Grup Group Manager, Kunci Baris, dan Notifikasi Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Oscar Pranata (Pre-setup #9; Group Manager IT Infrastructure dan Accounts Payable dengan Group Role Manage group C/R/U/D pada kedua grup), akun `Spectra.env.FA_GM_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan baca notifikasi in-app per pengguna (disediakan tim FE/BE): jumlah notifikasi Auto-Revert Oscar Pranata per grup dan per judul dibaca sebelum aksi.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Oscar Pranata dipulihkan sesudah tiap aksi (langkah 11, 17) dan di hook `after`. Efek pada Pre-setup: Home Group dan status Group Manager Oscar Pranata berubah (Last Updated, Modified By), entri log permanen `Edit Home Group` dan `Auto-Revert` bertambah, dan Oscar Pranata menerima notifikasi in-app. Spec berakhir pada akun Oscar Pranata; hook `after` memulihkan sesi ke akun default suite.

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi Auto-Revert Oscar Pranata untuk IT Infrastructure dan Accounts Payable sebagai baseline

### TC-FA-SU-297: Dialog gabungan lebih dari satu grup

2. Klik ⋯ pada baris Oscar Pranata lalu klik `Edit Home Group`
3. Klik node Branch Surabaya lalu klik `[Select]`
4. Verifikasi dialog Title `Remove Group Manager` memuat `This change will remove Group Manager status for these groups:` diikuti bullet nama grup terdampak (Accounts Payable dan IT Infrastructure) dan `Are you sure you want to remove it?`
5. Klik `[Remove]`
6. Tunggu aksi selesai: permintaan `[Remove]` pada langkah 5 selesai dan dialog tertutup
7. Buka Detail Oscar Pranata > Tab Changelog
8. Verifikasi satu entri `Auto-Revert` per grup (IT Infrastructure dan Accounts Payable) tercatat
9. Baca jumlah entri `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
10. Verifikasi jumlah entri `Auto-Revert` bertambah 2 (satu per grup) dibanding baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
11. Pulihkan Home Group dan status Group Manager Oscar Pranata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-298: Kunci baris Group Manager tidak menghalangi pencabutan

12. Kembali ke User List lalu klik ⋯ pada baris Oscar Pranata dan klik `Edit Home Group`
13. Klik node Accounts Payable lalu klik `[Select]`
14. Klik `[Remove]`
15. Verifikasi pencabutan Group Role penopang Group Manager tersimpan setelah dialog gabungan dikonfirmasi
16. Verifikasi Total Control dapat mencabut Group Role penopang Group Manager walau baris itu terkunci bagi aktor Manage user & role
17. Pulihkan Home Group dan status Group Manager Oscar Pranata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-319: Notifikasi Auto-Revert akibat Edit Home Group

18. Klik ⋯ pada baris Oscar Pranata lalu klik `Edit Home Group`
19. Klik node Accounts Payable lalu klik `[Select]`
20. Klik `[Remove]`
21. Tunggu aksi selesai: permintaan `[Remove]` pada langkah 20 selesai dan dialog tertutup
22. Ganti akun: Logout lalu login sebagai Oscar Pranata
23. Buka panel notifikasi
24. Verifikasi notifikasi in-app view-only per grup yang terlepas bertambah dibanding baseline: IT Infrastructure 3 dan Accounts Payable 1 notifikasi baru (IT Infrastructure satu dari tiap TC-FA-SU-297, TC-FA-SU-298, dan TC-FA-SU-319; Accounts Payable satu dari TC-FA-SU-297 saja)
25. Verifikasi notifikasi terbaru memiliki Title `You are no longer Group Manager for IT Infrastructure`
26. Verifikasi Body `Your Group Manager status for IT Infrastructure was automatically removed after Lina Marlina set your Home Group on [Date].` dengan nama aktor Lina Marlina dan [Date] tanggal aksi
27. Verifikasi notifikasi tidak dapat ditindaklanjuti (tanpa tombol aksi)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Notifikasi Oscar Pranata diamati sekali pada akhir spec karena satu kali ganti akun cukup; selisih kumulatif terhadap baseline langkah 1: IT Infrastructure 3 (TC-FA-SU-297, TC-FA-SU-298, TC-FA-SU-319) dan Accounts Payable 1 (TC-FA-SU-297). Rincian: TC-FA-SU-297 memilih node Branch Surabaya sehingga status Group Manager terlepas di kedua grup (IT Infrastructure +1, Accounts Payable +1); TC-FA-SU-298 dan TC-FA-SU-319 memilih node Accounts Payable sebagai Home Group sehingga hanya IT Infrastructure yang terlepas (+1 masing-masing), bukan Accounts Payable. Copy Title dan Body diasersi pada notifikasi terbaru (hasil TC-FA-SU-319).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), kembali ke User List, dan langkah 11 serta 17 (pemulihan), langkah 6 (menunggu aksi `[Remove]` selesai sebelum membuka Tab Changelog), dan langkah 21 (menunggu aksi `[Remove]` selesai sebelum ganti akun, bagian 8b butir 8). Pelaku kedua tidak dipakai; pergantian akun ke Oscar Pranata hanya untuk membaca notifikasi (berurutan, bukan sesi paralel).
- Temuan untuk QA (S-15): (1) TC-FA-SU-319 berlabel `Manual Only — (d) dua sesi paralel`; spec menjalankannya berurutan (aksi lalu ganti akun) karena asersi hanya pada hasil. (2) TC-FA-SU-297 Expected b menyebut "notifikasi tetap satu per grup" tanpa langkah pengamatan; diamati bersama TC-FA-SU-319. (3) Post Condition TC-FA-SU-298 (Home Group berubah, entri `Auto-Revert` per grup, notifikasi terkirim) tanpa langkah observasi tidak diasersi kecuali yang tercakup Expected.
