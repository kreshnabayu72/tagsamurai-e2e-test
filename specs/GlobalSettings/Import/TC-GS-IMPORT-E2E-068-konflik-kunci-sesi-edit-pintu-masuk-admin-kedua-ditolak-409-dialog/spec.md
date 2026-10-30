---
id: TC-GS-IMPORT-E2E-068-konflik-kunci-sesi-edit-pintu-masuk-admin-kedua-ditolak-409-dialog
title: "Konflik Kunci Sesi Edit: Pintu Masuk Admin Kedua Ditolak 409 dengan Dialog Draft Is Being Edited, Baca Tetap Diizinkan, dan UI Tidak Menerima Status Kunci"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-237
  - TC-GS-IMPORT-248
  - TC-GS-IMPORT-249
  - TC-GS-IMPORT-679
  - TC-GS-IMPORT-680
coverage:
  web: automated
---

# Konflik Kunci Sesi Edit: Pintu Masuk Admin Kedua Ditolak 409 dengan Dialog Draft Is Being Edited, Baca Tetap Diizinkan, dan UI Tidak Menerima Status Kunci

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client A:
  - Sesi TC: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #2 `Lenovo`, #4 `Honeywell`, #11 `Cisco`, #12 `Asus`). D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil pada TC-GS-IMPORT-249.
- Tabel varian TC-GS-IMPORT-679 (langkah 36 sampai 43):

| Varian | Aksi Sesi TC |
|---|---|
| 1 Save diblokir | klik `⋯` baris #1, pilih Edit, kosongkan Brand Name, klik `[Save]` |
| 2 Keep Editing | klik `⋯` baris #1, pilih Edit, ubah Brand Name menjadi `Acme Corporation`, klik `[Cancel]`, klik `[Keep Editing]` |
| 3 Cancel pada dialog Unsaved Changes | klik `⋯` baris #1, pilih Edit, ubah Brand Name menjadi `Acme Corporation`, klik menu sidebar Global Settings > User, klik `[Cancel]` |

- Tabel varian TC-GS-IMPORT-680 (langkah 44 sampai 53; langkah 44 dan 45 membuka sesi edit Sesi TC):

| Varian | Aksi Sesi Admin kedua |
|---|---|
| 1 Duplicate | klik `⋯` baris #2 lalu pilih Duplicate |
| 2 Edit Baris | klik `⋯` baris #4 lalu pilih Edit |
| 3 Edit this page | aktifkan Switch `Edit this page` |

- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: sesi edit Sesi TC ditutup dengan `[Cancel]` di akhir tiap blok; draft D-01 dipulihkan antar TC.

## Test Steps

### TC-GS-IMPORT-237: Admin kedua memulai sesi edit saat kunci dipegang

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi Admin kedua] Klik `⋯` pada baris #2
4. [Sesi Admin kedua] Pilih Edit
5. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
6. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
7. [Sesi Admin kedua] Verifikasi dialog tertutup
8. [Sesi Admin kedua] Verifikasi baris #2 tidak menjadi input
9. [Sesi Admin kedua] Verifikasi footer tetap `[Import (12)]`
10. [Sesi TC] Verifikasi baris #1 tetap input aktif
11. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
12. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-248: Pembacaan Staging Table oleh admin kedua tetap diizinkan

13. [Sesi TC] Klik `⋯` pada baris #1
14. [Sesi TC] Pilih Edit
15. [Sesi Admin kedua] Muat ulang halaman Import > Brand
16. [Sesi Admin kedua] Klik tombol halaman 2 pada paginator
17. [Sesi Admin kedua] Verifikasi Staging Table tampil dengan footer `[Import (12)]` tanpa dialog
18. [Sesi Admin kedua] Verifikasi halaman 2 menampilkan baris #11 `Cisco` dan #12 `Asus` tanpa dialog
19. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-249: UI admin kedua tidak menerima status kunci

20. Siapkan draft D-01 berumur 25 jam (varian 1)
21. [Sesi TC] Klik `⋯` pada baris #1
22. [Sesi TC] Pilih Edit
23. [Sesi Admin kedua] Muat ulang halaman Import > Brand
24. [Sesi Admin kedua] Hover `[Discard]`
25. [Sesi Admin kedua] Verifikasi `[Discard]` Enabled tanpa tooltip
26. [Sesi Admin kedua] Hover `[Upload File]`
27. [Sesi Admin kedua] Verifikasi `[Upload File]` Enabled tanpa tooltip
28. [Sesi Admin kedua] Hover `⋯` baris #2
29. [Sesi Admin kedua] Verifikasi `⋯` baris #2 Enabled tanpa tooltip
30. [Sesi Admin kedua] Hover `[Import (12)]`
31. [Sesi Admin kedua] Verifikasi `[Import (12)]` Enabled tanpa tooltip
32. [Sesi Admin kedua] Klik `[Import (12)]`
33. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
34. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
35. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-679: Kunci tetap dipegang saat Save diblokir, Keep Editing, atau Cancel pada dialog Unsaved Changes

Untuk setiap varian (langkah 36 sampai 43):

36. [Sesi TC] Masuk sesi edit sesuai kolom "Aksi Sesi TC" pada tabel varian TC-GS-IMPORT-679
37. [Sesi Admin kedua] Klik `⋯` pada baris #2
38. [Sesi Admin kedua] Pilih Edit
39. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
40. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
41. [Sesi TC] Verifikasi baris #1 tetap input aktif
42. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
43. [Sesi TC] Tutup sesi edit: klik `[Cancel]`, lalu klik `[Discard]` pada dialog; pulihkan draft D-01

### TC-GS-IMPORT-680: Pintu masuk Duplicate, Edit Baris, dan Edit this page oleh admin kedua ditolak

Untuk setiap varian (langkah 44 sampai 53):

44. [Sesi TC] Klik `⋯` pada baris #1
45. [Sesi TC] Pilih Edit
46. [Sesi Admin kedua] Masuk sesi edit sesuai kolom "Aksi Sesi Admin kedua" pada tabel varian TC-GS-IMPORT-680
47. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
48. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
49. [Sesi Admin kedua] Verifikasi tidak ada baris yang berupa input untuk Admin kedua
50. [Sesi Admin kedua] Verifikasi footer Admin kedua tetap `[Import (12)]`
51. [Sesi TC] Verifikasi baris #1 tetap input aktif
52. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
53. [Sesi TC] Klik `[Cancel]` pada footer

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); kedua sesi UI menjadi objek asersi.
- Spec memuat 53 langkah, dan langkah 36 sampai 43 serta 44 sampai 53 diulang per varian (3 iterasi masing-masing; ekspansi sekitar 90 langkah), di atas smell 35 langkah. Alasan: semua blok satu kelas harness (dua sesi admin) dan tiap blok berdiri sendiri dengan draft D-01 yang dipulihkan; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah ulang memakai parameter varian pada dua tabel varian di Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 19, 35, 43, 53 (menutup sesi edit Sesi TC), langkah 15, 16, 23 (muat ulang dan paginasi), langkah 20 (menyiapkan draft berumur 25 jam).
- Langkah 25, 27, 29, 31 mengasersi `Enabled tanpa tooltip` sebelum langkah 32 yang memicu dialog (8b butir 5).
- Temuan untuk QA:
  - TC-GS-IMPORT-679 dan 680 memuat tiga varian di kolom Data Uji dengan langkah yang berbeda pada langkah 1 atau 3; spec menuliskan ketiga varian pada satu langkah berparameter.
  - TC-GS-IMPORT-249 tidak mengatakan apakah sesi Total Control ditutup sebelum akhir; spec menutupnya dengan `[Cancel]` sebagai langkah penghubung.
