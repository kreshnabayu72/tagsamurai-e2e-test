---
id: TC-FA-CF-E2E-077-edit-cap-per-asset-name
title: "Edit: Pemeriksaan Cap Per Asset Name"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-278
  - TC-FA-CF-279
  - TC-FA-CF-280
  - TC-FA-CF-281
  - TC-FA-CF-282
coverage:
  web: automated
---

# Edit: Pemeriksaan Cap Per Asset Name

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Cap (pengguna Total Control Pre-setup #1 pada Company Cap, Pre-setup #16). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CAP_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Cap (#16; Max custom fields per asset name 2; tujuh field tab General pada halaman pertama): Asset Name `Compressor`, `Generator`, `Pump`, `Turbine`; Active: `Cap General` (General), `Cap Pump` ({Pump}), `Cap Compressor` ({Compressor}); Inactive: `Cap Pump Inactive` ({Pump}), `Cap Gen Inactive` ({Generator}), `Cap Both Inactive` ({Compressor, Generator}), `Cap Orphan` (Scope kosong). Hitungan field Active: `Pump` 2, `Compressor` 2, `Generator` 1, `Turbine` 1. Nama hasil rename Dinamis bersuffix `Cap Pump Renamed {runId}-077`. Nilai data mengacu `Fixture.faCustomFields.cap` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Cap lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Cap Pump`, `Cap General`, `Cap Both Inactive`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Cap yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-278: Edit field Active yang memperluas Scope ke Asset Name penuh ditolak dengan dialog batas

1. Klik row action `⋯` > `Edit` pada baris `Cap Pump`
2. Tambahkan chip `Compressor` pada Scope
3. Klik `[Save]`
4. Verifikasi dialog `Limit Reached` dengan teks `You've reached the limit of 2 custom fields for Compressor. Remove an existing field or narrow the scope, or contact support if you need a higher limit.` tampil di atas modal Edit
5. Klik `[OK]`
6. Verifikasi dialog tertutup
7. Verifikasi modal Edit tetap terbuka
8. Verifikasi seluruh input dipertahankan: Scope memuat chip `Pump` dan `Compressor`
9. Klik icon close `[✕]`
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Verifikasi kolom Scope baris `Cap Pump` menampilkan `Pump` (tidak ada data berubah)

### TC-FA-CF-279: Mengubah Scope field Active ke General ditolak bila minimal satu Asset Name penuh

13. Klik row action `⋯` > `Edit` pada baris `Cap Compressor`
14. Pilih Scope `General`
15. Klik `[Save]`
16. Verifikasi dialog `Limit Reached` dengan teks `You've reached the limit of 2 custom fields for Pump. Remove an existing field or narrow the scope, or contact support if you need a higher limit.` tampil
17. Klik `[OK]`
18. Verifikasi Save ditolak: modal tetap terbuka dan toast `Success, custom field has been updated.` tidak tampil
19. Klik icon close `[✕]`
20. Verifikasi dialog `Unsaved Changes` tampil
21. Klik `[Leave]`

### TC-FA-CF-281: Edit field Inactive yang memperluas Scope tidak diperiksa terhadap cap

22. Klik row action `⋯` > `Edit` pada baris `Cap Both Inactive`
23. Tambahkan chip `Pump` pada Scope
24. Klik `[Save]`
25. Verifikasi toast sukses `Success, custom field has been updated.` tampil
26. Verifikasi dialog batas tidak tampil
27. Verifikasi switch Active baris `Cap Both Inactive` tetap OFF (Inactive)

### TC-FA-CF-280: Edit lain pada field Active di Asset Name penuh tidak diperiksa terhadap cap

28. Klik row action `⋯` > `Edit` pada baris `Cap Pump`
29. Ubah Field Name menjadi `Cap Pump Renamed {runId}-077`
30. Tunggu toast lama hilang otomatis
31. Klik `[Save]`
32. Verifikasi toast sukses `Success, custom field has been updated.` tampil
33. Verifikasi dialog batas tidak tampil

### TC-FA-CF-282: Mempersempit Scope field Active tidak diperiksa terhadap cap

34. Klik row action `⋯` > `Edit` pada baris `Cap General`
35. Ubah Scope dari `General` menjadi `Specific Asset Name` dengan `Generator`
36. Tunggu toast lama hilang otomatis
37. Klik `[Save]`
38. Verifikasi toast sukses `Success, custom field has been updated.` tampil
39. Verifikasi dialog batas tidak tampil

## Notes

- Urutan TC di spec: 278, 279, 281, 280, 282. Kasus yang ditolak (278, 279) berjalan lebih dulu dan diakhiri tanpa menyimpan; kasus yang menyimpan berada di akhir (bagian 3 prinsip 6), dengan TC-FA-CF-282 terakhir karena mempersempit Scope `Cap General` mengurangi hitungan field Active tiap Asset Name.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 17 (menutup dialog `Limit Reached` dengan `[OK]`), langkah 9 sampai 11 dan 19 sampai 21 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Spec melewati sekitar 35 langkah (39 langkah). Seluruhnya satu topik (pemeriksaan cap saat Edit), satu akun, satu dataset Company Cap; tiap blok memakai field berbeda dan berdiri sendiri.
- Company Cap hanya memiliki tujuh field pada tab General sehingga semua baris target berada di halaman pertama tanpa mengubah ukuran halaman.
- Langkah penghubung toast (S-03, R-22): langkah 30 dan 36 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-278 menyebut dialog `Limit Reached` "di atas modal Edit" tanpa menyebut cara memeriksanya selain tampil; spec mengasersinya pada langkah yang sama dengan teks dialog.
  - TC-FA-CF-279 tidak menyebut tombol penutup dialog; spec memakai `[OK]` dari TC-FA-CF-278 supaya modal dapat ditutup.
  - Pre-setup TC tidak mencantumkan email dan nama env var password Total Control Company Cap; spec memakai `FA_TC_CAP_PASSWORD` yang disediakan tim FE.
