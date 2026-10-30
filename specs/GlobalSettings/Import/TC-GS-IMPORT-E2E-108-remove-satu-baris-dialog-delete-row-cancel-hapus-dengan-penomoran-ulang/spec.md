---
id: TC-GS-IMPORT-E2E-108-remove-satu-baris-dialog-delete-row-cancel-hapus-dengan-penomoran-ulang
title: "Remove satu baris: dialog Delete Row, Cancel, hapus dengan penomoran ulang, dan Remove dari halaman basi memakai identitas baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-258
  - TC-GS-IMPORT-259
  - TC-GS-IMPORT-260
  - TC-GS-IMPORT-686
coverage:
  web: automated
---

# Remove satu baris: dialog Delete Row, Cancel, hapus dengan penomoran ulang, dan Remove dari halaman basi memakai identitas baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Penghapus baris kedua (hanya memicu perubahan state, P-2): sesi API dengan akun Total Control Client A yang sama pada konteks terpisah; klien HTTP disediakan tim FE/BE.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, #4 `Honeywell`, #5 `Dell`, ..., #12 `Asus`; nama literal karena asersi bergantung pada isi dan penomoran, pengecualian S-12), dipulihkan oleh hook `beforeEach` dan oleh skrip pemulihan sebelum TC-686 (Kontrak Fixture R2).
- Kemampuan teknis: skrip pemulihan draft D-01, sesi API untuk menghapus baris (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01.

## Test Steps

### TC-GS-IMPORT-258: Screening Dialog Delete Row

1. Klik `⋯` pada baris #3, pilih `Remove`
2. Verifikasi dialog dengan Title "Delete Row"
3. Verifikasi Body dialog berisi item list `Row #3`
4. Verifikasi Body dialog memuat teks "This row will be permanently removed from this draft. Are you sure you want to delete it? This action cannot be undone."
5. Verifikasi dialog memiliki tombol `[Cancel]` dan `[Delete]`

### TC-GS-IMPORT-259: Cancel pada Dialog Delete Row

6. Klik `[Cancel]`
7. Verifikasi dialog tertutup
8. Verifikasi baris #3 `Zebra Technologies` tetap ada
9. Verifikasi footer tetap `[Import (12)]`

### TC-GS-IMPORT-260: Remove satu baris dengan penomoran ulang

10. Klik `⋯` pada baris #3, pilih `Remove`
11. Klik `[Delete]`
12. Verifikasi muncul toast sukses: "Success, row has been deleted."
13. Verifikasi baris `Zebra Technologies` tidak tampil
14. Verifikasi baris `Honeywell` menjadi #3 (Row # dinomori ulang padat 1 sampai 11)
15. Verifikasi Staging Metric Cards: Total Rows 11 dan Ready to Import 11
16. Verifikasi footer `[Import (11)]`

### TC-GS-IMPORT-686: Remove dari halaman basi memakai identitas baris (paling akhir)

17. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
18. Verifikasi baris #5 `Dell` tampil pada halaman (Tab 1)
19. Penghapus baris kedua menghapus baris #3 `Zebra Technologies` lewat sesi API hingga tersimpan
20. Pada halaman yang belum dimuat ulang: klik `⋯` pada baris `Dell` (tampil sebagai #5), pilih `Remove`
21. Verifikasi dialog "Delete Row" memuat item list `Row #5`
22. Klik `[Delete]`
23. Verifikasi muncul toast sukses: "Success, row has been deleted."
24. Verifikasi baris `Dell` tidak tampil
25. Verifikasi baris `Honeywell` tetap ada
26. Verifikasi footer `[Import (10)]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; penghapus baris kedua hanya pemicu (P-2, sesi API).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-686 dijalankan paling akhir (hapus lewat halaman basi) dan TC-260 sebelumnya; langkah 17 memulihkan D-01 karena TC-260 menghapus baris.
- Langkah penghubung (tanpa `Verifikasi`): langkah 17; langkah 19 menjalankan Langkah 2 sampai 5 TC-686 sebagai penghapusan lewat sesi API, bukan sesi UI kedua (P-2).
- Pembagian TC lintas spec: TC-GS-IMPORT-262 sampai 269 dan 688 sampai 690 (seleksi dan Bulk Action) ada di spec 109 dan 110; TC-GS-IMPORT-276, 277 di spec 107.
- Temuan untuk QA:
  - TC-GS-IMPORT-686 Expected c menyebut `Honeywell` tetap ada tetapi tidak menyebut `Zebra Technologies` yang dihapus dari Tab 2; spec tidak mengasersinya.
  - TC-GS-IMPORT-260 Post Condition ("Draft Brand 11 baris") sudah diasersi pada Expected c-d.
