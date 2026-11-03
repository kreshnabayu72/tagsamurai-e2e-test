---
id: TC-AC-ACTS-E2E-092-add-stock-gps-volume-job-background-gagal-ambang-lintas-upload-dan-remove-ke-5000
title: "Add Stock GPS Volume: Kegagalan Job Background, Ambang 5.000 Lintas Upload Berurutan, Remove Menurunkan Total ke 5.000, dan Bar Non-Interaktif saat Parse"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-771
  - TC-AC-ACTS-772
  - TC-AC-ACTS-885
  - TC-AC-ACTS-887
coverage:
  web: automated
---

# Add Stock GPS Volume: Kegagalan Job Background, Ambang 5.000 Lintas Upload Berurutan, Remove Menurunkan Total ke 5.000, dan Bar Non-Interaktif saat Parse

## Prerequisites

- Mode: FE+BE. Intercept menahan respons cek-match saat parse berkas (TC-AC-ACTS-887) lewat `Spectra.intercept()` di atas backend nyata; kegagalan job background diinjeksi di sisi server (TC-AC-ACTS-771).
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kelas e (volume 5.000 dan 5.001 baris). Berkas CSV berisi 5.001 IMEI valid baru (dua kali), file A 3.000 IMEI dan file B 2.001 IMEI (semua unik), dan file 5.000 IMEI, dibuat oleh pembuat berkas dengan IMEI yang belum terdaftar (disediakan tim FE). Dua IMEI manual `356938035643809` dan `356938035643812` (Data Dinamis #2) dipakai sebagai precondition TC-AC-ACTS-887, tidak diasersi.
- Kemampuan teknis disediakan tim FE/BE: injeksi kegagalan job background di sisi server beserta pelepasannya (hook `after`), kueri status job, kemampuan baca jumlah unit Available SKU, jumlah Subject, dan jumlah entri Activity Log `Add Stock` (baseline, S-12); unit yang didaftarkan spec ini dihapus lewat fixture BE di hook `before` dan `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-771: Kegagalan job background membatalkan seluruh batch

1. Atur job background gagal di sisi server (injeksi kegagalan BE)
2. Catat baseline jumlah unit Available SKU, jumlah Subject di Approvals > TAG Stock Tab Active dan Tab History, dan jumlah entri Activity Log `Add Stock`
3. Unggah file CSV berisi 5.001 IMEI valid baru
4. Klik `[Submit]`
5. Verifikasi toast "Preparing your import. We'll notify you when it's ready."
6. Verifikasi toast "Success, TAG has been registered." dan toast "Success, [N] TAGs have been sent for approval." tidak tampil (sesudah anchor toast Preparing, sebelum polling)
7. Klik `[Cancel]`
8. Verifikasi dialog Unsaved Changes tampil
9. Klik `[Leave]`
10. Muat ulang halaman Detail SKU > Tab Available setiap 5 detik sampai status job gagal (kueri status job, batas tunggu 2 menit)
11. Verifikasi tidak ada satu pun unit baru di Tab Available (selisih nol terhadap baseline)
12. Verifikasi tidak ada Subject baru di Tab Active dan Tab History (selisih nol terhadap baseline)
13. Verifikasi tidak ada entri Activity Log `Add Stock` baru (selisih nol terhadap baseline)
14. Lepas injeksi kegagalan job background

### TC-AC-ACTS-772: Ambang 5.000 baris dihitung dari total Preview lintas upload berurutan

15. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
16. Unggah file A berisi 3.000 IMEI valid baru
17. Unggah file B berisi 2.001 IMEI valid baru
18. Verifikasi Preview memuat 5.001 baris (upload kedua menambah baris)
19. Klik `[Submit]`
20. Verifikasi toast "Preparing your import. We'll notify you when it's ready." (total baris Preview melebihi 5.000 sehingga job background)
21. Klik `[Cancel]`
22. Verifikasi dialog Unsaved Changes tampil
23. Klik `[Leave]`

### TC-AC-ACTS-885: Remove dari Preview menurunkan total ke 5.000 baris, Submit sinkron tanpa toast T-23

24. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
25. Unggah file CSV berisi 5.001 IMEI valid baru
26. Centang satu baris
27. Pilih Bulk Action > `Remove`
28. Klik `[Remove]` pada dialog
29. Verifikasi Ringkasan `5000 valid, 0 waiting approval, 0 duplicate, 0 invalid of 5000 entries`
30. Klik `[Submit]`
31. Verifikasi toast "Success, TAG has been registered." (diproses sinkron)
32. Verifikasi toast "Preparing your import. We'll notify you when it's ready." tidak tampil

### TC-AC-ACTS-887: Checkbox dan Bulk Action Bar Preview non-interaktif selama parse file berjalan

33. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
34. Tambahkan IMEI `356938035643809` dan `356938035643812` lewat Manual Entry (Preview berisi 2 baris)
35. Centang satu baris
36. Tahan respons cek-match, lalu unggah file CSV berisi 5.000 IMEI valid baru
37. Coba klik checkbox, Select All, dan aksi pada Bulk Action Bar selama parse berjalan
38. Verifikasi checkbox, Select All, dan Bulk Action Bar tidak dapat diklik selama parse berjalan
39. Lepas tahanan respons cek-match
40. Verifikasi checkbox, Select All, dan Bulk Action Bar interaktif kembali setelah parse selesai
41. Verifikasi seleksi satu baris masih ada
42. Klik `[Cancel]`
43. Verifikasi dialog Unsaved Changes tampil
44. Klik `[Leave]`

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (44 langkah); alasan: semua blok satu kelas harness (kelas e, volume 5.000 dan 5.001 baris) dan satu dataset berkas, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-1 (state berat): TC-AC-ACTS-771 memuat asersi selisih nol atas Activity Log `Add Stock` karena state job background gagal dengan 5.001 baris baru dibangun langkah sebelumnya; asersinya memakai baseline (asersi jumlah, bukan kelas g).
- Langkah penghubung tanpa Verifikasi (S-03): injeksi dan pelepasan kegagalan job, mencatat baseline (S-12), `[Cancel]` lalu `[Leave]` untuk menutup Preview yang tetap tampil (S-08), buka kembali halaman Add Stock, dan muat ulang tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit).
- Temuan untuk QA:
  - TC-AC-ACTS-771 menyebut "Buka Detail SKU > Tab Available dan Notification Center" tetapi Expected tidak menyebut isi Notification Center saat job gagal; Notification Center tidak diasersi.
  - TC-AC-ACTS-887 tidak menyebut cara membuat parse berjalan cukup lama; spec memakai tahanan respons cek-match (kemampuan disediakan tim FE).
