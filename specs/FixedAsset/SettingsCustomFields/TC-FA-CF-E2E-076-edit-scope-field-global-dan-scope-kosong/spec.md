---
id: TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong
title: "Edit Scope: Scope Kosong dan Field Global"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-273
  - TC-FA-CF-274
  - TC-FA-CF-275
  - TC-FA-CF-276
  - TC-FA-CF-277
coverage:
  web: automated
---

# Edit Scope: Scope Kosong dan Field Global

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General; Max custom fields per asset name 20): dipakai `Legacy Tag` (Text, Scope kosong), `Global Only Numeric` (Numeric 0 Decimal Places General Global `5`), dan `Voltage Spec` (Text {Generator, Pump} Global `220V` untuk `Generator` dan `110V` untuk `Pump`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Legacy Tag`, `Global Only Numeric`, `Voltage Spec`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE, termasuk pemulihan `Voltage Spec` di tengah spec (lihat Notes).
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-273: Edit field ber-Scope kosong mewajibkan Scope diisi

2. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
3. Verifikasi Scope kosong tampil pada modal Edit
4. Klik `[Save]` tanpa mengisi Scope
5. Verifikasi pesan inline `Scope must not be empty` tampil
6. Pilih Asset Name `Pump` pada Scope
7. Klik `[Save]`
8. Verifikasi toast sukses `Success, custom field has been updated.` tampil

### TC-FA-CF-277: Pindah Scope General ke Specific pada field Global menyimpan satu nilai wajib per Asset Name

9. Klik row action `⋯` > `Edit` pada baris `Global Only Numeric`
10. Pilih Scope `Specific Asset Name` dengan `Generator` dan `Pump`
11. Verifikasi dua input berlabel `Generator` dan `Pump` muncul
12. Isi Value `Generator` dengan `1` dan `Pump` dengan `2`
13. Klik `[Save]`
14. Klik `[Change Scope]` pada dialog `Change Scope`
15. Klik row action `⋯` > `Edit` pada baris `Global Only Numeric`
16. Verifikasi nilai per Asset Name tersimpan: `Generator` = `1` dan `Pump` = `2`
17. Verifikasi nilai shared dibuang: tidak ada input tunggal berlabel `Value`
18. Klik icon close `[✕]`

### TC-FA-CF-274: Menambah Asset Name pada field Global mewajibkan nilai Global Asset Name baru

19. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
20. Tambahkan chip `Compressor` pada Scope
21. Verifikasi input Value berlabel `Compressor` muncul
22. Klik `[Save]` tanpa mengisi Value `Compressor`
23. Verifikasi pesan inline `Value must not be empty` tampil
24. Verifikasi Save ditolak: modal tetap terbuka

### TC-FA-CF-275: Mengeluarkan Asset Name pada field Global membuang nilai Global Asset Name itu

25. Hapus chip `Compressor` dari Scope
26. Hapus chip `Pump` dari Scope
27. Klik `[Save]`
28. Klik `[Change Scope]` pada dialog `Change Scope`
29. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
30. Verifikasi Scope menjadi `Generator`
31. Verifikasi nilai Global `Pump` dibuang
32. Verifikasi nilai `Generator` tetap `220V`
33. Klik icon close `[✕]`
34. Pulihkan `Voltage Spec` ke baseline (Scope {Generator, Pump} Global `220V` dan `110V`) lewat seed API
35. Muat ulang halaman (F5)
36. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-276: Pindah Scope Specific ke General pada field Global menyimpan satu nilai shared wajib diisi

37. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
38. Pilih Scope `General`
39. Verifikasi input Value tunggal berlabel `Value` menggantikan dua input
40. Isi satu input `Value` dengan `230V`
41. Klik `[Save]`
42. Klik `[Change Scope]` pada dialog `Change Scope`
43. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
44. Verifikasi satu nilai shared `230V` tersimpan
45. Verifikasi nilai per Asset Name dibuang
46. Klik icon close `[✕]`

## Notes

- Urutan TC di spec: 273, 277, 274, 275, 276. TC-FA-CF-274 berakhir dengan form dirty (chip `Compressor` ditambahkan dan Save ditolak); modal yang sama dilanjutkan ke TC-FA-CF-275 dengan langkah penghubung menghapus chip `Compressor` (mengembalikan Scope ke {Generator, Pump}, sama dengan keadaan awal TC-FA-CF-275). TC-FA-CF-275 dan 276 sama-sama mengubah Scope `Voltage Spec`, sehingga field dipulihkan lewat seed di antara keduanya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 36 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search; muat ulang pada langkah 35 mengembalikan ukuran halaman ke bawaan), langkah 14, 28, dan 42 (mengonfirmasi dialog `Change Scope` yang menjadi aksi TC), langkah 18, 33, dan 46 (menutup modal yang tidak diubah sejak disimpan, tanpa dialog), langkah 25 (menghapus chip `Compressor` yang ditambahkan TC-FA-CF-274), langkah 34 dan 35 (memulihkan `Voltage Spec` dan memuat ulang halaman supaya tabel mencerminkan seed).
- Spec melewati sekitar 35 langkah (46 langkah). Seluruhnya satu topik (mengedit Scope pada field Global dan Scope kosong), satu akun, satu dataset Company Nilai; kelima blok memakai field berbeda atau dipulihkan lewat seed sehingga berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-CF-274 tidak menyebut cara menutup modal sesudah Save ditolak; spec melanjutkan ke TC-FA-CF-275 pada modal yang sama setelah menghapus chip `Compressor`.
  - TC-FA-CF-277 tidak menyebut nilai shared lama (`5`) pada Expected; spec mengasersi bahwa tidak ada input tunggal berlabel `Value`.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
