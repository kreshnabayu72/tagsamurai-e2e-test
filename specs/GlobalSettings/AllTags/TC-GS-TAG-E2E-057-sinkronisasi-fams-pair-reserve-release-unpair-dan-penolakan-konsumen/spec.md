---
id: TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen
title: "Sinkronisasi FAMS: Pair (SSE), Reserved lalu Paired, Aset Ditolak, Unpair, Unpair QR, dan Identifier Belum Aktif Ditolak Modul Konsumen"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-293
  - TC-GS-TAG-294
  - TC-GS-TAG-295
  - TC-GS-TAG-296
  - TC-GS-TAG-297
  - TC-GS-TAG-321
coverage:
  web: automated
---

# Sinkronisasi FAMS: Pair (SSE), Reserved lalu Paired, Aset Ditolak, Unpair, Unpair QR, dan Identifier Belum Aktif Ditolak Modul Konsumen

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah status tag lewat aksi FAMS; unpair tag QR (TC-GS-TAG-297) yang mengeluarkan tag dari registri dijalankan terakhir.
- Akun aktor (ganti akun eksplisit hanya pada TC-GS-TAG-321):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun ini sebagai default suite.
  - Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`: pemicu lewat sesi API aktor (Register Asset final, pair, unpair) dan, pada TC-GS-TAG-321, sesi UI FAMS Register Asset karena penolakan diasersi di FAMS.
  - Approver aset di FAMS (TC-GS-TAG-294 dan 295: menyetujui atau menolak aset Draft): tidak ada di Pre-setup TC; akun dan kredensial disediakan tim FE (S-13). Sesi API aktor, hanya pemicu.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu Health dan License RFID – Object TAG). Baris yang dipakai: DD-15 `E28011606000020F00000001` (Available; Reserved oleh aset Draft pada TC-GS-TAG-295 lewat fixture BE), DD-01 `E2801160600002054D8A0001` (Paired), DD-05 `TAG-QR-00512` (QR Paired), DD-10 `04A224B2C15E82` (NFC Paired), DD-02 (Available), identifier uji `E2801160600002054D8A3003` (EPC valid belum diaktivasi). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum TC-GS-TAG-294.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Admin FAMS dan approver aset memicu Register Asset final, pendaftaran Draft, persetujuan, penolakan, dan unpair.
- Kemampuan teknis (disediakan tim FE/BE): sesi API FAMS untuk Register Asset final dengan tag, pendaftaran aset Draft/Waiting Approval dengan tag, persetujuan dan penolakan aset, unpair tag, dan unpair tag QR (mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD; Q-9, Q-15); simulasi reader di FAMS Register Asset untuk TC-GS-TAG-321 (D-4, Q-1); penanda event FAMS selesai diproses (Eventual/SSE); seed dan reset idempotent Seed Registri A dan keadaan Reserved oleh aset Draft.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-01, DD-05, DD-15), aset FAMS yang dibuat, dan sesi akun lewat fixture BE; kembalikan Rows per page ke 10.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-295: Aset ditolak, Reserved kembali Available

1. Atur DD-15 menjadi Reserved oleh aset Draft lewat fixture BE, muat ulang halaman, lalu klik Tab Not Paired
2. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
3. Verifikasi DD-15 berstatus `Reserved`
4. Verifikasi checkbox baris DD-15 Hidden
5. Tolak aset Draft di FAMS lewat sesi API approver aset hingga tersimpan
6. Verifikasi DD-15 berstatus `Available`
7. Verifikasi checkbox baris DD-15 tampil kembali
8. Buka menu baris DD-15, lalu klik `TAG Log`
9. Verifikasi entri `TAG Released by [pelaku approver]` dengan `Reason: Asset rejected`
10. Tutup popup TAG Log

### TC-GS-TAG-293: Pair tag Available dari FAMS Register Asset

11. Catat nilai kartu Health RFID – Object TAG
12. Klik Tab All
13. Catat nilai kartu License RFID – Object TAG
14. Klik Tab Not Paired
15. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
16. Simpan aset final dengan memindai tag DD-15 di FAMS Register Asset lewat sesi API Admin FAMS hingga tersimpan
17. Verifikasi kartu Health RFID – Object TAG berkurang 1 dari nilai yang dicatat
18. Verifikasi baris DD-15 hilang dari Tab Not Paired tanpa refresh manual
19. Klik Tab All
20. Verifikasi kartu License RFID – Object TAG tidak berubah dari nilai yang dicatat
21. Klik Tab Paired
22. Verifikasi Tab Paired memuat DD-15 berstatus `Paired`

### TC-GS-TAG-294: Reserved lalu Paired

23. Atur DD-15 menjadi Available lewat fixture BE, muat ulang halaman, lalu klik Tab Not Paired
24. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
25. Daftarkan aset di FAMS dengan memindai tag DD-15 sebagai Draft/Waiting Approval lewat sesi API Admin FAMS hingga tersimpan
26. Verifikasi DD-15 berstatus `Reserved` (badge secondary) di Tab Not Paired
27. Verifikasi checkbox baris DD-15 Hidden
28. Buka menu baris DD-15
29. Verifikasi menu hanya berisi `TAG Log`
30. Tutup menu
31. Setujui aset di FAMS lewat sesi API approver aset hingga tersimpan
32. Klik Tab Paired
33. Verifikasi DD-15 berstatus `Paired` di Tab Paired
34. Klik Tab Not Paired
35. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
36. Verifikasi sedikitnya satu baris tampil di Tab Not Paired
37. Verifikasi DD-15 tidak ada di Tab Not Paired

### TC-GS-TAG-296: Unpair tag RFID

38. Klik Tab Paired
39. Verifikasi sedikitnya satu baris tampil di Tab Paired
40. Lepas tautan tag DD-01 dari aset di FAMS lewat sesi API Admin FAMS hingga tersimpan
41. Verifikasi DD-01 hilang dari Tab Paired tanpa muat ulang
42. Klik Tab Not Paired
43. Verifikasi DD-01 berstatus `Available` di Tab Not Paired
44. Buka menu baris DD-01, lalu klik `TAG Log`
45. Verifikasi entri `Unpaired` dengan `Reason: Manual unpair`
46. Tutup popup TAG Log

### TC-GS-TAG-321: Identifier belum teraktivasi ditolak modul konsumen

47. Ganti akun ke Admin FAMS, buka FAMS Register Asset
48. Pindai `E2801160600002054D8A3003`
49. Verifikasi pemindaian ditolak oleh modul konsumen
50. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
51. Ketik Search `E2801160600002054D8A3003`, tekan Enter
52. Verifikasi pencarian menampilkan `No results found` (tag tidak muncul di registri Global Settings)
53. Klik `(←)` pada kotak Search

### TC-GS-TAG-297: Unpair tag QR

54. Klik Tab Paired
55. Verifikasi DD-10 tampil di Tab Paired
56. Lepas tautan tag QR DD-05 dari aset di FAMS lewat sesi API Admin FAMS hingga tersimpan dan event diproses
57. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab Paired
58. Klik Tab Not Paired
59. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
60. Verifikasi DD-02 tampil di Tab Not Paired
61. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab Not Paired (tidak kembali `Available`)
62. Klik Tab All
63. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
64. Verifikasi DD-02 tampil di Tab All
65. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab All
66. Ketik Search `TAG-QR-00512`, tekan Enter
67. Verifikasi pencarian menampilkan `No results found`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (67 langkah nominal). Alasan: enam TC satu topik (sinkronisasi status tag dari FAMS ke registri) dengan satu dataset Seed Registri A dan satu kelas harness; pemicu FAMS lewat sesi API aktor, dan blok berdiri sendiri karena DD-15 dipulihkan lewat fixture BE di langkah 1 dan 23.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (293, 294, 295, 296, 297, 321) disusun ulang menjadi 295, 293, 294, 296, 321, 297. TC-GS-TAG-295 mulai dari DD-15 Reserved lalu menghasilkan Available yang dipakai TC-GS-TAG-293; TC-GS-TAG-297 (tag QR keluar dari registri) di akhir.
- Seluruh aksi FAMS selain di TC-GS-TAG-321 dijalankan lewat sesi API aktor. Pada TC-GS-TAG-321 asersi ada di FAMS sehingga sesi UI dipakai dengan ganti akun eksplisit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 23 (memulihkan DD-15), 10 dan 46 (menutup popup TAG Log), 11 dan 13 (baseline kartu), 30 (menutup menu), 12, 14, 19, 21, 32, 34, 38, 42, 54, 58, dan 62 (pindah tab), 47 dan 50 (ganti akun), 51 (Search untuk menemukan baris target), 53 (membersihkan Search Tab All, karena Search tersimpan per tab dan akan menyaring DD-02 pada langkah 64), 35, 59, dan 63 (mengubah Rows per page menjadi 50 supaya baris halaman 2 dan 3 Tab Not Paired dan Tab All tampil; ukuran halaman tidak diasumsikan terbawa antar tab atau muat ulang). Rows per page 50 pada langkah 2, 15, dan 24 adalah langkah TC-GS-TAG-295, 293, dan 294; ukuran halaman dikembalikan ke 10 di hook `after`.
- Kartu License hanya tampil di Tab All, sedangkan kartu Health RFID – Object TAG dibaca di Tab Not Paired (TC-GS-TAG-293 langkah 3 dan Expected c): Health dicatat dan diasersi di Tab Not Paired (langkah 11, 17), License dicatat dan diasersi di Tab All (langkah 13, 20), dan baris DD-15 diasersi hilang dari Tab Not Paired (langkah 18) sebelum pindah ke Tab All.
- Asersi tambahan di luar Expected TC (S-03): langkah 3 dan 4 (keadaan awal Reserved dan checkbox Hidden agar "tampil kembali" bermakna), langkah 36, 39, 55, 60, dan 64 (data pembanding sebagai anchor absence), langkah 37, 61, dan 65 (absence tab sebagai penjabaran "pindah" dan "tidak tampil di tab manapun").
- Temuan untuk QA:
  - Q-1: TC-GS-TAG-293, 294, dan 321 berlabel `Manual Only — (b)` (scan hardware); kemampuan simulasi reader dan sesi API dicatat di Prerequisites (D-4).
  - Q-9: langkah dan selektor FAMS (Register Asset, persetujuan aset, unpair) tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - Q-10: TC-GS-TAG-321 menyebut penolakan oleh modul konsumen "copy mengikuti PRD modul konsumen" tanpa menyebut modul atau teks; spec hanya mengasersi pemindaian ditolak (tanpa teks).
  - Q-15: TC-GS-TAG-295 menulis `[pelaku approver]` (nama pelaku di entri TAG Log) tanpa nilai dan format penulisan nama; akun approver aset tidak ada di Pre-setup TC.
  - Q-4: identifier tetap; kondisi Seed Registri A dipulihkan lewat fixture BE sebelum spec.
  - Post Condition TC-GS-TAG-293 butir b ("TAG Log DD-15 memuat entri Paired") tidak punya langkah observasi di TC dan tidak diasersi; butir a identik dengan Expected b. TC-GS-TAG-294, 295, 296, dan 321 tidak punya Post Condition; Post Condition TC-GS-TAG-297 identik dengan Expected a.
  - TC-GS-TAG-321 melibatkan kelas d (scan di FAMS Register Asset) dan berada di spec ini; simulasi reader hanya memicu pemindaian identifier yang belum teraktivasi, sedangkan penolakan modul konsumen dan ketiadaan baris di registri yang diasersi.
