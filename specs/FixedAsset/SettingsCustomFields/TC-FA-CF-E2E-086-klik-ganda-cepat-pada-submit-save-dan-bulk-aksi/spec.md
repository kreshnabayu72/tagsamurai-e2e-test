---
id: TC-FA-CF-E2E-086-klik-ganda-cepat-pada-submit-save-dan-bulk-aksi
title: "Klik Ganda Cepat pada Submit, Save, dan Konfirmasi Bulk Deactivate serta Bulk Activate"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-186
  - TC-FA-CF-290
  - TC-FA-CF-633
  - TC-FA-CF-634
coverage:
  web: automated
---

# Klik Ganda Cepat pada Submit, Save, dan Konfirmasi Bulk Deactivate serta Bulk Activate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini membuat, mengubah, dan menonaktifkan field Company Nilai serta membaca Changelog permanen yang dibagi suite.
- Akun aktor: Total Control Company Nilai (Pre-setup #18; pengguna Sarah Johnson, Modified By `Sarah J`), kredensial `Spectra.env.FA_TC_NILAI_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, memuat baseline Company Alpha #11 dan #12): `Storage Capacity` (Numeric 0 Decimal Places, Scope {Generator, Pump}) menjadi target langkah 12. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.nilai`).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; dipakai langkah 24 sampai 48): `Bulk Off A {runId}-086` dan `Bulk Off B {runId}-086` (Text, Active); `Bulk On A {runId}-086` dan `Bulk On B {runId}-086` (Text, Inactive). Field Dinamis langkah 2 dibuat spec lewat UI: `Double Click {runId}-086` (Text). Cleanup: hook `after` menghapus semua field bersuffix `{runId}-086` yang masih ada lewat API tanpa mengandalkan seeding berhasil penuh; seed reset Company memulihkan `Storage Capacity`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: klik ganda cepat pada `[Submit]`, `[Save]`, dan tombol konfirmasi dialog Bulk; Search tabel Custom Fields dan Modal Changelog; interception respons yang menunda respons Create, Save, Bulk Deactivate, dan Bulk Activate selama 3 detik (Pre-setup #26), hanya untuk mengamati state UI (bukan fault injection) dan dilepas segera sesudah asersi state sementara (langkah 8, 18, 31, dan 44).
- State global: tidak ada yang diubah selain data field di atas dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-186: Klik ganda cepat pada Submit hanya membuat satu field

1. Klik `[+ Custom Field]`
2. Isi Field Name `Double Click {runId}-086`
3. Pilih Data Type `Text`
4. Tunda respons Create 3 detik
5. Klik `[Submit]` dua kali dengan cepat
6. Verifikasi tombol `[Submit]` menampilkan state loading setelah klik pertama
7. Verifikasi tombol `[Submit]` disabled setelah klik pertama
8. Lepas tahanan respons Create
9. Ketik Search `Double Click {runId}-086`, tekan Enter
10. Verifikasi tabel memuat tepat satu baris `Double Click {runId}-086`

### TC-FA-CF-290: Klik ganda cepat pada Save hanya menyimpan satu perubahan

11. Ganti isi kotak search dengan `Storage Capacity`, tekan Enter
12. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
13. Ubah Field Name menjadi `Double Save {runId}-086`
14. Tunda respons Save 3 detik
15. Klik `[Save]` dua kali dengan cepat
16. Verifikasi tombol `[Save]` menampilkan state loading setelah klik pertama
17. Verifikasi tombol `[Save]` disabled setelah klik pertama
18. Lepas tahanan respons Save
19. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
20. Klik icon Changelog
21. Ketik Search `Double Save {runId}-086` pada Modal Changelog, tekan Enter
22. Verifikasi Modal Changelog memuat tepat satu entri Action `Edit` untuk `Double Save {runId}-086`
23. Tutup modal Changelog dengan `✕`

### TC-FA-CF-633: Klik ganda cepat pada konfirmasi Bulk Deactivate

24. Ganti isi kotak search dengan `Bulk Off`, tekan Enter
25. Centang baris `Bulk Off A {runId}-086` dan `Bulk Off B {runId}-086`
26. Klik `[Deactivate]` pada Bulk Action Bar
27. Tunda respons Bulk Deactivate 3 detik
28. Klik `[Deactivate]` pada dialog dua kali dengan cepat
29. Verifikasi tombol konfirmasi dialog menampilkan state loading setelah klik pertama
30. Verifikasi tombol konfirmasi dialog disabled setelah klik pertama
31. Lepas tahanan respons Bulk Deactivate
32. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
33. Klik icon Changelog
34. Ketik Search `Bulk Off` pada Modal Changelog, tekan Enter
35. Verifikasi Modal Changelog memuat tepat satu baris Action `Deactivate` per field, yaitu `Bulk Off A {runId}-086` dan `Bulk Off B {runId}-086` (dua baris Deactivate total)
36. Tutup modal Changelog dengan `✕`

### TC-FA-CF-634: Klik ganda cepat pada konfirmasi Bulk Activate

37. Ganti isi kotak search dengan `Bulk On`, tekan Enter
38. Centang baris `Bulk On A {runId}-086` dan `Bulk On B {runId}-086`
39. Klik `[Activate]` pada Bulk Action Bar
40. Tunda respons Bulk Activate 3 detik
41. Klik `[Activate]` pada dialog dua kali dengan cepat
42. Verifikasi tombol konfirmasi dialog menampilkan state loading setelah klik pertama
43. Verifikasi tombol konfirmasi dialog disabled setelah klik pertama
44. Lepas tahanan respons Bulk Activate
45. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
46. Klik icon Changelog
47. Ketik Search `Bulk On` pada Modal Changelog, tekan Enter
48. Verifikasi Modal Changelog memuat tepat satu baris Action `Activate` per field, yaitu `Bulk On A {runId}-086` dan `Bulk On B {runId}-086` (dua baris Activate total)
49. Tutup modal Changelog dengan `✕`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (49 langkah). Seluruhnya satu topik (klik ganda cepat pada tombol konfirmasi tulis) dan satu Company; empat blok berdiri sendiri dengan data milik sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; tiap blok hanya berisi satu penundaan respons, satu aksi klik ganda, dan pembacaan Changelog.
- Urutan TC dalam spec: 186, 290, 633, 634 (aksi tulis berurutan tanpa Delete); sama dengan urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 14, 27, dan 40 (menunda respons 3 detik sebelum klik ganda; Pre-setup #26), langkah 8, 18, 31, dan 44 (melepas tahanan respons sesudah asersi state sementara, bagian 8b butir 11), langkah 19, 32, dan 45 (Tunggu aksi selesai sebelum Modal Changelog dibuka; bagian 8b butir 8), langkah 9, 11, 24, dan 37 (Search agar baris target tampil; tabel Company Nilai memuat lebih dari sepuluh baris), langkah 20, 33, dan 46 (membuka Modal Changelog), langkah 21, 34, dan 47 (Search entri), serta langkah 23, 36, dan 49 (menutup modal Changelog).
- Asersi tambahan di luar Expected TC (S-03): TC-FA-CF-186 butir b dan TC-FA-CF-290, TC-FA-CF-633, TC-FA-CF-634 menulis "state loading dan disabled" sebagai dua `Verifikasi` (langkah 6 dan 7, 16 dan 17, 29 dan 30, 42 dan 43) karena spinner dan state tombol adalah klausa terpisah; urutannya mendahului asersi hasil (bagian 8b butir 5) dan ditulis selagi respons masih ditahan.
- Data milik spec (S-06, S-12): TC-FA-CF-633 dan TC-FA-CF-634 menyebut field Pre-setup `Asset Serial Tag`, `Legacy Tag`, `Depreciated Ratio`, dan `Compliance File`; spec memakai field Dinamis bersuffix `{runId}-086` agar jumlah baris Deactivate dan Activate pada Changelog permanen dapat diasersi dari baseline nol (S-12), tanpa mengubah field Pre-setup bersama.
- Temuan untuk QA:
  - TC-FA-CF-290 tidak menyebut apakah entri Changelog Edit untuk perubahan Field Name memuat nama lama atau nama baru; spec mencari nama baru `Double Save {runId}-086`.
  - TC-FA-CF-290 menyebut Company Nilai tanpa alasan pemakaian nilai aset; langkah TC tidak menyentuh nilai aset.
  - Email akun Total Control Company Nilai tidak ada di Pre-setup TC.
