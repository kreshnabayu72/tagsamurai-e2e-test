---
id: TC-FA-RP-E2E-352-subgroup-baru-di-bawah-node-gm-menulis-baris-pola-dan-group-level-one-tidak
title: "Subgroup baru di bawah node Group Manager menulis baris pola GM dengan log Assign biasa, sedangkan Group level-one tidak"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1183
coverage:
  web: automated
---

# Subgroup baru di bawah node Group Manager menulis baris pola GM dengan log Assign biasa, sedangkan Group level-one tidak

## Prerequisites

- Mode: FE+BE.
- Akun (login akun urutan 1 di hook `before`; akun urutan 2 lewat langkah ganti akun eksplisit):

  | Urutan | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|---|
  | 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | 2 | Group Manager target, Kevin Susanto | #13 | akun login Kevin Susanto; email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE | password disediakan tim FE (nama env belum ada di `suite.md`) |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE; hanya dibaca): #5 (Fajar Nugroho, Group Manager di `IT Infrastructure`), #13 (Kevin Susanto, Group Manager di `Data Center`), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`), #21 (seed pemegang Update `Manage asset & TAG`; tidak diasersi), #43 (seed Group Manager: Fajar Nugroho, Kevin Susanto, dan Lina Marlina di `Head Office`).
- Data Dinamis (Tabel Data Uji Dinamis TC #11, #12; nama bersuffix `{runId}` dan nomor spec 352): Subgroup `GM Sub {runId}-352` di bawah `Data Center` dan Group level-one `GM Root {runId}-352`. Pembuatan kedua Group (langkah 3 dan 4) adalah aksi TC yang hasilnya diasersi lewat baris pola, bukan seeding.
- Pengecualian S-11 atas pembersihan: kedua Group dinamis tetap ada sampai akhir sesi pengujian sesuai kolom Lifecycle Tabel Data Uji Dinamis TC (#11 dan #12) dan tidak dihapus di hook `after`. Alasan TC: Group menjadi bagian pohon uji sampai akhir sesi. Nama bersuffix unik per run sehingga tidak bentrok antar run; baris pola pada kedua Group dicakup TC ini dan TC-FA-RP-1157 untuk baris pola Total Control dan Read Only.
- Kemampuan teknis: membaca jumlah notifikasi in-app Kevin Susanto sebagai baseline (disediakan tim FE/BE, tanpa endpoint karangan). Jendela asersi notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD). Nama Group bersuffix unik sehingga baseline entri Changelog nol (S-12).
- Tabel yang diulang:

  | Role katalog dengan baris pola GM (langkah 7 sampai 9) |
  |---|
  | `Manage files` |
  | `Manage asset & TAG` |
  | `Manage group` |
  | `Manage purchase` |

  | Sub-tab (langkah 16 sampai 18) |
  |---|
  | `Disposal` |
  | `Transfer` |

- State yang diubah dan pemulihannya: spec hanya menambah Group dinamis dan baris pola-nya (lihat pengecualian S-11 di atas); penugasan Pre-setup tidak diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1183: Subgroup baru di bawah node GM menulis baris pola GM, Group level-one tidak

1. Catat jumlah notifikasi in-app Kevin Susanto sebagai baseline lewat kemampuan baca
2. Buka Fixed Asset > Settings > Groups
3. Buat Subgroup `GM Sub {runId}-352` di bawah `Data Center` lewat row action `Add Subgroup`
4. Buat Group level-one `GM Root {runId}-352`
5. Tunggu aksi selesai: kedua Group tampil di pohon Group
6. Buka Fixed Asset > Settings > Role & Permission
7. Untuk setiap baris tabel "Role katalog dengan baris pola GM" (langkah 7 sampai 9 diulang untuk role itu): buka Tab `System` lalu Detail Role pada role itu
8. Klik node `GM Sub {runId}-352` pada Sidebar Group Tree
9. Verifikasi Kevin Susanto dan Fajar Nugroho tampil dengan CRUD penuh sesuai kolom berlaku pada node itu (mis. `Manage files` Read dan Delete)
10. Buka Tab `System` lalu Detail Role `Manage user & role`
11. Klik node `GM Sub {runId}-352`
12. Verifikasi sedikitnya satu baris lain tampil pada node itu
13. Verifikasi tidak ada baris Kevin Susanto maupun Fajar Nugroho pada `Manage user & role`
14. Klik Tab `Transaction Role`
15. Klik node `GM Sub {runId}-352`
16. Untuk setiap baris tabel "Sub-tab" (langkah 16 sampai 18 diulang untuk sub-tab itu): klik sub-tab pada node itu
17. Verifikasi Kevin Susanto dan Fajar Nugroho tampil di section Asset Admin dan Approver
18. Verifikasi Kevin Susanto dan Fajar Nugroho tidak tampil di section Monitoring & Report maupun Staff
19. Buka Tab `System` lalu Detail Role `Manage files`
20. Klik node `GM Root {runId}-352`
21. Verifikasi sedikitnya satu baris tampil pada node itu
22. Verifikasi tidak ada baris Kevin Susanto maupun Fajar Nugroho pada node `GM Root {runId}-352`
23. Klik ikon Changelog di toolbar Detail Role
24. Verifikasi entri Action `Assign` biasa (bukan `Assign (via Group Manager)`) per baris pola GM pada node `GM Sub {runId}-352`
25. Verifikasi entri tersebut memuat Old Value `—`, New Value `Assigned`, dan Modified By `Siti R`
26. Tutup modal Changelog
27. Ganti akun: logout dari akun Total Control
28. Login sebagai Kevin Susanto
29. Buka Overlay Notifikasi
30. Verifikasi panel notifikasi tampil
31. Tunggu 5 detik tanpa memuat ulang halaman
32. Verifikasi jumlah notifikasi Kevin Susanto sama dengan baseline langkah 1 (tidak ada notifikasi untuk pembuatan baris pola)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah nominal (44 langkah setelah ekspansi dua perulangan).
- Langkah 7 sampai 9 diulang untuk empat role dan langkah 16 sampai 18 untuk dua sub-tab sesuai tabel di `## Prerequisites` (idiom bagian 8b butir 7).
- Alasan melewati sekitar 35 langkah (44 langkah setelah ekspansi): TC-FA-RP-1183 mengamati empat role katalog dengan baris pola, satu role tanpa baris, dua sub-tab, node level-one, Changelog, dan notifikasi dari satu pembuatan Group yang tidak dapat dipisah tanpa mengulang pembuatan; sebagian besar langkah tambahan berasal dari perulangan tabel, bukan dari langkah unik.
- Langkah penghubung (S-03): langkah 2 sampai 6, 10, 11, 14 sampai 16, 19, 20, 23, 29 (navigasi dan pembuatan Group yang bukan Expected), langkah 5 (tunggu aksi selesai, 8b butir 8), langkah 26 (menutup modal Changelog), langkah 1 (baseline, S-12), langkah 27 dan 28 (ganti akun eksplisit, S-07), langkah 31 (jendela notifikasi, bagian 6). Langkah 12, 21, dan 30 adalah anchor positif atas asersi absence sesudahnya (8b butir 2); langkah 17 menjadi anchor atas langkah 18.
- Tanpa Search pada tabel Detail Role dan tabel Role Transaksi: Group baru memuat paling banyak delapan baris (lima baris pola Total Control dan Read Only ditambah tiga baris pola GM Pre-setup #43) dalam satu halaman, sehingga TC "cari" dipenuhi dengan membaca baris pada node itu.
- Teks Action `Assign` biasa (bukan `Assign (via Group Manager)`) mengikuti TC dan menunggu keputusan PM (Open Item #7c).
- Temuan untuk QA:
  - TC-FA-RP-1183 Expected a menyebut Kevin Susanto dan Fajar Nugroho tampil di "kelima role katalog" tetapi tidak ada baris pada `Manage user & role`; spec menafsirkan "kelima" sebagai empat role dengan baris pola (`Manage files`, `Manage asset & TAG`, `Manage group`, `Manage purchase`) ditambah `Manage user & role` tanpa baris (langkah 10 sampai 13).
  - TC-FA-RP-1183 Expected a menyebut "CRUD penuh sesuai kolom berlaku" tanpa merinci kolom tiap role; spec mengasersi CRUD penuh sesuai kolom berlaku dan hanya `Manage files` memberi contoh (Read dan Delete).
  - Ketidakcocokan seed Kevin Susanto belum direkonsiliasi: Pre-setup #13 dan #43 menaruh Kevin Susanto hanya di `Data Center`, sedangkan Pre-setup #38 (dan TC lain) menambah `Helpdesk`. Spec mengikuti precondition TC (`Data Center`).
  - TC-FA-RP-1183 langkah 6 dan Expected e membutuhkan login Kevin Susanto; email dan nama env password tidak ada di Pre-setup TC maupun `suite.md`, disediakan tim FE.
  - TC-FA-RP-1183 Expected d hanya menyebut Changelog toolbar Detail Role `Manage files`; spec tidak mengasersi Changelog role lain. Expected e (tidak ada notifikasi) tidak punya anchor positif pengiriman notifikasi; spec memakai panel notifikasi yang terbuka dan selisih terhadap baseline.
