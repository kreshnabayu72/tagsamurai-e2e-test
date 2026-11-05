---
id: TC-FA-RP-E2E-363-remove-gm-bersarang-pelepasan-penugasan-terakhir-role-transaksi-dan-notifikasi
title: "Remove Group Manager bersarang: melepas penugasan terakhir menghapus baris pola bersama Group Role dan Role Transaksi dengan satu notifikasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1186
coverage:
  web: automated
---

# Remove Group Manager bersarang: melepas penugasan terakhir menghapus baris pola bersama Group Role dan Role Transaksi dengan satu notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard), #18 (pohon Group).
- Seeding precondition TC (dipakai sebagai precondition, tidak diasersi): Dimas Pranata Group Manager hanya di `Data Center`, dengan baris pola GM (Group Role katalog dan Role Transaksi Asset Admin dan Approver) di `Data Center` dan `Rack A1`. Keadaan ini adalah hasil langkah 1 dan 2 TC-FA-RP-1186 (spec 350) dan dibentuk ulang spec ini lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Spec tidak membuat data Dinamis.
- Kemampuan teknis: membaca (a) jumlah entri Changelog Detail Role `Manage files`, (b) jumlah entri Changelog Transaction Role `Data Center` sub-tab `Disposal` (audit trail permanen, S-12), dan (c) jumlah notifikasi in-app Dimas Pranata sebagai baseline dan hasil, tanpa login sebagai Dimas Pranata (disediakan tim FE/BE, tanpa endpoint karangan). Jendela asersi notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- Tabel node yang ditelusuri pada langkah 8 sampai 10:

  | Node dengan baris pola Dimas Pranata hilang |
  |---|
  | `Data Center` |
  | `Rack A1` |

- State yang diubah dan pemulihannya: Remove penugasan `Data Center` melepas penugasan Group Manager terakhir Dimas Pranata dan seluruh baris pola GM-nya. Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 (tanpa penugasan Group Manager) lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"). Entri Changelog dan notifikasi bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1186: langkah 3 dan 4, Remove penugasan terakhir `Data Center`

1. Catat baseline lewat kemampuan baca: jumlah entri Changelog Detail Role `Manage files`, jumlah entri Changelog Transaction Role `Data Center` sub-tab `Disposal`, dan jumlah notifikasi in-app Dimas Pranata
2. Klik Tab `Group Manager`
3. Ketik Search `Dimas Pranata`, tekan Enter
4. Klik `[⋯]` baris Dimas Pranata di `Data Center` lalu `Remove`
5. Klik `[Remove]` pada dialog konfirmasi
6. Verifikasi toast sukses `Success, Group Manager has been removed.`
7. Buka Tab `System` lalu Detail Role `Manage files`
8. Untuk setiap baris tabel "Node dengan baris pola Dimas Pranata hilang" (langkah 8 sampai 10 diulang untuk node itu): klik node pada Sidebar Group Tree
9. Verifikasi sedikitnya satu baris lain tampil pada node itu
10. Verifikasi baris Dimas Pranata pada node itu tidak ada
11. Klik ikon Changelog di toolbar Detail Role
12. Verifikasi jumlah entri Changelog bertambah dua terhadap baseline langkah 1 (satu entri per baris yang hilang)
13. Verifikasi dua entri baru teratas ber-Action `Remove (via Group Manager)` untuk Dimas Pranata pada `Data Center` dan pada `Rack A1`
14. Tutup modal Changelog
15. Klik Tab `Transaction Role`
16. Klik node `Data Center`
17. Klik sub-tab `Disposal`
18. Verifikasi sedikitnya satu baris tampil pada section Asset Admin
19. Verifikasi Dimas Pranata tidak tampil di section Asset Admin, Approver, Monitoring & Report, dan Staff
20. Klik ikon Changelog pada baris sub-tab `Disposal`
21. Verifikasi jumlah entri Changelog Transaction Role bertambah terhadap baseline langkah 1
22. Verifikasi entri baru ber-Action `Remove (via Group Manager)` per baris pola Role Transaksi Dimas Pranata (Asset Admin dan Approver) pada `Data Center`
23. Tutup modal Changelog
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Verifikasi jumlah notifikasi in-app Dimas Pranata bertambah tepat satu terhadap baseline langkah 1 (satu notifikasi per pelepasan penugasan, tidak per baris)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 25 langkah nominal (28 langkah setelah ekspansi langkah 8 sampai 10 untuk dua node).
- Pembagian TC lintas spec: TC-FA-RP-1186 dibagi dua. Spec 350 memuat langkah 1 dan 2 TC beserta Expected a dan b; spec ini memuat langkah 3 dan 4 beserta Expected c dan d. Spec ini tidak menumpang hasil spec 350: precondition-nya dibentuk lewat seeding API (S-04, S-06).
- Langkah penghubung (S-03): langkah 1 (baseline, S-12), langkah 2 sampai 5 (membuka Tab, Search mencari baris target, dan aksi Remove; R-16), langkah 7, 15 sampai 17 (navigasi), langkah 11, 14, 20, dan 23 (membuka dan menutup modal Changelog), langkah 24 (jendela notifikasi, bagian 6). Langkah 9 dan 18 adalah anchor positif atas asersi absence langkah 10 dan 19 (8b butir 2). Langkah 25 mengasersi selisih tepat satu sehingga kehadiran notifikasi sekaligus menjadi anchor atas "tidak per baris".
- Tanpa Search pada tabel Detail Role dan tabel Role Transaksi: precondition TC hanya memuat Pre-setup #15 dan #18, sehingga tiap node memuat paling banyak enam baris dalam satu halaman.
- Temuan untuk QA:
  - TC-FA-RP-1186 Expected d menyebut "satu notifikasi per pelepasan penugasan (tidak per baris)" tanpa langkah observasi dan tanpa akun login Dimas Pranata di Pre-setup #15; spec membaca jumlah notifikasi lewat kemampuan baca disediakan tim FE/BE (langkah 25) dan tidak membuka sesi Dimas Pranata. Teks notifikasi tidak ditulis di TC sehingga tidak diasersi.
  - TC-FA-RP-1186 Expected d menyebut "entri `Remove (via Group Manager)` per baris" tanpa jumlah; spec menyimpulkan dua entri pada Detail Role `Manage files` (`Data Center` dan `Rack A1`). Entri Changelog Transaction Role tidak diberi jumlah karena TC tidak menyebut jenis transaksi yang dihitung; langkah 21 hanya mengasersi pertambahan. Nama Action `Remove (via Group Manager)` mengikuti TC dan menunggu keputusan PM (Open Item #7c).
  - Post Condition "Dimas Pranata dipulihkan ke state Pre-setup #15 oleh automation baseline" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
