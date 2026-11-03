---
id: TC-AC-ACC-E2E-226-request-retry-akses-langsung-ditolak-server
title: "Request Retry Akses Langsung Ditolak Server: Aktor Non-Total Control dan Aktor di Luar Jaringan Plan Owner"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-1039
coverage:
  web: automated
---

# Request Retry Akses Langsung Ditolak Server: Aktor Non-Total Control dan Aktor di Luar Jaringan Plan Owner

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Read Only (Principal), A-02 | `readOnlyPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_RO_PASSWORD` |
| Distributor Total Control (PT Distribusi Nusantara), A-13 | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |

- Env var `AC_CLIENT_RO_PASSWORD`, `AC_CLIENT_DIST_TC_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Login akun aktor pertama (Read Only, A-02) di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login/logout eksplisit.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-FX18-12 "PT Akses Gagal Plan Owner Principal" (Active; relasi Distributor-langsung PT Distribusi Nusantara tanpa Partner; Group Area Jakarta; FAMS Active plan owner Principal; penyediaan akses FAMS gagal final; riwayat Changelog Client dan Activity Log masing-masing memuat satu baris `Retry Access Setup` oleh Total Control (Principal)). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Request yang ditolak tidak mengubah fixture.
- Kemampuan teknis (kelas a, defense-in-depth): Sesi API aktor dan klien HTTP dari `suite.md` (bagian "Kemampuan teknis yang disediakan tim FE/BE") mengirim request `[Retry]` untuk FAMS Client uji langsung ke server tanpa melalui browser, memakai token sesi API akun yang sedang login (Read Only A-02, lalu A-13); pembacaan state penyediaan akses (jumlah rangkaian pengulangan) lewat Fixture BE disediakan tim FE/BE tanpa endpoint karangan (S-13).

## Test Steps

### TC-AC-ACC-1039: Request [Retry] langsung ditolak server

1. [Read Only] Klik sub-tab `Active`, ketik Search `PT Akses Gagal Plan Owner Principal`, tekan Enter, klik Company Name, dan buka Tab `Subscription` sub-tab `FAMS`
2. Verifikasi indikator "Access setup failed" tampil
3. Verifikasi tombol `[Retry]` tidak ada
4. [Read Only] Kirim request `[Retry]` langsung ke server lewat klien HTTP (tanpa melalui browser) untuk FAMS "PT Akses Gagal Plan Owner Principal"
5. Verifikasi request ditolak server dengan respons 403 Forbidden
6. [Read Only] Muat ulang Tab `Subscription` sub-tab `FAMS`
7. Verifikasi indikator tetap "Access setup failed"
8. Verifikasi indikator "Preparing access" tidak tampil
9. Logout dari akun Read Only, login sebagai Distributor Total Control (PT Distribusi Nusantara) A-13, dan buka Admin Console > Client
10. [A-13] Kirim request `[Retry]` langsung ke server lewat klien HTTP (tanpa melalui browser) untuk FAMS "PT Akses Gagal Plan Owner Principal"
11. Verifikasi request ditolak server dengan respons 404 (netral)
12. Verifikasi tidak ada rangkaian pengulangan baru dimulai (dibaca lewat Fixture BE)

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md` karena TC granular tetap sumber dan tiap TC tepat satu spec; BE mencatatnya pada tingkat endpoint.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Request langsung dikirim lewat klien HTTP; Expected TC hanya berupa status respons (403 untuk non-Total Control, 404 netral untuk di luar jaringan plan owner) dan state data, sehingga perilaku FE (toast) tidak diasersi (bagian 8b butir 1).
- TC menulis A-13 tanpa membuka Detail Client; spec membuka List saja. Post Condition `-`.
