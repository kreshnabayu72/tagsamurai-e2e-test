---
id: TC-FA-RP-E2E-350-remove-gm-bersarang-pelepasan-penugasan-ancestor-baris-pola-tercakup-dipertahankan
title: "Remove Group Manager bersarang: melepas penugasan ancestor menghapus baris pola di luar cakupan dan mempertahankan baris pola yang masih tercakup penugasan lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1186
coverage:
  web: automated
---

# Remove Group Manager bersarang: melepas penugasan ancestor menghapus baris pola di luar cakupan dan mempertahankan baris pola yang masih tercakup penugasan lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`).
- Seeding precondition d TC (dipakai sebagai precondition, tidak diasersi): Dimas Pranata Group Manager di `IT Infrastructure` dan di `Data Center`, dengan baris pola GM pada node penugasan dan descendant-nya (baris pola bersama di `Data Center` dan `Rack A1`). Dibentuk lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Spec tidak membuat data Dinamis.
- Kemampuan teknis: membaca jumlah entri Changelog Detail Role `Manage files` sebagai baseline (audit trail permanen, S-12; disediakan tim FE/BE).
- Tabel node yang ditelusuri pada langkah 8 sampai 12:

  | Node dengan baris Dimas Pranata hilang | Node dengan baris Dimas Pranata dipertahankan |
  |---|---|
  | `IT Infrastructure` | `Data Center` |
  | `Helpdesk` | `Rack A1` |

- State yang diubah dan pemulihannya: Remove Group Manager di `IT Infrastructure` melepas satu penugasan dan baris pola di luar cakupan penugasan `Data Center`. Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 (tanpa penugasan Group Manager) lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Entri Changelog bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1186: langkah 1 dan 2, Remove penugasan `IT Infrastructure` dan pengamatan baris pola Detail Role

1. Catat jumlah entri Changelog Detail Role `Manage files` sebagai baseline lewat kemampuan baca
2. Klik Tab `Group Manager`
3. Ketik Search `Dimas Pranata`, tekan Enter
4. Klik `[⋯]` baris Dimas Pranata di `IT Infrastructure` lalu `Remove`
5. Klik `[Remove]` pada dialog konfirmasi
6. Verifikasi toast sukses `Success, Group Manager has been removed.`
7. Buka Tab `System` lalu Detail Role `Manage files`
8. Untuk setiap baris kolom "Node dengan baris Dimas Pranata hilang" (langkah 8 sampai 10 diulang untuk node itu): klik node pada Sidebar Group Tree
9. Verifikasi sedikitnya satu baris lain tampil pada node itu
10. Verifikasi baris Dimas Pranata pada node itu tidak ada
11. Untuk setiap baris kolom "Node dengan baris Dimas Pranata dipertahankan" (langkah 11 dan 12 diulang untuk node itu): klik node pada Sidebar Group Tree
12. Verifikasi baris Dimas Pranata pada node itu tampil
13. Klik ikon Changelog di toolbar Detail Role
14. Verifikasi jumlah entri Changelog bertambah dua terhadap baseline langkah 1 (satu entri per baris yang hilang)
15. Verifikasi dua entri baru teratas ber-Action `Remove (via Group Manager)` untuk Dimas Pranata pada `IT Infrastructure` dan pada `Helpdesk`
16. Verifikasi tidak ada entri baru `Remove (via Group Manager)` untuk Dimas Pranata pada `Data Center` dan `Rack A1`
17. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 17 langkah nominal (22 langkah setelah ekspansi langkah 8 sampai 10 untuk dua node dan langkah 11 dan 12 untuk dua node).
- Pembagian TC lintas spec: TC-FA-RP-1186 dibagi dua. Spec ini memuat langkah 1 dan 2 TC beserta Expected a dan b; spec 363 memuat langkah 3 dan 4 beserta Expected c dan d (Remove penugasan `Data Center`, Role Transaksi, dan notifikasi). Keduanya menyiapkan state sendiri lewat seeding API (S-04, S-06).
- Langkah penghubung (S-03): langkah 1 (baseline, S-12), langkah 2 sampai 5 (membuka Tab, Search, dan aksi Remove; Search pada langkah 3 mencari baris target, R-16), langkah 7 (navigasi), langkah 13 dan 17 (membuka dan menutup modal Changelog). Langkah 9 adalah anchor positif atas asersi absence langkah 10 (8b butir 2); langkah 12 dan 14 sampai 15 menjadi anchor positif atas langkah 16.
- Tanpa Search pada tabel Detail Role: precondition TC hanya memuat Pre-setup #15 dan #18, sehingga tiap node memuat paling banyak tujuh baris (lima baris pola Total Control dan Read Only ditambah baris pola GM Dimas Pranata) dalam satu halaman.
- Temuan untuk QA:
  - TC-FA-RP-1186 Expected b menyebut "entri `Remove (via Group Manager)` per baris" tanpa jumlah; spec menyimpulkan dua entri baru pada Detail Role `Manage files` (satu untuk `IT Infrastructure`, satu untuk `Helpdesk`) dan mengasersi selisih dua terhadap baseline (langkah 14).
  - Nama Action `Remove (via Group Manager)` mengikuti TC; nama final menunggu keputusan PM (Open Item #7c). TC tidak menyebut kolom entri Changelog yang memuat nama node; langkah 15 dan 16 mengasersi node sebagai bagian entri.
  - Post Condition "Dimas Pranata dipulihkan ke state Pre-setup #15 oleh automation baseline" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
  - Pre-setup #38 (fixture terpisah) menaruh Dimas Pranata sebagai Group Manager di `Rack A1`; precondition TC-FA-RP-1186 tidak memuat #38 dan spec ini tidak mengandalkannya.
