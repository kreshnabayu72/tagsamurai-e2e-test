---
id: TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama
title: "Pagination Tabel Utama dan Retensi State setelah Refresh, Tab Baru, dan Logout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-150
  - TC-GS-FILEMGR-151
  - TC-GS-FILEMGR-152
  - TC-GS-FILEMGR-154
  - TC-GS-FILEMGR-155
coverage:
  web: automated
---

# Pagination Tabel Utama dan Retensi State setelah Refresh, Tab Baru, dan Logout

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data File Manager.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Tabel A2): 33 file aktif (F01 `budi-avatar.jpg` s.d. F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, F09-F33 `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), 4 halaman pada ukuran halaman 10, format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2 (tanpa sisa file, Recycle Bin, atau Changelog dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris dalam spec ini mengasumsikan dataset Tabel A2 segar tanpa sisa dari spec lain.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Data uji: ukuran halaman `10`, `25`, `50`, `100`; nomor halaman `3`, `0`, `99`, `abc`; Search `photo`; Filter Uploaded By `System`; Sort Size Descending; tab browser kedua untuk TC-GS-FILEMGR-155; sesi login ulang akun Total Control yang sama (`Spectra.env.GS_TC_PASSWORD`).
- Kemampuan teknis: membaca info pagination dan selector ukuran halaman; membuka tab browser baru; menekan `F5`; logout dan login ulang.
- Cleanup: hook `after` mengosongkan Search, Filter, dan Sort, serta mengembalikan ukuran halaman 10 dan halaman 1 (preferensi UI), dan memastikan sesi akun Total Control aktif.

## Test Steps

### TC-GS-FILEMGR-150: Opsi ukuran halaman dan kembali ke halaman 1 saat ukuran diubah

1. Buka selector ukuran halaman
2. Verifikasi opsi tepat `10`, `25`, `50`, `100` (tanpa opsi All)
3. Verifikasi ukuran halaman default `10`
4. Tutup selector ukuran halaman
5. Pindah ke halaman 2
6. Ubah ukuran halaman ke 25
7. Verifikasi tabel kembali ke halaman 1
8. Verifikasi tabel menampilkan 25 baris
9. Verifikasi total 2 halaman
10. Ubah ukuran halaman kembali ke 10

### TC-GS-FILEMGR-151: Input nomor halaman langsung dan nomor tidak valid diabaikan

11. Ketik `3` di input nomor halaman, tekan Enter
12. Verifikasi tabel pindah ke halaman 3
13. Ketik `0` di input nomor halaman, tekan Enter
14. Verifikasi tabel tetap di halaman 3 (input `0` diabaikan)
15. Ketik `99` di input nomor halaman, tekan Enter
16. Verifikasi tabel tetap di halaman 3 (input `99` diabaikan)
17. Ketik `abc` di input nomor halaman, tekan Enter
18. Verifikasi tabel tetap di halaman 3 (input `abc` diabaikan)

### TC-GS-FILEMGR-152: Mengubah sort tetap berada di nomor halaman yang sama

19. Pindah ke halaman 2
20. Klik header File Name sekali
21. Verifikasi tabel tetap di halaman 2
22. Verifikasi urutan dataset berubah sesuai File Name Ascending: baris halaman 2 adalah `staff-photo-03.jpg` s.d. `staff-photo-12.jpg`
23. Klik header File Name lagi
24. Klik header File Name sekali lagi (indikator sort hilang)

### TC-GS-FILEMGR-154: Refresh browser mempertahankan Search, Filter, Sort, dan Paginasi

25. Ketik Search `photo`, tekan Enter
26. Klik ikon Filter di toolbar
27. Pilih `System` pada `Uploaded By`
28. Klik `[Apply]`
29. Klik header Size sekali
30. Klik header Size lagi (Descending)
31. Pilih ukuran halaman `10`
32. Buka halaman 2
33. Tekan `F5` di tab yang sama
34. Verifikasi input Search berisi `photo`
35. Verifikasi Filter Uploaded By `System` tetap ter-Apply
36. Verifikasi Sort Size Descending tetap aktif
37. Verifikasi halaman 2 dengan ukuran halaman 10 tetap sama

### TC-GS-FILEMGR-155: Tab baru atau logout mengembalikan tabel utama ke default

38. Buka URL File Manager di tab browser baru
39. Verifikasi Search kosong di tab baru
40. Verifikasi tidak ada sort aktif di tab baru
41. Verifikasi tabel berada di halaman 1 di tab baru
42. Tutup tab baru dan kembali ke tab pertama
43. Klik ulang menu File Manager di sidebar pada tab pertama
44. Verifikasi tabel kembali ke default: Search kosong, tanpa sort aktif, halaman 1, dan 33 baris
45. Logout
46. Login kembali sebagai Total Control (`Spectra.env.GS_TC_PASSWORD`) dan buka File Manager
47. Verifikasi tabel di default: Search kosong, tanpa sort aktif, halaman 1, dan 33 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. TC-GS-FILEMGR-153 (pindah ke halaman terakhir setelah Bulk Delete) bukan bagian spec ini. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC mengikuti sumber (150, 151, 152, 154, 155). TC-GS-FILEMGR-155 ditaruh paling akhir karena melakukan logout dan login ulang (ganti sesi eksplisit; S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (mengembalikan ukuran halaman 10), langkah 23 (mengembalikan sort File Name ke netral), dan langkah 42 (menutup tab baru). Pada TC-GS-FILEMGR-154 langkah "Pilih ukuran halaman `10`" tidak mengubah nilai (default 10) tetapi dipertahankan karena TC sumber menuliskannya sebagai langkah. Asersi "input diabaikan" pada TC-GS-FILEMGR-151 teramati lewat tabel tetap di halaman 3 (TC tidak menyebut indikator lain).
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 47 langkah): lima TC memakai kontrol pagination dan state tabel utama yang sama pada dataset Tabel A2, satu akun, satu topik (Pagination dan retensi state); blok TC-GS-FILEMGR-150 sampai 152 dipisah dengan pemulihan eksplisit sehingga tiap blok tidak bergantung pada hasil asersi blok sebelumnya. Blok TC-GS-FILEMGR-155 memakai state TC-GS-FILEMGR-154 sebagai precondition (dependensi sumber), sehingga kegagalan keras di TC-GS-FILEMGR-154 membuat asersi TC-GS-FILEMGR-155 kurang bermakna; ketergantungan ini mengikuti TC sumber.
- Temuan untuk QA:
  - TC-GS-FILEMGR-152 butir a: TC tidak menyebut baris halaman 2; spec menurunkan `staff-photo-03.jpg` s.d. `staff-photo-12.jpg` dari urutan File Name Ascending Tabel A2 (delapan baris pertama `alex-photo.jpeg` s.d. `siti-profile.png`, lalu `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`).
  - TC-GS-FILEMGR-155: precondition TC hanya menyebut Search `photo` dan Sort Size Descending; state tab pertama (dari TC-GS-FILEMGR-154) juga memuat Filter `System` dan halaman 2. Spec mengasersi "default" lengkap (Search kosong, tanpa sort, halaman 1, 33 baris); TC tidak menyebut apakah Filter ikut kembali default.
  - TC-GS-FILEMGR-155 langkah 3: kredensial login ulang tidak disebut; spec memakai akun Total Control yang sama dengan `Spectra.env.GS_TC_PASSWORD`.
  - TC-GS-FILEMGR-151: nomor halaman `abc` pada input bertipe angka dapat tidak diterima oleh browser; TC tidak menyebut perilakunya selain "diabaikan".
  - Seeding Tabel A2 dan reset dataset antar spec tidak punya mekanisme tertulis di TC (lihat spec 031).
