---
id: TC-AC-ACC-E2E-177-default-user-detail-mengikuti-perubahan-global-settings
title: "Default User di Detail Client Mengikuti Perubahan Global Settings Tanpa Muat Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-238
coverage:
  web: automated
---

# Default User di Detail Client Mengikuti Perubahan Global Settings Tanpa Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| Client Default User PT Uji Tabel Detail (A-DTL-2) | `rini.hartono+{runId}-177@ptujitabeldetail.test` | `Spectra.env.AC_CLIENT_UTD_DU_PASSWORD` |

- Env var `AC_CLIENT_UTD_DU_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`. `AC_TC_PASSWORD` sudah terdaftar.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Client "PT Uji Tabel Detail {runId}-177" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-DTL-1 (Tabel A3) dan Default User Activated Rini Hartono (Email `rini.hartono+{runId}-177@ptujitabeldetail.test`, Division Operations, Position Operations Head); master Division memuat "Operations" dan "Logistics", master Position memuat "Operations Head" dan "Logistics Manager". Hook `after` menghapus Client dan Default User lewat API.
- Kemampuan teknis: sesi API Client Default User (login API password yang tidak dihitung sebagai sesi web, `suite.md`) untuk mengubah Name, Email, Division, dan Position di Global Settings > User; sesi UI Total Control tetap terbuka di Detail. Pelaku kedua hanya memicu perubahan state sehingga memakai sesi API dan tidak butuh butir `P-2`.
- Perubahan tampil tanpa muat ulang: mekanisme propagasi (mis. SSE) tidak disebut TC; asersi menunggu secara otomatis sampai nilai baru tampil (batas tunggu mengikuti konfigurasi runner). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-238: Name, Email, Division, dan Position Default User di Detail mengikuti perubahan di Global Settings tanpa muat ulang

1. Ketik Search `PT Uji Tabel Detail {runId}-177`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail {runId}-177" untuk membuka Detail
3. Amati Section "Default User"
4. Verifikasi Section "Default User" menampilkan Name "Rini Hartono"
5. Verifikasi Section "Default User" menampilkan Email "rini.hartono+{runId}-177@ptujitabeldetail.test"
6. Verifikasi Section "Default User" menampilkan Division "Operations"
7. Verifikasi Section "Default User" menampilkan Position "Operations Head"
8. [Sesi API Client Default User] Di Global Settings > User, ubah Name menjadi `Rina Hartati`, Email menjadi `rina.hartati+{runId}-177@ptujitabeldetail.test`, Division menjadi `Logistics`, dan Position menjadi `Logistics Manager` hingga tersimpan
9. Tunggu aksi selesai, lalu kembali ke sesi Detail tanpa memuat ulang halaman
10. Verifikasi Section "Default User" menampilkan Name "Rina Hartati"
11. Verifikasi Section "Default User" menampilkan Email "rina.hartati+{runId}-177@ptujitabeldetail.test"
12. Verifikasi Section "Default User" menampilkan Division "Logistics"
13. Verifikasi Section "Default User" menampilkan Position "Logistics Manager"

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Tunggu aksi selesai" adalah langkah penghubung (bagian 8b butir 8). Pemulihan Name, Email, Division, dan Position (Post Condition TC-238) dipenuhi hook `after` yang menghapus Client dan Default User milik spec.
- Temuan untuk QA (S-15): TC-238 meminta "sesi lain login sbg Client Default User" dan perubahan di Global Settings > User; spec memakai sesi API untuk pelaku kedua sesuai aturan pelaku kedua yang hanya memicu state (bagian 3 prinsip 13 P-2). TC tidak menyatakan durasi propagasi perubahan ke Detail yang terbuka ataupun mekanisme real-time-nya; PRD/LLD tidak diperiksa oleh spec ini. TC memberi email awal tanpa suffix (`rini.hartono@ptujitabeldetail.test`) sehingga spec memakai email bersuffix (S-12).
