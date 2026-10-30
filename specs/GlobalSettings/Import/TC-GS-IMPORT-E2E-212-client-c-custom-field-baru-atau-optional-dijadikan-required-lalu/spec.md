---
id: TC-GS-IMPORT-E2E-212-client-c-custom-field-baru-atau-optional-dijadikan-required-lalu
title: "Client C: Custom Field baru atau Optional dijadikan Required, lalu dikembalikan Optional"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-936
  - TC-GS-IMPORT-937
  - TC-GS-IMPORT-938
coverage:
  web: automated
---

# Client C: Custom Field baru atau Optional dijadikan Required, lalu dikembalikan Optional

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client C (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, password `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net`, password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (nama env baru). Sesi API membuat Custom Field dan mengubah flag Required di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Pre-setup: Client C tanpa draft (Kontrak Fixture R1; reset oleh hook `beforeEach` suite dan langkah pemulihan). Custom Field Active `Tax ID` (Text, Optional) ada di Client C. Custom Field `Cost Center` belum ada di Client C. Nama `Cost Center` dan `Tax ID` literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks error `Cost center must not be empty` dan `Tax ID must not be empty`).
- Data Dinamis: D-20 (draft User Login Client C 8 baris `pending` dari `user-login-8.csv`, salinan D-05; dipakai TC-GS-IMPORT-936), disiapkan lewat skrip seed sebelum TC itu. Berkas uji (upload UI, draft tidak di-commit): `user-login-taxid-mixed.csv` (berkas User Login standar D-45 3 baris data pertama ditambah kolom `Tax ID`: `TX-001` baris 1, kosong baris 2 dan 3) dan `user-login-taxid-empty-2.csv` (berkas User Login standar D-45 2 baris data pertama ditambah kolom `Tax ID` kosong pada kedua baris). Email berkas D-45 diberi suffix per run `+{runId}-212` sebelum `@` (TC menulis tanpa suffix).
- Urutan TC: 937, 938, 936 (TC-936 membuat Custom Field baru di akhir). Pemulihan dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R1 dan R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): `Tax ID` dikembalikan ke Optional; Custom Field `Cost Center` dihapus; draft User Login Client C dibuang.
- Kemampuan teknis: pemilihan berkas; skrip seed D-20; skrip reset draft Client C; sesi API Admin kedua.
- State global: Custom Field Client C (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Optional dijadikan Required (TC-GS-IMPORT-937)

1. Total Control Client C: unggah `user-login-taxid-mixed.csv` dan klik `[Confirm Mapping]` (kolom `Tax ID` terpetakan)
2. Verifikasi ketiga baris berstatus `pending`
3. Admin kedua Client C (sesi API) menjadikan Custom Field `Tax ID` Required hingga tersimpan
4. Total Control Client C: tekan `F5` pada halaman Import > User Login
5. Verifikasi baris 1 tetap `pending`
6. Verifikasi baris 2 dan 3 berstatus `error` dengan sel `Tax ID` berborder `danger`
7. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 1, Errors 2
8. Verifikasi footer menampilkan `[Import (1)]`
9. Verifikasi Error Summary Callout memuat `Tax ID must not be empty` dengan badge "2 rows"
10. Pulihkan: Admin kedua mengembalikan `Tax ID` ke Optional, buang draft User Login Client C lewat skrip reset, muat ulang halaman

### Required dikembalikan Optional (TC-GS-IMPORT-938)

11. Total Control Client C: unggah `user-login-taxid-empty-2.csv` dan klik `[Confirm Mapping]` (kolom `Tax ID` terpetakan, sel kosong)
12. Admin kedua Client C (sesi API) menjadikan Custom Field `Tax ID` Required hingga tersimpan
13. Total Control Client C: tekan `F5` pada halaman Import
14. Verifikasi kedua baris berstatus `error`
15. Verifikasi Staging Metric Cards: Ready to Import 0, Errors 2
16. Admin kedua Client C (sesi API) menjadikan Custom Field `Tax ID` kembali Optional hingga tersimpan
17. Total Control Client C: tekan `F5` pada halaman Import > User Login
18. Verifikasi kedua baris berstatus `pending` tanpa border `danger`
19. Verifikasi Staging Metric Cards: Total Rows 2, Ready to Import 2, Errors 0
20. Verifikasi Error Summary Callout tidak tampil
21. Pulihkan: buang draft User Login Client C lewat skrip reset

### Custom Field baru Required (TC-GS-IMPORT-936)

22. Seed draft D-20 lewat skrip seed, lalu muat ulang halaman Import > User Login
23. Admin kedua Client C (sesi API) membuat Custom Field `Cost Center` (Data Type Text, Required, Active) di Custom Field User hingga tersimpan
24. Total Control Client C: tekan `F5` pada halaman Import > User Login
25. Verifikasi kolom `Cost Center` tampil
26. Verifikasi seluruh 8 baris berstatus `error` dengan sel `Cost Center` kosong berborder `danger`
27. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 0, Errors 8
28. Verifikasi Error Summary Callout memuat `Cost center must not be empty` dengan badge "8 rows"
29. Pulihkan: Admin kedua menghapus Custom Field `Cost Center`, buang draft User Login Client C lewat skrip reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 29 langkah, di atas 35 langkah.
- P-2: Admin kedua hanya memicu perubahan Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 10, 21, dan 29 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan. Langkah 22 menyiapkan draft D-20 (penghubung, S-03).
- Urutan 937, 938, 936 mengubah urutan nomor TC; alasannya: TC-GS-IMPORT-936 membuat Custom Field baru dan memakai draft seed berbeda (D-20), sehingga diletakkan paling akhir (S-05).
- Temuan untuk QA:
  - TC-GS-IMPORT-937 dan 938 Data Uji menulis berkas dari D-45 (Email tanpa suffix per run); spec memakai suffix per run.
  - TC-GS-IMPORT-936 Post Condition ("Custom Field `Cost Center` dihapus dari Client C dan draft Client C dipulihkan") tidak punya langkah observasi di TC; ditulis sebagai langkah pemulihan, tanpa asersi.
  - Pemakaian "lewat fixture permintaan" untuk Admin kedua (TC-GS-IMPORT-937, 938) tidak merinci mekanismenya; spec memakai sesi API Admin kedua (kemampuan disediakan tim FE/BE).
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
