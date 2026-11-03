---
id: TC-FA-LIC-E2E-141-changelog-allocation-quota-paginasi-25-entri
title: "Paginasi Modal Changelog Allocation Quota dengan 25 Entri: Page Size, Nomor Halaman, Sort, Search, dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-357
  - TC-FA-LIC-358
  - TC-FA-LIC-359
coverage:
  web: automated
---

# Paginasi Modal Changelog Allocation Quota dengan 25 Entri: Page Size, Nomor Halaman, Sort, Search, dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data: riwayat Changelog Allocation Quota Pre-setup #27 (6 entri) ditambah sampai 25 entri lewat fixture BE (disediakan tim FE/BE; komposisi entri tambahan tidak didefinisikan di TC, spec mensyaratkan sedikitnya 11 entri dengan Action `Edit` sehingga Search `edit` dan Filter Action `Edit` mengembalikan lebih dari 10 baris). Hook `before` menambah entri dan hook `after` memulihkan riwayat ke Pre-setup #27 lewat fixture BE pemulih riwayat.
- Spec ini tidak mengubah state global; Sort dan Search yang diubah spec dikembalikan ke netral dan kosong di akhir blok.

## Test Steps

### TC-FA-LIC-357: Default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Verifikasi default 10 baris per halaman
3. Ketik nomor halaman 2 pada input, tekan Enter
4. Verifikasi input nomor halaman 2 langsung membuka halaman 2
5. Buka pilihan page size
6. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
7. Pilih 25
8. Verifikasi seluruh 25 baris tampil dalam satu halaman
9. Verifikasi tabel kembali ke halaman 1

### TC-FA-LIC-358: Nomor halaman tidak valid diabaikan, ganti sort tetap di halaman, ganti page size ke halaman 1

10. Pilih page size 10
11. Pindah ke halaman 2
12. Ketik `0` pada input nomor halaman, tekan Enter
13. Ketik `99` pada input nomor halaman, tekan Enter
14. Ketik `abc` pada input nomor halaman, tekan Enter
15. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2
16. Klik header kolom `Date` untuk sort
17. Verifikasi mengganti sort tetap di halaman 2
18. Klik header kolom `Date` dua kali lagi sampai netral
19. Ganti page size menjadi 25
20. Verifikasi mengganti page size kembali ke halaman 1

### TC-FA-LIC-359: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

21. Pilih page size 10
22. Pindah ke halaman 2
23. Ketik Search `edit`, tekan Enter
24. Verifikasi setelah Search tabel kembali ke halaman 1
25. Pindah ke halaman 2 lagi
26. Klik ikon Filter, pada `Action` pilih `Edit`, klik `[Apply]`
27. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
28. Klik `[Clear Field]`, klik `[Apply]`, klik icon panah `(←)` di kiri toolbar, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 10 dan 21 mengembalikan page size ke 10; langkah 18 mengembalikan sort ke netral; langkah 28 membersihkan filter dan Search lalu menutup modal (S-09).
- Perubahan urutan di TC-FA-LIC-357: lompat ke halaman 2 (langkah 3 dan 4) dilakukan sebelum mengganti page size ke 25, karena dengan 25 entri dan page size 25 halaman 2 tidak ada. TC menulis lompat sesudah ganti page size dengan frasa "bila tersedia".
- Temuan untuk QA:
  - TC-FA-LIC-357 langkah 4 dan 5 membuat halaman 2 tidak tersedia pada page size 25 dengan 25 entri; butir d memakai frasa "(bila tersedia)".
  - TC-FA-LIC-358 langkah 4 tidak menyebut kolom sort; spec memakai `Date`.
  - TC-FA-LIC-359 tidak menyebut kata kunci Search yang mengembalikan lebih dari 10 baris dan komposisi 25 entri; spec memakai `edit` dengan syarat fixture di Prerequisites.
