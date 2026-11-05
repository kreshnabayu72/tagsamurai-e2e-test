---
id: TC-GS-IMPORT-E2E-007-guided-tooltip-replay-lewat-3-langkah-tombol-back-navigasi-keyboard-dan
title: "Guided Tooltip Replay Lewat [?]: 3 Langkah, Tombol Back, Navigasi Keyboard, dan Target Disabled pada Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-22
  - TC-GS-IMPORT-23
  - TC-GS-IMPORT-591
  - TC-GS-IMPORT-592
coverage:
  web: automated
---

# Guided Tooltip Replay Lewat [?]: 3 Langkah, Tombol Back, Navigasi Keyboard, dan Target Disabled pada Read Only

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor:
  - Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-22, 591, dan 592. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTB_TC_PASSWORD`.
  - Read Only Client B (Mega Puspita) `readOnly_automated_qaTeam2@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-23: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTB_RO_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor; spec ini tidak menguji navigasi sehingga tidak mengulang langkah buka kecuali sesudah ganti akun.
- Data: Client B tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); flag Guided Tooltip `gs-import` aktif (seen) untuk kedua akun sesuai hook suite `before` (lihat `suite.md`; spec ini menguji replay lewat `[?]`, bukan flag otomatis). Tidak ada Data Dinamis.
- Kemampuan teknis: hover; klik `[?]`; navigasi keyboard (Enter, panah kanan, panah kiri, Esc); ganti akun.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-22: Tombol [?] memutar ulang Guided Tooltip 3 langkah

1. Hover tombol `[?]` di kanan Breadcrumb
2. Verifikasi tooltip hover "Show guide" tampil
3. Klik tombol `[?]`
4. Perhatikan Step 1
5. Verifikasi Step 1 of 3 menyorot `[Download Template]` di Dropzone dengan Title "Download Template"
6. Verifikasi Description Step 1 "Get a template for the selected import type so your file uses the expected columns."
7. Klik `[Next]`
8. Perhatikan Step 2
9. Verifikasi Step 2 of 3 menyorot `[Upload File]` di Dropzone dengan Title "Upload File"
10. Verifikasi Description Step 2 "Upload a CSV or XLSX file and map its columns. Nothing is imported until you review the staged rows."
11. Klik `[Next]`
12. Perhatikan Step 3
13. Verifikasi Step 3 of 3 menyorot Staging Metric Cards dengan Title "Staging Summary"
14. Verifikasi Description Step 3 "Track the status of your staged rows and select a card to filter the table below."
15. Verifikasi tombol `[Next]` berganti menjadi `[Done]`
16. Klik `[Done]`
17. Perhatikan halaman
18. Verifikasi walkthrough tertutup

### TC-GS-IMPORT-591: Tombol [Back] tersembunyi di Step 1 dan kembali ke langkah sebelumnya

19. Klik tombol `[?]` di kanan Breadcrumb
20. Perhatikan tombol pada Step 1
21. Verifikasi Step 1 of 3 menampilkan `[Skip]` dan `[Next]` tanpa tombol `[Back]`
22. Klik `[Next]`
23. Perhatikan tombol pada Step 2
24. Verifikasi Step 2 of 3 menampilkan `[Skip]`, `[Back]`, dan `[Next]`
25. Klik `[Back]`
26. Perhatikan tombol dan Title
27. Verifikasi walkthrough kembali ke Step 1 of 3 dengan Title "Download Template"
28. Verifikasi tombol `[Back]` tersembunyi
29. Klik `[Skip]`
30. Verifikasi walkthrough tertutup

### TC-GS-IMPORT-592: Navigasi keyboard: Enter, panah kanan, panah kiri, dan Esc

31. Klik tombol `[?]` di kanan Breadcrumb
32. Tekan tombol Enter
33. Perhatikan Step
34. Verifikasi walkthrough berpindah ke Step 2 of 3 dengan Title "Upload File"
35. Tekan tombol panah kanan
36. Perhatikan Step
37. Verifikasi walkthrough berpindah ke Step 3 of 3 dengan Title "Staging Summary"
38. Tekan tombol panah kiri
39. Perhatikan Step
40. Verifikasi walkthrough kembali ke Step 2 of 3 dengan Title "Upload File"
41. Tekan tombol Esc
42. Perhatikan halaman
43. Verifikasi walkthrough tertutup

### TC-GS-IMPORT-23: Target Guided Tooltip tetap dirender untuk Read Only pada state belum ada draft

44. Ganti akun: logout dari Total Control Client B
45. Login sebagai Read Only Client B dengan `Spectra.env.GS_CLIENTB_RO_PASSWORD`
46. Buka menu Import dari sidebar (User berada di Import > Brand)
47. Klik tombol `[?]`
48. Perhatikan Step 1
49. Verifikasi Step 1 menyorot `[Download Template]` di Dropzone yang tampil aktif
50. Klik `[Next]`
51. Perhatikan Step 2
52. Verifikasi Step 2 menyorot `[Upload File]` di Dropzone yang tampil Disabled
53. Klik `[Next]`
54. Perhatikan Step 3
55. Verifikasi Step 3 menyorot Staging Metric Cards

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 22, 591, 592, 23. TC-GS-IMPORT-23 di akhir karena ganti akun ke Read Only Client B (bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal; bagian 3).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah mengamati sesuai Langkah Uji TC (4, 8, 12, 17, 20, 23, 26, 33, 36, 39, 42, 48, 51, 54), langkah 44 sampai 46 (ganti akun dan buka menu).
- Spec melewati sekitar 35 langkah (55 langkah). Seluruhnya satu topik (replay Guided Tooltip via `[?]`) tanpa aksi yang mengubah data; tiap blok berdiri sendiri; blok pada akun lain berada di akhir dengan langkah ganti akun eksplisit.
- Temuan untuk QA:
  - Skrip reset Client B ke tanpa draft tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-22 dan 23 tidak menyebut cara pengecekan "tampil Disabled/aktif" pada target yang disorot; spec mengasersi state target seperti pada Expected TC.
