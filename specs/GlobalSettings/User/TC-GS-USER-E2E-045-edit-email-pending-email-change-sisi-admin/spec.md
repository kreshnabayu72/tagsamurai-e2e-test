---
id: TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin
title: "Edit Email User Activated: Pending Email Change, Email Pending Dicadangkan, Edit Email Ulang, dan Dialog Cancel Pending Email Change"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-228
  - TC-GS-USER-229
  - TC-GS-USER-230
  - TC-GS-USER-233
  - TC-GS-USER-234
  - TC-GS-USER-235
  - TC-GS-USER-1080
  - TC-GS-USER-1082
coverage:
  web: automated
---

# Edit Email User Activated: Pending Email Change, Email Pending Dicadangkan, Edit Email Ulang, dan Dialog Cancel Pending Email Change

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`; menggantikan Dewi Lestari No. 12 dan Rina Putri No. 15 agar data Pre-setup tidak diubah, S-06):
  - User `Dewi Lestari {runId}-045`: email `dewilestari+{runId}-045@qwertysystem.net`, Activated, tanpa email pending. Email baru uji: `dewilestari.new+{runId}-045@qwertysystem.net`.
  - User `Rina Putri {runId}-045`: email `rinaputri+{runId}-045@qwertysystem.net`, Activated, dengan email pending `rinaputri.new+{runId}-045@qwertysystem.net` (Confirmation Email pertama terkirim ke alamat itu). Email pending kedua uji: `rina.second+{runId}-045@qwertysystem.net`.
- Kemampuan teknis:
  - Mail-catcher yang dapat dibaca per alamat email dan link konfirmasi dapat dibuka dari tab baru (disediakan tim FE); email dicari berdasarkan alamat tujuan.
  - Membuka link konfirmasi di tab baru pada sesi aktor lalu menutup tab itu.
  - Mencatat jumlah entri Tab Changelog sebagai baseline (S-12).
- State global: tidak ada. Mail-catcher tidak diubah, hanya dibaca.
- Cleanup (`after`): hapus kedua user seed.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Dewi Lestari {runId}-045`, tekan Enter

### TC-GS-USER-228: Edit email user Activated menyimpan email baru sebagai pending

3. Klik (⋯) baris `Dewi Lestari {runId}-045` → `Edit`
4. Ubah Email ke `dewilestari.new+{runId}-045@qwertysystem.net`
5. Klik `[Save]`
6. Verifikasi toast sukses: "Success, user has been updated."
7. Verifikasi hanya satu toast yang tampil (tanpa toast khusus email)
8. Verifikasi baris `Dewi Lestari {runId}-045` menampilkan badge `Pending Email Confirmation`
9. Verifikasi kolom Email baris `Dewi Lestari {runId}-045` tetap `dewilestari+{runId}-045@qwertysystem.net`
10. Klik (⋯) baris `Dewi Lestari {runId}-045` → `Edit`
11. Verifikasi field Email berisi `dewilestari+{runId}-045@qwertysystem.net`
12. Verifikasi label `Pending email change to dewilestari.new+{runId}-045@qwertysystem.net`
13. Verifikasi Button Cancel di samping label pending
14. Klik `✕` pada header Popup Edit

### TC-GS-USER-229: Email pending dicadangkan, user lain tidak bisa memakai email pending

15. Klik `[+ User]` di Table Tools
16. Ketik Email `rinaputri.new+{runId}-045@qwertysystem.net`
17. Tunggu ±500 ms
18. Verifikasi inline error `Email already exists` pada field Email
19. Klik `✕` pada header Popup Create
20. Verifikasi dialog `Unsaved Changes`
21. Klik `[Leave]`

### TC-GS-USER-1080: Edit Email ke email pending user lain ditolak

22. Klik (⋯) baris `Dewi Lestari {runId}-045` → `Edit`
23. Ubah Email ke `rinaputri.new+{runId}-045@qwertysystem.net`
24. Tunggu ±500 ms
25. Verifikasi inline error `Email already exists` pada field Email
26. Klik `[Save]`
27. Verifikasi Popup Edit tetap terbuka
28. Verifikasi tidak ada toast sukses
29. Klik `✕` pada header Popup Edit
30. Verifikasi dialog `Unsaved Changes`
31. Klik `[Leave]`
32. Verifikasi kolom Email baris `Dewi Lestari {runId}-045` tetap `dewilestari+{runId}-045@qwertysystem.net`

### TC-GS-USER-233 dan TC-GS-USER-235: Dialog Cancel Pending Email Change, screening dan Go Back

33. Ganti isi kotak search dengan `Rina Putri {runId}-045`, tekan Enter
34. Klik Name `Rina Putri {runId}-045` di User List
35. Klik Tab Changelog
36. Catat jumlah entri Tab Changelog `Rina Putri {runId}-045` sebagai baseline
37. Klik menu User di sidebar Global Settings
38. Klik icon Search, ketik `Rina Putri {runId}-045`, tekan Enter
39. Klik (⋯) baris `Rina Putri {runId}-045` → `Edit`
40. Klik Button Cancel di samping label pending
41. Verifikasi dialog Title `Cancel Pending Email Change`
42. Verifikasi body dialog memuat bullet `• Rina Putri {runId}-045`
43. Verifikasi body dialog memuat `The email will revert to rinaputri+{runId}-045@qwertysystem.net.` dan `Are you sure you want to cancel it?`
44. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Change]`
45. Klik `[Go Back]`
46. Verifikasi dialog tertutup
47. Verifikasi label `Pending email change to rinaputri.new+{runId}-045@qwertysystem.net` tetap tampil
48. Verifikasi tidak ada toast
49. Klik `✕` pada header Popup Edit
50. Klik Name `Rina Putri {runId}-045` di User List
51. Klik Tab Changelog
52. Verifikasi jumlah entri Tab Changelog sama dengan baseline (tidak ada entri log baru)
53. Klik menu User di sidebar Global Settings

### TC-GS-USER-230: Edit email lagi sebelum konfirmasi membatalkan link lama

54. Klik icon Search, ketik `Rina Putri {runId}-045`, tekan Enter
55. Klik (⋯) baris `Rina Putri {runId}-045` → `Edit`
56. Ubah email pending ke `rina.second+{runId}-045@qwertysystem.net`
57. Klik `[Save]`
58. Tunggu aksi selesai
59. Klik (⋯) baris `Rina Putri {runId}-045` → `Edit`
60. Verifikasi label `Pending email change to rina.second+{runId}-045@qwertysystem.net`
61. Klik `✕` pada header Popup Edit
62. Buka tab baru, buka link konfirmasi pertama (email ke `rinaputri.new+{runId}-045@qwertysystem.net`) dari mail-catcher
63. Verifikasi link pertama ditolak dengan pesan `"This confirmation link has expired or was already used."`
64. Tutup tab link konfirmasi

### TC-GS-USER-234: [Cancel Change] membatalkan pending

65. Klik (⋯) baris `Rina Putri {runId}-045` → `Edit`
66. Klik Button Cancel di samping label pending
67. Klik `[Cancel Change]`
68. Verifikasi toast sukses: "Success, pending email change has been canceled."
69. Verifikasi label pending hilang
70. Verifikasi Button Cancel hilang
71. Verifikasi field Email berisi `rinaputri+{runId}-045@qwertysystem.net` (email aktual tetap email lama)
72. Klik `✕` pada header Popup Edit
73. Verifikasi badge `Pending Email Confirmation` hilang dari baris `Rina Putri {runId}-045` di User List
74. Buka tab baru, buka link konfirmasi lama (email ke `rina.second+{runId}-045@qwertysystem.net`) dari mail-catcher
75. Verifikasi link konfirmasi lama ditolak sebagai kedaluwarsa
76. Tutup tab link konfirmasi

### TC-GS-USER-1082: Email pending dilepas setelah Cancel Pending Email Change

77. Klik `[+ User]` di Table Tools
78. Ketik Email `rina.second+{runId}-045@qwertysystem.net`
79. Tunggu ±500 ms
80. Verifikasi field Email berisi `rina.second+{runId}-045@qwertysystem.net`
81. Verifikasi tidak ada inline error `Email already exists` pada field Email
82. Klik `✕` pada header Popup Create
83. Verifikasi dialog `Unsaved Changes`
84. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Semua TC di spec ini satu topik aksi (Pending Email Change sisi admin) dan tidak berkelas harness; pembacaan link dari mail-catcher adalah langkah rutin (bagian 3 prinsip 13 butir d).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (84 langkah) karena delapan TC berada di satu topik aksi dan satu layar (Popup Edit dan Popup Create untuk email), dengan dua user seed; tiap blok TC berdiri sendiri dan memakai keadaan pending yang dibangun hook `before`, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan layar dan baseline (langkah 1 sampai 2, 33 sampai 38) tidak dihitung.
- Urutan TC sumber diubah: TC-GS-USER-229 dan TC-GS-USER-1080 memakai email pending awal Rina Putri (`rinaputri.new+...`) sebelum diganti; TC-GS-USER-233 dan TC-GS-USER-235 berada sebelum aksi yang mengubah atau membatalkan pending (TC-GS-USER-230 lalu TC-GS-USER-234); TC-GS-USER-1082 berada paling akhir karena membutuhkan pending yang sudah dibatalkan. TC-GS-USER-1082 mengetik email pending kedua (`rina.second+...`) yang dilepas oleh `[Cancel Change]` TC-GS-USER-234, setara email `rinaputri.new@qwertysystem.net` pada TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 sampai 2 (pembukaan), 14, 49, 61, 72 (menutup Popup Edit tanpa perubahan), 19 sampai 21, 29 sampai 31, dan 82 sampai 84 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, `[Leave]`, S-08), 33 sampai 38 dan 50 sampai 54 (navigasi ke Tab Changelog dan Search), 58 (menunggu aksi selesai), 62, 64, 74, 76 (membuka dan menutup tab link konfirmasi).
- Asersi tambahan di luar Expected TC (S-03): langkah 27, 28, dan 32 membuktikan Expected b TC-GS-USER-1080 ("[Save] tidak menyimpan perubahan email"); langkah 52 adalah asersi jumlah berbaseline untuk "tidak ada entri log" TC-GS-USER-235 (bukan asersi absence log kelas g); langkah 80 adalah anchor positif untuk absence inline error.
- Temuan untuk QA:
  - TC-GS-USER-228 Post Condition (Confirmation Email dikirim ke email baru; email lama tetap dipakai login) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-USER-234 Post Condition (banner Pending Email Change di My Profile hilang) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-USER-1080 Post Condition (email aktual dan pending Dewi Lestari tidak berubah) tidak punya langkah observasi; tidak diasersi (S-01). Langkah 32 membaca kolom Email aktual hanya sebagai bukti Expected b.
  - TC-GS-USER-1080 Expected b tidak menyebut langkah klik `[Save]` di Langkah Uji; spec menambah klik `[Save]` (langkah 26) untuk mengamati bahwa perubahan tidak tersimpan.
  - TC-GS-USER-234 tidak menyebut apakah Popup Edit tetap terbuka sesudah `[Cancel Change]`; spec berasumsi popup tetap terbuka (label dan Button Cancel diasersi di popup) dan menutupnya dengan `✕` sebelum mengamati User List.
  - TC-GS-USER-233 Expected b memakai placeholder `[email lama]`; spec memakai email lama user seed.
  - TC-GS-USER-230 menyebut "link konfirmasi pertama dari mail-catcher" tanpa baseline jumlah email; spec mengambil link dari email tujuan alamat pending pertama.
  - TC-GS-USER-235 Expected b "entri log" tidak menyebut surface log; spec memakai jumlah entri Tab Changelog berbaseline.
  - TC-GS-USER-228 sampai 234 dan 1080 sampai 1082 menyebut Dewi Lestari dan Rina Putri Pre-setup (No. 12, No. 15); spec memakai user seed bersuffix agar data Pre-setup tidak diubah (S-06).
