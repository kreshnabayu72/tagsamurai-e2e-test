---
id: TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda
title: "Revoke Tablet: Dialog, Batal, Hidden pada Tablet Revoked, Sukses, Kuota Station Tetap, dan Klik Ganda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-329
  - TC-AC-ACC-330
  - TC-AC-ACC-331
  - TC-AC-ACC-332
  - TC-AC-ACC-901
  - TC-AC-ACC-918
coverage:
  web: automated
---

# Revoke Tablet: Dialog, Batal, Hidden pada Tablet Revoked, Sukses, Kuota Station Tetap, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca, dialog dibatalkan): C-01 "PT Sejahtera Abadi" dengan Station "Gerbang Gudang A" (Active) berisi Tablet "Tablet Lobi 1" (Active), dan Station "Gerbang Lama" (Deactivated) berisi Tablet "Tablet Lama" (Revoked) untuk TC-AC-ACC-329, 331, 332.
- Data fixture Tabel A3 (skrip seed, bukan lewat UI; Revoke permanen sehingga di-seed ulang lewat reset data uji): C-AST-7 "PT Uji Aksi Asset Control" dengan Station "Stasiun Tablet Uji" (Active) berisi Tablet Active "Tablet Revoke Aktif" dan "Tablet Klik Ganda Revoke", dan Tablet Inactive "Tablet Revoke Inactive" (TC-AC-ACC-330, 901, 918).
- Kemampuan teknis: baca jumlah baris Changelog Asset Control lewat Search di modal (baseline, S-12).
- State global: tidak ada yang diubah selain data fixture di atas; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-329: Dialog Revoke Tablet

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control
2. Klik row Station "Gerbang Gudang A" untuk expand Tablet List
3. Buka ⋯ pada Tablet "Tablet Lobi 1" (Active) lalu klik Revoke
4. Verifikasi dialog: Title "Revoke Tablet", bullet `• Tablet Lobi 1`, teks "This will revoke this tablet's enrollment. It will no longer sync with this station. Are you sure you want to revoke it?", tombol [Cancel] dan [Revoke]
5. Klik [Cancel]

### TC-AC-ACC-331: Cancel dialog Revoke Tablet

6. Buka ⋯ pada Tablet "Tablet Lobi 1" lalu klik Revoke
7. Klik [Cancel]
8. Verifikasi dialog tertutup
9. Verifikasi Status "Tablet Lobi 1" tetap `Active`
10. Verifikasi tidak ada toast

### TC-AC-ACC-332: Row action Revoke Hidden pada Tablet Revoked

11. Klik row Station "Gerbang Lama" untuk expand Tablet List
12. Verifikasi Status "Tablet Lama" berbadge `Revoked` (danger)
13. Buka ⋯ pada Tablet "Tablet Lama"
14. Verifikasi row action Revoke tidak tampil
15. Tutup menu ⋯ dengan Esc

### TC-AC-ACC-330: Revoke Tablet Active: status Revoked permanen, Tablets berkurang, kuota Station tidak berubah

16. Klik breadcrumb "Client", ketik Search "PT Uji Aksi Asset Control", tekan Enter, klik Company Name "PT Uji Aksi Asset Control", lalu klik Tab Asset Control
17. Catat Station Quota, lalu klik row "Stasiun Tablet Uji" untuk expand Tablet List dan catat kolom Tablets (T1)
18. Buka ⋯ pada "Tablet Revoke Aktif" lalu pilih Revoke
19. Klik [Revoke] pada dialog
20. Verifikasi toast sukses: "Success, tablet has been revoked."
21. Verifikasi baris "Tablet Revoke Aktif" tampil dengan badge `Revoked` (danger)
22. Buka ⋯ pada "Tablet Revoke Aktif"
23. Verifikasi row action Revoke Hidden
24. Tutup menu ⋯ dengan Esc
25. Verifikasi kolom Tablets "Stasiun Tablet Uji" = T1 - 1 (Revoked tidak dihitung)
26. Verifikasi Station Quota sama dengan nilai yang dicatat (Used dan Available tidak berubah)
27. Verifikasi status Station "Stasiun Tablet Uji" tetap `Active`

### TC-AC-ACC-901: Revoke Tablet berstatus Inactive: Changelog Asset Control mencatat Old Value Inactive

28. Catat Station Quota dan kolom Tablets "Stasiun Tablet Uji" (T2)
29. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Tablet Revoke Inactive", tekan Enter, catat jumlah baris (L2), lalu tutup modal
30. Buka ⋯ pada "Tablet Revoke Inactive" lalu pilih Revoke
31. Verifikasi dialog: Title "Revoke Tablet", bullet `• Tablet Revoke Inactive`, teks "This will revoke this tablet's enrollment. It will no longer sync with this station. Are you sure you want to revoke it?", tombol [Cancel] dan [Revoke]
32. Klik [Revoke] pada dialog
33. Verifikasi toast sukses: "Success, tablet has been revoked."
34. Verifikasi baris "Tablet Revoke Inactive" berbadge `Revoked` (danger)
35. Buka ⋯ pada "Tablet Revoke Inactive"
36. Verifikasi row action Revoke Hidden
37. Tutup menu ⋯ dengan Esc
38. Verifikasi kolom Tablets "Stasiun Tablet Uji" = T2 - 1
39. Verifikasi Station Quota sama dengan nilai yang dicatat (Used dan Available tidak berubah)
40. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Tablet Revoke Inactive", tekan Enter
41. Verifikasi jumlah baris = L2 + 1
42. Verifikasi baris baru: Action `Revoke Tablet`, Object `Tablet Revoke Inactive`, Field `Status`, Old Value `Inactive`, New Value `Revoked`
43. Tutup modal Changelog

### TC-AC-ACC-918: Double-klik [Revoke] hanya memproses satu kali

44. Catat kolom Tablets "Stasiun Tablet Uji" (T3)
45. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Tablet Klik Ganda Revoke", tekan Enter, catat jumlah baris (L3), lalu tutup modal
46. Buka ⋯ pada "Tablet Klik Ganda Revoke" lalu pilih Revoke
47. Klik [Revoke] dua kali cepat
48. Verifikasi satu toast sukses: "Success, tablet has been revoked."
49. Verifikasi "Tablet Klik Ganda Revoke" berbadge `Revoked` (danger)
50. Verifikasi kolom Tablets "Stasiun Tablet Uji" = T3 - 1 (berkurang tepat 1)
51. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Tablet Klik Ganda Revoke", tekan Enter
52. Verifikasi jumlah baris = L3 + 1 dengan Action `Revoke Tablet` dan Object `Tablet Klik Ganda Revoke`
53. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 dan 16 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 2, 11 (expand row agar Tablet List teramati), langkah 15, 24, 37 (menutup menu), langkah 43 dan 53 (menutup modal Changelog).
- Baseline (S-12): TC-AC-ACC-901 dan 918 tidak mencatat jumlah baris Changelog; langkah 29 dan 45 menambahkan baseline L2 dan L3 serta Search dan ukuran halaman 100 agar "baris baru" teruji dengan selisih (S-14).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu topik aksi (Revoke Tablet) dengan Active-Full tanpa ganti akun, tiap blok memakai Tablet sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: asersi "tanpa log" untuk Cancel (TC-AC-ACC-331) ada di spec 272; Deactivate Station di spec 238; kegagalan Global Settings di spec 240; dua sesi (stale 409) di spec 247; pencatatan lintas surface Revoke di spec 270.
- Temuan untuk QA:
  - TC-AC-ACC-330 Post Condition a sampai c (sesi Station User di-terminate via Auth, Global Settings > Hardware menampilkan "Tablet Revoke Aktif" Revoked, baris Changelog Asset Control `Revoke Tablet`) tidak punya langkah observasi di TC-AC-ACC-330 sehingga tidak diasersi; pencatatan Changelog Asset Control Revoke diasersi lewat TC-AC-ACC-901 dan 911 (spec 267).
  - TC-AC-ACC-331 Expected "Status tetap" tidak menyebut "tanpa log"; TC-AC-ACC-326 menyebutnya. Spec memakai Expected apa adanya.
  - TC-AC-ACC-329 dan TC-AC-ACC-331 tidak menyebut Tablet target selain "Tablet Active"; spec memakai "Tablet Lobi 1" (Pre-setup C-01).
