---
id: TC-FA-FAAC-E2E-097-aksi-asset-name-pada-asset-class-dihapus-pengguna-lain
title: "Aksi Assign, Move, dan Unassign Asset Name pada Asset Class yang Dihapus Pengguna Lain"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-170
  - TC-FA-FAAC-213
  - TC-FA-FAAC-240
  - TC-FA-FAAC-241
coverage:
  web: automated
---

# Aksi Assign, Move, dan Unassign Asset Name pada Asset Class yang Dihapus Pengguna Lain

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Temp Equipment` (`TEMP-EQ`) tanpa Asset Name beserta Asset Name `Meeting Table` tanpa Asset Class (TC-170); `TEMP-EQ` dengan Asset Name ter-assign `Scrap Bin` (0 aset aktif) dan Asset Class tujuan Active `Machinery` (`MACHINERY`) serta `Vehicles` (`VEHICLES`), dengan `Office Equipment (Legacy)` (`OFFICE-OLD`) Inactive (TC-213 dan TC-240); Asset Class Active `Temp Equipment 2` (`TEMP-EQ2`) dengan Asset Name `Scrap Bin 2` dan `Scrap Bin 3` (0 aset aktif) (TC-241).
- Pelaku kedua: sesi API aktor (kemampuan suite, lihat suite.md): menghapus `TEMP-EQ` atau `TEMP-EQ2` lewat fixture BE, bukan sesi UI kedua. State BE (Asset Name tidak ter-assign atau tidak berpindah) dibaca lewat kemampuan baca fixture BE yang disediakan tim FE/BE.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: `TEMP-EQ` dan `TEMP-EQ2` dibuat ulang beserta Asset Name-nya. Karena `TEMP-EQ` terhapus di setiap TC, fixture BE memulihkannya sebagai langkah penghubung sebelum TC-213 dan TC-240 (dengan `Scrap Bin`).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-170: Assign pada Asset Class yang sudah dihapus pengguna lain menampilkan toast netral

1. Ketik Search `TEMP-EQ`, tekan Enter
2. Buka Detail `Temp Equipment` tab `Asset Names`
3. Klik tombol `+ Assign Asset Names`
4. Centang `Meeting Table`
5. Lewat sesi API aktor, hapus Asset Class `Temp Equipment` hingga penghapusan tersimpan
6. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
7. Klik `[Assign]`
8. Verifikasi toast netral (info) `This asset class is no longer available.`
9. Verifikasi Asset Name `Meeting Table` tidak ter-assign (dibaca lewat fixture BE)
10. Verifikasi halaman Detail kembali ke tabel Asset Class yang disegarkan
11. Verifikasi `Temp Equipment` tidak ada di tabel
12. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-213: Move pada Asset Class asal yang sudah dihapus pengguna lain menampilkan toast netral

13. Pulihkan `TEMP-EQ` dengan Asset Name `Scrap Bin` lewat fixture BE hingga tersimpan, lalu muat ulang tabel
14. Ketik Search `TEMP-EQ`, tekan Enter
15. Buka Detail `Temp Equipment` (`TEMP-EQ`) pada tab `Asset Names`
16. Klik ikon `⋯` pada baris `Scrap Bin`, lalu pilih `Move`
17. Pilih `Destination Asset Class` = `MACHINERY – Machinery`
18. Lewat sesi API aktor, hapus Asset Class `Temp Equipment` hingga penghapusan tersimpan
19. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
20. Klik `[Move]`
21. Verifikasi toast netral (info) `This asset class is no longer available.`
22. Verifikasi `Scrap Bin` tidak berpindah ke `MACHINERY` (dibaca lewat fixture BE)
23. Verifikasi halaman Detail kembali ke tabel Asset Class yang disegarkan
24. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-240: Unassign pada Asset Class yang sudah dihapus pengguna lain menampilkan toast netral

25. Pulihkan `TEMP-EQ` dengan Asset Name `Scrap Bin` lewat fixture BE hingga tersimpan, lalu muat ulang tabel
26. Ketik Search `TEMP-EQ`, tekan Enter
27. Buka Detail `Temp Equipment` (`TEMP-EQ`) pada tab `Asset Names`
28. Klik ikon `⋯` pada baris `Scrap Bin`, lalu pilih `Unassign`
29. Lewat sesi API aktor, hapus Asset Class `Temp Equipment` hingga penghapusan tersimpan
30. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
31. Klik `[Unassign]`
32. Verifikasi toast netral (info) `This asset class is no longer available.`
33. Verifikasi halaman Detail kembali ke tabel Asset Class yang disegarkan
34. Verifikasi `Scrap Bin` tidak berubah (dibaca lewat fixture BE)
35. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-241: Unassign massal saat seluruh Asset Class sudah dihapus pengguna lain hanya menampilkan toast netral

36. Ganti isi kotak search dengan `TEMP-EQ2`, tekan Enter
37. Buka Detail `Temp Equipment 2` (`TEMP-EQ2`) pada tab `Asset Names`
38. Centang baris `Scrap Bin 2` dan `Scrap Bin 3`, lalu klik `Bulk Action` dan pilih `Unassign`
39. Lewat sesi API aktor, hapus Asset Class `Temp Equipment 2` hingga penghapusan tersimpan
40. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
41. Klik `[Unassign]` pada dialog
42. Verifikasi hanya toast netral (info) `This asset class is no longer available.` yang tampil
43. Verifikasi tidak ada toast sukses yang tampil
44. Verifikasi halaman Detail kembali ke tabel Asset Class yang disegarkan
45. Verifikasi `Scrap Bin 2` dan `Scrap Bin 3` tetap ter-assign (dibaca lewat fixture BE)
46. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
47. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: Assign (TC-170), Move (TC-213), Unassign single (TC-240), lalu Unassign massal (TC-241); tiap TC menghapus `TEMP-EQ` atau `TEMP-EQ2` sehingga fixture BE memulihkannya sebelum TC berikutnya.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 14, 26, dan 36 (Search untuk menemukan baris target, R-16; langkah 14 dan 26 sesudah muat ulang tabel), langkah 2, 15, 27, dan 37 (membuka Detail dari hasil Search), langkah 13 dan 25 (memulihkan `TEMP-EQ`), langkah 6, 19, 30, dan 40 (baseline Changelog, S-12), dan langkah 47 (mengosongkan Search). Langkah 5, 18, 29, dan 39 adalah pemicu pelaku kedua lewat sesi API (bukan kelas c; tidak memakai P-2).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal yang dihapus oleh aksi TC; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. S-05 dan P-1: Expected "tanpa log" pada TC-170, TC-213, TC-240, dan TC-241 diasersi di spec ini (langkah 12, 24, 35, dan 46) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class. Baseline dicatat sesudah penghapusan oleh sesi API aktor, sehingga entri Delete milik aktor tidak terhitung.
5. Alasan melebihi sekitar 35 langkah (47 langkah): spec berisi empat blok TC yang berdiri sendiri pada `TEMP-EQ` atau `TEMP-EQ2` yang dipulihkan fixture BE sebelum tiap blok dan satu topik aksi (aksi Asset Name atas Asset Class yang dihapus pengguna lain); kegagalan satu blok tidak membuat blok lain kehilangan makna.
6. Temuan untuk QA: Langkah TC-213 nomor 4 berbunyi "hapus Asset Class 'Temp Equipment' setelah memindahkan 'Scrap Bin'" padahal Move belum dikonfirmasi; spec menghapus Asset Class setelah `Destination Asset Class` dipilih dan sebelum `[Move]` diklik, sesuai urutan langkah pada TC-213. Post Condition tentang tidak adanya perubahan data pada TC-170, TC-213, TC-240, dan TC-241 diasersi dengan `Verifikasi` yang dibaca lewat kemampuan baca fixture BE (langkah 9, 22, 34, dan 45) karena TC tidak menyebut cara cek.
