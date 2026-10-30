---
id: TC-GS-UCF-E2E-068-pencatatan-activate-deactivate-delete-bulk-dan-log-aktor-non-total-control
title: "Pencatatan Activate, Deactivate, Delete, Bulk Activate Deactivate Delete per Field yang Diproses, dan Log Aksi Aktor Non-Total Control pada Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-285
  - TC-GS-UCF-286
  - TC-GS-UCF-287
  - TC-GS-UCF-290
coverage:
  web: automated
---

# Pencatatan Activate, Deactivate, Delete, Bulk Activate Deactivate Delete per Field yang Diproses, dan Log Aksi Aktor Non-Total Control pada Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) untuk TC-GS-UCF-285, 286, dan 287. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Seeding dan seluruh aksi pada ketiga TC ini dilakukan Sari Dewi.
  - Manage user and role: Create dan Read Rina Marlina `manageUserCreate_automated_qaTeam1@qwertysystem.net` (Pre-setup TC; Read aktif otomatis) untuk TC-GS-UCF-290, login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CREATE_PASSWORD`. Pre-setup TC memuat dua akun bernama tampil Rina Marlina (akun ini dan akun Import data `importCreate_automated_qaTeam1@qwertysystem.net`); Detail User dipilih lewat email akun ini.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field. Langkah yang membuka ulang halaman itu berfungsi sebagai pemulihan state sesudah System Log atau Activity Log.
- Data Pre-setup: tidak ada yang dipakai (seluruh target aksi adalah data milik spec).
- Data Dinamis (nama bersuffix `{runId}-068`; fixture baru `Fixture.customFieldUser.logAction068`):
  - Di-seed lewat API oleh Sari Dewi di hook `before` (seeding menghasilkan satu entri Create per field di tiga surface; entri ini menjadi baseline untuk hitungan Action lain): `Log Toggle Probe {runId}-068` (Text, Active; TC-GS-UCF-285), `Log Delete Probe {runId}-068` (Text; TC-GS-UCF-286), `Log Bulk On A {runId}-068` (Text, Inactive), `Log Bulk On B {runId}-068` (Text, Inactive), `Log Bulk On C {runId}-068` (Text, Active), `Log Bulk Off D {runId}-068` (Text, Inactive) untuk TC-GS-UCF-287. Seeding status Active dan Inactive melalui API.
  - Dibuat lewat UI oleh Rina Marlina: `Log Actor Probe {runId}-068` (TC-GS-UCF-290).
  - Entri Changelog, System Log, dan Activity Log bersifat audit trail permanen dan tidak dibersihkan; asersi hitungan memakai nama bersuffix unik per run (baseline dari entri Create seeding, S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-068` yang masih ada (`Log Toggle Probe`, `Log Actor Probe`); kembalikan sesi ke Sari Dewi.
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (Sari Dewi dan Rina Marlina) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding Custom Field dan statusnya lewat API; Search pada Modal Changelog, tab System Log di Detail User, dan Activity Log tab User Action (kolom pencarian tidak dijelaskan di TC; lihat Temuan untuk QA); ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip dan sesi akun.

## Test Steps

### TC-GS-UCF-285: Log Activate dan Deactivate mencatat Inactive dan Active

1. Ketik Search `Log Toggle Probe {runId}-068` pada tabel utama, tekan Enter
2. Matikan switch Active baris `Log Toggle Probe {runId}-068`
3. Klik `[Deactivate]`
4. Nyalakan switch Active baris `Log Toggle Probe {runId}-068`
5. Klik `[Activate]`
6. Tunggu aksi selesai (dialog tertutup)
7. Klik icon Changelog
8. Ketik Search `Log Toggle Probe {runId}-068`, tekan Enter
9. Verifikasi Changelog: entri Deactivate tampil tepat 1 kali
10. Verifikasi entri Deactivate: Field `Log Toggle Probe {runId}-068 — Status`, Old Value `Active`, New Value `Inactive`
11. Verifikasi Changelog: entri Activate tampil tepat 1 kali
12. Verifikasi entri Activate: Field `Log Toggle Probe {runId}-068 — Status`, Old Value `Inactive`, New Value `Active`
13. Verifikasi Modified By kedua entri Changelog `Sari D`
14. Klik `[✕]`
15. Buka Global Settings > User > Detail Sari Dewi > tab System Log
16. Ketik Search `Log Toggle Probe {runId}-068`, tekan Enter
17. Verifikasi System Log Sari Dewi: entri Deactivate dan entri Activate masing-masing tampil tepat 1 kali dengan Object `Custom Field`, Name `Log Toggle Probe {runId}-068`
18. Buka Global Settings > Activity Log > tab User Action
19. Ketik Search `Log Toggle Probe {runId}-068`, tekan Enter
20. Verifikasi Activity Log: entri Deactivate dan entri Activate masing-masing tampil tepat 1 kali dengan Modified By `Sari D`
21. Buka Global Settings > User > Custom Field

### TC-GS-UCF-287: Bulk Activate, Deactivate, dan Delete mencatat satu entri per field yang diproses

22. Ketik Search `{runId}-068` pada tabel utama, tekan Enter
23. Centang `Log Bulk On A {runId}-068`, `Log Bulk On B {runId}-068`, dan `Log Bulk On C {runId}-068`
24. Klik `Bulk Action` > `Activate`
25. Klik `[Activate]`
26. Tunggu aksi selesai (dialog tertutup)
27. Centang `Log Bulk On A {runId}-068`, `Log Bulk On B {runId}-068`, dan `Log Bulk Off D {runId}-068`
28. Klik `Bulk Action` > `Deactivate`
29. Klik `[Deactivate]`
30. Tunggu aksi selesai (dialog tertutup)
31. Centang `Log Bulk On A {runId}-068`, `Log Bulk On B {runId}-068`, dan `Log Bulk On C {runId}-068`
32. Klik `Bulk Action` > `Delete`
33. Klik `[Delete]`
34. Tunggu aksi selesai (dialog tertutup)
35. Klik icon Changelog
36. Ketik Search `Log Bulk On A {runId}-068`, tekan Enter
37. Verifikasi Changelog: entri Activate untuk `Log Bulk On A {runId}-068` tepat 1
38. Verifikasi Changelog: entri Deactivate untuk `Log Bulk On A {runId}-068` tepat 1
39. Verifikasi Changelog: entri Delete untuk `Log Bulk On A {runId}-068` tepat 1
40. Ganti isi kotak search dengan `Log Bulk On B {runId}-068`, tekan Enter
41. Verifikasi Changelog: entri Activate untuk `Log Bulk On B {runId}-068` tepat 1
42. Verifikasi Changelog: entri Deactivate untuk `Log Bulk On B {runId}-068` tepat 1
43. Verifikasi Changelog: entri Delete untuk `Log Bulk On B {runId}-068` tepat 1
44. Ganti isi kotak search dengan `Log Bulk On C {runId}-068`, tekan Enter
45. Verifikasi Changelog: entri Delete untuk `Log Bulk On C {runId}-068` tepat 1
46. Verifikasi Changelog: `Log Bulk On C {runId}-068` yang sudah Active tidak memiliki entri Activate (entri untuk nama itu hanya Create seeding dan Delete)
47. Ganti isi kotak search dengan `Log Bulk Off D {runId}-068`, tekan Enter
48. Verifikasi Changelog: entri Create seeding untuk `Log Bulk Off D {runId}-068` tampil
49. Verifikasi Changelog: `Log Bulk Off D {runId}-068` yang sudah Inactive tidak memiliki entri Deactivate
50. Klik `[✕]`
51. Buka Global Settings > User > Detail Sari Dewi > tab System Log
52. Ketik Search `Log Bulk On A {runId}-068`, tekan Enter
53. Verifikasi System Log Sari Dewi: entri Activate, Deactivate, dan Delete untuk `Log Bulk On A {runId}-068` masing-masing tampil tepat 1 kali
54. Ganti isi kotak search dengan `Log Bulk On B {runId}-068`, tekan Enter
55. Verifikasi System Log Sari Dewi: entri Activate, Deactivate, dan Delete untuk `Log Bulk On B {runId}-068` masing-masing tampil tepat 1 kali
56. Ganti isi kotak search dengan `Log Bulk On C {runId}-068`, tekan Enter
57. Verifikasi System Log Sari Dewi: entri Delete untuk `Log Bulk On C {runId}-068` tampil tepat 1 kali dan tidak ada entri Activate untuk nama itu
58. Ganti isi kotak search dengan `Log Bulk Off D {runId}-068`, tekan Enter
59. Verifikasi System Log Sari Dewi: entri Create seeding untuk `Log Bulk Off D {runId}-068` tampil dan tidak ada entri Deactivate untuk nama itu
60. Buka Global Settings > Activity Log > tab User Action
61. Ketik Search `Log Bulk On A {runId}-068`, tekan Enter
62. Verifikasi Activity Log: entri Activate, Deactivate, dan Delete untuk `Log Bulk On A {runId}-068` masing-masing tampil tepat 1 kali
63. Ganti isi kotak search dengan `Log Bulk On B {runId}-068`, tekan Enter
64. Verifikasi Activity Log: entri Activate, Deactivate, dan Delete untuk `Log Bulk On B {runId}-068` masing-masing tampil tepat 1 kali
65. Ganti isi kotak search dengan `Log Bulk On C {runId}-068`, tekan Enter
66. Verifikasi Activity Log: entri Delete untuk `Log Bulk On C {runId}-068` tampil tepat 1 kali dan tidak ada entri Activate untuk nama itu
67. Ganti isi kotak search dengan `Log Bulk Off D {runId}-068`, tekan Enter
68. Verifikasi Activity Log: entri Create seeding untuk `Log Bulk Off D {runId}-068` tampil dan tidak ada entri Deactivate untuk nama itu
69. Buka Global Settings > User > Custom Field

### TC-GS-UCF-286: Log Delete mencatat nama field sebagai Old Value dan strip sebagai New Value

70. Ketik Search `Log Delete Probe {runId}-068` pada tabel utama, tekan Enter
71. Klik `⋯` pada baris `Log Delete Probe {runId}-068`, pilih `Delete`
72. Klik `[Delete]`
73. Tunggu aksi selesai (dialog tertutup)
74. Klik icon Changelog
75. Ketik Search `Log Delete Probe {runId}-068`, tekan Enter
76. Verifikasi Changelog: entri Delete tampil tepat 1 kali
77. Verifikasi entri Delete: Field `Log Delete Probe {runId}-068`, Old Value `Log Delete Probe {runId}-068`, New Value `-`, Modified By `Sari D`
78. Klik `[✕]`
79. Buka Global Settings > User > Detail Sari Dewi > tab System Log
80. Ketik Search `Log Delete Probe {runId}-068`, tekan Enter
81. Verifikasi System Log Sari Dewi: entri Delete tampil tepat 1 kali dengan Object `Custom Field`, Name `Log Delete Probe {runId}-068`
82. Buka Global Settings > Activity Log > tab User Action
83. Ketik Search `Log Delete Probe {runId}-068`, tekan Enter
84. Verifikasi Activity Log: entri Delete tampil tepat 1 kali dengan Modified By `Sari D`
85. Buka Global Settings > User > Custom Field

### TC-GS-UCF-290: Log aksi aktor non-Total Control masuk ke System Log aktor itu

86. Ganti akun: logout dari Total Control Client A Sari Dewi
87. Login sebagai Manage user and role: Create dan Read Rina Marlina (`manageUserCreate_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_CREATE_PASSWORD`)
88. Buka Global Settings > User > Custom Field
89. Klik `[+ Custom Field]`
90. Isi Field Name `Log Actor Probe {runId}-068`
91. Pilih Data Type `Text`
92. Klik `[Submit]`
93. Tunggu aksi selesai (modal tertutup)
94. Buka Global Settings > User > Detail Rina Marlina (`manageUserCreate_automated_qaTeam1@qwertysystem.net`) > tab System Log
95. Ketik Search `Log Actor Probe {runId}-068`, tekan Enter
96. Verifikasi System Log Rina Marlina: entri Create `Log Actor Probe {runId}-068` tampil
97. Buka Global Settings > User > Detail Sari Dewi > tab System Log
98. Ketik Search `Log Toggle Probe {runId}-068`, tekan Enter
99. Verifikasi anchor System Log Sari Dewi: entri milik Sari Dewi untuk `Log Toggle Probe {runId}-068` tampil
100. Ganti isi kotak search dengan `Log Actor Probe {runId}-068`, tekan Enter
101. Verifikasi System Log Sari Dewi: empty state `No results found` (entri `Log Actor Probe {runId}-068` tidak muncul)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 285, 287, 286, 290. Urutan menyimpang dari urutan TC sumber: aksi yang menghapus data (TC-GS-UCF-286 dan Delete bulk di TC-GS-UCF-287) ditaruh sesudah TC-GS-UCF-285 (bagian 3 prinsip 5), dan TC-GS-UCF-290 di akhir karena ganti akun ke Rina Marlina (ganti akun eksplisit pada langkah awal blok TC-GS-UCF-290 dan bagian sesudahnya tetap bermakna bila blok sebelumnya gagal). TC-GS-UCF-287 sebelum TC-GS-UCF-286 supaya tidak ada entri Activate atau Deactivate tambahan dari `Log Toggle Probe` pada pencarian per nama.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengisian Search tabel utama, Search pada Changelog, System Log, dan Activity Log, penutupan Modal Changelog lewat `[✕]` (tanpa dialog karena tidak ada form), pembukaan ulang Global Settings > User > Custom Field sebagai pemulihan state, centang baris pada Bulk Action, dan langkah "Tunggu aksi selesai" sesudah `[Deactivate]`, `[Activate]`, `[Delete]`, dan `[Submit]` yang hasilnya tidak diasersi langsung dan langkah berikutnya berpindah surface (bagian 8b butir 8).
- TC-GS-UCF-287 Expected a dan b ("tidak dicatat") serta Expected c TC-GS-UCF-290 ("tidak muncul di System Log Sari Dewi") diasersi sebagai hitungan entri berbaseline: baseline adalah entri Create seeding untuk nama bersuffix unik (S-12) yang berfungsi sebagai anchor positif di surface yang sama, dan empty state `No results found` untuk pencarian `Log Actor Probe` adalah anchor positif. Asersi ini mengikuti P-1: state berat dibangun oleh tiga aksi bulk berurutan pada langkah awal blok TC-GS-UCF-287. Asersi absence log murni (Edit No-Op, aksi gagal, item dilewati) ada di spec 070. Isolasi log per aktor (TC-GS-UCF-290) adalah asersi kepemilikan log dan boleh berada di spec pencatatan.
- Spec melewati sekitar 35 langkah (101 langkah). Seluruhnya satu kelas (pencatatan aksi status dan Delete, tiga surface), sebagian besar blok baca-log berpola yang tidak dihitung ke ambang; tiap blok TC memakai field bersuffix sendiri sehingga tetap bermakna bila blok lain gagal. Pemisahan akun (Sari Dewi lalu Rina Marlina) memakai langkah ganti akun eksplisit dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Temuan untuk QA:
  - Mekanisme pencarian pada tab System Log Detail User dan Activity Log tab User Action, serta kolom yang tersedia (Object, Name, Modified By), tidak dijelaskan di TC; spec memakai Search atas nama field bersuffix pada kedua surface.
  - TC-GS-UCF-290 memakai "Detail Rina Marlina" dan "Detail Sari Dewi" untuk akun yang tidak dibedakan dari akun lain bernama sama (Pre-setup TC memuat dua akun Rina Marlina); spec memilih Detail lewat email akun Manage user and role: Create dan Read. TC-GS-UCF-290 juga tidak menyebut apakah Rina Marlina diizinkan melihat Detail User Sari Dewi dan tab System Log-nya; spec mengikuti langkah TC.
  - TC-GS-UCF-287 tidak menyebut cara men-seed status Active dan Inactive field fixture (D-148 sampai D-151); disediakan tim FE/BE lewat API.
  - TC-GS-UCF-287 Expected d menyebut "entri identik muncul di System Log dan Activity Log" tanpa menyebut jumlah per field; spec mengasersi hitungan sama seperti Changelog.
  - Token nilai kosong New Value di TC-GS-UCF-286 ditulis `-` (hyphen) sedangkan TC-GS-UCF-283 dan 380 memakai `—`; spec mengikuti masing-masing TC.
  - TC-GS-UCF-285 menyebut pembukaan dialog Deactivate dan Activate tanpa menyebut toast hasil; toast tidak diasersi.
  - Post Condition TC-GS-UCF-290 (`Log Actor Probe` ada) tidak punya langkah observasi tambahan selain Expected a.
