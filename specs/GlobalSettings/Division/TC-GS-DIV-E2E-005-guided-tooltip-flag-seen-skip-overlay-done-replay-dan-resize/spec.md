---
id: TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize
title: "Guided Tooltip Tab Division: Flag Seen, Skip, Overlay, Done, Replay, dan Resize"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-11
  - TC-GS-DIV-12
  - TC-GS-DIV-13
  - TC-GS-DIV-14
  - TC-GS-DIV-15
coverage:
  web: automated
---

# Guided Tooltip Tab Division: Flag Seen, Skip, Overlay, Done, Replay, dan Resize

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data: memakai data Pre-setup Division (6 Division, data environment tetap); spec tidak membuat data.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-division`, sehingga flag dihapus ("belum ada") lewat API sebelum tiap TC yang mensyaratkannya (langkah reset eksplisit). Hook `before` mencatat nilai awal flag; hook `after` memulihkan nilai awal walau spec gagal di tengah.
- Kemampuan teknis: menghapus dan membaca nilai flag `guided_tooltip_seen_gs-division` akun aktor lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); mengubah lebar viewport saat walkthrough berjalan (TC-GS-DIV-15) dan memulihkannya (langkah 39, hook `after` sebagai cadangan); muat ulang halaman (F5).
- State global yang diubah: flag Guided Tooltip dan viewport (dipulihkan seperti di atas).

## Test Steps

### TC-GS-DIV-11: Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelah Skip

1. Hapus flag `guided_tooltip_seen_gs-division` lewat API sehingga flag belum ada
2. Buka Global Settings > User > Tab Division untuk kunjungan pertama
3. Verifikasi walkthrough muncul otomatis dari Step 1
4. Klik `[Skip]`
5. Verifikasi `[Skip]` menutup walkthrough
6. Verifikasi flag `guided_tooltip_seen_gs-division` bernilai true (baca lewat API)
7. Muat ulang halaman (F5)
8. Verifikasi walkthrough tidak muncul otomatis lagi

### TC-GS-DIV-14: Tombol [?] memulai ulang walkthrough dari Step 1 tanpa mereset flag

9. Klik trigger `[?]` di header halaman
10. Verifikasi walkthrough mulai dari Step 1
11. Klik `[Skip]`
12. Muat ulang halaman (F5)
13. Verifikasi flag `guided_tooltip_seen_gs-division` tetap true (baca lewat API)
14. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-DIV-12: Klik overlay gelap menutup walkthrough dan menyimpan flag seen

15. Hapus flag `guided_tooltip_seen_gs-division` lewat API sehingga flag belum ada
16. Buka Tab Division untuk kunjungan pertama (muat ulang Global Settings > User > Tab Division)
17. Klik area overlay gelap di luar tooltip
18. Verifikasi klik overlay menutup walkthrough
19. Muat ulang halaman (F5)
20. Verifikasi walkthrough tidak muncul lagi (flag `seen` tersimpan)

### TC-GS-DIV-13: Navigasi Back, Next, dan Done pada walkthrough

21. Hapus flag `guided_tooltip_seen_gs-division` lewat API sehingga flag belum ada
22. Buka Tab Division untuk kunjungan pertama (muat ulang Global Settings > User > Tab Division)
23. Verifikasi tombol `[Back]` Hidden pada Step 1
24. Klik `[Next]` ke Step 2
25. Verifikasi Step 2 muncul
26. Klik `[Back]`
27. Verifikasi `[Back]` kembali ke Step 1
28. Klik `[Next]` ke Step 2
29. Klik `[Next]` ke Step 3
30. Verifikasi pada Step 3 (terakhir) tombol `[Next]` berubah menjadi `[Done]`
31. Klik `[Done]`
32. Verifikasi `[Done]` menutup walkthrough
33. Verifikasi flag `guided_tooltip_seen_gs-division` bernilai true (baca lewat API)

### TC-GS-DIV-15: Resize viewport atau pindah halaman di tengah walkthrough tidak menyimpan flag seen

34. Hapus flag `guided_tooltip_seen_gs-division` lewat API sehingga flag belum ada
35. Buka Tab Division untuk kunjungan pertama (muat ulang Global Settings > User > Tab Division)
36. Ubah lebar viewport browser saat Step 1 tampil
37. Verifikasi resize menutup walkthrough
38. Verifikasi flag `guided_tooltip_seen_gs-division` tetap belum ada (baca lewat API)
39. Kembalikan lebar viewport ke ukuran awal
40. Muat ulang halaman
41. Verifikasi walkthrough muncul lagi otomatis dari Step 1
42. Klik Tab Position saat walkthrough tampil
43. Klik Tab Division untuk kembali ke Tab Division
44. Verifikasi walkthrough muncul lagi otomatis dari Step 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (44 langkah) karena lima TC flag seen berada di satu kelas harness (fungsional, state flag Guided Tooltip akun aktor); tiap blok TC mereset flag di awalnya (langkah 1, 15, 21, 34) dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-DIV-14 ditaruh langsung sesudah TC-GS-DIV-11 karena precondition-nya (flag `seen` true, dependensi TC-GS-DIV-11) dipenuhi oleh state akhir TC-GS-DIV-11 tanpa reset tambahan; sesudahnya TC-GS-DIV-12, TC-GS-DIV-13, lalu TC-GS-DIV-15 terakhir karena mengubah viewport.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 15, 21, dan 34 (hapus flag lewat API untuk memenuhi precondition "flag belum ada"), 16, 22, dan 35 (muat ulang tab agar kunjungan pertama berikutnya terpenuhi), 39 (pulihkan viewport sebelum muat ulang), 43 (kembali ke Tab Division).
- Pembacaan flag lewat API (langkah 6, 13, 33, 38) menjadi dasar klausa "menyimpan flag `seen`" atau "tanpa menyimpan flag" pada Expected Result TC-GS-DIV-11 b, TC-GS-DIV-14 b, TC-GS-DIV-13 d, dan TC-GS-DIV-15 a. Klausa yang diamati lewat perilaku halaman (TC-GS-DIV-12 b) diasersi dari walkthrough yang tidak muncul setelah muat ulang. Post Condition TC-GS-DIV-11, TC-GS-DIV-12, dan TC-GS-DIV-13 tidak diasersi terpisah; Post Condition TC-GS-DIV-15 sudah menjadi padanan Expected Result a (langkah 38).
- Perilaku konten step dan keyboard diuji di spec `TC-GS-DIV-E2E-004-guided-tooltip-konten-dan-navigasi-keyboard`.
- Temuan untuk QA:
  - TC-GS-DIV-15 langkah 4 meminta pindah ke Tab Position saat walkthrough tampil, tetapi overlay walkthrough dapat menutupi tab; TC tidak menyatakan apakah walkthrough menutup klik tab atau navigasi dilakukan lewat cara lain. Spec mengklik Tab Position (langkah 42) dan Tab Division (langkah 43). Expected Result TC tidak menyebut walkthrough tertutup saat pindah tab, sehingga tidak diasersi.
  - TC-GS-DIV-15 langkah 2 tidak menyebut lebar viewport tujuan; tim FE menentukan nilainya.
  - Cara membaca dan menghapus flag `guided_tooltip_seen_gs-division` tidak didefinisikan di TC dan PRD Division; disediakan tim FE/BE.
