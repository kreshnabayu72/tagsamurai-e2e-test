---
id: TC-AC-ACC-E2E-227-retry-akses-gagal-diproses-toast-error
title: "Retry Akses Gagal Diproses: Toast Error, Indikator Tetap Access Setup Failed, dan Tidak Ada Baris Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-1008
coverage:
  web: automated
---

# Retry Akses Gagal Diproses: Toast Error, Indikator Tetap Access Setup Failed, dan Tidak Ada Baris Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-FX14-4 "PT Akses Gagal Final" (Active; Direct; Group Area Jakarta; FAMS Active; penyediaan akses FAMS berstatus gagal final). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Request `[Retry]` dipaksa gagal sehingga fixture tidak berubah.
- Kemampuan teknis (kelas b, fault injection): `Spectra.intercept()` di atas backend nyata untuk memaksa permintaan `[Retry]` dijawab error server (5xx); endpoint tidak disebut TC sehingga disediakan tim FE (S-13). Intercept dilepas segera sesudah pemicu (S-09); hook `after` melepas intercept yang tersisa.

## Test Steps

### TC-AC-ACC-1008: Retry manual penyediaan akses produk gagal diproses

1. Klik sub-tab `Active`, ketik Search `PT Akses Gagal Final`, tekan Enter
2. Klik Company Name "PT Akses Gagal Final", lalu buka Tab `Subscription` sub-tab `FAMS`
3. Verifikasi indikator "Access setup failed" tampil dengan tombol `[Retry]`
4. Aktifkan intercept 5xx pada permintaan `[Retry]`
5. Klik `[Retry]` pada indikator "Access setup failed"
6. Verifikasi toast error "Error, failed to retry access setup."
7. Lepas intercept, lalu muat ulang Tab `Subscription` sub-tab `FAMS`
8. Verifikasi sub-tab `FAMS` tetap menampilkan indikator "Access setup failed" dengan tombol `[Retry]`
9. Verifikasi indikator "Preparing access" tidak tampil
10. Kembali ke List, klik `[Changelog]` di toolbar, ketik Search modal `PT Akses Gagal Final`, tekan Enter
11. Verifikasi Modal Changelog tidak memuat baris Action `Retry Access Setup` untuk "PT Akses Gagal Final"

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Aktifkan intercept" dan "Lepas intercept" adalah pemicu dan pemulihan (S-03, S-09). Mode FE+BE dengan intercept parsial (bagian 6).
- Temuan untuk QA (S-15): TC-1008 Expected butir c (absence baris Changelog) tidak menyebut baris pembanding atau empty state pada hasil Search modal untuk Client ini; asersi absence memakai anchor terbaik yang tersedia di TC (toast error dan indikator pada Detail). Perlu dikonfirmasi QA apakah hasil Search kosong atau memuat baris lain. Post Condition (batalkan simulasi) dipenuhi hook `after`.
