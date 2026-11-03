---
id: TC-FA-CF-E2E-161-resilience-edit-dan-delete
title: "Resilience: Edit dan Delete 5xx dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-287
  - TC-FA-CF-288
  - TC-FA-CF-289
  - TC-FA-CF-321
  - TC-FA-CF-322
coverage:
  web: automated
---

# Resilience: Edit dan Delete 5xx dan Timeout

## Prerequisites

- Mode: FE+BE (backend nyata). Respons 500 dan timeout dipaksa lewat intercept parsial di atas backend nyata (Pre-setup #26); state backend (data tersimpan, nilai aset) tetap diasersi.
- Akun aktor blok pertama: Total Control Company Nilai (Pre-setup #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite.
- Akun aktor blok kedua (ganti akun eksplisit di langkah 40 dan 41): Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Nilai (Pre-setup #18): `Storage Capacity`, `Rated Power` Numeric 1 Decimal Place Scope {Generator, Pump} bernilai `12.5` pada aset `A1` (Asset Name `Pump`). Company Alpha (Pre-setup #11 dan #12): `Legacy Tag`. Aksi yang gagal tidak mengubah data (S-06). Nilai data mengacu `Fixture.faCustomFields.nilai` dan `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Data Dinamis: Field Name hasil Edit yang gagal `Fail 5xx {runId}-161` dan `Fail Timeout {runId}-161`.
- Kemampuan teknis: intercept dan penundaan respons (`Spectra.intercept`) untuk request Edit dan Delete.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah; intercept dilepas segera setelah pemicu (S-09). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-287: Edit gagal 5xx

1. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
2. Ubah Field Name menjadi `Fail 5xx {runId}-161`
3. Intersep respons Edit dengan 500
4. Klik `[Save]`
5. Verifikasi toast error `Error, failed to update custom field.` tampil
6. Verifikasi modal tetap terbuka dengan input dipertahankan
7. Verifikasi `[Save]` aktif kembali
8. Lepas intersepsi
9. Tutup toast error
10. Klik icon close `[✕]`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Verifikasi baris `Storage Capacity` tetap di tabel dengan Field Name tersimpan (data tidak berubah)

### TC-FA-CF-288: Edit timeout

14. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
15. Ubah Field Name menjadi `Fail Timeout {runId}-161`
16. Tunda respons Edit melewati batas waktu
17. Klik `[Save]`
18. Verifikasi toast `Connection problem. Please try again.` tampil
19. Verifikasi modal tetap terbuka dengan input dipertahankan
20. Verifikasi `[Save]` aktif kembali
21. Lepas tahanan respons
22. Tutup toast
23. Klik icon close `[✕]`
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`

### TC-FA-CF-289: 5xx pada Save yang dikonfirmasi lewat Change Data Type

26. Klik row action `⋯` > `Edit` pada baris `Rated Power`
27. Ganti Data Type menjadi `Text`
28. Klik `[Save]`
29. Intersep respons Edit dengan 500
30. Klik `[Change Data Type]` pada dialog
31. Verifikasi toast error `Error, failed to update custom field.` tampil
32. Verifikasi modal tetap terbuka
33. Lepas intersepsi
34. Tutup toast error
35. Klik icon close `[✕]`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Buka Detail aset `A1`
39. Verifikasi nilai aset `A1` untuk `Rated Power` tidak direset (tetap `12.5`)

### TC-FA-CF-321 dan TC-FA-CF-322: Delete 5xx dan timeout (Company Alpha)

40. Ganti akun: `Logout` dari Total Control Company Nilai
41. Login sebagai Total Control Company Alpha dengan `Spectra.env.FA_TC_PASSWORD`
42. Klik row action `⋯` > `Delete` pada baris `Legacy Tag`
43. Intersep respons Delete dengan 500
44. Klik `[Delete]`
45. Verifikasi dialog Delete tertutup
46. Verifikasi toast error `Error, failed to delete custom field.` tampil
47. Lepas intersepsi
48. Verifikasi tabel di-refresh
49. Verifikasi baris `Legacy Tag` beserta nilainya tetap ada
50. Tutup toast error
51. Klik row action `⋯` > `Delete` pada baris `Legacy Tag`
52. Tunda respons Delete melewati batas waktu
53. Klik `[Delete]`
54. Verifikasi dialog Delete tertutup
55. Verifikasi toast `Connection problem. Please try again.` tampil
56. Lepas tahanan respons
57. Verifikasi tabel di-refresh
58. Verifikasi baris `Legacy Tag` tetap ada

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 58 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas b, fault injection pada Edit dan Delete), berdiri sendiri, dan tiap blok memuat Verifikasi per klausa (S-01) serta penutupan form dirty yang deterministik (S-08); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Intercept dipakai sebagai pemicu dan dilepas segera setelah pemicu (S-09). TC-FA-CF-287 sampai 289 memakai Company Nilai dan TC-FA-CF-321 dan 322 memakai Company Alpha sesuai Precondition TC; ganti akun eksplisit di langkah 40 dan 41.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 21, 33, 47, dan 56 (melepas intersepsi atau tahanan), langkah 9, 22, 34, dan 50 (menutup toast, R-12), langkah 10 sampai 12, 23 sampai 25, dan 35 sampai 37 (menutup form dirty, S-08).
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Nilai (Pre-setup #18 hanya mendeskripsikan Company); akun disediakan tim FE.
  - TC-FA-CF-289 menyebut "Ganti Data Type menjadi `Text`, klik `[Save]`, lalu `[Change Data Type]` dengan respons 500 terintersep"; spec menempatkan intersepsi sebelum klik `[Change Data Type]` (langkah 29).
  - TC-FA-CF-321 menyebut "beserta nilainya"; `Legacy Tag` Company Alpha tidak punya nilai aset di Pre-setup #12, sehingga `Verifikasi` hanya pada baris yang tetap ada.
