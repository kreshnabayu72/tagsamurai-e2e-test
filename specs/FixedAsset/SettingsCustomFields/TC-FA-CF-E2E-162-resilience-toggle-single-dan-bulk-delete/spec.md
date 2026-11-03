---
id: TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete
title: "Resilience: Toggle Single dan Bulk Delete 5xx dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-302
  - TC-FA-CF-303
  - TC-FA-CF-307
  - TC-FA-CF-308
  - TC-FA-CF-353
  - TC-FA-CF-354
coverage:
  web: automated
---

# Resilience: Toggle Single dan Bulk Delete 5xx dan Timeout

## Prerequisites

- Mode: FE+BE (backend nyata). Respons 500 dan timeout dipaksa lewat intercept parsial di atas backend nyata (Pre-setup #26); state backend (status keaktifan, field tersimpan) tetap diasersi.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12): `Asset Serial Tag` (Active), `Depreciated Ratio` (Inactive), `Legacy Tag`, dan `Compliance File`. Semua aksi gagal sehingga data tidak berubah (S-06). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Kemampuan teknis: intercept dan penundaan respons (`Spectra.intercept`) untuk request Deactivate, Activate, dan Bulk Delete; Bulk Action Bar dengan `Unselect All`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah; intercept dilepas segera setelah pemicu (S-09). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-302: Deactivate single gagal 5xx

1. Geser switch Active baris `Asset Serial Tag` ke OFF
2. Intersep respons Deactivate dengan 500
3. Klik `[Deactivate]`
4. Verifikasi toast error `Error, failed to deactivate custom field.` tampil
5. Verifikasi switch kembali ke posisi ON
6. Verifikasi status keaktifan `Asset Serial Tag` tidak berubah
7. Lepas intersepsi
8. Tutup toast error

### TC-FA-CF-303: Deactivate single timeout

9. Geser switch Active baris `Asset Serial Tag` ke OFF
10. Tunda respons Deactivate melewati batas waktu
11. Klik `[Deactivate]`
12. Verifikasi toast `Connection problem. Please try again.` tampil
13. Verifikasi switch kembali ke posisi ON
14. Lepas tahanan respons
15. Tutup toast

### TC-FA-CF-307: Activate single gagal 5xx

16. Geser switch Active baris `Depreciated Ratio` ke ON
17. Intersep respons Activate dengan 500
18. Klik `[Activate]`
19. Verifikasi toast error `Error, failed to activate custom field.` tampil
20. Verifikasi switch kembali ke posisi OFF
21. Lepas intersepsi
22. Tutup toast error

### TC-FA-CF-308: Activate single timeout

23. Geser switch Active baris `Depreciated Ratio` ke ON
24. Tunda respons Activate melewati batas waktu
25. Klik `[Activate]`
26. Verifikasi toast `Connection problem. Please try again.` tampil
27. Verifikasi switch kembali ke posisi OFF
28. Lepas tahanan respons
29. Tutup toast

### TC-FA-CF-353: Bulk Delete gagal 5xx

30. Centang dua baris (`Legacy Tag` dan `Compliance File`)
31. Intersep respons Bulk Delete dengan 500
32. Klik `[Delete]` pada Bulk Action Bar
33. Klik `[Delete]` pada dialog
34. Verifikasi dialog tertutup
35. Verifikasi toast error `Error, failed to delete custom field.` tampil
36. Verifikasi tabel di-refresh
37. Verifikasi kedua baris tetap ada
38. Verifikasi Bulk Action Bar dan seleksi dipertahankan
39. Lepas intersepsi
40. Tutup toast error
41. Klik `Unselect All`

### TC-FA-CF-354: Bulk Delete timeout

42. Centang dua baris (`Legacy Tag` dan `Compliance File`)
43. Tunda respons Bulk Delete melewati batas waktu
44. Klik `[Delete]` pada Bulk Action Bar
45. Klik `[Delete]` pada dialog
46. Verifikasi toast `Connection problem. Please try again.` tampil
47. Verifikasi tabel di-refresh
48. Verifikasi seleksi dan Bulk Action Bar dipertahankan
49. Lepas tahanan respons
50. Tutup toast
51. Klik `Unselect All`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 51 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas b, fault injection pada toggle dan Bulk Delete), berdiri sendiri, dan tiap blok pendek (7 sampai 12 langkah) dengan Verifikasi per klausa (S-01); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Intercept dipakai sebagai pemicu dan dilepas segera setelah pemicu (S-09); toast error berulang ditutup sebelum asersi berikutnya (R-12).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 14, 21, 28, 39, dan 49 (melepas intersepsi atau tahanan), langkah 8, 15, 22, 29, 40, dan 50 (menutup toast), langkah 41 dan 51 (`Unselect All`, S-09).
- Temuan untuk QA:
  - TC-FA-CF-353 dan 354 menyebut "Centang dua baris" tanpa nama; spec memakai `Legacy Tag` dan `Compliance File`.
  - TC-FA-CF-302 dan 303 tidak menyebut cara membuktikan "status keaktifan tidak berubah" selain posisi switch; spec mengasersi posisi switch (langkah 5 dan 6 TC-FA-CF-302).
