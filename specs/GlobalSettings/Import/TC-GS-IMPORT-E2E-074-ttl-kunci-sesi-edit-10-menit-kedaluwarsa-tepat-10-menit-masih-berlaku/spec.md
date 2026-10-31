---
id: TC-GS-IMPORT-E2E-074-ttl-kunci-sesi-edit-10-menit-kedaluwarsa-tepat-10-menit-masih-berlaku
title: "TTL Kunci Sesi Edit 10 Menit: Kedaluwarsa Tepat 10 Menit, Masih Berlaku pada Menit ke-9, dan Hitungan Diatur Ulang oleh Mutasi Terakhir"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-250
  - TC-GS-IMPORT-251
  - TC-GS-IMPORT-252
  - TC-GS-IMPORT-821
coverage:
  web: automated
---

# TTL Kunci Sesi Edit 10 Menit: Kedaluwarsa Tepat 10 Menit, Masih Berlaku pada Menit ke-9, dan Hitungan Diatur Ulang oleh Mutasi Terakhir

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah jam server; lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client A:
  - Sesi TC: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua, memulihkan jam server, dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` (TC-GS-IMPORT-250 dan 251); D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41) dengan badge saran AI (TC-GS-IMPORT-252 dan 821); mock AI mode normal (D-40, tabel D-41 dan D-42; D-11), dikembalikan ke normal sesudah spec.
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi, NC-08):
  - Fixture timestamp kunci: mengatur penanda waktu kunci Sesi TC menjadi tepat 10 atau 9 menit sebelum waktu server saat ini (acuan waktu server dibaca lewat API seeding).
  - Fixture jam server: dimajukan 6 atau 9 menit, atau diatur absolut menjadi tepat 10 menit sejak mutasi `[Dismiss]` (T0 = waktu server saat `[Dismiss]` diproses, dibaca lewat API seeding). Hanya jam server yang diatur karena TTL kunci dihitung murni di server dan tidak diamati lewat countdown UI; jam dipulihkan ke waktu nyata lewat langkah eksplisit sesudah TC-GS-IMPORT-252 dan 821.
- Margin jam (8b.3): T0 dibaca lewat fixture dan usia kunci hanya bertambah oleh waktu nyata (arah aman ke kedaluwarsa). Titik tepat 10 menit (langkah 3 dan 46) bernilai kedaluwarsa, margin 0 menit ke arah kedaluwarsa dan tidak terganggu waktu nyata. Titik 9 menit (langkah 12 dan 39): margin 60 detik terhadap TTL 10 menit (10 menit dikurangi 9 menit), sehingga dialog pada langkah 13 sampai 15 dan langkah 40 sampai 42 harus muncul dalam 60 detik sejak langkah 12 atau 39. Titik 6 menit (langkah 24, 26, 37): margin 4 menit (10 menit dikurangi 6 menit) tiap titik; 12 menit sejak awal sesi pada langkah 26 melewati TTL hanya bila hitungan tidak diatur ulang oleh mutasi `[Dismiss]`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: sesi edit ditutup dengan `[Cancel]`; draft dipulihkan antar TC.

## Test Steps

### TC-GS-IMPORT-250: Kunci kedaluwarsa tepat 10 menit

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. Atur penanda waktu kunci Sesi TC menjadi tepat 10 menit sebelum waktu server saat ini (fixture timestamp kunci)
4. [Sesi Admin kedua] Klik `⋯` pada baris #2
5. [Sesi Admin kedua] Pilih Edit
6. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
7. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
8. [Sesi Admin kedua] Verifikasi dialog "Draft Is Being Edited" tidak tampil
9. [Sesi Admin kedua] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-251: Kunci masih berlaku pada menit ke-9

10. [Sesi TC] Klik `⋯` pada baris #1
11. [Sesi TC] Pilih Edit
12. Atur penanda waktu kunci Sesi TC menjadi tepat 9 menit sebelum waktu server saat ini (fixture timestamp kunci)
13. [Sesi Admin kedua] Klik `⋯` pada baris #2
14. [Sesi Admin kedua] Pilih Edit
15. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
16. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
17. [Sesi Admin kedua] Verifikasi dialog tertutup
18. [Sesi Admin kedua] Verifikasi baris #2 tidak menjadi input
19. [Sesi TC] Klik `[Cancel]` pada footer (tanpa perubahan sehingga tanpa dialog); pulihkan draft D-01

### TC-GS-IMPORT-252: Mutasi server terakhir pemegang mengatur ulang hitungan TTL

20. Pulihkan draft D-09 dan muat ulang halaman Import > Brand pada kedua sesi
21. [Sesi TC] Klik tombol halaman 2 pada paginator
22. [Sesi TC] Klik `⋯` pada baris #13
23. [Sesi TC] Pilih Edit
24. Majukan jam server 6 menit sejak sesi edit dimulai (fixture jam server)
25. [Sesi TC] Klik `[Dismiss]` pada badge saran AI di sel Brand Name baris #13
26. Majukan jam server 6 menit lagi (6 menit sejak mutasi terakhir, 12 menit sejak awal sesi)
27. [Sesi Admin kedua] Klik `⋯` pada baris #2
28. [Sesi Admin kedua] Pilih Edit
29. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
30. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
31. [Sesi Admin kedua] Verifikasi dialog tertutup
32. [Sesi Admin kedua] Verifikasi baris #2 tidak menjadi input
33. Pulihkan jam server ke waktu nyata; tutup sesi edit Sesi TC; pulihkan draft D-09

### TC-GS-IMPORT-821: TTL dihitung sejak mutasi terakhir, kedaluwarsa tepat 10 menit

34. [Sesi TC] Klik tombol halaman 2 pada paginator
35. [Sesi TC] Klik `⋯` pada baris #13
36. [Sesi TC] Pilih Edit
37. Majukan jam server 6 menit sejak sesi edit dimulai (fixture jam server)
38. [Sesi TC] Klik `[Dismiss]` pada badge saran AI di sel Brand Name baris #13
39. Majukan jam server 9 menit sejak `[Dismiss]` (fixture jam server)
40. [Sesi Admin kedua] Klik `⋯` pada baris #2
41. [Sesi Admin kedua] Pilih Edit
42. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
43. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
44. [Sesi Admin kedua] Verifikasi dialog tertutup
45. [Sesi Admin kedua] Verifikasi baris #2 tidak menjadi input
46. Atur jam server menjadi tepat 10 menit sejak `[Dismiss]` (fixture jam server, absolut)
47. [Sesi Admin kedua] Klik `⋯` pada baris #2
48. [Sesi Admin kedua] Pilih Edit
49. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
50. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
51. [Sesi Admin kedua] Verifikasi dialog "Draft Is Being Edited" tidak tampil
52. [Sesi Admin kedua] Klik `[Cancel]` pada footer; pulihkan jam server ke waktu nyata dan draft D-09

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji TTL kunci 10 menit sebagai batas waktu); Sesi Admin kedua menjadi objek asersi.
- Spec memuat 52 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (fixture timestamp dan jam server pada TTL kunci) dengan pola identik, tiap blok berdiri sendiri dengan draft yang dipulihkan, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9, 19, 33, 52 (menutup sesi edit dan memulihkan jam serta draft), langkah 20 (menyiapkan draft D-09 dan memuat ulang), langkah 21, 34 (pindah ke halaman 2).
- Konteks kedua beraksi: belum ada id pengecualian untuk Sesi Admin kedua yang beraksi (Edit) dan diasersi di spec kelas d (TC-GS-IMPORT-250, 251, 252, 821); `P-2` hanya untuk konteks yang bukan objek asersi dan `P-6` hanya untuk pengamat read-only tanpa interaksi. Spec tidak dipecah (satu kelas harness, blok berdiri sendiri); usulan aturan baru menunggu batch konvensi.
- Langkah 8, 51 (absence dialog) memakai baris #2 yang menjadi input (langkah 6 dan 49) sebagai anchor positif.
- Temuan untuk QA:
  - Nilai waktu uji 6 menit (TC-GS-IMPORT-252 dan 821) dan 9 menit (TC-GS-IMPORT-821) ditandai `PRD?` pada dump TC (tidak tertulis di PRD); nilai itu pilihan TC sendiri, aturan PRD hanya TTL 10 menit.
  - TC-GS-IMPORT-250 dan 251 tidak menyebut cara menutup sesi edit sesudah Expected; langkah 19 menutupnya lewat `[Cancel]` sebagai langkah penghubung.
