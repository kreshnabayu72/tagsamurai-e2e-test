---
id: TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1
title: "Efek status user, App Access, dan cascade lintas modul (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-900
  - TC-FA-RP-901
  - TC-FA-RP-902
  - TC-FA-RP-904
  - TC-FA-RP-905
  - TC-FA-RP-906
coverage:
  web: automated
---

# Efek status user, App Access, dan cascade lintas modul (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Akun ganti (TC-FA-RP-901 dan 902): Total Control pada `Company Isolated` (Pre-setup #35). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso sebagai Standard), #18 (pohon group Company Alpha), #19 (seed Role Transaksi Disposal pada `IT Infrastructure`; Pandu Wijaya sebagai Approver), #36 (Tab Total Control terisi; Budi Santoso Total Control), #39 (Detail Role `Manage Open API` dan `Manage files` terisi; Budi Santoso), #43 (Kevin Susanto Group Manager di `Data Center`), dan #35 (`Company Isolated`: Pandu Wijaya sebagai Approver pada `Disposal` di `IT Infrastructure`; `Helpdesk` tanpa Group Manager aktif).
- Kondisi awal TC-FA-RP-905 yang di-seed: Budi Santoso memegang Total Control dan Asset Admin di `IT Infrastructure` (sub-tab `Disposal`), tanpa Group Manager. Kondisi awal TC-FA-RP-901 dan 902 di `Company Isolated`: Kevin Susanto ditugaskan sebagai satu-satunya Group Manager `Helpdesk` lalu dinonaktifkan (901); toggle `Require Approval for Disposal` ON di `IT Infrastructure` dengan satu Approver Pandu Wijaya yang kemudian dinonaktifkan (902).
- Kemampuan teknis: pengubahan Status pengguna, pencabutan dan pemulihan App Access FAMS, dan penghapusan identitas dikerjakan lewat UI Global Settings > User sesuai langkah TC; pemulihan memakai seeding API (Catatan TC "Pemulihan fixture destruktif"). Hook `after`: Status Budi Santoso, App Access Pandu Wijaya, identitas Budi Santoso beserta penugasannya, dan Ahmad Fauzi dipulihkan ke Tabel Pre-setup TC.
- Baseline audit trail (S-12): jumlah entri Changelog Tab Total Control dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (TC-FA-RP-905).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD` dan `FA_ISOLATED_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-900: User dinonaktifkan: baris penugasan tetap tersimpan dan tampil di Detail Role dan tab

1. Catat baseline (aksi tanpa `Verifikasi`): nilai CRUD baris Budi Santoso pada Detail Role `Manage Open API`
2. Nonaktifkan Status Budi Santoso di Settings > User
3. Tunggu aksi selesai: Status tersimpan
4. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage Open API`
5. Verifikasi baris Budi Santoso tetap tampil di Detail Role dengan Status `Inactive`
6. Verifikasi nilai CRUD baris Budi Santoso sama dengan baseline (penugasan tidak dihapus)
7. Buka Tab Total Control
8. Verifikasi baris Budi Santoso tetap tampil di Tab Total Control dengan Status `Inactive`
9. Aktifkan kembali Status Budi Santoso lewat seeding API hingga tersimpan

### TC-FA-RP-906: Assign Total Control di FAMS tidak memengaruhi tingkat akses di produk lain

10. Klik `[+ Assign]` di Tab Total Control, centang Ahmad Fauzi, klik `[Assign]` (Assign Total Control ke Ahmad Fauzi di FAMS)
11. Tunggu aksi selesai: popup tertutup
12. Buka Admin Console > Settings > Role & Permission > Tab Total Control
13. Verifikasi sedikitnya satu baris pengguna lain tampil di Tab Total Control Admin Console
14. Verifikasi Ahmad Fauzi tidak tampil di Tab Total Control Admin Console
15. Buka Global Settings > Role > Tab Total Control
16. Verifikasi sedikitnya satu baris pengguna lain tampil di Tab Total Control Global Settings
17. Verifikasi Ahmad Fauzi tidak tampil di Tab Total Control Global Settings

### TC-FA-RP-904: App Access FAMS dicabut: penugasan dormant dan user keluar dari resolusi; pemulihan mengembalikannya

18. Cabut App Access FAMS Pandu Wijaya di Global Settings > User
19. Tunggu aksi selesai: App Access tersimpan
20. Buka Tab Transaction Role pada node `IT Infrastructure` sub-tab `Disposal`
21. Verifikasi baris Pandu Wijaya tetap tersimpan dan tampil di section Approver saat App Access dicabut
22. Klik node `Data Center` lalu sub-tab `Disposal`, aktifkan toggle `Require Approval for Disposal`
23. Verifikasi dialog `Cannot Require Approval` tampil dan toggle kembali OFF (Pandu Wijaya tidak dihitung pada resolusi approver)
24. Pulihkan App Access FAMS Pandu Wijaya di Global Settings > User
25. Tunggu aksi selesai: App Access tersimpan
26. Buka Tab Transaction Role, klik node `Data Center` lalu sub-tab `Disposal`, aktifkan toggle `Require Approval for Disposal`
27. Verifikasi toggle `Require Approval for Disposal` tetap ON tanpa dialog `Cannot Require Approval` (wewenang lama Pandu Wijaya kembali)

### TC-FA-RP-905: Identitas user dihapus permanen: seluruh baris FAMS dihapus cascade tanpa entri log per role

28. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri pada Changelog Tab Total Control
29. Hapus identitas Budi Santoso di Global Settings > User
30. Tunggu aksi selesai: identitas terhapus
31. Buka Tab Total Control
32. Verifikasi sedikitnya satu baris pengguna lain tampil di Tab Total Control
33. Verifikasi Budi Santoso tidak ada di Tab Total Control
34. Buka Tab Transaction Role, klik node `IT Infrastructure` lalu sub-tab `Disposal`
35. Verifikasi sedikitnya satu baris pengguna lain tampil di Tab Transaction Role
36. Verifikasi Budi Santoso tidak ada di Tab Transaction Role
37. Buka Tab Total Control, lalu klik ikon Changelog di toolbar Tab Total Control
38. Verifikasi modal Changelog Tab Total Control tampil dengan jumlah entri yang terbaca
39. Verifikasi jumlah entri Changelog Tab Total Control sama dengan baseline (tidak ada entri log per role untuk penghapusan cascade)

### TC-FA-RP-901: Group Manager nonaktif tidak dihitung pada prasyarat aktivasi toggle

40. Ganti akun: logout lalu login sebagai Total Control pada `Company Isolated` (Pre-setup #35; akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`)
41. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
42. Klik node `Helpdesk` lalu sub-tab `Disposal`
43. Aktifkan toggle `Require Approval for Disposal`
44. Verifikasi dialog `Cannot Require Approval` tampil
45. Verifikasi toggle `Require Approval for Disposal` kembali OFF

### TC-FA-RP-902: Approver nonaktif setelah toggle ON: toggle tetap ON dengan Total Control sebagai fallback

46. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
47. Verifikasi toggle `Require Approval for Disposal` tetap ON
48. Verifikasi baris Pandu Wijaya tetap tampil di section Approver

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 48 langkah.
- Urutan blok: TC-FA-RP-900, 906, 904, 905 pada Company Alpha (TC-FA-RP-905 menghapus identitas pengguna sehingga paling akhir di Company Alpha), lalu ganti akun ke Total Control `Company Isolated` untuk TC-FA-RP-901 dan 902. Ganti akun memakai Step eksplisit (S-07); hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (S-03): pencatatan baseline, pembukaan tab dan Detail Role, pemulihan lewat seeding API, dan "Tunggu aksi selesai". Asersi "tidak ada/tidak tampil" didahului Verifikasi baris pengguna lain pada surface yang sama sebagai anchor (bagian 8b butir 2).
- `P-1` (state berat) untuk TC-FA-RP-905: Expected b ("tidak ada entri log per role untuk penghapusan cascade") bergantung pada penghapusan identitas pengguna yang baru dibangun langkah sebelumnya (cascade seluruh baris FAMS); asersi absence tetap di spec ini dengan baseline jumlah entri (S-05, S-12) dan anchor modal Changelog tampil. Aksi nyata di spec asal; bukan di spec absence.
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama (sinkronisasi atau efek lintas modul), tiap blok berdiri sendiri dan punya Expected sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - Akun login Total Control `Company Isolated` (TC-FA-RP-901 dan 902) tidak tertulis di Pre-setup TC. TC-FA-RP-901 dan 902 juga tidak menyebut cara menonaktifkan Kevin Susanto dan Pandu Wijaya selain keterangan precondition; spec men-seed kondisi itu.
  - TC-FA-RP-904 Expected b ("prasyarat toggle di node lain yang bergantung padanya gagal") tidak menyebut node mana; spec memakai node `Data Center` sub-tab `Disposal` dengan asumsi bahwa prasyaratnya bergantung pada Approver Pandu Wijaya di `IT Infrastructure` (Pre-setup #19 dan #43). Expected c ("wewenang lama kembali") ditulis sebagai toggle yang sama kini berhasil ON tanpa dialog `Cannot Require Approval`. Asumsi ini perlu konfirmasi QA.
  - TC-FA-RP-900 Expected b ("Penugasan tidak dihapus") tumpang tindih dengan Expected a; spec mengasersinya sebagai nilai CRUD baris yang sama dengan baseline. TC-FA-RP-906 tidak menyebut URL Admin Console dan Global Settings; spec memakai jalur menu dari TC.
  - Post Condition kosong pada TC-FA-RP-900 sampai 906.
