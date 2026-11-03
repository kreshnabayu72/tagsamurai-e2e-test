---
id: TC-AC-ACHA-E2E-002-list-empty-state-belum-ada-transaksi
title: "Empty State List Saat Entitas Belum Memiliki Transaksi Alokasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-6
coverage:
  web: automated
---

# Empty State List Saat Entitas Belum Memiliki Transaksi Alokasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Partner CV Karya Mandiri (Pre-setup #46) `totalControlPartner2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_P2_PASSWORD`.
- Login akun aktor di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`).
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Kondisi data (spec kondisi data sendiri, prinsip 12): tidak ada transaksi alokasi dalam scope baca CV Karya Mandiri (tidak ada transaksi yang dikirim CV Karya Mandiri dan tidak ada yang ditujukan ke Client terafiliasi langsung PT Cipta Kreasi). Fixture baseline (disediakan tim FE/BE) memastikan kondisi ini sebelum spec dijalankan, termasuk menyingkirkan transaksi seed Pre-setup #50 dan #70 milik MB_P2 dari scope CV Karya Mandiri, lalu memulihkannya di hook `after`. Seed Pre-setup #48 tidak memuat transaksi pengirim CV Karya Mandiri.
- State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_P2_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-6: Empty state saat belum ada transaksi alokasi sama sekali

1. Amati tabel pada halaman Allocation > Device Allocation (halaman dibuka hook `beforeEach`)
2. Verifikasi Table Tools `[+ Allocation]` tampil
3. Verifikasi tabel menampilkan empty state dengan ilustrasi, judul "No device allocations yet", dan deskripsi "Create your first device allocation to start distributing hardware to clients."
4. Verifikasi tidak ada tombol di dalam empty state (tombol `[+ Allocation]` hanya ada di Table Tools)
5. Verifikasi tidak ada teks "No results found"
6. Verifikasi tidak ada teks "Unable to load this data."

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec kondisi data (prinsip 12): satu TC, entitas tanpa transaksi.
- Anchor absence (bagian 8b butir 2): langkah 2 membuktikan halaman termuat (Table Tools tampil) sebelum asersi tombol, "No results found", dan "Unable to load this data." yang tidak ada.
- Pembagian TC lintas spec: empty state Filtered (TC-7, TC-9) ada di spec 037; error load (TC-8) di spec 058.
- Temuan untuk QA:
  - TC-6 Precondition c ("belum ada transaksi alokasi dalam scope CV Karya Mandiri") bertabrakan dengan Pre-setup #50 dan #70 yang dibuat MB_P2 (CV Karya Mandiri) dan dipakai TC lain; spec mengandalkan fixture baseline yang menyingkirkan transaksi itu untuk spec ini (kontrak fixture tidak tertulis di TC, PRD, atau LLD; disediakan tim FE/BE).
