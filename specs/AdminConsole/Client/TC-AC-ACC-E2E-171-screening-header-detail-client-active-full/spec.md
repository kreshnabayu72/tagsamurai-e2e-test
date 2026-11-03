---
id: TC-AC-ACC-E2E-171-screening-header-detail-client-active-full
title: "Screening Header Detail Client dan Header Tanpa Suspend/Unsuspend (Active-Full)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-233
  - TC-AC-ACC-869
  - TC-AC-ACC-870
coverage:
  web: automated
---

# Screening Header Detail Client dan Header Tanpa Suspend/Unsuspend (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng), A-15 | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` |

- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): Client Active "PT Sejahtera Abadi" (C-01) dan Client Suspended "PT Wahana Nusantara" (C-03). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja; tidak memakai intercept, jam server, atau klien HTTP. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-233: Screening Detail Page Client

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Verifikasi Breadcrumb `Client > Detail`
4. Verifikasi header menampilkan Photo thumbnail, Company Name, badge status entitas `Active`, dan tombol `[Edit]` di pojok kanan atas
5. Verifikasi Client Code tampil sebagai subtitle muted
6. Verifikasi Section Company Information tampil di atas tab dengan grid Company Email | Industry | Website | Fax
7. Verifikasi Section "PIC" menampilkan PIC Name | PIC Email | PIC Phone
8. Verifikasi Section "Address" menampilkan Address | Country | State | City | Postal Code
9. Verifikasi Section "Parent / Pengelola" menampilkan Partner (list nama, read-only) | Distributor (Anchor; `—` untuk Direct) | Group (read-only)
10. Verifikasi Section "Default User" (highlight box) menampilkan Name | Email | Division | Position (`—` jika kosong) dan badge "Activated"/"Not Yet Activated"
11. Verifikasi Section "Settings" menampilkan toggle "Allow Self-Purchased Device Activation"
12. Verifikasi navigasi tab `Subscription (aktif) | TAG | Hardware | Asset Control | Storage`
13. Verifikasi tidak ada footer halaman

### TC-AC-ACC-869: Header Detail Client Active tidak memiliki tombol Suspend maupun Unsuspend

14. Amati header Company Information "PT Sejahtera Abadi" (halaman Detail masih terbuka)
15. Verifikasi badge status entitas `Active` dan tombol `[Edit]` tampil di header
16. Verifikasi header tidak memuat tombol Suspend dan tidak memuat tombol Unsuspend

### TC-AC-ACC-870: Header Detail Client Suspended tidak memiliki tombol Suspend maupun Unsuspend

17. Kembali ke List lewat breadcrumb Client
18. Klik sub-tab `Suspended`
19. Ketik Search `PT Wahana Nusantara`, tekan Enter
20. Klik Company Name "PT Wahana Nusantara" untuk membuka Detail
21. Verifikasi badge status entitas `Suspended` tampil di header
22. Verifikasi header tidak memuat tombol Suspend dan tidak memuat tombol Unsuspend

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Amati header Company Information" (TC-869), "Kembali ke List", dan klik sub-tab `Suspended` adalah langkah penghubung (S-03). TC-869 membuka Detail yang sama dengan TC-233 sehingga tidak membuka ulang Detail (S-10); TC-870 membuka Client Suspended.
- Temuan untuk QA (S-15): TC-233 tidak menyebut sub-tab asal "PT Sejahtera Abadi" dan TC-870 tidak menyebut sub-tab Suspended pada langkahnya; spec memakai sub-tab Active (default) dan sub-tab `Suspended` mengikuti Tabel A2 (C-01 Active, C-03 Suspended). Post Condition TC-233, TC-869, dan TC-870 `-` sehingga tidak diasersi.
