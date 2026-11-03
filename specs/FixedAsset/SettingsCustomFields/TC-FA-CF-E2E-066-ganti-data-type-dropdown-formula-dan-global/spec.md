---
id: TC-FA-CF-E2E-066-ganti-data-type-dropdown-formula-dan-global
title: "Ganti Data Type: Dropdown, Formula, dan Field Global"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-233
  - TC-FA-CF-234
  - TC-FA-CF-235
  - TC-FA-CF-236
coverage:
  web: automated
---

# Ganti Data Type: Dropdown, Formula, dan Field Global

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Voltage Spec` (Text {Generator, Pump} Global `220V` dan `110V`), `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`), `Required Check` (Text General Required No), dan `Total Cost` (Formula `Purchase Price + 10`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Required Check` dan `Total Cost`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-233: Mengganti Data Type ke Dropdown mengharuskan opsi dan mengembalikan Value Type ke Specific

2. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
3. Ganti Data Type menjadi `Dropdown`
4. Verifikasi kontrol Value Type disembunyikan
5. Verifikasi Value Type menjadi Specific
6. Klik `[Save]` tanpa menambah opsi
7. Verifikasi pesan inline `Dropdown options must not be empty` tampil pada Values
8. Verifikasi Save ditolak: modal tetap terbuka
9. Klik icon close `[✕]`
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`

### TC-FA-CF-234: Mengganti Dropdown ke Multi-Dropdown membuang konfigurasi opsi tipe lama

12. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
13. Ganti Data Type menjadi `Multi-Dropdown`
14. Verifikasi section Values kosong tanpa badge `Gold`, `Silver`, `Bronze`
15. Klik `[Save]`
16. Verifikasi pesan inline `Dropdown options must not be empty` tampil
17. Verifikasi Save ditolak: modal tetap terbuka
18. Klik icon close `[✕]`
19. Verifikasi dialog `Unsaved Changes` tampil
20. Klik `[Leave]`

### TC-FA-CF-235: Mengganti Data Type ke Formula mengembalikan Required ke No dan menyembunyikan Value Type

21. Klik row action `⋯` > `Edit` pada baris `Required Check`
22. Ubah toggle Required ke Yes
23. Klik `[Save]`
24. Klik row action `⋯` > `Edit` pada baris `Required Check`
25. Ganti Data Type menjadi `Formula`
26. Verifikasi kontrol Required, Value Type, dan Placeholder disembunyikan
27. Susun token Formula: field `Purchase Price`, operator `+`, konstanta `1`
28. Klik `[Save]`
29. Verifikasi kolom Data Type baris `Required Check` menampilkan `Formula`
30. Verifikasi kolom Value Type baris `Required Check` menampilkan `—`
31. Verifikasi kolom Required baris `Required Check` menampilkan `—`

### TC-FA-CF-236: Mengganti Data Type dari Formula tanpa dialog karena Formula tidak menyimpan nilai

32. Klik row action `⋯` > `Edit` pada baris `Total Cost`
33. Ganti Data Type menjadi `Text`
34. Klik `[Save]`
35. Verifikasi dialog `Change Data Type` tidak tampil
36. Verifikasi kolom Data Type baris `Total Cost` menampilkan `Text`
37. Verifikasi kolom Value Type baris `Total Cost` menampilkan `Specific`
38. Verifikasi kolom Required baris `Total Cost` menampilkan `No`

## Notes

- Urutan TC di spec: 233, 234, 235, 236. Kasus yang ditolak (233, 234) berjalan lebih dulu dan diakhiri tanpa menyimpan; kasus yang menyimpan (235, 236) di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 9 sampai 11 dan 18 sampai 20 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 22 sampai 24 (TC-FA-CF-235 menyimpan Required Yes lebih dulu lalu membuka Edit lagi, sesuai langkah 2 dan 3 TC).
- Spec melewati sekitar 35 langkah (38 langkah). Seluruhnya satu topik (mengganti Data Type pada modal Edit), satu akun, satu dataset Company Nilai; keempat blok memakai field berbeda dan berdiri sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Langkah 4 TC-FA-CF-235 menyebut token `Purchase Price`, `+`, `1` tanpa menyebut cara menyusun token pada Formula Builder; spec menulisnya sebagai satu langkah penyusunan token.
  - Expected TC-FA-CF-233 tidak menyebut apakah form dirty sesudah Save ditolak; spec menutup modal lewat `[✕]` dan `[Leave]`.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
