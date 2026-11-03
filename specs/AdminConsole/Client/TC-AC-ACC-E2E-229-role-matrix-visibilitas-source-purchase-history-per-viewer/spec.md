---
id: TC-AC-ACC-E2E-229-role-matrix-visibilitas-source-purchase-history-per-viewer
title: "Role Matrix: Source pada Purchase History TAG, Hardware, dan Storage per Viewer Partner dan Distributor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-1014
  - TC-AC-ACC-1015
coverage:
  web: automated
---

# Role Matrix: Source pada Purchase History TAG, Hardware, dan Storage per Viewer Partner dan Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Partner Total Control (CV Mitra Sejati), A-14 | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` |
| Distributor Total Control (PT Distribusi Nusantara), A-13 | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |

- Env var `AC_CLIENT_PARTNER_TC_PASSWORD`, `AC_CLIENT_DIST_TC_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Tabel "Role yang diuji" di atas; blok dijalankan berurutan per akun dengan Step ganti akun eksplisit. Login akun aktor pertama (Partner Total Control CV Mitra Sejati, A-14) di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-FX16-1 "PT Jaringan Ganda Uji" (Active; Client Code `FX16-001`; relasi Partner aktif ke CV Mitra Sejati (Anchor), CV Mitra Lestari (Distributor induk PT Distribusi Nusantara), dan CV Mitra Timur (Distributor induk PT Distribusi Timur); Group Cabang Menteng; Default User Activated). Riwayat Purchase History TAG, Hardware, dan Storage FX16: tiap tabel empat baris dengan Source `CV Mitra Sejati`, `CV Mitra Lestari`, `CV Mitra Timur`, dan `TAG Samurai` (Source Principal), satu baris per Source. Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### Partner Total Control (CV Mitra Sejati): TC-AC-ACC-1014

1. Klik sub-tab `Active`, ketik Search `PT Jaringan Ganda Uji`, tekan Enter
2. Klik Company Name "PT Jaringan Ganda Uji" untuk membuka Detail
3. Klik Tab `TAG`, lihat tabel Purchase History TAG, lalu buka Filter Source
4. Verifikasi tabel Purchase History TAG memuat 2 baris dengan Source "CV Mitra Sejati", "TAG Samurai" (Source Principal tetap tampil)
5. Verifikasi baris Source "CV Mitra Lestari" dan "CV Mitra Timur" tidak tampil pada tabel Purchase History TAG
6. Verifikasi opsi Filter Source pada tabel Purchase History TAG hanya memuat "CV Mitra Sejati", "TAG Samurai"
7. Verifikasi tidak ada baris placeholder atau teks "Other manager" pada tabel Purchase History TAG
8. Klik ulang icon Filter untuk menutup panel Filter
9. Klik Tab `Hardware`, lihat tabel Purchase History Hardware, lalu buka Filter Source
10. Verifikasi tabel Purchase History Hardware memuat 2 baris dengan Source "CV Mitra Sejati", "TAG Samurai" (Source Principal tetap tampil)
11. Verifikasi baris Source "CV Mitra Lestari" dan "CV Mitra Timur" tidak tampil pada tabel Purchase History Hardware
12. Verifikasi opsi Filter Source pada tabel Purchase History Hardware hanya memuat "CV Mitra Sejati", "TAG Samurai"
13. Verifikasi tidak ada baris placeholder atau teks "Other manager" pada tabel Purchase History Hardware
14. Klik ulang icon Filter untuk menutup panel Filter
15. Klik Tab `Storage`, lihat tabel Purchase History Storage, lalu buka Filter Source
16. Verifikasi tabel Purchase History Storage memuat 2 baris dengan Source "CV Mitra Sejati", "TAG Samurai" (Source Principal tetap tampil)
17. Verifikasi baris Source "CV Mitra Lestari" dan "CV Mitra Timur" tidak tampil pada tabel Purchase History Storage
18. Verifikasi opsi Filter Source pada tabel Purchase History Storage hanya memuat "CV Mitra Sejati", "TAG Samurai"
19. Verifikasi tidak ada baris placeholder atau teks "Other manager" pada tabel Purchase History Storage
20. Klik ulang icon Filter untuk menutup panel Filter

### Distributor Total Control (PT Distribusi Nusantara): TC-AC-ACC-1015

21. Logout dari akun Partner Total Control (CV Mitra Sejati)
22. Login sebagai Distributor Total Control (PT Distribusi Nusantara)
23. Klik sub-tab `Active`, ketik Search `PT Jaringan Ganda Uji`, tekan Enter
24. Klik Company Name "PT Jaringan Ganda Uji" untuk membuka Detail
25. Klik Tab `TAG`, lihat tabel Purchase History TAG, lalu buka Filter Source
26. Verifikasi tabel Purchase History TAG memuat 3 baris dengan Source "CV Mitra Sejati", "CV Mitra Lestari", "TAG Samurai" (Source Principal tetap tampil)
27. Verifikasi baris Source "CV Mitra Timur" tidak tampil pada tabel Purchase History TAG
28. Verifikasi opsi Filter Source pada tabel Purchase History TAG hanya memuat "CV Mitra Sejati", "CV Mitra Lestari", "TAG Samurai"
29. Verifikasi tidak ada baris placeholder atau teks "Other manager" pada tabel Purchase History TAG
30. Klik ulang icon Filter untuk menutup panel Filter
31. Klik Tab `Hardware`, lihat tabel Purchase History Hardware, lalu buka Filter Source
32. Verifikasi tabel Purchase History Hardware memuat 3 baris dengan Source "CV Mitra Sejati", "CV Mitra Lestari", "TAG Samurai" (Source Principal tetap tampil)
33. Verifikasi baris Source "CV Mitra Timur" tidak tampil pada tabel Purchase History Hardware
34. Verifikasi opsi Filter Source pada tabel Purchase History Hardware hanya memuat "CV Mitra Sejati", "CV Mitra Lestari", "TAG Samurai"
35. Verifikasi tidak ada baris placeholder atau teks "Other manager" pada tabel Purchase History Hardware
36. Klik ulang icon Filter untuk menutup panel Filter
37. Klik Tab `Storage`, lihat tabel Purchase History Storage, lalu buka Filter Source
38. Verifikasi tabel Purchase History Storage memuat 3 baris dengan Source "CV Mitra Sejati", "CV Mitra Lestari", "TAG Samurai" (Source Principal tetap tampil)
39. Verifikasi baris Source "CV Mitra Timur" tidak tampil pada tabel Purchase History Storage
40. Verifikasi opsi Filter Source pada tabel Purchase History Storage hanya memuat "CV Mitra Sejati", "CV Mitra Lestari", "TAG Samurai"
41. Verifikasi tidak ada baris placeholder atau teks "Other manager" pada tabel Purchase History Storage
42. Klik ulang icon Filter untuk menutup panel Filter

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec ditulis per blok role karena ganti akun memakai Step eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3a). Spec melewati sekitar 35 langkah; alasan: seluruh blok berupa pembacaan dua role pada satu Client dan tiga tab, tiap blok berdiri sendiri.
- Anchor absence: Verifikasi baris yang tampil (Source viewer dan Source Principal) pada tabel yang sama mendahului asersi baris Source manager lain tidak tampil dan opsi Filter (bagian 8b butir 2). Penutupan panel Filter lewat klik ulang icon Filter (D-001) adalah langkah penghubung (S-03).
- Temuan untuk QA (S-15): kedua TC menyebut "Source Principal" sebagai nilai Source `TAG Samurai`. Post Condition `-`.
