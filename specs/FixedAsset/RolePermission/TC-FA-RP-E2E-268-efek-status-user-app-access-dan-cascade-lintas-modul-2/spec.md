---
id: TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2
title: "Efek status user, App Access, dan cascade lintas modul (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-907
  - TC-FA-RP-908
  - TC-FA-RP-909
  - TC-FA-RP-910
  - TC-FA-RP-912
  - TC-FA-RP-1102
  - TC-FA-RP-1103
coverage:
  web: automated
---

# Efek status user, App Access, dan cascade lintas modul (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso sebagai Standard; Ahmad Fauzi Total Control di FAMS dan di Admin Console untuk TC-FA-RP-907), #18 (pohon group Company Alpha), #36 (Tab Total Control terisi), #37 (Tab Read Only terisi; Read Only untuk TC-FA-RP-908) dan #22 (Custom Field aktif Company Alpha: `Cost Center`, `Joined Date`, `Badge No`).
- Data Dinamis: Subgroup `Tree Fresh {runId}-268` (TC-FA-RP-912), dibuat spec di bawah `IT Infrastructure` dan dihapus lewat seeding API di hook `after`.
- Kemampuan teknis: penambahan satu Global Role baru ke katalog (setara rilis aplikasi; TC-FA-RP-908 berlabel `Manual Only — (c)`) disediakan tim FE/BE; pemulihan Custom Field `Cost Center` (dinonaktifkan lalu diaktifkan kembali di langkah TC) dan `Joined Date` (dihapus pada TC-FA-RP-1103) lewat seeding API di hook `after` (Catatan TC "Pemulihan fixture destruktif").
- Baseline audit trail (S-12): jumlah entri Changelog Detail Role dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (TC-FA-RP-908).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-907: Remove Total Control di FAMS tidak mengubah tingkat akses di produk lain

1. Klik `[⋯]` baris Ahmad Fauzi di Tab Total Control lalu `Remove`, klik `[Remove]`
2. Tunggu aksi selesai: dialog tertutup
3. Buka Admin Console > Settings > Role & Permission > Tab Total Control
4. Verifikasi Ahmad Fauzi tetap Total Control di Admin Console

### TC-FA-RP-909: Post Condition Assign mencantumkan modul terdampak; perilaku modul konsumen diuji di modul pemilik

5. Buka Tab System, lalu Detail Role `Manage asset & TAG` dan pilih node `Data Center`
6. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]` (Assign Budi Santoso ke Group Role `Manage asset & TAG` di `Data Center`)
7. Tunggu aksi selesai: popup tertutup
8. Verifikasi baris Budi Santoso tampil di Detail Role `Manage asset & TAG` pada node `Data Center`
9. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Group Role
10. Verifikasi baris Budi Santoso `Manage asset & TAG` tampil di Tab Role Settings > User

### TC-FA-RP-910: Changelog: User milik target menampilkan cascade Global Role tetapi aggregate tidak

11. Catat baseline (aksi tanpa `Verifikasi`): Settings > User > Detail Ahmad Fauzi > Changelog: User, jumlah entri aggregate
12. Buka Tab Read Only
13. Klik `[+ Assign]` di Tab Read Only, centang Ahmad Fauzi, klik `[Assign]` (Assign Read Only ke Ahmad Fauzi)
14. Tunggu aksi selesai: popup tertutup
15. Buka Settings > User > Detail Ahmad Fauzi > Changelog: User (aggregate)
16. Verifikasi aggregate memuat satu baris baru `Access Level` `—` ke `Read Only` (selisih satu terhadap baseline)
17. Verifikasi aggregate tidak memuat baris cascade per role (tidak ada entri baru Action `Assign (via Read Only)`)

### TC-FA-RP-908: Role baru di katalog muncul di Tab System dan diisi otomatis untuk Default User, Total Control, dan Read Only (backfill)

18. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri pada Changelog Detail Role role baru dan kolom Users baris role baru sesudah rilis, serta tambahkan satu Global Role baru ke katalog lewat kemampuan rilis aplikasi yang disediakan tim FE/BE
19. Buka Fixed Asset > Settings > Role & Permission > Tab System
20. Verifikasi role baru tampil di section Global Role tanpa migrasi manual
21. Buka Detail Role role baru
22. Verifikasi Admin Utama dan user Total Control memiliki baris dengan CRUD penuh sesuai kolom berlaku
23. Verifikasi user Read Only memiliki baris dengan Read saja
24. Verifikasi backfill tidak memicu auto-revert (seluruh user Total Control tetap ada di Tab Total Control)
25. Verifikasi backfill ikut dihitung di kolom Users baris role baru
26. Klik ikon Changelog di toolbar Detail Role
27. Verifikasi jumlah entri Changelog Detail Role role baru sama dengan baseline (backfill tidak dicatat per role)

### TC-FA-RP-912: Group yang baru dibuat langsung muncul di Sidebar Group Tree dan pemilih group

28. Buat Subgroup `Tree Fresh {runId}-268` di bawah `IT Infrastructure` di Settings > Groups
29. Tunggu aksi selesai: Subgroup tersimpan
30. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage files`
31. Verifikasi node `Tree Fresh {runId}-268` tampil di Sidebar Group Tree
32. Klik `[+ Assign]` lalu buka field Group
33. Verifikasi `Tree Fresh {runId}-268` dapat dipilih pada field Group tanpa assign ulang cakupan ancestor
34. Tutup popup lewat `✕`

### TC-FA-RP-1102: Custom Field aktif yang dinonaktifkan hilang dari kolom curated dan field Filter lalu muncul kembali saat diaktifkan

35. Buka Global Settings > Custom Field lalu nonaktifkan field `Cost Center`
36. Tunggu aksi selesai: field nonaktif tersimpan
37. Buka Fixed Asset > Settings > Role & Permission > Tab Total Control lalu buka popup Setup Column
38. Verifikasi daftar Setup Column tidak memuat `Cost Center`
39. Tutup popup Setup Column lewat `✕`, lalu klik ikon Filter
40. Verifikasi Filter Panel tidak memuat field `Cost Center`
41. Tutup Filter Panel
42. Aktifkan kembali field `Cost Center` di Global Settings > Custom Field
43. Tunggu aksi selesai: field aktif tersimpan
44. Muat ulang Tab Total Control lalu buka popup Setup Column
45. Verifikasi `Cost Center` tersedia kembali di Setup Column
46. Tutup popup Setup Column lewat `✕`, lalu klik ikon Filter
47. Verifikasi `Cost Center` tersedia kembali di Filter Panel
48. Tutup Filter Panel

### TC-FA-RP-1103: Custom Field aktif yang dihapus hilang permanen dari kolom curated dan field Filter

49. Buka Global Settings > Custom Field lalu hapus field `Joined Date`
50. Tunggu aksi selesai: field terhapus
51. Buka Fixed Asset > Settings > Role & Permission > Tab Total Control lalu buka popup Setup Column
52. Verifikasi daftar Setup Column tidak memuat `Joined Date`
53. Tutup popup Setup Column lewat `✕`, lalu klik ikon Filter
54. Verifikasi Filter Panel tidak memuat field `Joined Date`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 54 langkah.
- Urutan blok: TC-FA-RP-907, 909, 910, 908, 912, 1102, lalu TC-FA-RP-1103 (menghapus Custom Field) terakhir (S-10).
- Langkah penghubung (S-03): pencatatan baseline, pembukaan tab dan Detail Role, penutupan popup dan Filter Panel, "Tunggu aksi selesai", dan muat ulang Tab Total Control. Asersi "tidak ada/tidak memuat" didahului Verifikasi baris pengguna lain atau elemen lain yang tampil sebagai anchor (bagian 8b butir 2).
- TC-FA-RP-909 Expected b (efek pada modul asset, asset-registration, tag, license, dan approvals dimiliki TC modul pemilik) bukan asersi di Settings > Role & Permission dan tidak diasersi (NC-11).
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama (sinkronisasi atau efek lintas modul), tiap blok berdiri sendiri dan punya Expected sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - TC-FA-RP-908 berlabel `Manual Only — (c)` (penambahan role katalog hanya lewat rilis aplikasi); spec ditulis sebagai kemampuan yang disediakan tim FE/BE dan tidak menyebut role baru tertentu. Expected c TC-FA-RP-908 tidak menyebut cara menghitung kolom Users; spec membandingkannya dengan baseline.
  - TC-FA-RP-1102 dan 1103 tidak menyebut cara mengaktifkan, menonaktifkan, atau menghapus Custom Field di Global Settings > Custom Field selain langkah TC; spec memakai langkah TC apa adanya. Nama Custom Field Pre-setup #22 bersifat literal.
  - TC-FA-RP-907 sampai 910 dan 912 tidak punya detail copy toast sesudah aksi; tidak diasersi. TC-FA-RP-1103 Post Condition menunjuk Catatan TC (pemulihan) dan ditangani hook `after`; Post Condition TC-FA-RP-908 dan 909 tidak punya langkah observasi sehingga tidak diasersi (TC-FA-RP-909 Post Condition mencantumkan modul terdampak).
