---
id: TC-FA-LBL-E2E-045-edit-simpan-perubahan-nama-warna-dan-keduanya
title: "Edit: Simpan Perubahan Nama, Warna, dan Keduanya"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-137
  - TC-FA-LBL-138
  - TC-FA-LBL-139
coverage:
  web: automated
---

# Edit: Simpan Perubahan Nama, Warna, dan Keduanya

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-045`):
  - `Edit Target 137 {runId}-045` (TC-FA-LBL-137)
  - `Edit Target 138 {runId}-045` (TC-FA-LBL-138)
  - `Edit Target 139 {runId}-045` (TC-FA-LBL-139)
- Data Pre-setup: Palet Preset Color Picker (Pre-setup #33); spec memakai swatch baris 1 kolom 1.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.swatchBaris1Kolom1` | kode swatch baris 1 kolom 1 Palet Preset (Pre-setup #33), dicatat dari kolom Hex |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |

- Kemampuan teknis: mengetik ke kolom Hex, mengklik swatch preset, dan membaca kode Hex sesudahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-137: Edit hanya nama disimpan dan warna tidak berubah

1. Ketik Search `Edit Target 137 {runId}-045`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 137 {runId}-045`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Edit Name Only 137 {runId}-045`
4. Klik `[Save]`
5. Verifikasi toast `Success, label has been updated.`
6. Ganti isi kotak search dengan `Edit Name Only 137 {runId}-045`, tekan Enter
7. Verifikasi baris menampilkan chip `Edit Name Only 137 {runId}-045`
8. Verifikasi Color Hex baris tetap `Fixture.assetLabeling.warnaSeed`
9. Verifikasi Total Asset baris `0`

### TC-FA-LBL-138: Edit hanya warna disimpan dan nama tidak berubah

10. Ganti isi kotak search dengan `Edit Target 138 {runId}-045`, tekan Enter
11. Klik `⋯` pada baris `Edit Target 138 {runId}-045`, lalu klik `Edit`
12. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
13. Klik swatch baris 1 kolom 1, lalu catat kode di kolom Hex sebagai Warna Swatch
14. Klik `[Save]`
15. Verifikasi toast `Success, label has been updated.`
16. Verifikasi kolom Color Hex baris menampilkan Warna Swatch
17. Verifikasi chip baris berlatar Warna Swatch
18. Verifikasi nama baris tetap `Edit Target 138 {runId}-045`

### TC-FA-LBL-139: Edit nama dan warna sekaligus menyimpan keduanya

19. Ganti isi kotak search dengan `Edit Target 139 {runId}-045`, tekan Enter
20. Klik `⋯` pada baris `Edit Target 139 {runId}-045`, lalu klik `Edit`
21. Ganti isi Label Name dengan `Edit Both 139 {runId}-045`
22. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
23. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
24. Klik `[Save]`
25. Verifikasi toast `Success, label has been updated.`
26. Ganti isi kotak search dengan `Edit Both 139 {runId}-045`, tekan Enter
27. Verifikasi baris menampilkan chip `Edit Both 139 {runId}-045` berlatar `Fixture.assetLabeling.hexValid`
28. Verifikasi Color Hex baris menampilkan `Fixture.assetLabeling.hexValid`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 10, 19, 26 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03): pada TC-FA-LBL-137 dan TC-FA-LBL-139 Search diganti ke nama baru agar baris yang tersimpan tampil di tabel yang tersaring.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-137 Post Condition (Modified By dan Last Updated diperbarui ke aktor dan waktu simpan; label lain tidak berubah), TC-FA-LBL-138 Post Condition (Modified By dan Last Updated diperbarui), dan TC-FA-LBL-139 Post Condition ("satu toast") tidak punya langkah observasi di TC dan tidak diasersi.
