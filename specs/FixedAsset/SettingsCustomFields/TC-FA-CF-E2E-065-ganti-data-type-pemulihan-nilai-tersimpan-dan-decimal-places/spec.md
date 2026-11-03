---
id: TC-FA-CF-E2E-065-ganti-data-type-pemulihan-nilai-tersimpan-dan-decimal-places
title: "Ganti Data Type: Pemulihan Nilai Tersimpan dan Decimal Places"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-229
  - TC-FA-CF-230
  - TC-FA-CF-231
  - TC-FA-CF-232
coverage:
  web: automated
---

# Ganti Data Type: Pemulihan Nilai Tersimpan dan Decimal Places

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Rated Power` (Numeric 1 Decimal Place, bernilai `12.5` pada aset A1), `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`, A1 = `Gold`), dan `Maintenance Note` (Text General, bernilai `Checked` pada A1). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Maintenance Note` kembali bertipe Text beserta nilai A1) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-229: Memilih kembali Data Type tersimpan membatalkan penggantian dan memulihkan Decimal Places

2. Klik row action `⋯` > `Edit` pada baris `Rated Power`
3. Ganti Data Type menjadi `Percentage`
4. Pilih Decimal Places `2 (.00)`
5. Pilih kembali Data Type `Numeric`
6. Verifikasi Decimal Places kembali ke nilai tersimpan `1 (.0)`
7. Verifikasi kontrol Decimal Places kembali terkunci disabled
8. Klik `[Save]`
9. Verifikasi dialog `Change Data Type` tidak tampil

### TC-FA-CF-232: Mengganti Numeric ke Percentage mereset Decimal Places ke 0

10. Klik row action `⋯` > `Edit` pada baris `Rated Power`
11. Ganti Data Type menjadi `Percentage`
12. Verifikasi Decimal Places `0 (Integer)` terpilih
13. Verifikasi kontrol Decimal Places bebas dipilih (enabled)
14. Klik icon close `[✕]`
15. Verifikasi dialog `Unsaved Changes` tampil
16. Klik `[Leave]`

### TC-FA-CF-230: Memilih kembali Dropdown tersimpan memulihkan daftar opsi tersimpan

17. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
18. Ganti Data Type menjadi `Text`
19. Pilih kembali Data Type `Dropdown`
20. Verifikasi badge `Gold`, `Silver`, `Bronze` tampil kembali
21. Klik `[Save]`
22. Verifikasi dialog `Change Data Type` tidak tampil
23. Verifikasi toast netral `No changes to save.` tampil

### TC-FA-CF-231: Mengganti Data Type ke Numeric pada field bernilai memulai Decimal Places dari 0 yang bebas dipilih

24. Klik row action `⋯` > `Edit` pada baris `Maintenance Note`
25. Ganti Data Type menjadi `Numeric`
26. Verifikasi Decimal Places `0 (Integer)` terpilih
27. Verifikasi semua radio Decimal Places enabled (tidak terkunci)
28. Pilih Decimal Places `2 (.00)`
29. Klik `[Save]`
30. Klik `[Change Data Type]` pada dialog konfirmasi
31. Verifikasi kolom Data Type baris `Maintenance Note` menampilkan `Numeric`
32. Verifikasi kolom Value Setting baris `Maintenance Note` menampilkan `2 Decimal Places`

## Notes

- Urutan TC di spec: 229, 232, 230, 231. Kasus pemulihan tanpa perubahan data (229, 230) dan kasus yang tidak disimpan (232) berjalan lebih dulu; TC-FA-CF-231 mengubah dan menyimpan `Maintenance Note`, sehingga berada di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 14 sampai 16 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 30 (mengonfirmasi dialog `Change Data Type` yang menjadi bagian aksi TC-FA-CF-231).
- Pada langkah 8 dan 21 `[Save]` tanpa perubahan akhir adalah no-op; toast netral hanya diasersi pada langkah 23 karena Expected TC-FA-CF-230 menyebutnya.
- Temuan untuk QA:
  - TC-FA-CF-229 tidak menyebut toast atau penutupan modal setelah `[Save]` no-op; spec hanya mengasersi ketiadaan dialog `Change Data Type`.
  - TC-FA-CF-231 tidak menyebut toast sesudah konfirmasi; spec mengasersi hasil di kolom Data Type dan Value Setting.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
