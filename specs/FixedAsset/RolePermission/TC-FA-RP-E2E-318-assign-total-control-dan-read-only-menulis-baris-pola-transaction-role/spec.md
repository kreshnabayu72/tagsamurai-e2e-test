---
id: TC-FA-RP-E2E-318-assign-total-control-dan-read-only-menulis-baris-pola-transaction-role
title: "Assign Total Control dan Read Only menulis baris pola Transaction Role pada semua Jenis Transaksi × Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1145
  - TC-FA-RP-1146
coverage:
  web: automated
---

# Assign Total Control dan Read Only menulis baris pola Transaction Role pada semua Jenis Transaksi × Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Addon On` (Pre-setup #31; lisensi Addon Audit, Maintenance, Tracking aktif), email tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), password `Spectra.env.FA_ADDON_ON_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup pada `Client Addon On`: #15 (kolam pengguna Standard; Ahmad Fauzi dipakai sebagai target kedua TC, di-seed berstatus Standard tanpa penugasan Transaction Role sebagai precondition TC, tidak diasersi), #18 (pohon group dengan tujuh node) dan #31 (`Client Addon On`).
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

- Tabel iterasi node Sidebar Group Tree (tujuh node Pre-setup #18; urutan baris = urutan iterasi): `Head Office`, `IT Infrastructure`, `Data Center`, `Rack A1`, `Helpdesk`, `Logistics Warehouse`, `Dock 1`.
- Seeding dan pemulihan: kondisi Precondition (Ahmad Fauzi berstatus Standard tanpa penugasan Transaction Role) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Ahmad Fauzi dan baris pola dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Env var yang dipakai: `FA_ADDON_ON_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1145: Assign Total Control: baris pola Transaction Role (Asset Admin dan Approver) terbentuk pada semua Jenis Transaksi × Group

1. Klik Tab `Transaction Role`
2. Untuk setiap baris tabel iterasi sub-tab (langkah 2 sampai 4): klik sub-tab pada baris tabel
3. Untuk setiap baris tabel iterasi node (langkah 3 sampai 4): klik node pada baris tabel di Sidebar Group Tree
4. Catat jumlah header section Asset Admin dan Approver sebagai baseline untuk kombinasi sub-tab dan node itu
5. Klik Tab `Total Control`
6. Klik `[+ Assign]` di Tab Total Control
7. Centang Ahmad Fauzi
8. Klik `[Assign]`
9. Verifikasi muncul satu toast sukses: `Success, Total Control has been assigned.`
10. Klik Tab `Transaction Role`
11. Untuk setiap baris tabel iterasi sub-tab (langkah 11 sampai 19): klik sub-tab pada baris tabel
12. Untuk setiap baris tabel iterasi node (langkah 12 sampai 19): klik node pada baris tabel di Sidebar Group Tree
13. Verifikasi Ahmad Fauzi tampil di section Asset Admin
14. Verifikasi Ahmad Fauzi tampil di section Approver
15. Verifikasi header jumlah section Asset Admin bertambah satu dari baseline langkah 4
16. Verifikasi header jumlah section Approver bertambah satu dari baseline langkah 4
17. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report
18. Verifikasi Ahmad Fauzi tidak tampil di section Monitoring & Report
19. Verifikasi Ahmad Fauzi tidak tampil di section Staff (pada sub-tab tanpa section Staff menurut tabel iterasi, section itu sendiri tidak tampil)

### TC-FA-RP-1146: Assign Read Only: baris pola Monitoring & Report terbentuk tanpa Approver pada semua Jenis Transaksi × Group

20. Pulihkan Ahmad Fauzi ke status Standard tanpa penugasan Transaction Role lewat seeding API
21. Klik Tab `Read Only`
22. Klik `[+ Assign]` di Tab Read Only
23. Centang Ahmad Fauzi
24. Klik `[Assign]`
25. Verifikasi muncul satu toast sukses: `Success, Read Only has been assigned.`
26. Klik Tab `Transaction Role`
27. Untuk setiap baris tabel iterasi sub-tab (langkah 27 sampai 31): klik sub-tab pada baris tabel
28. Untuk setiap baris tabel iterasi node (langkah 28 sampai 31): klik node pada baris tabel di Sidebar Group Tree
29. Verifikasi Ahmad Fauzi tampil di section Monitoring & Report
30. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin
31. Verifikasi Ahmad Fauzi tidak tampil di section Asset Admin, Staff, dan Approver (pada sub-tab tanpa section Staff menurut tabel iterasi, section itu sendiri tidak tampil)
32. Klik `[+ Assign]` pada section Approver di sub-tab dan node terakhir iterasi langkah 27 dan 28 (`Maintenance Routine`, `Dock 1`)
33. Ketik Search `Ahmad Fauzi` pada popup Assign Approver, tekan Enter
34. Verifikasi popup Assign Approver tidak memuat Ahmad Fauzi (empty state `No results found`; Read Only tidak eligible sebagai Approver)
35. Klik `[Cancel]` untuk menutup popup Assign Approver

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 35 langkah.
- Pembagian TC lintas spec: TC-FA-RP-1147 (peran tangga lama) ada di spec `TC-FA-RP-E2E-337-assign-total-control-ke-user-standard-pemegang-peran-tangga-lama` karena berjalan pada akun Total Control Company Alpha (bukan `Client Addon On`) dan memuat asersi Changelog.
- Langkah penghubung (S-03): langkah 1 sampai 4 (pencatatan baseline header), 5, 10, 20, 21 dan 26 (pindah tab), 35 (menutup popup). Akun aktor pertama sudah login di hook `before` (S-07). Langkah 20 adalah pemulihan state lewat seeding API tanpa `Verifikasi` (S-09).
- Langkah berulang (8b.7): langkah 2 sampai 4, 11 sampai 19, dan 27 sampai 31 diulang per baris tabel iterasi sub-tab dan per baris tabel iterasi node. Parameter tiap iterasi ada di `## Prerequisites`. Langkah 32 sampai 35 dijalankan pada kombinasi terakhir iterasi (`Maintenance Routine`, `Dock 1`) karena TC menyebut "salah satu node".
- Urutan Expected pada TC-FA-RP-1145 dan 1146 disusun mengikuti state dan anchor absence (8b.2): `Verifikasi` tampil di section yang memuat Ahmad Fauzi ditulis lebih dulu, lalu `Verifikasi` sedikitnya satu baris lain di section yang sama atau yang berdekatan, baru `Verifikasi` tidak tampil.
- Alasan ukuran spec (35 langkah nominal, tetapi langkah efektif jauh di atas sekitar 35 karena ekspansi 9 sub-tab × 7 node = 63 kombinasi): Expected TC-FA-RP-1145 dan 1146 mensyaratkan asersi pada setiap sub-tab dan setiap node, sehingga mengurangi kombinasi berarti mengurangi cakupan Expected. Kedua blok berkelas fungsional, memakai akun, client, permukaan, dan tabel iterasi yang sama, dan hanya berbeda pada tingkat akses yang di-Assign; dipisah menjadi dua spec hanya menggandakan login `Client Addon On`, hook, dan tabel iterasi yang sama. Parameter iterasi ditulis di tabel `## Prerequisites` tanpa langkah bersyarat.
- Post Condition TC-FA-RP-1145 (log `Assign` per baris pola, lihat TC-FA-RP-1163; baris pola Group Role Ahmad Fauzi ikut dibentuk, lihat TC-FA-RP-1169) dan TC-FA-RP-1146 (log `Assign` per baris pola, lihat TC-FA-RP-1163) tidak punya langkah observasi di TC; tidak diasersi di spec ini. Baris pola Group Role Ahmad Fauzi diasersi untuk Budi Setiawan di spec `TC-FA-RP-E2E-319-assign-total-control-dan-read-only-menulis-baris-pola-group-role`.
- Temuan untuk QA:
  - TC-FA-RP-1145 dan 1146 Precondition menyebut Pre-setup #15, #18, dan #31 tetapi tidak menyatakan Ahmad Fauzi berstatus Standard tanpa penugasan Transaction Role, padahal Pre-setup #40 mencantumkan Ahmad Fauzi sebagai Asset Admin manual di `Disposal` `IT Infrastructure`. Bila penugasan itu ada, baris pola menggantikan baris manual (lihat TC-FA-RP-1147) sehingga header Asset Admin pada kombinasi itu tidak bertambah satu. Spec mengasumsikan seed Standard tanpa penugasan (aturan seed pool Pre-setup #32) dan header bertambah satu pada setiap kombinasi.
  - TC-FA-RP-1145 Expected c menyebut Ahmad Fauzi tidak tampil di section Staff pada setiap dari sembilan sub-tab, sedangkan `Borrowing & Assignment`, `Damaged`, dan `Missing` tidak punya section Staff (TC-FA-RP-9); spec mengasersi section itu sendiri tidak tampil pada tiga sub-tab tersebut. Sub-tab `Transfer` diasumsikan punya section Staff (Precondition TC-FA-RP-1147 menyebut Staff `Transfer`).
  - Kedua TC dijalankan pada `Client Addon On` (Precondition d) sehingga Pre-setup #15 dan #18 diasumsikan tersedia pada client itu; email dan password akun Total Control `Client Addon On` tidak tertulis di Pre-setup TC (disediakan tim FE).
  - TC-FA-RP-1146 langkah 4 hanya menyebut "salah satu node" dan "cari Ahmad Fauzi" pada picker tanpa menyebut sub-tab; spec memakai kombinasi terakhir iterasi dan Search di popup Assign Approver.
  - TC-FA-RP-1145 dan 1146 Expected "setiap dari tujuh node" mengikuti Pre-setup #18; tidak ada daftar node di TC, sehingga tabel iterasi node di `## Prerequisites` mengikuti pohon Pre-setup #18.
