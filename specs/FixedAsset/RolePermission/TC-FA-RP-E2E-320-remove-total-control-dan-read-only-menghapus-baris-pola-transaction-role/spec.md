---
id: TC-FA-RP-E2E-320-remove-total-control-dan-read-only-menghapus-baris-pola-transaction-role
title: "Remove Total Control dan Read Only menghapus baris pola Transaction Role pada semua sub-tab dan node"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1148
  - TC-FA-RP-1149
coverage:
  web: automated
---

# Remove Total Control dan Read Only menghapus baris pola Transaction Role pada semua sub-tab dan node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Addon On` (Pre-setup #31; ketiga lisensi Addon Audit, Maintenance, dan Tracking aktif), email disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.FA_ADDON_ON_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup: #15 (Ahmad Fauzi, pool pengguna Standard), #18 (pohon Group Company Alpha, tujuh node), #19 (seed Role Transaksi: baris manual Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report, Putri Wulandari Staff, dan Pandu Wijaya Approver pada `IT Infrastructure` sub-tab `Disposal`; baris pola pada setiap node dan sub-tab), #31 (`Client Addon On`).
- Precondition TC-FA-RP-1148: Ahmad Fauzi di-seed berstatus Total Control dengan baris pola Transaction Role lengkap (Asset Admin dan Approver pada setiap Jenis Transaksi × Group) lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Precondition TC-FA-RP-1149: Ahmad Fauzi di-seed berstatus Read Only dengan baris pola Monitoring & Report lengkap, dibentuk di langkah 11 (dipakai sebagai precondition TC, tidak diasersi).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): Ahmad Fauzi dikembalikan ke state Pre-setup #15 (Standard, tanpa baris pola) beserta penugasan Global Role dan Group Role yang direset oleh Remove, mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (suite.md, Pre-setup bersama). Setelah Remove di langkah 2 dan 14 Ahmad Fauzi kembali Standard sehingga tidak ada langkah pemulihan di tengah spec.
- Identitas Pre-setup mengacu ke fixture `Fixture.fixedAssetRolePermission` (belum ada di repo, tanpa password; ditandai untuk tim FE).
- Env var yang dipakai: `FA_ADDON_ON_TC_PASSWORD`, `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

Node pohon Pre-setup #18 yang ditelusuri (langkah 6 sampai 8 dan 18 sampai 20):

| Node |
|---|
| `Head Office` |
| `IT Infrastructure` |
| `Data Center` |
| `Rack A1` |
| `Helpdesk` |
| `Logistics Warehouse` |
| `Dock 1` |

Sub-tab Transaction Role yang ditelusuri pada tiap node (`Client Addon On` menampilkan kesembilannya):

| Sub-tab |
|---|
| `Disposal` |
| `Transfer` |
| `Borrowing & Assignment` |
| `Damaged` |
| `Missing` |
| `Audit` |
| `Repair Ticketing` |
| `Tracking` |
| `Maintenance Routine` |

## Test Steps

### TC-FA-RP-1148: Confirm Remove Total Control: baris pola Transaction Role Asset Admin dan Approver terhapus pada semua Jenis Transaksi × Group

1. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
2. Klik `[Remove]`
3. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
4. Klik Tab `Transaction Role`
5. Verifikasi sedikitnya satu baris tampil pada tabel Role Transaksi
6. Untuk setiap baris tabel "Node": klik node pada Sidebar Group Tree (langkah 7 dan 8 diulang untuk setiap baris tabel "Sub-tab" di node itu)
7. Klik sub-tab pada tabel "Sub-tab"
8. Verifikasi Ahmad Fauzi tidak tampil di section mana pun pada sub-tab dan node itu
9. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
10. Verifikasi baris manual Nadia Putri (Asset Admin), Oscar Pratama (Monitoring & Report), Putri Wulandari (Staff), dan Pandu Wijaya (Approver) tetap tampil di section masing-masing dan tidak berubah

### TC-FA-RP-1149: Confirm Remove Read Only: baris pola Monitoring & Report terhapus pada semua Jenis Transaksi × Group

11. Tetapkan Ahmad Fauzi sebagai Read Only dengan baris pola Monitoring & Report lengkap lewat seeding API
12. Klik Tab `Total Control` lalu klik Tab `Read Only`
13. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
14. Klik `[Remove]`
15. Verifikasi muncul toast sukses: `Success, Read Only has been removed.`
16. Klik Tab `Transaction Role`
17. Verifikasi sedikitnya satu baris tampil pada tabel Role Transaksi
18. Untuk setiap baris tabel "Node": klik node pada Sidebar Group Tree (langkah 19 dan 20 diulang untuk setiap baris tabel "Sub-tab" di node itu)
19. Klik sub-tab pada tabel "Sub-tab"
20. Verifikasi Ahmad Fauzi tidak tampil di section mana pun pada sub-tab dan node itu
21. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
22. Verifikasi baris manual user lain (Nadia Putri, Oscar Pratama, Putri Wulandari, dan Pandu Wijaya) tetap tampil di section masing-masing dan tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- Langkah penghubung (S-03): langkah 4 dan 16 (membuka Tab Transaction Role, langkah TC 3), langkah 6, 7, 9, 18, 19, 21 (penelusuran node dan sub-tab, langkah TC 3 dan 4), langkah 12 (memuat ulang data tabel sesudah seeding). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding (S-04, S-09): langkah 11; tidak ada `Verifikasi`.
- Langkah 5 dan 17 adalah anchor positif untuk asersi absence langkah 8 dan 20 (butir 8b.2); toast sukses langkah 3 dan 15 menjadi anchor bahwa Remove sudah diproses server. Keduanya dicatat sebagai asersi tambahan di luar TC (S-03).
- Penelusuran sembilan sub-tab × tujuh node memakai idiom "Untuk setiap baris tabel" (8b.7): langkah 7 dan 8 diulang 63 kali per TC (langkah 19 dan 20 untuk TC kedua), sehingga ekspansi seluruh spec sekitar 290 langkah, jauh di atas smell sekitar 35 langkah. Alasan mempertahankannya dalam satu spec: Expected b kedua TC mensyaratkan penelusuran setiap kombinasi sub-tab dan node, kedua TC berkelas sama (fungsional), memakai akun, client, target, dan dataset yang sama, dan memakai blok ulang identik yang parameternya ada di tabel Prerequisites tanpa langkah bersyarat; memecahnya tidak mengurangi ekspansi. Nomor cadangan 339 dan 340 tidak dipakai.
- Search tidak dipakai untuk menemukan baris Ahmad Fauzi: Tab Total Control dan Tab Read Only memuat 9 dan 4 baris (Pre-setup #36 dan #37), tidak melebihi satu halaman.
- Temuan untuk QA:
  - TC-FA-RP-1148 dan 1149 mensyaratkan `Login pada Client Addon On` (Pre-setup #31) tanpa email akun; spec memakai Total Control `Client Addon On` (`FA_ADDON_ON_TC_PASSWORD`), bukan Siti Rahmawati (`FA_TC_PASSWORD`). Email tidak tertulis di Pre-setup TC.
  - Pre-setup #40 menyebut Ahmad Fauzi sebagai baris manual Asset Admin pada `IT Infrastructure` sub-tab `Disposal`, sedangkan #19 (dirujuk TC) tidak menyebutnya dan Expected b TC-FA-RP-1148 dan 1149 menyatakan Ahmad Fauzi tidak tampil di section mana pun. Spec mengikuti #19 dan TC; baris manual Ahmad Fauzi tidak diseed.
  - TC-FA-RP-1149 Expected c "baris manual user lain tidak berubah" tidak menyebut nama; spec memakai empat baris manual Pre-setup #19 yang sama dengan TC-FA-RP-1148 (asumsi).
  - TC-FA-RP-1148 dan 1149 Post Condition "Log `Remove` per baris pola tercatat" tidak punya langkah observasi di TC dan tidak diasersi; rujukannya TC-FA-RP-1163 (spec 335).
  - TC-FA-RP-1148 dan 1149 tidak menyebut `Rina Wulandari` dan Pre-setup #3 padahal Expected b mencakup semua baris pola; spec hanya mengasersi Ahmad Fauzi.
  - Pernyataan Pre-setup bersama di `suite.md` belum menyebut Pre-setup #31 untuk akun `Client Addon On`; akunnya sudah tercatat di bagian "Env password akun aktor".
