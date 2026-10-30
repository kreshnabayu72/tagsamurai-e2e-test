---
id: TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save
title: "Edit Custom Field: Save Tanpa Perubahan (No-Op), Kapitalisasi, Sukses Tidak Menyentuh Nilai User, Saving State, Klik Ganda Save, Field Inactive, dan Modified By Admin Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-126
  - TC-GS-UCF-127
  - TC-GS-UCF-128
  - TC-GS-UCF-99
  - TC-GS-UCF-129
  - TC-GS-UCF-130
  - TC-GS-UCF-463
  - TC-GS-UCF-374
  - TC-GS-UCF-133
  - TC-GS-UCF-459
coverage:
  web: automated
---

# Edit Custom Field: Save Tanpa Perubahan (No-Op), Kapitalisasi, Sukses Tidak Menyentuh Nilai User, Saving State, Klik Ganda Save, Field Inactive, dan Modified By Admin Lain

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun (password hanya lewat env var, tidak ditulis di spec atau fixture):
  - Akun aktor utama (login di hook `before`): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Dipakai TC-GS-UCF-126, 127, 128, 99, 129, 130, 463, 374, 133.
  - Admin kedua Client A (Nadia Pratama, Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`. Dipakai TC-GS-UCF-459 lewat langkah ganti akun eksplisit.
  - Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; blok akun kedua membukanya lewat langkah eksplisit sesudah ganti akun.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk setiap akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup Client A (hanya dibaca, tidak diubah; Last Updated dan Modified By tidak berubah; 14 field di-seed hook `before` lewat API dengan `Fixture.customFieldUser.preset14`): `Employee Grade` (TC-GS-UCF-126 dan 127; Save tanpa perubahan nyata).
- Data Dinamis milik spec Client A (seeding lewat API di hook `before`, bersuffix `{runId}-033`; fixture baru `Fixture.customFieldUser.edit033`; Active kecuali dinyatakan lain, Required No, Placeholder kosong kecuali dinyatakan lain):
  - `Edit Meta Renamed {runId}-033`: Text, nilai User Rahmat Hidayat = `Alpha Value` (dipakai sebagai precondition TC, diasersi pada Detail User; nilai User di-seed lewat mekanisme yang disediakan tim FE/BE). Menjadi `Edit Meta Final {runId}-033` pada TC-GS-UCF-99 dan dipakai TC-GS-UCF-129 dan 130.
  - `Case DD {runId}-033`: Dropdown `Alpha`, `Beta` (TC-GS-UCF-128).
  - `Case Mix DD {runId}-033`: Dropdown `Alpha`, `Beta` (TC-GS-UCF-463).
  - `Cap Mix {runId}-033`: Text (TC-GS-UCF-374).
  - `Inactive Probe {runId}-033`: Text, Inactive (TC-GS-UCF-133).
  - `Modifier Probe {runId}-033`: Text; Modified By `Sari D`; Last Updated lebih lama dari hari uji (TC-GS-UCF-459; Last Updated lama diatur backend, "disediakan tim BE").
- Akun Login User Client A `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Rahmat Hidayat) hanya menjadi pemilik nilai Custom Field yang dibaca pada Detail User.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-033` (termasuk nama hasil perubahan).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons PATCH selama 3 detik (TC-GS-UCF-129, objek uji Saving state, bukan kegagalan yang dipaksa); klik ganda cepat pada `[Save]`; membaca Changelog Custom Field (Search) dengan baseline jumlah entri; jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit, kolom Last Updated berketelitian menit).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite). Required Yes pada `Edit Meta Final {runId}-033` memengaruhi form Create User selama spec ini; suite serial dan field dihapus di `after`.

## Test Steps

### TC-GS-UCF-126: Save tanpa perubahan memberi toast netral tanpa log dan tanpa mengubah Last Updated

1. Ketik Search `Employee Grade`, tekan Enter
2. Catat Last Updated dan Modified By baris `Employee Grade`
3. Buka Changelog Custom Field, Search `Employee Grade`, catat jumlah entri sebagai baseline, lalu tutup Modal Changelog
4. Klik `⋯` pada baris `Employee Grade`, pilih `Edit`
5. Klik `[Save]` tanpa mengubah apa pun
6. Verifikasi toast netral (Info): "No changes to save."
7. Verifikasi popup tertutup
8. Verifikasi tidak ada error `Field name already exists` terhadap dirinya sendiri
9. Verifikasi Last Updated baris `Employee Grade` tidak berubah
10. Verifikasi Modified By baris `Employee Grade` tidak berubah
11. Buka Changelog Custom Field, Search `Employee Grade`
12. Verifikasi jumlah entri sama dengan baseline (tidak ada entri Changelog baru)
13. Tutup Modal Changelog

### TC-GS-UCF-127: Save yang hanya mengubah kapitalisasi atau spasi tepi Field Name diperlakukan No-Op

14. Klik `⋯` pada baris `Employee Grade`, pilih `Edit`
15. Ubah Field Name menjadi ` EMPLOYEE GRADE `
16. Klik `[Save]`
17. Verifikasi toast netral (Info): "No changes to save."
18. Verifikasi popup tertutup
19. Verifikasi nama di tabel tetap `Employee Grade`
20. Verifikasi Last Updated baris `Employee Grade` tidak berubah
21. Buka Changelog Custom Field, Search `Employee Grade`
22. Verifikasi jumlah entri sama dengan baseline (tidak ada entri Changelog baru)
23. Tutup Modal Changelog

### TC-GS-UCF-128: Save yang hanya mengubah kapitalisasi label value Dropdown diperlakukan No-Op

24. Ganti isi kotak search dengan `Case DD {runId}-033`, tekan Enter
25. Buka Changelog Custom Field, Search `Case DD {runId}-033`, catat jumlah entri sebagai baseline, lalu tutup Modal Changelog
26. Klik `⋯` pada baris `Case DD {runId}-033`, pilih `Edit`
27. Ubah badge `Alpha` menjadi `ALPHA`, tekan Enter
28. Klik `[Save]`
29. Verifikasi toast netral (Info): "No changes to save."
30. Verifikasi Value Setting baris `Case DD {runId}-033` tetap `Alpha`, `Beta`
31. Buka Changelog Custom Field, Search `Case DD {runId}-033`
32. Verifikasi jumlah entri sama dengan baseline (tidak ada entri Changelog baru)
33. Tutup Modal Changelog

### TC-GS-UCF-99: Mengubah Field Name, Placeholder, dan Required Field tidak menyentuh nilai User

34. Ganti isi kotak search dengan `Edit Meta Renamed {runId}-033`, tekan Enter
35. Klik `⋯` pada baris `Edit Meta Renamed {runId}-033`, pilih `Edit`
36. Ubah Field Name menjadi `Edit Meta Final {runId}-033`, Placeholder menjadi `Type here`, dan Required Field ke Yes
37. Klik `[Save]`
38. Verifikasi toast sukses: "Success, custom field has been updated."
39. Verifikasi baris menampilkan Field Name `Edit Meta Final {runId}-033`
40. Verifikasi baris menampilkan Placeholder `Type here`
41. Verifikasi baris menampilkan Required `Yes`
42. Verifikasi Modified By baris `Sari D`
43. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
44. Verifikasi label field `Edit Meta Final {runId}-033` tampil
45. Verifikasi nilai `Alpha Value` tetap
46. Kembali ke Global Settings > User > Custom Field, ketik Search `Edit Meta Final {runId}-033`, tekan Enter

### TC-GS-UCF-129: Tombol Save menampilkan Saving state dan menutup kontrol selama request

47. Klik `⋯` pada baris `Edit Meta Final {runId}-033`, pilih `Edit`
48. Ubah Placeholder menjadi `Slow`
49. Pasang intercept pada request PATCH Custom Field: tahan respons 3 detik
50. Klik `[Save]`
51. Verifikasi `[Save]` dalam keadaan loading selama request
52. Verifikasi `[Save]` disabled selama request
53. Verifikasi `[Clear Field]` disabled selama request
54. Verifikasi `[✕]` disabled selama request
55. Verifikasi input popup disabled selama request
56. Verifikasi popup tertutup setelah respons
57. Verifikasi toast sukses: "Success, custom field has been updated."
58. Lepas intercept PATCH

### TC-GS-UCF-130: Klik ganda [Save] hanya menyimpan satu perubahan

59. Buka Changelog Custom Field, Search `Edit Meta Final {runId}-033`, catat jumlah entri Edit Placeholder sebagai baseline, lalu tutup Modal Changelog
60. Klik `⋯` pada baris `Edit Meta Final {runId}-033`, pilih `Edit`
61. Ubah Placeholder menjadi `Twice`
62. Klik `[Save]` dua kali cepat
63. Verifikasi hanya 1 toast sukses
64. Buka Changelog Custom Field, Search `Edit Meta Final {runId}-033`
65. Verifikasi Changelog bertambah tepat 1 entri Edit Placeholder terhadap baseline untuk perubahan ini
66. Tutup Modal Changelog

### TC-GS-UCF-463: Save yang mengubah kapitalisasi label value Dropdown bersama penambahan value menyimpan keduanya

67. Ganti isi kotak search dengan `Case Mix DD {runId}-033`, tekan Enter
68. Klik `⋯` pada baris `Case Mix DD {runId}-033`, pilih `Edit`
69. Ubah badge `Alpha` menjadi `ALPHA`, tekan Enter
70. Ketik `Gamma` di Dropdown Values, tekan Enter
71. Klik `[Save]`
72. Verifikasi toast sukses: "Success, custom field has been updated." (bukan toast netral)
73. Perhatikan kolom Value Setting baris `Case Mix DD {runId}-033`
74. Verifikasi kolom Value Setting menampilkan badge `ALPHA`, `Beta`, lalu `+1 more`
75. Buka Changelog Custom Field, Search `Case Mix DD {runId}-033`
76. Verifikasi Changelog memuat 1 entri Edit: Field `Case Mix DD {runId}-033 — Value Setting`, Old Value `Alpha, Beta`, New Value `ALPHA, Beta, Gamma`
77. Tutup Modal Changelog

### TC-GS-UCF-374: Save campuran yang mengubah kapitalisasi Field Name dan Placeholder menyimpan keduanya

78. Ganti isi kotak search dengan `Cap Mix {runId}-033`, tekan Enter
79. Klik `⋯` pada baris `Cap Mix {runId}-033`, pilih `Edit`
80. Ubah Field Name menjadi `CAP MIX {runId}-033`
81. Isi Placeholder `Hint`, klik `[Save]`
82. Verifikasi toast sukses: "Success, custom field has been updated."
83. Verifikasi nama di tabel `CAP MIX {runId}-033`
84. Buka Changelog Custom Field, Search `CAP MIX {runId}-033`
85. Verifikasi Changelog memuat entri Edit Field `CAP MIX {runId}-033 — Field Name` dengan Old Value `Cap Mix {runId}-033` dan New Value `CAP MIX {runId}-033`
86. Verifikasi Changelog memuat entri Edit Field `CAP MIX {runId}-033 — Placeholder` dengan Old Value `—` dan New Value `Hint`
87. Tutup Modal Changelog

### TC-GS-UCF-133: Field Inactive dapat diedit tanpa mengubah statusnya

88. Ganti isi kotak search dengan `Inactive Probe {runId}-033`, tekan Enter
89. Klik `⋯` pada baris `Inactive Probe {runId}-033`, pilih `Edit`
90. Ubah Placeholder menjadi `Still off`
91. Klik `[Save]`
92. Verifikasi toast sukses: "Success, custom field has been updated."
93. Verifikasi Placeholder baris `Inactive Probe {runId}-033` `Still off`
94. Verifikasi switch Active baris `Inactive Probe {runId}-033` tetap Off

### TC-GS-UCF-459: Edit oleh admin lain memperbarui Modified By dan Last Updated

95. Ganti akun: Logout, lalu login sebagai Total Control Client A (admin kedua, Nadia Pratama) dan buka Global Settings > User > Custom Field
96. Ketik Search `Modifier Probe {runId}-033`, tekan Enter
97. Catat nilai kolom Modified By dan Last Updated baris `Modifier Probe {runId}-033`
98. Verifikasi Modified By baris `Modifier Probe {runId}-033` `Sari D`
99. Klik `⋯` pada baris `Modifier Probe {runId}-033`, pilih `Edit`
100. Ubah Placeholder menjadi `By second admin`, klik `[Save]`
101. Verifikasi toast sukses: "Success, custom field has been updated."
102. Verifikasi Modified By baris `Modifier Probe {runId}-033` menampilkan `Nadia P` sebagai plain text
103. Verifikasi Last Updated baris `Modifier Probe {runId}-033` menampilkan waktu hari uji
104. Verifikasi Last Updated lebih baru dari nilai yang dicatat sebelumnya
105. Hover sel Modified By baris `Modifier Probe {runId}-033`
106. Verifikasi tooltip `Nadia Pratama` tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (106 langkah). Seluruhnya satu kelas (fungsional, hasil Save popup Edit), tiap blok memakai seed bersuffix sendiri atau target Pre-setup yang tidak diubah. Blok akun kedua (TC-GS-UCF-459) berada di akhir dengan langkah ganti akun eksplisit dan tetap bermakna walau blok sebelumnya gagal (Konvensi bagian 3, pemisah "beda akun, role, atau entity" butir b; kedua akun satu entitas Client A dan satu kelas harness). Jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Urutan TC: aksi tanpa perubahan (TC-GS-UCF-126, 127, 128) lebih dulu, lalu aksi yang menyimpan; TC-GS-UCF-99 mendahului TC-GS-UCF-129 dan 130 karena ketiganya memakai field `Edit Meta Final` (prasyarat TC-GS-UCF-129 dan 130 adalah hasil TC-GS-UCF-99 sehingga langkah TC-GS-UCF-99 disalin utuh, S-04).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target; mencatat baseline Last Updated, Modified By, dan jumlah entri Changelog; membuka dan menutup Modal Changelog; kembali ke tab Custom Field dari Detail User; memasang dan melepas intercept; ganti akun. Asersi "tidak ada entri Changelog baru" (TC-GS-UCF-126, 127, 128) memakai baseline jumlah entri (S-12), bukan asersi absence kelas g, karena aksi Save No-Op ada di spec ini (Post Condition tidak diklaim di spec absence).
- Pembagian TC lintas spec: Changelog pencatatan Edit lain (Placeholder, Required, Data Type) ada di spec 067; TC-GS-UCF-284 (absence log No-Op) ada di spec 070 dengan aksi sendiri; TC-GS-UCF-464 (Edit tidak memicu dialog limit, butuh 1.000 field Client Limit) ada di spec 027.
- Temuan untuk QA:
  - TC-GS-UCF-126 dan 127 memakai `Employee Grade` (Pre-setup, Last Updated 10 Sep 2026 14:15) sebagai target Save No-Op; spec tidak mengubahnya (S-06 pengecualian aksi no-op yang dinyatakan di Prerequisites).
  - TC-GS-UCF-126: langkah 1 TC ("catat Last Updated dan jumlah entri Changelog") adalah Precondition tanpa Expected; spec menulisnya sebagai langkah baseline sebelum aksi.
  - TC-GS-UCF-374 memakai token kosong `—` pada Old Value Placeholder, sedangkan TC-GS-UCF-470 dan 106 memakai `-` pada New Value untuk nilai kosong; TC menetapkan token yang berbeda untuk Old dan New Value. Spec mengikuti TC masing-masing; perlu konfirmasi QA apakah token kosong Changelog konsisten (`—` atau `-`).
  - TC-GS-UCF-99, 129, 130 menyebut dependensi TC lain untuk field `Edit Meta Final`; spec menyalin langkah TC-GS-UCF-99 sebagai prasyarat (S-04). TC-GS-UCF-99 mengubah Required menjadi Yes pada field milik spec; dampak ke form Create User dicatat di Prerequisites.
  - TC-GS-UCF-99: Post Condition "Modified By `Sari D`" diasersi lewat Expected b; "nilai User tidak berubah" diasersi lewat Expected c.
  - TC-GS-UCF-459: Last Updated dibandingkan dengan nilai yang dicatat dan dengan waktu hari uji (toleransi satu menit); TC tidak menyebut toleransi.
  - TC-GS-UCF-129: "Tunda respons PATCH 3 detik" ditulis sebagai penahanan respons lewat intercept; nilai 3 detik berasal dari langkah TC.
  - Keputusan NC-14 (No-Op kapitalisasi) dan NC-23 (kolom Field Changelog berprefiks Field Name) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
