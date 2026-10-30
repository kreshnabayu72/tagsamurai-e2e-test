---
id: TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain
title: "Multi-Konteks Dua Admin: Email Kembar saat Create, Last-Write-Wins pada Edit, Toggle, dan Inline Custom Field, Race Cancel Change, serta Record Dihapus Sesi Lain pada Edit, Toggle, Delete, dan Bulk Delete"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-1006
  - TC-GS-USER-195
  - TC-GS-USER-353
  - TC-GS-USER-237
  - TC-GS-USER-985
  - TC-GS-USER-1010
  - TC-GS-USER-1011
  - TC-GS-USER-1015
  - TC-GS-USER-1016
coverage:
  web: automated
---

# Multi-Konteks Dua Admin: Email Kembar saat Create, Last-Write-Wins pada Edit, Toggle, dan Inline Custom Field, Race Cancel Change, serta Record Dihapus Sesi Lain pada Edit, Toggle, Delete, dan Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata; kelas harness c: multi-konteks dua admin, bagian 3 prinsip 13). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`), untuk akun Sesi A dan Sesi B.
- Akun Sesi A (Admin A, sesi UI utama): Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Akun Admin B (Total Control kedua): disediakan tim FE (tidak ada di Tabel Pre-setup TC); kredensial `Spectra.env.GS_TC2_PASSWORD`. Admin B dipakai di dua bentuk: sesi UI kedua (Sesi B, konteks browser terpisah dengan sesi login sendiri, login di hook `before` dan berada di User List) hanya untuk TC-GS-USER-1006 dan TC-GS-USER-985 karena hasil di sesi itu diasersi; dan sesi API (`[API Admin B]`) untuk TC-GS-USER-195, 353, 1010, 1011, 1015, dan 1016, yang hanya memicu perubahan state (konvensi bagian 3, P-2 `[KEPUTUSAN 2026-10-21]`). Klien HTTP untuk sesi API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Position `Staff` dan `Supervisor` (No. 22), Division `Finance` (No. 23), Custom Field Blood Type (No. 24), produk `Fixed Asset` (No. 26). Dewi Lestari, Rina Putri, dan user lain di Tabel Pre-setup No. 10-22 diganti user seed milik spec karena menjadi target aksi tulis atau hapus (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (HK1), Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Dewi Lestari {runId}-070`, Email `dewilestari+{runId}-070@qwertysystem.net`, Active, Position `Staff`, Employee ID `DL-{runId}-070`, Blood Type `A` (TC-GS-USER-195, 353, dan 985). Employee ID baru TC-GS-USER-195: `DL2-{runId}-070`.
  - `Rina Putri {runId}-070`, Email `rinaputri+{runId}-070@qwertysystem.net`, email pending `rinaputri.new+{runId}-070@qwertysystem.net` (TC-GS-USER-237).
  - `Rudi Hakim A {runId}-070`, `Rudi Hakim B {runId}-070`, dan `Rudi Hakim C {runId}-070`, Email `rudihakima+{runId}-070@qwertysystem.net`, `rudihakimb+{runId}-070@qwertysystem.net`, dan `rudihakimc+{runId}-070@qwertysystem.net`, Active (TC-GS-USER-1010, 1011, dan 1015).
  - `Tono Wijaya {runId}-070` (Email `tonowijaya+{runId}-070@qwertysystem.net`) dan `Rani Lestari {runId}-070` (Email `ranilestari+{runId}-070@qwertysystem.net`) (TC-GS-USER-1016).
- Data Dinamis yang dibuat lewat UI oleh spec: `Hana Pertiwi {runId}-070` (First Name `Hana`, Last Name `Pertiwi {runId}-070`, Email `hanapertiwi+{runId}-070@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`) dibuat Sesi A di TC-GS-USER-1006 dan dihapus di hook `after`.
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Dua konteks browser paralel dalam satu spec (Sesi A dan Sesi B) dan satu sesi API Admin B; langkah dijalankan berurutan dengan penanda `[Sesi A]`, `[Sesi B]`, dan `[API Admin B]`.
  - Seeding user (termasuk Position, Employee ID, Blood Type, dan email pending) lewat API.
  - Sesi A dan Sesi B tidak menerima pembaruan otomatis User List dari perubahan sesi lain selama langkah "tanpa refresh" (TC-GS-USER-985, 1010, 1011, 1015, dan 1016).
  - Mail-catcher: membaca tautan konfirmasi pada email ke `rinaputri.new+{runId}-070@qwertysystem.net` (HK4) dan membukanya di tab baru Sesi A (TC-GS-USER-237).
- State global yang diubah: tidak ada selain data user milik spec. Spec tidak mengubah jam, plan, atau konfigurasi.
- Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah, tanpa mengandalkan setup berhasil penuh): hapus lewat API semua user seed dan `Hana Pertiwi {runId}-070` yang masih ada; tutup konteks Sesi B dan lepas sesi API Admin B; kembalikan sesi ke akun default suite.

## Test Steps

### Pembukaan layar

1. [Sesi A] Buka Global Settings > User > User List (sub-tab Login User)
2. [Sesi A] Pilih 100 baris per halaman pada Pagination
3. [Sesi A] Klik icon Search, ketik `{runId}-070`, tekan Enter

### TC-GS-USER-1006: Create, dua admin submit email sama bersamaan, submit kedua ditolak inline

4. [Sesi A] Klik `[+ User]` di Table Tools
5. [Sesi B] Klik `[+ User]` di Table Tools
6. [Sesi A] Isi First Name `Hana`, Last Name `Pertiwi {runId}-070`, Division `Finance`, Email `hanapertiwi+{runId}-070@qwertysystem.net`, centang Access `Fixed Asset`
7. [Sesi B] Isi First Name `Hana`, Last Name `Pertiwi {runId}-070`, Division `Finance`, Email `hanapertiwi+{runId}-070@qwertysystem.net`, centang Access `Fixed Asset`
8. [Sesi A] Klik `[Submit]`
9. [Sesi A] Verifikasi toast sukses: "Success, user has been created."
10. [Sesi B] Klik `[Submit]`
11. [Sesi B] Verifikasi inline error `Email already exists` pada field Email
12. [Sesi B] Verifikasi Popup Create tetap terbuka
13. [Sesi B] Verifikasi input First Name, Last Name, Division, dan Access utuh
14. [Sesi B] Verifikasi tidak ada dialog yang tampil
15. [Sesi B] Klik `✕` pada header Popup Create
16. [Sesi B] Verifikasi dialog `Unsaved Changes` tampil
17. [Sesi B] Klik `[Leave]`

### TC-GS-USER-195: Edit, data diubah sesi lain tersimpan last-write-wins tanpa dialog Data has changed

18. [Sesi A] Klik (⋯) baris `Dewi Lestari {runId}-070` → `Edit`
19. [API Admin B] Ubah Position `Dewi Lestari {runId}-070` ke `Supervisor`
20. [Sesi A] Ubah Employee ID ke `DL2-{runId}-070`
21. [Sesi A] Klik `[Save]`
22. [Sesi A] Verifikasi toast sukses: "Success, user has been updated."
23. [Sesi A] Verifikasi tidak ada dialog `Data has changed`
24. [Sesi A] Verifikasi Popup Edit tertutup
25. [Sesi A] Verifikasi kolom Employee ID baris `Dewi Lestari {runId}-070` menampilkan `DL2-{runId}-070`
26. [Sesi A] Verifikasi kolom Position baris `Dewi Lestari {runId}-070` menampilkan `Staff` (nilai yang termuat di form Sesi A, bukan `Supervisor` dari Admin B)

### TC-GS-USER-353: Inline edit Custom Field, last-write-wins saat admin lain mengubah field sama

27. [Sesi A] Klik Name `Dewi Lestari {runId}-070` di User List
28. [Sesi A] Hover baris Blood Type, klik icon edit
29. [Sesi A] Pilih `O`
30. [API Admin B] Ubah Blood Type `Dewi Lestari {runId}-070` ke `B`
31. [Sesi A] Klik `[✓ Save]`
32. [Sesi A] Verifikasi toast sukses: "Success, Blood Type has been updated."
33. [Sesi A] Verifikasi Display `Blood Type: O`
34. [Sesi A] Klik menu User di sidebar Global Settings
35. [Sesi A] Klik icon Search, ketik `{runId}-070`, tekan Enter

### TC-GS-USER-237: Race, link konfirmasi dibuka tepat setelah admin Cancel Change

36. Baca tautan konfirmasi pada email ke `rinaputri.new+{runId}-070@qwertysystem.net` dari mail-catcher
37. [Sesi A] Klik (⋯) baris `Rina Putri {runId}-070` → `Edit`
38. [Sesi A] Klik Button Cancel di samping label pending
39. [Sesi A] Klik `[Cancel Change]`
40. [Sesi A] Segera buka tautan konfirmasi di tab baru, tanpa menunggu toast
41. [Sesi A] Verifikasi tautan ditolak sebagai kedaluwarsa
42. [Sesi A] Tutup tab tautan konfirmasi
43. [Sesi A] Klik `✕` pada header Popup Edit
44. [Sesi A] Verifikasi kolom Email baris `Rina Putri {runId}-070` tetap `rinaputri+{runId}-070@qwertysystem.net`

### TC-GS-USER-985: Concurrent, dua admin toggle user yang sama

45. [Sesi B] Buka Global Settings > User > User List (sub-tab Login User)
46. [Sesi B] Klik icon Search, ketik `Dewi Lestari {runId}-070`, tekan Enter
47. [Sesi A] Klik icon Changelog di Table Tools
48. [Sesi A] Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
49. [Sesi A] Klik icon Search pada Modal Changelog, ketik `Dewi Lestari {runId}-070`, tekan Enter
50. [Sesi A] Catat jumlah entri hasil Search sebagai baseline J0
51. [Sesi A] Tutup Modal Changelog User dengan klik `✕`
52. [Sesi A] Ganti isi kotak search dengan `Dewi Lestari {runId}-070`, tekan Enter
53. [Sesi A] Klik switch Active baris `Dewi Lestari {runId}-070`
54. [Sesi A] Klik `[Deactivate]`
55. [Sesi A] Tunggu aksi selesai (toast sukses tampil)
56. [Sesi B] Klik switch Active baris `Dewi Lestari {runId}-070` tanpa refresh
57. [Sesi B] Klik `[Deactivate]`
58. [Sesi B] Verifikasi toast sukses: "Success, user has been deactivated."
59. [Sesi B] Verifikasi switch Active baris `Dewi Lestari {runId}-070` OFF
60. [Sesi B] Verifikasi tidak ada dialog `Data has changed`
61. [Sesi A] Klik icon Changelog di Table Tools
62. [Sesi A] Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
63. [Sesi A] Klik icon Search pada Modal Changelog, ketik `Dewi Lestari {runId}-070`, tekan Enter
64. [Sesi A] Verifikasi jumlah entri hasil Search sama dengan J0 + 1 (hanya entri Deactivate dari Sesi A, tidak ada entri kedua dari Sesi B)
65. [Sesi A] Tutup Modal Changelog User dengan klik `✕`
66. [Sesi A] Verifikasi switch Active baris `Dewi Lestari {runId}-070` tetap OFF

### TC-GS-USER-1010: Edit user yang sudah dihapus sesi lain, toast netral dan list ter-refresh

67. [Sesi A] Ganti isi kotak search dengan `{runId}-070`, tekan Enter
68. [Sesi A] Klik (⋯) baris `Rudi Hakim A {runId}-070` → `Edit`
69. [API Admin B] Hapus `Rudi Hakim A {runId}-070`
70. [Sesi A] Ubah Position ke `Supervisor`
71. [Sesi A] Klik `[Save]`
72. [Sesi A] Verifikasi toast netral: "This user is no longer available."
73. [Sesi A] Verifikasi Popup Edit tertutup
74. [Sesi A] Verifikasi baris `Dewi Lestari {runId}-070` tampil di User List (pembanding)
75. [Sesi A] Verifikasi User List ter-refresh tanpa baris `Rudi Hakim A {runId}-070`

### TC-GS-USER-1011: Toggle Active user yang sudah dihapus sesi lain, toast netral

76. [API Admin B] Hapus `Rudi Hakim B {runId}-070`
77. [Sesi A] Klik switch Active baris `Rudi Hakim B {runId}-070` tanpa refresh
78. [Sesi A] Klik `[Deactivate]`
79. [Sesi A] Verifikasi toast netral: "This user is no longer available."
80. [Sesi A] Verifikasi baris `Dewi Lestari {runId}-070` tampil di User List (pembanding)
81. [Sesi A] Verifikasi User List ter-refresh tanpa baris `Rudi Hakim B {runId}-070`

### TC-GS-USER-1015: Delete user yang sudah dihapus sesi lain, toast netral

82. [Sesi A] Klik (⋯) baris `Rudi Hakim C {runId}-070` → `Delete`
83. [API Admin B] Hapus `Rudi Hakim C {runId}-070`
84. [Sesi A] Klik `[Delete]`
85. [Sesi A] Verifikasi toast netral: "This user is no longer available."
86. [Sesi A] Verifikasi dialog Delete tertutup
87. [Sesi A] Verifikasi baris `Dewi Lestari {runId}-070` tampil di User List (pembanding)
88. [Sesi A] Verifikasi User List ter-refresh tanpa baris `Rudi Hakim C {runId}-070`

### TC-GS-USER-1016: Bulk Delete partial, satu baris sudah dihapus sesi lain

89. [Sesi A] Centang baris `Tono Wijaya {runId}-070` dan `Rani Lestari {runId}-070`
90. [API Admin B] Hapus `Rani Lestari {runId}-070`
91. [Sesi A] Bulk Action → `Delete`
92. [Sesi A] Klik `[Delete]`
93. [Sesi A] Verifikasi toast: "Success, user has been deleted. Some items failed."
94. [Sesi A] Verifikasi baris `Dewi Lestari {runId}-070` tampil di User List (pembanding)
95. [Sesi A] Verifikasi User List tidak memuat baris `Tono Wijaya {runId}-070`
96. [Sesi A] Verifikasi Bulk Action Bar hilang
97. [Sesi A] Verifikasi seleksi reset (tidak ada baris yang tercentang)

## Notes

- Mode: FE+BE (backend nyata, kelas harness c: multi-konteks dua admin). Sumber: `global-settings/user/TestCases/tc-user.md`. Suite serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Penanda `[Sesi A]` dan `[Sesi B]` menunjuk sesi UI, `[API Admin B]` menunjuk sesi API Admin B.
- Spec melewati sekitar 35 langkah (97 langkah). Alasan: kesembilan TC berada di satu kelas harness (c, dua admin pada entitas yang sama), tiap blok memakai user seed bersuffix sendiri sehingga blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah muncul dari satu baris per aksi per sesi dan satu `Verifikasi` per klausa Expected.
- Urutan TC sumber diubah: TC-GS-USER-1006 dan 195 dan 353 dan 237 lebih dulu (aksi yang mengubah atau membuat data), TC-GS-USER-985 sesudah TC-GS-USER-195 dan 353 karena menonaktifkan `Dewi Lestari {runId}-070` yang dipakai kedua TC itu, dan TC-GS-USER-1010, 1011, 1015, serta 1016 (aksi yang menghapus data) paling akhir (bagian 3 prinsip 5). Sesi B UI hanya dipakai di TC-GS-USER-1006 dan 985.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan layar dan Search `{runId}-070`, membaca tautan konfirmasi dari mail-catcher, menutup tab tautan, `✕` yang menutup Popup Edit (form tidak berubah sehingga tidak memunculkan `Unsaved Changes`), `Klik menu User` dan Search ulang setelah inline edit, membuka dan menutup Modal Changelog untuk baseline J0, "Tunggu aksi selesai" setelah `[Deactivate]` Sesi A, dan mengganti isi kotak search. Verifikasi "Modal Changelog User memuat entri" adalah anchor positif sebelum Search, dan verifikasi baris `Dewi Lestari {runId}-070` adalah anchor positif untuk asersi ketiadaan baris di User List (bagian 8b butir 2).
- TC-GS-USER-237 ditulis tanpa jeda antara klik `[Cancel Change]` dan pembukaan tautan; toast sukses Cancel Change tidak diasersi di blok ini (bukan Expected TC-GS-USER-237).
- Asersi "tidak ada entri Changelog kedua" TC-GS-USER-985 ditulis sebagai jumlah entri sama dengan baseline J0 + 1, yaitu asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g.
- Pembagian TC lintas spec: membuka tautan konfirmasi lama sesudah Cancel Change dengan jeda (TC-GS-USER-234) diverifikasi di spec 045; Create sukses di spec 024, Edit sukses di spec 035, Toggle Active sukses di spec 047, inline edit Custom Field sukses di spec 060, dan Bulk Delete sukses di spec 055.
- Temuan untuk QA:
  - TC-GS-USER-985, 1010, 1011, 1015, dan 1016 mensyaratkan sesi A tidak menyegarkan list ("tanpa refresh", "sesi lain"); error-handling-convention bagian 5.4 menyebut List dapat auto-refresh via SSE. Spec mengikuti TC dan mensyaratkan sesi tidak menerima pembaruan otomatis (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-195 menulis "Di tab lain" tanpa menyebut admin yang sama atau berbeda dan tanpa nilai Position serta Employee ID; spec memakai Admin B sesi API, Position `Supervisor`, dan Employee ID `DL2-{runId}-070`.
  - TC-GS-USER-353 Expected a ("Save diterima tanpa reject") tidak menyebut observasinya; spec mengasersi toast sukses `Success, Blood Type has been updated.` (teks mengikuti inline edit sukses di TC-GS-USER-346).
  - TC-GS-USER-237 berstatus Manual Only tetapi tetap ditulis (bagian 2 konvensi); "Segera" tidak punya batas waktu, dan tautan konfirmasi dibaca dari mail-catcher yang tidak punya mekanisme di TC, PRD, atau LLD (disediakan tim FE/BE). Perbedaannya dengan TC-GS-USER-234 hanya tidak adanya jeda.
  - TC-GS-USER-1006 hanya menyebut Email; spec mengisi First Name, Last Name, Division, dan Access (field wajib TC-GS-USER-117) di kedua sesi supaya submit pertama sukses.
  - TC-GS-USER-1010, 1011, 1015, dan 1016 menulis "sesi lain" atau "Total Control lain"; spec memakai Admin B sesi API. TC-GS-USER-1011 tidak menyebut apakah dialog Deactivate tertutup setelah toast netral; spec tidak menutupnya dan hook `beforeEach` menutup dialog yang masih terbuka.
  - TC-GS-USER-195, 985, 1010, 1011, 1015, dan 1016 menyebut Dewi Lestari, Rudi Hakim, Tono Wijaya, dan Rani Lestari tanpa suffix; spec memakai user seed bersuffix `{runId}-070` milik spec (S-06).
  - TC-GS-USER-985 Expected b ("tidak ada entri Changelog kedua") mengandaikan satu Deactivate menghasilkan tepat satu entri; spec mengasersi selisih jumlah entri sebesar 1 terhadap baseline J0.
