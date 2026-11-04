---
id: TC-FA-RP-E2E-330-group-baru-subgroup-level-one-dan-import-menulis-baris-pola
title: "Group baru (Subgroup, level 1, dan hasil Import) menulis baris pola Transaction Role Total Control dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1157
  - TC-FA-RP-1158
coverage:
  web: automated
---

# Group baru (Subgroup, level 1, dan hasil Import) menulis baris pola Transaction Role Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Addon On` (Pre-setup #31; ketiga lisensi Addon Audit, Maintenance, dan Tracking aktif, sehingga kesembilan sub-tab tampil), email disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.FA_ADDON_ON_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group; `IT Infrastructure` menjadi induk Subgroup), #3 (Rina Wulandari, Total Control kedua), #12 (Maya Anggraeni, Read Only), #15 (pool pengguna Standard), #31 (`Client Addon On`). Baris pola yang diharapkan: Admin Utama, Siti Rahmawati, dan Rina Wulandari (Total Control) untuk Asset Admin dan Approver; Dewi Anggraini dan Maya Anggraeni (Read Only) untuk Monitoring & Report.
- Data Dinamis (bersuffix `{runId}` dan nomor spec 330): Subgroup `Pola Create {runId}-330` di bawah `IT Infrastructure`, Group level 1 `Pola Root {runId}-330`, Group hasil Import `Pola Import {runId}-330`. Berkas Import `Fixture.fixedAssetRolePermission.berkasImportGroupPola` (belum ada; disediakan tim FE) memuat satu Group level 1 bernama `Pola Import {runId}-330`.
- Pemulihan (hook `after`, tidak berasumsi pembuatan berhasil penuh): ketiga Group dinamis dihapus lewat sesi API Total Control (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Tabel Data Uji Dinamis TC menulis ketiga Group "tetap ada sampai akhir sesi"; spec ini menghapusnya di hook `after` supaya tidak menumpang run lain (S-06).
- Env var yang dipakai: `FA_ADDON_ON_TC_PASSWORD`, `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

Node baru yang ditelusuri pada langkah 9 sampai 14:

| Node baru |
|---|
| `Pola Create {runId}-330` |
| `Pola Root {runId}-330` |

Sub-tab Transaction Role yang ditelusuri pada tiap node baru:

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

### TC-FA-RP-1157: Create Group level 1 dan Subgroup, baris pola TC/RO terbentuk untuk semua Jenis Transaksi dan TC/RO tidak ter-auto-revert

1. Buka Fixed Asset > Settings > Groups
2. Buat Subgroup `Pola Create {runId}-330` di bawah `IT Infrastructure` lewat row action `Add Subgroup`
3. Buat Group level 1 `Pola Root {runId}-330`
4. Verifikasi `Pola Create {runId}-330` dan `Pola Root {runId}-330` tampil di pohon Group
5. Verifikasi tidak ada dialog auto-revert yang tampil
6. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
7. Klik node `Pola Create {runId}-330` pada Sidebar Group Tree
8. Verifikasi section Asset Admin memuat baris pola Admin Utama sejak pembukaan pertama node, tanpa jeda tanpa baris
9. Untuk setiap baris tabel "Node baru": klik node pada Sidebar Group Tree (langkah 10 sampai 14 diulang untuk setiap baris tabel "Sub-tab" pada node itu)
10. Klik sub-tab pada tabel "Sub-tab"
11. Verifikasi section Asset Admin memuat Admin Utama, Siti Rahmawati, dan Rina Wulandari pada sub-tab dan node itu
12. Verifikasi section Approver memuat Admin Utama, Siti Rahmawati, dan Rina Wulandari pada sub-tab dan node itu
13. Verifikasi section Monitoring & Report memuat Dewi Anggraini dan Maya Anggraeni pada sub-tab dan node itu
14. Verifikasi section Staff tidak memuat baris pola (Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, dan Maya Anggraeni tidak tampil) pada sub-tab dan node itu
15. Klik Tab `Total Control`
16. Verifikasi Rina Wulandari tampil di Tab Total Control
17. Klik Tab `Read Only`
18. Verifikasi Maya Anggraeni tampil di Tab Read Only

### TC-FA-RP-1158: Group hasil Import, baris pola TC/RO terbentuk, tanpa penugasan Standard

19. Buka Fixed Asset > Settings > Groups
20. Import Group `Pola Import {runId}-330` lewat Import di Settings > Groups dengan berkas Import `Fixture.fixedAssetRolePermission.berkasImportGroupPola`
21. Verifikasi `Pola Import {runId}-330` tampil di pohon Group
22. Buka Fixed Asset > Settings > Role & Permission, klik Tab `Transaction Role`, lalu klik node `Pola Import {runId}-330`
23. Klik sub-tab `Disposal`
24. Verifikasi section Asset Admin memuat baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari
25. Verifikasi section Approver memuat baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari
26. Verifikasi section Monitoring & Report memuat Dewi Anggraini dan Maya Anggraeni
27. Verifikasi tidak ada penugasan Standard (mis. Nadia Putri) pada node `Pola Import {runId}-330` (tanpa pewarisan)
28. Klik Tab `Total Control`
29. Verifikasi Siti Rahmawati dan Rina Wulandari tampil di Tab Total Control
30. Klik Tab `Read Only`
31. Verifikasi Dewi Anggraini dan Maya Anggraeni tampil di Tab Read Only

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Langkah penghubung (S-03): langkah 1, 6, 7, 9, 10, 15, 17, 19, 22, 23, 28, dan 30 (navigasi, penelusuran node dan sub-tab; tanpa `Verifikasi`). Langkah 4 dan 21 adalah asersi tambahan di luar TC yang menjadi anchor positif bahwa pembuatan Group sudah diproses (8b butir 2) untuk asersi absence langkah 5 dan 14; langkah 11 sampai 13 menjadi pembanding positif untuk absence langkah 14, dan langkah 24 sampai 26 untuk absence langkah 27. Akun aktor pertama sudah login di hook `before` (S-07).
- Penelusuran sembilan sub-tab pada dua node memakai idiom "Untuk setiap baris tabel" (8b butir 7): langkah 10 sampai 14 diulang 18 kali, sehingga ekspansi spec sekitar 117 langkah, di atas smell sekitar 35 langkah (nominal 31). Alasan mempertahankannya dalam satu spec: Expected a TC-FA-RP-1157 mensyaratkan setiap node baru pada setiap dari sembilan sub-tab, kedua TC satu topik (baris pola pada Group baru) dengan akun, client, dan dataset yang sama, parameter tiap iterasi ada di tabel Prerequisites tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa; memecahnya tidak mengurangi ekspansi.
- Urutan klausa TC-FA-RP-1157: Expected c ("tidak ada dialog auto-revert") ditaruh pada langkah 5, tepat sesudah pemicu pembuatan Group dan anchor langkah 4, karena dialog adalah state sementara (8b butir 5 dan 11); klausa Rina Wulandari tetap di Tab Total Control dan Maya Anggraeni tetap di Tab Read Only ada pada langkah 16 dan 18.
- Pembagian TC lintas spec: TC-FA-RP-1174 (baris pola yang sama pada Detail Role Group Role, Changelog Detail Role, dan notifikasi) ada di spec 345 dengan Group dinamis miliknya sendiri; spec ini hanya mengamati surface Transaction Role.
- Search tidak dipakai pada Tab Total Control dan Tab Read Only karena masing-masing memuat tidak lebih dari satu halaman (Pre-setup #36 dan #37).
- Temuan untuk QA:
  - Tidak ada klausa Expected TC yang membedakan "Siti Rahmawati" sebagai aktor dari baris pola Siti Rahmawati pada node baru; spec mengikuti TC (Siti Rahmawati termasuk baris pola Asset Admin dan Approver).
  - TC-FA-RP-1157 mensyaratkan login pada `Client Addon On` (Pre-setup #31) tanpa email dan tanpa rincian pengguna di client itu; TC-FA-RP-1158 tidak menyebut client. Spec memakai `Client Addon On` untuk keduanya (sub-tab `Disposal` ada di semua client) dan mengasumsikan pool pengguna Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, dan Maya Anggraeni sama dengan Company Alpha. Mohon konfirmasi.
  - TC-FA-RP-1157 tidak menyebut label aksi pembuatan Group level 1; spec menulis "Buat Group level 1" tanpa label tombol. Aksi `Add Subgroup` mengikuti spec 129.
  - TC-FA-RP-1157 Expected b ("baris pola terbentuk dalam transaksi pembuatan Group yang sama, tanpa jeda tanpa baris") tidak dapat diamati sebagai atomisitas transaksi lewat UI; spec mengasersi baris pola sudah ada pada pembukaan pertama node (langkah 8).
  - TC-FA-RP-1157 Expected c tidak menyebut judul atau teks dialog auto-revert; spec mengasersi "tidak ada dialog auto-revert" tanpa teks.
  - TC-FA-RP-1158 langkah 3 menyebut Nadia Putri sebagai contoh penugasan Standard, padahal Nadia Putri adalah seed Pre-setup #19 yang tidak dirujuk precondition TC (precondition memakai #18, #3, #12, #15). Spec menulis contoh itu apa adanya pada langkah 27.
  - Format berkas Import dan langkah dialog Import (pemetaan kolom, konfirmasi) tidak dirinci TC; spec menulis satu langkah "Import ... dengan berkas Import" dan berkasnya disediakan tim FE.
  - Tabel Data Uji Dinamis TC memakai `{n}` untuk nama Group; spec memakai suffix `{runId}-330` agar unik per run (S-12). TC-FA-RP-1157 dan 1158 tidak punya Post Condition dengan langkah observasi.
  - Pre-setup bersama di `suite.md` belum menyebut Pre-setup #31 (client `Client Addon On`) dan #39; akunnya hanya tercatat di bagian "Env password akun aktor".
  - TC-FA-RP-1174 (spec 345) tumpang tindih dengan TC-FA-RP-1157 dan 1158: precondition d TC-FA-RP-1174 memakai Group dari kedua TC ini. Ditempatkan terpisah per surface dan tidak digabung; mohon konfirmasi bahwa ini bukan duplikat yang seharusnya digabung di TC.
