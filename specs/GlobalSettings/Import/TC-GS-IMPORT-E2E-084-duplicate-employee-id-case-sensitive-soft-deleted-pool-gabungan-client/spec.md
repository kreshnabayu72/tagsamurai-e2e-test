---
id: TC-GS-IMPORT-E2E-084-duplicate-employee-id-case-sensitive-soft-deleted-pool-gabungan-client
title: "Duplicate Employee ID: case-sensitive, soft-deleted, pool gabungan, client lain, dan urutan field tooltip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-182
  - TC-GS-IMPORT-183
  - TC-GS-IMPORT-184
  - TC-GS-IMPORT-648
  - TC-GS-IMPORT-650
  - TC-GS-IMPORT-651
  - TC-GS-IMPORT-856
coverage:
  web: automated
---

# Duplicate Employee ID: case-sensitive, soft-deleted, pool gabungan, client lain, dan urutan field tooltip

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini, R4): Division `Engineering`, Position `Finance Manager`; User Login `dewi.anggraini.c@example.com` (Employee ID `EMP-0001`) dan `rina.admin.c@example.com` (Activated); User Non Login `agus.nonlogin.c@example.com` (Employee ID `EMP-NL-01`); satu User Login soft-deleted dengan Employee ID `EMP-DEL`. Employee ID `EMP-7001` ada di Client A dan tidak ada di Client C. Client C tanpa draft pada tiap Sub-Tab sebelum tiap TC (Kontrak Fixture R1).
- Data Dinamis (berkas fixture uji, D-07; nilai literal karena draft tidak di-commit, dibuang oleh reset, dan asersi bergantung pada kecocokan dengan data Pre-setup). Header User Login: `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`; baris valid berpola `Budi,Setiawan,budi.setiawan{n}@example.com,Engineering,Finance Manager,EMP-100{n},Global Settings,` (n = nomor baris data). Header User Non Login: `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period`; baris valid berpola `Siti,Rahayu,siti.rahayu{n}@example.com,Engineering,,,rina.admin.c@example.com,`.

  Tabel "Berkas Employee ID duplicate" (3 baris data, Employee ID baris 2 diganti):

  | TC | Sub-Tab | Berkas | Employee ID baris 2 (dan baris 3) |
  |---|---|---|---|
  | 182 | User Login | `user-login-dup-emp.csv` | `EMP-0001` |
  | 650 | User Login | `user-login-dup-emp-nlu.csv` | `EMP-NL-01` (milik User Non Login existing) |
  | 648 | User Non Login | `user-non-login-dup-emp.csv` | baris 2 `EMP-0001`, baris 3 `emp-0001`; Email tiap baris berbeda |

  Tabel "Berkas Employee ID bukan duplicate" (User Login, 3 baris data, Employee ID baris 2 diganti):

  | TC | Berkas | Employee ID baris 2 |
  |---|---|---|
  | 183 | `user-login-emp-case.csv` | `emp-0001` |
  | 184 | `user-login-emp-soft.csv` | `EMP-DEL` |
  | 651 | `user-login-emp-other-client.csv` | `EMP-7001` |

  TC-856 `user-login-dup-email-emp.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Access`; 1 baris data: `Siti`, `Rahmawati`, `rina.admin.c@example.com`, `Engineering`, kosong, `EMP-0001`, `Global Settings`.
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip reset draft per Sub-Tab (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Sub-Tab User Login dan User Non Login Client C dibuang lewat skrip reset.

## Test Steps

### TC-GS-IMPORT-182, 650, 648: Employee ID sama dengan data sistem berstatus duplicate

Untuk setiap baris tabel "Berkas Employee ID duplicate" (langkah 1 sampai 12 diulang tiga kali, urutan 182, 650, 648; pada TC-648 baris 3 diverifikasi pending sesuai langkah 9):

1. Tunggu toast lama hilang otomatis; pilih Sub-Tab sesuai kolom Sub-Tab; reset draft Sub-Tab itu di Client C lewat skrip reset, lalu muat ulang halaman
2. Klik `[Upload File]`
3. Pilih berkas sesuai kolom Berkas pada file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal Column Mapping tertutup
6. Verifikasi muncul toast: "Success, row has been added."
7. Verifikasi Staging Table menampilkan 3 baris
8. Verifikasi badge Status baris 2 bertuliskan `duplicate`
9. Verifikasi badge Status baris 1 dan baris 3 bertuliskan `pending`
10. Arahkan kursor ke badge Status baris 2
11. Verifikasi tooltip pada badge Status baris 2: "Employee ID already exists. This row will be skipped automatically."
12. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-183, 184, 651: Employee ID bukan duplicate

Untuk setiap baris tabel "Berkas Employee ID bukan duplicate" (langkah 13 sampai 21 diulang tiga kali, urutan 183, 184, 651):

13. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
14. Klik `[Upload File]`
15. Pilih berkas sesuai kolom Berkas pada file picker
16. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
17. Verifikasi modal Column Mapping tertutup
18. Verifikasi muncul toast: "Success, row has been added."
19. Verifikasi badge Status baris 2 bertuliskan `pending`
20. Verifikasi Staging Table menampilkan 3 baris berstatus `pending`
21. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled)

### TC-GS-IMPORT-856: Email dan Employee ID sama-sama bentrok

22. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
23. Klik `[Upload File]`
24. Pilih berkas `user-login-dup-email-emp.csv` pada file picker
25. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
26. Verifikasi badge Status baris 1 bertuliskan `duplicate`
27. Arahkan kursor ke badge Status baris 1
28. Verifikasi tooltip pada badge Status baris 1: "Email already exists. This row will be skipped automatically."
29. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 0, Errors 0 (Disabled), Duplicates 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1-12 diulang tiga kali dan langkah 13-21 diulang tiga kali (satu putaran per baris tabel Prerequisites, tanpa langkah bersyarat). Dengan ekspansi spec berisi sekitar 72 langkah (36 + 27 + 8, termasuk langkah 22-29 TC-856). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional), tiap blok berdiri sendiri dengan reset draft dan unggah sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 13, dan 22 (menunggu toast, pemilihan Sub-Tab, reset draft, muat ulang) menjalankan Precondition "Client C tanpa draft Tab X (fixture direset sebelum TC, Kontrak Fixture R1)".
- Pada TC-648 Expected c ("Badge Status baris 3 (Employee ID `emp-0001`) bertuliskan `pending`") diasersi pada langkah 9 bersama baris 1 (TC-182 dan TC-650 hanya mengasersi baris 1 dan 3 `pending` pada Expected b).
- Pembagian TC lintas spec: TC-GS-IMPORT-179 sampai 181 dan 185 (Email) ada di spec 083.
- Temuan untuk QA:
  - Post Condition tiap TC (isi draft, direset sebelum TC berikutnya) tidak punya langkah observasi dan padanan Expected-nya sudah diasersi; tidak diasersi terpisah (S-01).
  - TC-GS-IMPORT-182, 650, dan 648: Expected b TC menyebut "baris lainnya berstatus `pending`" (TC-182, 650) sehingga spec mengasersi baris 1 dan baris 3 sekaligus; pada TC-648 Expected hanya menyebut baris 2 dan 3, sedangkan baris 1 tidak disebut. Spec mengasersi baris 1 `pending` juga (langkah 9), turunan dari kartu "Ready to Import 2" pada Expected d.
  - Mekanisme skrip reset draft per Sub-Tab (Kontrak Fixture R1) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
