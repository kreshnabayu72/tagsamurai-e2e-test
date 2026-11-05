---
id: TC-FA-RP-E2E-386-picker-asset-admin-ber-constraint-node-sama-dan-descendant-ya-sibling-dan-ancestor-tidak
title: "Picker Asset Admin untuk user ber-constraint: node sama dan descendant ya, sibling dan ancestor tidak"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1225
coverage:
  web: automated
---

# Picker Asset Admin untuk user ber-constraint: node sama dan descendant ya, sibling dan ancestor tidak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Gunawan Halim, Home Group `Data Center`; Active, Activated), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`), dan #19 (penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal`).
- Kemampuan teknis (disediakan tim FE/BE lewat fixture BE, tanpa endpoint karangan): seeding precondition TC di hook `before` berupa Gunawan Halim tanpa penugasan Role Transaksi pada node mana pun (penugasan yang tersisa dicabut; dipakai sebagai precondition TC, tidak diasersi), serta pemulihan Pre-setup #17 dan #19 ke kondisi Tabel Data Uji Pre-setup TC di hook `after` sebagai cadangan.
- Data Dinamis: tidak ada data yang dibuat spec. Spec tidak menyimpan penugasan apa pun (tanpa klik `[Assign]`); tidak ada state yang berubah selain pembukaan dan penutupan popup, sehingga tidak ada pemulihan tambahan di luar cadangan hook `after` di atas.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture. Spec ini tidak login sebagai Gunawan Halim.

## Test Steps

### TC-FA-RP-1225: Picker Asset Admin untuk user ber-constraint: node sama dengan constraint dan descendant eligible, sibling dan ancestor tidak

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Gunawan Halim`, tekan Enter
4. Verifikasi Gunawan Halim ada di daftar picker (node sama dengan constraint)
5. Tutup popup Assign lewat `[×]`
6. Klik node `Rack A1` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
7. Klik `[+ Assign]` pada section Asset Admin
8. Ketik Search `Gunawan Halim`, tekan Enter
9. Verifikasi Gunawan Halim ada di daftar picker (descendant constraint)
10. Tutup popup Assign lewat `[×]`
11. Klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
12. Klik `[+ Assign]` pada section Asset Admin
13. Ketik Search `Gunawan Halim`, tekan Enter
14. Verifikasi empty state `No results found` tampil sehingga Gunawan Halim tidak ada di daftar picker (sibling di luar constraint)
15. Tutup popup Assign lewat `[×]`
16. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
17. Klik `[+ Assign]` pada section Asset Admin
18. Ketik Search `Gunawan Halim`, tekan Enter
19. Verifikasi empty state `No results found` tampil sehingga Gunawan Halim tidak ada di daftar picker (ancestor di atas constraint)
20. Tutup popup Assign lewat `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 20 langkah.
- Langkah penghubung (S-03): langkah 1, 6, 11, dan 16 (navigasi Tab, node, sub-tab; sub-tab `Disposal` diklik ulang di tiap node agar sub-tab aktif deterministik), langkah 2, 7, 12, dan 17 (membuka popup Assign), dan langkah 5, 10, 15, dan 20 (menutup popup, S-09). Langkah 3, 8, 13, dan 18 adalah Search nama kandidat di Table User Picker yang dapat memuat lebih dari satu halaman (R-16, R-22).
- Asersi absence langkah 14 dan 19 memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); langkah 4 dan 9 membuktikan pada sesi dan user yang sama bahwa Gunawan Halim muncul di picker bila node memenuhi constraint, sehingga hasil kosong pada langkah 14 dan 19 bukan karena user tidak dimuat. Spec tidak menyimpan penugasan, tanpa asersi log (S-05).
- Penjelasan dalam kurung pada Expected c dan d TC ("sibling di luar constraint", "ancestor di atas constraint ditolak walau cakupan penugasan di node itu meliputi `Data Center`") adalah rasional perilaku dan tidak diasersi tersendiri (S-01); yang diasersi adalah keberadaan atau ketiadaan Gunawan Halim di daftar picker.
- Temuan untuk QA:
  - NC-20 / Open Item #9 (menunggu PM): arah gate Home Group sebagai constraint (node sama dan descendant eligible, ancestor dan sibling tidak) belum dikonfirmasi PM; bila PM menetapkan lain, Expected 1225.a sampai 1225.d usang.
  - TC-FA-RP-1225 tidak memuat asersi preview scope popup dan PRD tidak memuat locator preview scope atau empty state picker; spec tidak mengasersi preview scope. Teks empty state `No results found` mengikuti pola picker pada spec lain di suite ini; TC hanya menyebut "tidak ada di daftar picker".
  - Email Gunawan Halim tidak tertulis di Pre-setup #17; spec ini tidak login sebagai Gunawan Halim. Bila spec lain memakai sesinya, kredensial lewat env `FA_GUNAWAN_PASSWORD` (terdaftar di `suite.md`), tanpa password di spec atau fixture.
  - Precondition TC-FA-RP-1225 ("tanpa penugasan Role Transaksi") tidak menyebut cara membentuknya; spec menetapkannya lewat fixture BE yang disediakan tim FE/BE (kemampuan seeding dan pemulihan Pre-setup #17 belum punya nama di Pre-setup).
  - TC-FA-RP-1225 menyebut `Rack A1` sebagai descendant `Data Center` dan `Helpdesk` sebagai sibling; keduanya sesuai Pre-setup #18.
  - Post Condition TC-FA-RP-1225 kosong ("-").
