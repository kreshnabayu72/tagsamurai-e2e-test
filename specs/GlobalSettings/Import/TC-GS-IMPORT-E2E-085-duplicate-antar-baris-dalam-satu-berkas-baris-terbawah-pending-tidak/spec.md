---
id: TC-GS-IMPORT-E2E-085-duplicate-antar-baris-dalam-satu-berkas-baris-terbawah-pending-tidak
title: "Duplicate antar-baris dalam satu berkas: baris terbawah pending, tidak peka huruf besar-kecil, Email, Employee ID, Division Name+Code"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-186
  - TC-GS-IMPORT-642
  - TC-GS-IMPORT-643
  - TC-GS-IMPORT-644
  - TC-GS-IMPORT-645
  - TC-GS-IMPORT-646
  - TC-GS-IMPORT-838
coverage:
  web: automated
---

# Duplicate antar-baris dalam satu berkas: baris terbawah pending, tidak peka huruf besar-kecil, Email, Employee ID, Division Name+Code

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini, R4): Division `Engineering` (Code `ENG`), Position `Finance Manager`. Client C tanpa draft pada tiap Sub-Tab sebelum tiap TC (Kontrak Fixture R1).
- Data Dinamis (berkas fixture uji, D-07; nilai literal karena draft tidak di-commit, dibuang oleh reset, dan asersi bergantung pada kesamaan nilai antar-baris). Tabel "Berkas duplicate antar-baris" (3 baris data, baris 1 dan baris 3 sama menurut aturan tab, baris terbawah tetap `pending`):

  | TC | Sub-Tab | Berkas | Header | Baris 1 / Baris 2 / Baris 3 |
  |---|---|---|---|---|
  | 186 | Brand | `brand-mutual.csv` | `Brand Name` | `Pioneer` / `Nexus` / `Pioneer` |
  | 642 | Measurement | `measurement-mutual.csv` | `Unit Name,Symbol` | `Meter,m` / `Liter,L` / `METER,mtr` |
  | 643 | Position | `position-mutual.csv` | `Position Name` | `Teknisi Gudang` / `Kepala Shift` / `teknisi gudang` |
  | 644 | Division | `division-mutual.csv` | `Division Name,Code` | `Logistik,` / `Keuangan,KEU` / `LOGISTIK,` |
  | 645 | User Login | `user-login-mutual-email.csv` | `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period` | Email baris 1 `Siti.Rahayu@Example.com`, baris 2 `budi.setiawan2@example.com`, baris 3 `  siti.rahayu@example.com  ` (dua spasi di kiri dan di kanan); kolom lain berpola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,` (angka pada Email dan Employee ID mengikuti nomor baris data) |

  TC-646 `user-login-mutual-emp.csv`: header User Login seperti TC-645; 3 baris data; Employee ID baris 1 `EMP-5001`, baris 2 `emp-5001`, baris 3 `EMP-5001`; Email tiap baris berbeda; kolom lain berpola sama.

  TC-838 `division-dup-name-code.csv`: header `Division Name,Code`; 4 baris data: `Engineering,ENG` / `Logistik,LOG` / `Keuangan,KEU` / `Keuangan,KEU`.
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip reset draft per Sub-Tab (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Sub-Tab Brand, Measurement, Position, Division, dan User Login Client C dibuang lewat skrip reset.

## Test Steps

### TC-GS-IMPORT-186, 642, 643, 644, 645: Duplicate antar-baris, baris terbawah tetap pending

Untuk setiap baris tabel "Berkas duplicate antar-baris" (langkah 1 sampai 12 diulang lima kali, urutan 186, 642, 643, 644, 645):

1. Tunggu toast lama hilang otomatis; pilih Sub-Tab sesuai kolom Sub-Tab; reset draft Sub-Tab itu di Client C lewat skrip reset, lalu muat ulang halaman
2. Klik `[Upload File]`
3. Pilih berkas sesuai kolom Berkas pada file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal Column Mapping tertutup
6. Verifikasi muncul toast: "Success, row has been added."
7. Verifikasi badge Status baris 1 bertuliskan `duplicate`
8. Arahkan kursor ke badge Status baris 1
9. Verifikasi tooltip pada badge Status baris 1: "This row duplicates another row in this draft. It will be skipped automatically."
10. Verifikasi badge Status baris 3 (terbawah) bertuliskan `pending`
11. Verifikasi badge Status baris 2 bertuliskan `pending`
12. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-646: Employee ID antar-baris peka huruf besar-kecil

13. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
14. Klik `[Upload File]`
15. Pilih berkas `user-login-mutual-emp.csv` pada file picker
16. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
17. Verifikasi modal Column Mapping tertutup
18. Verifikasi muncul toast: "Success, row has been added."
19. Verifikasi badge Status baris 1 (Employee ID `EMP-5001`) bertuliskan `duplicate`
20. Arahkan kursor ke badge Status baris 1
21. Verifikasi tooltip pada badge Status baris 1: "This row duplicates another row in this draft. It will be skipped automatically."
22. Verifikasi badge Status baris 2 (Employee ID `emp-5001`) bertuliskan `pending`
23. Verifikasi badge Status baris 3 (Employee ID `EMP-5001`, terbawah) bertuliskan `pending`
24. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-838: Division Name dan Code sama dengan sistem dan baris kembar

25. Tunggu toast lama hilang otomatis; pilih Sub-Tab Division; reset draft Division Client C lewat skrip reset, lalu muat ulang halaman
26. Klik `[Upload File]`
27. Pilih berkas `division-dup-name-code.csv` pada file picker
28. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
29. Verifikasi modal Column Mapping tertutup
30. Verifikasi muncul toast: "Success, row has been added."
31. Verifikasi Staging Table menampilkan 4 baris
32. Verifikasi badge Status baris 1 dan baris 3 bertuliskan `duplicate`
33. Verifikasi badge Status baris 2 dan baris 4 bertuliskan `pending`
34. Arahkan kursor ke badge Status baris 1
35. Verifikasi tooltip pada badge Status baris 1: "Division name already exists. This row will be skipped automatically."
36. Arahkan kursor ke badge Status baris 3
37. Verifikasi tooltip pada badge Status baris 3: "This row duplicates another row in this draft. It will be skipped automatically."
38. Verifikasi Error Summary Callout tidak tampil
39. Verifikasi Error Summary Callout tidak memuat baris pesan "Code already exists"
40. Verifikasi Staging Metric Cards: Total Rows 4 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 2

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1-12 diulang lima kali (satu putaran per baris tabel Prerequisites, tanpa langkah bersyarat). Dengan ekspansi spec berisi sekitar 84 langkah (12 kali 5 ditambah 12 langkah TC-646 dan 16 langkah TC-838). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional), tiap blok berdiri sendiri dengan reset draft dan unggah sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 13, dan 25 (menunggu toast, pemilihan Sub-Tab, reset draft, muat ulang) menjalankan Precondition "Client C tanpa draft Tab X (fixture direset sebelum TC, Kontrak Fixture R1)".
- Asersi absence pada langkah 38 dan 39 didahului baris Staging Table tampil (langkah 31 sampai 37) sebagai anchor positif pada surface yang sama (butir 2 bagian 8b).
- Pembagian TC lintas spec: TC-GS-IMPORT-173 sampai 178 (duplicate terhadap data sistem) ada di spec 082.
- Temuan untuk QA:
  - Post Condition tiap TC (isi draft, direset sebelum TC berikutnya) tidak punya langkah observasi dan padanan Expected-nya sudah diasersi; tidak diasersi terpisah (S-01).
  - TC-GS-IMPORT-642 sampai 645 Expected menyebut baris 3 (terbawah) lalu baris 2 `pending`; urutan asersi spec mengikuti urutan Expected TC (langkah 10 lalu 11).
  - TC-GS-IMPORT-838 Expected d: tooltip baris 3 memakai teks duplikat antar-baris; Expected e memuat dua klausa (Callout tidak tampil, tanpa pesan "Code already exists") yang dipecah menjadi langkah 38 dan 39.
  - Mekanisme skrip reset draft per Sub-Tab (Kontrak Fixture R1) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
