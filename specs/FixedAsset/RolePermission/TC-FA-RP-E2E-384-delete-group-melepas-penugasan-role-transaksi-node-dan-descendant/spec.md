---
id: TC-FA-RP-E2E-384-delete-group-melepas-penugasan-role-transaksi-node-dan-descendant
title: "Delete Group melepas penugasan Role Transaksi pada node yang dihapus dan descendant tanpa menyentuh penugasan ancestor"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1222
coverage:
  web: automated
---

# Delete Group melepas penugasan Role Transaksi pada node yang dihapus dan descendant tanpa menyentuh penugasan ancestor

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 (langkah 16) | Gunawan Halim (Asset Admin pada node yang dihapus) | #17 | tidak tertulis di Pre-setup #17; akun disediakan tim FE | `Spectra.env.FA_GUNAWAN_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Spec ini destruktif (Delete Group) dan dijalankan sesudah spec lain pada suite serial (`parallel: false`).
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (Ahmad Fauzi), #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group; `IT Infrastructure` menjadi induk rantai Group milik spec), #19 (Nadia Putri, Asset Staff, Logistics), #24 (`Company Changelog`; latar log, tidak diasersi).
- Data Dinamis (Group sementara milik spec, bersuffix `{runId}-384`; S-06 dan S-12): rantai tiga Group di bawah `IT Infrastructure`, tanpa aset aktif dan bukan tujuan Transfer atau Disposal (syarat fixture Pre-setup #18 agar guard Delete tidak menahan penghapusan):

  | Peran dalam rantai | Nama Group | Pengganti nama pada TC |
  |---|---|---|
  | Ancestor (tidak dihapus) | `Induk Hapus {runId}-384` | `IT Infrastructure` |
  | Node yang dihapus | `Node Hapus {runId}-384` | `Data Center` |
  | Descendant (ikut terhapus) | `Turunan Hapus {runId}-384` | `Rack A1` |

- Seeding precondition d TC (hook `before`, dipakai sebagai precondition, tidak diasersi; kemampuan disediakan tim FE/BE, tanpa endpoint karangan): rantai Group di atas dengan `Node Hapus {runId}-384` sebagai anak `Induk Hapus {runId}-384` dan `Turunan Hapus {runId}-384` sebagai anak `Node Hapus {runId}-384`; pada sub-tab `Disposal`: Nadia Putri Asset Admin di `Induk Hapus {runId}-384`, Gunawan Halim Asset Admin di `Node Hapus {runId}-384`, Ahmad Fauzi Approver di `Turunan Hapus {runId}-384`; Home Group Gunawan Halim (Pre-setup #17) diatur ke `Node Hapus {runId}-384` lebih dulu, sebelum penugasan Asset Admin di-seed (Home Group user = constraint Role Transaksi, V-17/V-18: node penugasan sama dengan Home Group sehingga lolos gate seeding lewat API biasa; Nadia Putri dan Ahmad Fauzi tanpa Home Group sehingga lolos di mana pun). Baris pola Total Control dan Read Only pada tiap Group terbentuk saat Group dibuat.
- Kemampuan teknis: membaca jumlah notifikasi in-app Gunawan Halim sebagai baseline (bagian 8b butir 10; disediakan tim FE/BE). Jendela absence notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" (pilihan spec, bukan nilai TC atau PRD; langkah 19).
- State yang diubah dan pemulihannya: Delete Group menghapus `Node Hapus {runId}-384` dan `Turunan Hapus {runId}-384` beserta penugasannya. Hook `after` (tidak berasumsi seeding atau penghapusan berhasil penuh) menghapus ketiga Group milik spec bila masih ada, lewat sesi API Total Control (kemampuan disediakan tim FE/BE), dan memulihkan Home Group Gunawan Halim ke `Data Center` (Pre-setup #17). Pre-setup `Data Center`, `Rack A1`, dan `IT Infrastructure` tidak diubah. Entri Changelog bersifat permanen.
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_GUNAWAN_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1222: Delete Group melepas penugasan Role Transaksi pada node yang dihapus dan descendant

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE, sesudah seeding hook `before`): jumlah notifikasi in-app Gunawan Halim
2. Buka Fixed Asset > Settings > Groups
3. Hapus group `Node Hapus {runId}-384` (beserta descendant `Turunan Hapus {runId}-384`) lewat row action Delete, lalu konfirmasi dialog `Delete Group`
4. Tunggu aksi selesai: group `Node Hapus {runId}-384` hilang dari daftar Group
5. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
6. Verifikasi node `Induk Hapus {runId}-384` tampil di Sidebar Group Tree
7. Verifikasi node `Node Hapus {runId}-384` dan `Turunan Hapus {runId}-384` tidak ada lagi di Sidebar Group Tree beserta penugasan Role Transaksi di kedua node
8. Klik node `Induk Hapus {runId}-384` lalu sub-tab `Disposal`
9. Verifikasi Nadia Putri tetap tampil di section Asset Admin
10. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
11. Telusuri seluruh halaman Pagination modal Changelog
12. Verifikasi modal memuat entri Action `Remove (Group Deleted)` untuk setiap penugasan yang dilepas pada `Node Hapus {runId}-384` dan `Turunan Hapus {runId}-384`, satu entri per penugasan
13. Verifikasi modal memuat entri Action `Remove (Group Deleted)` dengan Field `Asset Admin — Node Hapus {runId}-384`, Old Value `Gunawan Halim`, dan New Value `—`
14. Verifikasi modal memuat entri Action `Remove (Group Deleted)` dengan Field `Approver — Turunan Hapus {runId}-384`, Old Value `Ahmad Fauzi`, dan New Value `—`
15. Verifikasi tidak ada entri `Remove` untuk Nadia Putri pada Field `Asset Admin — Induk Hapus {runId}-384`
16. Tutup modal Changelog
17. Ganti akun: logout, lalu login sebagai Gunawan Halim dengan `Spectra.env.FA_GUNAWAN_PASSWORD`
18. Buka Overlay Notifikasi lewat Bell icon navbar
19. Verifikasi Overlay Notifikasi tampil
20. Tunggu 5 detik tanpa memuat ulang halaman
21. Verifikasi jumlah notifikasi Gunawan Halim sama dengan baseline langkah 1 (tidak ada notifikasi ke Gunawan Halim)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 21 langkah.
- Kelas g (asersi absence) dengan anchor positif: spec tunggal untuk TC-FA-RP-1222 karena aksi Delete Group bersifat destruktif dan tidak diulang. Anchor positif (bagian 8b butir 2): node `Induk Hapus {runId}-384` tampil (langkah 6) mendahului absence node yang dihapus (langkah 7); entri `Remove (Group Deleted)` yang tampil (langkah 12 sampai 14) mendahului absence entri `Remove` untuk Nadia Putri (langkah 15); Overlay Notifikasi tampil (langkah 19) dan jendela 5 detik (langkah 20) mendahului absence notifikasi (langkah 21; bagian 6 dan 8b butir 11). Presence klausa a sampai c (langkah 7, 9, 12 sampai 14) berada di spec yang sama karena bergantung pada state berat hasil Delete Group yang sama (`P-1`).
- Penggantian nama node TC (keputusan S-06): TC-FA-RP-1222 menghapus `Data Center` (descendant `Rack A1`) dan menempatkan Nadia Putri di `IT Infrastructure`, yaitu data Pre-setup #18 bersama. Spec membangun sendiri rantai Group sementara bersuffix `{runId}-384` dan memakainya sebagai pengganti: `IT Infrastructure` menjadi `Induk Hapus {runId}-384`, `Data Center` menjadi `Node Hapus {runId}-384`, dan `Rack A1` menjadi `Turunan Hapus {runId}-384`. Teks Expected TC ditulis dengan nama pengganti itu. Nadia Putri, Gunawan Halim, dan Ahmad Fauzi di-seed pada Group sementara (bukan pada Pre-setup #19).
- Entri Changelog dicari lewat nama Group bersuffix unik `{runId}-384` sehingga baseline entri nol (S-12); tidak ada asersi total entri. Langkah 11 menelusuri seluruh halaman Pagination modal karena penghapusan melepas banyak penugasan (baris pola dan seed) dan entri tersebar di lebih dari satu halaman (S-14).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (baseline notifikasi, S-12); langkah 2 sampai 5, 8, 10, 11, 16, 18 (navigasi, membuka dan menutup modal); langkah 4 (tunggu aksi selesai, bagian 8b butir 8); langkah 17 (ganti akun, S-07; layar yang dibutuhkan dibuka eksplisit pada langkah 18); langkah 20 (jendela absence notifikasi).
- Urutan: Delete Group pada langkah 3, lalu seluruh pengamatan sebagai Total Control, dan ganti akun ke Gunawan Halim sebagai langkah terakhir agar sesi Total Control tidak diganti di tengah pengamatan.
- Temuan untuk QA:
  - TC-FA-RP-1222 menghapus `Data Center` (Pre-setup #18 bersama); spec memakai Group sementara bersuffix sebagai pengganti (S-06). Konsekuensi: kalimat "Gunawan Halim Asset Admin di `Data Center`" dan "Ahmad Fauzi Approver di `Rack A1`" ditulis dengan nama Group sementara; seed penugasan itu dibentuk di hook `before`, bukan dari Pre-setup #19.
  - Home Group Gunawan Halim (Pre-setup #17) adalah `Data Center`. Spec mengatur Home Group Gunawan Halim ke Group sementara selama spec berjalan dan memulihkannya di hook `after`. TC tidak menyebut Home Group pada TC-FA-RP-1222; Home Group diatur sebelum seed penugasan karena Home Group user = constraint Role Transaksi (V-17/V-18): tanpa itu, seed Gunawan Halim Asset Admin di `Node Hapus {runId}-384` (di bawah `IT Infrastructure`, di luar `Data Center`) ditolak `422` bila lewat API biasa. Urutan seeding (Home Group dulu, penugasan kemudian) wajib; seeding lewat API biasa cukup, tanpa kemampuan bypass gate.
  - Email akun login Gunawan Halim tidak tertulis di Pre-setup #17; akun disediakan tim FE. Nama env `FA_GUNAWAN_PASSWORD` sudah terdaftar di `suite.md`.
  - TC-FA-RP-1222 Expected d ("tidak ada notifikasi ke Gunawan Halim") tidak memberi anchor positif pengiriman notifikasi; spec memakai Overlay Notifikasi yang terbuka dan selisih jumlah notifikasi terhadap baseline sebagai anchor (bagian 6). Notifikasi yang tidak diharapkan tidak dapat dibedakan dari notifikasi lain Gunawan Halim kecuali lewat hitungan total; spec membandingkan total.
  - TC-FA-RP-1222 Expected c menyebut entri `Remove (Group Deleted)` "per penugasan yang dilepas" tanpa merinci baris pola Total Control dan Read Only pada Group; spec mengasersi satu entri per penugasan secara umum (langkah 12) dan hanya Field yang disebut TC secara eksplisit (langkah 13 dan 14).
  - TC-FA-RP-1222 langkah 4 membuka ikon `[Changelog]` di baris sub-tab `Disposal` tanpa menyebut node; spec membukanya dari node `Induk Hapus {runId}-384` (satu-satunya node yang tersisa dari rantai).
  - Post Condition TC-FA-RP-1222 kosong ("-").
