---
id: TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail
title: "Toggle Active Single: Dialog Deactivate dan Activate, Cancel, Posisi Toggle Per-Produk, Modified By, dan Header Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-241
  - TC-GS-USER-242
  - TC-GS-USER-244
  - TC-GS-USER-246
  - TC-GS-USER-247
  - TC-GS-USER-248
  - TC-GS-USER-250
  - TC-GS-USER-251
  - TC-GS-USER-1087
coverage:
  web: automated
---

# Toggle Active Single: Dialog Deactivate dan Activate, Cancel, Posisi Toggle Per-Produk, Modified By, dan Header Detail

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22) tidak dipakai sebagai target aksi dan tidak diubah.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user berstatus Activated, Division `Finance`, nilai field wajib lain seragam:
  - U-1: Name `Dewi Lestari {runId}-047`, email `dewilestari+{runId}-047@qwertysystem.net`, Active, tanpa approval, Access `Fixed Asset`.
  - U-2: Name `Jane Smith {runId}-047`, email `janesmith+{runId}-047@qwertysystem.net`, Inactive (dinonaktifkan manual), Access `Supply Asset`.
  - U-3: Name `Joko Susilo {runId}-047`, email `jokosusilo+{runId}-047@qwertysystem.net`, Active, Access `Fixed Asset` dan `Supply Asset`, toggle per-produk Fixed Asset ON dan Supply Asset OFF, approver pada 2 approval yang menunggu, dan memegang aset Borrowed (HK8; seeding approval in-flight dan aset Borrowed disediakan tim FE/BE).
  - U-4: Name `Dewi Lestari Header {runId}-047`, email `dewilestariheader+{runId}-047@qwertysystem.net`, Active, Access `Fixed Asset` (target toggle dari header Detail).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 sampai U-4 lewat API.
- Kemampuan teknis: jam server dan jam browser sinkron (asersi Last Update sama dengan waktu aksi, toleransi 1 menit; S-12); hover; membuka halaman Fixed Asset > Settings > User dan Supply Asset > Settings > User dengan akun Total Control; membuka Modal Changelog User dan Tab Changelog Detail.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-047`, tekan Enter
2. Klik icon Changelog pada Table Tools
3. Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
4. Klik icon Search pada Modal Changelog, ketik `Dewi Lestari {runId}-047`, tekan Enter
5. Catat jumlah entri hasil Search sebagai baseline J0
6. Tutup Modal Changelog lewat `✕`

### TC-GS-USER-241: Toggle Active OFF memunculkan dialog Deactivate User

7. Klik switch Active baris `Dewi Lestari {runId}-047` (ON)
8. Verifikasi Title dialog `Deactivate User`
9. Verifikasi body memuat bullet `• Dewi Lestari {runId}-047`
10. Verifikasi body memuat `This will deactivate user across all products. This user will be immediately logged out.`
11. Verifikasi body memuat `Are you sure you want to deactivate it?`
12. Verifikasi tombol `[Cancel]` dan `[Deactivate]`
13. Verifikasi body tidak memuat baris `Pending approvals of this user will be reassigned to other approvers.`

### TC-GS-USER-244: Deactivate dialog [Cancel] mengembalikan switch ON

14. Klik `[Cancel]`
15. Verifikasi dialog tertutup
16. Verifikasi switch Active baris `Dewi Lestari {runId}-047` kembali ON
17. Verifikasi tidak ada toast
18. Klik icon Changelog pada Table Tools
19. Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
20. Klik icon Search pada Modal Changelog, ketik `Dewi Lestari {runId}-047`, tekan Enter
21. Verifikasi jumlah entri hasil Search sama dengan baseline J0 (tidak ada entri baru sesudah baseline)
22. Tutup Modal Changelog lewat `✕`

### TC-GS-USER-242: Dialog Deactivate menambah baris approval in-flight tanpa angka

23. Klik switch Active baris `Joko Susilo {runId}-047`
24. Verifikasi body memuat baris `Pending approvals of this user will be reassigned to other approvers.` tanpa angka jumlah
25. Verifikasi body memuat baris peringatan aset aktif (Joko Susilo memegang aset Borrowed) tampil terpisah dari baris approval, tanpa angka jumlah
26. Verifikasi body ditutup `Are you sure you want to deactivate it?`
27. Klik `[Cancel]`

### TC-GS-USER-246: Toggle Active ON user Inactive memunculkan dialog Activate

28. Klik switch Active baris `Jane Smith {runId}-047` (OFF)
29. Verifikasi body memuat bullet `• Jane Smith {runId}-047`
30. Verifikasi body memuat `This will activate user across all products. Are you sure you want to activate it?`
31. Verifikasi tombol `[Cancel]` dan `[Activate]`

### TC-GS-USER-248: Activate dialog [Cancel] mengembalikan switch OFF

32. Klik `[Cancel]`
33. Verifikasi switch Active baris `Jane Smith {runId}-047` tetap OFF
34. Verifikasi tidak ada toast

### TC-GS-USER-247 dan TC-GS-USER-1087: Activate dikonfirmasi, Modified By dan Last Update diperbarui

35. Klik switch Active baris `Jane Smith {runId}-047`
36. Klik `[Activate]`
37. Verifikasi toast sukses "Success, user has been activated."
38. Verifikasi switch Active baris `Jane Smith {runId}-047` ON
39. Catat waktu aksi sebagai T1 (sesudah `[Activate]`, jam server dan jam browser sinkron)
40. Verifikasi Modified By baris `Jane Smith {runId}-047` `Siti N`
41. Verifikasi Last Update baris `Jane Smith {runId}-047` sama dengan T1 (toleransi 1 menit)
42. Catat nilai Last Update baris `Jane Smith {runId}-047` sebagai L1

### TC-GS-USER-250: Global OFF lalu ON mempertahankan posisi toggle per-produk

43. Klik switch Active baris `Joko Susilo {runId}-047`
44. Klik `[Deactivate]`
45. Tunggu aksi selesai (switch Active baris `Joko Susilo {runId}-047` berubah OFF)
46. Buka Fixed Asset > Settings > User
47. Cari baris `Joko Susilo {runId}-047`
48. Verifikasi toggle Fixed Asset baris `Joko Susilo {runId}-047` tampil disabled dengan posisi ON
49. Buka Supply Asset > Settings > User
50. Cari baris `Joko Susilo {runId}-047`
51. Verifikasi toggle Supply Asset baris `Joko Susilo {runId}-047` tampil disabled dengan posisi OFF
52. Klik menu User di sidebar Global Settings
53. Klik icon Search, ketik `{runId}-047`, tekan Enter
54. Klik switch Active baris `Joko Susilo {runId}-047`
55. Klik `[Activate]`
56. Tunggu aksi selesai (switch Active baris `Joko Susilo {runId}-047` berubah ON)
57. Buka Fixed Asset > Settings > User
58. Cari baris `Joko Susilo {runId}-047`
59. Verifikasi toggle Fixed Asset baris `Joko Susilo {runId}-047` enabled dengan posisi ON
60. Buka Supply Asset > Settings > User
61. Cari baris `Joko Susilo {runId}-047`
62. Verifikasi toggle Supply Asset baris `Joko Susilo {runId}-047` enabled dengan posisi OFF

### TC-GS-USER-1087: Last Update sama dengan Date baris Activate di Tab Changelog

63. Klik menu User di sidebar Global Settings
64. Klik icon Search, ketik `{runId}-047`, tekan Enter
65. Buka Detail `Jane Smith {runId}-047` dengan klik Name
66. Klik Tab `Changelog`
67. Verifikasi Date baris `Activate` terbaru sama dengan L1 (Last Update yang dicatat pada langkah 42)

### TC-GS-USER-251: Toggle Active dari header User Detail memakai dialog yang sama dengan List

68. Klik menu User di sidebar Global Settings
69. Klik icon Search, ketik `{runId}-047`, tekan Enter
70. Buka Detail `Dewi Lestari Header {runId}-047` dengan klik Name
71. Klik switch Active header
72. Verifikasi Title dialog `Deactivate User`
73. Verifikasi body memuat bullet `• Dewi Lestari Header {runId}-047`
74. Verifikasi body memuat `This will deactivate user across all products. This user will be immediately logged out.`
75. Verifikasi body memuat `Are you sure you want to deactivate it?`
76. Verifikasi tombol `[Cancel]` dan `[Deactivate]`
77. Klik `[Deactivate]`
78. Verifikasi toast "Success, user has been deactivated."
79. Verifikasi badge header berubah `Inactive`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (79 langkah) karena sembilan TC Toggle Active single berada di satu kelas harness (fungsional), satu layar (User List dan header Detail), dan satu dataset seed milik spec. Tiap blok berdiri sendiri pada user seed sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-244 mengikuti TC-GS-USER-241 pada dialog yang sama dan TC-GS-USER-248 mengikuti TC-GS-USER-246 pada dialog yang sama (langkah "Klik switch" TC-244 dan TC-248 sumber dipenuhi oleh langkah 7 dan 28). TC-GS-USER-247 dan TC-GS-USER-1087 digabung pada satu aksi Activate user U-2 (langkah 35 sampai 42; Expected 1087 a sama dengan Expected 247 a), dengan pembacaan Tab Changelog 1087 di langkah 63 sampai 67. TC-GS-USER-242 ditaruh sesudah TC-GS-USER-244 supaya perbandingan jumlah entri Changelog (langkah 21) terjadi sebelum aksi yang mengubah data. TC-GS-USER-250 dan TC-GS-USER-251 ditaruh paling akhir karena pindah halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1, 2, 4, 5, 6 (Search dan baseline), 18, 20, 22, 27 dan 32 (menutup dialog dengan `[Cancel]` setelah screening), 39 dan 42 (mencatat waktu aksi dan nilai), 45 dan 56 (Tunggu aksi selesai), 46 sampai 47, 49 sampai 50, 57 sampai 58, 60 sampai 61 (membuka halaman produk), 52 sampai 53, 63 sampai 65, 68 sampai 70 (kembali ke User List dan membuka Detail).
- Asersi tambahan: langkah 3 dan 19 (Modal Changelog memuat entri) adalah pembanding sebelum Search dan perbandingan jumlah (bagian 8b butir 2). Langkah 13 (baris approval in-flight tidak tampil) didahului langkah 8 sampai 12 yang menampilkan isi dialog pada surface yang sama.
- P-1: TC-GS-USER-244 butir b ("tidak ada ... entri log") diasersi di spec ini lewat perbandingan jumlah entri Modal Changelog User terhadap baseline J0 (langkah 5 dan 21), bukan lewat spec absence, karena tidak ada spec absence yang memuat aksi Cancel Deactivate untuk TC itu dan dialog Cancel dibangun dalam alur ini (S-05).
- TC-GS-USER-243 diverifikasi di spec 159.
- Nama seed: U-4 dipakai untuk TC-GS-USER-251. Teks bullet dialog 251 memuat Name U-4.
- Last Update (TC-GS-USER-1087 c): diasersi sama dengan waktu aksi T1 (langkah 39 dan 41, toleransi 1 menit, S-12); klausa "lebih baru dari nilai yang dicatat" tidak diasersi terpisah karena kolom Last Update berketelitian menit sehingga nilai lama dan baru dapat jatuh pada menit yang sama.
- Langkah 25 (peringatan aset aktif Borrowed, TC-GS-USER-242 b) diasersi tanpa teks persis karena TC tidak menuliskan teks barisnya (lihat Temuan untuk QA).
- Pembagian TC: log Deactivate dan Activate (Changelog, System Log, Activity Log) diverifikasi di spec pencatatan log; toggle per-produk dari sisi produk dan Toggle Active gagal 5xx diverifikasi di spec lain.
- Temuan untuk QA:
  - TC-GS-USER-247 Post Condition ("Terdampak: Supply Asset > Settings > User ..., approver dropdown") tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-242 butir b tidak menuliskan teks baris peringatan aset aktif; spec hanya mengasersi keberadaannya, terpisah dari baris approval, tanpa angka.
  - TC-GS-USER-246 butir a tidak menyebut Title dialog Activate; spec tidak mengasersi Title.
  - TC-GS-USER-247 dan TC-GS-USER-248 tidak menyatakan status awal Jane Smith (Inactive) di precondition TC-GS-USER-247; status Inactive berasal dari TC-GS-USER-246.
  - TC-GS-USER-250 langkah 2 tidak menyebut cara mencari baris di Fixed Asset > Settings > User dan Supply Asset > Settings > User, dan mengandaikan akun Total Control dapat membuka kedua halaman; spec memakai pencarian baris berdasarkan Name.
  - TC-GS-USER-244 butir b ("entri log") tidak menyebut surface log; spec memakai Modal Changelog User.
  - TC-GS-USER-241, TC-GS-USER-246, dan TC-GS-USER-251 memakai user Pre-setup (Dewi Lestari, Jane Smith); spec memakai seed milik spec agar data Pre-setup tidak berubah.
