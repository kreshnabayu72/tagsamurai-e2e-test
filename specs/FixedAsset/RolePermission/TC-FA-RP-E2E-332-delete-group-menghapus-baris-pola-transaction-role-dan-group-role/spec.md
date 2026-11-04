---
id: TC-FA-RP-E2E-332-delete-group-menghapus-baris-pola-transaction-role-dan-group-role
title: "Delete Group menghapus baris pola Transaction Role dan Group Role pada node dan descendant dengan log Remove (Group Deleted) per baris"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1159
  - TC-FA-RP-1176
coverage:
  web: automated
---

# Delete Group menghapus baris pola Transaction Role dan Group Role pada node dan descendant dengan log Remove (Group Deleted) per baris

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Total Control kedua, Rina Wulandari | #3 | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC2_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Spec ini destruktif (Delete Group) dan dijalankan sesudah spec lain pada suite serial (`parallel: false`).
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group; `IT Infrastructure` menjadi induk Group sementara), #19 (baris pola Transaction Role), #3 (Rina Wulandari), #12 (Maya Anggraeni), #24 (`Company Changelog`, log 25 entri campuran; latar log, tidak diasersi), #39 (Detail Role `Manage files`, `All Groups` memuat 41 baris sebelum spec ini).
- Data Dinamis (bersuffix `{runId}` dan nomor spec 332): Subgroup induk `Hapus Pola Induk {runId}-332` di bawah `IT Infrastructure` dan Subgroup anak `Hapus Pola Anak {runId}-332` di bawah induk itu, tanpa aset aktif dan bukan tujuan Transfer atau Disposal (syarat fixture Pre-setup #18 agar guard Delete tidak menahan penghapusan). Keduanya dibuat spec ini sebagai pengganti `Data Center` dan `Rack A1` pada TC (target aksi hapus memakai data milik spec, S-06). Baris pola Transaction Role dan Group Role terbentuk saat Group dibuat (langkah 2 dan 3 adalah precondition, tidak diasersi).
- Kemampuan teknis: membaca jumlah notifikasi in-app Rina Wulandari dan Maya Anggraeni sebagai baseline (disediakan tim FE/BE, tanpa endpoint karangan); jendela absence notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau penghapusan berhasil penuh): bila Subgroup induk atau anak masih ada, keduanya dihapus lewat sesi API Total Control (kemampuan disediakan tim FE/BE). Pre-setup `Data Center` dan `Rack A1` tidak disentuh.
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### Persiapan Group sementara (precondition TC, tidak diasersi)

1. Buka Fixed Asset > Settings > Groups
2. Buat Subgroup induk `Hapus Pola Induk {runId}-332` di bawah `IT Infrastructure` lewat row action `Add Subgroup`
3. Buat Subgroup anak `Hapus Pola Anak {runId}-332` di bawah `Hapus Pola Induk {runId}-332` lewat row action `Add Subgroup`
4. Tunggu aksi selesai (kedua Subgroup tampil di pohon Group)
5. Catat jumlah notifikasi in-app Rina Wulandari dan Maya Anggraeni sebagai baseline lewat kemampuan baca

### TC-FA-RP-1159: Delete Group menghapus baris pola Transaction Role pada node dan descendant dengan log Remove (Group Deleted) per baris

6. Hapus group `Hapus Pola Induk {runId}-332` (beserta descendant `Hapus Pola Anak {runId}-332`) dan konfirmasi `Delete Group`
7. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
8. Verifikasi node `IT Infrastructure` tampil di Sidebar Group Tree
9. Verifikasi node `Hapus Pola Induk {runId}-332` dan `Hapus Pola Anak {runId}-332` tidak ada lagi di Sidebar Group Tree beserta baris pola
10. Klik ikon `[Changelog]` pada baris sub-tab `Disposal`
11. Verifikasi modal memuat tiga entri Action `Remove (Group Deleted)` dengan Field `Asset Admin — Hapus Pola Induk {runId}-332` dan Old Value masing-masing `Admin Utama`, `Siti Rahmawati`, dan `Rina Wulandari`
12. Verifikasi modal memuat tiga entri Action `Remove (Group Deleted)` dengan Field `Approver — Hapus Pola Induk {runId}-332` dan Old Value masing-masing `Admin Utama`, `Siti Rahmawati`, dan `Rina Wulandari`
13. Verifikasi modal memuat dua entri Action `Remove (Group Deleted)` dengan Field `Monitoring & Report — Hapus Pola Induk {runId}-332` dan Old Value masing-masing `Dewi Anggraini` dan `Maya Anggraeni`
14. Verifikasi seluruh entri pada langkah 11 sampai 13 memuat New Value `—`
15. Verifikasi modal memuat entri yang sama untuk `Hapus Pola Anak {runId}-332` (Field `Asset Admin`, `Approver`, dan `Monitoring & Report` dengan Old Value dan New Value `—` sama seperti induk)
16. Verifikasi entri tersebut terpisah per baris pola, bukan satu entri ringkasan
17. Tutup modal Changelog

### TC-FA-RP-1176: Delete Group menghapus baris pola Group Role Default User, Total Control, dan Read Only pada node dan descendant dengan log Remove (Group Deleted) per baris

18. Buka Fixed Asset > Settings > Role & Permission > Tab `System` > Detail Role Group Role `Manage files`, lalu klik `All Groups`
19. Verifikasi sedikitnya satu baris tampil pada tabel `All Groups`
20. Telusuri seluruh halaman Pagination tabel `All Groups`
21. Verifikasi tidak ada baris pada node `Hapus Pola Induk {runId}-332` dan `Hapus Pola Anak {runId}-332` (baris pola ikut terhapus)
22. Klik ikon Changelog di toolbar Detail Role
23. Verifikasi modal memuat lima entri Action `Remove (Group Deleted)` dengan Role Name — User — Group Name `Manage files — Admin Utama — Hapus Pola Induk {runId}-332`, `Manage files — Siti Rahmawati — Hapus Pola Induk {runId}-332`, `Manage files — Rina Wulandari — Hapus Pola Induk {runId}-332`, `Manage files — Dewi Anggraini — Hapus Pola Induk {runId}-332`, dan `Manage files — Maya Anggraeni — Hapus Pola Induk {runId}-332`
24. Verifikasi kelima entri tersebut memuat Field `Access`, Old Value `Assigned`, dan New Value `—`
25. Verifikasi modal memuat entri yang sama untuk `Hapus Pola Anak {runId}-332` (lima entri dengan Field `Access`, Old Value `Assigned`, New Value `—`)
26. Verifikasi entri tersebut terpisah per baris pola, bukan satu entri ringkasan
27. Tutup modal Changelog

### TC-FA-RP-1159 dan TC-FA-RP-1176: tidak ada notifikasi ke Rina Wulandari maupun Maya Anggraeni

28. Ganti akun: logout, lalu login sebagai Total Control kedua Rina Wulandari
29. Klik Bell icon
30. Verifikasi panel notifikasi tampil
31. Tunggu 5 detik tanpa memuat ulang halaman
32. Verifikasi jumlah notifikasi Rina Wulandari sama dengan baseline langkah 5 (tidak ada notifikasi akibat penghapusan Group)
33. Verifikasi jumlah notifikasi Maya Anggraeni sama dengan baseline langkah 5 lewat kemampuan baca

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah.
- Langkah penghubung (S-03): langkah 1 sampai 5 (pembentuk precondition dan baseline, S-12), langkah 7, 10, 17, 18, 20, 22, 27, 28, 29 (navigasi, membuka dan menutup modal, ganti akun), langkah 31 (jendela absence notifikasi, bagian 6). Langkah 8 dan 19 adalah pembanding positif (8b butir 2) untuk absence langkah 9 dan 21; langkah 30 adalah anchor positif tambahan untuk absence langkah 32 dan 33. Telusur halaman langkah 20 mendahului absence langkah 21 karena `All Groups` memuat lebih dari sepuluh baris (R-22).
- Langkah 6 menghapus satu pasang Group yang melayani kedua TC: langkah 1 TC-FA-RP-1159 dan TC-FA-RP-1176 identik (hapus group dengan descendant, konfirmasi `Delete Group`) dan precondition kedua TC sama (Pre-setup #18, #3, #12, #24). Dihapus sekali supaya aksi destruktif tidak diulang; langkah 7 sampai 17 adalah langkah 2 dan 3 TC-FA-RP-1159, langkah 18 sampai 27 adalah langkah 2 dan 3 TC-FA-RP-1176. Klausa notifikasi (Expected c kedua TC) dan langkah 4 kedua TC ("Login sbg Rina Wulandari lalu klik Bell icon" atau "Buka Notifikasi sebagai Rina Wulandari") dikerjakan sekali pada langkah 28 sampai 33.
- Entri Changelog dicari lewat nama Group bersuffix unik `{runId}-332` sehingga baseline entri nol (S-12); tidak ada asersi total entri.
- Pembagian TC lintas spec: TC-FA-RP-1157, 1158 ada di spec 330; TC-FA-RP-1174 ada di spec 345. Nomor cadangan 346 tidak dipakai (spec 33 langkah, di bawah smell sekitar 35 langkah).
- Spec ini destruktif (Delete Group) tetapi hanya menghapus Group milik spec; spec 054 dan spec lain yang memakai `Data Center` tidak terpengaruh.
- Temuan untuk QA:
  - TC-FA-RP-1159 dan 1176 menghapus `Data Center` (descendant `Rack A1`) dan Expected memakai nama itu. Spec memakai Group sementara bersuffix milik spec (S-06) sehingga teks Expected "Data Center" dan "Rack A1" ditulis dengan nama sementara itu; pemulihan "sesuai aturan pemulihan fixture destruktif pada Catatan" menjadi tidak perlu.
  - TC-FA-RP-1159 dan 1176 tumpang tindih (aksi hapus identik, surface log berbeda: Transaction Role dan Group Role). Dikerjakan dengan satu penghapusan dan dua surface pengamatan; mohon konfirmasi bahwa itu bukan duplikat yang seharusnya digabung di TC.
  - TC-FA-RP-1159 langkah 3 tidak menyebut node tempat ikon `[Changelog]` pada baris sub-tab `Disposal` dibuka (kedua node sudah terhapus); spec menulis langkah apa adanya.
  - TC-FA-RP-1159 Expected c menyebut notifikasi ke Rina Wulandari dan Maya Anggraeni, tetapi langkah 4 hanya membuka Notifikasi sebagai Rina Wulandari; akun Maya Anggraeni tidak punya env password di `suite.md`, sehingga spec membaca notifikasinya lewat kemampuan baca (langkah 33). Tidak ada anchor positif pengiriman notifikasi di TC; spec memakai panel notifikasi yang terbuka dan selisih terhadap baseline.
  - TC-FA-RP-1176 Expected a menyebut "tidak ada baris pada node"; node yang sudah dihapus tidak dapat dipilih di Sidebar Group Tree, sehingga spec mengasersi tidak ada baris dengan nama Group itu pada seluruh halaman `All Groups`.
  - Pre-setup #24 (`Company Changelog`) dan #39 belum disebut pada pernyataan Pre-setup bersama di `suite.md`; spec menganggap #24 latar log pada client default (seperti spec 054) dan pemulihan #39 dijamin tim FE/BE.
  - Post Condition kedua TC ("dipulihkan sesuai aturan pemulihan fixture destruktif") tidak punya langkah observasi dan tidak diasersi.
