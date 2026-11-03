---
id: TC-AC-ACC-E2E-179-isolasi-tab-subscription-partner-cv-mitra-timur
title: "Isolasi Plan Owner: Tab dan Sub-tab Subscription bagi Partner CV Mitra Timur"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-275
  - TC-AC-ACC-864
  - TC-AC-ACC-865
coverage:
  web: automated
---

# Isolasi Plan Owner: Tab dan Sub-tab Subscription bagi Partner CV Mitra Timur

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Partner Total Control (CV Mitra Timur), A-AST-1 | `totalControlPartnerTimur_automated_cvMitraTimur@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TIMUR_TC_PASSWORD` |

- Env var `AC_CLIENT_PARTNER_TIMUR_TC_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): "PT Relasi Tanpa Plan Owner" (C-ISO-2; Anchor CV Mitra Sejati + CV Mitra Timur; FAMS Active dengan plan owner CV Mitra Sejati), "PT Lintas Jaringan" (C-10; FAMS plan owner CV Mitra Sejati, SAMS dan SIEM plan owner CV Mitra Timur), "PT Lintas SIEM" (C-AST-1; FAMS dan SAMS plan owner CV Mitra Sejati, SIEM plan owner CV Mitra Timur). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-275: Viewer tanpa akses plan owner: Tab Subscription tampil kosong dengan pesan akses

1. Ketik Search `PT Relasi Tanpa Plan Owner`, tekan Enter
2. Klik Company Name "PT Relasi Tanpa Plan Owner" untuk membuka Detail
3. Klik Tab `Subscription`
4. Verifikasi Tab `Subscription` tetap tampil
5. Verifikasi Tab `Subscription` kosong dan menampilkan teks "You don't have access to this client's subscriptions."
6. Klik Tab `TAG`
7. Verifikasi Tab `TAG` dapat dibuka
8. Klik Tab `Hardware`
9. Verifikasi Tab `Hardware` dapat dibuka
10. Klik Tab `Asset Control`
11. Verifikasi Tab `Asset Control` dapat dibuka

### TC-AC-ACC-864: Partner yang hanya memiliki plan owner SAMS dan SIEM: sub-tab FAMS Hidden dan SAMS aktif pertama

12. Kembali ke List lewat breadcrumb Client
13. Ganti isi Search dengan `PT Lintas Jaringan`, tekan Enter
14. Klik Company Name "PT Lintas Jaringan" untuk membuka Detail (FAMS plan owner CV Mitra Sejati; SAMS dan SIEM plan owner CV Mitra Timur)
15. Verifikasi Tab `Subscription` aktif
16. Verifikasi sub-tab yang tampil hanya `SAMS | SIEM`
17. Verifikasi sub-tab `FAMS` Hidden total (bukan read-only) karena plan owner-nya CV Mitra Sejati
18. Verifikasi sub-tab `SAMS` aktif pertama

### TC-AC-ACC-865: Partner yang hanya memiliki plan owner SIEM: sub-tab FAMS dan SAMS Hidden dan SIEM aktif pertama

19. Kembali ke List lewat breadcrumb Client
20. Ganti isi Search dengan `PT Lintas SIEM`, tekan Enter
21. Klik Company Name "PT Lintas SIEM" untuk membuka Detail (FAMS dan SAMS plan owner CV Mitra Sejati; SIEM plan owner CV Mitra Timur)
22. Verifikasi Tab `Subscription` aktif
23. Verifikasi sub-tab yang tampil hanya `SIEM`
24. Verifikasi sub-tab `FAMS` dan `SAMS` Hidden total (bukan read-only)
25. Verifikasi sub-tab `SIEM` aktif pertama

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Absence sub-tab `FAMS`/`SAMS` Hidden didahului Verifikasi sub-tab lain yang tampil pada strip yang sama sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA (S-15): TC-275 memakai tombol Tab TAG/Hardware/Asset Control hanya diuji "dapat dibuka" tanpa isi; Post Condition ketiga TC `-` sehingga tidak diasersi.
