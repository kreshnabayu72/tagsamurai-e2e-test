---
id: TC-FA-CAT-E2E-022-form-dirty-refresh-f5-dan-pindah-route-spa-category
title: "Form New Category Dirty: Refresh F5 dan Pindah Route SPA"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-72
  - TC-FA-CAT-73
coverage:
  web: automated
---

# Form New Category Dirty: Refresh F5 dan Pindah Route SPA

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); hanya dibaca.
- Data milik spec: kategori `Unload Cat {runId}-022` dibuat oleh TC-FA-CAT-72 lewat UI. Hook `after` menghapusnya lewat API. TC-FA-CAT-73 tidak menyimpan kategori.
- Kemampuan teknis: menangani dialog `beforeunload` bawaan browser (mengamati kemunculannya dan membatalkan reload); teks dialog ditentukan browser dan tidak diasersi.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-72: Refresh F5 saat form dirty memunculkan konfirmasi bawaan browser dan tidak setelah submit sukses

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Unload Cat {runId}-022`
3. Tekan F5
4. Verifikasi konfirmasi bawaan browser (beforeunload) muncul saat form dirty
5. Batalkan konfirmasi browser
6. Klik `[Submit]`
7. Verifikasi toast `Success, category has been created.` tampil dan popup tertutup
8. Klik `[+] Category` pada sidebar
9. Tekan F5
10. Verifikasi F5 pada form yang bersih berjalan tanpa konfirmasi bawaan browser dan halaman Categories dimuat ulang

### TC-FA-CAT-73: Berpindah route SPA saat form dirty dicegat dengan dialog Unsaved Changes

11. Klik `[+] Category` pada sidebar
12. Isi Category Name `Route Cat`
13. Klik link menu lain pada sidebar navigasi
14. Verifikasi perpindahan route dicegat dan dialog `You have unsaved changes. Are you sure you want to leave?` tampil
15. Pada dialog klik `[Cancel]`
16. Verifikasi navigasi dibatalkan dan pengguna tetap di form dengan input `Route Cat`
17. Klik link menu lain pada sidebar navigasi lagi
18. Pada dialog klik `[Leave]`
19. Verifikasi navigasi dilanjutkan dan form tertutup tanpa menyimpan
20. Buka Fixed Asset > Settings > Categories

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5 (membatalkan dialog beforeunload bawaan browser; penanganan dialog browser disediakan tim FE) dan langkah 20 (kembali ke halaman Categories sesudah Leave meninggalkannya; tidak ada TC berikutnya yang bergantung, jadi hanya memulihkan layar untuk hook `after`).
- Nama `Unload Cat` diberi suffix `{runId}-022` karena kategori tersimpan (S-12); nama `Route Cat` tidak disimpan dan ditulis literal.
- Temuan untuk QA:
  - TC-FA-CAT-72 Expected b menggabungkan dua kondisi (submit sukses dan form bersih) tanpa menyebut toast; spec mengasersi toast sukses sebagai anchor submit (8b butir 2).
  - TC-FA-CAT-73 tidak menyebut menu tujuan "link menu lain"; spec memakai link menu lain yang tersedia di sidebar navigasi.
  - TC-FA-CAT-72 langkah 5 ("Buka popup New Category lagi dan tekan F5") tidak mengasersi kondisi akhir halaman; spec mengasersi halaman Categories dimuat ulang tanpa konfirmasi.
