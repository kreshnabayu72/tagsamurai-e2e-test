---
id: TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download
title: "Modal Changelog: Sort, Pagination, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-368
  - TC-AC-LA-369
  - TC-AC-LA-370
  - TC-AC-LA-371
  - TC-AC-LA-372
  - TC-AC-LA-379
  - TC-AC-LA-380
coverage:
  web: automated
---

# Modal Changelog: Sort, Pagination, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status dan 25 entri Changelog; Action `Create` dengan Old Value `—`; Modified By `Dewi A` untuk dua pengguna `Dewi Anggraini` dan `Dewi Angkasa` serta `System`; Old Value dan New Value campuran angka dan teks; entri pada sedikitnya dua hari berbeda) bersifat baca-saja untuk spec ini. Changelog adalah audit trail permanen yang tumbuh; asersi urutan memakai baris pada halaman teramati dengan sedikitnya dua nilai distinct, dan posisi `—` di akhir diamati pada halaman terakhir (S-12, S-14).
- Kemampuan teknis: membaca berkas hasil unduhan peramban untuk nama berkas, jumlah baris, dan baris header (bukan isi sel), disediakan tim FE; berkas unduhan dihapus di hook `after`. Spec menyembunyikan kolom `Field` lewat overlay Column Visibility Changelog (langkah 56 menyembunyikan, langkah 61 memulihkan); hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`), disediakan tim FE.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-368: Sort Date

1. Klik ikon Changelog
2. Verifikasi urutan awal Date Newest First
3. Klik header Date
4. Verifikasi Oldest First
5. Klik header Date
6. Verifikasi Newest First
7. Klik header Date
8. Verifikasi netral dan kembali ke urutan default

### TC-AC-LA-369: Sort alfabetis Action, Allocation ID, dan Field

9. Klik header Action
10. Verifikasi Action ascending A-Z tanpa membedakan huruf besar dan kecil
11. Klik header Action
12. Verifikasi Action descending Z-A tanpa membedakan huruf besar dan kecil
13. Klik header Allocation ID
14. Verifikasi Allocation ID ascending A-Z tanpa membedakan huruf besar dan kecil
15. Klik header Allocation ID
16. Verifikasi Allocation ID descending Z-A tanpa membedakan huruf besar dan kecil
17. Klik header Field
18. Verifikasi Field ascending A-Z tanpa membedakan huruf besar dan kecil
19. Klik header Field
20. Verifikasi Field descending Z-A tanpa membedakan huruf besar dan kecil

### TC-AC-LA-370: Sort Old Value dan New Value

21. Klik header Old Value
22. Verifikasi Old Value ascending: numerik didahulukan lalu teks
23. Pindah ke halaman terakhir
24. Verifikasi nilai `—` (Create) di akhir
25. Klik header Old Value
26. Klik header New Value
27. Verifikasi New Value ascending: numerik didahulukan lalu teks
28. Klik header New Value
29. Verifikasi New Value descending kebalikan dari ascending

### TC-AC-LA-371: Sort Modified By

30. Klik header Modified By
31. Verifikasi Modified By ascending menurut nama lengkap
32. Verifikasi `System` ikut terurut alfabetis
33. Klik header Modified By
34. Verifikasi Modified By descending kebalikan dari ascending

### TC-AC-LA-372: Header Actions

35. Verifikasi header kolom Actions tidak punya ikon sort

### TC-AC-LA-379: Pagination

36. Verifikasi default 10 data per halaman
37. Buka overlay page size
38. Verifikasi pilihan 10, 25, 50, dan 100
39. Pilih 25
40. Verifikasi 25 baris per halaman
41. Klik halaman berikutnya
42. Verifikasi tabel berpindah ke halaman 2
43. Klik halaman sebelumnya
44. Verifikasi tabel berpindah ke halaman 1

### TC-AC-LA-380: Download Changelog

45. Download as CSV pada Modal Changelog
46. Verifikasi tidak ada toast tampil
47. Verifikasi berkas `Changelog-License-Allocation.csv` terunduh
48. Download as XLSX pada Modal Changelog
49. Verifikasi tidak ada toast tampil
50. Verifikasi berkas `Changelog-License-Allocation.xlsx` terunduh
51. Ketik Search `Create`, tekan Enter
52. Download as CSV pada Modal Changelog
53. Verifikasi berkas hanya memuat baris yang cocok (jumlah baris sama dengan hasil Search)
54. Klik ikon panah `(←)`
55. Klik `⋯` pada header kolom Actions Changelog
56. Hapus centang `Field` pada overlay
57. Tekan `Esc` untuk menutup overlay
58. Download as CSV pada Modal Changelog
59. Verifikasi header berkas tanpa kolom `Field`
60. Klik `⋯` pada header kolom Actions Changelog
61. Centang `Field` pada overlay
62. Tekan `Esc` untuk menutup overlay

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah `Download as CSV` dan `Download as XLSX` berarti: klik ikon Download lalu pilih opsi dengan nama itu.
- Absence toast (langkah 46 dan 49) diletakkan segera setelah pemicu dan sebelum asersi berkas; pemicu dan berkas terunduh menjadi anchor positif (konvensi bagian 8b butir 11).
- Langkah penghubung (S-03): langkah 23 (pindah ke halaman terakhir agar posisi `—` teramati, S-14), langkah 25 (sort Old Value descending tanpa asersi sesuai langkah TC), langkah 54, 57, 62 (menutup search bar dan overlay).
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (tabel Modal Changelog) pada satu dataset baca-saja; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-370 Expected a hanya menyebut ascending Old Value; spec tidak mengasersi descending Old Value.
  - TC-AC-LA-379 menyebut data uji "25 entri" tetapi Changelog adalah audit trail permanen yang tumbuh; spec mengasersi 25 baris per halaman tanpa mengasersi jumlah total.
  - TC-AC-LA-380 butir c ("Kolom yang disembunyikan tidak ikut diekspor") tidak menyebut kolom yang disembunyikan; spec memakai `Field`.
  - TC-AC-LA-380 butir a ("terunduh tanpa toast") bersifat absence atas toast; spec memakai pemicu dan berkas terunduh sebagai anchor.
