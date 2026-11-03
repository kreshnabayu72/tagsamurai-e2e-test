---
id: TC-AC-ACHA-E2E-057-race-commit-timeout-melawan-aksi
title: "Race Commit Timeout Auto-Cancel Melawan Cancel Manual dan Approve"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-447
  - TC-AC-ACHA-448
  - TC-AC-ACHA-449
  - TC-AC-ACHA-450
coverage:
  web: automated
---

# Race Commit Timeout Auto-Cancel Melawan Cancel Manual dan Approve

## Prerequisites

- Mode: FE+BE.
- Kelas harness d (time-travel dan job latar): objek uji adalah urutan commit antara job Timeout Auto-Cancel dan aksi pengguna. Satu sesi browser per blok; dialog atau Review yang dibiarkan terbuka hanya menahan aksi pengguna sampai job commit, bukan konteks kedua kelas c (lihat Notes).
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Dipakai di | Env var password |
|---|---|---|---|---|
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON; aktor hook `before`, pembuat transaksi) | TC-AC-ACHA-447, 448 | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `totalControlDistributor` | #27 | Hendra Wibowo (approver) | TC-AC-ACHA-449, 450 | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |

- Login akun pertama (Budi Santoso) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan jam server.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #14 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00, #63 Approval Timeout 3 day(s).
- Data seeding milik spec (fixture API tim FE/BE; salinan milik spec dari Pre-setup #49 yang dibuat pada T1 oleh MB_ON): transaksi Waiting for Approval (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00), satu salinan baru untuk tiap blok TC. T1 (waktu terbit transaksi) dibaca lewat fixture untuk tiap transaksi.
- Waktu pembuatan salinan: semua blok spec ini menggeser jam server, sehingga tiap salinan dibuat lewat fixture pada langkah pembuka blok (bukan di hook `before`), sesudah jam dipulihkan oleh blok sebelumnya. Dengan begitu geser jam suatu blok tidak membatalkan salinan blok lain, dan tidak ada transaksi Waiting for Approval milik spec ini yang tersisa antar blok. Semua asersi memakai Allocation ID salinan blok. Geser jam tetap membatalkan transaksi Waiting for Approval milik spec lain yang melewati batas; efek itu di luar asersi spec ini.
- Baseline Reserved dan saldo (S-12): tiap blok mencatat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca pada langkah pembuka blok, sesudah salinan dibuat, dan semua asersi saldo dan Reserved berupa selisih terhadap S0 dan R0 (nilai absolut $0.00 dan $20,000.00 tidak dipakai karena transaksi Waiting for Approval lain dapat memegang Reserve).
- Pemulihan (R-08): hook `after` memulihkan jam server, saldo dan Reserved kantong PT Global Distribusi, dan seed 30 baris lewat fixture yang disediakan tim FE/BE; transaksi yang dibuat spec tidak dapat dihapus lewat UI dan audit trail bertambah permanen. Tidak ada Pre-setup bersama yang diubah selain jam server dan saldo/Reserve kantong PT Global Distribusi.
- Kemampuan teknis (disediakan tim FE/BE): pergeseran jam server absolut ke `T1 + 3 hari + 1 menit` lewat fixture yang disediakan tim FE/BE (margin 1 menit terhadap batas Approval Timeout 3 hari dihitung dari T1, bukan dari waktu hook); sesi UI dan API tetap valid saat jam digeser (dinyatakan di `suite.md`); jam browser tidak diubah karena Timeout dihitung murni di server dan tidak diamati lewat hitung mundur UI; jam server dipulihkan segera sesudah job selesai dan sebelum asersi UI berikutnya. Kendali urutan commit dicapai secara deterministik lewat urutan langkah (aksi pengguna ditahan di dialog yang terbuka sampai job commit, atau aksi pengguna commit dulu sebelum jam digeser); menunggu satu siklus job memakai idiom polling: muat ulang List tiap 5 detik sampai status transaksi `Canceled`, batas tunggu 2 menit (untuk kasus Timeout tidak terjadi, polling memakai jeda nyata 30 detik lalu baca status). Fixture baca Reserved dan saldo kantong (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`): jam server dan saldo kantong adalah state global.

## Test Steps

### TC-AC-ACHA-447: Race Cancel manual melawan Timeout: Timeout commit lebih dulu

1. Buat salinan transaksi Waiting for Approval milik MB_ON lewat fixture, lalu catat Allocation ID, T1, saldo (S0) dan Reserved (R0) kantong PT Global Distribusi, serta jumlah entri Allocation Log transaksi itu sebagai baseline blok
2. Klik `Cancel Allocation` pada transaksi itu sehingga dialog konfirmasi terbuka
3. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture (Timeout Auto-Cancel commit lebih dulu)
4. Tunggu satu siklus job dengan memuat ulang data status lewat fixture baca tiap 5 detik sampai status transaksi itu `Canceled` (batas tunggu 2 menit), tanpa menutup dialog
5. Pulihkan jam server ke waktu nyata lewat fixture
6. Klik `[Cancel Allocation]` pada dialog yang sudah terbuka
7. Verifikasi Cancel manual ditolak dengan dialog konflik berjudul "Allocation Changed"
8. Verifikasi body dialog konflik "This allocation was changed by someone else. Please review."
9. Verifikasi footer dialog konflik hanya memuat satu tombol `[OK]`
10. Klik `[OK]` pada dialog konflik
11. Verifikasi dialog tertutup dan List dimuat ulang
12. Baca status, Reserved, dan saldo kantong PT Global Distribusi lewat fixture baca
13. Verifikasi status `Canceled` oleh Timeout
14. Verifikasi Reserved sama dengan R0 dikurangi $250.00 (Release hanya satu kali, tidak ada double-Release)
15. Verifikasi saldo kantong sama dengan S0
16. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
17. Verifikasi Allocation Log memuat entri `Allocation auto-canceled`
18. Verifikasi Allocation Log tidak memuat entri `Allocation canceled by Budi S`
19. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-448: Race Cancel manual melawan Timeout: Cancel manual commit lebih dulu

20. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, lalu catat Allocation ID, T1, saldo (S0) dan Reserved (R0) kantong PT Global Distribusi
21. Klik `Cancel Allocation` pada transaksi itu, lalu konfirmasi sampai toast sukses
22. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture
23. Tunggu satu siklus job dengan jeda nyata 30 detik (Timeout tidak mengubah apa pun sehingga tidak ada perubahan status yang bisa dipolling)
24. Pulihkan jam server ke waktu nyata lewat fixture
25. Muat ulang halaman (F5), buka menu row action `⋯` transaksi itu, dan klik `Allocation Log`
26. Verifikasi Allocation Log memuat entri `Allocation canceled by Budi S` sebagai anchor bahwa halaman termuat
27. Verifikasi Allocation Log tidak memuat entri `Allocation auto-canceled`
28. Tutup modal Allocation Log dengan `[×]`
29. Baca status, Reserved, dan saldo kantong PT Global Distribusi lewat fixture baca
30. Verifikasi Timeout Auto-Cancel tidak mengubah apa pun (guard status): status tetap `Canceled`
31. Verifikasi tidak ada Release kedua: Reserved sama dengan R0 dikurangi $250.00
32. Verifikasi saldo kantong sama dengan S0

### Ganti akun ke Hendra Wibowo

33. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Approvals > Device Allocation

### TC-AC-ACHA-449: Race Approve melawan Timeout: Timeout commit lebih dulu

34. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, lalu catat Allocation ID, T1, saldo (S0) dan Reserved (R0) kantong PT Global Distribusi
35. Buka Review transaksi itu di Approvals > Device Allocation, lalu biarkan terbuka
36. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture (Timeout Auto-Cancel commit lebih dulu)
37. Tunggu satu siklus job dengan memuat ulang data status lewat fixture baca tiap 5 detik sampai status transaksi itu `Canceled` (batas tunggu 2 menit), tanpa menutup Review
38. Pulihkan jam server ke waktu nyata lewat fixture
39. Klik `[Approve]` pada Review yang masih terbuka, lalu konfirmasi
40. Verifikasi Approve ditolak dengan dialog `Request No Longer Available`
41. Verifikasi dialog `Request No Longer Available` mengalihkan ke Tab Active di Approvals
42. Baca status, Reserved, dan saldo kantong PT Global Distribusi lewat fixture baca
43. Verifikasi status `Canceled`
44. Verifikasi Reserved sama dengan R0 dikurangi $250.00
45. Verifikasi tidak ada Capture: saldo kantong sama dengan S0

### TC-AC-ACHA-450: Race Approve melawan Timeout: Approve commit lebih dulu

46. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, lalu catat Allocation ID, T1, saldo (S0) dan Reserved (R0) kantong PT Global Distribusi
47. Buka Approvals > Device Allocation, klik `[Approve]` pada transaksi itu, lalu konfirmasi sampai toast sukses
48. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture
49. Tunggu satu siklus job dengan jeda nyata 30 detik (Timeout tidak mengubah apa pun sehingga tidak ada perubahan status yang bisa dipolling)
50. Pulihkan jam server ke waktu nyata lewat fixture
51. Buka Allocation > Device Allocation, muat ulang halaman (F5), buka menu row action `⋯` transaksi itu, dan klik `Allocation Log`
52. Verifikasi Allocation Log memuat entri `Allocation approved by Hendra W` sebagai anchor bahwa halaman termuat
53. Verifikasi Allocation Log tidak memuat entri `Allocation auto-canceled`
54. Tutup modal Allocation Log dengan `[×]`
55. Baca status, Reserved, dan saldo kantong PT Global Distribusi lewat fixture baca
56. Verifikasi Timeout Auto-Cancel tidak mengubah apa pun: status tetap `Completed`
57. Verifikasi tidak ada Release: Reserved sama dengan R0 dikurangi $250.00 (dikonsumsi Capture dari Approve)
58. Verifikasi saldo kantong sama dengan S0 dikurangi $250.00 (Capture dari Approve)

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 9b). Subjudul `###` memetakan langkah ke id TC granular.
- Kelas d (time-travel dan job latar) satu spec: objek uji tiap TC adalah urutan commit job Timeout melawan aksi pengguna dalam satu sesi browser per blok; tidak ada konteks UI kedua yang menjadi objek asersi, sehingga tidak ada campuran dengan kelas c dan tidak ada pengecualian yang perlu dicatat.
- Kendali urutan commit: kemampuan fixture jam server dan baca status disediakan tim FE/BE; urutan dijamin lewat urutan langkah, bukan kendali internal job.
- Pengecualian P-2 tidak dipakai: jam server digeser sebagai langkah eksplisit karena bagian dari skenario race; dipulihkan sebelum asersi UI (S-09).
- Langkah penghubung (S-03): langkah catat baseline Allocation Log, langkah menunggu siklus job (polling 5 detik, batas 2 menit, atau jeda nyata 30 detik untuk kasus Timeout tidak mengubah apa pun, bagian 6 konvensi), langkah memulihkan jam server, langkah memuat ulang List dan membuka Allocation Log, tutup modal Allocation Log, langkah ganti akun (S-07).
- Anchor absence (bagian 8b butir 2): asersi "tidak memuat entri `Allocation auto-canceled`" pada TC-AC-ACHA-448 dan 450 didahului `Verifikasi` entri milik aksi yang menang (entri Cancel manual atau Approve) pada modal Allocation Log yang sama.
- Pengecualian S-12 nama literal (Lampiran A butir A-6): Notes `Batch uji` ditulis persis seperti TC.
- Baris target (R-16): transaksi di List (Cancel, Allocation Log) ditemukan lewat Search Allocation ID yang dicatat saat fixture sebagai langkah penghubung tanpa `Verifikasi`; langkah ini tidak diberi nomor sendiri.
- Langkah pembuka blok (membuat salinan dan mencatat baseline S0, R0) adalah langkah penghubung tanpa `Verifikasi`; geser jam server pada tiap blok dipulihkan sebelum blok berikutnya membuat salinan (S-09).
- Ukuran spec: 58 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu topik (race commit Timeout) dan tiap blok memakai transaksi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pergeseran dan pemulihan jam, polling job, dan pembacaan state menambah langkah tanpa verifikasi.
- Temuan untuk QA:
  - TC-AC-ACHA-447, 449 (dan 448, 450) bergantung pada interval pengecekan job Timeout yang tidak ditulis PRD (Catatan TC); polling 2 menit adalah pilihan spec.
  - TC-AC-ACHA-448 dan 450 mengasersi tidak adanya efek job Timeout; tidak ada sinyal teramati kapan job selesai, sehingga spec memakai jeda nyata 30 detik (bagian 6 konvensi).
  - TC-AC-ACHA-447 a menyebut dialog konflik berjudul "Allocation Changed" yang merupakan inferensi dari pola sibling `Device Changed` (Catatan TC: bukan kata user); ganti bila judul lain dikehendaki.
  - TC-AC-ACHA-449 a menyebut dialog `Request No Longer Available` tanpa isi dan tombol.
  - TC-AC-ACHA-450 tidak menyebut nilai saldo; spec mengasersi selisih terhadap saldo awal blok.
  - TC-AC-ACHA-447 sampai 450 mengandaikan hanya satu transaksi Waiting for Approval memegang Reserve dan tidak menyatakan efek job Timeout global terhadap transaksi lain; spec mengasersi selisih terhadap baseline S0 dan R0 per blok.
  - Post Condition TC-AC-ACHA-447 sampai 450 ("-") tidak ada.
