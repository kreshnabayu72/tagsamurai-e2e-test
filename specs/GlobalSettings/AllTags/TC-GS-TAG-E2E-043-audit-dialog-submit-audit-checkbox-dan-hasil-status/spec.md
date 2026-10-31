---
id: TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status
title: "Audit: Dialog Submit Audit, Mark all as Damaged/Missing, Tanpa Centang, Retired Tetap, dan Induk Combined Not Scanned"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-128
  - TC-GS-TAG-129
  - TC-GS-TAG-130
  - TC-GS-TAG-131
  - TC-GS-TAG-174
  - TC-GS-TAG-339
coverage:
  web: automated
---

# Audit: Dialog Submit Audit, Mark all as Damaged/Missing, Tanpa Centang, Retired Tetap, dan Induk Combined Not Scanned

## Prerequisites

- Mode: FE+BE (backend nyata; reader tersimulasi).
- Akun aktor: Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`, `Spectra.env.GS_TC_AUDIT_PASSWORD`. Login di hook `before`. Tidak ada ganti akun. Nama env belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup (Seed Client Audit, dipulihkan lewat fixture BE sebelum spec dan antar blok yang meng-commit, S-12): AU1 (DD-31) `E2801160600002054D8A5001` RFID Object Available (combined dengan AUN); AU2 (DD-32) `E2801160600002054D8A5002` Damaged/Missing; AU3 (DD-33) `E2801160600002054D8A5003` Retired; AU4 (DD-34) `E2801160600002054D8A5004` Available; AU5 (DD-35) `E2801160600002054D8A5005` Reserved; AU6 (DD-36) `E2801160600002054D8A5006` Paired; AU7 (DD-37) `E2801160600002054D8A5007` To be Returned; AUN (DD-38) NFC `04A224B2C15E95` Available (combined dengan AU1). AU5, AU6, dan AU7 dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis (disediakan tim FE, kelas d harness hardware, D-4, Q-1): simulasi Handheld Reader `Zebra RFD40 (SN-2201)`; `Pindai X` pada popup Audit berarti memulai sesi pemindaian pada popup (kontrol pemicu disediakan tim FE), X dipindai, lalu klik [Stop] pada Floating Status Widget; baca jumlah entri Event Log Tab Audit TAG, Activity Log (Action `Update TAG Condition` per kode), dan TAG Log AU1 dan NFC (baseline); seed/reset Seed Client Audit antar blok.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): reset Seed Client Audit, buang hasil scan popup Audit yang tersisa.
- Suite serial (`parallel: false`). Spec mengubah data Seed Client Audit (dipulihkan seperti di atas). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-339: Dialog Submit Audit dengan satu tag Not Scanned memakai bentuk tunggal

1. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
2. Pindai AU1, AU2, dan AU4 (AU3 Retired tidak dipindai)
3. Klik [Submit]
4. Verifikasi dialog `Submit Audit` dengan body "1 TAG was not found during this audit."
5. Verifikasi checkbox `Mark all as Damaged/Missing` dicentang
6. Klik [Cancel]
7. Klik `[✕]`, lalu klik [Discard] pada dialog (membuang hasil scan)

### TC-GS-TAG-128: Submit dengan baris Not Scanned memunculkan dialog Submit Audit

8. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
9. Pindai AU1 dan AU2 saja
10. Klik [Submit]
11. Verifikasi dialog `Submit Audit` dengan body "2 TAGs were not found during this audit." (seluruh baris Not Scanned dihitung, termasuk Retired)
12. Verifikasi satu checkbox `Mark all as Damaged/Missing` dicentang default tanpa rincian per tipe
13. Verifikasi tombol [Cancel] dan [Confirm] pada dialog
14. Klik [Cancel]
15. Verifikasi dialog tertutup
16. Verifikasi tanpa commit: kolom `Status` AU2 pada popup masih `Damaged/Missing`
17. Verifikasi popup Audit tetap terbuka dengan progres (AU1 dan AU2 berlencana `✓ Verified`)
18. Klik `[✕]`, lalu klik [Discard] pada dialog (membuang hasil scan)

### TC-GS-TAG-129: Confirm dengan checkbox dicentang

19. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
20. Pindai AU2 saja
21. Klik [Submit]
22. Verifikasi dialog `Submit Audit` menampilkan "3 TAGs were not found during this audit."
23. Biarkan checkbox dicentang dan klik [Confirm]
24. Verifikasi toast sukses: "Success, audit has been submitted."
25. Klik Tab Not Paired, ketik Search `E2801160600002054D8A500`, tekan Enter
26. Verifikasi AU2 berubah dari `Damaged/Missing` menjadi `Available`
27. Verifikasi AU1 berubah dari `Available` menjadi `Damaged/Missing`
28. Verifikasi AU4 berubah dari `Available` menjadi `Damaged/Missing`
29. Verifikasi AU3 (Retired) tetap `Retired`
30. Ganti isi kotak search dengan `04A224B2C15E95`, tekan Enter
31. Verifikasi NFC `04A224B2C15E95` (sibling AU1, berbagi satu Status) berubah dari `Available` menjadi `Damaged/Missing`
32. Pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-130: Confirm dengan checkbox tidak dicentang

33. Buka Event Log > Tab Audit TAG, catat jumlah entri sebagai baseline `E130`, lalu tutup Event Log
34. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
35. Pindai AU2 saja
36. Klik [Submit]
37. Hapus centang `Mark all as Damaged/Missing`
38. Klik [Confirm]
39. Ganti isi kotak search dengan `E2801160600002054D8A500`, tekan Enter
40. Verifikasi AU2 menjadi `Available`
41. Verifikasi AU1 dan AU4 tetap `Available`
42. Verifikasi AU3 tetap `Retired`
43. Buka Event Log > Tab Audit TAG dan buka entri sesi baru (jumlah entri bertambah satu dari `E130`)
44. Verifikasi `Not Found` sesi tersebut bernilai `3`
45. Verifikasi `Not Found Action` sesi tersebut bernilai `Kept previous status`
46. Tutup Event Log, lalu pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-131: Baris Retired tidak pernah berubah status oleh Audit saat Verified

47. Buka Event Log > Tab Audit TAG, catat jumlah entri sebagai baseline `E131`, lalu tutup Event Log
48. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
49. Pindai AU3 (Retired), AU1, AU2, dan AU4
50. Klik [Submit]
51. Ganti isi kotak search dengan `E2801160600002054D8A5003`, tekan Enter
52. Verifikasi AU3 tetap `Retired` setelah Submit
53. Buka Event Log > Tab Audit TAG dan buka Audit Detail sesi baru (jumlah entri bertambah satu dari `E131`)
54. Verifikasi kolom `Status After` AU3 di Audit Detail bernilai `Retired`
55. Tutup Audit Detail dan Event Log, lalu pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-174: Induk combined Not Scanned ditandai Damaged/Missing, sibling ikut

56. Buka Activity Log, catat jumlah entri Action `Update TAG Condition` untuk AU1 sebagai `UA1` dan untuk NFC `04A224B2C15E95` sebagai `UAN`
57. Buka Global Settings > TAG > Tab Not Paired, ketik Search `E2801160600002054D8A5001`, tekan Enter, buka menu baris AU1 > `TAG Log`, catat jumlah entri sebagai `TL1`, lalu tutup popup TAG Log
58. Ganti isi kotak search dengan `04A224B2C15E95`, tekan Enter, buka menu baris NFC `04A224B2C15E95` > `TAG Log`, catat jumlah entri sebagai `TLN`, lalu tutup popup TAG Log
59. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
60. Pindai AU2, AU3, dan AU4 (AU1 tidak dipindai)
61. Klik [Submit]
62. Biarkan checkbox dicentang dan klik [Confirm]
63. Ganti isi kotak search dengan `E2801160600002054D8A5001`, tekan Enter
64. Verifikasi AU1 berstatus `Damaged/Missing`
65. Ganti isi kotak search dengan `04A224B2C15E95`, tekan Enter
66. Verifikasi NFC `04A224B2C15E95` berstatus `Damaged/Missing` (berbagi satu Status dengan AU1)
67. Buka Activity Log
68. Verifikasi jumlah entri `Update TAG Condition` untuk AU1 bertambah satu dari `UA1`
69. Verifikasi jumlah entri `Update TAG Condition` untuk NFC `04A224B2C15E95` bertambah satu dari `UAN`
70. Buka Global Settings > TAG > Tab Not Paired, ketik Search `04A224B2C15E95`, tekan Enter, lalu buka menu baris NFC `04A224B2C15E95` > `TAG Log`
71. Verifikasi popup TAG Log NFC tampil
72. Verifikasi jumlah entri TAG Log NFC sama dengan `TLN` (tidak ada entri baru apa pun)
73. Tutup popup TAG Log, ganti isi kotak search dengan `E2801160600002054D8A5001`, tekan Enter, lalu buka menu baris AU1 > `TAG Log`
74. Verifikasi TAG Log AU1 memuat entri `Audit` baru (jumlah entri bertambah satu dari `TL1`) dengan `Result: Not Found`
75. Verifikasi entri `Audit` tersebut memuat `Status: Available → Damaged/Missing`

## Notes

- Mode: FE+BE. Kelas d (harness hardware tersimulasi; D-4, Q-1). P-1 (S-05, keputusan D-1): klausa absence TC-GS-TAG-174 butir c (TAG Log NFC tanpa entri baru) berada di spec asal dengan baseline `TLN` dan anchor positif langkah 71 dan 74.
- Spec melewati sekitar 35 langkah (75 langkah). Alasan: seluruh blok satu topik aksi (Submit Audit dan hasil status) dan satu kelas harness (reader tersimulasi) atas satu dataset Seed Client Audit; tiap blok berdiri sendiri karena hasil scan dibuang (langkah 7, 18) dan Seed Client Audit dipulihkan antar blok yang meng-commit (langkah 32, 46, 55); kegagalan satu blok tidak membuat blok lain kehilangan makna kecuali kegagalan reader tersimulasi. Pemisahan lebih lanjut tidak dipilih karena semua blok memakai dataset dan dialog `Submit Audit` yang sama.
- Urutan: blok tanpa commit (TC-GS-TAG-339, 128) di awal; blok yang meng-commit sesudahnya.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 6, 7, 8, 14, 18, 19, 25, 30, 32, 33, 34, 37, 39, 43, 46, 47, 48, 51, 53, 55, 56, 57, 58, 59, 63, 65, 67, 70, 73 (membuka popup dan surface log, Search untuk menemukan baris target, mencatat baseline, membuang hasil scan, pemulihan).
- Pembagian TC lintas spec: TC-GS-TAG-127 (Submit semua Verified, tanpa dialog) dan TC-GS-TAG-170/171 di spec 042; TC-GS-TAG-135 (Dialog 7 tutup popup) di spec 044.
- Temuan untuk QA:
  - Q-1: simulasi reader tidak didefinisikan di TC, PRD, LLD; ditulis "disediakan tim FE".
  - TC-GS-TAG-129 Post Condition b dan c (Event Log Audit Not Found Action Marked as Damaged/Missing; Activity Log memuat Audit TAG dan empat entri Update TAG Condition) tidak punya langkah observasi di TC dan tidak diasersi. Sebagian padanannya diasersi di TC-GS-TAG-174 (Activity Log `Update TAG Condition` AU1 dan NFC).
  - TC-GS-TAG-130 Expected c tidak menyebut tempat membaca `Not Found` dan `Not Found Action`; spec memakai Event Log > Tab Audit TAG (nama tab diturunkan dari TC-GS-TAG-109 untuk Activate) dan mengidentifikasi sesi baru lewat selisih jumlah entri (S-12).
  - TC-GS-TAG-131 Expected b menyebut "Audit Detail"; jalur membukanya tidak ditulis di TC (spec memakai Event Log > Tab Audit TAG).
  - TC-GS-TAG-174 Expected b/c: filter atau pencarian Activity Log per kode tidak dijelaskan; spec menghitung entri Action `Update TAG Condition` per kode terhadap baseline.
  - TC-GS-TAG-128 Expected c ("dialog tertutup tanpa commit; popup Audit tetap dengan progres") dipecah menjadi tiga klausa (langkah 15 sampai 17).
