---
id: TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss
title: "Flag Seen dan Dismiss Guided Tooltip: Skip, Overlay, Tombol [?], Resize, Navigasi Halaman"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-17
  - TC-GS-UOM-18
  - TC-GS-UOM-19
  - TC-GS-UOM-20
  - TC-GS-UOM-334
coverage:
  web: automated
---

# Flag Seen dan Dismiss Guided Tooltip: Skip, Overlay, Tombol [?], Resize, Navigasi Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data: memakai Pre-setup Client A dan Population D-01 (hanya dibaca; di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md`); spec tidak membuat data.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-measurement` sehingga dikecualikan dari pernyataan hook suite di `suite.md`. Flag diatur ke "belum ada" atau true lewat mekanisme penyetelan flag yang disediakan tim FE/BE (tanpa endpoint karangan, S-13), sebagai langkah eksplisit di awal tiap TC (langkah 1, 9, 16, 29, 37). Hook `before` mencatat nilai awal flag Measurement untuk akun aktor dan hook `after` memulihkannya walau spec gagal di tengah. Flag `guided_tooltip_seen_gs-brand` mengikuti hook suite.
- Kemampuan teknis: mengubah lebar viewport saat walkthrough berjalan (TC-GS-UOM-20); hook `after` memulihkan viewport ke ukuran awal.
- State global yang diubah: flag Guided Tooltip dan viewport (dipulihkan seperti di atas).
- Layar awal: sesi baru tanpa membuka Master Reference. Spec ini dikecualikan dari pembukaan layar oleh hook `beforeEach` suite (lihat `suite.md`, bagian Hook suite); langkah 2 membuka Global Settings > Master Reference lalu Tab Measurement karena pembukaan layar dengan flag yang sudah diatur adalah objek uji.

## Test Steps

### TC-GS-UOM-17: Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelah Skip

1. Atur flag `guided_tooltip_seen_gs-measurement` ke "belum ada"
2. Buka Global Settings > Master Reference, lalu klik Tab Measurement
3. Verifikasi walkthrough muncul otomatis di Step 1
4. Klik [Skip]
5. Verifikasi [Skip] menutup walkthrough
6. Muat ulang halaman, lalu klik Tab Measurement
7. Verifikasi Table Tools tab Measurement tampil
8. Verifikasi walkthrough tidak muncul lagi setelah muat ulang

### TC-GS-UOM-18: Klik overlay gelap menutup walkthrough dan menyimpan flag seen

9. Atur flag `guided_tooltip_seen_gs-measurement` ke "belum ada"
10. Muat ulang halaman, lalu klik Tab Measurement
11. Klik area overlay gelap di luar tooltip
12. Verifikasi walkthrough tertutup
13. Muat ulang halaman, lalu klik Tab Measurement
14. Verifikasi Table Tools tab Measurement tampil
15. Verifikasi walkthrough tidak muncul lagi setelah muat ulang

### TC-GS-UOM-19: Tombol [?] memulai ulang walkthrough dari Step 1 tanpa mereset flag

16. Atur flag `guided_tooltip_seen_gs-measurement` ke true
17. Muat ulang halaman, lalu klik Tab Measurement
18. Klik `[?]`
19. Verifikasi walkthrough mulai dari Step 1
20. Klik [Next]
21. Klik [Back]
22. Verifikasi [Back] kembali ke Step 1
23. Klik [Next]
24. Klik [Done]
25. Verifikasi [Done] menutup walkthrough
26. Muat ulang halaman, lalu klik Tab Measurement
27. Verifikasi Table Tools tab Measurement tampil
28. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-GS-UOM-20: Resize viewport di tengah walkthrough menutupnya tanpa menyimpan flag seen

29. Atur flag `guided_tooltip_seen_gs-measurement` ke "belum ada"
30. Muat ulang halaman, lalu klik Tab Measurement
31. Tunggu walkthrough Step 1 tampil
32. Ubah lebar viewport saat Step 1 tampil
33. Verifikasi walkthrough tertutup saat resize
34. Muat ulang halaman, lalu klik Tab Measurement
35. Verifikasi walkthrough muncul lagi setelah muat ulang
36. Kembalikan lebar viewport ke ukuran awal

### TC-GS-UOM-334: Navigasi ke halaman lain di tengah walkthrough menutupnya tanpa menyimpan flag seen

37. Atur flag `guided_tooltip_seen_gs-measurement` ke "belum ada"
38. Muat ulang halaman, lalu klik Tab Measurement hingga walkthrough Step 1 tampil
39. Klik menu sidebar Global Settings > Activity Log
40. Verifikasi halaman Activity Log tampil
41. Verifikasi walkthrough tertutup saat berpindah ke halaman Activity Log
42. Kembali ke Global Settings > Master Reference, lalu klik Tab Measurement
43. Verifikasi walkthrough muncul lagi otomatis dari Step 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. Karena flag tersimpan permanen setelah TC-GS-UOM-17 dan TC-GS-UOM-18, spec mengatur flag di awal tiap TC (langkah 1, 9, 16, 29, 37) supaya tiap TC mulai dari kondisi flag yang disyaratkan TC sumber ("belum ada" untuk TC-GS-UOM-17, 18, 20, 334; true untuk TC-GS-UOM-19).
- Spec ini sekitar 43 langkah, di atas batas 35 langkah: seluruh blok satu kelas harness (flag Guided Tooltip di backend), satu akun, tanpa membuat data, dan tiap blok mengatur flagnya sendiri sehingga berdiri sendiri.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 9, 16, 29, dan 37 (mengatur flag), 6, 10, 13, 17, 26, 30, 34, 38, dan 42 (muat ulang atau buka halaman lalu klik Tab Measurement; tab aktif setelah muat ulang atau kembali dari halaman lain tidak disebut TC, sehingga langkah ini memastikan tab Measurement aktif), 31 dan 38 (menunggu Step 1 tampil), dan 36 (memulihkan viewport; hook `after` sebagai cadangan).
- Verifikasi tambahan di luar Expected TC: langkah 7, 14, dan 27 (Table Tools tab Measurement tampil sebagai anchor permukaan bagi asersi absence "walkthrough tidak muncul", bagian 8b butir 2) dan langkah 40 (halaman Activity Log tampil sebagai anchor bagi "walkthrough tertutup saat berpindah halaman").
- Kasus konten step, keyboard, dan Step 1 dilewati tanpa Create diuji di spec `TC-GS-UOM-E2E-010-guided-tooltip-konten-navigasi-keyboard`.
- Temuan untuk QA:
  - TC-GS-UOM-17 Post Condition (flag = true pada akun user) tidak punya langkah observasi di TC; padanannya adalah Expected c (walkthrough tidak muncul lagi setelah muat ulang, langkah 8), sehingga flag tidak dibaca langsung.
  - TC-GS-UOM-18 dan TC-GS-UOM-20 tidak menyebut tab yang aktif setelah muat ulang; spec memastikan tab Measurement aktif lewat klik Tab Measurement.
