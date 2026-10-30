---
id: TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah
title: "Multi-Konteks Toggle Active: Record Sudah Dihapus atau Sudah Berubah Status oleh Admin Lain (Single dan Bulk)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-169
  - TC-GS-UCF-170
  - TC-GS-UCF-171
  - TC-GS-UCF-477
  - TC-GS-UCF-478
  - TC-GS-UCF-479
  - TC-GS-UCF-480
  - TC-GS-UCF-319
  - TC-GS-UCF-320
coverage:
  web: automated
---

# Multi-Konteks Toggle Active: Record Sudah Dihapus atau Sudah Berubah Status oleh Admin Lain (Single dan Bulk)

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas multi-konteks (c): dua admin pada Client A yang sama.
- Suite serial (`parallel: false`): spec ini mengubah dan menghapus Custom Field milik sendiri dengan dua pelaku; tidak berjalan bersamaan dengan spec lain.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field pada Sesi A; langkah tidak mengulang pembukaan layar.
- Akun Sesi A (Admin A, sesi UI): Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Akun Admin B (pelaku kedua): Total Control Client A `Nadia Pratama` (Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup, fixture baru), kredensial `Spectra.env.GS_TC2_PASSWORD`. Admin B hanya memicu perubahan state (hapus, aktifkan, atau nonaktifkan Custom Field) dan hasilnya diasersi di Sesi A, sehingga Admin B memakai sesi API (P-2); kemampuan sesi API Admin B (login dan pemanggilan hapus atau ubah status Custom Field atas nama Admin B hingga tersimpan) disediakan tim FE/BE tanpa mengarang endpoint.
- Data Pre-setup Client A: tidak dipakai langsung; 14 Custom Field Pre-setup dan Population di-seed idempotent oleh hook `before` (disediakan tim FE/BE) sebagai latar tabel dan tidak diubah.
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; fixture baru `Fixture.customFieldUser.multiToggle048`; seluruhnya Text, bebas nilai User):
  - `Bulk Skip A {runId}-048`, `Bulk Skip B {runId}-048`: Inactive (TC-GS-UCF-169).
  - `Bulk Idem A {runId}-048`, `Bulk Idem B {runId}-048`: Inactive (TC-GS-UCF-170).
  - `Bulk Gone A {runId}-048`, `Bulk Gone B {runId}-048`: Active (TC-GS-UCF-171).
  - `Skip Off A {runId}-048`, `Skip Off B {runId}-048`: Active (TC-GS-UCF-477).
  - `Gone On A {runId}-048`, `Gone On B {runId}-048`: Inactive (TC-GS-UCF-478).
  - `Toggle Vanish On {runId}-048`: Inactive (TC-GS-UCF-479).
  - `Idem On Probe {runId}-048`: Inactive (TC-GS-UCF-480).
  - `Toggle Same {runId}-048`: Active (TC-GS-UCF-319).
  - `Toggle Gone {runId}-048`: Active (TC-GS-UCF-320).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-048` yang masih ada; tutup sesi API Admin B.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: sesi API Admin B (di atas); Search tabel dan Changelog Custom Field dengan filter Action; menunggu toast sukses lama hilang otomatis (jeda pendek, ≤ 4 detik, TC-GS-UCF-489) pada langkah 13, 26, 40, 54, 68, 81, 93, dan 104. Entri Changelog bersifat permanen; asersi entri memakai nama bersuffix `{runId}-048` penuh sehingga baseline entri milik run ini adalah nol.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-UCF-169: Bulk Activate dengan satu item yang sudah dihapus admin lain memproses sisanya dengan toast sebagian

1. [Sesi A] Ketik Search `Bulk Skip`, tekan Enter
2. [Sesi A] Centang `Bulk Skip A {runId}-048` dan `Bulk Skip B {runId}-048`
3. [Admin B, sesi API] Hapus `Bulk Skip B {runId}-048` hingga tersimpan
4. [Sesi A] Klik `Bulk Action` > `Activate`, klik `[Activate]`
5. [Sesi A] Verifikasi toast sukses: "Success, custom field has been activated. Some items were skipped."
6. [Sesi A] Verifikasi `Bulk Skip A {runId}-048` berstatus Active
7. [Sesi A] Verifikasi `Bulk Skip B {runId}-048` tidak ada di tabel
8. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset (list di-refresh)
9. [Sesi A] Klik icon Changelog, pilih filter Action `Activate`, Search `Bulk Skip`, tekan Enter
10. [Sesi A] Verifikasi Changelog memuat entri Activate untuk `Bulk Skip A {runId}-048`
11. [Sesi A] Verifikasi Changelog tidak memuat entri Activate untuk `Bulk Skip B {runId}-048`
12. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-170: Bulk Activate dengan item yang sudah diaktifkan admin lain diproses idempotent tanpa dilewati

13. [Sesi A] Tunggu toast dari langkah 5 hilang otomatis
14. [Sesi A] Ketik Search `Bulk Idem`, tekan Enter
15. [Sesi A] Centang `Bulk Idem A {runId}-048` dan `Bulk Idem B {runId}-048`
16. [Admin B, sesi API] Aktifkan `Bulk Idem A {runId}-048` hingga tersimpan
17. [Sesi A] Klik `Bulk Action` > `Activate`, klik `[Activate]`
18. [Sesi A] Verifikasi toast sukses: "Success, custom field has been activated."
19. [Sesi A] Verifikasi toast tidak memuat "Some items were skipped"
20. [Sesi A] Verifikasi `Bulk Idem A {runId}-048` dan `Bulk Idem B {runId}-048` berstatus Active
21. [Sesi A] Klik icon Changelog, pilih filter Action `Activate`, Search `Bulk Idem`, tekan Enter
22. [Sesi A] Verifikasi Changelog memuat entri Activate (satu) untuk `Bulk Idem A {runId}-048` (oleh `Nadia P`)
23. [Sesi A] Verifikasi Changelog memuat satu entri Activate untuk `Bulk Idem B {runId}-048` (oleh `Sari D`)
24. [Sesi A] Verifikasi tidak ada entri Activate duplikat untuk `Bulk Idem A {runId}-048`
25. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-171: Bulk Deactivate dengan seluruh item sudah dihapus admin lain memberi toast netral

26. [Sesi A] Tunggu toast dari langkah 18 hilang otomatis
27. [Sesi A] Ketik Search `Bulk Gone`, tekan Enter
28. [Sesi A] Centang `Bulk Gone A {runId}-048` dan `Bulk Gone B {runId}-048`
29. [Admin B, sesi API] Hapus `Bulk Gone A {runId}-048` dan `Bulk Gone B {runId}-048` hingga tersimpan
30. [Sesi A] Klik `Bulk Action` > `Deactivate`, klik `[Deactivate]`
31. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
32. [Sesi A] Verifikasi tidak ada toast sukses
33. [Sesi A] Verifikasi tidak ada dialog blok
34. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset (list di-refresh)
35. [Sesi A] Klik icon Changelog, pilih filter Action `Delete`, Search `Bulk Gone`, tekan Enter
36. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Bulk Gone A {runId}-048` dan `Bulk Gone B {runId}-048` oleh `Nadia P`
37. [Sesi A] Ubah filter Action menjadi `Deactivate`
38. [Sesi A] Verifikasi Changelog tidak memuat entri Deactivate untuk `Bulk Gone A {runId}-048` dan `Bulk Gone B {runId}-048`
39. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-477: Bulk Deactivate dengan satu item yang sudah dihapus admin lain memproses sisanya dengan toast sebagian

40. [Sesi A] Tunggu toast dari langkah 31 hilang otomatis
41. [Sesi A] Ketik Search `Skip Off`, tekan Enter
42. [Sesi A] Centang `Skip Off A {runId}-048` dan `Skip Off B {runId}-048`
43. [Admin B, sesi API] Hapus `Skip Off B {runId}-048` hingga tersimpan
44. [Sesi A] Klik `Bulk Action` > `Deactivate`, klik `[Deactivate]`
45. [Sesi A] Verifikasi toast sukses: "Success, custom field has been deactivated. Some items were skipped."
46. [Sesi A] Verifikasi `Skip Off A {runId}-048` berstatus Inactive
47. [Sesi A] Verifikasi `Skip Off B {runId}-048` tidak ada di tabel
48. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset (list di-refresh)
49. [Sesi A] Klik icon Changelog, Search `Skip Off`, tekan Enter
50. [Sesi A] Verifikasi Changelog memuat entri Deactivate untuk `Skip Off A {runId}-048` oleh `Sari D`
51. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Skip Off B {runId}-048` oleh `Nadia P`
52. [Sesi A] Verifikasi Changelog tidak memuat entri Deactivate untuk `Skip Off B {runId}-048`
53. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-478: Bulk Activate dengan seluruh item sudah dihapus admin lain memberi toast netral

54. [Sesi A] Tunggu toast dari langkah 45 hilang otomatis
55. [Sesi A] Ketik Search `Gone On`, tekan Enter
56. [Sesi A] Centang `Gone On A {runId}-048` dan `Gone On B {runId}-048`
57. [Admin B, sesi API] Hapus `Gone On A {runId}-048` dan `Gone On B {runId}-048` hingga tersimpan
58. [Sesi A] Klik `Bulk Action` > `Activate`, klik `[Activate]`
59. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
60. [Sesi A] Verifikasi tidak ada toast sukses
61. [Sesi A] Verifikasi tidak ada dialog blok
62. [Sesi A] Verifikasi `Gone On A {runId}-048` dan `Gone On B {runId}-048` tidak ada di tabel (list di-refresh)
63. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset
64. [Sesi A] Klik icon Changelog, Search `Gone On`, tekan Enter
65. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Gone On A {runId}-048` dan `Gone On B {runId}-048` oleh `Nadia P`
66. [Sesi A] Verifikasi Changelog tidak memuat entri Activate untuk `Gone On A {runId}-048` dan `Gone On B {runId}-048`
67. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-479: Activate single pada field yang sudah dihapus admin lain memberi toast netral

68. [Sesi A] Tunggu toast dari langkah 59 hilang otomatis
69. [Sesi A] Ketik Search `Toggle Vanish On {runId}-048`, tekan Enter
70. [Sesi A] Nyalakan switch Active baris `Toggle Vanish On {runId}-048`
71. [Sesi A] Verifikasi dialog `Activate Custom Field` tampil
72. [Admin B, sesi API] Hapus `Toggle Vanish On {runId}-048` hingga tersimpan
73. [Sesi A] Klik `[Activate]`
74. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
75. [Sesi A] Verifikasi tidak ada toast sukses
76. [Sesi A] Verifikasi `Toggle Vanish On {runId}-048` tidak ada di tabel (list di-refresh)
77. [Sesi A] Klik icon Changelog, Search `Toggle Vanish On {runId}-048`, tekan Enter
78. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Toggle Vanish On {runId}-048` oleh `Nadia P`
79. [Sesi A] Verifikasi Changelog tidak memuat entri Activate untuk `Toggle Vanish On {runId}-048`
80. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-480: Activate single ke status yang sudah tercapai oleh admin lain sukses idempotent

81. [Sesi A] Tunggu toast dari langkah 74 hilang otomatis
82. [Sesi A] Ketik Search `Idem On Probe {runId}-048`, tekan Enter
83. [Sesi A] Nyalakan switch Active baris `Idem On Probe {runId}-048`
84. [Sesi A] Verifikasi dialog `Activate Custom Field` tampil
85. [Admin B, sesi API] Aktifkan `Idem On Probe {runId}-048` hingga tersimpan
86. [Sesi A] Klik `[Activate]`
87. [Sesi A] Verifikasi toast sukses: "Success, custom field has been activated."
88. [Sesi A] Verifikasi switch `Idem On Probe {runId}-048` On
89. [Sesi A] Klik icon Changelog, Search `Idem On Probe {runId}-048`, tekan Enter
90. [Sesi A] Verifikasi Changelog memuat entri Activate untuk `Idem On Probe {runId}-048` oleh `Nadia P`
91. [Sesi A] Verifikasi Changelog hanya memuat 1 entri Activate (tidak ada entri Activate kedua)
92. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-319: Toggle ke status yang sudah tercapai oleh admin lain sukses idempotent

93. [Sesi A] Tunggu toast dari langkah 87 hilang otomatis
94. [Sesi A] Ketik Search `Toggle Same {runId}-048`, tekan Enter
95. [Sesi A] Matikan switch Active baris `Toggle Same {runId}-048` (dialog Deactivate terbuka)
96. [Admin B, sesi API] Nonaktifkan `Toggle Same {runId}-048` hingga tersimpan
97. [Sesi A] Klik `[Deactivate]`
98. [Sesi A] Verifikasi toast sukses: "Success, custom field has been deactivated."
99. [Sesi A] Verifikasi switch `Toggle Same {runId}-048` Off
100. [Sesi A] Klik icon Changelog, Search `Toggle Same {runId}-048`, tekan Enter
101. [Sesi A] Verifikasi Changelog memuat entri Deactivate (tepat 1) untuk `Toggle Same {runId}-048`
102. [Sesi A] Verifikasi tidak ada entri Deactivate kedua untuk `Toggle Same {runId}-048`
103. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-320: Toggle pada field yang sudah dihapus admin lain

104. [Sesi A] Tunggu toast dari langkah 98 hilang otomatis
105. [Sesi A] Ketik Search `Toggle Gone {runId}-048`, tekan Enter
106. [Sesi A] Matikan switch Active baris `Toggle Gone {runId}-048` (dialog Deactivate terbuka)
107. [Admin B, sesi API] Hapus `Toggle Gone {runId}-048` hingga tersimpan
108. [Sesi A] Klik `[Deactivate]`
109. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
110. [Sesi A] Verifikasi `Toggle Gone {runId}-048` tidak ada di tabel (list di-refresh)
111. [Sesi A] Klik icon Changelog, Search `Toggle Gone {runId}-048`, tekan Enter
112. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Toggle Gone {runId}-048` oleh `Nadia P`
113. [Sesi A] Verifikasi Changelog tidak memuat entri Deactivate untuk `Toggle Gone {runId}-048`
114. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: multi-konteks (prinsip 13c); penanda `[Sesi A]` dan `[Admin B, sesi API]` pada tiap langkah.
- Spec melewati sekitar 35 langkah (114 langkah). Seluruhnya satu kelas (multi-konteks toggle atas record yang sudah berubah), satu pasangan aktor, dan tiap blok memakai field milik sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Sembilan blok memakai pola yang sama (seleksi atau dialog, Admin B memicu, Sesi A mengonfirmasi, toast, tabel, Changelog); jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Admin B memakai sesi API (P-2, keputusan 2026-10-21): Admin B hanya memicu perubahan state dan hasilnya (toast, tabel, Changelog) diasersi di Sesi A; langkah pemicu ditulis "hingga tersimpan".
- Urutan TC dalam spec: 169, 170, 171, 477, 478, 479, 480, 319, 320. Tiap blok mengasersi toast yang mirip dengan blok sebelumnya; karena itu langkah 13, 26, 40, 54, 68, 81, 93, 104 menunggu toast lama hilang otomatis (S-09). TC-GS-UCF-319 dan 320 ditaruh paling akhir karena single toggle dengan dialog terbuka.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 14, 27, 41, 55, 69, 82, 94, 105 (Search agar baris target tampil), langkah 9, 21, 35, 37, 49, 64, 77, 89, 100, 111 (membuka Changelog atau mengubah filter Action), dan langkah penutup tiap blok (menutup modal dan Search).
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` jumlah/ada entri Delete oleh `Nadia P` pada langkah 36, 51, 65, 78, 112 berfungsi sebagai anchor positif untuk asersi absence entri Activate atau Deactivate (butir 2 konvensi 8b); langkah 8, 34, 48, 63 (bar hilang dan seleksi di-reset) menyatakan "list di-refresh" yang tidak punya observasi terpisah.
- P-1 (state berat): asersi tidak-ada-entri-log TC-GS-UCF-169 (langkah 11), 171 (langkah 38), 477 (langkah 52), 478 (langkah 66), 479 (langkah 79), dan 320 (langkah 113) tetap di spec ini, bukan di spec absence 070, karena konteksnya bergantung pada state yang dibangun langkah sebelumnya: pelaku kedua (Admin B) menghapus atau mengubah record di antara pembukaan dialog atau seleksi dan konfirmasi Sesi A. Sesi A memicu aksi Activate atau Deactivate sungguhan di spec ini dengan baseline (nama bersuffix `{runId}-048`) dan anchor positif entri Delete `Nadia P`; state itu tidak murah dibentuk ulang di spec 070.
- Pembagian TC lintas spec: Delete atas record yang sudah berubah (TC-GS-UCF-151, 152, 153, 318, 322) ada di spec 047. Asersi absence log TC-GS-UCF-171, 478, 479, dan 320 tidak punya aksi di spec absence (spec 070), sehingga ditulis sebagai `Verifikasi` berbaseline dengan anchor positif di spec ini (S-05).
- Temuan untuk QA:
  - TC-GS-UCF-169, 170, 171, 477, 478, 479, 480, 319, dan 320 ditandai `Manual Only — (d)` (dua sesi paralel); spec memakai sesi API Admin B sebagai pemicu dan sesi UI hanya untuk Admin A, sehingga dapat diotomasi.
  - TC-GS-UCF-320 Expected b menyatakan Changelog tidak memuat entri Deactivate untuk aksi Admin A (entri Delete oleh Admin kedua boleh ada); spec mengasersinya dengan anchor entri Delete (langkah 112 dan 113).
  - TC-GS-UCF-319 Expected b ("tidak ada entri Deactivate kedua") dan TC-GS-UCF-480 Expected c ("tidak ada entri Activate kedua") ditulis sebagai asersi jumlah entri (tepat 1 entri), bukan absence kelas g.
  - TC-GS-UCF-319 langkah 4 hanya menyebut "Buka Changelog" tanpa Search; spec mencari berdasarkan nama bersuffix.
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-UCF-477 ("efek ke User, Non-Login User, My Profile, FA > Settings > User, AC > Settings > User, AC > Settings > Group popup Total User Detail, Import") dan TC-GS-UCF-480 (idem).
  - TC-GS-UCF-169 sampai 480 memakai nama field tanpa suffix; spec memakai versi bersuffix `{runId}-048`. TC-GS-UCF-319 dan 320 (`Toggle Same`, `Toggle Gone`) tidak menyebut nilai User.
