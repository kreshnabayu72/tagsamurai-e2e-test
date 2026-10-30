---
id: TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned
title: "Audit Submit Semua Verified: Tanpa Dialog, Recovery Damaged/Missing, Klik Ganda, Last Scanned, dan Role Manage TAG (Update)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-32
  - TC-GS-TAG-127
  - TC-GS-TAG-170
  - TC-GS-TAG-171
  - TC-GS-TAG-329
coverage:
  web: automated
---

# Audit Submit Semua Verified: Tanpa Dialog, Recovery Damaged/Missing, Klik Ganda, Last Scanned, dan Role Manage TAG (Update)

## Prerequisites

- Mode: FE+BE (backend nyata; reader tersimulasi).
- Akun aktor (ganti akun eksplisit pada blok terakhir; bagian sesudah ganti akun tetap bermakna):
  - Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`, `Spectra.env.GS_TC_AUDIT_PASSWORD`. Login di hook `before` (TC-GS-TAG-127, 170, 171, 329).
  - Manage TAG (Update) Client A Agus Wijaya `manageTagUpdate_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TAG_UPDATE_PASSWORD` (TC-GS-TAG-32). Kedua nama env belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12):
  - Seed Client Audit: AU1 (DD-31) `E2801160600002054D8A5001` RFID Object Available (combined dengan AUN); AU2 (DD-32) `E2801160600002054D8A5002` Damaged/Missing; AU3 (DD-33) `E2801160600002054D8A5003` Retired; AU4 (DD-34) `E2801160600002054D8A5004` Available; AU5 (DD-35) `E2801160600002054D8A5005` Reserved; AU6 (DD-36) `E2801160600002054D8A5006` Paired; AU7 (DD-37) `E2801160600002054D8A5007` To be Returned; AUN (DD-38) NFC `04A224B2C15E95` Available (combined dengan AU1).
  - Client A (TC-GS-TAG-32): Seed Registri A; satu-satunya tag NFC eligible Audit adalah `04A224B2C15E83` (DD-13, Available, combined dengan DD-11). Submit mengubah Last Scanned DD-13; dipulihkan lewat fixture BE (langkah 62 dan hook `after`).
- Kolom `Last Scanned` dan `Last Scanned In` ditampilkan di registri (precondition TC-GS-TAG-170 dan 171; cara menampilkannya disediakan tim FE). Format tanggal `dd/MM/yy`, 24-hour, Asia/Jakarta.
- Kemampuan teknis (disediakan tim FE, kelas d harness hardware, D-4, Q-1, Q-6): simulasi Handheld Reader `Zebra RFD40 (SN-2201)`; `Pindai X` pada popup Audit berarti memulai sesi pemindaian pada popup (kontrol pemicu disediakan tim FE), X dipindai, lalu klik [Stop] pada Floating Status Widget; jam server dan jam browser diatur bersama (waktu pindai dicatat sesudah pemindaian dengan toleransi satu menit; jam dimajukan 5 menit agar selisih dengan waktu Submit melebihi toleransi dan dipulihkan sesudah Submit, sebelum asersi, S-09); baca jumlah entri Event Log Tab Audit TAG dan TAG Log NFC (baseline); seed/reset Seed Client Audit dan Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan jam server dan jam browser, reset Seed Client Audit dan Seed Registri A, kembalikan sesi ke akun default suite.
- Suite serial (`parallel: false`). Spec mengubah jam server dan jam browser serta data Seed Client Audit dan DD-13 (dipulihkan seperti di atas). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-127: Submit semua Verified, tanpa dialog, recovery Damaged/Missing

1. Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
2. Pindai AU1, AU2, AU3, dan AU4
3. Catat waktu pindai `T127` (waktu browser sesudah pemindaian terakhir)
4. Klik [Submit]
5. Verifikasi tidak ada dialog konfirmasi
6. Verifikasi toast sukses: "Success, audit has been submitted."
7. Klik Tab All, ketik Search `E2801160600002054D8A500`, tekan Enter
8. Verifikasi AU2 berstatus `Available`
9. Verifikasi AU1 dan AU4 tetap `Available`
10. Verifikasi AU3 tetap `Retired`
11. Verifikasi Last Scanned AU1, AU2, AU3, AU4 diperbarui sesuai `T127` (toleransi satu menit)
12. Pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-170: Submit Audit memperbarui Last Scanned hanya untuk baris Verified

13. Klik Tab Not Paired, ketik Search `E2801160600002054D8A5001`, tekan Enter, lalu catat Last Scanned dan Last Scanned In AU1 sebagai baseline `LS1` dan `LI1`
14. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
15. Pindai AU2 dan AU4
16. Catat waktu pindai `T170` (waktu browser sesudah pemindaian terakhir)
17. Majukan jam server dan jam browser bersama sebesar 5 menit
18. Klik [Submit], biarkan checkbox dicentang, lalu klik [Confirm]
19. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
20. Pulihkan jam server dan jam browser ke waktu semula
21. Klik item sidebar `TAG`, klik Tab Not Paired, ketik Search `E2801160600002054D8A500`, tekan Enter
22. Verifikasi Last Scanned AU2 sama dengan `T170` (toleransi satu menit), bukan waktu Submit
23. Verifikasi Last Scanned AU4 sama dengan `T170` (toleransi satu menit), bukan waktu Submit
24. Hover badge Last Scanned In AU2
25. Verifikasi tooltip AU2 "Global Settings > TAG > Audit TAG"
26. Hover badge Last Scanned In AU4
27. Verifikasi tooltip AU4 "Global Settings > TAG > Audit TAG"
28. Verifikasi Last Scanned AU1 tidak berubah dari `LS1`
29. Verifikasi Last Scanned In AU1 tidak berubah dari `LI1`
30. Pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-171: Sibling combined yang ikut Verified secara silent

31. Ketik Search `04A224B2C15E95`, tekan Enter, buka menu baris NFC `04A224B2C15E95` > `TAG Log`, catat jumlah entri sebagai `TLN`, lalu tutup popup TAG Log
32. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
33. Pindai AU1 (combined dengan NFC `04A224B2C15E95`)
34. Catat waktu pindai `T171` (waktu browser sesudah pemindaian)
35. Majukan jam server dan jam browser bersama sebesar 5 menit
36. Klik [Submit], lalu klik [Confirm]
37. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
38. Pulihkan jam server dan jam browser ke waktu semula
39. Klik item sidebar `TAG`, klik Tab Not Paired, ketik Search `04A224B2C15E95`, tekan Enter
40. Verifikasi Last Scanned NFC `04A224B2C15E95` sama dengan `T171` (toleransi satu menit), bukan waktu Submit
41. Hover badge Last Scanned In NFC `04A224B2C15E95`
42. Verifikasi tooltip "Global Settings > TAG > Audit TAG" (path sesi yang sama)
43. Buka menu baris NFC `04A224B2C15E95` > `TAG Log`
44. Verifikasi popup TAG Log NFC tampil
45. Verifikasi jumlah entri TAG Log NFC sama dengan `TLN` (tidak ada entri `Audit` untuk NFC tersebut)
46. Tutup popup TAG Log, lalu pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-329: Klik ganda Submit Audit hanya memproses satu sesi

47. Buka Event Log > Tab Audit TAG, catat jumlah entri sebagai baseline `E329`, lalu tutup Event Log
48. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
49. Pindai AU1, AU2, AU3, dan AU4
50. Klik dua kali cepat [Submit]
51. Verifikasi tepat satu toast sukses: "Success, audit has been submitted."
52. Buka Event Log > Tab Audit TAG
53. Verifikasi jumlah entri Event Log Audit bertambah tepat satu dari baseline `E329`
54. Tutup Event Log, lalu pulihkan Seed Client Audit lewat fixture BE

### TC-GS-TAG-32: Manage TAG (Update) menyelesaikan Audit TAG sampai sukses

55. Ganti akun: logout, lalu login sebagai Manage TAG (Update) Client A dengan `Spectra.env.GS_TAG_UPDATE_PASSWORD`
56. Buka Global Settings > TAG > Tab All
57. Klik `Audit TAG`, lalu pilih `NFC` pada overlay `Select TAG Type`
58. Pindai `04A224B2C15E83`
59. Klik [Submit]
60. Verifikasi toast sukses: "Success, audit has been submitted."
61. Tutup popup bila masih terbuka
62. Pulihkan Seed Registri A lewat fixture BE

## Notes

- Mode: FE+BE. Kelas d (harness hardware tersimulasi; D-4, Q-1). P-1 (S-05, keputusan D-1): klausa absence TC-GS-TAG-171 (tidak ada entri TAG Log `Audit` untuk NFC) berada di spec asal dengan baseline `TLN` dan anchor positif langkah 42. TC-GS-TAG-32 ditempatkan di spec Audit karena butuh scan (rujukan dua arah dengan spec Role Matrix positif, TC-GS-TAG-31 dan 33).
- Spec melewati sekitar 35 langkah (62 langkah). Alasan: seluruh blok satu topik aksi (Submit Audit) dan satu kelas harness (reader tersimulasi), tiap blok berdiri sendiri karena Seed Client Audit dipulihkan antar blok (langkah 12, 30, 46, 54) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok akun Manage TAG (Update) memakai ganti akun eksplisit dan tetap bermakna sendiri (bagian 3, pemisah (b)) dan ditaruh paling akhir karena mengubah Seed Registri A.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 3, 7, 12, 13, 14, 16, 17, 19, 20, 21, 30, 31, 32, 34, 35, 37, 38, 39, 43, 46, 47, 48, 52, 54, 55, 56, 57, 61, 62 (membuka popup dan surface log, Search untuk menemukan baris target, mencatat nilai, menunggu aksi konfirmasi selesai sebelum memulihkan jam, mengatur dan memulihkan jam, pemulihan data, ganti akun).
- Pembagian TC lintas spec: TC-GS-TAG-128 sampai 131 dan 174 (dialog Submit Audit dan hasil status) di spec 043; TC-GS-TAG-132 (sibling silent) di spec 041; TC-GS-TAG-31 dan 33 di spec Role Matrix positif (slice 1).
- Temuan untuk QA:
  - Q-6: "Tunggu minimal 1 menit" (TC-GS-TAG-170 dan 171) tidak menentukan menunggu nyata atau mengatur jam; spec mengatur jam server dan jam browser bersama (5 menit). VAL "1 menit" diturunkan dari Tabel Data Uji (Q-13).
  - TC-GS-TAG-32: precondition menyebut Client A dan akun Manage TAG (Update) Client A, sedangkan TC Audit lain memakai Client Audit; spec memakai ganti akun eksplisit ke akun Client A.
  - TC-GS-TAG-127 Expected c ("Last Scanned AU1 s.d. AU4 diperbarui") tidak menyebut nilai; spec membandingkan dengan waktu pindai yang dicatat (`T127`). Post Condition c (Event Log Audit satu sesi baru dan TAG Log setiap tag memuat entri Audit) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-GS-TAG-170 dan 171 langkah konfirmasi: dialog `Submit Audit` muncul karena ada baris Not Scanned; TC hanya menyebut `Confirm` sehingga langkah 18 dan 36 mengikuti urutan TC tanpa asersi dialog.
  - TC-GS-TAG-329: "satu baris Event Log Audit baru" tidak menyebut tab Event Log; spec memakai Event Log > Tab Audit TAG (nama tab diturunkan dari TC-GS-TAG-109 untuk Activate).
