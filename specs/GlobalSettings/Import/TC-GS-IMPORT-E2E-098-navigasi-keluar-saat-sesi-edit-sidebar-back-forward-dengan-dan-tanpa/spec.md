---
id: TC-GS-IMPORT-E2E-098-navigasi-keluar-saat-sesi-edit-sidebar-back-forward-dengan-dan-tanpa
title: "Navigasi keluar saat sesi edit: sidebar, Back, Forward dengan dan tanpa perubahan (dialog Unsaved Changes global, Leave, Cancel)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-206
  - TC-GS-IMPORT-570
  - TC-GS-IMPORT-660
  - TC-GS-IMPORT-662
  - TC-GS-IMPORT-663
coverage:
  web: automated
---

# Navigasi keluar saat sesi edit: sidebar, Back, Forward dengan dan tanpa perubahan (dialog Unsaved Changes global, Leave, Cancel)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi; pengecualian S-12), dipulihkan oleh hook `beforeEach` sesuai Kontrak Fixture R2: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, ..., #12 `Asus`) dan D-04 (Draft Division 6 baris `pending`). Nilai ubahan: `Acme Corp Baru`, `Acme Corporation`.
- Kemampuan teknis: navigasi tombol Back dan Forward browser, pengamatan dialog, skrip pemulihan draft (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01 dan D-04 dan lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-662: Back browser tanpa perubahan

1. Klik Sub-Tab Division
2. Klik Sub-Tab Brand
3. Klik `⋯` pada baris #1, pilih `Edit`
4. Tekan Back browser
5. Verifikasi tidak ada dialog yang tampil
6. Verifikasi halaman berpindah ke Import > Division dengan Breadcrumb `Import > Division`
7. Verifikasi footer tidak menampilkan `[Cancel]` dan `[Save]`

### TC-GS-IMPORT-570: Back browser dengan perubahan

8. Klik Sub-Tab Brand
9. Klik `⋯` pada baris #1, pilih `Edit`
10. Ubah Brand Name baris #1 menjadi `Acme Corp Baru`
11. Tekan Back browser
12. Verifikasi dialog dengan Title "Unsaved Changes" dan Body "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Cancel]` pada dialog
14. Verifikasi pengguna tetap di Import > Brand
15. Verifikasi baris #1 tetap input bernilai `Acme Corp Baru`
16. Verifikasi footer `[Cancel]` dan `[Save]`
17. Tekan Back browser lagi
18. Klik `[Leave]` pada dialog
19. Verifikasi halaman berpindah ke Import > Division
20. Verifikasi footer tidak lagi menampilkan `[Cancel]` dan `[Save]`

### TC-GS-IMPORT-663: Forward browser dengan perubahan

21. Klik Sub-Tab Brand
22. Klik Sub-Tab Division
23. Tekan Back browser
24. Klik `⋯` pada baris #1, pilih `Edit`
25. Ubah Brand Name baris #1 menjadi `Acme Corp Baru`
26. Tekan Forward browser
27. Verifikasi dialog dengan Title "Unsaved Changes" dan Body "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Cancel]` pada dialog
29. Verifikasi pengguna tetap di Import > Brand
30. Verifikasi baris #1 tetap input bernilai `Acme Corp Baru`
31. Verifikasi footer `[Cancel]` dan `[Save]`
32. Tekan Forward browser lagi
33. Klik `[Leave]` pada dialog
34. Verifikasi halaman berpindah ke Import > Division
35. Verifikasi footer tidak lagi menampilkan `[Cancel]` dan `[Save]`

### TC-GS-IMPORT-206 dan TC-GS-IMPORT-660: Navigasi sidebar dengan perubahan

36. Klik Sub-Tab Brand
37. Klik `⋯` pada baris #1, pilih `Edit`
38. Ubah Brand Name baris #1 menjadi `Acme Corporation`
39. Klik menu sidebar Global Settings > User
40. Verifikasi dialog dengan Title "Unsaved Changes" dan Body "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Cancel]` dan `[Leave]`
41. Klik `[Cancel]` pada dialog
42. Verifikasi dialog tertutup dan pengguna tetap di Import > Brand
43. Verifikasi baris #1 tetap input dengan nilai `Acme Corporation`
44. Verifikasi footer tetap `[Cancel]` dan `[Save]`
45. Klik menu sidebar Global Settings > User
46. Verifikasi dialog dengan Title "Unsaved Changes" dan Body "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Cancel]` dan `[Leave]`
47. Klik `[Leave]` pada dialog
48. Verifikasi halaman Global Settings > User terbuka
49. Klik menu sidebar Global Settings > Import
50. Verifikasi Import > Brand menampilkan baris #1 `Acme Corp` sebagai teks (perubahan tidak tersimpan)
51. Verifikasi footer `[Import (12)]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (navigasi browser sebagai aksi pengguna).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penggabungan: TC-206 (Cancel pada dialog sidebar) dan TC-660 (Leave) berbagi satu sesi Edit Baris dengan perubahan `Acme Corporation`; dialog pada langkah 40 dan 46 sama-sama diasersi sesuai Expected a masing-masing TC. Langkah 36 dan 37 menjalankan Precondition (kembali ke Import > Brand dengan draft D-01 tanpa sesi edit).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 sampai 3, 8, 21 sampai 24, dan 36 menyusun riwayat Back dan Forward sesuai langkah TC sumber.
- Spec berisi 51 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (navigasi keluar saat sesi edit), tiap blok membuka dan menutup sesi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-224 sampai 232 (Cancel dan Discard) ada di spec 096 dan 097.
- Temuan untuk QA:
  - TC-GS-IMPORT-570 dan 663 Langkah 10 sampai 12 (Back/Forward kedua dengan Leave) bergantung pada riwayat browser setelah dialog Cancel; spec mengikuti Langkah TC dan tidak mengasersi isi riwayat.
  - Post Condition semua TC di spec ini kosong; tidak ada yang diasersi (S-01).
