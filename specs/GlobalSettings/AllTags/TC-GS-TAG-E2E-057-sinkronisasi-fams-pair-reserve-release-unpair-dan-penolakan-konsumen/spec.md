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
  - Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`: pemicu lewat sesi API (P-2; Register Asset final, pair, unpair) dan, pada TC-GS-TAG-321, sesi UI FAMS Register Asset karena penolakan diasersi di FAMS.
  - Approver aset di FAMS (TC-GS-TAG-294 dan 295: menyetujui atau menolak aset Draft): tidak ada di Pre-setup TC; akun dan kredensial disediakan tim FE (S-13). Sesi API, hanya pemicu (P-2).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu Health dan License RFID – Object TAG). Baris yang dipakai: DD-15 `E28011606000020F00000001` (Available; Reserved oleh aset Draft pada TC-GS-TAG-295 lewat fixture BE), DD-01 `E2801160600002054D8A0001` (Paired), DD-05 `TAG-QR-00512` (QR Paired), DD-10 `04A224B2C15E82` (NFC Paired), DD-02 (Available), identifier uji `E2801160600002054D8A3003` (EPC valid belum diaktivasi). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum TC-GS-TAG-294.
- Kemampuan teknis (disediakan tim FE/BE): sesi API FAMS untuk Register Asset final dengan tag, pendaftaran aset Draft/Waiting Approval dengan tag, persetujuan dan penolakan aset, unpair tag, dan unpair tag QR (mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD; Q-9, Q-15); simulasi reader di FAMS Register Asset untuk TC-GS-TAG-321 (D-4, Q-1); penanda event FAMS selesai diproses (Eventual/SSE); seed dan reset idempotent Seed Registri A dan keadaan Reserved oleh aset Draft.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-01, DD-05, DD-15), aset FAMS yang dibuat, dan sesi akun lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-295: Aset ditolak, Reserved kembali Available

1. Atur DD-15 menjadi Reserved oleh aset Draft lewat fixture BE, muat ulang halaman, lalu klik Tab Not Paired
2. Verifikasi DD-15 berstatus `Reserved`
3. Verifikasi checkbox baris DD-15 Hidden
4. Tolak aset Draft di FAMS lewat sesi API approver aset hingga tersimpan
5. Verifikasi DD-15 berstatus `Available`
6. Verifikasi checkbox baris DD-15 tampil kembali
7. Buka menu baris DD-15, lalu klik `TAG Log`
8. Verifikasi entri `TAG Released by [pelaku approver]` dengan `Reason: Asset rejected`
9. Tutup popup TAG Log

### TC-GS-TAG-293: Pair tag Available dari FAMS Register Asset

10. Catat nilai kartu Health RFID – Object TAG
11. Klik Tab All
12. Catat nilai kartu License RFID – Object TAG
13. Klik Tab Not Paired
14. Simpan aset final dengan memindai tag DD-15 di FAMS Register Asset lewat sesi API Admin FAMS hingga tersimpan
15. Verifikasi kartu Health RFID – Object TAG berkurang 1 dari nilai yang dicatat
16. Verifikasi baris DD-15 hilang dari Tab Not Paired tanpa refresh manual
17. Klik Tab All
18. Verifikasi kartu License RFID – Object TAG tidak berubah dari nilai yang dicatat
19. Klik Tab Paired
20. Verifikasi Tab Paired memuat DD-15 berstatus `Paired`

### TC-GS-TAG-294: Reserved lalu Paired

21. Atur DD-15 menjadi Available lewat fixture BE, muat ulang halaman, lalu klik Tab Not Paired
22. Daftarkan aset di FAMS dengan memindai tag DD-15 sebagai Draft/Waiting Approval lewat sesi API Admin FAMS hingga tersimpan
23. Verifikasi DD-15 berstatus `Reserved` (badge secondary) di Tab Not Paired
24. Verifikasi checkbox baris DD-15 Hidden
25. Buka menu baris DD-15
26. Verifikasi menu hanya berisi `TAG Log`
27. Tutup menu
28. Setujui aset di FAMS lewat sesi API approver aset hingga tersimpan
29. Klik Tab Paired
30. Verifikasi DD-15 berstatus `Paired` di Tab Paired
31. Klik Tab Not Paired
32. Verifikasi sedikitnya satu baris tampil di Tab Not Paired
33. Verifikasi DD-15 tidak ada di Tab Not Paired

### TC-GS-TAG-296: Unpair tag RFID

34. Klik Tab Paired
35. Verifikasi sedikitnya satu baris tampil di Tab Paired
36. Lepas tautan tag DD-01 dari aset di FAMS lewat sesi API Admin FAMS hingga tersimpan
37. Verifikasi DD-01 hilang dari Tab Paired tanpa muat ulang
38. Klik Tab Not Paired
39. Verifikasi DD-01 berstatus `Available` di Tab Not Paired
40. Buka menu baris DD-01, lalu klik `TAG Log`
41. Verifikasi entri `Unpaired` dengan `Reason: Manual unpair`
42. Tutup popup TAG Log

### TC-GS-TAG-321: Identifier belum teraktivasi ditolak modul konsumen

43. Ganti akun ke Admin FAMS, buka FAMS Register Asset
44. Pindai `E2801160600002054D8A3003`
45. Verifikasi pemindaian ditolak oleh modul konsumen
46. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
47. Ketik Search `E2801160600002054D8A3003`, tekan Enter
48. Verifikasi pencarian menampilkan `No results found` (tag tidak muncul di registri Global Settings)

### TC-GS-TAG-297: Unpair tag QR

49. Klik Tab Paired
50. Verifikasi DD-10 tampil di Tab Paired
51. Lepas tautan tag QR DD-05 dari aset di FAMS lewat sesi API Admin FAMS hingga tersimpan dan event diproses
52. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab Paired
53. Klik Tab Not Paired
54. Verifikasi DD-02 tampil di Tab Not Paired
55. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab Not Paired (tidak kembali `Available`)
56. Klik Tab All
57. Verifikasi DD-02 tampil di Tab All
58. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab All
59. Ketik Search `TAG-QR-00512`, tekan Enter
60. Verifikasi pencarian menampilkan `No results found`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (60 langkah nominal). Alasan: enam TC satu topik (sinkronisasi status tag dari FAMS ke registri) dengan satu dataset Seed Registri A dan satu kelas harness; pemicu FAMS lewat sesi API (P-2), dan blok berdiri sendiri karena DD-15 dipulihkan lewat fixture BE di langkah 1 dan 21.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (293, 294, 295, 296, 297, 321) disusun ulang menjadi 295, 293, 294, 296, 321, 297. TC-GS-TAG-295 mulai dari DD-15 Reserved lalu menghasilkan Available yang dipakai TC-GS-TAG-293; TC-GS-TAG-297 (tag QR keluar dari registri) di akhir.
- Pengecualian P-2: seluruh aksi FAMS selain di TC-GS-TAG-321 (Register Asset final, pendaftaran Draft, persetujuan, penolakan, unpair) hanyalah pemicu state lewat sesi API; objek asersi adalah status dan baris di registri Global Settings. Pada TC-GS-TAG-321 asersi ada di FAMS sehingga sesi UI dipakai dengan ganti akun eksplisit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 21 (memulihkan DD-15), 9 dan 42 (menutup popup TAG Log), 10 dan 12 (baseline kartu), 27 (menutup menu), 11, 13, 17, 19, 29, 31, 34, 38, 49, 53, dan 56 (pindah tab), 43 dan 46 (ganti akun), 47 (Search untuk menemukan baris target).
- Kartu License hanya tampil di Tab All, sedangkan kartu Health RFID – Object TAG dibaca di Tab Not Paired: pada TC-GS-TAG-293 Health dicatat dan diasersi di Tab Not Paired (langkah 10, 15), License dicatat dan diasersi di Tab All (langkah 12, 18), dan baris DD-15 diasersi hilang dari Tab Not Paired (langkah 16) sebelum pindah ke Tab All (S-03).
- Asersi tambahan di luar Expected TC (S-03): langkah 2 dan 3 (keadaan awal Reserved dan checkbox Hidden agar "tampil kembali" bermakna), langkah 32, 35, 50, 54, dan 57 (data pembanding sebagai anchor absence), langkah 33, 55, dan 58 (absence tab sebagai penjabaran "pindah" dan "tidak tampil di tab manapun").
- Temuan untuk QA:
  - Q-1: TC-GS-TAG-293, 294, dan 321 berlabel `Manual Only — (b)` (scan hardware); kemampuan simulasi reader dan sesi API dicatat di Prerequisites (D-4).
  - Q-9: langkah dan selektor FAMS (Register Asset, persetujuan aset, unpair) tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - Q-10: TC-GS-TAG-321 menyebut penolakan oleh modul konsumen "copy mengikuti PRD modul konsumen" tanpa menyebut modul atau teks; spec hanya mengasersi pemindaian ditolak (tanpa teks).
  - Q-15: TC-GS-TAG-295 menulis `[pelaku approver]` (nama pelaku di entri TAG Log) tanpa nilai dan format penulisan nama; akun approver aset tidak ada di Pre-setup TC.
  - Q-4: identifier tetap; kondisi Seed Registri A dipulihkan lewat fixture BE sebelum spec.
  - Post Condition TC-GS-TAG-293 butir b ("TAG Log DD-15 memuat entri Paired") tidak punya langkah observasi di TC dan tidak diasersi; butir a identik dengan Expected b. TC-GS-TAG-294, 295, 296, dan 321 tidak punya Post Condition; Post Condition TC-GS-TAG-297 identik dengan Expected a.
  - TC-GS-TAG-321 melibatkan kelas d (scan di FAMS Register Asset) tetapi ditempatkan di spec fungsional sesuai rencana.
