---
id: TC-AC-ACC-E2E-224-retry-akses-dari-tampilan-basi-dua-sesi
title: "Retry Akses dari Tampilan Basi: Server Idempoten, Tidak Ada Rangkaian Kedua dan Tidak Ada Baris Log Baru"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1035
coverage:
  web: automated
---

# Retry Akses dari Tampilan Basi: Server Idempoten, Tidak Ada Rangkaian Kedua dan Tidak Ada Baris Log Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dikonsumsi pada TC, ditiru bersuffix): Client "PT Retry Tampilan Basi {runId}-224" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE; atribut C-FX15-10: Active, Direct, Group Area Jakarta, FAMS Active, penyediaan akses FAMS berstatus gagal final). Hook `after` membatalkan simulasi penyediaan dan menghapus Client lewat API.
- Kemampuan teknis (kelas c, multi-konteks): dua sesi UI Total Control (Principal) bersamaan (Sesi 1 dan Sesi 2, browser/konteks terpisah); simulasi penyediaan instance FAMS tetap berjalan (belum selesai) selama klik `[Retry]` kedua (kelas d, disediakan tim FE/BE tanpa endpoint karangan, S-13).
- Sesi 2 memakai akun yang sama tanpa mengusir Sesi 1 (suite.md > Kemampuan teknis > Dua sesi web akun yang sama).
- Jendela amat: asersi absence toast sesudah klik `[Retry]` didahului langkah "Tunggu 5 detik tanpa memuat ulang halaman" (jendela standar 5 detik adalah pilihan spec, bukan nilai TC atau PRD; bagian 6). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-1035: [Retry] ditekan dari tampilan basi saat rangkaian pengulangan sudah dimulai sesi lain

1. [Sesi 1] Buka Admin Console > Client, ketik Search `PT Retry Tampilan Basi {runId}-224`, tekan Enter, klik Company Name, buka Tab `Subscription` sub-tab `FAMS`, dan jangan muat ulang
2. Verifikasi [Sesi 1] sub-tab `FAMS` menampilkan indikator "Access setup failed" dengan tombol `[Retry]`
3. [Sesi 2] Buka Tab `Subscription` sub-tab `FAMS` Client yang sama lalu klik `[Retry]` pada indikator "Access setup failed"
4. Verifikasi [Sesi 2] toast sukses "Success, access setup retry has been started."
5. Verifikasi [Sesi 2] indikator menjadi "Preparing access"
6. [Sesi 1] Klik `[Retry]` pada indikator "Access setup failed" (tampilan basi)
7. [Sesi 1] Tunggu 5 detik tanpa memuat ulang halaman
8. Verifikasi [Sesi 1] Breadcrumb `Client > Detail` tampil (halaman Detail masih termuat)
9. Verifikasi [Sesi 1] tidak ada toast apa pun (toast T-30 "Success, access setup retry has been started." tidak tampil dan tidak ada toast error)
10. Verifikasi [Sesi 1] tidak ada rangkaian pengulangan kedua dimulai
11. [Sesi 1] Lihat indikator pada halaman Detail
12. Verifikasi [Sesi 1] indikator menjadi "Preparing access" tanpa tombol `[Retry]`
13. [Sesi 1] Kembali ke List, klik `[Changelog]` di toolbar, ketik Search modal `PT Retry Tampilan Basi {runId}-224`, tekan Enter
14. Verifikasi Modal Changelog memuat tepat satu baris Action `Retry Access Setup` untuk Client "PT Retry Tampilan Basi {runId}-224" (klik dari tampilan basi tidak menulis baris log baru)

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah penghubung (S-03, R-16): langkah 11 (lihat indikator di Detail) dan langkah 13 (kembali ke List dan buka modal Changelog).
- Langkah "Tunggu 5 detik" adalah langkah penghubung tanpa Verifikasi (bagian 6 jendela amat). "Tidak ada rangkaian pengulangan kedua" diasersi lewat fixture BE (kemampuan baca disediakan tim FE/BE) dan baris Changelog tunggal.
- Temuan untuk QA (S-15): TC-1035 menyebut "Sesi 1 dan Sesi 2" sebagai dua sesi Total Control; email akun kedua tidak disebut sehingga memakai akun A-01 pada dua konteks browser. TC menyebut Langkah 4 "Lihat indikator" sebelum Changelog; indikator diasersi sebelum modal dibuka. Post Condition TC (seed ulang, batalkan simulasi) dipenuhi hook `after`.
