---
id: TC-FA-FAAM-E2E-237-multi-konteks-dua-edit-last-write-wins
title: "Multi-Konteks: Dua Edit Bersamaan pada Record yang Sama (Last-Write-Wins dan Keunikan Tetap Ditolak)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-235
  - TC-FA-FAAM-641
  - TC-FA-FAAM-642
coverage:
  web: automated
---

# Multi-Konteks: Dua Edit Bersamaan pada Record yang Sama (Last-Write-Wins dan Keunikan Tetap Ditolak)

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor sesi A: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1, dua sesi untuk skenario paralel; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Sesi B adalah konteks UI kedua dengan akun yang sama, dibuka pada langkah 1 dan ditutup pada langkah 44 (sesi B menjadi objek asersi). Akun harus mengizinkan dua sesi web paralel (kemampuan disediakan tim FE/BE). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 10 (`Dell Latitude`, dipakai sebagai nama yang sudah ada pada TC-FA-FAAM-642; tidak diubah), No. 24 (UoM `Unit`, `Pcs`).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-237`, Code literal Tabel Dinamis (batas panjang Code; hook `before` menghapus sisa Code yang sama dari run lama): `Edit Target Item 235 {runId}-237` (Code `ETI235`; Tabel Dinamis No. 35), `Edit Target Item 641 {runId}-237` (Code `ETI641`; salinan fixture 13d, Total Asset 0, UoM `Unit`), dan `Edit Target Item 642 {runId}-237` (Code `ETI642`; No. 54). Hasil edit: Code `LWW-A` dan `LWW-B` (TC-FA-FAAM-235), Code `ETI641-B` dan UoM `Pcs` (TC-FA-FAAM-641), nama `Renamed 642 B {runId}-237` (TC-FA-FAAM-642).
- Kemampuan teknis: dua konteks UI paralel untuk akun yang sama; Modal Changelog dan Search di dalamnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tutup konteks UI kedua dan hapus seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-235, 641, 642: login sebagai Total Control pada dua sesi dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan sesi B

1. Sesi B: buka konteks UI kedua, login sebagai Total Control, dan buka Fixed Asset > Settings > Asset Master > Asset Name
2. Sesi A: ketik Search `{runId}-237`, tekan Enter
3. Sesi B: ketik Search `{runId}-237`, tekan Enter

### TC-FA-FAAM-235: Dua Edit bersamaan pada record yang sama: yang terakhir menang

4. Sesi A: klik `⋯` baris `Edit Target Item 235 {runId}-237` lalu `Edit`
5. Sesi B: klik `⋯` baris `Edit Target Item 235 {runId}-237` lalu `Edit`
6. Sesi A: ubah Code menjadi `LWW-A`
7. Sesi A: klik `[Save]`
8. Tunggu aksi selesai
9. Sesi B: ubah Code menjadi `LWW-B`
10. Sesi B: klik `[Save]`
11. Verifikasi Save sesi B sukses
12. Verifikasi tidak ada dialog konflik di sesi B
13. Verifikasi Code akhir `LWW-B`
14. Klik icon Changelog
15. Ketik Search `Edit Target Item 235 {runId}-237`, tekan Enter
16. Verifikasi Changelog memuat dua entri Edit Code
17. Tutup Modal Changelog

### TC-FA-FAAM-641: Dua Edit pada field berbeda di record yang sama

18. Sesi A: klik `⋯` baris `Edit Target Item 641 {runId}-237` lalu `Edit`
19. Sesi B: klik `⋯` baris `Edit Target Item 641 {runId}-237` lalu `Edit`
20. Sesi A: ubah UoM menjadi `Pcs`
21. Sesi B: ubah Code menjadi `ETI641-B`
22. Sesi A: klik `[Save]`
23. Tunggu aksi selesai
24. Sesi B: klik `[Save]`
25. Verifikasi kedua Save sukses
26. Verifikasi tidak ada dialog konflik pada kedua sesi
27. Klik icon Changelog
28. Ketik Search `Edit Target Item 641 {runId}-237`, tekan Enter
29. Verifikasi Changelog memuat entri Edit masing-masing sesi (Field `UoM` dari sesi A dan Field `Code` dari sesi B)
30. Verifikasi Code akhir `ETI641-B` (field yang diubah sesi B menimpa sesuai kiriman B)
31. Tutup Modal Changelog

### TC-FA-FAAM-642: Last-write-wins tetap menolak pelanggaran keunikan dan guard

32. Sesi A: klik `⋯` baris `Edit Target Item 642 {runId}-237` lalu `Edit`
33. Sesi B: klik `⋯` baris `Edit Target Item 642 {runId}-237` lalu `Edit`
34. Sesi B: ubah Asset Name menjadi `Renamed 642 B {runId}-237`
35. Sesi B: klik `[Save]`
36. Tunggu aksi selesai
37. Sesi A: ubah Asset Name menjadi `Dell Latitude`
38. Sesi A: klik `[Save]`
39. Verifikasi Save sesi A ditolak sebagai duplikat nama
40. Verifikasi tidak ada dialog konflik versi di sesi A
41. Sesi A: klik `✕` pada Modal Edit
42. Verifikasi dialog `Unsaved Changes`
43. Sesi A: klik `[Leave]`
44. Tutup konteks UI kedua dan hapus sesi login browser terkait

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka sesi B), langkah 2 dan 3 (Search di kedua sesi), langkah 8, 23, dan 36 (`Tunggu aksi selesai` sesudah `[Save]` sesi A atau sesi B tanpa hasil yang diasersi, sebelum aksi sesi lain), langkah 14, 15, 17, 27, 28, 31 (membuka, mencari, dan menutup Modal Changelog; S-12, S-14), langkah 41 sampai 43 (menutup form dirty secara deterministik; S-08), dan langkah 44 (menutup konteks kedua; S-09).
- Di atas smell 35 langkah. Spec berisi 44 langkah, di atas ~35. Alasan: seluruh blok kelas c (dua sesi pada record yang sama), tiap blok memakai seed sendiri dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Asersi Save sukses pada langkah 11 dan 25 mengamati toast `Success, asset name has been updated.` (teks toast Edit sukses pada TC-FA-FAAM-604 dan 731).
- Temuan untuk QA:
  - TC-FA-FAAM-641 butir c ("field yang diubah B menimpa sesuai kiriman B") tidak menyebut nilai akhir UoM; spec hanya mengasersi Code akhir dan entri Changelog masing-masing sesi.
  - TC-FA-FAAM-642 tidak menyebut pesan duplikat nama pada Edit; spec mengasersi penolakan duplikat tanpa teks (teks pada Create: `Asset name already exists`).
  - TC-FA-FAAM-235 butir c menyebut "dua entri Edit Code" tanpa nilai Old/New; spec tidak mengasersi nilai.
