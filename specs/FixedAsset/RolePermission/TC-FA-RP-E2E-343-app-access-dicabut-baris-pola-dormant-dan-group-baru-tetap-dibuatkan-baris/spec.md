---
id: TC-FA-RP-E2E-343-app-access-dicabut-baris-pola-dormant-dan-group-baru-tetap-dibuatkan-baris
title: App Access FAMS dicabut, baris pola dormant dan Group baru tetap dibuatkan baris
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1166
coverage:
  web: automated
---

# App Access FAMS dicabut, baris pola dormant dan Group baru tetap dibuatkan baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`. Target aksi: Total Control kedua (Pre-setup #3, Rina Wulandari), email `totalControlSecond_automated_{namaCompany}@qwertysystem.net`; Rina Wulandari tidak login di spec ini.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #18 (pohon Group, node `IT Infrastructure` sebagai induk Subgroup), #19 (baris pola Asset Admin dan Approver Admin Utama, Siti Rahmawati, dan Rina Wulandari pada setiap node dan sub-tab), #3 (Rina Wulandari).
- Data Dinamis (suffix memuat nomor spec, S-12): Subgroup `Pola Dormant {runId}-343` di bawah `IT Infrastructure` (Data Dinamis TC #10 `Pola Dormant {n}`), dibuat oleh langkah 7.
- Kemampuan teknis: pencabutan dan pemberian kembali App Access FAMS dikerjakan lewat UI Global Settings > User sesuai langkah TC. Kemampuan membaca jumlah entri Changelog `IT Infrastructure` sub-tab `Disposal` sebelum aksi (baseline, S-12), pemulihan App Access FAMS, dan penghapusan Subgroup disediakan tim FE/BE tanpa endpoint karangan.
- State lintas modul dan pemulihan (S-11): App Access FAMS Rina Wulandari dicabut oleh langkah 4 dan diberikan kembali oleh langkah 22. Hook `after` memulihkan App Access FAMS Rina Wulandari (state Pre-setup #3) lewat seeding API bila spec berhenti di antara langkah 4 dan 22, dan menghapus Subgroup `Pola Dormant {runId}-343` lewat API (data milik spec; S-06).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite". Suite berjalan serial (`parallel: false`).
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, disediakan tim FE).
- Env var yang dipakai: `FA_TC_PASSWORD` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1166: App Access FAMS dicabut dari user Total Control, baris pola dormant tetap ada, Group baru tetap dibuatkan baris, dan baris langsung berlaku saat App Access diberikan lagi

1. Catat baseline B2 (aksi tanpa `Verifikasi`): jumlah entri Changelog `IT Infrastructure` sub-tab `Disposal` lewat kemampuan baca
2. Buka Global Settings > User
3. Ketik Search `Rina Wulandari`, tekan Enter
4. Cabut App Access FAMS Rina Wulandari
5. Tunggu aksi selesai: App Access tersimpan
6. Buka Fixed Asset > Settings > Groups
7. Buat Subgroup `Pola Dormant {runId}-343` di bawah `IT Infrastructure` lewat row action `Add Subgroup`
8. Tunggu aksi selesai: Subgroup `Pola Dormant {runId}-343` muncul di pohon Group
9. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
10. Klik node `Pola Dormant {runId}-343` lalu klik sub-tab `Disposal`
11. Verifikasi baris pola Rina Wulandari ada di section Asset Admin pada node `Pola Dormant {runId}-343` walau App Access dicabut
12. Verifikasi baris pola Rina Wulandari ada di section Approver pada node `Pola Dormant {runId}-343` walau App Access dicabut
13. Klik node `IT Infrastructure` lalu klik sub-tab `Disposal`
14. Verifikasi baris pola Rina Wulandari tetap tersimpan dan tampil di section Asset Admin pada `IT Infrastructure`
15. Verifikasi baris pola Rina Wulandari tetap tersimpan dan tampil di section Approver pada `IT Infrastructure`
16. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
17. Verifikasi modal Changelog tampil dengan jumlah entri terbaca
18. Verifikasi jumlah entri Changelog sama dengan B2 (tidak ada entri `Remove` akibat pencabutan)
19. Tutup modal Changelog
20. Buka Global Settings > User
21. Ketik Search `Rina Wulandari`, tekan Enter
22. Berikan kembali App Access FAMS Rina Wulandari
23. Tunggu aksi selesai: App Access tersimpan
24. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
25. Klik node `Pola Dormant {runId}-343` lalu klik sub-tab `Disposal`
26. Verifikasi baris pola Rina Wulandari langsung berlaku di section Asset Admin pada node `Pola Dormant {runId}-343` tanpa pemulihan dan tanpa backfill
27. Verifikasi baris pola Rina Wulandari langsung berlaku di section Approver pada node `Pola Dormant {runId}-343` tanpa pemulihan dan tanpa backfill
28. Klik node `IT Infrastructure` lalu klik sub-tab `Disposal`
29. Verifikasi baris pola Rina Wulandari langsung berlaku di section Asset Admin pada `IT Infrastructure` tanpa pemulihan dan tanpa backfill
30. Verifikasi baris pola Rina Wulandari langsung berlaku di section Approver pada `IT Infrastructure` tanpa pemulihan dan tanpa backfill
31. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
32. Verifikasi modal Changelog tampil dengan jumlah entri terbaca
33. Verifikasi jumlah entri Changelog sama dengan B2 (tidak ada entri `Assign` baru)
34. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 34 langkah.
- TC-FA-RP-1156 (Deactivate user yang sama) ada di spec 328.
- Langkah penghubung (S-03): 1, 2, 3, 5, 6, 8, 9, 19, 20, 21, 23, 24, dan 34 (pencatatan baseline, pembukaan halaman, Search, "Tunggu aksi selesai", dan penutupan modal). Langkah 3 dan 21 adalah Search baris target (R-16, bagian 8b butir 9); Search dimulai ulang di tiap kunjungan Global Settings > User karena klik sidebar mereset Search. Section Asset Admin dan Approver pada tiap node memuat paling banyak enam baris (Pre-setup #19), sehingga baris Rina Wulandari berada di halaman pertama tanpa Search.
- Asersi jumlah (bukan kelas g): Expected b ("tidak ada entri `Remove`") dan Expected c ("tanpa entri `Assign` baru") diasersi sebagai selisih nol terhadap baseline B2 (S-12), dengan `Verifikasi` modal Changelog tampil dengan jumlah entri terbaca sebagai anchor (bagian 8b butir 2). B2 dibaca sekali sebelum pencabutan karena tidak ada aksi lain yang menulis ke Changelog itu di antara kedua pembacaan.
- Pada langkah 11, 12, 26, dan 27 node `Pola Dormant {runId}-343` dibuka sesudah dibuat (langkah 7), sehingga baris pola Rina Wulandari yang teramati adalah baris yang ditulis saat pembuatan Group.
- Subgroup tetap ada sampai hook `after` yang menghapusnya (Data Dinamis TC menyatakan "tetap ada sampai akhir sesi pengujian"; penghapusan di hook `after` adalah pembersihan data milik spec, S-06).
- Temuan untuk QA:
  - Expected c ("Rina kembali dihitung pada resolusi wewenang", "tanpa pemulihan", "tanpa backfill") tidak menyebut cara mengamati resolusi wewenang di UI; spec mengasersi baris pola tampil pada kedua node (langkah 26, 27, 29, 30) dan tidak ada entri `Assign` baru (langkah 33). Tidak ada langkah pemulihan di antara pemberian App Access dan pengamatan.
  - Langkah 4 dan 6 TC ("buka Changelog sub-tab `Disposal`", "buka kembali Changelog") tidak menyebut node mana yang dibaca; spec memakai `IT Infrastructure` sesuai langkah 4 TC. Pembuatan Subgroup (langkah 7) mungkin juga menulis entri pada Changelog `IT Infrastructure`; TC tidak menyatakannya, dan jika terjadi, baseline B2 (dicatat sebelum pencabutan) perlu dicatat ulang sesudah langkah 8.
  - TC tidak merinci form Create Subgroup (field wajib selain Name) maupun batas panjang Name dengan suffix `{runId}-343`; spec memakai row action `Add Subgroup` seperti spec 129 dan nama bersuffix untuk keunikan per run (S-12).
  - Kolom Post Condition menyebut Rina Wulandari dipulihkan oleh automation baseline dan Group `Pola Dormant {n}` tetap ada sampai akhir sesi; tidak ada langkah observasi di TC sehingga tidak diasersi. Pemulihan dikerjakan langkah 22 dan hook `after`.
