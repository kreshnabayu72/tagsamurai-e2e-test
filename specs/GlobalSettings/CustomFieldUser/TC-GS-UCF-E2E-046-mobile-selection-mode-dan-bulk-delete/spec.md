---
id: TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete
title: "Mobile Android: Selection Mode Long-press, Keluar dari Mode Multi-select, Select All, dan Bulk Delete Custom Field"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-325
  - TC-GS-UCF-436
  - TC-GS-UCF-437
  - TC-GS-UCF-438
  - TC-GS-UCF-439
coverage:
  mobile: automated
---

# Mobile Android: Selection Mode Long-press, Keluar dari Mode Multi-select, Select All, dan Bulk Delete Custom Field

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android dengan gesture long-press (sekitar 500 ms), tap, dan tombol Back perangkat. Spec ini memakai perangkat bersama: `parallel: false` (suite serial).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field di aplikasi Android; blok TC-GS-UCF-439 dan TC-GS-UCF-325 membuka ulang layar itu lewat langkah eksplisit karena state Search sesudah tombol Back (TC-GS-UCF-438) tidak didefinisikan di TC dan Search berganti untuk TC-GS-UCF-325; blok TC-GS-UCF-436, 437, dan 438 berurutan pada satu pembukaan layar dan satu Search `Mobile Exit`.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` pada aplikasi Android. Password tidak ditulis di spec atau fixture.
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; fixture baru `Fixture.customFieldUser.mobileSelection046`; seluruhnya Text, Active, bebas nilai User):
  - `Mobile Exit A {runId}-046` dan `Mobile Exit B {runId}-046` (TC-GS-UCF-436, 437, 438, 439); tetap ada.
  - `Mobile A {runId}-046` dan `Mobile B {runId}-046` (TC-GS-UCF-325); dihapus oleh spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-046` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`); pada aplikasi Android mekanisme penyetelan flag disediakan tim FE/BE.
- Environment variable: `GS_TC_PASSWORD`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-UCF-436: Tombol [✕] pada bulk bar membatalkan seleksi dan keluar dari mode multi-select

1. Klik `[🔍]`, ketik `Mobile Exit`, tekan Enter
2. Long-press kartu `Mobile Exit A {runId}-046`
3. Tap kartu `Mobile Exit B {runId}-046`
4. Verifikasi counter `2 Selected`
5. Klik `[✕]` pada floating bulk bar
6. Verifikasi floating bulk bar hilang
7. Verifikasi checkbox seluruh kartu disembunyikan
8. Verifikasi tidak ada kartu terpilih
9. Verifikasi kartu `Mobile Exit A {runId}-046` dan `Mobile Exit B {runId}-046` tetap ada

### TC-GS-UCF-437: Menghapus centang seluruh kartu hingga 0 Selected keluar dari mode multi-select

10. Long-press kartu `Mobile Exit A {runId}-046`
11. Verifikasi counter `1 Selected`
12. Tap kartu `Mobile Exit A {runId}-046` sekali lagi
13. Verifikasi floating bulk bar hilang
14. Verifikasi checkbox seluruh kartu disembunyikan

### TC-GS-UCF-438: Tombol Back perangkat Android keluar dari mode multi-select

15. Long-press kartu `Mobile Exit A {runId}-046`
16. Verifikasi counter `1 Selected`
17. Tekan tombol Back perangkat Android
18. Verifikasi floating bulk bar hilang
19. Verifikasi checkbox seluruh kartu disembunyikan
20. Verifikasi layar tetap berada di daftar Custom Field

### TC-GS-UCF-439: [Select All] memilih seluruh kartu yang dimuat pada daftar

21. Buka Global Settings > User > Custom Field
22. Klik `[🔍]`, ketik `Mobile Exit`, tekan Enter
23. Verifikasi daftar memuat kartu `Mobile Exit A {runId}-046` dan `Mobile Exit B {runId}-046`
24. Long-press kartu `Mobile Exit A {runId}-046`
25. Verifikasi counter `1 Selected`
26. Klik `[Select All]`
27. Verifikasi counter `2 Selected`
28. Verifikasi kedua kartu terpilih
29. Klik `[✕]` pada floating bulk bar

### TC-GS-UCF-325: Long-press kartu masuk selection mode untuk Bulk Delete

30. Buka Global Settings > User > Custom Field
31. Klik `[🔍]`, ketik `{runId}-046`, tekan Enter
32. Verifikasi kartu `Mobile A {runId}-046` dan `Mobile B {runId}-046` tanpa checkbox
33. Long-press kartu `Mobile A {runId}-046` (sekitar 500 ms)
34. Verifikasi kartu `Mobile A {runId}-046` terpilih (`[✓]`)
35. Verifikasi checkbox kosong `[ ]` muncul pada kartu lain
36. Tap kartu `Mobile B {runId}-046`
37. Verifikasi floating bulk bar menampilkan `[✕]`, counter `2 Selected`, `[Select All]`, dan aksi `Delete`
38. Pilih aksi `Delete` di floating bulk bar
39. Verifikasi dialog `Delete Custom Fields` menampilkan 2 bullet: `Mobile A {runId}-046` dan `Mobile B {runId}-046`
40. Klik `[Delete]`
41. Verifikasi muncul toast sukses: "Success, custom field has been deleted."

## Notes

- Mode: FE+BE (mobile). Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (41 langkah) tanpa kelas harness lain: seluruhnya satu surface (daftar card Custom Field di Android) dengan satu perangkat dan satu akun. Blok TC-GS-UCF-436, 437, dan 438 berurutan pada satu Search `Mobile Exit` (seleksi dibersihkan lewat `[✕]`, hapus centang, dan tombol Back) tanpa pembukaan ulang layar; blok TC-GS-UCF-439 dan TC-GS-UCF-325 dimulai dari layar yang dibuka ulang (langkah 21 dan 30) karena state Search sesudah tombol Back tidak didefinisikan (TC-GS-UCF-438) dan Search berganti untuk TC-GS-UCF-325. Blok memakai field Mobile Exit yang tidak dihapus, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Urutan TC dalam spec: 436, 437, 438, 439 (tanpa mutasi), lalu 325 (menghapus `Mobile A` dan `Mobile B`, paling akhir; prinsip 5). Urutan menyimpang dari urutan TC sumber (325, 436, 437, 438, 439).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 22, 31 (Search agar kartu target tampil), langkah 21 dan 30 (membuka ulang layar Custom Field karena state Search berubah atau tidak terdefinisi, S-09; TC-GS-UCF-436 memakai layar awal hook `beforeEach`), dan langkah 29 (membatalkan seleksi sebelum TC berikutnya).
- Asersi tambahan di luar Expected TC (S-03): langkah 23 mengikuti Expected TC-GS-UCF-439 butir a (daftar memuat kedua kartu); langkah 9 mengikuti TC-GS-UCF-436 butir b ("tetap ada").
- Temuan untuk QA:
  - TC-GS-UCF-325 tidak memuat Search pada langkah 1 sampai 2 padahal kartu `Mobile A` dan `Mobile B` harus tampil bersama banyak kartu lain; spec mencari dengan Search `{runId}-046` (mencakup juga kartu `Mobile Exit A` dan `Mobile Exit B` milik spec yang sama, sehingga bullet dialog hanya memuat kartu yang dipilih).
  - TC-GS-UCF-325 butir c menyebut counter `2 Selected` pada floating bulk bar sedangkan butir b (sesudah long-press) hanya satu kartu terpilih; spec mengasersi bar lengkap sesudah tap kartu kedua (langkah 41).
  - TC-GS-UCF-436 sampai 439 memakai `Mobile Exit A` dan `B` (D-176, D-177) tanpa suffix; spec memakai versi bersuffix `{runId}-046`.
  - TC-GS-UCF-325 dan 436 sampai 439 tidak menyebut langkah login pada aplikasi Android (login di hook `before`) dan tidak mendefinisikan keadaan Search sesudah menekan Back (TC-GS-UCF-438); spec membuka ulang layar di awal tiap blok.
