---
id: TC-AC-DN-E2E-023-guided-tooltip-tombol-bantuan
title: "Guided Tooltip: Tombol [?] di Sebelah Kanan Breadcrumb Memulai Ulang Walkthrough"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-646
coverage:
  web: automated
---

# Guided Tooltip: Tombol [?] di Sebelah Kanan Breadcrumb Memulai Ulang Walkthrough

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16), baca-saja. Tidak ada data Dinamis. Flag `guided_tooltip_seen_ac-settings-device` akun #1 sudah true (disetel hook `before` suite); kemampuan membaca nilai flag disediakan tim FE/BE. Viewport minimal 1280 px dengan Category Sidebar terbuka (state default).

## Test Steps

### TC-AC-DN-646: Tombol [?] di sebelah kanan Breadcrumb memulai ulang walkthrough dari Step 1

1. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb `Settings > Device > Device Name`
2. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
3. Verifikasi tooltip tombol: `Show guide`
4. Klik tombol `[?]`
5. Verifikasi klik `[?]` memulai walkthrough dari Step 1 of 6
6. Verifikasi flag `guided_tooltip_seen_ac-settings-device` tetap true (tidak di-reset oleh replay)
7. Klik `[Skip]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7 menutup walkthrough (langkah TC nomor 4). Asersi flag tetap true ditulis sebelum `[Skip]` karena `[Skip]` sendiri menyetel flag true; setelah `[Skip]` asersi itu tidak lagi membuktikan replay tidak mereset flag (bagian 8b butir 5).
- TC-AC-DN-646 memakai akun Pre-setup #1 (flag sudah true dari hook suite); TC Guided Tooltip lain memakai akun #28 di spec 015, 016, dan 017.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
