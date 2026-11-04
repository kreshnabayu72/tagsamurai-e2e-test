---
id: TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi
title: "Almost Timeout Borrow: Batas Menit H-1 dan Satu Kali per Transaksi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-333
  - TC-FA-NOTIF-334
  - TC-FA-NOTIF-335
  - TC-FA-NOTIF-336
  - TC-FA-NOTIF-337
  - TC-FA-NOTIF-417
coverage:
  web: automated
---

# Almost Timeout Borrow: Batas Menit H-1 dan Satu Kali per Transaksi

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: batas menit job almost_timeout menjadi objek uji.
- Akun aktor pertama Approver (Borrowing & Assignment, Gedung A): Pre-setup #4 (`approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai lewat langkah Ganti akun eksplisit di `## Test Steps`.
- Kemampuan menjalankan job latar (`F-FATX-07`), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di awal tiap TC. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta. Waktu job dihitung dari `cancel_deadline_at` transaksi yang dibaca fixture BE penyetel state sumber saat seed dibuat (bukan diperkirakan dari waktu hook), jam server diset absolut ke nilai itu dikurangi 1 hari ditambah selisih menit pada kolom Waktu job (baris TC-336 memakai −1 jam). Margin terhadap batas hanya satu menit (kurang dari 5 menit) dan dihitung sebagai selisih menit terhadap `cancel_deadline_at` − 1 hari (bagian 8b butir 3).
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (Pre-setup #19). Status transaksi, timeout snapshot, `cancel_deadline_at`, dan penanda pengingat terkirim disiapkan fixture BE penyetel state sumber sebelum tiap TC. Approve transaksi pada TC-FA-NOTIF-337 dikerjakan sesi API Approver (Borrowing & Assignment) Pre-setup #4; verifikasi scan pada TC-FA-NOTIF-417 dikerjakan lewat fixture BE pemicu event.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job, Approve, dan verifikasi scan pada transaksi Pre-setup bersama (BRW-2026-0342) yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar TC; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan, sesudah aksi penyiapan (Approve, verifikasi scan) karena aksi itu bisa menghasilkan notifikasi; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di Dropdown Panel yang sama (status job selesai lewat kueri fixture BE hanya penanda pemicu selesai, bukan anchor absence; bagian 8b butir 2 dan 11; item pembanding adalah item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_APPROVERBA_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.
- Tabel "Kasus tidak dikirim TC-FA-NOTIF-333 dan 336" (urutan baris = urutan iterasi):

  | TC | State | Waktu job |
  |---|---|---|
  | TC-FA-NOTIF-333 | BRW-2026-0342 Waiting for Approval, timeout snapshot 3 hari | `cancel_deadline_at` − 1 hari − 1 menit (selisih −1 menit) |
  | TC-FA-NOTIF-336 | BRW-2026-0342 Waiting for Approval, snapshot batas waktu transaksi 1 hari | `cancel_deadline_at` − 1 jam (mendekati batas) |

- Tabel "Kasus dikirim TC-FA-NOTIF-334 dan 335" (urutan baris = urutan iterasi):

  | TC | State | Waktu job |
  |---|---|---|
  | TC-FA-NOTIF-334 | BRW-2026-0342 Waiting for Approval, timeout snapshot 3 hari | `cancel_deadline_at` − 1 hari + 0 menit (selisih +0 menit) |
  | TC-FA-NOTIF-335 | BRW-2026-0342 Waiting for Approval, timeout snapshot 3 hari | `cancel_deadline_at` − 1 hari + 1 menit (selisih +1 menit) |


## Test Steps


### TC-FA-NOTIF-333 dan TC-FA-NOTIF-336: almost_timeout tidak dikirim

1. Untuk setiap baris tabel "Kasus tidak dikirim TC-FA-NOTIF-333 dan 336" (langkah 1 sampai 11): pulihkan jam server dan jam browser ke waktu nyata
2. Pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
3. Atur jam server dan jam browser ke waktu job pada baris itu
4. Catat jumlah badge Bell icon akun aktor sebagai baseline
5. Jalankan job `F-FATX-07` lewat kemampuan job latar hingga selesai
6. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Klik Bell icon
9. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
10. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor sebagai pembanding
11. Verifikasi Dropdown Panel tidak memuat item ber-Title `Please finish this approval — expiring soon` untuk BRW-2026-0342

### TC-FA-NOTIF-334 dan TC-FA-NOTIF-335: almost_timeout dikirim di dan setelah batas H-1

12. Untuk setiap baris tabel "Kasus dikirim TC-FA-NOTIF-334 dan 335" (langkah 12 sampai 19): pulihkan jam server dan jam browser ke waktu nyata
13. Pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
14. Atur jam server dan jam browser ke waktu job pada baris itu
15. Catat jumlah badge Bell icon akun aktor sebagai baseline
16. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
17. Klik Bell icon
18. Verifikasi badge Bell icon bertambah 1 terhadap baseline
19. Verifikasi item ber-Title `Please finish this approval — expiring soon` dan Body `Request BRW-2026-0342 will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request.` diterima

### TC-FA-NOTIF-337: satu kali per transaksi walau status berpindah

20. Ganti akun: Logout, lalu login sebagai Asset Admin Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`)
21. Buka halaman Fixed Asset > Dashboard
22. Pulihkan jam server dan jam browser ke waktu nyata
23. Pulihkan seed lewat fixture BE pemulih, siapkan BRW-2026-0342 Waiting for Approval yang sudah menerima almost_timeout varian Approver, lalu muat ulang halaman Fixed Asset > Dashboard
24. Approve BRW-2026-0342 lewat sesi API Approver hingga tersimpan sehingga status Ready for Verification dalam jendela 24 jam
25. Catat jumlah badge Bell icon akun aktor sebagai baseline
26. Jalankan job `F-FATX-07` langkah 2 lewat kemampuan job latar hingga selesai
27. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
28. Tunggu 5 detik tanpa memuat ulang halaman
29. Klik Bell icon sebagai PIC pembuat
30. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
31. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor sebagai pembanding
32. Verifikasi Dropdown Panel tidak memuat item ber-Title `Please finish this transaction — expiring soon` untuk BRW-2026-0342

### TC-FA-NOTIF-417: satu kali varian PIC admin walau status berpindah antar-fase pra-komitmen

33. Pulihkan jam server dan jam browser ke waktu nyata
34. Pulihkan seed lewat fixture BE pemulih, siapkan BRW-2026-0342 Ready for Verification dengan timeout snapshot 3 hari, sisa 24 jam, dan pengingat belum pernah dikirim, lalu muat ulang halaman Fixed Asset > Dashboard
35. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `Please finish this transaction — expiring soon` untuk BRW-2026-0342 milik akun aktor sebagai jumlah awal
36. Jalankan job `F-FATX-07` langkah 2 lewat kemampuan job latar hingga selesai
37. Klik Bell icon sebagai PIC pembuat
38. Verifikasi badge Bell icon bertambah 1 terhadap baseline
39. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Please finish this transaction — expiring soon` untuk BRW-2026-0342 milik akun aktor sama dengan jumlah awal langkah 35 + 1
40. Selesaikan verifikasi scan BRW-2026-0342 lewat fixture BE pemicu event hingga status Waiting for Confirmation dalam jendela 24 jam
41. Catat jumlah badge Bell icon akun aktor sebagai baseline kedua
42. Jalankan job `F-FATX-07` langkah 2 lagi lewat kemampuan job latar hingga selesai
43. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
44. Tunggu 5 detik tanpa memuat ulang halaman
45. Verifikasi badge Bell icon sama dengan baseline kedua (selisih 0, tidak ada notifikasi kedua setelah job kedua)
46. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Please finish this transaction — expiring soon` untuk BRW-2026-0342 milik akun aktor tetap sama dengan jumlah awal langkah 35 + 1 (job kedua tidak menambah item)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 11 diulang untuk dua baris tabel "Kasus tidak dikirim TC-FA-NOTIF-333 dan 336" dan langkah 12 sampai 19 untuk dua baris tabel "Kasus dikirim TC-FA-NOTIF-334 dan 335" (65 langkah setelah ekspansi). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi): semua blok satu kelas (batas menit dan satu kali per transaksi untuk job almost_timeout, kelas d), nominalnya 46 langkah, dan tiap blok berdiri sendiri dengan seed dipulihkan.
- Urutan: kasus tidak dikirim dahulu, lalu kasus dikirim (S-10); TC-FA-NOTIF-336 dikelompokkan bersama TC-FA-NOTIF-333 karena hasilnya sama (tidak dikirim). Ganti akun ke Asset Admin sekali untuk TC-FA-NOTIF-337 dan 417 (S-07).
- Langkah penghubung (S-03): langkah 1, 2, 12, 13, 22, 23, 33, dan 34 (pemulihan jam, pemulihan seed, dan penyiapan state; jam server dan jam browser yang digeser TC sebelumnya dipulihkan di awal tiap TC, S-09 dan R-08); "Catat jumlah badge Bell icon" (baseline S-12; pada TC-FA-NOTIF-337 sesudah Approve dan pada TC-FA-NOTIF-417 baseline kedua sesudah verifikasi scan, karena aksi penyiapan itu bisa menghasilkan notifikasi); "Kueri status job" (penanda pemicu selesai, bukan anchor absence; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); Approve lewat sesi API (R-20, "hingga tersimpan").
- Asersi tambahan di luar Expected TC (S-03): pada TC-FA-NOTIF-417 pengamatan sesudah job pertama (langkah 37 sampai 39) memisahkan Expected a dari Expected b supaya tiap Expected punya `Verifikasi` tepat setelah aksinya (R-03); item pembanding Dropdown Panel (langkah 10 dan 31) adalah anchor positif absence (bagian 8b butir 2); badge sama dengan baseline pada kasus tidak dikirim dan badge bertambah 1 pada kasus dikirim, karena Dropdown Panel hanya memuat lima item terbaru dan jumlah notifikasi harus memakai baseline per penerima (bagian 8b butir 10); Body pada TC-FA-NOTIF-334 diasersi selain Title karena Body konstan (jendela nominal 24 hours, lihat Expected TC-FA-NOTIF-335); jumlah item per Title (langkah 39 dan 46) dibaca lewat kemampuan baca BE terhadap jumlah awal langkah 35, bukan hitungan item Dropdown Panel (bagian 8b butir 10).
- Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-336 menulis "mendekati batas" tanpa waktu job eksak; spec memakai `cancel_deadline_at` − 1 jam.
  - TC-FA-NOTIF-337 menulis Role Asset Admin dan TC-FA-NOTIF-333 sampai 336 Approver tanpa nomor Pre-setup; spec memakai Pre-setup #8 dan #4.
  - TC-FA-NOTIF-337 dan 417 tidak menyebut jam job eksak; fixture BE mengatur jam sehingga sisa waktu 24 jam.
  - Post Condition ketujuh TC kosong (`-`); tidak ada yang diasersi.
