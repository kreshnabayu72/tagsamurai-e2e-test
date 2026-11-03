---
id: TC-AC-ACC-E2E-178-role-matrix-parent-pengelola-per-viewer
title: "Role Matrix: Section Parent / Pengelola pada Detail Client per Viewer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-1010
  - TC-AC-ACC-1011
  - TC-AC-ACC-1030
  - TC-AC-ACC-1031
coverage:
  web: automated
---

# Role Matrix: Section Parent / Pengelola pada Detail Client per Viewer

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Distributor Total Control (PT Distribusi Nusantara), A-13 | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |
| Partner Total Control (CV Mitra Sejati), A-14 | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` |
| Partner Total Control (CV Mitra Mandiri); akun tidak ada di Tabel Pre-setup TC (lihat Temuan untuk QA) | disediakan tim FE | `Spectra.env.AC_CLIENT_PARTNER_MANDIRI_TC_PASSWORD` |

- Env var `AC_CLIENT_DIST_TC_PASSWORD`, `AC_CLIENT_PARTNER_TC_PASSWORD`, `AC_CLIENT_PARTNER_MANDIRI_TC_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Tabel "Role yang diuji" di atas; blok dijalankan berurutan per akun dengan Step ganti akun eksplisit. Login akun aktor pertama (Distributor Total Control, A-13) di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): "PT Jaringan Ganda Uji" (C-FX16-1; relasi Partner aktif ke CV Mitra Sejati (Anchor), CV Mitra Lestari (Distributor induk PT Distribusi Nusantara), dan CV Mitra Timur (Distributor induk PT Distribusi Timur); Group Cabang Menteng), "PT Mandiri Jaya" (C-ROL-4; Partner aktif hanya CV Mitra Mandiri tanpa Distributor induk, Cabang Bekasi), "PT Mandiri Distributor Timur" (C-FX18-8; relasi Partner aktif ke CV Mitra Mandiri dan relasi Distributor-Client langsung ke PT Distribusi Timur). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### Viewer Distributor Total Control (PT Distribusi Nusantara): TC-AC-ACC-1010

1. Ketik Search `PT Jaringan Ganda Uji`, tekan Enter
2. Klik Company Name "PT Jaringan Ganda Uji" untuk membuka Detail
3. Amati Section "Parent / Pengelola" (field Partner, Distributor, dan Group)
4. Verifikasi field Partner memuat "CV Mitra Sejati" dan "CV Mitra Lestari"
5. Verifikasi field Partner tidak memuat "CV Mitra Timur" dan tidak ada teks pengganti (mis. "Other manager" atau "+1 more")
6. Verifikasi field Distributor tampil dan menampilkan "PT Distribusi Nusantara"
7. Verifikasi teks "PT Distribusi Timur" dan "CV Mitra Timur" tidak muncul di Section "Parent / Pengelola"

### Viewer Partner Total Control (CV Mitra Sejati): TC-AC-ACC-1011

8. Logout dari akun Distributor Total Control
9. Login sebagai Partner Total Control (CV Mitra Sejati)
10. Ketik Search `PT Jaringan Ganda Uji`, tekan Enter
11. Klik Company Name "PT Jaringan Ganda Uji" untuk membuka Detail
12. Amati Section "Parent / Pengelola" (field Partner, Distributor, dan Group)
13. Verifikasi field Partner memuat "CV Mitra Sejati" saja
14. Verifikasi "CV Mitra Lestari" dan "CV Mitra Timur" tidak muncul dan tidak ada teks pengganti (mis. "Other manager" atau "+2 more")
15. Verifikasi field Distributor tampil dan menampilkan "PT Distribusi Nusantara"
16. Verifikasi teks "PT Distribusi Timur" tidak muncul di Section "Parent / Pengelola"

### Viewer Partner Total Control (CV Mitra Mandiri): TC-AC-ACC-1030 dan TC-AC-ACC-1031

17. Logout dari akun Partner Total Control (CV Mitra Sejati)
18. Login sebagai Partner Total Control (CV Mitra Mandiri)
19. Klik sub-tab `Active`, ketik Search `PT Mandiri Jaya`, tekan Enter
20. Klik Company Name "PT Mandiri Jaya" untuk membuka Detail
21. Amati Section "Parent / Pengelola" (field Partner, Distributor, dan Group)
22. Verifikasi field Partner memuat "CV Mitra Mandiri"
23. Verifikasi field Distributor tidak tampil sama sekali: tidak ada label "Distributor" dan tidak ada nilai atau teks pengganti (mis. `—`)
24. Verifikasi tidak ada nama Distributor mana pun di Section "Parent / Pengelola"
25. Kembali ke List lewat breadcrumb Client
26. Klik sub-tab `Active`, ketik Search `PT Mandiri Distributor Timur`, tekan Enter
27. Klik Company Name "PT Mandiri Distributor Timur" untuk membuka Detail
28. Amati Section "Parent / Pengelola" (field Partner, Distributor, dan Group)
29. Verifikasi field Partner memuat "CV Mitra Mandiri"
30. Verifikasi field Distributor tidak tampil sama sekali (PT Distribusi Timur bukan Distributor induk CV Mitra Mandiri), tanpa label, nilai, atau teks pengganti
31. Verifikasi teks "PT Distribusi Timur" tidak muncul di Section "Parent / Pengelola"

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec ditulis per blok role (bukan perulangan identik) karena tiap role membuka Client berbeda dan hasilnya berbeda; ganti akun memakai Step eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3a).
- Anchor absence: Verifikasi field Partner (atau Distributor "PT Distribusi Nusantara") pada Section yang sama mendahului tiap asersi "tidak muncul/tidak tampil" (bagian 8b butir 2).
- Temuan untuk QA (S-11/S-15): akun Partner Total Control CV Mitra Mandiri tidak ada di Tabel Pre-setup TC (Tabel A1/A3 hanya memuat Partner P-ROL-1 "CV Mitra Mandiri" tanpa aktor); email dan password akun ini disediakan tim FE. Post Condition keempat TC `-` sehingga tidak diasersi. TC-1030/1031 tidak menyebut sub-tab asal; spec memakai sub-tab `Active` karena kedua Client Active.
