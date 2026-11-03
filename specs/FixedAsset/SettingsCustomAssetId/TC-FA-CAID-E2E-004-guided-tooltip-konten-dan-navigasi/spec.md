---
id: TC-FA-CAID-E2E-004-guided-tooltip-konten-dan-navigasi
title: "Guided Tooltip: Konten, Kunjungan Pertama, Ulang, dan Navigasi Step"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-13
  - TC-FA-CAID-14
  - TC-FA-CAID-15
  - TC-FA-CAID-16
coverage:
  web: automated
---

# Guided Tooltip: Konten, Kunjungan Pertama, Ulang, dan Navigasi Step

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Akun aktor: Total Control Company Alpha (Pre-setup No 1, akun default suite) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pengecualian hook suite untuk flag Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-asset-id` (page_key `fa-settings-custom-asset-id`) ke seen untuk akun aktor dan hook `after` suite memulihkan nilai awal. Spec ini menguji flag itu sendiri, jadi langkah spec mengatur flag Total Control ke belum diset atau seen sesudah hook dengan kemampuan "atur flag Guided Tooltip akun aktor" (menulis flag; disediakan tim FE, mekanisme tidak tertulis di TC, PRD, atau LLD). Spec tidak mengubah flag akun lain.
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), hanya dibaca. Teks walkthrough lima step dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Spec tidak membuat data dan tidak menekan `[Save]`.
- State global: flag Guided Tooltip akun Total Control; hook `after` suite memulihkannya ke nilai awal yang dicatat hook `before` suite, walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-14: Guided Tooltip muncul otomatis pada kunjungan pertama dan tidak pada kunjungan berikutnya

1. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan
2. Muat ulang halaman (F5) sebagai kunjungan pertama ke tab Custom Asset ID
3. Verifikasi walkthrough tampil otomatis mulai dari step 1 dengan indikator `Step 1 of 5`
4. Klik `[Skip]`
5. Verifikasi walkthrough tertutup
6. Klik tab `Asset Name` pada Tabs Bar
7. Klik tab `Custom Asset ID` pada Tabs Bar
8. Verifikasi tab `Custom Asset ID` tampil dengan Breadcrumb `Settings > Asset Master > Custom Asset ID`
9. Verifikasi walkthrough tidak muncul otomatis lagi

### TC-FA-CAID-15: Tombol `[?]` mengulang walkthrough dari step 1 tanpa mereset flag seen

10. Hover tombol `[?]` di kanan Breadcrumb
11. Verifikasi tooltip tombol `[?]` berbunyi `Show guide`
12. Klik tombol `[?]`
13. Verifikasi walkthrough mulai dari step 1
14. Klik `[Next]` dua kali
15. Klik `[Skip]`
16. Verifikasi walkthrough tertutup
17. Muat ulang halaman (F5)
18. Verifikasi tab `Custom Asset ID` tampil dengan Breadcrumb `Settings > Asset Master > Custom Asset ID`
19. Verifikasi walkthrough tidak muncul otomatis karena flag seen tidak direset

### TC-FA-CAID-13: Guided Tooltip: konten lima step

20. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan, tanpa memuat ulang halaman
21. Klik tombol `[?]` di kanan Breadcrumb
22. Verifikasi step 1: menyorot switch `Master Switch`, Title `Master Switch`, Description `Turn this on to customize how your asset IDs are numbered.`, indikator `Step 1 of 5`
23. Klik `[Next]`
24. Verifikasi step 2: menyorot baris `Initial Company`, Title `Initial Company`, Description `Check this to start every Asset ID with your company initials, then type the initials.`, indikator `Step 2 of 5`
25. Klik `[Next]`
26. Verifikasi step 3: menyorot Live Preview Card, Title `Live Preview`, Description `See an example of the Asset ID that your current format produces.`, indikator `Step 3 of 5`
27. Klik `[Next]`
28. Verifikasi step 4: menyorot Daftar Segmen (drag handle dan checkbox), Title `Segments Order`, Description `Drag the handles to set the order of the segments and check the ones you want to use.`, indikator `Step 4 of 5`
29. Klik `[Next]`
30. Verifikasi step 5: menyorot tombol `[View Code List]`, Title `View Code List`, Description `Open this to review the abbreviation codes that the segments use.`, indikator `Step 5 of 5`
31. Verifikasi tombol `[Next]` berubah menjadi `[Done]` di step 5
32. Klik `[Done]`

### TC-FA-CAID-16: Guided Tooltip: navigasi Back, Next, dan Done antar step

33. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan, tanpa memuat ulang halaman
34. Klik tombol `[?]` di kanan Breadcrumb
35. Verifikasi di step 1 tombol `[Back]` tidak tampil (hidden) dan tersedia `[Skip]` dan `[Next]`
36. Klik `[Next]` dua kali sampai step 3
37. Klik `[Back]`
38. Verifikasi step 2 tampil
39. Klik `[Next]` tiga kali sampai step 5
40. Verifikasi di step 5 tombol `[Next]` berubah menjadi `[Done]`
41. Klik `[Done]`
42. Verifikasi walkthrough tertutup
43. Muat ulang halaman (F5)
44. Verifikasi kartu `Custom Asset ID Configuration` tampil
45. Verifikasi walkthrough tidak muncul otomatis karena `[Done]` menyetel flag seen

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC di spec: TC-FA-CAID-14, 15, 13, 16. Alasan: flag seen dari hook suite berarti kunjungan berikutnya tidak memunculkan walkthrough otomatis, sehingga TC kunjungan pertama dan ulang berurutan lebih dulu pada state flag yang dibangun langkah sebelumnya, lalu TC konten dan navigasi memakai `[?]` setelah flag diatur ulang tanpa muat ulang (S-10).
- Spec ini 45 langkah tanpa langkah bersyarat, melewati sekitar 35 langkah. Alasan: semua blok satu kelas (fungsional, state flag Guided Tooltip), satu akun, satu layar, dan tiap blok mengatur ulang flag sendiri sehingga berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- S-01, klausa digabung dengan alasan: Expected TC-FA-CAID-13 menyebut tiap step sebagai satu butir (target, Title, Description, dan indikator satu kotak tooltip), sehingga langkah 22, 24, 26, 28, 30 masing-masing satu `Verifikasi` atas satu kotak tooltip. Memecahnya menjadi empat `Verifikasi` per step menambah 15 langkah pada spec yang sudah melewati batas tanpa menambah cakupan. Daftar tombol di langkah 35 (`[Back]` hidden, `[Skip]` dan `[Next]` tersedia) juga disebut utuh dalam satu butir Expected TC-FA-CAID-16.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 20, 33 (mengatur flag), langkah 2 dan 17 dan 43 (muat ulang sebagai pemicu), langkah 6 dan 7 (pindah tab ke Asset Name lalu kembali sebagai pemicu), langkah 4, 10, 12, 14, 15, 21, 23, 25, 27, 29, 34, 36, 37, 39, 41 (aksi walkthrough sebagai pemicu), dan langkah 32 (klik `[Done]` untuk menutup walkthrough sebelum TC-FA-CAID-16 mengatur ulang flag).
- Pada TC-FA-CAID-13 dan 16 flag diatur belum diset tanpa memuat ulang halaman sehingga langkah TC "klik `[?]`" memulai walkthrough dari step 1 seperti tertulis di TC, bukan muncul otomatis lebih dulu.
- Asersi absence (langkah 9, 19, 45) didahului asersi positif atas elemen lain pada halaman yang sama (langkah 8 dan 18: tab `Custom Asset ID` tampil dengan Breadcrumb, sesuai klausa Expected TC-FA-CAID-14 c dan TC-FA-CAID-15 d; langkah 44: kartu konfigurasi tampil).
- Langkah 42 sampai 45 mengamati hasil "klik `[Done]` menyetel flag seen" lewat muat ulang halaman, karena TC tidak memberi cara lain mengamati flag.
- Temuan untuk QA:
  - `guided-tooltip.md` §16.6 tidak mendaftar `fa-settings-custom-asset-id`; TC mengikuti PRD §4.7 (G-1 di catatan TC).
  - TC-FA-CAID-13 dan 16 berprecondition "flag belum diset" tetapi Langkah Uji-nya memulai dengan klik `[?]`; bila flag belum diset saat halaman dimuat, walkthrough sudah tampil otomatis sebelum klik. Spec mengatur flag sesudah halaman dimuat agar klik `[?]` memulai walkthrough; QA perlu menegaskan urutan yang dimaksud.
  - Expected TC-FA-CAID-16 c tidak memuat klausa anchor untuk asersi "tidak muncul otomatis" setelah muat ulang (TC-FA-CAID-14 dan 15 memuat Breadcrumb); spec memakai kartu `Custom Asset ID Configuration` tampil (langkah 44) sebagai anchor tambahan (S-03, S-15).
  - Mekanisme mengatur dan membaca flag Guided Tooltip akun tidak tertulis di TC, PRD, atau LLD; disediakan tim FE (S-13).
  - Post Condition TC-FA-CAID-13, 14, 15, 16 kosong; tidak ada yang diasersi.
