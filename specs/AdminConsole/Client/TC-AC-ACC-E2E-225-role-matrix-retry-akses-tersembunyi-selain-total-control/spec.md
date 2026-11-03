---
id: TC-AC-ACC-E2E-225-role-matrix-retry-akses-tersembunyi-selain-total-control
title: "Role Matrix: Tombol Retry pada Indikator Access Setup Failed Hidden untuk Read Only dan Active-Full"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-993
coverage:
  web: automated
---

# Role Matrix: Tombol Retry pada Indikator Access Setup Failed Hidden untuk Read Only dan Active-Full

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Read Only (Principal), A-02 | `readOnlyPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_RO_PASSWORD` |
| Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng), A-15 | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` |

- Env var `AC_CLIENT_RO_PASSWORD`, `AC_CLIENT_ACTIVE_FULL_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Tabel "Role yang diuji" di atas; blok dijalankan berurutan per akun dengan Step ganti akun eksplisit (akun pertama Read Only login di hook `before`; hook `after` mengembalikan sesi ke akun default suite, Total Control, `AC_TC_PASSWORD`).
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-FX14-4 "PT Akses Gagal Final" (Active; Client Code `FX14-004`; Direct; Group Area Jakarta; FAMS Active; penyediaan akses FAMS berstatus gagal final (seed state); Default User Not Yet Activated). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### Read Only (Principal)

1. Klik sub-tab `Active`, ketik Search `PT Akses Gagal Final`, tekan Enter
2. Klik Company Name "PT Akses Gagal Final" untuk membuka Detail
3. Buka Tab `Subscription` sub-tab `FAMS`, lalu lihat indikator penyediaan akses
4. Verifikasi indikator "Access setup failed" tampil
5. Verifikasi tombol `[Retry]` tidak ada

### Active-Full (Manage active client: C/R/U/D)

6. Logout dari akun Read Only
7. Login sebagai Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng)
8. Klik sub-tab `Active`, ketik Search `PT Akses Gagal Final`, tekan Enter
9. Klik Company Name "PT Akses Gagal Final" untuk membuka Detail
10. Buka Tab `Subscription` sub-tab `FAMS`, lalu lihat indikator penyediaan akses
11. Verifikasi indikator "Access setup failed" tampil
12. Verifikasi tombol `[Retry]` tidak ada

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah dua role identik tetapi ganti akun memakai Step eksplisit; spec ditulis per blok role (bagian 3a). Anchor absence: Verifikasi indikator "Access setup failed" pada surface yang sama mendahului asersi `[Retry]` tidak ada.
- Temuan untuk QA (S-15): judul TC-993 menyebut "Hidden untuk Read Only dan Manage active client (bukan tier Total Control)"; Langkah memakai Active-Full. Post Condition `-`. Tidak ada kombinasi role × aksi lain yang dikarang.
