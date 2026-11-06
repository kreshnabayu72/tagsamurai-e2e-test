---
id: TC-FA-RP-E2E-348-assign-total-control-di-atas-gm-hapus-pola-gm-dulu
title: "Assign Total Control ke target Group Manager: baris pola GM dihapus lebih dulu (log per baris) lalu baris pola Total Control ditulis dalam satu transaksi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1198
coverage:
  web: automated
---

# Assign Total Control ke target Group Manager: baris pola GM dihapus lebih dulu (log per baris) lalu baris pola Total Control ditulis dalam satu transaksi

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 (langkah 31) | Kevin Susanto (target; memiliki akun login) | #13 | tidak tertulis di Pre-setup TC (disediakan tim FE) | disediakan tim FE (belum ada nama env di `suite.md`) |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, target), #18 (pohon Group: `IT Infrastructure` > `Data Center` > `Rack A1`), #19 (seed Role Transaksi), #24 (`Company Changelog`, log 25 entri campuran; dipakai sebagai latar log, tidak diasersi).
- Precondition TC (dipakai sebagai precondition TC, tidak diasersi): Kevin Susanto Group Manager hanya di `Data Center` dengan baris pola GM di `Data Center` dan `Rack A1` (Group Role katalog selain `Manage user & role` CRUD penuh sesuai kolom berlaku; Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi), baris non-pola `Manage user & role` di `Data Center`, dan memiliki akun login. Seed GM itu (Pre-setup #13 dan #43) dibuat lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri berdasarkan kombinasi kolom pada Changelog Detail Role `Manage files` (All Groups) dan Changelog Transaction Role sub-tab `Disposal`, serta jumlah notifikasi in-app Kevin Susanto (langkah 1). Entri dan notifikasi yang diasersi adalah selisih jumlah terhadap baseline, bukan posisi baris dan bukan total absolut (S-12). Jendela absence notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- State berat yang diubah dan pemulihannya (S-11): Assign Total Control mengubah Kevin Susanto menjadi Total Control, menghapus penugasan Group Manager dan baris pola GM (Group Role dan Role Transaksi) di `Data Center` dan `Rack A1`, lalu menulis baris pola Total Control. Changelog dan notifikasi bertambah (audit trail permanen, tidak dipulihkan). Hook `after` memulihkan Kevin Susanto ke state Pre-setup #13 (Group Manager hanya di `Data Center` dengan baris pola dan baris non-pola) beserta seed GM-nya lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #13 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1198: Assign Total Control ke target Group Manager: baris pola GM dihapus lebih dulu lalu baris pola Total Control ditulis

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri per Object dan Action pada Changelog Detail Role `Manage files` (`Remove (via Group Manager)` dan `Assign (via Total Control)` untuk Object `Manage files — Kevin Susanto — Data Center` dan `Manage files — Kevin Susanto — Rack A1`; `Remove (via Group Manager)` untuk Object `Manage user & role — Kevin Susanto — Data Center`), jumlah entri per Field dan Action pada Changelog Transaction Role sub-tab `Disposal` (`Remove (via Group Manager)` dan `Assign (via Total Control)` untuk Field `Asset Admin — Data Center`, `Approver — Data Center`, `Asset Admin — Rack A1`, `Approver — Rack A1`), dan jumlah notifikasi in-app Kevin Susanto
2. Klik `[+ Assign]` di Tab Total Control
3. Ketik Search `Kevin Susanto`, tekan Enter pada popup Assign
4. Centang Kevin Susanto
5. Klik `[Assign]`
6. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
7. Verifikasi Kevin Susanto tampil di Tab Total Control
8. Klik Tab `Group Manager`
9. Ketik Search `Kevin Susanto`, tekan Enter
10. Verifikasi tidak ada baris Kevin Susanto dengan badge Group `Data Center` di Tab Group Manager
11. Buka Tab `System` dan Detail Role Group Role `Manage files`
12. Klik `All Groups` di Sidebar Group Tree
13. Klik ikon Changelog di toolbar Detail Role
14. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove (via Group Manager)`, Object `Manage files — Kevin Susanto — Data Center`, Field `Access`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`
15. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove (via Group Manager)`, Object `Manage files — Kevin Susanto — Rack A1`, Field `Access`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`
16. Verifikasi entri `Remove (via Group Manager)` Object `Manage files — Kevin Susanto — Data Center` lebih lama (Date tidak lebih baru) dari entri `Assign (via Total Control)` Object yang sama
17. Verifikasi entri `Remove (via Group Manager)` Object `Manage files — Kevin Susanto — Rack A1` lebih lama (Date tidak lebih baru) dari entri `Assign (via Total Control)` Object yang sama
18. Verifikasi tidak ada entri baru untuk `Manage user & role` Kevin Susanto (jumlah entri Object `Manage user & role — Kevin Susanto — Data Center` sama dengan baseline langkah 1)
19. Tutup modal Changelog
20. Klik Tab `Transaction Role`
21. Klik node `Data Center` di Sidebar Group Tree
22. Klik sub-tab `Disposal`
23. Klik ikon Changelog pada baris sub-tab `Disposal`
24. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove (via Group Manager)`, Field `Asset Admin — Data Center`, Old Value `Kevin Susanto`, New Value `—`
25. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove (via Group Manager)`, Field `Approver — Data Center`, Old Value `Kevin Susanto`, New Value `—`
26. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove (via Group Manager)`, Field `Asset Admin — Rack A1`, Old Value `Kevin Susanto`, New Value `—`
27. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove (via Group Manager)`, Field `Approver — Rack A1`, Old Value `Kevin Susanto`, New Value `—`
28. Verifikasi entri `Remove (via Group Manager)` Field `Asset Admin — Data Center` dan `Approver — Data Center` lebih lama (Date tidak lebih baru) dari entri `Assign (via Total Control)` Field yang sama (New Value `Kevin Susanto`)
29. Verifikasi entri `Remove (via Group Manager)` Field `Asset Admin — Rack A1` dan `Approver — Rack A1` lebih lama (Date tidak lebih baru) dari entri `Assign (via Total Control)` Field yang sama (New Value `Kevin Susanto`)
30. Tutup modal Changelog
31. Ganti akun: logout, lalu login sebagai Kevin Susanto
32. Klik Bell icon
33. Verifikasi notifikasi `You are no longer Group Manager for Data Center` tampil
34. Tunggu 5 detik tanpa memuat ulang halaman
35. Verifikasi jumlah notifikasi Kevin Susanto bertambah tepat satu terhadap baseline langkah 1 (tidak ada notifikasi per baris pola)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 35 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (baseline entri Changelog dan notifikasi, S-12), 2, 8, 11, 12, 13, 20, 21, 22, 23 (membuka Tab, node, sub-tab, dan modal Changelog), 3 (Search kandidat di popup Assign supaya Kevin Susanto pasti tampil pada Table User Picker berpaginasi; R-22), 9 (Search baris target pada Tab Group Manager; R-16, 8b butir 13), 19 dan 30 (menutup modal), 34 (jendela absence notifikasi, bagian 6). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah 31 adalah ganti akun eksplisit (S-07) untuk notifikasi login target; notifikasi disusun sebagai langkah akhir spec ini (Kevin Susanto adalah target, bukan objek uji multi-konteks), bukan spec kelas c terpisah.
- Absence pada langkah 10 memakai hasil Search sebagai anchor (8b butir 2): hasil Search `Kevin Susanto` diproses (empty state `No results found` atau baris Kevin Susanto di node lain). Absence pada langkah 18 didahului langkah 14 dan 15 (entri `Remove (via Group Manager)` Kevin Susanto pada surface Changelog yang sama sudah tampil). Absence "tidak ada notifikasi per baris pola" pada langkah 35 berupa selisih jumlah tepat satu sesudah notifikasi tampil (langkah 33, anchor positif) dan jendela 5 detik (langkah 34).
- Kelas g tidak dipakai: asersi absence di spec ini punya aksi dalam alurnya (Assign Total Control) dan memakai baseline per baris; TC-FA-RP-1198 tidak dipindah ke spec absence.
- Search tidak dipakai pada Tab Total Control (langkah 7): tabel hanya memuat Default User, dua Total Control, dan Kevin Susanto. Search tidak dipakai pada Changelog: entri dikenali lewat kombinasi Action, Object atau Field, dan nilai serta selisih jumlahnya terhadap baseline (S-12, S-14).
- Pembagian TC lintas spec: tidak ada; TC-FA-RP-1198 hanya di spec ini.
- Post Condition TC-FA-RP-1198 ("tanpa sisa baris pola GM karena penugasan GM dilepas"; "pola Read Only dicakup Assign Read Only yang sama, TC-FA-RP-198") tidak punya langkah observasi di TC; tidak diasersi. Kevin Susanto dipulihkan di hook `after`.
- Temuan untuk QA:
  - Kevin Susanto Group Manager hanya di `Data Center` (Pre-setup #13 dan #43, Precondition d TC-FA-RP-1198) belum direkonsiliasi dengan Pre-setup #38 (Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`) dan TC yang menyebut Kevin Susanto di `Helpdesk`. Spec mengikuti Precondition d (hanya `Data Center`) dan tidak mengasersi baris non-pola `Helpdesk`.
  - Expected c "lebih lama dari entri `Assign (via Total Control)`" tidak punya cara membaca urutan yang pasti: kolom Date berketelitian menit dan kedua entri ditulis dalam satu transaksi. Spec mengasersi "Date tidak lebih baru" (longgar) dan tidak mengandalkan urutan baris dalam menit yang sama.
  - Nama Action `Remove (via Group Manager)` dan `Assign (via Total Control)` menunggu konfirmasi PM (PRD 12 Open Item #7); spec menulisnya persis seperti TC.
  - Expected c menyebut Changelog Detail Role "untuk `Data Center` dan `Rack A1`" tanpa menyebut node Sidebar yang dipilih; spec memakai `All Groups` mengikuti langkah 4 TC.
  - Expected d menyebut entri pada Changelog Transaction Role sub-tab `Disposal` untuk node `Data Center`, dan "entri yang sama untuk `Rack A1`"; spec mengasumsikan modal Changelog baris sub-tab memuat entri kedua node.
  - Expected e menulis teks `You are no longer Group Manager for Data Center` tanpa menyebut Title atau Body notifikasi; spec mengasersi teks itu persis tampil pada item notifikasi.
  - Email dan password akun Kevin Susanto tidak tertulis di Pre-setup TC dan `suite.md` belum memuat nama env untuknya; spec tidak mengarang nama env (disediakan tim FE).
  - `suite.md` (Pre-setup bersama) belum menyebut Pre-setup #13 sebagai pool yang dipulihkan; pemulihan Kevin Susanto beserta seed GM dijamin fixture backend yang disediakan tim FE/BE.
  - Notifikasi login target disusun sebagai langkah akhir spec ini (bukan spec kelas c terpisah); bila audit menilai sebagai kelas c, langkah 31 sampai 35 dipindah ke spec multi-konteks.
  - Post Condition tidak punya langkah observasi di TC; tidak diasersi.
