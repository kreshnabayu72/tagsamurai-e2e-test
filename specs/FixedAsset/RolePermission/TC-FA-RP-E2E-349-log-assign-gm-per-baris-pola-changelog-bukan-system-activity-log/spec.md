---
id: TC-FA-RP-E2E-349-log-assign-gm-per-baris-pola-changelog-bukan-system-activity-log
title: "Log Assign Group Manager per baris pola: Assign (via Group Manager) di Changelog, tidak di System Log dan Activity Log, tanpa notifikasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1181
coverage:
  web: automated
---

# Log Assign Group Manager per baris pola: Assign (via Group Manager) di Changelog, tidak di System Log dan Activity Log, tanpa notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 (langkah 32) | Dimas Pranata (target; memiliki akun login) | #15 | tidak tertulis di Pre-setup TC (disediakan tim FE) | disediakan tim FE (belum ada nama env di `suite.md`) |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard; target Assign Group Manager), #18 (pohon Group: `IT Infrastructure` > `Data Center` > `Rack A1`), #24 (`Company Changelog`, log 25 entri campuran; dipakai sebagai latar log, tidak diasersi).
- Precondition TC (dipakai sebagai precondition TC, tidak diasersi): Dimas Pranata tanpa penugasan di subtree `Data Center` dan memiliki akun login. Kondisi itu dibuat lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri berdasarkan kombinasi kolom pada Changelog Detail Role `Manage files` (All Groups), Changelog Transaction Role sub-tab `Disposal`, Changelog: User Dimas Pranata (Group Role dan Transaction Role), System Log aktor Siti Rahmawati, dan Activity Log FAMS, serta jumlah notifikasi in-app Dimas Pranata (langkah 1). Entri dan notifikasi yang diasersi adalah selisih jumlah terhadap baseline, bukan posisi baris dan bukan total absolut (S-12). Jendela absence notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- State yang diubah dan pemulihannya: Assign Group Manager menulis penugasan Group Manager Dimas Pranata di `Data Center` dan baris pola Group Role dan Role Transaksi di `Data Center` dan `Rack A1`. Changelog bertambah entri (audit trail permanen, tidak dipulihkan). Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1181: Log Assign Group Manager per baris pola (Changelog Detail Role, Transaction Role, Changelog: User; tidak di System Log dan Activity Log; tanpa notifikasi)

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign (via Group Manager)` untuk Dimas Pranata pada Changelog Detail Role `Manage files` (Object `Manage files — Dimas Pranata — Data Center` dan `— Rack A1`; Object `Manage user & role` Dimas Pranata), Changelog Transaction Role sub-tab `Disposal` (Field `Asset Admin` dan `Approver` untuk `Data Center` dan `Rack A1`), dan Changelog: User Dimas Pranata (Group Role dan Transaction Role); jumlah entri Action `Assign (via Group Manager)` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS; jumlah notifikasi in-app Dimas Pranata
2. Klik Tab `Group Manager`
3. Klik `[+ Assign]` di Tab Group Manager
4. Pilih group `Data Center` pada field Group
5. Ketik Search `Dimas Pranata`, tekan Enter pada popup Assign
6. Centang Dimas Pranata
7. Klik `[Assign]`
8. Tunggu aksi selesai: popup Assign tertutup
9. Buka Tab `System` dan Detail Role Group Role `Manage files`
10. Klik `All Groups` di Sidebar Group Tree
11. Klik ikon Changelog di toolbar Detail Role
12. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Assign (via Group Manager)`, Object `Manage files — Dimas Pranata — Data Center`, Field `Access`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`
13. Verifikasi modal memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Assign (via Group Manager)`, Object `Manage files — Dimas Pranata — Rack A1`, Field `Access`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`
14. Verifikasi tidak ada entri baru untuk `Manage user & role` Dimas Pranata (jumlah entri Object `Manage user & role` Dimas Pranata sama dengan baseline langkah 1)
15. Tutup modal Changelog
16. Klik Tab `Transaction Role`
17. Klik node `Data Center` lalu sub-tab `Disposal`
18. Klik ikon Changelog pada baris sub-tab `Disposal`
19. Verifikasi modal memuat satu entri baru per baris pola (jumlah tiap kombinasi bertambah tepat satu terhadap baseline langkah 1): Action `Assign (via Group Manager)`, Field `Asset Admin — Data Center` dan `Approver — Data Center`, Old Value `—`, New Value `Dimas Pranata`
20. Verifikasi modal memuat satu entri baru per baris pola (jumlah tiap kombinasi bertambah tepat satu terhadap baseline langkah 1): Action `Assign (via Group Manager)`, Field `Asset Admin — Rack A1` dan `Approver — Rack A1`, Old Value `—`, New Value `Dimas Pranata`
21. Tutup modal Changelog
22. Buka Settings > User > Detail Dimas Pranata > Changelog: User > Group Role
23. Verifikasi Changelog: User Group Role memuat entri baru Action `Assign (via Group Manager)` dengan Field `Manage files — Data Center` (jumlah entri bertambah terhadap baseline langkah 1)
24. Klik Transaction Role pada Changelog: User
25. Verifikasi Changelog: User Transaction Role memuat entri baru Action `Assign (via Group Manager)` per baris pola Role Transaksi (jumlah entri bertambah terhadap baseline langkah 1)
26. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
27. Verifikasi sedikitnya satu entri lain tampil di System Log aktor Siti Rahmawati
28. Verifikasi System Log aktor tidak memuat entri baru Action `Assign (via Group Manager)` per baris pola (jumlah entri sama dengan baseline langkah 1)
29. Buka Activity Log FAMS (menu Activity Log)
30. Verifikasi sedikitnya satu entri lain tampil di Activity Log
31. Verifikasi Activity Log tidak memuat entri baru Action `Assign (via Group Manager)` per baris pola (jumlah entri sama dengan baseline langkah 1)
32. Ganti akun: logout, lalu login sebagai Dimas Pranata
33. Klik Bell icon
34. Verifikasi panel notifikasi tampil
35. Tunggu 5 detik tanpa memuat ulang halaman
36. Verifikasi jumlah notifikasi Dimas Pranata sama dengan baseline langkah 1 (tidak ada notifikasi)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 36 langkah.
- Kelas g (asersi absence, 13g): langkah 14, 28, 31, dan 36 mengasersi tidak ada pencatatan atau notifikasi. Pemicu Assign Group Manager (langkah 2 sampai 8) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5`). Anchor positif: entri Changelog langkah 12 dan 13 (pemicu yang sama, Changelog Detail Role) untuk langkah 14; entri lain pada surface yang sama (langkah 27 dan 30) untuk System Log dan Activity Log (8b butir 2); panel notifikasi tampil (langkah 34) dan jendela 5 detik (langkah 35) untuk langkah 36 (8b butir 11 dan bagian 6). Tiap absence memakai baseline sendiri (langkah 1, S-12).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (baseline, S-12), 2, 9, 10, 11, 16, 17, 18, 22, 24, 26, 29 (membuka Tab, node, sub-tab, modal Changelog, dan surface lain), 8 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), 5 (Search kandidat di popup Assign supaya Dimas Pranata pasti tampil pada Table User Picker berpaginasi; R-22), 15 dan 21 (menutup modal), 35 (jendela absence notifikasi). Akun aktor pertama sudah login di hook `before` (S-07). Langkah 22 dan 26 menyalin jalur navigasi ke Detail user persis seperti langkah TC (satu langkah navigasi, tanpa Search nama tersendiri).
- Langkah 32 adalah ganti akun eksplisit (S-07) untuk notifikasi login target; notifikasi disusun sebagai langkah akhir spec ini (Dimas Pranata adalah target, bukan objek uji multi-konteks), bukan spec kelas c terpisah.
- Entri dikenali lewat kombinasi Action, Object atau Field, dan nilai serta selisih jumlahnya terhadap baseline; posisi baris dan total entri tidak diasersi (S-12, S-14). Langkah 19 dan 20 menyebut dua Field pada satu node dalam satu `Verifikasi` karena Expected b TC menyebutnya sebagai contoh (`mis.`) yang berurutan (daftar disebut utuh).
- Alasan ukuran spec (36 langkah, di atas smell sekitar 35): satu TC tunggal dengan satu pemicu (Assign Group Manager) yang diamati pada tujuh permukaan (Changelog Detail Role, Changelog Transaction Role, Changelog: User dua tab, System Log, Activity Log, notifikasi); semua blok satu kelas harness (log dan notifikasi, tanpa harness eksternal) dan memakai state yang sama sehingga memisahkannya hanya mengulang pemicu dan seeding. Tidak ada blok yang berdiri sendiri tanpa pemicu.
- Pembagian TC lintas spec: TC-FA-RP-1179 (baris pola Group Role pada Assign Group Manager yang sama) ada di spec 346 dan TC-FA-RP-1180 (baris pola Role Transaksi) ada di spec 361; tidak ada asersi log di spec itu.
- Post Condition TC-FA-RP-1181 ("Dimas Pranata dipulihkan ke state Pre-setup #15 oleh automation baseline"; "nama Action menunggu konfirmasi PM (PRD 12 #7)") tidak punya langkah observasi; tidak diasersi, dipulihkan di hook `after`.
- Temuan untuk QA:
  - Nama Action `Assign (via Group Manager)` menunggu konfirmasi PM (PRD 12 Open Item #7); spec menulisnya persis seperti TC.
  - Expected b menyebut Field Role Transaksi sebagai contoh (`mis.` Asset Admin dan Approver, juga `Rack A1`) dan "satu entri per baris pola"; spec mengasersi hanya contoh itu, bukan seluruh baris pola pada setiap sub-tab.
  - Expected c menulis "entri yang sama tampil per baris" di Changelog: User Transaction Role tanpa menyebut Field; spec mengasersi entri `Assign (via Group Manager)` per baris pola Role Transaksi tampil dengan selisih jumlah terhadap baseline (longgar).
  - Expected d "System Log dan Activity Log aktor tidak memuat entri `Assign (via Group Manager)` per baris pola" tidak punya anchor positif di TC dan tidak menyebut Object entri; spec memakai Action sebagai kunci baseline dan entri lain pada surface yang sama sebagai anchor.
  - Expected e "tidak ada notifikasi untuk Dimas Pranata" tidak punya anchor positif pengiriman notifikasi; spec memakai panel notifikasi yang terbuka dan selisih nol terhadap baseline.
  - Email dan password akun Dimas Pranata tidak tertulis di Pre-setup TC dan `suite.md` belum memuat nama env untuknya; spec tidak mengarang nama env (disediakan tim FE).
  - Notifikasi login target disusun sebagai langkah akhir spec ini (bukan spec kelas c terpisah); bila audit menilai sebagai kelas c, langkah 32 sampai 36 dipindah ke spec multi-konteks. TC-FA-RP-1181 tidak ada di spec absence log lain (291 sampai 294) karena memuat aksi Assign sendiri.
  - Post Condition tidak punya langkah observasi di TC; tidak diasersi.
