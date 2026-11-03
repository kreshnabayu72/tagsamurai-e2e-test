---
id: TC-FA-CAT-E2E-093-penerapan-seleksi-di-t0-pada-suspended-expired-dan-log-penyubmit-terakhir
title: "Penerapan Seleksi Tersimpan di T-0 pada Client Suspended atau Expired dan Log Penyubmit Terakhir"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-611
  - TC-FA-CAT-612
coverage:
  web: automated
---

# Penerapan Seleksi Tersimpan di T-0 pada Client Suspended atau Expired dan Log Penyubmit Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatPreT0Susp (Pre-setup #47); halaman dibuka hook `beforeEach` suite. Langkah 18 berganti akun ke Total Control client CatPreT0 (Pre-setup #32) dan langkah 24 ke Total Control Kedua (Pre-setup #46, akun disediakan tim FE) dengan `Spectra.env.FA_TC_PASSWORD`; hook `after` mengembalikan sesi ke akun default suite.
- Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) mengubah status entitas CatPreT0Susp (langkah 7 dan 9).
- Data Pre-setup #47 (CatPreT0Susp, downgrade terjadwal Professional cap 100 ke Starter cap 5, T-0 belum tiba): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Data Pre-setup #32 (CatPreT0, kondisi yang sama dengan #47, T-0 belum tiba) untuk TC-FA-CAT-612.
- Parameter iterasi langkah 1 sampai 17 (TC-FA-CAT-611):

  | Varian | Status entitas pada langkah 7 |
  |---|---|
  | Suspended | Suspended |
  | Expired | Expired |

- Waktu: T-0 dibaca dari data downgrade terjadwal client lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 8 dan 30 (bagian 6 konvensi). Kemampuan disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog `Marked as Excess (Category Consolidation)` (baseline NM), Activity Log (NA), dan System Log kedua akun (NS1 dan NS2) sebelum aksi (S-12) pada langkah 6 dan 29.
- State yang diubah spec: jam server, status entitas CatPreT0Susp, seleksi tersimpan CatPreT0Susp dan CatPreT0. Pemulihan seed, status entitas, dan jam dilakukan fixture backend (disediakan tim FE/BE) pada langkah 1, 19, dan 36 (jam dipulihkan sebelum Activity Log dan System Log dibuka, S-09) serta di hook `after`. Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-611: Penerapan seleksi tersimpan di T-0 tetap berjalan pada client Suspended atau Expired

1. Untuk setiap varian pada tabel parameter (langkah 1 sampai 17): pulihkan seed Pre-setup #47 (T-0 belum tiba, entitas aktif) lewat fixture dan muat ulang halaman Categories
2. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
3. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
4. Klik `[Save Selection]`
5. Tunggu aksi selesai
6. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
7. Principal Automation (sesi API) mengubah status entitas CatPreT0Susp menjadi status varian hingga tersimpan
8. Majukan jam server dan jam browser ke T-0 hingga tersimpan
9. Principal Automation (sesi API) mengaktifkan kembali entitas hingga tersimpan
10. Buka Fixed Asset > Settings > Categories
11. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear` berstatus usable (seleksi tersimpan tetap diterapkan)
12. Verifikasi `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` yang tidak dicentang berstatus Excess
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tidak tampil (tanpa penolakan 403)
14. Buka Modal Changelog
15. Verifikasi Changelog bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` (NM + 3) untuk `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy`
16. Verifikasi Modified By tiap baris baru adalah aktor Total Control penyubmit, bukan `System`
17. Tutup Modal Changelog

### TC-FA-CAT-612: Log penerapan seleksi tersimpan di T-0, aktor penyubmit terakhir pada Changelog dan Activity Log, System Log ditempel ke penyubmit

18. Ganti akun: logout, lalu login sebagai Total Control client CatPreT0 (Pre-setup #32)
19. Pulihkan seed Pre-setup #32 (T-0 belum tiba) dan jam lewat fixture, lalu muat ulang halaman Categories
20. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
21. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, dan `Delta Supply`
22. Klik `[Save Selection]`
23. Tunggu aksi selesai
24. Ganti akun: logout, lalu login sebagai Total Control Kedua (Pre-setup #46)
25. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
26. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
27. Klik `[Save Selection]`
28. Tunggu aksi selesai
29. Catat baseline NM, NA, NS1 (System Log Total Control pertama), dan NS2 (System Log Total Control Kedua)
30. Majukan jam server dan jam browser ke T-0 hingga tersimpan
31. Buka Fixed Asset > Settings > Categories lalu buka Modal Changelog
32. Verifikasi Changelog bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` (NM + 3) untuk `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy`
33. Verifikasi Modified By tiap baris baru adalah Total Control Kedua (penyubmit terakhir), bukan Total Control pertama dan bukan `System`
34. Verifikasi Date tiap baris baru adalah waktu penerapan di T-0, bukan waktu Submit
35. Tutup Modal Changelog
36. Pulihkan jam server dan jam browser ke waktu nyata hingga tersimpan (fixture, disediakan tim FE/BE)
37. Buka Activity Log
38. Verifikasi Activity Log bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` (NA + 3) dengan Modified By Total Control Kedua
39. Buka Detail User Total Control Kedua > Tab System Log
40. Verifikasi System Log Total Control Kedua bertambah tepat tiga baris yang sama (NS2 + 3)
41. Buka Detail User Total Control pertama > Tab System Log
42. Verifikasi jumlah baris System Log Total Control pertama sama dengan NS1 (tidak memuat baris dari penerapan ini)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (42 langkah nominal, sekitar 59 dengan ekspansi langkah 1 sampai 17 untuk dua varian). Alasan: seluruh blok satu kelas (harness eksternal: time-travel T-0 dan perubahan status entitas) dan berdiri sendiri; tiap blok memulai dari seed yang dipulihkan, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Dua varian TC-FA-CAT-611 berbagi langkah identik (S-04) dan ditulis sebagai satu blok iterasi (8b.7).
- Principal Automation lewat sesi API bukan konteks kedua (tidak ada `P-2`). Total Control Kedua pada TC-FA-CAT-612 melakukan Submit dan membaca log dari sesi UI sendiri secara berurutan (ganti akun eksplisit pada langkah 18 dan 24), bukan sesi paralel.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 19 (pemulihan seed), 5, 23, 28 (menunggu aksi selesai), 6 dan 29 (baseline), 7, 8, 9, 30 (pemicu), 10, 31 (navigasi), 17 dan 35 (menutup Modal Changelog), 36 (pemulihan jam).
- Asersi tidak adanya toast langkah 13 memakai langkah 11 (kategori usable tampil pada halaman yang sama) sebagai anchor positif; asersi jumlah langkah 42 memakai langkah 40 sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-611 langkah 6 menyuruh Principal "mengaktifkan kembali entitas" untuk varian Expired tanpa menyebut mekanisme; spec memakai langkah Principal yang sama dengan varian Suspended.
  - TC-FA-CAT-612 menyebut "Total Control Kedua" tanpa client; spec memakai akun Pre-setup #46 pada client CatPreT0.
  - TC-FA-CAT-611 menyebut Expected "tanpa toast"; spec hanya mengasersi tidak adanya toast penolakan yang disebut pada langkah 13 karena toast lain tidak terdefinisi.
