---
id: TC-FA-CF-E2E-064-ganti-data-type-dialog-konfirmasi-dan-tanpa-dialog
title: "Ganti Data Type: Dialog Change Data Type dan Kasus Tanpa Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-223
  - TC-FA-CF-224
  - TC-FA-CF-226
  - TC-FA-CF-240
coverage:
  web: automated
---

# Ganti Data Type: Dialog Change Data Type dan Kasus Tanpa Dialog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Empty Metric` (Numeric 2 Decimal Places General, tanpa nilai aset dan tanpa Global Value), `Deleted Only Metric` (Numeric 2 Decimal Places, bernilai hanya pada aset A3 berstatus deleted), `Global Only Numeric` (Numeric 0 Decimal Places General Global bernilai `5`, tanpa nilai aset), dan `Rated Power` (Numeric 1 Decimal Place, bernilai `12.5` pada aset A1). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Empty Metric` dan `Deleted Only Metric` kembali bertipe Numeric) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-223: Mengganti Data Type field tanpa nilai langsung tersimpan tanpa dialog

2. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
3. Ganti Data Type menjadi `Text`
4. Klik `[Save]`
5. Verifikasi dialog `Change Data Type` tidak tampil
6. Verifikasi toast sukses `Success, custom field has been updated.` tampil
7. Verifikasi kolom Data Type baris `Empty Metric` menampilkan `Text`

### TC-FA-CF-224: Nilai pada aset berstatus deleted tidak dihitung sehingga ganti Data Type tanpa dialog

8. Klik row action `⋯` > `Edit` pada baris `Deleted Only Metric`
9. Ganti Data Type menjadi `Text`
10. Tunggu toast lama hilang otomatis
11. Klik `[Save]`
12. Verifikasi dialog `Change Data Type` tidak tampil
13. Verifikasi toast sukses `Success, custom field has been updated.` tampil
14. Verifikasi kolom Data Type baris `Deleted Only Metric` menampilkan `Text`

### TC-FA-CF-226: Field hanya dengan Global Value juga memicu dialog konfirmasi saat ganti Data Type

15. Klik row action `⋯` > `Edit` pada baris `Global Only Numeric`
16. Ganti Data Type menjadi `Text`
17. Klik `[Save]`
18. Verifikasi dialog konfirmasi danger berjudul `Change Data Type` dengan bullet `• Global Only Numeric`, teks `Changing the data type will reset all existing values for this field. This action cannot be undone.`, `Are you sure you want to change it?`, serta tombol `[Cancel]` dan `[Change Data Type]` tampil
19. Klik `[Cancel]` pada dialog
20. Klik icon close `[✕]`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik `[Leave]`

### TC-FA-CF-240: Validasi inline dievaluasi sebelum dialog Change Data Type muncul

23. Klik row action `⋯` > `Edit` pada baris `Rated Power`
24. Ganti Data Type menjadi `Text`
25. Kosongkan Field Name
26. Klik `[Save]`
27. Verifikasi pesan inline `Field name must not be empty` tampil
28. Verifikasi dialog `Change Data Type` tidak tampil
29. Klik icon close `[✕]`
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`

## Notes

- Urutan TC di spec: 223, 224, 226, 240. Aksi yang menyimpan (223, 224) berjalan lebih dulu pada field milik kasusnya masing-masing; kasus dialog (226) dan validasi (240) diakhiri tanpa menyimpan supaya `Global Only Numeric` dan `Rated Power` tidak berubah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 19 sampai 22 dan 29 sampai 31 (membatalkan dialog lalu menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Kasus yang mengonfirmasi dialog `Change Data Type` pada field bernilai (TC-FA-CF-225 dan 228) ada di spec 170.
- Dialog pada langkah 18 dibaca sebagai satu elemen dialog konfirmasi (judul, bullet, teks, pertanyaan, dan tombol disebut utuh; S-01).
- Langkah penghubung toast (S-03, R-22): langkah 10 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - Precondition TC-FA-CF-223 menyebut `Empty Metric` "tanpa Global Value" dan TC-FA-CF-226 "Global Value tanpa nilai aset"; spec memakai data Pre-setup #18 apa adanya.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
