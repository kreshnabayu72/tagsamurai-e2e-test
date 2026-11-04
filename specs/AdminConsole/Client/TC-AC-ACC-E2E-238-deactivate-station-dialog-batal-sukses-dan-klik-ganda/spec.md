---
id: TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda
title: "Deactivate Station: Dialog, Batal, Hidden pada Station Deactivated, Sukses, Kuota Kembali, dan Klik Ganda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-324
  - TC-AC-ACC-325
  - TC-AC-ACC-326
  - TC-AC-ACC-327
  - TC-AC-ACC-328
  - TC-AC-ACC-902
  - TC-AC-ACC-917
coverage:
  web: automated
---

# Deactivate Station: Dialog, Batal, Hidden pada Station Deactivated, Sukses, Kuota Kembali, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca, dialog dibatalkan): C-01 "PT Sejahtera Abadi" dengan Station "Gerbang Gudang A" (Active) dan "Gerbang Lama" (Deactivated) untuk TC-AC-ACC-324, 326, 327.
- Data Dinamis milik spec (kembaran fixture; skrip seed di hook `before`, bukan lewat UI; dihapus di hook `after`; Deactivate permanen sehingga spec tidak memakai C-AST-7, C-AST-43, dan C-AST-44 bersama [S-06]; Company Name bersuffix `{runId}-238`, atribut setara baris fixture asal di Tabel A3 (Partner CV Mitra Sejati; Group Area Jakarta; FAMS Active), nama SFR, Station, dan Tablet di dalam kembaran sama dengan fixture asal karena terlingkup pada Client kembaran):
  - "PT Uji Aksi Asset Control {runId}-238" (kembaran C-AST-7, TC-AC-ACC-902 dan 917): Asset Control Total 10 / Used 6 (nilai awal sama dengan fixture asal; asersi memakai selisih relatif terhadap nilai yang dicatat); Station Active "Stasiun Klik Ganda Deactivate" dengan Tablet "Tablet Klik Ganda Deactivate 1" Active; Station Inactive "Stasiun Inactive Uji" dengan satu Tablet "Tablet Inactive Uji 1" Inactive.
  - "PT Uji Deactivate Satu {runId}-238" (kembaran C-AST-43, TC-AC-ACC-325): Total 3 / Used 2 / Available 1; Station "Gerbang Uji Satu" Active dengan Tablet "Tablet Uji Satu 1" Active dan "Tablet Uji Satu 2" Inactive; Station "Gerbang Uji Satu Pendamping" Inactive dengan Tablet "Tablet Pendamping Satu" Inactive; setiap Station dibuat dari token Enrollment Used.
  - "PT Uji Deactivate Dua {runId}-238" (kembaran C-AST-44, TC-AC-ACC-328): Total 3 / Used 2 / Available 1; Station "Gerbang Uji Dua" Inactive dengan Tablet "Tablet Uji Dua 1" Inactive; Station "Gerbang Uji Dua Pendamping" Active dengan Tablet "Tablet Dua Pendamping" Active; setiap Station dibuat dari token Enrollment Used; tanpa token Active.
- Kemampuan teknis: baca jumlah baris Changelog Asset Control lewat Search di modal (baseline, S-12); jam server uji dapat dimajukan (token Active hasil TC-AC-ACC-328 dikembalikan ke Expired dengan memajukan jam server 15 menit di langkah penghubung 73 dan di hook `after`; jam dipulihkan).
- State global: jam server dimajukan lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-324: Dialog Deactivate Station

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control
2. Buka ⋯ pada Station "Gerbang Gudang A" (Active) lalu klik Deactivate
3. Verifikasi dialog: Title "Deactivate Station", bullet `• Gerbang Gudang A`, teks "This will deactivate this station and revoke all of its tablets. Its Enrollment QR slot will return to available quota. Are you sure you want to deactivate it?", tombol [Cancel] dan [Deactivate]
4. Klik [Cancel]
5. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Gerbang Gudang A", tekan Enter, catat jumlah baris Action `Deactivate Station` (D1), lalu tutup modal

### TC-AC-ACC-326: Cancel dialog Deactivate Station

6. Buka ⋯ pada Station "Gerbang Gudang A" lalu klik Deactivate
7. Klik [Cancel]
8. Verifikasi dialog tertutup
9. Verifikasi Status "Gerbang Gudang A" tetap `Active`
10. Verifikasi tidak ada toast
11. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, lalu ketik Search "Gerbang Gudang A", tekan Enter
12. Verifikasi tidak ada baris log baru Action `Deactivate Station` di Changelog Asset Control (jumlah baris tetap D1)
13. Tutup modal Changelog

### TC-AC-ACC-327: Row action Deactivate Hidden pada Station Deactivated

14. Verifikasi Status "Gerbang Lama" berbadge `Deactivated` (danger)
15. Buka ⋯ pada Station "Gerbang Lama"
16. Verifikasi row action Deactivate tidak tampil
17. Verifikasi tidak ada Reactivate
18. Tutup menu ⋯ dengan Esc

### TC-AC-ACC-902: Deactivate Station berstatus Inactive: kuota dan Changelog Asset Control

19. Klik breadcrumb "Client", ketik Search "PT Uji Aksi Asset Control {runId}-238", tekan Enter, klik Company Name "PT Uji Aksi Asset Control {runId}-238", lalu klik Tab Asset Control
20. Catat Station Quota (Used U1 dan Available A1)
21. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Stasiun Inactive Uji", tekan Enter, catat jumlah baris (L1), lalu tutup modal
22. Buka ⋯ pada "Stasiun Inactive Uji" lalu pilih Deactivate
23. Verifikasi dialog: Title "Deactivate Station", bullet `• Stasiun Inactive Uji`, teks "This will deactivate this station and revoke all of its tablets. Its Enrollment QR slot will return to available quota. Are you sure you want to deactivate it?", tombol [Cancel] dan [Deactivate]
24. Klik [Deactivate] pada dialog
25. Verifikasi toast sukses: "Success, station has been deactivated."
26. Verifikasi "Stasiun Inactive Uji" berbadge `Deactivated` (danger)
27. Buka ⋯ pada "Stasiun Inactive Uji"
28. Verifikasi row action Deactivate Hidden
29. Tutup menu ⋯ dengan Esc
30. Verifikasi kolom Tablets "Stasiun Inactive Uji" bernilai 0
31. Klik row "Stasiun Inactive Uji" untuk expand Tablet List
32. Verifikasi "Tablet Inactive Uji 1" berbadge `Revoked`
33. Verifikasi Station Quota: Used = U1 - 1 dan Available = A1 + 1
34. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Stasiun Inactive Uji", tekan Enter
35. Verifikasi jumlah baris = L1 + 1
36. Verifikasi baris baru: Action `Deactivate Station`, Object `Stasiun Inactive Uji`, Field `Status`, Old Value `Inactive`, New Value `Deactivated`
37. Tutup modal Changelog

### TC-AC-ACC-917: Double-klik [Deactivate] hanya memproses satu kali

38. Catat Station Quota (Used U2 dan Available A2)
39. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Klik Ganda Deactivate", tekan Enter, catat jumlah baris Action `Deactivate Station` (D2) dan jumlah baris Action `Revoke Tablet` (R2), lalu tutup modal
40. Buka ⋯ pada "Stasiun Klik Ganda Deactivate" lalu pilih Deactivate
41. Klik [Deactivate] dua kali cepat
42. Verifikasi satu toast sukses: "Success, station has been deactivated."
43. Verifikasi "Stasiun Klik Ganda Deactivate" berbadge `Deactivated` (danger)
44. Verifikasi Station Quota: Used = U2 - 1 dan Available = A2 + 1 (berkurang tepat 1)
45. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Klik Ganda Deactivate", tekan Enter
46. Verifikasi jumlah baris Action `Deactivate Station` = D2 + 1 dengan Object `Stasiun Klik Ganda Deactivate`
47. Verifikasi jumlah baris Action `Revoke Tablet` tetap R2
48. Tutup modal Changelog, lalu klik row "Stasiun Klik Ganda Deactivate" untuk expand Tablet List
49. Verifikasi "Tablet Klik Ganda Deactivate 1" berbadge `Revoked`

### TC-AC-ACC-325: Deactivate Station: Deactivated permanen, kuota kembali, kedua tablet Revoked

50. Klik breadcrumb "Client", ketik Search "PT Uji Deactivate Satu {runId}-238", tekan Enter, klik Company Name "PT Uji Deactivate Satu {runId}-238", lalu klik Tab Asset Control
51. Catat Station Quota
52. Buka ⋯ pada Station "Gerbang Uji Satu", klik Deactivate, lalu klik [Deactivate] pada dialog
53. Verifikasi toast sukses: "Success, station has been deactivated."
54. Verifikasi Status "Gerbang Uji Satu" berbadge `Deactivated` (danger)
55. Buka ⋯ pada "Gerbang Uji Satu"
56. Verifikasi row action Deactivate Hidden
57. Tutup menu ⋯ dengan Esc
58. Verifikasi Station Quota: Used 1 dan Available 2 (Total 3)
59. Verifikasi kolom Tablets "Gerbang Uji Satu" bernilai 0
60. Klik row "Gerbang Uji Satu" untuk expand Tablet List
61. Verifikasi "Tablet Uji Satu 1" berbadge `Revoked` (danger)
62. Verifikasi "Tablet Uji Satu 2" berbadge `Revoked` (danger)
63. Verifikasi "Gerbang Uji Satu" tetap tampil di Station List sebagai riwayat

### TC-AC-ACC-328: Slot kembali Available setelah Station dengan token Used di-Deactivate

64. Klik breadcrumb "Client", ketik Search "PT Uji Deactivate Dua {runId}-238", tekan Enter, klik Company Name "PT Uji Deactivate Dua {runId}-238", lalu klik Tab Asset Control
65. Verifikasi Station Quota: Total 3, Used 2, Available 1
66. Buka ⋯ pada Station "Gerbang Uji Dua", klik Deactivate, lalu klik [Deactivate] pada dialog
67. Verifikasi Station Quota: Used 1 dan Available 2 (Total 3)
68. Verifikasi Status "Gerbang Uji Dua" berbadge `Deactivated`
69. Klik [Generate Enrollment QR]
70. Verifikasi dialog dengan Title "Enrollment QR" langsung tampil
71. Verifikasi dialog warning "Active Enrollment QR" tidak muncul
72. Klik [Close]
73. Majukan jam server uji 15 menit hingga token Active menjadi Expired, lalu pulihkan jam server dan jam browser

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 19, 50, 64 (Search dan buka Detail Client; hook suite hanya membuka List Client); langkah 4 (menutup dialog setelah verifikasi), 18, 29, 57 (menutup menu), 13, 37 dan 48 (menutup modal Changelog); langkah 73 (memulihkan token Active menjadi Expired, melayani Post Condition seed ulang C-AST-44 pada kembarannya).
- Baseline (S-12): TC-AC-ACC-326 menyebut Changelog Asset Control pada Expected tetapi langkahnya tidak mencatat jumlah baris; TC-AC-ACC-902 dan 917 juga tidak mencatat jumlah baris Changelog; langkah 5, 20, 21, 38, 39 menambahkan baseline agar "tidak ada baris baru Deactivate Station" (langkah 11 sampai 13), "baris baru" dan "tidak ada baris Revoke Tablet" teruji dengan selisih terhadap baseline. Search di modal dan ukuran halaman 100 agar baris yang dihitung berada di halaman teramati (S-14).
- Urutan TC di spec: dialog dan batal (324, 326, 327) di awal, TC yang menghabisi data kemudian. TC-AC-ACC-902 dan 917 memakai Client C-AST-7 dengan Station yang berbeda sehingga tidak saling bergantung.
- Spec ini melewati batas 35 langkah (73 langkah). Alasan: semua blok satu topik aksi (Deactivate Station) dengan Active-Full tanpa ganti akun, tiap blok memakai Station atau Client sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: asersi tanpa toast dan tanpa baris log `Deactivate Station` untuk Cancel (TC-AC-ACC-326) dibuktikan di spec ini dengan baseline (langkah 5 dan 11 sampai 13; TC terbelah presence/absence menurut S-05, spec 272 tidak memuat TC-326); Revoke Tablet ada di spec 239; kegagalan Global Settings di spec 240; dua sesi (stale 409) di spec 247; pencatatan lintas surface Deactivate di spec 270.
- Replika S-06 [KEPUTUSAN 2026-11-03]: Deactivate menghabisi Station, sehingga TC-AC-ACC-902, 917, 325, dan 328 memakai kembaran C-AST-7, C-AST-43, dan C-AST-44 bersuffix `{runId}-238` (seed di `before`, cleanup di `after`); C-01 "PT Sejahtera Abadi" hanya dibaca (dialog dibatalkan).
- Temuan untuk QA:
  - TC-AC-ACC-324 dan TC-AC-ACC-326 tidak menyebut Station target selain "Station Active"; spec memakai "Gerbang Gudang A" (Pre-setup C-01).
  - TC-AC-ACC-328 Post Condition "seed ulang C-AST-44" tidak menyebut token Active hasil langkah Generate; spec memulihkannya lewat memajukan jam server.
