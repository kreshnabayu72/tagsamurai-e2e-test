---
id: TC-FA-CF-E2E-170-ganti-data-type-konfirmasi-field-bernilai-dan-dialog-berurutan
title: "Ganti Data Type: Konfirmasi pada Field Bernilai, Value Global Wajib Diisi Ulang, dan Dialog Berurutan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-225
  - TC-FA-CF-228
  - TC-FA-CF-237
  - TC-FA-CF-238
coverage:
  web: automated
---

# Ganti Data Type: Konfirmasi pada Field Bernilai, Value Global Wajib Diisi Ulang, dan Dialog Berurutan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Rated Power` (Numeric 1 Decimal Place {Generator, Pump}, bernilai `12.5` pada aset A1) dan `Voltage Spec` (Text {Generator, Pump} Global `220V` dan `110V`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Rated Power` beserta nilai A1) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE. `Rated Power` dipulihkan juga di tengah spec (lihat Notes) lewat seed reset field itu.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-225: Mengganti Data Type field bernilai aset menampilkan dialog konfirmasi saat Save

2. Klik row action `⋯` > `Edit` pada baris `Rated Power`
3. Ganti Data Type menjadi `Text`
4. Klik `[Save]`
5. Verifikasi dialog konfirmasi danger berjudul `Change Data Type` dengan bullet `• Rated Power`, teks `Changing the data type will reset all existing values for this field. This action cannot be undone.`, `Are you sure you want to change it?`, serta tombol `[Cancel]` dan `[Change Data Type]` tampil
6. Verifikasi dialog tampil setelah validasi inline lolos dan sebelum data tersimpan: tidak ada pesan inline dan toast `Success, custom field has been updated.` belum tampil

### TC-FA-CF-228: Confirm pada dialog Change Data Type menyimpan Data Type baru dan mereset nilai

7. Klik `[Change Data Type]`
8. Verifikasi toast sukses `Success, custom field has been updated.` tampil
9. Verifikasi modal tertutup
10. Verifikasi kolom Data Type baris `Rated Power` menampilkan `Text`
11. Verifikasi kolom Value Setting baris `Rated Power` menampilkan `—`
12. Klik row action `⋯` > `Edit` pada baris `Rated Power`
13. Verifikasi Decimal Places tidak tampil
14. Verifikasi konfigurasi tipe lama tidak ada
15. Klik icon close `[✕]`

### TC-FA-CF-237: Mengganti Data Type pada field Global mewajibkan Global Value diisi ulang

16. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
17. Ganti Data Type menjadi `Numeric`
18. Verifikasi input Value `Generator` dan `Pump` kosong
19. Klik `[Save]` tanpa mengisi
20. Verifikasi pesan inline `Value must not be empty` tampil pada tiap input
21. Verifikasi Save ditolak: modal tetap terbuka
22. Klik icon close `[✕]`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`

### TC-FA-CF-238: Dialog Change Data Type, Change to Global Value, lalu Change Scope tampil berurutan

25. Pulihkan `Rated Power` ke baseline (Numeric 1 Decimal Place, Scope {Generator, Pump}, nilai `12.5` pada aset A1) lewat seed API
26. Muat ulang halaman (F5)
27. Atur ukuran halaman Pagination menjadi 100
28. Klik row action `⋯` > `Edit` pada baris `Rated Power`
29. Ganti Data Type menjadi `Text`
30. Pilih Value Type `Global` dan isi Value `Generator` dengan `Gen` dan `Pump` dengan `Pmp`
31. Hapus chip `Pump` dari Scope
32. Klik `[Save]`
33. Verifikasi dialog `Change Data Type` tampil pertama
34. Klik `[Change Data Type]`
35. Verifikasi dialog `Change to Global Value` tampil kedua
36. Klik `[Change to Global]`
37. Verifikasi dialog `Change Scope` tampil ketiga
38. Klik `[Change Scope]`
39. Verifikasi toast sukses `Success, custom field has been updated.` tampil setelah ketiga dialog dikonfirmasi

## Notes

- Urutan TC di spec: 225, 228, 237, 238. TC-FA-CF-225 dan 228 berjalan berantai pada modal yang sama: langkah mengganti Data Type ke `Text` dan `[Save]` pada TC-FA-CF-228 identik dengan TC-FA-CF-225, sehingga keduanya memakai dialog yang sudah tampil. TC-FA-CF-238 membutuhkan `Rated Power` bertipe Numeric bernilai, padahal TC-FA-CF-228 telah mengubahnya ke Text; karena itu field dipulihkan lewat seed di antara keduanya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 27 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search; muat ulang pada langkah 26 mengembalikan ukuran halaman ke bawaan), langkah 15 (menutup modal `Rated Power` yang tidak diubah, tanpa dialog), langkah 22 sampai 24 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 25 dan 26 (memulihkan `Rated Power` dan memuat ulang halaman supaya tabel mencerminkan seed).
- Dialog pada langkah 5 dibaca sebagai satu elemen dialog konfirmasi (judul, bullet, teks, pertanyaan, dan tombol disebut utuh; S-01).
- Spec melewati sekitar 35 langkah (39 langkah). Seluruhnya satu topik (konfirmasi pada penggantian Data Type), satu akun, satu dataset Company Nilai; ketiga blok memakai field atau keadaan berbeda dan berdiri sendiri setelah pemulihan seed.
- Kasus Cancel pada dialog `Change Data Type` dan dialog berurutan yang dibatalkan ada di spec 067.
- Temuan untuk QA:
  - Langkah 4 TC-FA-CF-228 tidak menyebut apa yang dimaksud "konfigurasi tipe lama tidak ada" pada Expected c; spec mengasersi bahwa kontrol Decimal Places tidak tampil dan konfigurasi tipe lama tidak ada pada modal Edit.
  - TC-FA-CF-238 tidak menyebut label tombol konfirmasi dialog kedua dan ketiga; spec memakai `[Change to Global]` (dari Expected TC-FA-CF-262) dan `[Change Scope]` (dari TC-FA-CF-269).
  - TC-FA-CF-238 tidak menyebut Value untuk Generator selain pola `Gen`/`Pmp`; spec memakai `Gen` untuk Generator dan `Pmp` untuk Pump.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
