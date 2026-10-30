---
id: TC-GS-IMPORT-E2E-070-aksi-admin-kedua-pada-draft-ber-error-ditolak-409-delete-all-rows-ai
title: "Aksi Admin Kedua pada Draft Ber-error Ditolak 409: Delete All Rows, AI Accept, dan AI Dismiss"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-242
  - TC-GS-IMPORT-243
  - TC-GS-IMPORT-244
coverage:
  web: automated
---

# Aksi Admin Kedua pada Draft Ber-error Ditolak 409: Delete All Rows, AI Accept, dan AI Dismiss

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client A:
  - Sesi TC: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41) dengan badge saran AI `AI suggestion: 'Samsung Electronics Indonesia'?`; D-40/D-41/D-42 mock AI mode normal (D-11), dikembalikan ke normal sesudah spec.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: sesi edit Sesi TC ditutup dengan `[Cancel]` di akhir tiap blok; draft D-09 dipulihkan antar TC.

## Test Steps

### TC-GS-IMPORT-242: Delete All Rows oleh Admin kedua

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi Admin kedua] Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
4. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
5. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
6. [Sesi Admin kedua] Muat ulang halaman Import > Brand
7. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 13
8. [Sesi Admin kedua] Verifikasi Staging Metric Cards Errors tetap 1
9. [Sesi TC] Verifikasi baris #1 tetap input aktif
10. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
11. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-243: AI Accept oleh Admin kedua

12. [Sesi TC] Klik `⋯` pada baris #1
13. [Sesi TC] Pilih Edit
14. [Sesi Admin kedua] Klik tombol halaman 2 pada paginator
15. [Sesi Admin kedua] Klik `[Accept]` pada badge saran AI di sel Brand Name baris #13
16. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
17. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
18. [Sesi Admin kedua] Muat ulang halaman Import > Brand
19. [Sesi Admin kedua] Klik tombol halaman 2 pada paginator
20. [Sesi Admin kedua] Verifikasi baris #13 tetap berstatus `error` dengan Brand Name 121 karakter semula
21. [Sesi TC] Verifikasi baris #1 tetap input aktif
22. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
23. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-244: AI Dismiss oleh Admin kedua

24. [Sesi TC] Klik `⋯` pada baris #1
25. [Sesi TC] Pilih Edit
26. [Sesi Admin kedua] Klik tombol halaman 2 pada paginator
27. [Sesi Admin kedua] Klik `[Dismiss]` pada badge saran AI di sel Brand Name baris #13
28. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
29. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
30. [Sesi Admin kedua] Muat ulang halaman Import > Brand
31. [Sesi Admin kedua] Klik tombol halaman 2 pada paginator
32. [Sesi Admin kedua] Verifikasi badge `AI suggestion: 'Samsung Electronics Indonesia'?` pada sel Brand Name baris #13 tetap tampil
33. [Sesi TC] Verifikasi baris #1 tetap input aktif
34. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
35. [Sesi TC] Klik `[Cancel]` pada footer

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); kedua sesi UI menjadi objek asersi.
- Spec memuat 35 langkah dan mengikuti pola yang sama dengan spec 069.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11, 23, 35 (menutup sesi edit Sesi TC), langkah 6, 14, 18, 19, 26, 30, 31 (muat ulang dan paginasi Sesi Admin kedua).
- Pembagian TC lintas spec: aksi tulis lain Admin kedua saat kunci dipegang ada di spec 069 dan 071.
- Temuan untuk QA:
  - TC-GS-IMPORT-242 Expected b menyebut "Total Rows tetap 13 dan Errors tetap 1" tanpa nomor langkah; spec memetakan ke setelah muat ulang.
  - TC-GS-IMPORT-243 dan 244 tidak menyebut cara menutup sesi edit Total Control; spec menambahkan `[Cancel]` sebagai langkah penghubung.
