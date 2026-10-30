---
id: TC-GS-IMPORT-E2E-043-tampilan-error-dan-penyimpanan-baris-urutan-pesan-callout-penanda-sel
title: "Tampilan Error dan Penyimpanan Baris: Urutan Pesan Callout, Penanda Sel Bukan Warna Semata, Save Edit Baris Dropdown, dan Custom Field Dijadikan Required"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-170
  - TC-GS-IMPORT-172
  - TC-GS-IMPORT-566
  - TC-GS-IMPORT-872
coverage:
  web: automated
---

# Tampilan Error dan Penyimpanan Baris: Urutan Pesan Callout, Penanda Sel Bukan Warna Semata, Save Edit Baris Dropdown, dan Custom Field Dijadikan Required

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec mengubah flag Required Custom Field `Tax ID` Client C dan memakai draft bersama Client A; lihat `suite.md`.
- Akun aktor:
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-170 dan 872. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup): hanya sesi API sebagai pemicu perubahan flag Required `Tax ID` pada TC-GS-IMPORT-872, tanpa sesi UI dan tanpa asersi di sesi itu (P-2); password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (env baru). Mekanisme "fixture permintaan" disediakan tim FE/BE (S-13).
  - Total Control (Client A, Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-172 dan 566: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun ini.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor pertama; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data Dinamis:
  - Client C: tanpa draft Tab User Login (Kontrak Fixture R1); berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4); Custom Field Active `Tax ID` (Text) opsional (Pre-setup).
  - `user-login-multi-error.csv` (TC-GS-IMPORT-170): header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`; 3 baris data; baris ke-2 melanggar tiga aturan sekaligus: First Name `A` diulang 121 kali, Division `Gudng`, Position `Seniur Developer`; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`.
  - `user-login-taxid-empty.csv` (TC-GS-IMPORT-872): berkas User Login standar (D-45) ditambah kolom `Tax ID`; 1 baris data dengan Tax ID kosong.
  - Client A: D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` dengan Brand Name nilai sumber Brand pertama D-41, 121 karakter) untuk TC-GS-IMPORT-172; D-05 draft User Login 8 baris `pending` dari `user-login-8.csv` (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, Overtime Hours `1.25` pada Row # 4) untuk TC-GS-IMPORT-566, disiapkan skrip fixture; Custom Field Shift Active dengan opsi Pagi, Siang, Malam. Mock layanan AI mode normal D-40.
- Pemulihan: flag Required `Tax ID` Client C dikembalikan ke opsional (langkah eksplisit sesudah TC-GS-IMPORT-872; hook `after` sebagai cadangan); draft Client C dan Client A dibuang atau dipulihkan ke D-05 (Kontrak Fixture R2).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun yang dipakai, lihat `suite.md`.
- Kemampuan teknis: file picker; fixture permintaan perubahan flag Required Custom Field (sesi API Admin kedua Client C, disediakan tim FE/BE); skrip seed/reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: flag Required Custom Field `Tax ID` Client C dan draft Client A/C (dipulihkan).

## Test Steps

### TC-GS-IMPORT-170: Urutan baris pesan Error Summary Callout mengikuti urutan field target lalu urutan aturan

1. Klik Sub-Tab User Login
2. Klik `[Upload File]`
3. Pilih berkas `user-login-multi-error.csv` di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal tertutup
6. Verifikasi muncul toast "Success, row has been added."
7. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
8. Verifikasi Staging Table menampilkan 3 baris; baris 2 berstatus `error` dan baris lainnya berstatus `pending`
9. Verifikasi Error Summary Callout memuat tiga baris pesan berurutan: "First Name: Max. 120 characters", "Division not found", "Position not found"
10. Verifikasi setiap baris pesan berbadge "1 row"
11. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled)
12. Buang draft User Login Client C (reset ke tanpa draft, Kontrak Fixture R1) lalu muat ulang halaman Import > User Login

### TC-GS-IMPORT-872: Sel Custom Field kosong pada baris pending yang field-nya dijadikan Required menjadi error

13. Total Control Client C: Klik `[Upload File]` dan pilih `user-login-taxid-empty.csv` di file picker
14. Total Control Client C: Klik `[Confirm Mapping]` (kolom `Tax ID` terpetakan, sel kosong)
15. Total Control Client C: Tunggu aksi selesai (modal tertutup)
16. Admin kedua Client C menjadikan `Tax ID` Required lewat fixture permintaan (sesi API) hingga tersimpan
17. Total Control Client C: muat ulang halaman Import > User Login
18. Perhatikan baris 1, Staging Metric Cards, dan Error Summary Callout
19. Verifikasi baris 1 berstatus `error`
20. Verifikasi sel `Tax ID` baris 1 kosong dengan border `danger`
21. Verifikasi sel `Tax ID` baris 1 memuat pesan sel `Tax ID must not be empty`
22. Verifikasi Error Summary Callout memuat `Tax ID must not be empty` dengan badge "1 row"
23. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 0, Errors 1
24. Pulihkan flag Required `Tax ID` Client C ke opsional lewat fixture permintaan dan buang draft User Login Client C

### TC-GS-IMPORT-172: Sel error ditandai ikon merah dan teks pesan, bukan warna semata

25. Ganti akun: logout dari Total Control Client C
26. Login sebagai Total Control Client A dengan `Spectra.env.GS_TC_PASSWORD`
27. Siapkan draft Brand D-09 pada Client A (13 baris, baris #13 `error`) lewat skrip fixture, lalu buka menu Import dari sidebar dan muat ulang halaman Import > Brand
28. Klik halaman 2 pada Pagination Staging Table
29. Perhatikan sel Brand Name baris #13 pada Staging Table
30. Verifikasi sel Brand Name baris #13 berborder merah
31. Verifikasi sel Brand Name baris #13 menampilkan ikon penanda merah
32. Verifikasi sel Brand Name baris #13 menampilkan teks pesan "Max. 120 characters"

### TC-GS-IMPORT-566: Save sesi Edit Baris dengan Custom Field Dropdown di luar opsi menyimpan baris sebagai error

33. Pulihkan draft Client A ke D-05 (User Login 8 baris `pending`) dan klik Sub-Tab User Login
34. Klik `⋯` pada baris #1
35. Pilih Edit
36. Klik sel Shift baris #1 dan ketik `Dini`
37. Perhatikan daftar pilihan pada sel Shift
38. Verifikasi daftar pilihan memuat satu pilihan `Use "Dini"`
39. Verifikasi daftar pilihan tidak memuat opsi yang cocok
40. Pilih `Use "Dini"`
41. Klik `[Save]`
42. Perhatikan toast, sel Shift baris #1, Error Summary Callout, Staging Metric Cards, dan footer
43. Verifikasi `[Save]` tidak diblokir: toast sukses "Success, row has been updated."
44. Verifikasi sesi edit berakhir
45. Verifikasi sel Shift baris #1 menampilkan `Dini` dengan border `danger` dan pesan "Dini is not a valid option for shift"
46. Verifikasi baris #1 berstatus `error`
47. Verifikasi Error Summary Callout memuat satu baris pesan "Shift: Invalid option" dengan badge "1 row"
48. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 7, Errors 1
49. Buka Global Settings > User > Custom Field
50. Perhatikan Value Setting Shift
51. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam` (tidak ada opsi dibuat oleh `[Save]`)
52. Pulihkan draft Client A ke D-05 (Kontrak Fixture R2)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- P-2: Admin kedua Client C hanya memicu perubahan flag Required `Tax ID` lewat sesi API (langkah 16), bukan objek uji; tidak ada sesi UI kedua dan tidak ada asersi di sesi Admin kedua. Pemulihan flag ditulis sebagai langkah eksplisit (langkah 24, S-09); hook `after` sebagai cadangan.
- Urutan TC: 170 dan 872 (Client C), lalu ganti akun ke Client A untuk 172 dan 566 (langkah 25 dan 26). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Alasan di atas sekitar 35 langkah (52 langkah): satu topik (tampilan error Staging Table dan penyimpanan baris) dengan dua client; tiap blok memakai draft sendiri yang dibuang atau dipulihkan; kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7, 18, 29, 37, 42, 50 (mengamati sesuai Langkah Uji TC), langkah 12, 24, 27, 33, 52 (reset/seed/pemulihan, S-09; langkah 27 juga membuka menu Import dari sidebar sebelum muat ulang karena halaman sesudah ganti akun belum berada di Import), langkah 25 dan 26 (ganti akun), langkah 49 (navigasi ke Custom Field), langkah 16 (pemicu P-2), langkah 15 (menunggu aksi selesai sebelum Admin kedua mengubah flag Required).
- Pembagian TC: TC-GS-IMPORT-172 bergantung pada draft D-09 (hasil TC-GS-IMPORT-74 di spec 018); spec ini menyiapkan D-09 sendiri lewat skrip fixture dan tidak menumpang hasil spec lain (S-06). TC-GS-IMPORT-566 bergantung pada draft D-05 (hasil TC-GS-IMPORT-5 di spec 012); spec ini menyiapkan D-05 lewat skrip fixture.
- Temuan untuk QA:
  - TC-GS-IMPORT-872 memakai "fixture permintaan" untuk menjadikan `Tax ID` Required tanpa mendefinisikan mekanismenya di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan (S-13). Password akun Admin kedua Client C tidak ada di TC; env `GS_CLIENTC_TC2_PASSWORD` baru.
  - TC-GS-IMPORT-172 menyebut Dependensi TC-GS-IMPORT-74 dan TC-GS-IMPORT-566 menyebut TC-GS-IMPORT-5; spec memulihkan draft D-09 dan D-05 lewat skrip fixture karena tidak boleh menumpang hasil spec lain.
  - Skrip seed/reset draft tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nilai literal tanpa suffix `{runId}`.
