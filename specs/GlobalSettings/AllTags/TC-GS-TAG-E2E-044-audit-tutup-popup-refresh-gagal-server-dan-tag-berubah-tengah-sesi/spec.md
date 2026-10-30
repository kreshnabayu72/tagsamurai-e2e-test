---
id: TC-GS-TAG-E2E-044-audit-tutup-popup-refresh-gagal-server-dan-tag-berubah-tengah-sesi
title: "Audit: Dialog Keep Auditing/Discard, Refresh, Submit Gagal Server T-03, dan Tag Dihapus atau Tidak Eligible di Tengah Sesi T-13"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-133
  - TC-GS-TAG-134
  - TC-GS-TAG-135
  - TC-GS-TAG-136
coverage:
  web: automated
---

# Audit: Dialog Keep Auditing/Discard, Refresh, Submit Gagal Server T-03, dan Tag Dihapus atau Tidak Eligible di Tengah Sesi T-13

## Prerequisites

- Mode: FE+BE (backend nyata dengan intercept parsial pada request submit Audit).
- Akun aktor: Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`, `Spectra.env.GS_TC_AUDIT_PASSWORD`. Login di hook `before`. Tidak ada ganti akun. Nama env belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori).
- Pelaku kedua (TC-GS-TAG-133, sesi API, hanya memicu perubahan state): admin kedua Client Audit yang menghapus AU2. Akun tidak ada di Pre-setup TC (hanya admin kedua Client A); disediakan tim FE (S-13).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup (Seed Client Audit, dipulihkan lewat fixture BE sebelum spec dan sesudah blok TC-GS-TAG-133, S-12): AU1 (DD-31) `E2801160600002054D8A5001` RFID Object Available (combined dengan AUN); AU2 (DD-32) `E2801160600002054D8A5002` Damaged/Missing; AU3 (DD-33) `E2801160600002054D8A5003` Retired; AU4 (DD-34) `E2801160600002054D8A5004` Available; AU5 (DD-35) `E2801160600002054D8A5005` Reserved; AU6 (DD-36) `E2801160600002054D8A5006` Paired; AU7 (DD-37) `E2801160600002054D8A5007` To be Returned; AUN (DD-38) NFC `04A224B2C15E95` Available (combined dengan AU1).
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): admin kedua Client Audit menghapus AU2 pada TC-GS-TAG-133 (langkah 34).
- Kemampuan teknis (disediakan tim FE, kelas d harness hardware, D-4, Q-1): simulasi Handheld Reader `Zebra RFD40 (SN-2201)`; `Pindai X` pada popup Audit berarti memulai sesi pemindaian pada popup (kontrol pemicu disediakan tim FE), X dipindai, lalu klik [Stop] pada Floating Status Widget; penanganan dialog `beforeunload` (mendeteksi, membatalkan; S-08); intercept jaringan di atas backend nyata untuk request submit Audit (respons 5xx; endpoint dari `openapi.yaml` dilengkapi tahap script, S-13) dan dilepas segera setelah pemicu selesai (S-09); sesi API admin kedua; baca jumlah entri Event Log Tab Audit TAG dan Activity Log (N sebelum aksi: Action `Update TAG Condition` per kode dan Action `Audit TAG`; asersi memakai selisih terhadap N).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): lepas intercept yang tersisa, reset Seed Client Audit, buang hasil scan popup Audit yang tersisa.
- Suite serial (`parallel: false`). Spec mengubah data Seed Client Audit (dipulihkan seperti di atas). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-136: Refresh saat ada baris Verified belum di-Submit (bagian tanpa baris Verified)

1. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
2. Muat ulang halaman (F5) tanpa baris Verified
3. Verifikasi halaman termuat ulang (sidebar Global Settings tampil)
4. Verifikasi konfirmasi bawaan browser (`beforeunload`) tidak muncul

### TC-GS-TAG-135: Menutup popup Audit, Dialog 7 hanya bila ada baris Verified

5. Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
6. Klik `[✕]`
7. Verifikasi popup tertutup langsung tanpa dialog (toolbar registri tampil)
8. Klik `Audit TAG` lagi, lalu pilih `RFID` pada overlay `Select TAG Type`
9. Pindai `E2801160600002054D8A5004` (AU4)
10. Tekan `Esc`
11. Verifikasi dialog dengan pesan "Are you sure you want to cancel this audit session? Unsaved scan records will be lost."
12. Verifikasi tombol [Keep Auditing] dan [Discard] pada dialog
13. Klik [Keep Auditing]
14. Verifikasi progres dipertahankan (AU4 berlencana `✓ Verified`)

### TC-GS-TAG-136: Refresh saat ada baris Verified belum di-Submit (bagian dengan baris Verified)

15. Muat ulang halaman (F5) dengan AU4 `✓ Verified`
16. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
17. Batalkan konfirmasi bawaan browser (tetap di halaman)

### TC-GS-TAG-135 (lanjutan): Discard membuang hasil scan

18. Tekan `Esc`, lalu klik [Discard] pada dialog
19. Verifikasi popup tertutup
20. Klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
21. Verifikasi AU4 berlencana `Not Scanned` (hasil scan dibuang)

### TC-GS-TAG-134: Submit Audit gagal server T-03

22. Aktifkan intercept: request submit Audit dijawab 5xx
23. Pindai AU1, AU2, AU3, dan AU4
24. Klik [Submit]
25. Verifikasi toast error: "Error, failed to submit audit."
26. Verifikasi popup Audit tetap terbuka
27. Verifikasi seluruh lencana `✓ Verified` (AU1, AU2, AU3, AU4) dipertahankan
28. Lepas intercept
29. Klik `[✕]`, lalu klik [Discard] pada dialog (membuang hasil scan)

### TC-GS-TAG-133: Tag dihapus atau tidak eligible di tengah sesi T-13

30. Buka Event Log > Tab Audit TAG, catat jumlah entri sebagai baseline `E133`, lalu tutup Event Log
31. Buka Activity Log, catat jumlah entri Action `Update TAG Condition` untuk AU2 sebagai `UA2` dan jumlah entri Action `Audit TAG` sebagai `UAT`
32. Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
33. Pindai AU4
34. Dari sesi kedua (admin kedua Client Audit, sesi API), hapus tag AU2 (Damaged/Missing, tidak combined) hingga tersimpan
35. Klik [Submit]
36. Biarkan checkbox dicentang dan klik [Confirm]
37. Verifikasi toast sukses: "Success, audit has been submitted. Some TAGs were skipped because they are no longer available for audit."
38. Buka Event Log > Tab Audit TAG dan buka Audit Detail sesi baru (jumlah entri bertambah satu dari `E133`)
39. Verifikasi Audit Detail memuat baris AU4, AU1, dan AU3 (baris lain tetap commit)
40. Verifikasi Audit Detail tidak memuat baris AU2
41. Verifikasi `Found` sesi tersebut bernilai `1` (AU2 tidak dihitung)
42. Verifikasi `Not Found` sesi tersebut bernilai `2` (AU1 dan AU3; AU3 Retired tetap dihitung)
43. Tutup Audit Detail dan Event Log, lalu buka Activity Log
44. Verifikasi jumlah entri `Audit TAG` bertambah dari `UAT`
45. Verifikasi jumlah entri `Update TAG Condition` untuk AU2 sama dengan `UA2` (AU2 tidak dicatat di Activity Log sesi ini)
46. Pulihkan Seed Client Audit lewat fixture BE

## Notes

- Mode: FE+BE. P-1 (S-05, keputusan D-1): klausa absence TC-GS-TAG-133 (AU2 tidak dicatat di Activity Log, langkah 45) berada di spec asal dengan baseline `UA2` dan anchor positif langkah 44. Kelas d (harness hardware tersimulasi; D-4, Q-1) dengan intercept ringan (kelas b) pada TC-GS-TAG-134 (P-5(b): satu TC objek-uji ringan kelas b, tanpa harness eksternal dan tanpa state berat sendiri, pada spec dengan harness dominan yang sama).
- Spec melewati sekitar 35 langkah (46 langkah). Alasan: seluruh blok satu kelas harness (pemindaian Audit, reader tersimulasi) atas satu dataset Seed Client Audit; blok non-commit (136, 135, 134) berbagi satu popup dan satu pembukaan karena precondition identik; blok yang menghapus data (TC-GS-TAG-133) paling akhir dengan pemulihan di langkah 46. Kegagalan satu blok tidak membuat blok lain kehilangan makna kecuali kegagalan reader tersimulasi.
- Urutan dan penggabungan: bagian TC-GS-TAG-136 tanpa baris Verified (langkah 2 sampai 4) dan bagian TC-GS-TAG-135 tanpa Verified (langkah 6 sampai 7) dijalankan lebih dulu; bagian dengan baris Verified TC-GS-TAG-136 (langkah 15 sampai 17) memakai popup berisi AU4 Verified dari TC-GS-TAG-135 (pemindaian AU4 yang sama dengan Langkah Uji TC-GS-TAG-136). Perubahan urutan dari urutan TC dicatat di sini.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 5, 8, 17, 18, 20, 22, 28, 29, 30, 31, 32, 38, 43, 46 (membuka popup dan surface log, membatalkan konfirmasi bawaan, pasang dan lepas intercept, mencatat baseline, pemulihan).
- Langkah tambahan demi Expected (S-03): langkah 2 sampai 4 (Expected TC-GS-TAG-136 "tanpa baris Verified tidak ada konfirmasi"), langkah 18 sampai 21 (Expected TC-GS-TAG-135 butir b "Discard menutup popup dan membuang hasil scan").
- Pembagian TC lintas spec: TC-GS-TAG-123 sampai 126 dan 180 (pemindaian dan page-lock) di spec 041; TC-GS-TAG-182 (refresh saat sesi scan aktif Activate) di spec 038; TC-GS-TAG-328 (dua admin submit audit) di spec 045.
- Temuan untuk QA:
  - TC-GS-TAG-133 Expected b/c tidak menyebut nilai `Found` dan `Not Found`; spec menurunkannya (Found 1 = AU4; Not Found 2 = AU1 dan AU3, AU2 dilewati) pada langkah 41 dan 42 (nilai turunan, bukan dari PRD). Marka 🔖 pada "Toast sukses 🔖" tidak dijelaskan di TC; spec hanya mengasersi teksnya. Akun admin kedua Client Audit tidak ada di Pre-setup.
  - TC-GS-TAG-133: absence AU2 di Activity Log tidak punya definisi entri; spec membatasi pada Action `Update TAG Condition` untuk AU2 dengan baseline `UA2`, dan memakai pertambahan jumlah entri `Audit TAG` dari baseline `UAT` sebagai anchor positif.
  - TC-GS-TAG-134: "request submit dibuat gagal 5xx" tidak menyebut endpoint; disediakan tim FE dari `openapi.yaml`.
  - TC-GS-TAG-135 Expected a menyebut `[✕]` sedangkan Langkah Uji 6 memakai `Esc` pada kondisi Verified; spec mengikuti Langkah Uji dan Expected, menjalankan `[✕]` tanpa Verified dan `Esc` dengan Verified.
  - Post Condition semua TC bernilai `-`.
