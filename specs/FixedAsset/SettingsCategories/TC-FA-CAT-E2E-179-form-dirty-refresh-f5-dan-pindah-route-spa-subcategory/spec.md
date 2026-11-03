---
id: TC-FA-CAT-E2E-179-form-dirty-refresh-f5-dan-pindah-route-spa-subcategory
title: "Form New Subcategory Dirty: Refresh F5 dan Pindah Route SPA"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-618
  - TC-FA-CAT-619
coverage:
  web: automated
---

# Form New Subcategory Dirty: Refresh F5 dan Pindah Route SPA

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); baris `Peripheral` (level 1) dipakai sebagai parent dan hanya dibaca.
- Data milik spec: subkategori `Unload Sub {runId}-179` dibuat oleh TC-FA-CAT-618 lewat UI di bawah `Peripheral`. Hook `after` menghapusnya lewat API. TC-FA-CAT-619 tidak menyimpan kategori.
- Kemampuan teknis: menangani dialog `beforeunload` bawaan browser (mengamati kemunculannya dan membatalkan reload); teks dialog ditentukan browser dan tidak diasersi.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-618: Refresh F5 saat popup New Subcategory dirty memunculkan konfirmasi bawaan browser dan tidak setelah submit sukses

1. Klik elipsis (⋯) pada baris `Peripheral`
2. Klik `+ Add Subcategory`
3. Isi Category Name `Unload Sub {runId}-179`
4. Tekan F5
5. Verifikasi konfirmasi bawaan browser (beforeunload) muncul saat form dirty
6. Batalkan konfirmasi browser
7. Klik `[Submit]`
8. Verifikasi toast `Success, category has been created.` tampil dan popup tertutup
9. Klik elipsis (⋯) pada baris `Peripheral`
10. Klik `+ Add Subcategory`
11. Tekan F5
12. Verifikasi F5 pada form yang bersih berjalan tanpa konfirmasi bawaan browser dan halaman Categories dimuat ulang

### TC-FA-CAT-619: Berpindah route SPA saat popup New Subcategory dirty dicegat dengan dialog Unsaved Changes

13. Klik elipsis (⋯) pada baris `Peripheral`
14. Klik `+ Add Subcategory`
15. Isi Category Name `Route Sub`
16. Klik link menu lain pada sidebar navigasi
17. Verifikasi perpindahan route dicegat dan dialog `You have unsaved changes. Are you sure you want to leave?` tampil
18. Pada dialog klik `[Cancel]`
19. Verifikasi navigasi dibatalkan dan pengguna tetap di form dengan input `Route Sub`
20. Klik link menu lain pada sidebar navigasi lagi
21. Pada dialog klik `[Leave]`
22. Verifikasi navigasi dilanjutkan dan form tertutup tanpa menyimpan
23. Buka Fixed Asset > Settings > Categories

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6 (membatalkan dialog beforeunload bawaan browser; penanganan dialog browser disediakan tim FE) dan langkah 23 (kembali ke halaman Categories sesudah Leave meninggalkannya).
- Nama `Unload Sub` diberi suffix `{runId}-179` karena subkategori tersimpan (S-12); nama `Route Sub` tidak disimpan dan ditulis literal.
- Temuan untuk QA:
  - TC-FA-CAT-618 Expected b menggabungkan dua kondisi (submit sukses dan form bersih) tanpa menyebut toast; spec mengasersi toast sukses sebagai anchor submit (8b butir 2).
  - TC-FA-CAT-619 tidak menyebut menu tujuan "link menu lain"; spec memakai link menu lain yang tersedia di sidebar navigasi.
