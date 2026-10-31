---
id: TC-GS-IMPORT-E2E-028-validasi-berkas-ditolak-seluruhnya-custom-field-required-kosong-client
title: "Validasi Berkas Ditolak Seluruhnya: Custom Field Required Kosong (Client G) pada User Login, User Non Login, dan Append"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-109
  - TC-GS-IMPORT-612
  - TC-GS-IMPORT-948
coverage:
  web: automated
---

# Validasi Berkas Ditolak Seluruhnya: Custom Field Required Kosong (Client G) pada User Login, User Non Login, dan Append

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client G (Putri Ananda) `totalControl_automated_qaTeam10@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client G; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client G tanpa draft Tab User Login dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client G berisi Division `Engineering` dan Position `Finance Manager` (data master Pre-setup), produk Global Settings, dan User Login aktif `rina.admin.g@example.com` (Pre-setup; dipakai sebagai Represented By pada `user-non-login-empty-badge.csv`); Custom Field Active Required `Badge Code` (Text) adalah satu-satunya Custom Field Active (Kontrak Fixture R4).
- Berkas fixture D-07 (isi literal):
  - `user-login-empty-badge.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Badge Code`; 3 baris data; baris ke-2 Badge Code kosong; baris lain Badge Code `BC-1` dan `BC-3`; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`.
  - `user-non-login-empty-badge.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period,Badge Code`; 3 baris data; baris ke-2 Badge Code kosong; baris lain Badge Code `BC-1` dan `BC-3`; baris valid mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.g@example.com,`.
  - `user-login-badge-valid.csv`: header sama dengan `user-login-empty-badge.csv`; 2 baris data valid dengan Email dan Employee ID unik, Badge Code `BC-10` dan `BC-11`.
  (Angka pada Email dan Employee ID mengikuti nomor baris data.)
- Cleanup: TC-GS-IMPORT-948 membuat draft User Login 2 baris pada Client G; draft dibuang di hook `after` (Kontrak Fixture R1), tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah selain draft Client G (dibuang hook).

## Test Steps

### TC-GS-IMPORT-109: Custom Field Required kosong pada User Login menolak seluruh berkas

1. Klik Sub-Tab User Login
2. Klik `[Upload File]`
3. Pilih berkas `user-login-empty-badge.csv` di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
6. Verifikasi Error Banner tampil di dalam modal dengan header "1 row couldn't be imported. Fix the following and upload again:"
7. Verifikasi baris pesan Error Banner `Badge code must not be empty. 2`
8. Verifikasi tidak ada toast
9. Klik `[Cancel]` pada Modal Column Mapping
10. Verifikasi modal tertutup
11. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner

### TC-GS-IMPORT-612: Custom Field Required kosong pada User Non Login menolak seluruh berkas

12. Klik Sub-Tab User Non Login
13. Klik `[Upload File]`
14. Pilih berkas `user-non-login-empty-badge.csv` di file picker
15. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
16. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
17. Verifikasi Error Banner tampil di dalam modal dengan header "1 row couldn't be imported. Fix the following and upload again:"
18. Verifikasi baris pesan Error Banner `Badge code must not be empty. 2`
19. Verifikasi tidak ada toast
20. Klik `[Cancel]` pada Modal Column Mapping
21. Verifikasi modal tertutup
22. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner

### TC-GS-IMPORT-948: Append dengan sel Custom Field Required kosong ditolak seluruhnya dan draft existing tidak berubah

23. Klik Sub-Tab User Login
24. Klik `[Upload File]` dan pilih `user-login-badge-valid.csv` di file picker
25. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
26. Verifikasi draft berisi 2 baris `pending`
27. Klik `[Upload File]` dan pilih `user-login-empty-badge.csv` di file picker
28. Klik `[Append Records]` pada Dialog Append to Draft
29. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
30. Verifikasi Modal Column Mapping tetap terbuka
31. Verifikasi Error Banner tampil dengan header "1 row couldn't be imported. Fix the following and upload again:"
32. Verifikasi baris pesan Error Banner `Badge code must not be empty. 2`
33. Klik `[Cancel]` pada Modal Column Mapping
34. Perhatikan Staging Table dan Staging Metric Cards
35. Verifikasi Staging Table tetap berisi 2 baris `pending` dari berkas pertama
36. Verifikasi Staging Metric Cards: Total Rows 2, Ready to Import 2, Errors 0

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Spec berisi 36 langkah, hanya sedikit di atas 35 langkah. Alasan: tiga TC (109, 612, 948) satu kelas (validasi berkas ditolak seluruhnya) pada tiga Sub-Tab; TC yang diblokir lebih dulu, TC yang membuat draft di akhir.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 109 dan 612 (diblokir, tidak membuat data), lalu 948 (Append membuat draft 2 baris) di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 12, 23 (pindah Sub-Tab), langkah 34 (mengamati sesuai Langkah Uji TC), langkah 33 (menutup modal dengan `[Cancel]`; mapping tidak diubah sehingga tidak ada dialog Unsaved Changes, sesuai Langkah Uji TC-GS-IMPORT-948).
- Asersi absence "tidak ada toast" (langkah 8, 19) didahului `Verifikasi` Error Banner tampil di modal sebagai anchor positif; "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11, 22) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-948 tidak menyebut Post Condition observasi selain Expected c; draft Client G dibuang oleh hook `after`.
  - Skrip reset draft Client G tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nilai data literal tanpa suffix `{runId}`.
