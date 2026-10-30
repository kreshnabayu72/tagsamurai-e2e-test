---
id: TC-GS-IMPORT-E2E-083-duplicate-email-terhadap-user-login-non-login-client-lain-dan-email
title: "Duplicate Email terhadap User Login, Non-Login, client lain dan email pending (Tab User Login dan User Non Login)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-179
  - TC-GS-IMPORT-180
  - TC-GS-IMPORT-181
  - TC-GS-IMPORT-185
  - TC-GS-IMPORT-649
  - TC-GS-IMPORT-819
  - TC-GS-IMPORT-820
  - TC-GS-IMPORT-869@L937
coverage:
  web: automated
---

# Duplicate Email terhadap User Login, Non-Login, client lain dan email pending (Tab User Login dan User Non Login)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini, R4): Division `Engineering`, Position `Finance Manager`; User Login `dewi.anggraini.c@example.com` (Employee ID `EMP-0001`) dan `rina.admin.c@example.com` (Activated); User Non Login `agus.nonlogin.c@example.com`. Client lain: User Login `dewi.anggraini.e@example.com` dan `budi.manager.e@example.com` (Client E), `rina.admin.limit@example.com` (Client Limit), `dewi.anggraini.g@example.com` (Client G), dan User Non Login `agus.nonlogin.g@example.com` (Client G), ada di client masing-masing dan tidak ada di Client C. Client C tanpa draft pada tiap Sub-Tab sebelum tiap TC (Kontrak Fixture R1).
- Data Dinamis (berkas fixture uji, D-07; nilai literal karena draft tidak di-commit, dibuang oleh reset, dan asersi bergantung pada kecocokan email dengan data Pre-setup). Pola baris valid User Login: `Budi,Setiawan,budi.setiawan{n}@example.com,Engineering,Finance Manager,EMP-100{n},Global Settings,` dan pola baris valid User Non Login: `Siti,Rahayu,siti.rahayu{n}@example.com,Engineering,,,rina.admin.c@example.com,` dengan n = nomor baris data:

  Header User Login: `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`. Header User Non Login: `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period`.

  Tabel "Berkas duplicate Email":

  | TC | Sub-Tab | Berkas (3 baris data) | Email baris 2 |
  |---|---|---|---|
  | 179 | User Login | `user-login-dup-email.csv` | `dewi.anggraini.c@example.com` |
  | 180 | User Login | `user-login-dup-email-nlu.csv` | `agus.nonlogin.c@example.com` (milik User Non Login existing) |
  | 181 | User Login | `user-login-dup-email-case.csv` | `  DEWI.ANGGRAINI.C@Example.com  ` (dua spasi di kiri dan di kanan) |
  | 185 | User Non Login | `user-non-login-dup-email.csv` | `dewi.anggraini.c@example.com` (milik User Login existing) |
  | 649 | User Non Login | `user-non-login-dup-email-nlu.csv` | `agus.nonlogin.c@example.com` |

  - TC-819 `user-login-dup-email-other-clients.csv` (5 baris data): baris 1 `Budi,Setiawan,budi.setiawan1@example.com,Engineering,Finance Manager,EMP-1001,Global Settings,`; baris 2 sampai 5 berpola `Budi,Setiawan,[Email],Engineering,Finance Manager,EMP-100n,Global Settings,` dengan [Email]: baris 2 `dewi.anggraini.e@example.com`, baris 3 `rina.admin.limit@example.com`, baris 4 `dewi.anggraini.g@example.com`, baris 5 `agus.nonlogin.g@example.com`.
  - TC-820 `user-non-login-dup-email-other-clients.csv` (4 baris data): baris 1 `Siti,Rahayu,siti.rahayu1@example.com,Engineering,,,rina.admin.c@example.com,`; baris 2 sampai 4 berpola `Siti,Rahayu,[Email],Engineering,,,rina.admin.c@example.com,` dengan [Email]: baris 2 `dewi.anggraini.e@example.com`, baris 3 `agus.nonlogin.g@example.com`, baris 4 `budi.manager.e@example.com`.
  - TC-869@L937 `user-login-email-pending.csv`: berkas User Login standar (D-45), 1 baris data: `Siti`, `Rahmawati`, `baru.pending.c+{runId}-083@example.com`, `Engineering`, kosong, `Global Settings`. Fixture: satu User Login milik spec di Client C (`Pemohon Ganti Email {runId}-083`, disediakan tim FE/BE lewat skrip fixture) memiliki permintaan ganti email yang belum dikonfirmasi ke `baru.pending.c+{runId}-083@example.com`; pemulihan (pembatalan permintaan dan penghapusan user fixture) dikerjakan hook `after`.
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip reset draft per Sub-Tab, fixture permintaan ganti email belum terkonfirmasi (semuanya disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Sub-Tab User Login dan User Non Login Client C dibuang lewat skrip reset; user fixture dan permintaan ganti email TC-869@L937 dibersihkan.

## Test Steps

### TC-GS-IMPORT-179, 180, 181, 185, 649: Duplicate Email terhadap User Login atau User Non Login existing

Untuk setiap baris tabel "Berkas duplicate Email" (langkah 1 sampai 12 diulang lima kali, urutan 179, 180, 181, 185, 649):

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
11. Verifikasi tooltip pada badge Status baris 2: "Email already exists. This row will be skipped automatically."
12. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-819: Email yang dipakai User di client lain (Tab User Login)

13. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
14. Klik `[Upload File]`
15. Pilih berkas `user-login-dup-email-other-clients.csv` pada file picker
16. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
17. Verifikasi modal Column Mapping tertutup
18. Verifikasi muncul toast: "Success, row has been added."
19. Verifikasi Staging Table menampilkan 5 baris
20. Verifikasi badge Status baris 1 bertuliskan `pending`
21. Verifikasi badge Status baris 2, 3, 4, dan 5 bertuliskan `duplicate`
22. Arahkan kursor ke badge Status baris 2
23. Verifikasi tooltip pada badge Status baris 2: "Email already exists. This row will be skipped automatically."
24. Arahkan kursor ke badge Status baris 3
25. Verifikasi tooltip pada badge Status baris 3: "Email already exists. This row will be skipped automatically."
26. Arahkan kursor ke badge Status baris 4
27. Verifikasi tooltip pada badge Status baris 4: "Email already exists. This row will be skipped automatically."
28. Arahkan kursor ke badge Status baris 5
29. Verifikasi tooltip pada badge Status baris 5: "Email already exists. This row will be skipped automatically."
30. Verifikasi Staging Metric Cards: Total Rows 5 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 4

### TC-GS-IMPORT-820: Email yang dipakai User di client lain (Tab User Non Login)

31. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Non Login; reset draft User Non Login Client C lewat skrip reset, lalu muat ulang halaman
32. Klik `[Upload File]`
33. Pilih berkas `user-non-login-dup-email-other-clients.csv` pada file picker
34. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
35. Verifikasi modal Column Mapping tertutup
36. Verifikasi muncul toast: "Success, row has been added."
37. Verifikasi Staging Table menampilkan 4 baris
38. Verifikasi badge Status baris 1 bertuliskan `pending`
39. Verifikasi badge Status baris 2, 3, dan 4 bertuliskan `duplicate`
40. Arahkan kursor ke badge Status baris 2
41. Verifikasi tooltip pada badge Status baris 2: "Email already exists. This row will be skipped automatically."
42. Arahkan kursor ke badge Status baris 3
43. Verifikasi tooltip pada badge Status baris 3: "Email already exists. This row will be skipped automatically."
44. Arahkan kursor ke badge Status baris 4
45. Verifikasi tooltip pada badge Status baris 4: "Email already exists. This row will be skipped automatically."
46. Verifikasi Staging Metric Cards: Total Rows 4 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 3

### TC-GS-IMPORT-869@L937: Email sama dengan email baru yang menunggu konfirmasi

47. Siapkan fixture permintaan ganti email belum terkonfirmasi untuk user `Pemohon Ganti Email {runId}-083` ke `baru.pending.c+{runId}-083@example.com` (aksi tanpa `Verifikasi`)
48. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
49. Klik `[Upload File]`
50. Pilih berkas `user-login-email-pending.csv` pada file picker
51. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
52. Verifikasi badge Status baris 1 bertuliskan `duplicate`
53. Arahkan kursor ke badge Status baris 1
54. Verifikasi tooltip pada badge Status baris 1: "Email already exists. This row will be skipped automatically."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1-12 diulang lima kali (satu putaran per baris tabel Prerequisites, tanpa langkah bersyarat). Dengan ekspansi spec berisi sekitar 102 langkah (12 langkah kali 5 putaran ditambah 42 langkah blok TC-819, TC-820, dan TC-869@L937). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional), tiap blok berdiri sendiri dengan reset draft dan unggah sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 13, 31, 48 (menunggu toast, pemilihan Sub-Tab, reset draft, muat ulang) menjalankan Precondition "Client C tanpa draft Tab X (fixture direset sebelum TC, Kontrak Fixture R1)"; langkah 47 menjalankan Precondition d TC-869@L937 (disiapkan lewat fixture).
- TC-GS-IMPORT-869@L937 diurutkan paling akhir karena membutuhkan fixture terpisah. Nomor 869 dipakai dua baris TC berbeda di `tc-import.md` (baris berkas 937 dan 1078); spec ini hanya memuat yang pertama (3e).
- Pembagian TC lintas spec: TC-GS-IMPORT-182 sampai 184 (Employee ID) ada di spec 084; TC-GS-IMPORT-869@L1078 (3g) ada di spec lain.
- Temuan untuk QA:
  - ID ganda: `TC-GS-IMPORT-869` dipakai dua kali di `tc-import.md` (baris 937 duplicate Email vs email pending, baris 1078 Import In Progress) dengan isi berbeda; `sourceTc` dan `check-suite.py` tidak dapat membedakannya, sehingga spec memakai notasi `id@baris`. TC tidak diubah; usulan QA memberi nomor baru.
  - Post Condition tiap TC (isi draft; baris `Draft ... berisi 3 baris ...`) tidak punya langkah observasi dan padanan Expected-nya sudah diasersi; tidak diasersi terpisah (S-01). Post Condition TC-869@L937 ("permintaan ganti email fixture dipulihkan") dikerjakan hook `after` dan tidak diasersi.
  - TC-GS-IMPORT-869@L937 Precondition d ("User lain di Client C memiliki permintaan ganti email yang belum dikonfirmasi ... disiapkan lewat fixture") tidak menyebut mekanisme fixture maupun user yang dipakai; spec memakai user milik spec dan fixture disediakan tim FE/BE (S-13).
  - Mekanisme skrip reset draft per Sub-Tab (Kontrak Fixture R1) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-869@L937 Expected hanya mengasersi status dan tooltip (tanpa kartu Metric); spec mengikuti TC.
