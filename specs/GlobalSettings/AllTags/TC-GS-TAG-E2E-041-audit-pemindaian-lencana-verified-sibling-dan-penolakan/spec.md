---
id: TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan
title: "Audit: Pemindaian Mengubah Lencana ke Verified, Sibling Combined Silent, Kode Belum Aktif T-01, Di Luar Daftar, dan Page-Lock"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-123
  - TC-GS-TAG-124
  - TC-GS-TAG-125
  - TC-GS-TAG-126
  - TC-GS-TAG-132
  - TC-GS-TAG-180
coverage:
  web: automated
---

# Audit: Pemindaian Mengubah Lencana ke Verified, Sibling Combined Silent, Kode Belum Aktif T-01, Di Luar Daftar, dan Page-Lock

## Prerequisites

- Mode: FE+BE (backend nyata; reader tersimulasi).
- Akun aktor: Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`, `Spectra.env.GS_TC_AUDIT_PASSWORD`. Login di hook `before`. Tidak ada ganti akun. Nama env belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori).
- Data Pre-setup (Seed Client Audit, dipulihkan lewat fixture BE sebelum spec, S-12):

  | Alias | Code | TAG Type | Status |
  |---|---|---|---|
  | AU1 (DD-31) | `E2801160600002054D8A5001` | RFID Object | Available (combined dengan AUN) |
  | AU2 (DD-32) | `E2801160600002054D8A5002` | RFID Object | Damaged/Missing |
  | AU3 (DD-33) | `E2801160600002054D8A5003` | RFID Object | Retired |
  | AU4 (DD-34) | `E2801160600002054D8A5004` | RFID Object | Available |
  | AU5 (DD-35) | `E2801160600002054D8A5005` | RFID Object | Reserved |
  | AU6 (DD-36) | `E2801160600002054D8A5006` | RFID Object | Paired |
  | AU7 (DD-37) | `E2801160600002054D8A5007` | RFID Object | To be Returned |
  | AUN (DD-38) | `04A224B2C15E95` | NFC | Available (combined dengan AU1) |

- Data uji: `E2801160600002054D8A3003` (DD-N9; RFID belum diaktivasi), `E2801160600002054D8A` (DD-N10; EPC 20 karakter, format salah).
- Kemampuan teknis (disediakan tim FE, kelas d harness hardware, D-4, Q-1): simulasi Handheld Reader `Zebra RFD40 (SN-2201)` (tersambung, pemindaian kode); `Pindai X` pada popup Audit berarti memulai sesi pemindaian pada popup (kontrol pemicu disediakan tim FE), X dipindai, lalu klik [Stop] pada Floating Status Widget, kecuali langkah menyebut sesi tetap aktif; baca jumlah entri TAG Log NFC dan Event Log Tab Audit TAG (baseline); seed/reset Seed Client Audit.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): reset Seed Client Audit, buang hasil scan popup Audit yang tersisa.
- Suite serial (`parallel: false`). Spec mengubah data Seed Client Audit (dipulihkan seperti di atas); blok yang menyubmit (TC-GS-TAG-132) paling akhir. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### Sesi Audit RFID bersama (TC-GS-TAG-124, 125, 123, 126, 180)

1. Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`

### TC-GS-TAG-124: Pemindaian kode yang belum teraktivasi (Toast T-01)

2. Pindai `E2801160600002054D8A3003` (belum pernah diaktivasi)
3. Verifikasi toast error: "Error, this TAG hasn't been activated yet. Please contact Admin."
4. Verifikasi keempat baris AU1, AU2, AU3, AU4 tetap `Not Scanned` (tidak ada baris yang berubah)

### TC-GS-TAG-125: Pemindaian di luar daftar atau berformat salah

5. Pindai `E2801160600002054D8A5006` (AU6 Paired, tidak ada di daftar)
6. Pindai `E2801160600002054D8A` (format salah)
7. Verifikasi tidak ada baris yang berubah (AU1, AU2, AU3, AU4 tetap `Not Scanned`)
8. Verifikasi daftar tetap sama (hanya AU1, AU2, AU3, AU4)

### TC-GS-TAG-123: Pemindaian mengubah lencana di tempat

9. Pindai `E2801160600002054D8A5004` (AU4)
10. Verifikasi baris AU4 berlencana `✓ Verified` pada posisi semula (urutan baris tidak berubah)
11. Verifikasi baris AU1, AU2, AU3 tetap `Not Scanned`
12. Verifikasi kolom `Status` AU4 masih `Available`
13. Verifikasi tabel tidak bertambah baris
14. Verifikasi tidak ada penghitung (counter) pada popup

### TC-GS-TAG-126: Pemindaian ulang baris Verified (melanjutkan sesi TC-GS-TAG-123)

15. Pindai `E2801160600002054D8A5004` (AU4) sekali lagi (pemindaian kedua)
16. Verifikasi baris AU4 tetap `✓ Verified`
17. Verifikasi tidak ada kontrol undo pada baris AU4

### TC-GS-TAG-180: Page-lock dan Floating Status Widget pada sesi scan Audit

18. Mulai sesi pemindaian pada popup Audit (sesi aktif)
19. Coba klik [Submit] dan `[✕]` pada popup
20. Verifikasi popup blur dan non-interaktif selama sesi
21. Verifikasi Floating Status Widget dengan counter dan [Stop] tampil
22. Pindai `E2801160600002054D8A5001` (AU1, sesi tetap aktif)
23. Klik [Stop] pada widget
24. Verifikasi popup interaktif kembali
25. Verifikasi baris AU1 berlencana `✓ Verified` (lencana hasil pindai)
26. Klik `[✕]`, lalu klik [Discard] pada dialog (membuang hasil scan)

### TC-GS-TAG-132: Sibling combined ikut Verified secara silent

27. Ketik Search `04A224B2C15E95`, tekan Enter, lalu catat Last Scanned NFC sebagai `LSN`
28. Buka menu baris NFC `04A224B2C15E95` > `TAG Log`, catat jumlah entri sebagai `TLN`, lalu tutup popup TAG Log
29. Buka Event Log > Tab Audit TAG, catat jumlah entri sebagai `EA`, lalu tutup Event Log
30. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
31. Pindai `E2801160600002054D8A5001` (AU1, combined dengan NFC AUN)
32. Pindai AU2, AU3, dan AU4
33. Klik [Submit]
34. Tunggu aksi selesai (popup Audit tertutup)
35. Buka Event Log > Tab Audit TAG dan buka Audit Detail sesi baru (jumlah entri bertambah satu dari `EA`)
36. Verifikasi Audit Detail memuat baris AU1, AU2, AU3, AU4
37. Verifikasi Audit Detail tidak memuat baris NFC `04A224B2C15E95`
38. Verifikasi nilai `Found` sesi tersebut tidak menghitung sibling NFC (Found = 4)
39. Tutup Audit Detail dan Event Log, lalu klik Tab Not Paired, ganti isi kotak Search dengan `04A224B2C15E95`, tekan Enter
40. Verifikasi Status NFC `04A224B2C15E95` tetap `Available`
41. Verifikasi Last Scanned NFC `04A224B2C15E95` diperbarui (berbeda dari `LSN`)
42. Buka menu baris NFC `04A224B2C15E95` > `TAG Log`
43. Verifikasi popup TAG Log NFC tampil
44. Verifikasi jumlah entri TAG Log NFC sama dengan `TLN` (tidak ada entri `Audit` untuk sibling)

## Notes

- Mode: FE+BE. Kelas d (harness hardware tersimulasi; D-4 dan Q-1). P-1 (S-05, keputusan D-1): klausa absence TC-GS-TAG-132 (tidak ada entri `Audit` untuk sibling di Audit Detail dan TAG Log) berada di spec asal dengan baseline `TLN` (S-12) dan anchor positif langkah 36 dan 43.
- Spec melewati sekitar 35 langkah (44 langkah). Alasan: seluruh blok satu kelas harness (pemindaian Audit, reader tersimulasi) atas satu dataset Seed Client Audit; TC-GS-TAG-124, 125, 123, 126, dan 180 berbagi satu popup (precondition identik dan tidak ada yang meng-commit) sehingga tidak perlu buka ulang; blok yang meng-commit (TC-GS-TAG-132) paling akhir dan memakai popup baru. Kegagalan satu blok tidak membuat blok lain kehilangan makna kecuali kegagalan reader tersimulasi yang sama untuk semua blok.
- Urutan dan penggabungan: TC-GS-TAG-126 melanjutkan TC-GS-TAG-123 (pemindaian pertama AU4 di langkah 9 dan kedua di langkah 15, jumlah pindai sama dengan Langkah Uji TC-GS-TAG-126); TC-GS-TAG-124 dan 125 dijalankan sebelum TC-GS-TAG-123 agar keduanya diasersi saat belum ada baris Verified.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 26, 27, 28, 29, 30, 34, 35, 39, 42 (membuka popup dan surface log, Search untuk menemukan baris target, mencatat nilai, membuang hasil scan; langkah 34 adalah Tunggu aksi selesai sesudah `[Submit]` sebelum pindah ke Event Log, 8b butir 8); langkah 19 adalah aksi uji TC-GS-TAG-180.
- Pembagian TC lintas spec: TC-GS-TAG-119 sampai 122 (screening popup) berada di spec 040; TC-GS-TAG-127 (Submit semua Verified) di spec 042; TC-GS-TAG-171 (Last Scanned sibling) di spec 042; TC-GS-TAG-133 sampai 136 di spec 044.
- Temuan untuk QA:
  - Q-1: simulasi reader tidak didefinisikan di TC, PRD, LLD; kontrol pemicu sesi pemindaian pada popup Audit tidak diberi label di TC (TC-GS-TAG-180 langkah 3 "Mulai sesi pemindaian"); disediakan tim FE.
  - TC-GS-TAG-180: Langkah Uji tidak memindai tag, sedangkan Expected b menyebut "lencana hasil pindai"; spec menambah pemindaian AU1 di langkah 22 (S-03).
  - TC-GS-TAG-132 Expected b menyebut `Found` tanpa nilai konkret; spec menafsirkan `Found` = 4 (empat RFID dipindai) pada langkah 38. Jalur menuju Audit Detail ("Buka Audit Detail sesi tersebut") tidak ditulis di TC; spec memakai Event Log > Tab Audit TAG.
  - TC-GS-TAG-125 Expected tidak menyebut toast untuk kode di luar daftar dan format salah; spec tidak mengasersi toast.
  - TC-GS-TAG-132 Expected a membaca "Last Scanned-nya diperbarui" tanpa nilai; spec membandingkan dengan nilai yang dicatat sebelum sesi (`LSN`).
  - Post Condition semua TC bernilai `-`.
