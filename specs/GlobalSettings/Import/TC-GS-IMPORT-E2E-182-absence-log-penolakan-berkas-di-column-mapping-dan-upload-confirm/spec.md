---
id: TC-GS-IMPORT-E2E-182-absence-log-penolakan-berkas-di-column-mapping-dan-upload-confirm
title: "Absence log: penolakan berkas di Column Mapping dan Upload + Confirm Mapping (Append) tidak mencatat ke Changelog Import, System Log, Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-432
  - TC-GS-IMPORT-433
coverage:
  web: automated
---

# Absence log: penolakan berkas di Column Mapping dan Upload + Confirm Mapping (Append) tidak mencatat ke Changelog Import, System Log, Activity Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client A dibagikan ke seluruh admin dan Changelog Import, System Log, serta Activity Log bersifat permanen sehingga asersi memakai baseline jumlah; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): skrip fixture pemulihan draft dasar Client A (D-01, Kontrak Fixture R2).
- Baseline log (S-12): tiga surface log dicatat sebelum aksi pemicu pertama tiap TC dari teks Pagination "Showing [From] - [To] of [N] items" (0 bila yang tampil adalah empty state): Changelog Import (icon `[Changelog]` di header halaman Import), System Log pada Detail User Sari Dewi (Tab System Log), dan Activity Log (Global Settings > Activity Log, tab User Action). Asersi memakai kesamaan total terhadap baseline, bukan angka absolut atau posisi baris.
- Data Dinamis (milik spec ini; Population Client A, nama literal karena asersi urutan baris dan jumlah; seeding idempotent dan dipulihkan sebelum tiap TC): D-01 draft Brand 12 baris `pending` (`Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`); `brand-empty-name.csv`: header `Brand Name,Catatan`; 10 baris data, baris data ke-4 Brand Name kosong dan Catatan `x` terisi; `brand-log-append-6.csv`: kolom Brand Name; 6 baris `Nikon`, `Pentax`, `Olympus`, `Fujifilm`, `Leica`, `Sigma`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan draft dasar Client A dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-432: Penolakan berkas pada Modal Column Mapping

1. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
2. Buka Changelog Import (icon `[Changelog]` di header halaman) dan catat angka total pada teks Pagination sebagai baseline Changelog
3. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total pada teks Pagination sebagai baseline System Log
4. Buka Activity Log (Global Settings > Activity Log) pada tab User Action dan catat angka total pada teks Pagination sebagai baseline Activity Log
5. Buka halaman Import > Brand
6. Klik `[Upload File]`
7. Pilih berkas `brand-empty-name.csv`
8. Klik `[Append Records]`
9. Klik `[Confirm Mapping]`
10. Verifikasi Modal Column Mapping tetap terbuka
11. Verifikasi Error Banner berheader "1 row couldn't be imported. Fix the following and upload again:"
12. Tutup Modal Column Mapping lewat `✕`
13. Verifikasi kartu Total Rows tetap 12
14. Buka Changelog Import dan baca angka total pada teks Pagination
15. Verifikasi total Changelog Import sama dengan baseline langkah 2
16. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
17. Verifikasi total System Log sama dengan baseline langkah 3
18. Buka Activity Log pada tab User Action dan baca angka total
19. Verifikasi total Activity Log sama dengan baseline langkah 4

### TC-GS-IMPORT-433: Upload dan Confirm Mapping (Append)

20. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
21. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
22. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
23. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
24. Buka halaman Import > Brand
25. Klik `[Upload File]`
26. Pilih berkas `brand-log-append-6.csv`
27. Klik `[Append Records]`
28. Klik `[Confirm Mapping]`
29. Verifikasi toast sukses "Success, row has been added." tampil
30. Verifikasi kartu Total Rows menampilkan 18
31. Buka Changelog Import dan baca angka total pada teks Pagination
32. Verifikasi total Changelog Import sama dengan baseline langkah 21
33. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
34. Verifikasi total System Log sama dengan baseline langkah 22
35. Buka Activity Log pada tab User Action dan baca angka total
36. Verifikasi total Activity Log sama dengan baseline langkah 23

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g); setiap TC memuat aksi nyata (upload berkas yang ditolak dan upload + Confirm Mapping Append) dengan baseline tiga surface sendiri, sehingga memenuhi S-05.
- Alasan melewati sekitar 35 langkah (36 langkah nominal): dua blok homogen satu kelas (absence log) yang berdiri sendiri dengan pemulihan draft di awal tiap blok. Sebagian besar langkah adalah blok baca-log berpola (buka surface, catat atau baca total, `Verifikasi` sama dengan baseline) yang tidak dihitung sebagai smell (bagian 3 konvensi). Urutan TC-432 sebelum TC-433 karena TC-433 menambah 6 baris pada draft.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan draft (langkah 1, 20), pembukaan surface dan pencatatan baseline (langkah 2 sampai 4, 21 sampai 23), pembacaan total, serta pembukaan Import > Brand dan upload. Langkah 12 menutup Modal Column Mapping lewat `✕` (tanpa perubahan dropdown, modal langsung tertutup). Asersi absence (kesamaan total) didahului Verifikasi hasil aksi (Error Banner pada langkah 11; toast dan Total Rows pada langkah 29 dan 30) sebagai anchor positif yang terhubung ke pemicu.
- Temuan untuk QA:
  - TC-GS-IMPORT-432 Expected a menyebut kartu Total Rows tetap 12 "setelah langkah 11" saat Modal Column Mapping masih terbuka; spec mengasersinya sesudah modal ditutup (langkah 13) agar kartu terbaca.
  - TC-GS-IMPORT-432 menyebut berkas dengan 10 baris data dan satu baris Brand Name kosong; header Error Banner "1 row couldn't be imported" menyiratkan satu baris ditolak walau berkas ditolak seluruhnya (PRD §6); TC tidak menjelaskan.
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
