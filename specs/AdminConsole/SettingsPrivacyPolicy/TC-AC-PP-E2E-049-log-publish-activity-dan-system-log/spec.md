---
id: TC-AC-PP-E2E-049-log-publish-activity-dan-system-log
title: "Entri Log Publish pada Activity Log dan System Log Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-154
  - TC-AC-PP-155
  - TC-AC-PP-157
  - TC-AC-PP-162
  - TC-AC-PP-164
coverage:
  web: automated
---

# Entri Log Publish pada Activity Log dan System Log Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`) sebagai aktor Publish dan pembaca Activity Log serta System Log di Settings > User > Detail. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat A (Version 3 Active, John Doe, 10 Aug 2026; Version 2; Version 1). Hook `before` men-seed Riwayat A lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI). Antar-TC dataset dikembalikan ke Riwayat A lewat Fixture BE, hook `after` mengembalikan ke Riwayat A. Entri log yang dibuat spec tidak dapat dihapus lewat UI.
- Baseline log (S-12): sebelum tiap Publish, jumlah entri dan penanda entri teratas dengan Object `Privacy Policy` pada Activity Log dan System Log `Andi Wijaya` dicatat; untuk TC-157 dicatat juga jumlah seluruh entri (semua Object) pada kedua surface. Asersi "entri baru" membandingkan dengan baseline itu.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide dan spec membuat versi baru.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-154: Publish menulis entri pada System Log di Detail User milik aktor

1. Catat baseline: buka Settings > User > Detail `Andi Wijaya` > Tab System Log, catat jumlah entri dengan Object `Privacy Policy` dan entri teratas
2. Buka Settings > Privacy Policy lewat sidebar
3. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
4. Klik di akhir konten editor lalu ketik " Log case."
5. Klik `[Publish New Version]`
6. Klik `[Publish]` pada Dialog Publish Confirm
7. Verifikasi tabel menampilkan `Version 4` berbadge `Active` di baris teratas
8. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
9. Verifikasi jumlah entri dengan Object `Privacy Policy` bertambah satu dari baseline
10. Verifikasi entri teratas: Action `Publish`
11. Verifikasi entri teratas: Object `Privacy Policy`
12. Verifikasi entri teratas: Field `Content`
13. Verifikasi entri teratas: New Value `Version 4`
14. Verifikasi entri teratas: Date sesuai format General Settings
15. Verifikasi kolom Action, Old Value, dan New Value tampil plain text tanpa badge berwarna
16. Verifikasi entri teratas: Name `Version 4`
17. Verifikasi entri teratas: Old Value `Version 3`

### TC-AC-PP-155: Publish menulis entri pada Activity Log dengan Modified By berformat singkat dan tooltip nama lengkap

18. Kembalikan dataset ke Riwayat A lewat Fixture BE
19. Catat baseline: buka Activity Log (Admin Console), catat jumlah entri dengan Object `Privacy Policy` dan entri teratas
20. Buka Settings > Privacy Policy lewat sidebar
21. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
22. Klik di akhir konten editor lalu ketik " Activity case."
23. Klik `[Publish New Version]`
24. Klik `[Publish]` pada Dialog Publish Confirm
25. Verifikasi tabel menampilkan `Version 4` berbadge `Active` di baris teratas
26. Buka Activity Log (Admin Console) dan cari entri teratas dengan Object `Privacy Policy`
27. Verifikasi jumlah entri dengan Object `Privacy Policy` bertambah satu dari baseline
28. Verifikasi entri: Action `Publish`
29. Verifikasi entri: Object `Privacy Policy`
30. Verifikasi entri: Field `Content`
31. Verifikasi entri: New Value `Version 4`
32. Verifikasi Modified By tampil `Andi W` sebagai plain text
33. Hover nilai Modified By
34. Verifikasi tooltip `Andi Wijaya`
35. Verifikasi Action tampil plain text tanpa badge
36. Verifikasi entri: Name `Version 4`
37. Verifikasi entri: Old Value `Version 3`

### TC-AC-PP-164: Entri log Publish terlihat pada surface setelah Publish selesai

38. Kembalikan dataset ke Riwayat A lewat Fixture BE
39. Catat baseline: buka Activity Log (Admin Console), catat jumlah entri dengan Object `Privacy Policy` dan entri teratas sebagai penanda baseline
40. Buka Settings > Privacy Policy lewat sidebar
41. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
42. Klik di akhir konten editor lalu ketik " Timing."
43. Klik `[Publish New Version]`
44. Klik `[Publish]` pada Dialog Publish Confirm
45. Verifikasi tabel menampilkan `Version 4` berbadge `Active` di baris teratas
46. Segera buka Activity Log (tanpa menunggu atau reload tambahan) dan cari entri teratas dengan Object `Privacy Policy` di atas penanda baseline
47. Verifikasi jumlah entri dengan Object `Privacy Policy` bertambah satu dari baseline
48. Verifikasi entri `Publish` untuk `Version 4` sudah terlihat pada Activity Log segera setelah Publish selesai
49. Verifikasi entri baru teratas: Name `Version 4`
50. Verifikasi entri baru teratas: Old Value `Version 3`
51. Verifikasi entri baru teratas: New Value `Version 4`

### TC-AC-PP-157: Satu Publish menghasilkan tepat satu entri pada tiap surface tanpa duplikat dan tanpa entri evaluasi consent

52. Kembalikan dataset ke Riwayat A lewat Fixture BE
53. Catat baseline: buka Activity Log (Admin Console) dan System Log `Andi Wijaya`, catat pada masing-masing surface jumlah entri dengan Object `Privacy Policy` dan jumlah seluruh entri (semua Object)
54. Buka Settings > Privacy Policy lewat sidebar
55. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
56. Klik di akhir konten editor lalu ketik " Single entry."
57. Klik `[Publish New Version]`
58. Klik `[Publish]` pada Dialog Publish Confirm
59. Verifikasi tabel menampilkan `Version 4` berbadge `Active` di baris teratas
60. Buka Activity Log (Admin Console) dan hitung entri baru dengan Object `Privacy Policy`
61. Verifikasi Activity Log bertambah tepat 1 entri (`Publish`, `Version 4`)
62. Hitung jumlah seluruh entri (semua Object) pada Activity Log dan bandingkan dengan baseline langkah 53
63. Verifikasi tidak ada entri tambahan terkait evaluasi persetujuan pengguna (consent) pada Activity Log: jumlah seluruh entri (semua Object) bertambah tepat 1 dari baseline
64. Buka System Log `Andi Wijaya` dan hitung entri baru dengan Object `Privacy Policy`
65. Verifikasi System Log `Andi Wijaya` bertambah tepat 1 entri
66. Hitung jumlah seluruh entri (semua Object) pada System Log `Andi Wijaya` dan bandingkan dengan baseline langkah 53
67. Verifikasi tidak ada entri tambahan terkait evaluasi persetujuan pengguna (consent) pada System Log `Andi Wijaya`: jumlah seluruh entri (semua Object) bertambah tepat 1 dari baseline

### TC-AC-PP-162: Entri log lama tidak berubah setelah Publish berikutnya

68. Kembalikan dataset ke Riwayat A lewat Fixture BE
69. Catat baseline: buka Activity Log (Admin Console), catat jumlah entri dengan Object `Privacy Policy` dan entri teratas sebagai penanda baseline
70. Buka Settings > Privacy Policy lewat sidebar
71. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
72. Klik di akhir konten editor lalu ketik " Immutable A."
73. Klik `[Publish New Version]`
74. Klik `[Publish]` pada Dialog Publish Confirm
75. Verifikasi tabel menampilkan `Version 4` berbadge `Active` di baris teratas
76. Buka Activity Log (Admin Console) dan catat entri baru teratas di atas penanda baseline (Name, Old Value, New Value) sebagai entri `Version 4`
77. Buka Settings > Privacy Policy lewat sidebar
78. Klik `[⋯]` pada baris `Version 4` lalu pilih `Edit`, tunggu konten termuat
79. Klik di akhir konten editor lalu ketik " Immutable B."
80. Klik `[Publish New Version]`
81. Klik `[Publish]` pada Dialog Publish Confirm
82. Verifikasi tabel menampilkan `Version 5` berbadge `Active` di baris teratas
83. Buka Activity Log (Admin Console) dan identifikasi dua entri baru di atas penanda baseline: entri `Version 5` (teratas) dan entri `Version 4` (tepat di bawahnya, yang dicatat di langkah 76)
84. Verifikasi entri `Version 4` (kedua dari atas) tetap berisi New Value `Version 4` dan tidak berubah dari catatan langkah 76
85. Verifikasi entri `Version 5` (teratas) berisi New Value `Version 5`
86. Verifikasi entri `Version 5` (teratas): Name `Version 5`
87. Verifikasi entri `Version 5` (teratas): Old Value `Version 4`
88. Verifikasi entri `Version 4` (kedua dari atas): Name `Version 4`
89. Verifikasi entri `Version 4` (kedua dari atas): Old Value `Version 3`


## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec ini 154, 155, 164, 157, 162 (TC sumber 154, 155, 157, 162, 164). TC-162 dipindah ke akhir karena melakukan dua Publish berturut-turut (membuat Version 4 dan 5), sehingga membuat jumlah entri awal TC lain lebih mudah dibaca; TC-164 didahulukan karena asersi waktu (entri langsung terlihat) paling jelas ketika dataset baru saja dikembalikan (S-05, S-10).
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09, S-12): langkah 1, 19, 39, 53, 69 (catat baseline entri: jumlah entri dan penanda entri teratas; langkah 53 mencatat juga jumlah seluruh entri semua Object), langkah 18, 38, 52, 68 (kembalikan dataset ke Riwayat A lewat Fixture BE, sesuai Catatan TC bahwa dataset dibuat ulang per TC), langkah 77 (buka halaman kembali), langkah 62 dan 66 (hitung jumlah seluruh entri semua Object; langkah baca). Dataset dikembalikan antar-TC sehingga Version 4 pada tiap TC identik dengan Expected TC.
- TC-157 Expected c ("tidak ada entri tambahan terkait evaluasi consent") diasersi pada langkah 63 (Activity Log) dan 67 (System Log `Andi Wijaya`) lewat baseline jumlah seluruh entri semua Object (langkah 53): bertambah tepat 1 berarti tidak ada entri consent atau entri lain selain `Publish`; ini asersi jumlah (bukan kelas g, konvensi bagian 3). Hitungan entri ber-Object `Privacy Policy` pada langkah 61 dan 65 tetap dipakai untuk Expected a dan b. Asersi absence murni untuk aksi yang tidak mencatat log (View, Search, Download, Publish gagal, Version 1 seed) ada di spec absence log (spec 051, TC-AC-PP-158, 159, 160).
- Penyimpangan kecil dari TC: TC-157 langkah 2 dan 3 TC sumber (hitung entri) dituliskan sebagai langkah baca setelah Publish dengan baseline sebelumnya (S-12); TC-162 langkah 2 ("catat entri log") diwujudkan sebagai langkah 76, dengan entri baru diidentifikasi lewat baseline langkah 69 (entri baru di atas penanda baseline), bukan lewat Name saja, karena entri `Version 4` dari TC sebelumnya tetap ada (log tidak bisa dihapus lewat UI; S-12).
- Temuan untuk QA: precondition TC-157 menyebut jumlah awal entri "tercatat" tanpa menentukan cara pencatatan; spec memakai baseline jumlah entri dengan Object `Privacy Policy` (langkah 53). TC-164 dan TC-162 mengidentifikasi entri hanya lewat Name `Version 4` padahal entri `Version 4` dari TC sebelumnya tetap ada di log; spec memakai baseline (penanda entri teratas) untuk menemukan entri baru, dan perbaikan di TC (Precondition mencatat baseline, Expected "entri baru teratas") diserahkan ke pemilik TC. TC-162 langkah 3 menyebut Publish "dengan menambah ' Immutable B.'" pada konten Active yang baru; spec memakai Edit dari baris `Version 4` (konten Active setelah Publish pertama).
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi tabel menampilkan Version 4 (5) berbadge Active` (langkah 7, 25, 45, 59, 75, 82) menjadi sinyal bahwa Publish selesai sebelum log dibaca, dan `Verifikasi jumlah entri ... bertambah satu dari baseline` (langkah 9, 27, 47) memastikan entri yang diasersi adalah entri baru dari Publish ini (S-12). Keduanya tidak mengganti Expected TC.
- Spec membuat versi baru dan entri log (tidak dapat dihapus lewat UI); dataset dipulihkan ke Riwayat A di hook `after`.
- Panjang spec (89 langkah) melewati perkiraan 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
