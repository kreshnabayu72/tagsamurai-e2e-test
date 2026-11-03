---
id: TC-AC-ACC-E2E-192-rekonsiliasi-harian-mengoreksi-used-tag
title: "Rekonsiliasi Harian Mengoreksi Used TAG saat Push Perubahan Terlewat"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-816
coverage:
  web: automated
---

# Rekonsiliasi Harian Mengoreksi Used TAG saat Push Perubahan Terlewat

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
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Client "PT Uji Top-up {runId}-192" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-DTL-5 (Tabel A3): TAG Quota RFID 20/5/15 (Total/Used/Available). Hook `after` menyambungkan kembali pengiriman perubahan Used dari FAMS, menghapus TAG uji, lalu menghapus Client lewat API tanpa mengandaikan seed berhasil penuh.
- Kemampuan teknis (kelas d, harness eksternal): memutus dan menyambung kembali pengiriman perubahan Used dari FAMS ke Admin Console untuk tenant uji; memicu job rekonsiliasi harian Admin Console; mendaftarkan satu TAG RFID baru di FAMS tenant uji lewat sesi API Client Default User. Semuanya disediakan tim FE/BE tanpa endpoint karangan (S-13). Pelaku kedua hanya memicu state lewat sesi API sehingga tidak butuh butir `P-2`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-816: Used TAG terkoreksi oleh rekonsiliasi harian saat push perubahan dari produk terlewat

1. Putuskan pengiriman perubahan Used dari FAMS ke Admin Console untuk tenant "PT Uji Top-up {runId}-192"
2. [Sesi API Client Default User] Di FAMS tenant "PT Uji Top-up {runId}-192", daftarkan satu TAG RFID baru hingga tersimpan
3. Tunggu aksi selesai, lalu ketik Search `PT Uji Top-up {runId}-192`, tekan Enter
4. Klik Company Name "PT Uji Top-up {runId}-192" untuk membuka Detail, lalu muat ulang Detail
5. Klik Tab `TAG`, lalu lihat baris RFID pada tabel Quota
6. Verifikasi baris RFID menampilkan Total Quota 20, Used 5, Available 15 (belum berubah)
7. Jalankan rekonsiliasi harian Admin Console
8. Tunggu aksi selesai, lalu muat ulang Detail
9. Klik Tab `TAG`, lalu lihat baris RFID pada tabel Quota
10. Verifikasi baris RFID menampilkan Total Quota 20, Used 6, Available 14

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Putuskan pengiriman", "Jalankan rekonsiliasi", dan "Tunggu aksi selesai" adalah langkah penghubung (S-03, bagian 8b butir 8).
- Temuan untuk QA (S-15): TC-816 menyebut akun sesi kedua `clientDefaultUser_automated_ptUjiTopUp@qwertysystem.net` (A-DTL-1) di tenant Client uji; dengan Client bersuffix akun itu harus dibuat pula bersuffix (disediakan tim FE/BE). TC-816 tidak menyebut cara memutus pengiriman perubahan maupun memicu job rekonsiliasi (di luar aplikasi, alasan Manual Only (c)); keduanya ditulis sebagai kemampuan disediakan tim FE/BE.
