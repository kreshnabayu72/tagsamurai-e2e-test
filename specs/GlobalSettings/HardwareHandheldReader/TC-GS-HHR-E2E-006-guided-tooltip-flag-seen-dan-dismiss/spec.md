---
id: TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss
title: "Guided Tooltip Halaman Handheld Reader: Muncul Otomatis, Done, Skip, Klik Overlay Menandai Seen, Replay lewat [?], serta Resize dan Navigasi Keluar Tidak Menandai Seen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-24
  - TC-GS-HHR-25
  - TC-GS-HHR-26
  - TC-GS-HHR-27
  - TC-GS-HHR-29
  - TC-GS-HHR-453
coverage:
  web: automated
---

# Guided Tooltip Halaman Handheld Reader: Muncul Otomatis, Done, Skip, Klik Overlay Menandai Seen, Replay lewat [?], serta Resize dan Navigasi Keluar Tidak Menandai Seen

## Prerequisites

- Mode: FE+BE (backend nyata). Suite `parallel: false`.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: kunjungan ke halaman Handheld Reader adalah pemicu auto-open Guided Tooltip, sehingga langkah buka ditulis di `## Test Steps` dan bukan di hook `beforeEach`.
- Guided Tooltip (page_key `gs-handheld-reader`): spec ini menguji flag `guided_tooltip_seen_gs-handheld-reader` sendiri, sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`). Hook `before` mencatat nilai awal flag akun Total Control lalu mereset flag ke belum ada (precondition "flag belum diset" TC-GS-HHR-24). Flag tetap bernilai seen sesudah `[Done]` pada TC-GS-HHR-24 dan itulah precondition "flag sudah diset" TC-GS-HHR-25. Flag di-reset ke belum ada sebagai langkah penghubung sebelum TC-GS-HHR-26 dan 27 (TC sebelumnya menandai seen); TC-GS-HHR-29 menjaga flag tetap belum ada sehingga TC-GS-HHR-453 memakai flag belum ada tanpa reset. Hook `after` memulihkan nilai awal flag. Mekanisme baca, reset, dan pemulihan flag disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Data Pre-setup (Client A, plan Growth, General Settings `dd/MM/yy` 24-hour): Seed Reader A (DD-01 s.d. DD-10) dipulihkan fixture backend (disediakan tim FE) sebelum spec berjalan; spec tidak membaca atau mengubah isi baris. Data Dinamis: tidak ada.
- Kemampuan teknis: klik pada area overlay gelap di luar tooltip box (koordinat di luar spotlight dan tooltip); mengubah ukuran viewport browser dan memulihkannya; navigasi lewat address bar (ke Global Settings > Activity Log dan kembali); muat ulang halaman dengan `F5`; pembacaan state flag lewat perilaku kunjungan ulang.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan nilai awal flag akun Total Control dan kembalikan viewport ke ukuran awal.
- State global: tidak ada yang diubah selain flag Guided Tooltip dan viewport (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-24: Walkthrough muncul otomatis pada kunjungan pertama dan tidak muncul lagi setelah Done

1. Buka Global Settings > Hardware > Handheld Reader lewat address bar
2. Verifikasi walkthrough muncul otomatis dari Step 1 (judul `License Counter`)
3. Klik `[Next]`
4. Klik `[Next]`
5. Klik `[Done]`
6. Verifikasi walkthrough tertutup setelah `[Done]`
7. Muat ulang halaman dengan `F5`
8. Verifikasi License Counter Cards tampil
9. Verifikasi walkthrough tidak muncul otomatis setelah `F5`

### TC-GS-HHR-25: Tombol [?] memulai ulang walkthrough dari Step 1 tanpa mereset flag

10. Arahkan kursor ke ikon `[?]` di kanan Breadcrumb
11. Verifikasi tooltip tombol `Show guide`
12. Klik `[?]`
13. Verifikasi walkthrough mulai dari Step 1 (judul `License Counter`)
14. Klik `[Skip]`
15. Muat ulang halaman dengan `F5`
16. Verifikasi License Counter Cards tampil
17. Verifikasi walkthrough tidak muncul otomatis setelah `F5` (flag tidak direset oleh replay)
18. Reset flag `guided_tooltip_seen_gs-handheld-reader` akun Total Control ke belum ada

### TC-GS-HHR-26: Skip lewat tombol menutup walkthrough dan menyetel flag

19. Buka Global Settings > Hardware > Handheld Reader lewat address bar
20. Klik `[Next]` sekali
21. Klik `[Skip]`
22. Verifikasi walkthrough tertutup
23. Muat ulang halaman dengan `F5`
24. Verifikasi License Counter Cards tampil
25. Verifikasi walkthrough tidak muncul otomatis setelah `F5`
26. Reset flag `guided_tooltip_seen_gs-handheld-reader` akun Total Control ke belum ada

### TC-GS-HHR-27: Skip lewat klik overlay gelap menutup walkthrough dan menyetel flag

27. Buka Global Settings > Hardware > Handheld Reader lewat address bar
28. Klik area overlay gelap di luar spotlight dan di luar tooltip box
29. Verifikasi walkthrough tertutup
30. Muat ulang halaman dengan `F5`
31. Verifikasi License Counter Cards tampil
32. Verifikasi walkthrough tidak muncul otomatis setelah `F5`
33. Reset flag `guided_tooltip_seen_gs-handheld-reader` akun Total Control ke belum ada

### TC-GS-HHR-29: Resize viewport di tengah walkthrough menutup tanpa menyetel flag

34. Buka Global Settings > Hardware > Handheld Reader lewat address bar
35. Ubah ukuran viewport browser dari ukuran awal menjadi lebar `1024` px dan tinggi `768` px (tetap di atas breakpoint Mobile `768` px) saat walkthrough berada di Step 1
36. Verifikasi walkthrough tertutup saat resize
37. Muat ulang halaman dengan `F5`
38. Verifikasi walkthrough muncul otomatis lagi dari Step 1 (judul `License Counter`), flag tidak diset

### TC-GS-HHR-453: Navigasi keluar halaman di tengah walkthrough menutup tanpa menyetel flag

39. Saat walkthrough berada di Step 1, buka Global Settings > Activity Log lewat address bar
40. Verifikasi halaman Global Settings > Activity Log tampil
41. Verifikasi walkthrough tertutup saat halaman ditinggalkan (tooltip walkthrough tidak tampil)
42. Buka kembali Global Settings > Hardware > Handheld Reader lewat address bar
43. Verifikasi walkthrough muncul otomatis lagi dari Step 1 (judul `License Counter`), flag tidak diset
44. Kembalikan ukuran viewport ke ukuran awal

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 24, 25, 26, 27, 29, 453. TC-GS-HHR-25 mengikuti TC-GS-HHR-24 karena precondition "flag sudah diset" dipenuhi oleh `[Done]` pada TC-GS-HHR-24; TC-GS-HHR-29 dan 453 ditaruh terakhir karena keduanya butuh flag belum ada dan tidak menyetelnya, sehingga TC-GS-HHR-453 tidak membutuhkan reset. Urutan ini meniadakan dua langkah buka: langkah "Buka Global Settings > Hardware > Handheld Reader" TC-GS-HHR-25 tidak ditulis karena halaman sudah terbuka sejak langkah 7 TC-GS-HHR-24, dan langkah buka TC-GS-HHR-453 tidak ditulis karena halaman sudah terbuka dengan walkthrough pada Step 1 sejak langkah 38 TC-GS-HHR-29.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18, 26, dan 33 (reset flag), langkah 44 (kembalikan viewport ke ukuran awal sesudah blok terakhir; viewport 1024x768 dipertahankan selama TC-GS-HHR-29 dan 453 karena mengubah ukuran menutup walkthrough Step 1 yang dipakai TC-GS-HHR-453), langkah 1, 19, 27, 34 (membuka halaman lewat address bar sebagai pemicu auto-open), serta langkah 8, 16, 24, 31 (`Verifikasi` License Counter Cards tampil) yang merupakan anchor positif absence walkthrough sesudah `F5` (konvensi bagian 8b butir 2) dan bukan asersi dari TC. Langkah 40 adalah anchor positif absence walkthrough pada halaman tujuan (langkah 41).
- Spec 006 (flag seen, dismiss, resize, navigasi keluar) dan spec 005 (konten, navigasi Back, keyboard) menguji Guided Tooltip halaman Handheld Reader yang sama dan sengaja dipisah: gabungannya 83 langkah (39 dan 44), jauh di atas sekitar 35 langkah, dan tiap blok mereset atau menjaga flag seen sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Spec melewati sekitar 35 langkah (44 langkah). Seluruhnya satu kelas (Guided Tooltip halaman Handheld Reader: flag seen dan dismiss), tiap blok TC berdiri sendiri karena flag di-reset atau dijaga sebelum tiap blok. Pengecualian: blok TC-GS-HHR-25 bergantung pada flag seen hasil `[Done]` blok TC-GS-HHR-24, dan blok TC-GS-HHR-453 bergantung pada halaman dengan walkthrough Step 1 hasil blok TC-GS-HHR-29; kegagalan keras blok sebelumnya membuat blok itu gagal. Risiko diterima karena alternatifnya (reset flag dan buka ulang halaman per blok) menambah langkah tanpa cakupan baru.
- Temuan untuk QA:
  - TC-GS-HHR-24 sampai 27, 29, dan 453 mensyaratkan flag belum diset atau sudah diset tanpa menyebut cara menyetelnya; mekanismenya disediakan tim FE/BE.
  - TC-GS-HHR-453 tidak menyebut apakah halaman tujuan Global Settings > Activity Log memuat Guided Tooltip sendiri; spec mengasersi tidak ada tooltip walkthrough Handheld Reader dan tidak mengasersi walkthrough halaman lain.
  - TC-GS-HHR-24 Expected a menyebut walkthrough muncul otomatis dari Step 1 tanpa judul step; spec memakai judul Step 1 `License Counter` dari PRD §4.7 dan TC-GS-HHR-23 sebagai penanda.
