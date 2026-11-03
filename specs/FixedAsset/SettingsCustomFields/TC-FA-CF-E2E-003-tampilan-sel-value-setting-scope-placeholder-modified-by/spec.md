---
id: TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by
title: "Tampilan Sel Kolom Value Setting, Scope, Placeholder, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-6
  - TC-FA-CF-7
  - TC-FA-CF-8
  - TC-FA-CF-9
  - TC-FA-CF-11
coverage:
  web: automated
---

# Tampilan Sel Kolom Value Setting, Scope, Placeholder, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12) dan tab Purchasing (Pre-setup #13, field `Rated Precision` Numeric 1 Decimal Place), dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` dan `Fixture.faCustomFields.baselinePurchasing`. Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-6: Value Setting Decimal Places tunggal, jamak, dan strip (baris tab General)

1. Verifikasi kolom Value Setting baris `Storage Capacity` menampilkan `0 Decimal Places`
2. Verifikasi kolom Value Setting baris `Depreciated Ratio` menampilkan `2 Decimal Places`
3. Verifikasi kolom Value Setting baris `Asset Serial Tag` menampilkan `—`

### TC-FA-CF-7: Value Setting Dropdown menampilkan dua badge lalu chip +N more

4. Verifikasi sel Value Setting baris `Equipment Class` menampilkan badge `Class A`, badge `Class B`, dan chip `+1 more`
5. Verifikasi opsi ketiga `Class C` tidak tampil sebagai badge pada sel Value Setting baris `Equipment Class`

### TC-FA-CF-8: Scope menampilkan badge General, nama Asset Name urut abjad, +N more, dan strip

6. Verifikasi kolom Scope baris `Asset Serial Tag` menampilkan badge `General`
7. Verifikasi kolom Scope baris `Storage Capacity` menampilkan badge `Generator` dan badge `Pump`
8. Verifikasi kolom Scope baris `Equipment Class` menampilkan badge `Compressor`, badge `Generator`, dan chip `+1 more`
9. Verifikasi kolom Scope baris `Legacy Tag` menampilkan `—`

### TC-FA-CF-9: Placeholder menampilkan nilai efektif

10. Verifikasi kolom Placeholder baris `Storage Capacity` menampilkan `Capacity in GB`
11. Verifikasi kolom Placeholder baris `Compliance File` menampilkan `Upload document`
12. Verifikasi kolom Placeholder baris `Total Cost` menampilkan `—`

### TC-FA-CF-11: Modified By menampilkan First Name dan inisial Last Name dengan tooltip nama lengkap

13. Verifikasi sel Modified By baris `Asset Serial Tag` menampilkan `Budi S` sebagai teks polos (bukan badge)
14. Arahkan kursor ke teks Modified By baris `Asset Serial Tag`
15. Verifikasi tooltip hover menampilkan `Budi Santoso`

### TC-FA-CF-6 (lanjutan): Value Setting 1 Decimal Place pada tab Purchasing

16. Klik tab `Purchasing`
17. Verifikasi kolom Value Setting baris `Rated Precision` menampilkan `1 Decimal Place`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 6 (tiga baris tab General), 7, 8, 9, 11, lalu 6 d (tab Purchasing). Expected d TC-FA-CF-6 (langkah 16 dan 17) ditempatkan di akhir supaya spec tidak berpindah tab sebelum TC lain yang bekerja di tab General selesai (S-10) dan tidak perlu langkah kembali ke tab General.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 (hover untuk mengamati tooltip Expected b TC-FA-CF-11) dan langkah 16 (pindah tab sesuai langkah 3 TC-FA-CF-6).
- Langkah 5 adalah klausa kedua Expected TC-FA-CF-7 dan beranchor langkah 4 (sel yang sama sudah diverifikasi tampil).
- Modified By pada langkah 13 diasersi berformat `[First Name] [Last Initial]` (R-14).
