---
id: TC-GS-ROLE-E2E-112-pencatatan-log-switch-active-remove-assign-auto-revert-dan-permintaan-sama
title: "Pencatatan Log Switch Active: Remove dan Auto-Revert Terpisah, Remove/Assign tanpa Activate/Deactivate, dan Permintaan Sama Berulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-329
  - TC-GS-ROLE-330
  - TC-GS-ROLE-338
coverage:
  web: automated
---

# Pencatatan Log Switch Active: Remove dan Auto-Revert Terpisah, Remove/Assign tanpa Activate/Deactivate, dan Permintaan Sama Berulang

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah access level dan baris role user Pre-setup bersama.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Akun penerima notifikasi: Cakra Mahendra (Pre-setup #20), email dan kredensial disediakan tim FE (Tabel Pre-setup TC tidak memuat email; lihat Temuan untuk QA). Login ke akun ini terjadi pada langkah ganti akun di Test Steps; hook `after` memulihkan sesi ke akun default suite.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; Access Global Settings dicentang pada kedua user): `Cakra Mahendra` (Active; Total Control dengan keenam baris Active CRUD penuh) untuk TC-329 dan `Hanif Pradipta` (Active; baris `Manage TAG` Active dengan Read dan Update tercentang) untuk TC-330 dan TC-338. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): kedua user dipastikan berada di state di atas. Mekanisme menyiapkan access level dan baris role per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Klien HTTP (TC-338): klien HTTP yang mengirim permintaan langsung ke server dengan sesi Ahmad Fauzi (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi di langkah itu hanya respons server dan state data (bagian 8b butir 1).
- Baseline (dicatat di hook `before` sesudah Given dan sebelum aksi pemicu pertama, S-12; kemampuan membaca total entri tiap surface disediakan tim FE):
  - `Cakra Mahendra`: total entri Changelog Detail `Manage TAG` hasil Search nama sebagai `C-DM`; Changelog Tab `Total Control` sebagai `C-TC`; Changelog Tab System sebagai `C-SY`; Changelog: User > Role sebagai `C-UR`; System Log Ahmad Fauzi hasil Filter Name sebagai `C-SL`; Activity Log hasil Search nama sebagai `C-AL`; jumlah notifikasi Overlay Notifikasi berjudul `Your Total Control access was removed` sebagai `C-NT`.
  - `Hanif Pradipta`: total entri Changelog Detail `Manage TAG` sebagai `H-DM`; Changelog Tab System sebagai `H-SY`; Changelog: User > Role sebagai `H-UR`; System Log Ahmad Fauzi hasil Filter Name sebagai `H-SL`; Activity Log hasil Search nama sebagai `H-AL`.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): `Cakra Mahendra` di-assign Total Control ulang dengan keenam baris Active CRUD penuh; baris `Manage TAG` `Hanif Pradipta` dikembalikan Active dengan Read dan Update tercentang; sesi dipulihkan ke akun default suite. Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log dan notifikasi bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif (berlaku untuk `[Date]` pada body notifikasi). Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-329: Switch Active OFF pada user Total Control mencatat Remove dan Auto-Revert terpisah

1. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Cakra Mahendra`, tekan Enter
2. Klik Name `Cakra Mahendra`, buka Tab `Role`
3. Matikan switch `Manage TAG`
4. Klik `[Remove]` pada dialog
5. Tunggu aksi selesai
6. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`
7. Klik `Changelog`, ketik Search `Cakra Mahendra`, tekan Enter
8. Verifikasi total entri sama dengan `C-DM` + 1
9. Verifikasi entry baru: Action `Remove`, Role — User `Manage TAG — Cakra Mahendra`, Field `Access`, Old `Assigned`, New `—`, Modified By `Ahmad F`
10. Tutup modal Changelog
11. Buka Tab `Total Control`, klik `Changelog`, ketik Search `Cakra Mahendra`, tekan Enter
12. Verifikasi total entri sama dengan `C-TC` + 1
13. Verifikasi entry baru: Action `Auto-Revert`, User Name `Cakra Mahendra`, Field `Access Level`, Old `Total Control`, New `—`, Modified By `Ahmad F`
14. Verifikasi tidak ada entry Action `Edit` untuk `Cakra Mahendra` (satu-satunya entry baru adalah `Auto-Revert` pada langkah 13)
15. Tutup modal Changelog
16. Buka Tab System, klik `Changelog`, ketik Search `Cakra Mahendra`, tekan Enter
17. Verifikasi total entri sama dengan `C-SY` + 1
18. Verifikasi satu-satunya entry baru adalah Action `Remove` untuk `Manage TAG — Cakra Mahendra` (tidak ada entry untuk lima role lain milik `Cakra Mahendra`)
19. Tutup modal Changelog
20. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
21. Buka Filter Panel, klik `[Clear Field]`, pilih Name `Cakra Mahendra`, klik `[Apply]`
22. Verifikasi total hasil Filter sama dengan `C-SL` + 2
23. Verifikasi entry System Log: Action `Remove`, Object `System Role`, Name `Cakra Mahendra`, Field `Manage TAG`, Old `Assigned`, New `—`
24. Verifikasi entry System Log: Action `Auto-Revert`, Object `Total Control`, Name `Cakra Mahendra`, Field `Access Level`, Old `Total Control`, New `—`
25. Buka Global Settings > Activity Log, ketik Search `Cakra Mahendra`, tekan Enter
26. Verifikasi total hasil Search sama dengan `C-AL` + 2
27. Verifikasi baris Activity Log: Action `Remove`, Object `System Role`, Name `Cakra Mahendra`, Field `Manage TAG`, Old `Assigned`, New `—`
28. Verifikasi baris Activity Log: Action `Auto-Revert`, Object `Total Control`, Name `Cakra Mahendra`, Field `Access Level`, Old `Total Control`, New `—`
29. Buka Global Settings > User > Cakra Mahendra > Changelog: User > Role
30. Verifikasi total entri sama dengan `C-UR` + 1
31. Verifikasi entry baru Action `Remove` untuk `Manage TAG`
32. Verifikasi Changelog: User > Role tidak memuat entry Action `Auto-Revert` baru (satu-satunya entry baru adalah `Remove` pada langkah 31)

### TC-GS-ROLE-330: Switch Active OFF dan ON mencatat Remove dan Assign tanpa Activate/Deactivate dan tanpa Edit

33. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Hanif Pradipta`, tekan Enter
34. Klik Name `Hanif Pradipta`, buka Tab `Role`
35. Matikan switch `Manage TAG`
36. Nyalakan switch `Manage TAG`
37. Tunggu aksi selesai
38. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`
39. Klik `Changelog`, ketik Search `Hanif Pradipta`, tekan Enter
40. Verifikasi total entri sama dengan `H-DM` + 2 (tepat 1 entry per toggle)
41. Verifikasi entry Action `Remove`: Role — User `Manage TAG — Hanif Pradipta`, Field `Access`, Old `Assigned`, New `—`, Modified By `Ahmad F`
42. Verifikasi entry Action `Assign`: Role — User `Manage TAG — Hanif Pradipta`, Field `Access`, Old `—`, New `Assigned`, Modified By `Ahmad F`
43. Verifikasi tidak ada entry Action `Activate`, `Deactivate`, atau `Edit` untuk `Hanif Pradipta`
44. Tutup modal Changelog
45. Buka Tab System, klik `Changelog`, ketik Search `Hanif Pradipta`, tekan Enter
46. Verifikasi total entri sama dengan `H-SY` + 2 (tepat 1 entry per toggle)
47. Verifikasi kedua entry yang sama tampil: Action `Remove` dan Action `Assign` untuk `Manage TAG — Hanif Pradipta`, Field `Access`
48. Verifikasi tidak ada entry Action `Activate`, `Deactivate`, atau `Edit` untuk `Hanif Pradipta`
49. Tutup modal Changelog
50. Buka Global Settings > User > Hanif Pradipta > Changelog: User > Role
51. Verifikasi total entri sama dengan `H-UR` + 2 (tepat 1 entry per toggle)
52. Verifikasi entry Action `Remove` dan entry Action `Assign` untuk `Manage TAG`, Field `Access`
53. Verifikasi tidak ada entry Action `Activate`, `Deactivate`, atau `Edit` untuk `Hanif Pradipta`
54. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
55. Buka Filter Panel, klik `[Clear Field]`, pilih Name `Hanif Pradipta`, klik `[Apply]`
56. Verifikasi total hasil Filter sama dengan `H-SL` + 2 (tepat 1 entry per toggle)
57. Verifikasi entry System Log: Action `Remove`, Object `System Role`, Name `Hanif Pradipta`, Field `Manage TAG`
58. Verifikasi entry System Log: Action `Assign`, Object `System Role`, Name `Hanif Pradipta`, Field `Manage TAG`
59. Verifikasi tidak ada entry Action `Activate`, `Deactivate`, atau `Edit` untuk `Hanif Pradipta` di System Log
60. Buka Global Settings > Activity Log, ketik Search `Hanif Pradipta`, tekan Enter
61. Verifikasi total hasil Search sama dengan `H-AL` + 2 (tepat 1 entry per toggle)
62. Verifikasi baris Activity Log: Action `Remove`, Object `System Role`, Name `Hanif Pradipta`, Field `Manage TAG`
63. Verifikasi baris Activity Log: Action `Assign`, Object `System Role`, Name `Hanif Pradipta`, Field `Manage TAG`
64. Verifikasi tidak ada baris Action `Activate`, `Deactivate`, atau `Edit` untuk `Hanif Pradipta` di Activity Log

### TC-GS-ROLE-338: Permintaan switch ke posisi yang sudah sama selesai sukses tanpa efek dan tanpa entry log

65. Kirim dua permintaan identik berurutan cepat lewat klien HTTP dengan sesi Ahmad Fauzi: matikan switch Active `Manage TAG` untuk `Hanif Pradipta`
66. Verifikasi kedua respons sukses (permintaan kedua tanpa efek tambahan)
67. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`
68. Klik `Changelog`, ketik Search `Hanif Pradipta`, tekan Enter
69. Verifikasi total entri sama dengan `H-DM` + 3
70. Verifikasi entry baru hanya 1 dengan Action `Remove` untuk `Hanif Pradipta` (tidak ada entry baru dari permintaan kedua)
71. Tutup modal Changelog
72. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Hanif Pradipta`, tekan Enter
73. Klik Name `Hanif Pradipta`, buka Tab `Role`
74. Verifikasi switch `Manage TAG` OFF
75. Verifikasi nilai tersimpan baris `Manage TAG`: Read dan Update tetap checked

### TC-GS-ROLE-329 (lanjutan): notifikasi Cakra Mahendra

76. Ganti akun: Logout dari akun Ahmad Fauzi, login sebagai `Cakra Mahendra`
77. Buka Overlay Notifikasi
78. Verifikasi jumlah notifikasi berjudul `Your Total Control access was removed` sama dengan `C-NT` + 1
79. Verifikasi notifikasi baru: Title `Your Total Control access was removed`, Body `Your Total Control access was automatically removed after Ahmad Fauzi changed your role permissions on [Date].`
80. Verifikasi notifikasi baru hanya memiliki tombol `[Mark as Read]`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: pencatatan (presence); TC-338 memakai permintaan langsung ke server sebagai objek uji ringan kelas a (maksimum satu TC; `P-5` butir b, dan K-1 di bawah). Subjudul `###` memetakan langkah ke id TC granular.
- `P-5` (butir b): TC-GS-ROLE-338 adalah satu TC objek-uji ringan kelas a (dua permintaan identik tanpa harness eksternal dan tanpa state berat sendiri) pada permukaan yang sama dengan blok pencatatan (Changelog Detail `Manage TAG` untuk `Hanif Pradipta`).
- K-1 (bagian 2 konvensi): TC-GS-ROLE-338 adalah TC kelas a dengan Expected respons API (kedua respons sukses, state data) yang tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-role-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC sumber diubah dari 329, 330, 338 menjadi blok 329 tanpa notifikasi, 330, 338, lalu notifikasi 329, supaya ganti akun ke `Cakra Mahendra` terjadi sekali di akhir.
- Spec melewati sekitar 35 langkah (80 langkah) karena ketiga blok satu topik (pencatatan Switch Active, membaca surface Changelog, System Log, dan Activity Log yang sama setelah pemicu yang berurutan) dan 330 dan 338 memakai user `Hanif Pradipta` yang sama dengan state berurutan (TC-338 memakai total entri sesudah TC-330); sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`) yang tidak dihitung pada ambang (bagian 3 Smell).
- Entri log dikenali lewat total entri terhadap baseline dan kombinasi kolom Action, Field, dan Name pada hasil Search atau Filter Name, bukan lewat posisi baris (S-12): entry berpasangan yang dibuat berurutan dalam hitungan detik berketelitian menit sama. Urutan "Remove lalu Assign" (Expected a TC-330) tidak diasersi lewat posisi baris. Pada Tab System Log, Filter Name dipakai sebagai pengganti Search nama karena placeholder Search tab itu tidak mencantumkan kolom Name; Activity Log memakai Search nama.
- Search dan Filter untuk menemukan user atau entri target ditulis sebagai langkah penghubung (R-16): langkah 1, 7, 11, 16, 21, 25, 33, 39, 45, 55, 60, 68, 72. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Tab `Role`, tab, Detail, Changelog, Tab System Log, dan Overlay Notifikasi (langkah 2, 6, 20, 29, 34, 38, 50, 54, 67, 77), menutup modal Changelog (langkah 10, 15, 19, 44, 49, 71), serta langkah "Tunggu aksi selesai" (langkah 5 dan 37).
- Klausa Expected c TC-329 ("tidak ada entry untuk lima role lain" dan "tidak ada entry Edit") adalah scope exclusion dengan anchor positif dan baseline sendiri (bagian 3 prinsip 13g), bukan asersi absence kelas g: entry `Remove` dan `Auto-Revert` tampil dan total entri dibandingkan dengan baseline (langkah 12 sampai 14 dan 17 sampai 18). Klausa Expected e TC-330 ("tidak ada Activate/Deactivate/Edit") diperlakukan sama pada langkah 43, 48, 53, 59, dan 64.
- Klausa TC-338 Expected b "hanya memuat 1 entry Remove" dibaca sebagai hanya 1 entry Remove baru untuk permintaan identik (langkah 69 dan 70), karena Changelog yang sama sudah memuat entry TC-330.
- Pemicu OFF `Cakra Mahendra` (langkah 1 sampai 4) menyalin langkah 1 sampai 4 TC-GS-ROLE-326 (S-04). Pemicu OFF lalu ON `Hanif Pradipta` (langkah 33 sampai 36) menyalin alur TC-GS-ROLE-319 dan TC-GS-ROLE-320.
- Temuan untuk QA:
  - Email, kredensial, dan env var akun `Cakra Mahendra` dan `Hanif Pradipta` tidak ada di Tabel Pre-setup TC; ditulis "disediakan tim FE".
  - Mekanisme menyiapkan access level dan baris role per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-329 Expected f memuat `[Date]` pada body notifikasi tanpa format; spec mengikuti format tanggal General Settings aktif.
  - TC-GS-ROLE-329 Langkah Uji tidak menyebut surface untuk "lima role lain"; spec memakai Changelog Tab System dengan Search nama user.
  - TC-GS-ROLE-338 Expected c ("switch OFF dengan nilai tersimpan") tidak menyebut nilai; spec membaca Read dan Update tetap checked sesuai Pre-setup #20.
  - TC-GS-ROLE-329 dan TC-GS-ROLE-330 Expected tidak menyebut cara menghitung entri; spec memakai total entri terhadap baseline dengan kemampuan baca yang disediakan tim FE.
