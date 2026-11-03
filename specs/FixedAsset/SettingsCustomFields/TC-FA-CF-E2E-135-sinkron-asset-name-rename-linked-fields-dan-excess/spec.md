---
id: TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess
title: "Sinkron Asset Name: Rename, Linked Custom Fields, Opsi Scope, dan Excess"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-521
  - TC-FA-CF-522
  - TC-FA-CF-523
  - TC-FA-CF-655
  - TC-FA-CF-656
coverage:
  web: automated
---

# Sinkron Asset Name: Rename, Linked Custom Fields, Opsi Scope, dan Excess

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 32): Total Control Company Excess (Pre-setup #29) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Excess; login UI dengan `Spectra.env.FA_TC_EXCESS_PASSWORD` (email tidak tertulis di Pre-setup TC; disediakan tim FE). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Aset konsumen A1 (Asset Name `Pump`, Active) dan A2 (Asset Name `Generator`, Active) (Pre-setup #31). Company Excess (Pre-setup #29): Asset Name `Turbine` berstatus excess, cap Max custom fields per asset name 2, belum ada field ber-Scope `Turbine`.
- Data Dinamis: Asset Name `Boiler Two {runId}-135`; hasil rename Asset Name `Generator` menjadi `Generator Unit {runId}-135`; field `Excess One {runId}-135`, `Excess Two {runId}-135`, dan `Excess Three {runId}-135` (tidak tersimpan).
- State global: rename Asset Name `Generator` dan penambahan `Boiler Two {runId}-135` dipulihkan seed reset Company di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog tab General yang memuat nama `Generator`; entri Changelog lama yang memuat `Generator` disediakan seed reset Company (lihat Temuan untuk QA).
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-523: Tab Linked Custom Fields di Detail Asset Name memuat field yang Scope-nya memuat Asset Name itu

1. Buka Detail Asset Name `Pump` di Settings > Asset Name
2. Klik tab `Linked Custom Fields`
3. Verifikasi tabel memuat `Equipment Class` dan `Storage Capacity`
4. Verifikasi tabel memuat field ber-Scope General
5. Verifikasi nilai Global tampil pada tabel
6. Verifikasi tag `(per-asset)` tampil untuk field Specific

### TC-FA-CF-655: Asset Name baru muncul sebagai opsi pada kontrol Scope tanpa reload

7. Tambah Asset Name `Boiler Two {runId}-135` di Settings > Asset Name
8. Tunggu aksi selesai
9. Kembali ke Settings > Custom Fields lalu klik `[+ Custom Field]`
10. Pilih Scope `Specific Asset Name` dan buka kontrol pemilihan Asset Name
11. Verifikasi opsi `Boiler Two {runId}-135` tersedia dan dapat dipilih pada kontrol Scope tanpa memuat ulang halaman
12. Klik `✕` pada modal Create (form belum diisi, sehingga tanpa dialog `Unsaved Changes`)

### TC-FA-CF-521: Rename Asset Name langsung tercermin di kolom Scope, opsi Filter, dan hasil Search

13. Catat jumlah entri Changelog tab General yang memuat nama `Generator` sebagai baseline
14. Rename Asset Name `Generator` menjadi `Generator Unit {runId}-135` di Settings > Asset Name
15. Tunggu aksi selesai
16. Kembali ke Settings > Custom Fields tab General tanpa reload tambahan
17. Verifikasi kolom Scope baris `Operating Voltage` menampilkan `Generator Unit {runId}-135`
18. Buka Filter dan buka opsi Filter Scope
19. Verifikasi opsi Filter Scope memuat `Generator Unit {runId}-135`
20. Tutup Filter lalu ketik Search `generator unit {runId}-135`, tekan Enter
21. Verifikasi hasil Search menemukan baris `Operating Voltage`
22. Klik `(←)` pada kotak Search
23. Buka Modal Changelog tab General
24. Verifikasi entri log lama tetap memuat nama `Generator` (jumlah entri yang memuat `Generator` sama dengan baseline pada langkah 13)
25. Tutup Modal Changelog
26. Klik row action `⋯` > `Edit` pada baris `Operating Voltage`
27. Verifikasi chip Scope `Operating Voltage` menampilkan `Generator Unit {runId}-135`
28. Buka kontrol pemilihan Asset Name
29. Verifikasi opsi kontrol Scope memuat `Generator Unit {runId}-135`
30. Verifikasi opsi kontrol Scope tidak memuat `Generator`
31. Tutup modal Edit dengan `✕` (form belum diubah, sehingga tanpa dialog `Unsaved Changes`)

### TC-FA-CF-522: Asset Name excess tetap dapat dipilih pada Scope dan tetap dihitung ke cap

32. Ganti akun: logout, lalu login sebagai Total Control Company Excess (Pre-setup #29)
33. Klik `[+ Custom Field]`
34. Pilih Scope `Specific Asset Name` dan buka dropdown Asset Name
35. Verifikasi opsi `Turbine` muncul dan dapat dipilih
36. Pilih `Turbine`, isi Field Name `Excess One {runId}-135` dan Data Type `Text`, lalu klik `[Submit]`
37. Verifikasi toast `Success, custom field has been created.` tampil
38. Tunggu toast lama hilang otomatis
39. Klik `[+ Custom Field]`, isi Field Name `Excess Two {runId}-135` dan Data Type `Text`, pilih Scope `Specific Asset Name` dengan `Turbine`, lalu klik `[Submit]`
40. Verifikasi toast `Success, custom field has been created.` tampil
41. Klik `[+ Custom Field]`, isi Field Name `Excess Three {runId}-135` dan Data Type `Text`, pilih Scope `Specific Asset Name` dengan `Turbine`, lalu klik `[Submit]`
42. Verifikasi dialog blok 🔒 `Limit Reached` dengan teks `You've reached the limit of 2 custom fields for Turbine. Remove an existing field or narrow the scope, or contact support if you need a higher limit.` tampil
43. Klik `[OK]` pada dialog `Limit Reached`
44. Klik icon close `[✕]` pada modal Create
45. Verifikasi dialog `Unsaved Changes` tampil
46. Klik `[Leave]` pada dialog `Unsaved Changes`
47. Verifikasi field `Excess Three {runId}-135` tidak tersimpan (baris `Excess One {runId}-135` dan `Excess Two {runId}-135` tampil pada tabel, baris `Excess Three {runId}-135` tidak ada)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 47 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log; 2 langkah, nomor 23 sampai 24) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 45 langkah. Spec dipertahankan karena semua blok satu topik (sinkron Asset Name ke Custom Fields) dan satu rename dipakai bersama oleh TC-FA-CF-521 dan TC-FA-CF-656.
- Urutan TC di spec: 523, 655, 521 dengan 656 (satu rename `Generator` dipakai bersama karena precondition dan aksi pemicu TC-FA-CF-521 dan TC-FA-CF-656 identik; observasi TC-FA-CF-656 mulai langkah 26), lalu 522 (ganti akun ke Company Excess di akhir).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 (baseline), langkah 8 dan 15 ("Tunggu aksi selesai" sebelum pindah surface; hasil penambahan dan rename Asset Name tidak diasersi langsung), langkah 32 (ganti akun eksplisit), langkah 43, 44, dan 46 (menutup dialog `Limit Reached` lalu form Create yang dirty secara deterministik, S-08; `Verifikasi` dialog `Unsaved Changes` ada di langkah 45), pembukaan Filter dan modal, penutupan modal tanpa perubahan, serta pencarian Search (langkah Search ditulis atomik dengan Enter; R-16).
- Langkah penghubung toast (S-03, R-22): langkah 38 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-521 Expected b mengasumsikan ada entri log lama yang memuat `Generator` di Company Alpha, tetapi Pre-setup #11 sampai #12 tidak mendefinisikan entri Changelog Company Alpha; spec memakai entri lama yang disediakan seed reset Company (kemampuan FE/BE) dan membandingkan jumlahnya dengan baseline.
  - TC-FA-CF-523 Expected tidak menyebut field ber-Scope General dan nilai Global yang dimaksud untuk Asset Name `Pump`; spec mengasersi keberadaan komponen tersebut tanpa nama field konkret kecuali `Equipment Class` dan `Storage Capacity`.
  - TC-FA-CF-522 tidak menyebut cara menutup dialog `Limit Reached`; spec menutupnya dengan `[OK]`, lalu menutup modal Create yang dirty dengan `✕` dan `[Leave]` supaya spec berakhir tanpa form atau dialog terbuka.
  - TC-FA-CF-521 dan TC-FA-CF-656 menyebut rename ke `Generator Unit`; spec memakai nama bersuffix `Generator Unit {runId}-135` (S-12).
  - Email akun Total Control Company Excess tidak tertulis di Pre-setup TC; env var `FA_TC_EXCESS_PASSWORD` disediakan tim FE.
