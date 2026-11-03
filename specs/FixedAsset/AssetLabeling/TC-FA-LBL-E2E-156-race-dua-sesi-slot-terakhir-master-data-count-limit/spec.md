---
id: TC-FA-LBL-E2E-156-race-dua-sesi-slot-terakhir-master-data-count-limit
title: "Race Dua Sesi: Slot Terakhir Master Data Count Limit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-471
coverage:
  web: automated
---

# Race Dua Sesi: Slot Terakhir Master Data Count Limit

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Konteks browser: dua konteks browser (kelas c): sesi 1 = Total Control Company Limit (Pre-setup #11, pengguna `Total Control Limit`), `Fixture.assetLabeling.akun.totalControlLimit`, `Spectra.env.FA_TC_LIMIT_PASSWORD`, login di hook `before` spec ini; sesi 2 = Total Control sesi 2 (Pre-setup #9) pada Company Limit sesuai Pre-setup #11, `Fixture.assetLabeling.akun.totalControlLimitSecond`, `Spectra.env.FA_TC_LIMIT2_PASSWORD`, login di hook `before` spec ini pada konteks browser kedua. Halaman dibuka hook `beforeEach` suite untuk sesi 1 dan hook `before` untuk sesi 2. Konteks kedua ditutup di hook `after`; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_TC_LIMIT_PASSWORD` dan `Spectra.env.FA_TC_LIMIT2_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- State global yang diubah: Master Data Count Limit Company Limit diturunkan ke `Fixture.assetLabeling.batasMinimum` di System Limits dan katalog Company Limit diisi lewat fixture BE sampai tepat satu di bawah batas (satu slot tersisa), di hook `before` (pelaku perubahan System Limits adalah kemampuan tim FE, S-13); hook `after` memulihkan batas dan menghapus seluruh label seed. Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.batasMinimum` | `1000` (Master Data Count Limit terendah yang diizinkan) |
  | `Fixture.assetLabeling.akun.totalControlLimit` | `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #11; `{namaCompany}` = nama Company Limit) |
  | `Fixture.assetLabeling.akun.totalControlLimitSecond` | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Pre-setup #11 dan #9; `{namaCompany}` = nama Company Limit) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): dua konteks browser dengan sinkronisasi pemicu "hampir serentak" (kedua klik dijalankan pada tick yang sama; hasil menang-kalah ditentukan server), sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state.
- Data Dinamis dibuat spec (nama bersuffix `{runId}-156`): `Slot One 471 {runId}-156` (sesi 1) dan `Slot Two 471 {runId}-156` (sesi 2); hanya satu yang tersimpan.
- Cleanup: hook `after` menghapus label hasil aksi spec dan seluruh label seed lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-471: Dua admin merebut slot terakhir Master Data Count Limit

1. Sesi 1: klik `[+ Label]` dan isi Label Name dengan `Slot One 471 {runId}-156`; sesi 2: klik `[+ Label]` dan isi Label Name dengan `Slot Two 471 {runId}-156`
2. Kedua sesi klik `[Submit]` hampir serentak
3. Verifikasi satu sesi menerima toast `Success, label has been created.`
4. Verifikasi sesi lainnya menerima dialog `Label Limit Reached`
5. Verifikasi sesi lainnya tidak menampilkan pesan duplikat `Label name already exists`
6. Verifikasi modal Create Label pada sesi yang kalah tetap terbuka
7. Verifikasi input Label Name pada sesi yang kalah dipertahankan
8. Pada sesi yang kalah: klik `[OK]` pada dialog `Label Limit Reached`
9. Pada sesi yang kalah: klik `✕` pada header modal Create Label
10. Verifikasi dialog Unsaved Changes tampil
11. Pada sesi yang kalah: klik `[Leave]` pada dialog Unsaved Changes
12. Sesi 1: muat ulang tab Labels, lalu ketik Search `471 {runId}-156`, tekan Enter
13. Verifikasi hanya satu label (`Slot One 471 {runId}-156` atau `Slot Two 471 {runId}-156`) tersimpan

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 9 (Edge Case Matrix & Concurrency Sisa) dan section 8. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 12 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 8, 9, 11 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Pemicu state Master Data Count Limit (kuota hampir penuh) pada spec multi-konteks yang objek ujinya race dua sesi tidak dipindah ke kelas e (P-2, 2026-10-13).
- Temuan untuk QA:
  - TC-FA-LBL-471 bertanda Manual Only (d) dua sesi paralel; "hampir serentak" butuh kemampuan sinkronisasi pemicu tim FE (Prerequisites).
  - TC-FA-LBL-471 tidak menyebut sesi mana yang menang; asersi dibuat netral terhadap urutan.
