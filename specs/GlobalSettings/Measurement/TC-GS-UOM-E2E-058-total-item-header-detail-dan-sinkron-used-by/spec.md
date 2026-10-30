---
id: TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by
title: "Total Item di Header Unit Detail: Client, Principal, Nol, Relasi Nonaktif, Recycle Bin, dan Perubahan Relasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-387
  - TC-GS-UOM-388
  - TC-GS-UOM-389
  - TC-GS-UOM-390
  - TC-GS-UOM-393
  - TC-GS-UOM-394
coverage:
  web: automated
tags: [principal]
---

# Total Item di Header Unit Detail: Client, Principal, Nol, Relasi Nonaktif, Recycle Bin, dan Perubahan Relasi

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai (dengan langkah ganti akun eksplisit):
  - Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Akun aktor pertama dan akun default suite: login di hook `before` suite. Dipakai langkah 1 sampai 56.
  - Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login lewat UI di langkah 58. Dipakai langkah 58 sampai 67.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite untuk akun aktor suite (lihat bagian "Hook suite" di `suite.md`); untuk akun Principal, mekanisme penyetelan flag disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`). Hook `after` mengembalikan sesi ke akun default suite bila spec berakhir di akun Principal.
- Data Pre-setup (tetap di environment, hanya dibaca):
  - Client A: `Box` (Symbol `box`; Used By (Items) `4`; referensi FAMS Asset Name `Storage Box A`, `Storage Box B`, `Storage Box C`, `Storage Box D`, tiga di antaranya aktif dan satu nonaktif untuk TC-GS-UOM-393; asset name yang nonaktif tidak disebut TC). `Liter` (Symbol `L`; bebas relasi; Used By (Items) `0`). `Box` hanya dibaca; Delete `Box` pada TC-GS-UOM-393 diblokir guard dan tidak mengubah data (pengecualian S-06 untuk baris in-use yang aksinya ditolak).
  - Principal: `Ampere` (Symbol `A`; Used By (Items) `3`: Asset Name FAMS `Power Meter`, Item Name Supply `Battery Pack`, Device Name `Fixed Reader`). Referensi Supply (SAMS) disiapkan lewat fixture backend (NC-09), disediakan tim FE.
- Seeding (hook `before`, lewat API oleh Sari Dewi; unit milik spec menggantikan unit Pre-setup yang akan diubah relasinya atau dihapus, S-06):
  - `Meter Uji {runId}-058` (Symbol `mu`), bebas relasi (Used By (Items) `0`); menggantikan `Meter` pada TC-GS-UOM-390.
  - `Peti {runId}-058` (Symbol `pt`), yang hanya direferensikan satu Asset Name FAMS yang sudah berada di Recycle Bin; menggantikan `Box` pada TC-GS-UOM-394. Pembuatan Asset Name dan pemindahannya ke Recycle Bin: disediakan tim FE (fixture backend; TC tidak menyebut mekanismenya).
- Pemicu TC-GS-UOM-390 (langkah 29 dan 37, bukan objek asersi): membuat dan menghapus Asset Name FAMS `Ruler {runId}-058` yang memakai `Meter Uji {runId}-058`; kemampuan FAMS ini disediakan tim FE (TC menyebut "Di FAMS, buat Asset Name").
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Meter Uji {runId}-058` dan `Peti {runId}-058` lewat API; hapus Asset Name FAMS `Ruler {runId}-058` dan Asset Name Recycle Bin milik `Peti` bila masih ada (disediakan tim FE). Last Updated baris Pre-setup tidak berubah.
- Kemampuan teknis: login/logout dalam satu spec (Client A ke Principal); klik angka Used By (Items) untuk membuka Detail; muat ulang halaman; membaca Last Updated baris tabel; hook `after` logout dan login ulang sebagai akun default suite.
- Precondition TC-GS-UOM-387, 389, 390, 393, 394: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement. TC-GS-UOM-388: login sebagai Total Control (Principal).

## Test Steps

### TC-GS-UOM-387: Header Total Item tampil di Modal Unit Detail (Client) dan sama dengan Used By (Items)

1. Ketik Search `Box`, tekan Enter
2. Catat angka Used By (Items) pada baris dengan Unit Name `Box`
3. Klik angka Used By (Items) pada baris `Box`
4. Verifikasi General Info menampilkan `Total Item` `4`
5. Verifikasi `Total Item` pada General Info Card sebaris dengan Unit Name
6. Verifikasi `Total Item` read-only (tidak dapat diedit)
7. Verifikasi Item Type List memuat 4 baris
8. Verifikasi accordion `Device Name List` tidak dirender (instance Client)
9. Verifikasi `Total Item` sama dengan angka Used By (Items) yang dicatat pada langkah 2
10. Klik `[✕]`

### TC-GS-UOM-393: Total Item dan Used By (Items) menghitung relasi nonaktif

11. Verifikasi Used By (Items) baris `Box` bernilai `4`
12. Klik angka Used By (Items) pada baris `Box`
13. Verifikasi `Total Item` bernilai `4`
14. Verifikasi Asset Name nonaktif tampil di Item Type List
15. Klik `[✕]`
16. Klik `⋯` pada baris `Box`
17. Klik Delete
18. Verifikasi Delete diblokir (dialog pemblokiran in-use tampil, bukan dialog konfirmasi biasa)
19. Tutup dialog pemblokiran

### TC-GS-UOM-389: Total Item bernilai 0 saat tanpa relasi

20. Ganti isi kotak search dengan `Liter`, tekan Enter
21. Klik `⋯` pada baris `Liter`
22. Klik Detail
23. Verifikasi `Total Item` bernilai `0` (bukan `—`)
24. Verifikasi accordion Item Type List menampilkan empty state Title `No item types linked`
25. Verifikasi accordion `Device Name List` tidak dirender (instance Client)
26. Klik `[✕]`

### TC-GS-UOM-390: Total Item dan Used By (Items) ikut berubah setelah relasi konsumen bertambah dan berkurang

27. Ganti isi kotak search dengan `Meter Uji {runId}-058`, tekan Enter
28. Catat Last Updated baris `Meter Uji {runId}-058`
29. Di FAMS, buat Asset Name `Ruler {runId}-058` yang memakai `Meter Uji {runId}-058` (pemicu)
30. Muat ulang halaman (F5)
31. Ketik Search `Meter Uji {runId}-058`, tekan Enter
32. Verifikasi Used By (Items) baris `Meter Uji {runId}-058` bernilai `1`
33. Klik angka Used By (Items) pada baris `Meter Uji {runId}-058`
34. Verifikasi `Total Item` bernilai `1`
35. Verifikasi Item Type List memuat satu baris `Ruler {runId}-058` (Fixed Asset)
36. Klik `[✕]`
37. Di FAMS, hapus Asset Name `Ruler {runId}-058` (pemicu)
38. Muat ulang halaman (F5)
39. Ketik Search `Meter Uji {runId}-058`, tekan Enter
40. Verifikasi Used By (Items) baris `Meter Uji {runId}-058` kembali `0`
41. Verifikasi Last Updated baris `Meter Uji {runId}-058` tidak berubah dari catatan langkah 28
42. Klik `⋯` pada baris `Meter Uji {runId}-058`
43. Klik Detail
44. Verifikasi `Total Item` kembali `0`
45. Klik `[✕]`

### TC-GS-UOM-394: Relasi di Recycle Bin tidak dihitung Total Item dan Used By (Items)

46. Ganti isi kotak search dengan `Peti {runId}-058`, tekan Enter
47. Verifikasi Used By (Items) baris `Peti {runId}-058` bernilai `0`
48. Klik `⋯` pada baris `Peti {runId}-058`
49. Klik Detail
50. Verifikasi `Total Item` bernilai `0`
51. Verifikasi Item Type List menampilkan empty state Title `No item types linked`
52. Klik `[✕]`
53. Klik `⋯` pada baris `Peti {runId}-058`
54. Klik Delete
55. Verifikasi dialog konfirmasi Delete biasa tampil (Delete tidak diblokir)
56. Klik `[Cancel]` pada dialog konfirmasi

### Ganti akun ke Total Control (Principal)

57. Logout dari akun Total Control Client A
58. Login sebagai Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`
59. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-388: Total Item Principal = baris Item Type + Device Name dan sama dengan Used By (Items)

60. Ketik Search `Ampere`, tekan Enter
61. Catat angka Used By (Items) pada baris `Ampere`
62. Klik `⋯` pada baris `Ampere`
63. Klik Detail
64. Hitung baris Item Type List dan Device Name List
65. Verifikasi `Total Item` bernilai `3`
66. Verifikasi Item Type List memuat 2 baris dan Device Name List memuat 1 baris (2 + 1 = 3)
67. Verifikasi `Total Item` sama dengan angka Used By (Items) Ampere yang dicatat pada langkah 61 (`3`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-387, 393 (Box), 389, 390, 394, lalu (Principal) 388. Alasan: TC yang hanya membaca di awal; TC-GS-UOM-390 mengubah relasi konsumen (pemicu) dan dipulihkan di langkah 37; TC-GS-UOM-394 menutup dengan dialog Delete yang dibatalkan (tidak menghapus data) sehingga tidak ada aksi destruktif; ganti akun ke Principal di akhir.
- Ganti akun (butir b prinsip "Beda akun" konvensi 3): TC-GS-UOM-388 berdiri sendiri sesudah login Principal dan tetap bermakna walau bagian Client A gagal.
- Pembagian TC lintas spec: Used By (Items) sebagai link dan kecocokan dengan Total Item per instance ada di `TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance`; spec ini memegang header Total Item di Detail, kasus nol, relasi nonaktif, Recycle Bin, dan perubahan relasi. TC-GS-UOM-390 (Last Updated tidak berubah saat relasi konsumen berubah) ada di spec ini dengan baseline Last Updated langkah 28 (pembagian lintas spec dengan spec 065 untuk TC-GS-UOM-225 dan 330).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 20, 27, 31, 39, 46, 60 (Search untuk menemukan baris target), langkah 10, 15, 26, 36, 45, 52 (menutup modal), langkah 19 dan 56 (menutup dialog), langkah 30 dan 38 (muat ulang tabel sesuai langkah TC), langkah 57 sampai 59 (ganti akun; hook `after` memulihkan sesi).
- Langkah 11 mengasersi Used By (Items) `Box` `4` sebagai Expected a TC-GS-UOM-393. Langkah 56 membatalkan dialog sehingga `Peti {runId}-058` tidak terhapus; hook `after` yang membersihkannya.
- Spec ini melewati sekitar 35 langkah (67 langkah). Alasan: semua blok satu kelas harness (fungsional, pembacaan Total Item pada Modal Unit Detail) dengan data Pre-setup dan dua unit seeding; bagian Client A berbagi login dan layar awal, sedangkan bagian Principal berdiri sendiri sesudah ganti akun. Pemisahan hanya menambah login dan seeding berulang.
- Temuan untuk QA:
  - TC-GS-UOM-390 menargetkan unit `Meter` (Pre-setup) dengan Delete relasi di FAMS; spec memakai `Meter Uji {runId}-058` (S-06) dengan baseline Last Updated sendiri. TC tidak menyebut mekanisme membuat dan menghapus Asset Name di FAMS (kemampuan disediakan tim FE).
  - TC-GS-UOM-394 menyebut `Box` hanya direferensikan satu Asset Name di Recycle Bin dan memerintahkan Delete `Box`, yang bertentangan dengan Pre-setup `Box` (Used By (Items) `4`, dipakai TC-GS-UOM-387 dan 393) dan dengan S-06 (tidak mengedit atau menghapus baris Pre-setup). Spec memakai `Peti {runId}-058` dan membatalkan dialog Delete; TC tidak menyebut apakah Delete dikonfirmasi.
  - TC-GS-UOM-393 menyebut 3 Asset Name aktif dan 1 nonaktif untuk `Box` tanpa menyebut Asset Name mana yang nonaktif dan cara menyiapkannya; Pre-setup TC hanya menyebut `Storage Box A, B, C, D`. Teks dan cara menutup dialog pemblokiran Delete juga tidak disebut TC.
  - TC-GS-UOM-394 Expected c menyebut "dialog konfirmasi biasa" tanpa judul dan isi; spec mengasersi dialog konfirmasi Delete tampil dan bukan dialog pemblokiran.
  - TC-GS-UOM-387 Expected a menyebut `Total Item` "sebaris dengan Unit Name" pada General Info Card; spec mengasersi seperti tertulis tanpa menambah kriteria posisi.
