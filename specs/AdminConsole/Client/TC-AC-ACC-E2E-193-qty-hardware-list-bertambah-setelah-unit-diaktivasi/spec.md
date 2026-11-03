---
id: TC-AC-ACC-E2E-193-qty-hardware-list-bertambah-setelah-unit-diaktivasi
title: "Qty Hardware List Bertambah setelah Unit Baru Diaktivasi di Global Settings"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-817
coverage:
  web: automated
---

# Qty Hardware List Bertambah setelah Unit Baru Diaktivasi di Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| Client Default User PT Uji Top-up, A-DTL-1 | `clientDefaultUser_automated_ptUjiTopUp@qwertysystem.net` | `Spectra.env.AC_CLIENT_TOPUP_DU_PASSWORD` |

- Env var `AC_CLIENT_TOPUP_DU_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`. `AC_TC_PASSWORD` sudah terdaftar.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Client "PT Uji Top-up {runId}-193" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-DTL-5 (Tabel A3): Hardware List Handheld Reader / RFID / Brand Alfa / HR-200 / SKU-HR-200 / Qty 2. Hook `after` menonaktifkan unit uji dan menghapus Client lewat API tanpa mengandaikan seed berhasil penuh.
- Kemampuan teknis (kelas d, perangkat hardware): aktivasi satu unit Handheld Reader SKU-HR-200 di Global Settings > Hardware tenant uji lewat sesi API Client Default User dan simulator reader yang disediakan tim FE/BE (TC Manual Only (b) perangkat hardware). Pelaku kedua hanya memicu state lewat sesi API sehingga tidak butuh butir `P-2`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-817: Qty Hardware List bertambah setelah unit baru diaktivasi

1. Ketik Search `PT Uji Top-up {runId}-193`, tekan Enter
2. Klik Company Name "PT Uji Top-up {runId}-193" untuk membuka Detail
3. Klik Tab `Hardware`, lalu lihat baris SKU-HR-200 pada Hardware List
4. Verifikasi baris SKU-HR-200 menampilkan Qty 2
5. [Sesi API Client Default User] Di Global Settings > Hardware tenant "PT Uji Top-up {runId}-193", aktivasi satu unit Handheld Reader SKU-HR-200 hingga tersimpan
6. Tunggu aksi selesai, lalu muat ulang Detail
7. Klik Tab `Hardware`, lalu lihat baris SKU-HR-200 pada Hardware List
8. Verifikasi baris SKU-HR-200 menampilkan Qty 3

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Tunggu aksi selesai" adalah langkah penghubung (bagian 8b butir 8). Post Condition TC-817 (nonaktifkan unit uji sehingga Qty kembali 2) dipenuhi hook `after`.
- Temuan untuk QA (S-15): TC-817 menyebut akun sesi kedua `clientDefaultUser_automated_ptUjiTopUp@qwertysystem.net` (A-DTL-1) milik fixture C-DTL-5; dengan Client bersuffix akun itu harus dibuat bersuffix (disediakan tim FE/BE). Cara aktivasi unit Handheld Reader (Sync perangkat) tidak dirinci TC.
