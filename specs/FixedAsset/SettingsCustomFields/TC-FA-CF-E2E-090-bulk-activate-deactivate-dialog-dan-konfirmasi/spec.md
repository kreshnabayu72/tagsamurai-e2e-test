---
id: TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi
title: "Bulk Activate dan Deactivate: Dialog Konfirmasi, Varian Single, Seleksi Campuran, dan Konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-330
  - TC-FA-CF-331
  - TC-FA-CF-332
  - TC-FA-CF-333
  - TC-FA-CF-334
  - TC-FA-CF-335
coverage:
  web: automated
---

# Bulk Activate dan Deactivate: Dialog Konfirmasi, Varian Single, Seleksi Campuran, dan Konfirmasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menonaktifkan dan mengaktifkan field baseline Company Alpha.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12), tab General delapan baris dalam satu halaman: `Asset Serial Tag` (Active), `Legacy Tag` (Active), `Depreciated Ratio` (Inactive), dan `Compliance File` (dinonaktifkan lewat seed API di hook `before`, sehingga Inactive; dipakai sebagai precondition TC-FA-CF-332 dan TC-FA-CF-333). Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`). Spec ini menonaktifkan `Asset Serial Tag` dan `Legacy Tag` (langkah 14) lalu mengaktifkan `Depreciated Ratio` dan `Compliance File` (langkah 22); hook `after` memulihkan.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: mencentang baris tabel; seeding status `Compliance File` Inactive lewat API (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain status field baseline dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-334: Bulk dengan satu baris terpilih memakai dialog varian single

1. Centang hanya baris `Asset Serial Tag`
2. Klik `[Deactivate]` pada Bulk Action Bar
3. Verifikasi dialog konfirmasi danger berjudul `Deactivate Custom Field` dengan bullet `• Asset Serial Tag`, teks `Deactivating this field will hide it and its data from all asset forms and screens. You can reactivate it later. Are you sure you want to deactivate it?`, serta tombol `[Cancel]` dan `[Deactivate]`
4. Klik `[Cancel]`
5. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-335: Bulk Activate pada seleksi campuran mencantumkan seluruh baris terpilih

6. Centang baris `Asset Serial Tag` dan `Depreciated Ratio`
7. Klik `[Activate]` pada Bulk Action Bar
8. Verifikasi dialog `Activate Custom Fields` (jamak) mencantumkan bullet `• Asset Serial Tag` dan `• Depreciated Ratio` karena N dihitung dari seluruh baris terpilih
9. Klik `[Cancel]`
10. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-330 dan TC-FA-CF-331: Dialog Bulk Deactivate dan konfirmasi

11. Centang baris `Asset Serial Tag` dan `Legacy Tag`
12. Klik `[Deactivate]` pada Bulk Action Bar
13. Verifikasi dialog konfirmasi danger berjudul `Deactivate Custom Fields` dengan bullet `• Asset Serial Tag` dan `• Legacy Tag` dalam container scrollable, teks `Deactivating these fields will hide them and their data from all asset forms and screens. You can reactivate them later. Are you sure you want to deactivate them?`, serta tombol `[Cancel]` dan `[Deactivate]`
14. Klik `[Deactivate]` pada dialog
15. Verifikasi toast sukses `Success, custom field has been deactivated.` tampil
16. Verifikasi switch Active baris `Asset Serial Tag` dan `Legacy Tag` berada di posisi OFF
17. Verifikasi Bulk Action Bar hilang
18. Verifikasi seleksi di-reset ke 0

### TC-FA-CF-332 dan TC-FA-CF-333: Dialog Bulk Activate dan konfirmasi

19. Centang baris `Depreciated Ratio` dan `Compliance File`
20. Klik `[Activate]` pada Bulk Action Bar
21. Verifikasi dialog berjudul `Activate Custom Fields` dengan bullet `• Depreciated Ratio` dan `• Compliance File`, teks `Activating these fields will make them and their data visible in all asset forms and screens. Are you sure you want to activate them?`, serta tombol `[Cancel]` dan `[Activate]`
22. Klik `[Activate]` pada dialog
23. Verifikasi toast sukses `Success, custom field has been activated.` tampil
24. Verifikasi switch Active baris `Depreciated Ratio` dan `Compliance File` berada di posisi ON
25. Verifikasi seleksi di-reset ke 0

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 334 dan 335 (dialog tanpa mutasi, ditutup `[Cancel]`), lalu 330 dan 331, 332 dan 333 (aksi yang mengubah data; S-10). Urutan menyimpang dari urutan TC sumber (330, 331, 332, 333, 334, 335) karena TC-FA-CF-334 dan TC-FA-CF-335 membutuhkan `Asset Serial Tag` Active dan `Depreciated Ratio` Inactive seperti baseline sebelum dikonfirmasi oleh TC lain. Dialog TC-FA-CF-330 dan TC-FA-CF-331 dipakai bersama (langkah 12 sampai 14), demikian juga TC-FA-CF-332 dan TC-FA-CF-333 (langkah 20 sampai 22).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 dan 9 (menutup dialog dengan `[Cancel]`; TC tidak menyebut cara menutup), langkah 5 dan 10 (membersihkan seleksi sebelum blok berikutnya; S-09).
- Temuan untuk QA:
  - TC-FA-CF-331 menyebut "secara atomik" pada judul tanpa Expected atomisitas; tidak diasersi.
  - TC-FA-CF-334 dan TC-FA-CF-335 tidak menyebut cara menutup dialog; spec memakai `[Cancel]`.
  - TC-FA-CF-333 Expected butir b hanya "seleksi di-reset ke 0" tanpa menyebut Bulk Action Bar hilang (berbeda dengan TC-FA-CF-331 butir c); spec mengikuti TC.
  - TC-FA-CF-332 sampai 333 mensyaratkan `Compliance File` dinonaktifkan lewat seed API padahal baseline Pre-setup #12 menyebutnya Active; spec men-seed status itu di hook `before`.
