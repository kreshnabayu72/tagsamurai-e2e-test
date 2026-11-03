---
id: TC-FA-LBL-E2E-027-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-2
title: "Validasi Label Name Create: Kosong, Spasi, Panjang, Emoji, dan Trim (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-72
  - TC-FA-LBL-74
  - TC-FA-LBL-75
  - TC-FA-LBL-82
coverage:
  web: automated
---

# Validasi Label Name Create: Kosong, Spasi, Panjang, Emoji, dan Trim (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Suffix nama bersuffix spec ini: `{runId}-027` (`{runId}` hanya digit).
- Nama120: kata `Alpha` dipisah spasi tunggal dan ditutup akhiran unik per run `{runId}-027` (suffix spec ini; Data Uji TC-FA-LBL-72 dan 74 menulis akhiran `{runId}-72` dan `{runId}-74`), disusun supaya total tepat 120 karakter termasuk akhiran (nilai dihitung di script).
- Label yang dibuat: `Nama120`; `Trim Test 75 {runId}-027` (diketik dengan dua spasi di awal dan di akhir); `R&D / Lab #82 (Main), "Core" {runId}-027`.
- Label yang dibuat spec ini (nama bersuffix `{runId}-027`) dihapus di hook `after` lewat sesi API aktor.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog dan menghapus label.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-74: Spasi tepi tidak dihitung terhadap batas 120 karakter

2. Ketik Nama120 diikuti 5 spasi di akhir di Label Name
3. Verifikasi `[Submit]` berstatus enabled
4. Verifikasi tidak ada inline error `Max. 120 characters` karena panjang setelah trim tetap 120

### TC-FA-LBL-72: Label Name tepat 120 karakter diterima

5. Ganti isi Label Name dengan Nama120 tanpa spasi tepi
6. Verifikasi tidak ada inline error `Max. 120 characters`
7. Klik `[Submit]`
8. Verifikasi toast `Success, label has been created.`
9. Ketik Search `Nama120`, tekan Enter
10. Verifikasi baris chip label dengan nama 120 karakter penuh tampil di Labels List
11. Klik `(←)` pada kotak Search

### TC-FA-LBL-75: Spasi awal dan akhir Label Name dibuang saat disimpan

12. Klik `[+ Label]`
13. Ketik `  Trim Test 75 {runId}-027  ` (dua spasi di awal dan dua spasi di akhir) di Label Name
14. Klik `[Submit]`
15. Verifikasi toast `Success, label has been created.`
16. Ketik Search `Trim Test 75 {runId}-027`, tekan Enter
17. Verifikasi baris di tabel menampilkan chip `Trim Test 75 {runId}-027` tanpa spasi tepi
18. Verifikasi spasi di tengah nama dipertahankan pada chip `Trim Test 75 {runId}-027`
19. Klik `(←)` pada kotak Search

### TC-FA-LBL-82: Karakter cetak non-emoji diizinkan di Label Name

20. Klik `[+ Label]`
21. Isi Label Name `R&D / Lab #82 (Main), "Core" {runId}-027`
22. Verifikasi tidak ada inline error
23. Klik `[Submit]`
24. Verifikasi toast `Success, label has been created.`
25. Ketik Search `R&D / Lab #82 (Main), "Core" {runId}-027`, tekan Enter
26. Verifikasi chip menampilkan teks persis `R&D / Lab #82 (Main), "Core" {runId}-027`
27. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 74, 72, 75, 82. TC-FA-LBL-74 (tanpa submit) ditaruh sebelum TC-FA-LBL-72 supaya modal yang sama dipakai bersama dan submit sukses berada sesudah kasus yang tidak menyimpan (S-10).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 9, 16, dan 25 (Search untuk menemukan baris target, R-16) serta langkah 11, 19, dan 27 (mengosongkan Search).
- Nama yang disimpan memakai suffix `{runId}-027` (S-12). Pada TC-FA-LBL-72 dan TC-FA-LBL-74, panjang nama dihitung termasuk suffix sehingga total tepat 120 karakter, sesuai Data Uji TC; akhiran unik TC (`{runId}-72`, `{runId}-74`) diseragamkan menjadi suffix spec `{runId}-027` karena TC-FA-LBL-74 dan 72 memakai satu nama Nama120.
- Temuan untuk QA:
  - TC-FA-LBL-75 Data Uji menulis `Trim Test 75` tanpa suffix per run; spec menambahkan suffix `{runId}-027` pada nama yang disimpan.
