---
id: TC-GS-IMPORT-E2E-146-fault-injection-layanan-ai-timeout-melebihi-batas-diperlakukan-tanpa
title: "Fault injection layanan AI: timeout melebihi batas diperlakukan tanpa saran dan hasil disimpan saat Confirm Mapping"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-298
  - TC-GS-IMPORT-316
  - TC-GS-IMPORT-843
  - TC-GS-IMPORT-844
coverage:
  web: automated
---

# Fault injection layanan AI: timeout melebihi batas diperlakukan tanpa saran dan hasil disimpan saat Confirm Mapping

## Prerequisites

- Mode: FE+BE (backend nyata). Kegagalan dipicu di sisi layanan AI (mock AI mode tunda 6 detik), bukan lewat intercept browser; asersi memakai state draft di backend.
- Suite serial (`parallel: false`): spec mengubah state global (mode mock layanan AI) dan memakai draft Client C yang dibagikan ke seluruh admin; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client C dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - Mock layanan AI deterministik D-40 dengan mode normal dan mode "tunda 6 detik" (respons terkirim setelah 6 detik, melampaui batas 5 detik), diatur lewat hook uji di lingkungan non-produksi dan dikembalikan ke normal.
  - Skrip fixture reset Client C ke tanpa draft pada Sub-Tab Brand dan User Login (Kontrak Fixture R1).
  - Jeda nyata `Tunggu 8 detik` (di bawah batas ±30 detik) disebut eksplisit pada langkah karena objek uji adalah pelampauan batas 5 detik layanan AI.
- Data Dinamis (milik spec ini; draft tidak di-commit sehingga nama baris berkas literal sesuai D-41, D-42, D-44, D-45):
  - D-44 `ai-brand-long.csv`: kolom `Brand Name`; 1 baris dengan Brand Name nilai sumber Brand D-41 (121 karakter, `PT Samsung Electronics Indonesia Manufacturing and Distribution Company for Consumer Electronics and Home Appliances Prod`).
  - `user-login-div-gudng.csv` (D-45): header `First Name,Last Name,Email,Division,Position,Access`; 1 baris Siti Rahmawati, `siti.rahmawati@example.com`, Division `Gudng`, Position kosong; Pre-setup Client C Division `Gudang` ada; mock D-42 mode normal untuk `Gudng`: `Gudang` 0,91.
- Pemulihan (hook `after`, tidak berasumsi setup berhasil penuh): kembalikan mock AI ke mode normal, hapus draft Brand dan User Login Client C, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-298: Timeout AI Field Shortening pada sel Brand Name

1. Reset Client C ke tanpa draft pada Sub-Tab Brand (aksi fixture)
2. Atur mock layanan AI ke mode tunda 6 detik (D-40)
3. Muat ulang halaman Import > Brand
4. Klik `[Upload File]` di toolbar dan pilih berkas `ai-brand-long.csv`
5. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
6. Verifikasi baris #1 berstatus `error`
7. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "1 row"
8. Tunggu 8 detik (jeda nyata melampaui batas 5 detik layanan AI)
9. Verifikasi sel Brand Name baris #1 tidak menampilkan badge saran
10. Verifikasi sel Brand Name baris #1 tetap bernilai 121 karakter semula

### TC-GS-IMPORT-316: Timeout AI Reference Suggestion pada sel Division

11. Reset Client C ke tanpa draft pada Sub-Tab Brand dan User Login (aksi fixture)
12. Muat ulang halaman Import > User Login
13. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-div-gudng.csv`
14. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
15. Verifikasi baris #1 berstatus `error`
16. Tunggu 8 detik (jeda nyata melampaui batas 5 detik layanan AI)
17. Verifikasi sel Division baris #1 tidak menampilkan badge saran
18. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
19. Verifikasi Error Summary Callout memuat `[Create Missing Divisions]`

### TC-GS-IMPORT-843: Hasil tanpa saran AI Field Shortening disimpan dan tidak diminta ulang

20. Reset Client C ke tanpa draft pada Sub-Tab Brand dan User Login (aksi fixture)
21. Muat ulang halaman Import > Brand
22. Klik `[Upload File]` di toolbar
23. Pilih berkas `ai-brand-long.csv` di file picker
24. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
25. Verifikasi baris #1 berstatus `error`
26. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "1 row"
27. Tunggu 8 detik (jeda nyata melampaui batas 5 detik layanan AI)
28. Verifikasi sel Brand Name baris #1 tidak menampilkan badge saran
29. Verifikasi sel Brand Name baris #1 tetap bernilai 121 karakter semula
30. Kembalikan layanan AI mock ke mode normal (D-40)
31. Muat ulang halaman Import > Brand
32. Tunggu 8 detik (jeda nyata agar permintaan ulang, bila ada, sempat dikirim)
33. Verifikasi sel Brand Name baris #1 tidak menampilkan badge saran
34. Verifikasi sel Brand Name baris #1 tetap bernilai 121 karakter semula
35. Verifikasi baris #1 tetap berstatus `error`

### TC-GS-IMPORT-844: Hasil tanpa saran AI Reference Suggestion disimpan dan tidak diminta ulang

36. Reset Client C ke tanpa draft pada Sub-Tab Brand dan User Login (aksi fixture)
37. Atur mock layanan AI ke mode tunda 6 detik (D-40)
38. Muat ulang halaman Import > User Login
39. Klik `[Upload File]` di toolbar
40. Pilih berkas `user-login-div-gudng.csv` di file picker
41. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
42. Verifikasi baris #1 berstatus `error`
43. Tunggu 8 detik (jeda nyata melampaui batas 5 detik layanan AI)
44. Verifikasi sel Division baris #1 tidak menampilkan badge saran
45. Kembalikan layanan AI mock ke mode normal (D-40)
46. Muat ulang halaman Import > User Login
47. Tunggu 8 detik (jeda nyata agar permintaan ulang, bila ada, sempat dikirim)
48. Verifikasi sel Division baris #1 tidak menampilkan badge "Did you mean 'Gudang'?"
49. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
50. Verifikasi Error Summary Callout memuat `[Create Missing Divisions]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection (b) dengan pemicu di layanan AI; seluruh blok satu kelas.
- Alasan melewati sekitar 35 langkah (50 langkah nominal): empat blok homogen (dua Sub-Tab, dua TC per Sub-Tab), tiap blok berdiri sendiri dengan reset Client C di awal sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-298 dan TC-316 menguji timeout pada Confirm Mapping, TC-843 dan TC-844 menguji hasil tersimpan sesudah muat ulang.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah reset dan pengaturan mock AI (1, 2, 11, 20, 30, 36, 37, 45), muat ulang halaman Import > Sub-Tab sesudah reset atau pengaturan mock, dan jeda nyata `Tunggu 8 detik` (langkah 8, 16, 27, 32, 43, 47).
- Langkah 30 dan 45 mengembalikan mock ke mode normal sebelum muat ulang sehingga badge saran akan tampil bila halaman meminta ulang saran; itu dasar asersi "tidak diminta ulang" pada langkah 33 sampai 35 dan 48.
- Temuan untuk QA:
  - TC-GS-IMPORT-843 dan TC-GS-IMPORT-844 judulnya menyatakan "tidak diminta ulang saat halaman dimuat ulang", tetapi Expected hanya mengasersi tidak adanya badge saran sesudah muat ulang dan setelah mock dikembalikan ke mode normal; tidak ada Expected yang membaca jumlah permintaan mock. Spec hanya mengasersi Expected TC dan tidak menambah asersi jumlah permintaan.
  - TC-GS-IMPORT-298 hanya mengasersi akibat timeout pada UI dan data; "timeout 5 detik" (batas layanan) tidak ada di PRD selain dirujuk TC (EC-24, IMP-LOGIC-09); angka 5 detik dan mode tunda 6 detik berasal dari D-40.
  - Post Condition TC-GS-IMPORT-843 b dan TC-GS-IMPORT-844 b (mock dikembalikan ke normal) tidak diasersi; pemulihan dikerjakan langkah 30, 45 dan hook `after`.
  - Post Condition TC-GS-IMPORT-298 dan TC-GS-IMPORT-316 ("draft berisi 1 baris `error`") tidak punya langkah observasi tersendiri dan tidak diasersi (S-01).
  - Mekanisme mode mock AI dan skrip reset Client C tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya; disediakan tim FE/BE.
