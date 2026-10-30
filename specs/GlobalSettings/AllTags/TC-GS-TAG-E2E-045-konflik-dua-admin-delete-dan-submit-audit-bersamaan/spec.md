---
id: TC-GS-TAG-E2E-045-konflik-dua-admin-delete-dan-submit-audit-bersamaan
title: "Konflik Dua Admin: Delete Tag yang Sama dan Submit Audit Tipe yang Sama Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-327
  - TC-GS-TAG-328
coverage:
  web: automated
---

# Konflik Dua Admin: Delete Tag yang Sama dan Submit Audit Tipe yang Sama Bersamaan

## Prerequisites

- Mode: FE+BE (kelas multi-konteks c: dua sesi UI paralel dalam konteks browser terpisah; hasil di kedua sesi diasersi sehingga keduanya sesi UI, bukan sesi API).
- Akun aktor (login di hook `before` pada konteks browser terpisah; ganti akun eksplisit untuk TC-GS-TAG-328):
  - Admin A, TC-GS-TAG-327: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Admin B, TC-GS-TAG-327: Total Control kedua Client A Dewi Lestari `totalControl2_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD` (kesamaan akun dengan `.env.example` perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B)).
  - Admin A, TC-GS-TAG-328: Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`, `Spectra.env.GS_TC_AUDIT_PASSWORD`. Nama env belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori).
  - Admin B, TC-GS-TAG-328: admin kedua Client Audit. Akun tidak ada di Pre-setup TC (hanya admin kedua Client A); disediakan tim FE (S-13).
  - Hook `after` menutup konteks Admin B dan mengembalikan sesi ke akun default suite.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12): TC-GS-TAG-327: Seed Registri A, tag `E2801160600002054D8A0002` (DD-02, RFID, Available, Self-Purchased); dihapus oleh spec dan dipulihkan lewat fixture BE (langkah 17 dan hook `after`). TC-GS-TAG-328: Seed Client Audit AU1 (DD-31) `E2801160600002054D8A5001` Available (combined dengan AUN), AU2 (DD-32) `E2801160600002054D8A5002` Damaged/Missing, AU3 (DD-33) `E2801160600002054D8A5003` Retired, AU4 (DD-34) `E2801160600002054D8A5004` Available, AUN (DD-38) NFC `04A224B2C15E95`.
- Kemampuan teknis (disediakan tim FE, kelas c multi-konteks dan simulasi reader d, D-4, Q-1): dua konteks browser paralel dalam satu spec dengan penanda `[Admin A]` dan `[Admin B]`; simulasi Handheld Reader `Zebra RFD40 (SN-2201)` di kedua konteks (`Pindai X` pada popup Audit berarti memulai sesi pemindaian pada popup, X dipindai, lalu klik [Stop] pada Floating Status Widget); baca jumlah entri Event Log Tab Activate TAG dan Tab Audit TAG (baseline); seed/reset Seed Registri A dan Seed Client Audit.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan Seed Registri A dan Seed Client Audit, tutup konteks Admin B.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-327: Dua admin menghapus tag yang sama bersamaan

1. [Admin A] Buka Global Settings > TAG > Tab All, ketik Search `E2801160600002054D8A0002`, tekan Enter
2. [Admin B] Buka Global Settings > TAG > Tab All, ketik Search `E2801160600002054D8A0002`, tekan Enter
3. [Admin A] Buka Event Log > Tab Activate TAG
4. [Admin A] Catat jumlah entri sebagai baseline `ED`
5. [Admin A] Tutup Event Log
6. [Admin A] Buka menu baris `E2801160600002054D8A0002`, lalu klik `Delete`
7. [Admin A] Verifikasi dialog Delete terbuka
8. [Admin B] Buka menu baris `E2801160600002054D8A0002`, lalu klik `Delete`
9. [Admin B] Verifikasi dialog Delete terbuka
10. [Admin A] Klik [Delete] pada dialog
11. [Admin A] Verifikasi toast sukses: "Success, TAG has been deleted."
12. [Admin B] Klik [Delete] pada dialog
13. [Admin B] Verifikasi toast netral: "This TAG is no longer available."
14. [Admin B] Verifikasi daftar di-refresh dan baris `E2801160600002054D8A0002` tidak lagi tampil
15. [Admin A] Buka Event Log > Tab Activate TAG
16. [Admin A] Verifikasi jumlah entri Event Log Delete bertambah tepat satu dari baseline `ED`
17. Pulihkan Seed Registri A lewat fixture BE

### TC-GS-TAG-328: Dua admin men-submit audit tipe yang sama bersamaan

18. [Admin A] Ganti akun: logout, lalu login sebagai Total Control Client Audit dengan `Spectra.env.GS_TC_AUDIT_PASSWORD`
19. [Admin B] Ganti akun: logout, lalu login sebagai admin kedua Client Audit (akun disediakan tim FE)
20. [Admin A] Buka Event Log > Tab Audit TAG
21. [Admin A] Catat jumlah entri sebagai baseline `EA`
22. [Admin A] Tutup Event Log
23. [Admin A] Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
24. [Admin B] Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
25. [Admin A] Pindai AU1, AU2, AU3, dan AU4
26. [Admin B] Pindai AU1, AU2, AU3, dan AU4 (tag yang sama)
27. [Admin A] Klik [Submit]
28. [Admin A] Buka Event Log > Tab Audit TAG
29. [Admin A] Verifikasi jumlah entri Event Log Audit bertambah tepat satu dari baseline `EA` (satu baris untuk satu Submit)
30. [Admin A] Tutup Event Log
31. [Admin B] Klik [Submit]
32. [Admin A] Buka Event Log > Tab Audit TAG
33. [Admin A] Verifikasi jumlah entri Event Log Audit bertambah tepat dua dari baseline `EA` (setiap sesi memiliki baris Event Log sendiri, tanpa baris ganda)
34. Pulihkan Seed Client Audit lewat fixture BE

## Notes

- Mode: FE+BE. Kelas c (dua admin, dua sesi UI). Spec memakai penanda sesi eksplisit; bagian TC-GS-TAG-328 tetap bermakna walau TC-GS-TAG-327 gagal karena memakai client dan akun sendiri (ganti akun eksplisit di langkah 18 dan 19). TC-GS-TAG-328 juga memakai simulasi reader di dua konteks (kelas d); keduanya ditulis sebagai kemampuan di Prerequisites dan blok TC-GS-TAG-328 diletakkan terakhir agar kegagalan reader tidak menutupi blok TC-GS-TAG-327. Subjudul `###` memetakan langkah ke id TC.
- Aksi menghabisi data (Delete DD-02) dilakukan pada tag Seed Registri A yang dipulihkan (langkah 17).
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 2, 3, 4, 5, 15, 17, 18, 19, 20, 21, 22, 23, 24, 28, 30, 32, 34 (membuka surface, Search untuk menemukan baris target, mencatat baseline, ganti akun, pemulihan).
- Urutan klik mengikuti TC: dialog Delete dibuka di kedua sesi lebih dulu, lalu Admin A mengonfirmasi, lalu Admin B (S-04). Langkah 28 sampai 30 (membuka Event Log di antara dua Submit) adalah langkah tambahan demi klausa "tidak ada baris ganda untuk satu Submit".
- Langkah 7 dan 9 (dialog Delete terbuka) berasal dari keterangan dalam Langkah Uji TC-GS-TAG-327, ditulis sebagai `Verifikasi` terpisah dari aksi klik.
- Pembagian TC lintas spec: TC-GS-TAG-330 (klik ganda Delete) di spec Delete konflik dan kegagalan server (053); TC-GS-TAG-129 dan 133 (hasil Submit Audit) di spec 043 dan 044.
- Temuan untuk QA:
  - Q-2: Pre-setup TC memakai `totalControl2_automated_qaTeam1`, sedangkan `.env.example` mendaftarkan `totalControl2` untuk GS_TC2; kesamaan dengan akun admin kedua perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B). Admin kedua Client Audit (TC-GS-TAG-328) tidak ada di Pre-setup.
  - Q-5: pemicu "bersamaan" (TC-GS-TAG-327 dan 328) tidak deterministik; spec mengurutkan klik sesuai Langkah Uji.
  - Q-8: TC-GS-TAG-328 Expected "commit membaca ulang status terkini" tidak punya nilai konkret; tidak diasersi. Spec mengasersi hanya klausa jumlah baris Event Log per sesi dan tanpa baris ganda.
  - TC-GS-TAG-327 Expected b: surface Event Log "satu baris Event Log Delete" tidak menyebut tab; spec memakai Event Log > Tab Activate TAG (baris `Delete` ada di Tab Activate TAG; TC-GS-TAG-153 dan TC-GS-TAG-247). TC-GS-TAG-327 menargetkan baris Pre-setup DD-02 (S-06); spec memulihkan lewat fixture BE.
  - Post Condition kedua TC bernilai `-`.
