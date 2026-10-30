---
id: TC-GS-IMPORT-E2E-110-bulk-delete-dialog-delete-rows-vs-delete-row-hapus-dua-baris-bulk
title: "Bulk Delete: dialog Delete Rows vs Delete Row, hapus dua baris, Bulk Delete dari halaman basi, Select All lalu Bulk Delete menghapus draft"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-264
  - TC-GS-IMPORT-265
  - TC-GS-IMPORT-267
  - TC-GS-IMPORT-687
coverage:
  web: automated
---

# Bulk Delete: dialog Delete Rows vs Delete Row, hapus dua baris, Bulk Delete dari halaman basi, Select All lalu Bulk Delete menghapus draft

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Penghapus baris kedua (hanya memicu perubahan state, P-2): sesi API dengan akun Total Control Client A yang sama pada konteks terpisah; klien HTTP disediakan tim FE/BE.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, ..., #4 `Honeywell`, #5 `Dell`, ..., #12 `Asus`; nama literal karena asersi bergantung pada isi dan penomoran, pengecualian S-12), dipulihkan oleh hook `beforeEach` dan oleh skrip pemulihan sebelum TC-687 dan TC-267 (Kontrak Fixture R2).
- Kemampuan teknis: skrip pemulihan draft D-01, sesi API untuk menghapus baris (disediakan tim FE/BE). Aksi Bulk Delete boleh dikonfirmasi sungguhan atas seluruh hasil Select All karena environment automation terisolasi dan draft milik automation.
- State global: draft Client A dihapus permanen pada langkah 38; hook `after` memulihkan draft ke D-01. Tidak ada state global lain yang diubah selain flag Guided Tooltip.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01.

## Test Steps

### TC-GS-IMPORT-265: Bulk Delete dengan satu baris terpilih memakai Title Delete Row

1. Centang baris #4
2. Klik `[Bulk Action ▾]`
3. Klik `[Delete]` pada overlay
4. Verifikasi dialog dengan Title "Delete Row"
5. Verifikasi Body dialog berisi item list `Row #4` lalu "This row will be permanently removed from this draft. Are you sure you want to delete it? This action cannot be undone."
6. Verifikasi dialog memiliki tombol `[Cancel]` dan `[Delete]`
7. Klik `[Cancel]`; klik `[×]` pada Bulk Action Bar untuk membersihkan seleksi

### TC-GS-IMPORT-264: Bulk Delete dua baris

8. Centang baris #2 dan #5
9. Klik `[Bulk Action ▾]`
10. Klik `[Delete]` pada overlay
11. Verifikasi dialog dengan Title "Delete Rows"
12. Verifikasi Body dialog berisi item list `Row #2` dan `Row #5` lalu "The selected rows will be permanently removed from this draft. Are you sure you want to delete them? This action cannot be undone."
13. Klik `[Delete]` pada dialog Delete Rows
14. Verifikasi muncul toast sukses: "Success, row has been deleted."
15. Verifikasi baris `Lenovo` dan `Dell` tidak tampil
16. Verifikasi Row # dinomori ulang padat 1 sampai 10 (draft menjadi 10 baris)
17. Verifikasi Bulk Action Bar hilang
18. Verifikasi tidak ada baris tercentang

### TC-GS-IMPORT-687: Bulk Delete dari halaman basi

19. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
20. Centang baris #2 (`Lenovo`)
21. Centang baris #5 (`Dell`)
22. Penghapus baris kedua menghapus baris #2 `Lenovo` lewat sesi API hingga tersimpan
23. Pada halaman yang belum dimuat ulang: klik `[Bulk Action ▾]`
24. Klik `[Delete]` pada overlay
25. Klik `[Delete]` pada dialog Delete Rows
26. Verifikasi muncul toast sukses: "Success, row has been deleted."
27. Verifikasi baris `Lenovo` dan `Dell` tidak tampil
28. Verifikasi footer `[Import (10)]` (hanya 10 baris tersisa)
29. Verifikasi tidak ada dialog error yang tampil

### TC-GS-IMPORT-267: Select All lalu Bulk Delete menghapus draft (paling akhir)

30. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
31. Centang baris #1
32. Klik `[Select All (12 records)]`
33. Klik `[Bulk Action ▾]`
34. Klik item `[Delete]`
35. Verifikasi dialog dengan Title "Delete Rows"
36. Verifikasi Body dialog berisi item list `Row #1` sampai `Row #12` lalu "The selected rows will be permanently removed from this draft. Are you sure you want to delete them? This action cannot be undone."
37. Verifikasi dialog memiliki tombol `[Cancel]` dan `[Delete]`
38. Klik `[Delete]` pada dialog Delete Rows
39. Verifikasi muncul toast sukses: "Success, row has been deleted."
40. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
41. Verifikasi Unsaved Banner tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; penghapus baris kedua hanya pemicu (P-2, sesi API).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-265 sebelum TC-264 (Cancel dahulu, lalu hapus); TC-267 paling akhir karena menghapus draft (prinsip 5 bagian 3, bagian 2 butir "Select All lalu Bulk Delete").
- Langkah penghubung (tanpa `Verifikasi`): langkah 7 (`[Cancel]`, bersihkan seleksi); langkah 19 dan 30 memulihkan D-01; langkah 22 menjalankan Langkah 3 sampai 6 TC-687 (Tab 2 menghapus baris) sebagai sesi API (P-2), bukan sesi UI kedua.
- Spec berisi 41 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Bulk Delete), tiap blok berdiri sendiri dengan pemulihan draft, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-262, 263, 266, 268, 269, 688 sampai 690 (seleksi dan Bulk Action Bar) ada di spec 109.
- Temuan untuk QA:
  - TC-GS-IMPORT-687 Expected b menyebut "hanya 10 baris tersisa" padahal dua baris (`Lenovo`, `Dell`) dihapus dari 12 baris dan salah satunya (`Lenovo`) sudah dihapus lebih dulu; spec mengasersi footer `[Import (10)]` sesuai TC.
  - TC-GS-IMPORT-267 Post Condition ("Draft Brand Client A dihapus permanen") sudah diasersi pada Expected c; TC-GS-IMPORT-264 Post Condition ("Draft Brand 10 baris") sudah diasersi pada Expected c.
