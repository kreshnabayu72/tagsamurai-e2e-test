---
id: TC-FA-RP-E2E-361-assign-gm-menulis-baris-pola-role-transaksi-asset-admin-dan-approver
title: "Assign Group Manager menulis baris pola Role Transaksi (Asset Admin dan Approver) pada setiap Jenis Transaksi di node penugasan dan descendant"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1180
coverage:
  web: automated
---

# Assign Group Manager menulis baris pola Role Transaksi (Asset Admin dan Approver) pada setiap Jenis Transaksi di node penugasan dan descendant

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Addon On` (Pre-setup #31; lisensi Addon Audit, Maintenance, Tracking aktif), email tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), kredensial `Spectra.env.FA_ADDON_ON_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup pada `Client Addon On` (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard; target Assign Group Manager), #18 (pohon Group: `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`), #19 (seed Role Transaksi; header `Data Center` sub-tab `Disposal`: Asset Admin 3 dan Approver 3), #31 (`Client Addon On`).
- Precondition TC (dipakai sebagai precondition TC, tidak diasersi): Dimas Pranata tanpa penugasan Role Transaksi di `Data Center`, `Rack A1`, dan `Helpdesk`, serta seed Group Manager Pre-setup #5, #11, #13, #14, dan #43 tidak dimuat (hitungan header #19 berlaku tanpa seed Group Manager). Kondisi itu dibuat lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Tabel iterasi node (urutan baris = urutan iterasi): `Data Center`, `Rack A1`.
- Tabel iterasi sub-tab (urutan baris = urutan iterasi; kolom Section Staff mengikuti screening TC-FA-RP-9 untuk sub-tab tanpa Staff):

| No | Sub-tab | Section Staff |
|---|---|---|
| 1 | `Disposal` | Ada |
| 2 | `Transfer` | Ada |
| 3 | `Borrowing & Assignment` | Tidak ada |
| 4 | `Damaged` | Tidak ada |
| 5 | `Missing` | Tidak ada |
| 6 | `Audit` | Ada |
| 7 | `Repair Ticketing` | Ada |
| 8 | `Tracking` | Ada |
| 9 | `Maintenance Routine` | Ada |

- State yang diubah dan pemulihannya: Assign Group Manager menulis penugasan Group Manager Dimas Pranata di `Data Center` dan baris pola Role Transaksi (Asset Admin dan Approver) pada setiap sub-tab di `Data Center` dan `Rack A1`. Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 (tanpa penugasan) lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_ADDON_ON_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1180: Assign Group Manager menulis baris pola Role Transaksi (Asset Admin dan Approver) pada setiap Jenis Transaksi di node penugasan dan descendant

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Pilih group `Data Center` pada field Group
4. Centang Dimas Pranata
5. Klik `[Assign]`
6. Tunggu aksi selesai: popup Assign tertutup
7. Klik Tab `Transaction Role`
8. Untuk setiap baris tabel iterasi node (langkah 8 sampai 14): klik node pada baris tabel di Sidebar Group Tree
9. Untuk setiap baris tabel iterasi sub-tab (langkah 9 sampai 14): klik sub-tab pada baris tabel
10. Verifikasi Dimas Pranata tampil di section Asset Admin sebagai baris biasa
11. Verifikasi Dimas Pranata tampil di section Approver sebagai baris biasa
12. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report
13. Verifikasi Dimas Pranata tidak tampil di section Monitoring & Report
14. Verifikasi Dimas Pranata tidak tampil di section Staff (pada sub-tab tanpa section Staff menurut tabel iterasi, section itu sendiri tidak tampil)
15. Klik node `Helpdesk` di Sidebar Group Tree
16. Klik sub-tab `Disposal`
17. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin
18. Verifikasi tidak ada baris Dimas Pranata di section Asset Admin, Monitoring & Report, Staff, dan Approver
19. Klik node `Data Center` di Sidebar Group Tree
20. Klik sub-tab `Disposal`
21. Verifikasi header section Asset Admin menjadi 4 (baseline Pre-setup #19: 3)
22. Verifikasi header section Approver menjadi 4 (baseline Pre-setup #19: 3)
23. Klik Tab `Group Manager`
24. Ketik Search `Dimas Pranata`, tekan Enter
25. Verifikasi baris Dimas Pranata tampil di Tab Group Manager
26. Klik Tab `Total Control`
27. Ketik Search `Dimas Pranata`, tekan Enter
28. Verifikasi tidak ada baris Dimas Pranata di Tab Total Control (empty state `No results found`)
29. Klik Tab `Read Only`
30. Ketik Search `Dimas Pranata`, tekan Enter
31. Verifikasi tidak ada baris Dimas Pranata di Tab Read Only (empty state `No results found`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1, 7, 23, 26, 29 (membuka Tab), 6 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), 8, 9, 15, 16, 19, 20 (memilih node dan sub-tab). Langkah 24, 27, dan 30 (Search Dimas Pranata) adalah langkah penghubung supaya baris target ditemukan pada tabel yang dapat memuat lebih dari satu halaman (R-16, 8b butir 13); empty state `No results found` hasil Search menjadi anchor positif untuk absence pada langkah 28 dan 31. Akun aktor pertama sudah login di hook `before` (S-07). Search tidak dipakai pada Tab Transaction Role: section tiap sub-tab memuat baris Pre-setup #19 dan baris pola, tidak melebihi satu halaman.
- Langkah berulang (8b.7): langkah 8 sampai 14 diulang per baris tabel iterasi node dan sub-tab (2 node x 9 sub-tab = 18 kombinasi; langkah 10 sampai 14 diulang 18 kali, ekspansi spec 134 langkah, nominal 31). Alasan tetap satu spec: Expected a dan b TC-FA-RP-1180 mensyaratkan asersi pada setiap sub-tab di kedua node; TC tunggal, satu akun, satu client, satu pemicu Assign; parameter tiap iterasi ada di tabel `## Prerequisites` tanpa langkah bersyarat dan `Verifikasi` tetap satu per klausa. Memecahnya tidak mengurangi ekspansi.
- Urutan Expected a, b disusun mengikuti anchor absence (8b butir 2): `Verifikasi` tampil di section Asset Admin dan Approver ditulis lebih dulu, lalu `Verifikasi` baris lain di Monitoring & Report, baru `Verifikasi` tidak tampil.
- Pembagian TC lintas spec: TC-FA-RP-1179 (baris pola Group Role pada Assign Group Manager yang sama) ada di spec 346; TC-FA-RP-1181 (log per baris pola) ada di spec 349.
- Post Condition TC-FA-RP-1180 ("Dimas Pranata dipulihkan ke state Pre-setup #15 oleh automation baseline") tidak punya langkah observasi; tidak diasersi, dipulihkan di hook `after`.
- Temuan untuk QA:
  - Precondition d TC-FA-RP-1180 menyebut login pada `Client Addon On`; email dan password akun Total Control `Client Addon On` tidak tertulis di Pre-setup TC (disediakan tim FE). Pre-setup #15, #18, dan #19 diasumsikan tersedia pada client itu (preseden spec 318).
  - Expected d menulis baseline Pre-setup #19 "3 dan 3" yang berlaku tanpa seed Group Manager (Pre-setup #19); Fajar Nugroho (#5, Group Manager `IT Infrastructure`) menambah baris pola pada `Data Center` bila seed dimuat. Spec mengasumsikan seed Group Manager tidak dimuat selama spec (kemampuan fixture disediakan tim FE/BE); TC tidak menyatakan hal itu pada Precondition.
  - Expected a menulis "sebagai baris biasa" tanpa penanda UI yang membedakan baris pola dari baris manual; spec mengasersi tampil di section dan tidak menambah asersi penanda.
  - Expected d menulis "baris pola ikut hitungan header" sebagai penjelasan; spec mengasersi hanya angka header 4 dan 4.
  - Expected c menyebut "perhatikan keempat section" pada `Helpdesk` sub-tab `Disposal`; spec mengasersi tidak ada baris Dimas Pranata di keempat section (daftar disebut utuh) dengan anchor baris lain di Asset Admin.
  - Expected e tidak menyebut cara memeriksa Tab Total Control dan Tab Read Only; spec memakai Search nama sebagai langkah penghubung.
  - Sub-tab `Transfer` diasumsikan punya section Staff; sub-tab `Borrowing & Assignment`, `Damaged`, dan `Missing` tidak punya section Staff (TC-FA-RP-9) sehingga Expected b untuk Staff diasersi sebagai section yang tidak tampil (preseden spec 318).
