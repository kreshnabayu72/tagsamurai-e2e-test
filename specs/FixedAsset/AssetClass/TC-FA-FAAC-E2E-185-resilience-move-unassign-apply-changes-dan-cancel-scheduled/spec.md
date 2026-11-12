---
id: TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled
title: "Resilience: Move, Unassign Massal, Apply Changes, dan Cancel Scheduled Version Gagal karena Error Server 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-211
  - TC-FA-FAAC-212
  - TC-FA-FAAC-238
  - TC-FA-FAAC-311
  - TC-FA-FAAC-335
coverage:
  web: automated
---

# Resilience: Move, Unassign Massal, Apply Changes, dan Cancel Scheduled Version Gagal karena Error Server 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis: `Spectra.intercept` parsial yang memaksa respons HTTP 5xx pada permintaan Move, Unassign, Edit (Apply Changes), dan Cancel Scheduled Version di atas backend nyata, dilepas segera sesudah pemicu (S-09); fixture BE yang memaksa kegagalan Move sesudah Asset Name pertama berhasil diproses dan mematikannya kembali (TC-212, "disediakan tim FE/BE", tanpa endpoint karangan). Endpoint permintaan tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga dipilih tim FE saat script. Pembacaan keanggotaan Asset Name, jumlah Asset Name per Asset Class, dan jumlah entri Changelog Asset Class, System Log, dan Activity Log lewat kemampuan baca BE (audit trail permanen, asersi log memakai selisih terhadap baseline, bukan angka absolut).
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser.
- Data seed Pre-setup (kode dan nama literal TC, disediakan fixture BE): Asset Class `Heavy Equipment` (`HEAVY-EQ`, Active) dengan Asset Name ter-assign `Excavator PC200` (8 aset aktif), `Wheel Loader` (4 aset aktif), `Crane Rental Unit` (0 aset aktif), `Rock Crusher`, `Road Roller`, dan `Grader G12` (masing-masing 0 aset aktif); `Machinery` (`MACHINERY`, Active) dengan Asset Name `Floor Jack` dan `Air Compressor Small` (0 aset aktif); Asset Class `B-ASSETS` (satu Asset Name dengan 5 aset aktif, Method `Straight Line`, Useful Life `60`, belum pernah diposting); Asset Class `B-SCHED` dengan versi Scheduled sejak M+2 dan aktor memiliki Update. Fixture BE memulihkan keanggotaan Asset Name dan Useful Life di hook `after`.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` menurut butir Keadaan awal precondition TC-211; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-211: Move gagal karena error server, dialog tetap terbuka dan pilihan dipertahankan

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-211)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel, lalu klik tab `Asset Names`
4. Klik ikon `⋯` pada baris `Crane Rental Unit`, lalu pilih `Move`
5. Pilih `Destination Asset Class` = `MACHINERY – Machinery`
6. Pasang intercept respons 5xx pada permintaan Move, lalu klik `[Move]`
7. Lepas intercept respons 5xx
8. Verifikasi toast error `Error, failed to move asset name.`
9. Verifikasi dialog Move tetap terbuka dengan tujuan `MACHINERY – Machinery` tetap terpilih
10. Verifikasi `[Move]` dapat dicoba ulang
11. Verifikasi `Crane Rental Unit` tetap di `Heavy Equipment`
12. Klik `[Cancel]` pada dialog Move

### TC-FA-FAAC-212: Move massal diulang setelah kegagalan sebagian hanya memproses Asset Name yang belum diproses

13. Centang baris `Rock Crusher`, `Road Roller`, dan `Grader G12`, klik `Bulk Action`, lalu pilih `Move to another asset class`
14. Pilih `Destination Asset Class` = `MACHINERY – Machinery`
15. Lewat fixture BE siapkan kegagalan setelah Asset Name pertama diproses, lalu klik `[Move]`
16. Verifikasi toast error `Error, failed to move asset name.` (percobaan pertama)
17. Verifikasi dialog tetap terbuka
18. Verifikasi satu Asset Name sudah berpindah ke `Machinery`
19. Klik `[Cancel]` pada dialog Move
20. Segarkan daftar tab `Asset Names`
21. Centang dua Asset Name yang tersisa, klik `Bulk Action`, lalu pilih `Move to another asset class`
22. Pilih `Destination Asset Class` = `MACHINERY – Machinery`
23. Matikan fixture kegagalan, lalu klik `[Move]`
24. Verifikasi toast sukses `Success, asset name has been moved.` (percobaan kedua)
25. Verifikasi jumlah Asset Name pada `Heavy Equipment` sama dengan baris yang tampil di tab `Asset Names`
26. Klik breadcrumb `Asset Class`
27. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
28. Klik link Class Code `MACHINERY` di tabel, lalu klik tab `Asset Names`
29. Verifikasi `Rock Crusher`, `Road Roller`, dan `Grader G12` berada di `Machinery` tepat sekali
30. Verifikasi jumlah Asset Name pada `Machinery` sama dengan baris yang tampil di tab `Asset Names`

### TC-FA-FAAC-238: Unassign massal gagal karena error server mempertahankan seleksi

31. Centang baris `Floor Jack` dan `Air Compressor Small`, klik `Bulk Action`, lalu pilih `Unassign`
32. Pasang intercept respons 5xx, lalu klik `[Unassign]` pada dialog
33. Lepas intercept respons 5xx
34. Verifikasi toast error `Error, failed to unassign asset name.`
35. Verifikasi seleksi kedua baris dipertahankan
36. Verifikasi `Floor Jack` dan `Air Compressor Small` tetap tampil di tab `Asset Names` (tidak ada Asset Name yang hilang)
37. Klik `Unselect All`

### TC-FA-FAAC-311: Apply gagal 5xx mempertahankan dialog

38. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
39. Klik breadcrumb `Asset Class`
40. Ganti isi kotak search dengan `B-ASSETS`, tekan Enter
41. Klik link Class Code `B-ASSETS` di tabel
42. Klik tab `Depreciation`
43. Ubah Useful Life menjadi `48`
44. Klik `Save`
45. Pasang intercept respons 5xx pada permintaan Apply, lalu klik `Apply`
46. Lepas intercept respons 5xx
47. Verifikasi toast error `Error, failed to update asset class.`
48. Verifikasi dialog Apply Changes tetap terbuka dengan Effective From dan checkbox dipertahankan
49. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
50. Klik `[Cancel]` pada dialog Apply Changes
51. Kembalikan Useful Life ke nilai tersimpan `60`

### TC-FA-FAAC-335: Cancel Scheduled Version gagal 5xx

52. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
53. Klik breadcrumb `Asset Class`
54. Ganti isi kotak search dengan `B-SCHED`, tekan Enter
55. Klik link Class Code `B-SCHED` di tabel
56. Klik `Cancel scheduled version`
57. Pasang intercept respons 5xx, lalu klik `Cancel version`
58. Lepas intercept respons 5xx
59. Verifikasi toast error `Error, failed to cancel scheduled version.`
60. Verifikasi Alert versi Scheduled tetap tampil
61. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan nomor TC supaya Asset Class yang sama (`HEAVY-EQ`, `MACHINERY`) dipakai berturutan dan form dirty (Useful Life `B-ASSETS`) dipulihkan sebelum TC berikutnya (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (fixture BE menyetel keadaan awal dinamis TC-211, S-14); langkah 2, 27, 40, dan 54 (Search untuk menemukan baris target, R-16); langkah 12, 19, dan 50 (menutup dialog Move dan Apply Changes dengan `[Cancel]`, yang tidak memunculkan dialog `Unsaved Changes` menurut Catatan Cakupan TC-698 dan TC-699); langkah 20 (menyegarkan daftar, sesuai langkah TC-212); langkah 26, 39, dan 53 (kembali ke tabel); langkah 37 (membersihkan seleksi, S-09); langkah 51 (mengembalikan field ke nilai tersimpan, S-09). Intercept dilepas segera sesudah pemicu (langkah 7, 33, 46, dan 58; S-09).
3. Prinsip 13g dan S-12: klausa "tidak ada log" pada TC-311 dan TC-335 adalah asersi jumlah pada TC fungsional (aksi UI dengan kegagalan server yang dipaksa, kelas b; bukan request langsung yang ditolak server) sehingga diasersi di spec ini dengan `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog Asset Class, System Log, Activity Log), sesudah toast error server sebagai anchor positif; baseline dicatat sebelum pemicu tiap TC.
4. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `HEAVY-EQ`, `MACHINERY`, `B-ASSETS`, `B-SCHED`, dan nama Asset Name literal; nilai dipakai apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nilai itu. TC-212 memindahkan tiga Asset Name seed ke `Machinery`; fixture BE memulihkannya di hook `after`.
5. Alasan di atas sekitar 35 langkah: kelima blok satu kelas harness (b), berdiri sendiri dengan data dan baseline sendiri; konvensi bagian 3 prinsip 13 menetapkan kelas ringan cukup satu spec per kelas per modul, bukan per aksi. Kegagalan satu blok tidak membuat blok lain kehilangan makna dan tiap blok memulihkan state-nya sebelum blok berikutnya.
6. Temuan untuk QA: TC-238 menulis "daftar disegarkan" tanpa cara mengamatinya; spec hanya mengasersi seleksi dipertahankan dan Asset Name tetap tampil. TC-311 tidak menyebut Effective From dan label tombol penutup dialog Apply Changes, dan TC-311 serta TC-335 tidak menyebut tombol penutup dialog; spec memakai `[Cancel]`. TC-212 dan TC-211 tidak menyebut Effective From pada Move Asset Name tanpa aset aktif; spec mengikuti TC dan tidak mengisinya. TC-211 dan TC-212 memakai Asset Class `HEAVY-EQ` yang sama dengan seed berbeda (tiga Asset Name per TC); spec memakai keenam Asset Name pada satu seed.
