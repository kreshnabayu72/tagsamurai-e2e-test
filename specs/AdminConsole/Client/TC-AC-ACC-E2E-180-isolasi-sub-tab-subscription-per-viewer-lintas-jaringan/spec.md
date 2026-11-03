---
id: TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan
title: "Isolasi Plan Owner: Sub-tab Subscription, Changelog, dan Empty State per Viewer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-276
  - TC-AC-ACC-277
  - TC-AC-ACC-989
  - TC-AC-ACC-278
  - TC-AC-ACC-279
  - TC-AC-ACC-990
coverage:
  web: automated
---

# Isolasi Plan Owner: Sub-tab Subscription, Changelog, dan Empty State per Viewer

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| Distributor Total Control (PT Distribusi Nusantara), A-13 | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |
| Partner Total Control (CV Mitra Sejati), A-14 | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` |

- Env var `AC_CLIENT_DIST_TC_PASSWORD`, `AC_CLIENT_PARTNER_TC_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`. `AC_TC_PASSWORD` sudah terdaftar.
- Tabel "Role yang diuji" di atas; blok dijalankan berurutan per akun dengan Step ganti akun eksplisit. Login akun aktor pertama (Total Control, A-01) di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): "PT Lintas Jaringan" (C-10; FAMS plan owner CV Mitra Sejati, SAMS dan SIEM plan owner CV Mitra Timur), "PT Urut Managed Alfa" (C-FX13-2; relasi Distributor-langsung PT Distribusi Nusantara, tanpa subscription), "PT Urut Managed Beta" (C-FX13-3; Partner CV Mitra Sejati saja, tanpa subscription). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data. Baris Changelog Subscription "PT Lintas Jaringan" untuk produk di luar akses Partner CV Mitra Sejati dipakai sebagai precondition TC-279 dan dibaca (tidak ditulis); TC tidak menyebut seed-nya (lihat Temuan untuk QA).

## Test Steps

### Total Control (Principal): TC-AC-ACC-276

1. Ketik Search `PT Lintas Jaringan`, tekan Enter
2. Klik Company Name "PT Lintas Jaringan" untuk membuka Detail
3. Klik Tab `Subscription`
4. Verifikasi sub-tab `FAMS`, `SAMS`, dan `SIEM` semua tampil

### Distributor Total Control (PT Distribusi Nusantara): TC-AC-ACC-277 dan TC-AC-ACC-989

5. Logout dari akun Total Control (Principal)
6. Login sebagai Distributor Total Control (PT Distribusi Nusantara)
7. Ketik Search `PT Lintas Jaringan`, tekan Enter
8. Klik Company Name "PT Lintas Jaringan" untuk membuka Detail
9. Klik Tab `Subscription`
10. Verifikasi hanya sub-tab `FAMS` yang tampil
11. Verifikasi sub-tab `SAMS` dan `SIEM` Hidden total (bukan read-only)
12. Kembali ke List lewat breadcrumb Client
13. Klik sub-tab `Active`, ketik Search `PT Urut Managed Alfa`, tekan Enter
14. Klik Company Name "PT Urut Managed Alfa" untuk membuka Detail
15. Klik Tab `Subscription`
16. Verifikasi Tab `Subscription` menampilkan ilustrasi (package) dengan Title "No subscriptions yet" dan Description "Active and pending subscriptions for this client will appear here."
17. Verifikasi teks "You don't have access to this client's subscriptions." tidak tampil

### Partner Total Control (CV Mitra Sejati): TC-AC-ACC-278, TC-AC-ACC-279, dan TC-AC-ACC-990

18. Logout dari akun Distributor Total Control
19. Login sebagai Partner Total Control (CV Mitra Sejati)
20. Ketik Search `PT Lintas Jaringan`, tekan Enter
21. Klik Company Name "PT Lintas Jaringan" untuk membuka Detail
22. Klik Tab `Subscription`
23. Verifikasi hanya sub-tab `FAMS` yang tampil (plan owner CV Mitra Sejati)
24. Verifikasi sub-tab milik plan owner Partner lain (`SAMS` dan `SIEM`) Hidden
25. Klik `[Changelog]` pada toolbar Tab `Subscription`
26. Verifikasi modal Changelog Subscription hanya memuat riwayat subscription yang boleh dilihat viewer
27. Tutup modal Changelog lewat `[✕]`
28. Kembali ke List lewat breadcrumb Client
29. Ganti isi Search dengan `PT Lintas Jaringan`, tekan Enter
30. Verifikasi baris "PT Lintas Jaringan" tampil pada List
31. Verifikasi kolom SAMS dan SIEM baris "PT Lintas Jaringan" menampilkan `—` (kolom produk di luar akses)
32. Klik sub-tab `Active`, ganti isi Search dengan `PT Urut Managed Beta`, tekan Enter
33. Klik Company Name "PT Urut Managed Beta" untuk membuka Detail
34. Klik Tab `Subscription`
35. Verifikasi Tab `Subscription` menampilkan ilustrasi (package) dengan Title "No subscriptions yet" dan Description "Active and pending subscriptions for this client will appear here."
36. Verifikasi teks "You don't have access to this client's subscriptions." tidak tampil

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu role pada satu surface, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna. Ganti akun memakai Step eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3 pemisah nyata (b)).
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Tutup modal Changelog", "Kembali ke List", dan Search adalah langkah penghubung (S-03).
- Temuan untuk QA (S-15): TC-279 Expected "Hanya riwayat subscription yang boleh dilihat viewer" tidak menyebut baris Changelog spesifik dan tidak ada seed Changelog Subscription produk lain pada fixture C-10; spec tidak mengasersi isi baris selain pernyataan Expected. Langkah Changelog TC-279 tidak menyebut Detail asal; spec memakai Detail "PT Lintas Jaringan". Post Condition seluruh TC `-`.
