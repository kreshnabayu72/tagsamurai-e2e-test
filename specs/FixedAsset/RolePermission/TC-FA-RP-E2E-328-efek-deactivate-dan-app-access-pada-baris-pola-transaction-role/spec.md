---
id: TC-FA-RP-E2E-328-efek-deactivate-dan-app-access-pada-baris-pola-transaction-role
title: Efek Deactivate user Total Control pada baris pola Transaction Role
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1156
coverage:
  web: automated
---

# Efek Deactivate user Total Control pada baris pola Transaction Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`. Target aksi: Total Control kedua (Pre-setup #3, Rina Wulandari), email `totalControlSecond_automated_{namaCompany}@qwertysystem.net`; Rina Wulandari tidak login di spec ini.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #18 (pohon Group, node `IT Infrastructure`), #19 (baris pola Asset Admin dan Approver Admin Utama, Siti Rahmawati, dan Rina Wulandari pada setiap node dan sub-tab, termasuk `IT Infrastructure` sub-tab `Disposal`), #3 (Rina Wulandari). Spec tidak membuat data Dinamis.
- Kemampuan teknis: Toggle Active dikerjakan lewat UI Fixed Asset > Settings > User sesuai langkah TC. Kemampuan membaca jumlah entri Changelog `IT Infrastructure` sub-tab `Disposal` sebelum aksi (baseline, S-12) disediakan tim FE/BE tanpa endpoint karangan.
- State lintas modul dan pemulihan (S-11): Status Rina Wulandari (Active) diubah dan dipulihkan oleh langkah 14. Hook `after` memastikan Rina Wulandari kembali Active dan ke state Pre-setup #3 lewat seeding API (kemampuan disediakan tim FE/BE; Catatan TC "Pemulihan fixture destruktif") bila spec berhenti di antara langkah 4 dan 14.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite". Suite berjalan serial (`parallel: false`).
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, disediakan tim FE).
- Env var yang dipakai: `FA_TC_PASSWORD` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1156: Deactivate user Total Control, baris pola Transaction Role tersimpan dan tampil kembali setelah Activate

1. Catat baseline B1 (aksi tanpa `Verifikasi`): jumlah entri Changelog `IT Infrastructure` sub-tab `Disposal` lewat kemampuan baca
2. Buka Fixed Asset > Settings > User
3. Ketik Search `Rina Wulandari`, tekan Enter
4. Nonaktifkan Rina Wulandari lewat Toggle Active
5. Tunggu aksi selesai: Status Rina Wulandari tersimpan
6. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
7. Klik node `IT Infrastructure` lalu klik sub-tab `Disposal`
8. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
9. Verifikasi modal Changelog tampil dengan jumlah entri terbaca
10. Verifikasi jumlah entri Changelog sama dengan B1 (tidak ada entri `Remove` baris pola akibat Deactivate)
11. Tutup modal Changelog
12. Buka Fixed Asset > Settings > User
13. Ketik Search `Rina Wulandari`, tekan Enter
14. Aktifkan kembali Rina Wulandari lewat Toggle Active
15. Tunggu aksi selesai: Status Rina Wulandari tersimpan
16. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
17. Klik node `IT Infrastructure` lalu klik sub-tab `Disposal`
18. Verifikasi baris pola Rina Wulandari tampil kembali di section Asset Admin tanpa Assign ulang
19. Verifikasi baris pola Rina Wulandari tampil kembali di section Approver tanpa Assign ulang
20. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
21. Verifikasi modal Changelog tampil dengan jumlah entri terbaca
22. Verifikasi jumlah entri Changelog sama dengan B1 (tidak ada entri `Assign` baru)
23. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 23 langkah.
- Langkah penghubung (S-03): 1, 2, 3, 5, 6, 11, 12, 13, 15, 16, dan 23 (pencatatan baseline, pembukaan halaman, Search, "Tunggu aksi selesai", dan penutupan modal). Langkah 3 dan 13 adalah Search baris target (R-16, bagian 8b butir 9); Search dimulai ulang di tiap kunjungan Settings > User karena klik sidebar mereset Search. Section Asset Admin dan Approver pada `IT Infrastructure` sub-tab `Disposal` masing-masing memuat paling banyak enam baris (Pre-setup #19), sehingga baris Rina Wulandari pada langkah 18 dan 19 berada di halaman pertama tanpa Search.
- Asersi jumlah (bukan kelas g): Expected a ("tidak ada entri `Remove`") dan Expected b ("tanpa entri `Assign` baru") diasersi sebagai selisih nol terhadap baseline B1 (S-12), dengan `Verifikasi` modal Changelog tampil dengan jumlah entri terbaca sebagai anchor (bagian 8b butir 2). B1 dibaca sekali sebelum Deactivate dan dipakai untuk kedua pembacaan karena tidak ada aksi lain yang menulis ke Changelog itu di antaranya.
- TC-FA-RP-1166 (App Access FAMS dicabut dari user yang sama) ada di spec 343.
- Temuan untuk QA:
  - TC-FA-RP-1156 langkah 2 menyebut "lihat Changelog" tanpa menyebut node dan sub-tab Changelog yang dimaksud; spec memakai Changelog sub-tab `Disposal` pada `IT Infrastructure` sesuai langkah yang sama.
  - Judul TC menyebut baris pola "tersimpan dan tampil kembali", tetapi Expected tidak menyatakan apakah baris tampil atau hilang selama Rina Wulandari nonaktif; spec hanya mengasersi keadaan sesudah Activate (S-02, tidak menambah asersi).
  - TC tidak menyebut apakah Deactivate dan Activate di Settings > User meminta dialog konfirmasi; spec tidak menulis langkah konfirmasi. Jika dialog muncul, langkah 4 dan 14 perlu ditambah.
  - Expected b "tanpa Assign ulang" adalah keterangan proses, bukan keadaan UI; spec mengasersinya lewat jumlah entri Changelog tanpa entri `Assign` baru.
  - Kolom Post Condition menyebut Rina Wulandari dipulihkan "oleh automation baseline"; tidak ada langkah observasi di TC sehingga tidak diasersi. Pemulihan Status dikerjakan langkah 14 dan hook `after`.
