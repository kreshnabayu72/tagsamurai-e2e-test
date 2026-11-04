---
id: TC-FA-RP-E2E-329-sub-tab-addon-tanpa-dan-dengan-lisensi-baris-pola-tidak-dihitung
title: Sub-tab Addon tanpa dan dengan lisensi, baris pola tidak dihitung
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1161
  - TC-FA-RP-1162
coverage:
  web: automated
---

# Sub-tab Addon tanpa dan dengan lisensi, baris pola tidak dihitung

## Prerequisites

- Mode: FE+BE.
- Akun (akun disediakan tim FE; email tidak tertulis di Pre-setup TC): Total Control pada `Client Addon Off` (Pre-setup #31; lisensi Addon Audit, Maintenance, dan Tracking tidak aktif saat spec dimulai), password `Spectra.env.FA_ADDON_OFF_TC_PASSWORD`. Seluruh langkah spec ini berjalan pada satu client (`Client Addon Off`) dan tidak ada ganti akun; lisensi Addon Audit diaktifkan oleh langkah 9.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: #31 (`Client Addon Off`), #12 (Maya Anggraeni, target Read Only), #18 (pohon Group, node `IT Infrastructure`). Dibaca oleh Expected TC-FA-RP-1162 dan tidak diubah: baris pola Asset Admin dan Approver Admin Utama (#1), Siti Rahmawati (#2), dan Rina Wulandari (#3) pada `IT Infrastructure` sub-tab `Audit` (digambarkan di Pre-setup #19 dan #3).
- Precondition TC-FA-RP-1161 yang di-seed di hook `before` (dipakai sebagai precondition TC, tidak diasersi): seed API menambahkan baris menyimpang Staff pada sub-tab `Audit` untuk Maya Anggraeni (Read Only). Kemampuan seed disediakan tim FE/BE tanpa endpoint karangan.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): (a) fixture BE untuk mengaktifkan dan menonaktifkan lisensi Addon Audit pada `Client Addon Off`; (b) seeding API untuk menghapus baris menyimpang Maya Anggraeni; (c) pembacaan jumlah entri Changelog `IT Infrastructure` sub-tab `Audit` sebelum aksi (baseline, S-12).
- State lintas modul dan pemulihan (S-11, R-08): lisensi Addon Audit pada `Client Addon Off` diaktifkan oleh langkah 9. Hook `after` menonaktifkan kembali lisensi Addon Audit sehingga `Client Addon Off` kembali seperti Pre-setup #31 (dipakai juga spec 134), dan menghapus baris menyimpang Staff Maya Anggraeni bila masih ada, sehingga Maya Anggraeni kembali ke state Pre-setup #12.
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, disediakan tim FE). Spec tidak membuat data Dinamis.
- Env var yang dipakai: `FA_ADDON_OFF_TC_PASSWORD` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1161: Addon tak berlisensi, baris pola tetap ada tetapi tidak dihitung dalam pola tier

1. Buka Tab Transaction Role
2. Klik node `IT Infrastructure` lalu klik sub-tab `Audit`
3. Verifikasi sub-tab `Audit` menampilkan banner `This feature requires the Audit add-on. Upgrade your license to use it.`
4. Verifikasi sub-tab `Audit` tidak menampilkan data penugasan
5. Buka Tab Read Only
6. Verifikasi Maya Anggraeni tetap tampil di Tab Read Only (baris sub-tab Addon tak berlisensi tidak dihitung dalam pola, `FARP-LOGIC-14g`)
7. Hapus baris menyimpang Staff Maya Anggraeni pada sub-tab `Audit` lewat seeding API hingga tersimpan

### TC-FA-RP-1162: Lisensi Addon aktif kembali, baris pola langsung dihitung tanpa backfill

8. Catat baseline B (aksi tanpa `Verifikasi`): jumlah entri Changelog `IT Infrastructure` sub-tab `Audit` lewat kemampuan baca
9. Aktifkan lisensi Addon Audit pada `Client Addon Off` lewat fixture BE hingga tersimpan
10. Muat ulang halaman (F5)
11. Buka Tab Transaction Role
12. Klik node `IT Infrastructure` lalu klik sub-tab `Audit`
13. Verifikasi kartu Approval Rule dan section role tampil normal pada sub-tab `Audit`
14. Verifikasi banner `This feature requires the Audit add-on. Upgrade your license to use it.` tidak tampil
15. Verifikasi section Asset Admin memuat baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari tanpa backfill
16. Verifikasi section Approver memuat baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari tanpa backfill
17. Klik ikon `[Changelog]` di baris sub-tab `Audit`
18. Verifikasi modal Changelog tampil dengan jumlah entri terbaca
19. Verifikasi jumlah entri Changelog sama dengan B (tidak ada entri `Assign` baru akibat aktivasi lisensi)
20. Tutup modal Changelog
21. Klik `[⋯]` baris Approver Rina Wulandari
22. Klik `Remove`
23. Verifikasi dialog auto-revert `D-04` tampil (baris sudah dihitung)
24. Klik `[Cancel]`

## Notes

- Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 24 langkah.
- Satu kelas harness ringan (state tenant, lisensi): 1161 membutuhkan client tanpa lisensi dan 1162 mengaktifkannya pada client yang sama; keduanya berurutan dalam satu spec karena 1162 membutuhkan client yang sama dalam keadaan lisensi nonaktif sebelum diaktifkan. Pemulihan lisensi di hook `after`.
- Urutan TC tidak berubah. Baris menyimpang Maya Anggraeni dihapus pada langkah 7 sebelum aktivasi supaya Precondition TC-FA-RP-1162 (Pre-setup #31 dan #18, tanpa baris menyimpang) terpenuhi dan efek aktivasi pada tier user yang barisnya menyimpang, yang tidak ditetapkan PRD, tidak ikut teramati.
- Langkah penghubung (S-03): 1, 5 (pembukaan tab), 7, 8, 10, 11, 20, dan 24 (seeding, baseline, muat ulang, penutupan modal, dan pembatalan dialog). Langkah 10 dan 11 membuka ulang halaman sesudah aktivasi supaya status lisensi terbaca ulang. Langkah 24 membatalkan Remove sehingga baris Approver Rina Wulandari tidak berubah.
- Asersi absence langkah 4 dan 14 memiliki anchor positif pada surface yang sama: banner pada langkah 3, dan kartu Approval Rule serta section role pada langkah 13 (bagian 8b butir 2, R-21 untuk langkah 14 sesudah F5).
- Asersi jumlah (bukan kelas g): langkah 19 mengasersi selisih nol terhadap baseline B (S-12), dengan modal Changelog tampil (langkah 18) sebagai anchor. Ekspektasi "tanpa backfill" pada langkah 15 dan 16 teramati lewat langkah 19.
- Baris Maya Anggraeni (Tab Read Only, empat baris) dan section role (paling banyak enam baris, Pre-setup #19) berada di halaman pertama, sehingga langkah 6, 15, 16, dan 21 tidak memakai Search (R-23).
- Teks banner pada langkah 3 dan 14 identik dengan banner sub-tab `Audit` di spec 134 (`This feature requires the Audit add-on. Upgrade your license to use it.`, pola `This feature requires the [Addon Name] add-on. Upgrade your license to use it.`). Spec 134 juga mengasersi CTA `[View License]`; TC-FA-RP-1161 tidak menyebut CTA sehingga spec ini tidak mengasersinya.
- Temuan untuk QA:
  - TC-FA-RP-1162 langkah 1 (aktivasi lisensi Addon Audit) tidak menyebut apakah state lisensi bersifat global atau per client uji, siapa pelaku aktivasi, dan apakah halaman perlu dimuat ulang. Spec mengasumsikan aktivasi pada `Client Addon Off` lewat fixture BE (disediakan tim FE/BE) lalu memuat ulang halaman (langkah 10). Asumsi ini perlu konfirmasi QA.
  - Precondition TC-FA-RP-1162 hanya menyebut Pre-setup #31 dan #18, sedangkan Expected menyebut baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari yang berasal dari Pre-setup #19 dan #3.
  - Post Condition TC-FA-RP-1161 ("Data baris Addon tetap tersimpan, field `license_status` pada API") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Post Condition TC-FA-RP-1162 menyatakan efek aktivasi lisensi pada tier user yang barisnya menyimpang tidak ditetapkan PRD (Gap Spec); spec tidak mengujinya. Post Condition yang sama menyebut Rina Wulandari dipulihkan ke Pre-setup #3 tanpa menyatakan apakah Remove dikonfirmasi; spec berhenti pada dialog auto-revert dan memilih `[Cancel]` (langkah 24), sehingga tidak ada state yang perlu dipulihkan.
  - TC-FA-RP-1162 Expected c menyebut dialog auto-revert `D-04` tanpa judul, isi, dan tombolnya; spec mengasersi kemunculannya saja dan tombol `[Cancel]` diasumsikan ada (seperti dialog `D-04` pada spec 112).
  - Precondition d TC-FA-RP-1161 tidak menyebut node untuk baris menyimpang Staff pada sub-tab `Audit`; spec men-seed pada node `IT Infrastructure`, sesuai langkah 1 TC.
  - Seluruh TC memakai `Client Addon Off` (Pre-setup #31); email akun Total Control client itu tidak tertulis di Pre-setup TC dan disediakan tim FE.
