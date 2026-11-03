---
id: TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog
title: "Generate Enrollment QR: Dialog, Pilihan SFR Otomatis, Token Active, Warning D-13, dan Changelog Asset Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-315
  - TC-AC-ACC-316
  - TC-AC-ACC-318
  - TC-AC-ACC-896
  - TC-AC-ACC-916
  - TC-AC-ACC-991
coverage:
  web: automated
---

# Generate Enrollment QR: Dialog, Pilihan SFR Otomatis, Token Active, Warning D-13, dan Changelog Asset Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Dinamis milik spec (kembaran fixture; skrip seed di hook `before`, bukan lewat UI; dihapus di hook `after`; Generate Enrollment QR menulis token Active sehingga spec tidak memakai C-01, C-AST-8, C-AST-41, dan C-AST-42 bersama [S-06]; Company Name bersuffix `{runId}-234`, atribut setara baris fixture asal di Tabel A2/A3 (Partner CV Mitra Sejati; Group Area Jakarta; FAMS Active), nama SFR, Station, dan Tablet di dalam kembaran sama dengan fixture asal karena terlingkup pada Client kembaran):
  - "PT Sejahtera Abadi {runId}-234" (kembaran C-01, TC-AC-ACC-315): Asset Control Total 3 / Used 2 / Available 1 (Station "Gerbang Gudang A" Active, "Gerbang Gudang B" Inactive, "Gerbang Lama" Deactivated); dua SFR eligible "Reader Alfa" dan "Reader Beta" (bertipe Asset Control, tanpa station aktif); tanpa token Enrollment QR Active.
  - "PT Uji Token QR {runId}-234" (kembaran C-AST-8, TC-AC-ACC-896, 991, 916): Asset Control Total 5 / Used 1; SFR "Reader Token 1" bertipe Asset Control tanpa station aktif, SFR "Reader Token Aktif" bertipe Asset Control dengan station "Stasiun Token Aktif" Active, SFR "Reader Umum Token" bukan bertipe Asset Control; tanpa token Active.
  - "PT Uji Generate QR {runId}-234" (kembaran C-AST-41, TC-AC-ACC-316): Asset Control Total 3 / Used 0 / Available 3; SFR "Reader Baru"; tanpa token Active.
  - "PT Uji Invalidasi QR {runId}-234" (kembaran C-AST-42, TC-AC-ACC-318): Asset Control Total 3 / Used 0 / Available 3; SFR "Reader Invalidasi"; tanpa token Active.
- Kemampuan teknis: jam server uji dapat dimajukan dan dipulihkan (token Active dikembalikan ke Expired dengan memajukan jam server 15 menit, dilakukan di langkah penghubung 15, 24, 34, 44, 69 dan di hook `after`; jam server dan jam browser dipulihkan bersama sesudahnya); penangkapan nama berkas unduhan di browser uji (disediakan tim FE).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- Baseline Changelog Asset Control: jumlah baris Action `Generate Enrollment QR` dicatat lewat Search di modal Changelog sebelum aksi pemicu pertama yang diasersi (S-12).
- State global: jam server dimajukan lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-315: Screening dialog Enrollment QR

1. Ketik Search "PT Sejahtera Abadi {runId}-234" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi {runId}-234", lalu klik Tab Asset Control
2. Klik [Generate Enrollment QR]
3. Verifikasi Header dialog: Title "Enrollment QR"
4. Verifikasi dropdown "Select Smart Fixed Reader" kosong (belum ada SFR terpilih)
5. Klik dropdown "Select Smart Fixed Reader"
6. Verifikasi dropdown memuat opsi "Reader Alfa" dan "Reader Beta"
7. Verifikasi QR Code belum tampil
8. Pilih "Reader Alfa"
9. Verifikasi QR Code tampil di tengah dialog
10. Verifikasi teks "Scan this QR to enroll a tablet as an Asset Control station."
11. Verifikasi teks "This QR can only be used once and expires in 15 minutes."
12. Verifikasi baris `Expiry: [timestamp]` tampil
13. Verifikasi Footer: [Download QR] dan [Close] tampil
14. Klik [Close]
15. Majukan jam server uji 15 menit hingga token Active menjadi Expired, lalu pulihkan jam server dan jam browser

### TC-AC-ACC-896: Dropdown Select Smart Fixed Reader hanya memuat SFR eligible

16. Klik breadcrumb "Client", ketik Search "PT Uji Token QR {runId}-234", tekan Enter, klik Company Name "PT Uji Token QR {runId}-234", lalu klik Tab Asset Control
17. Klik [Generate Enrollment QR]
18. Verifikasi dialog dengan Title "Enrollment QR" tampil
19. Klik dropdown "Select Smart Fixed Reader"
20. Verifikasi dropdown memuat opsi "Reader Token 1"
21. Verifikasi dropdown tidak memuat "Reader Token Aktif"
22. Verifikasi dropdown tidak memuat "Reader Umum Token"
23. Tutup dropdown dengan Esc lalu klik [Close]
24. Majukan jam server uji 15 menit hingga token Active menjadi Expired, lalu pulihkan jam server dan jam browser

### TC-AC-ACC-991: Satu SFR eligible otomatis terpilih dan QR langsung tampil

25. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter, catat jumlah baris Action `Generate Enrollment QR` (N1), lalu tutup modal
26. Klik [Generate Enrollment QR]
27. Verifikasi dialog dengan Title "Enrollment QR" tampil
28. Verifikasi dropdown "Select Smart Fixed Reader" sudah terisi "Reader Token 1" tanpa dipilih manual
29. Verifikasi QR Code langsung tampil
30. Klik [Close]
31. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter
32. Verifikasi jumlah baris Action `Generate Enrollment QR` = N1 + 1
33. Verifikasi baris baru: Action `Generate Enrollment QR`, Object `Enrollment Token`, Field `Status`, Old Value `—`, New Value `Active`
34. Tutup modal Changelog, lalu majukan jam server uji 15 menit hingga token Active menjadi Expired dan pulihkan jam server dan jam browser

### TC-AC-ACC-916: Double-klik [Generate Enrollment QR] hanya menghasilkan satu token Active

35. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter, catat jumlah baris Action `Generate Enrollment QR` (N2), lalu tutup modal
36. Klik [Generate Enrollment QR] dua kali cepat
37. Verifikasi hanya satu dialog "Enrollment QR" yang tampil (tidak ada dialog bertumpuk)
38. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Token 1" tanpa dipilih manual dan QR Code tampil
39. Verifikasi dialog "Active Enrollment QR" tidak muncul setelah QR tampil
40. Klik [Close]
41. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter
42. Verifikasi jumlah baris Action `Generate Enrollment QR` = N2 + 1
43. Verifikasi baris baru: Object `Enrollment Token`, Old Value `—`, New Value `Active`
44. Tutup modal Changelog, lalu majukan jam server uji 15 menit hingga token Active menjadi Expired dan pulihkan jam server dan jam browser

### TC-AC-ACC-316: Generate menampilkan QR dan mencatat token Active di Changelog Asset Control

45. Klik breadcrumb "Client", ketik Search "PT Uji Generate QR {runId}-234", tekan Enter, klik Company Name "PT Uji Generate QR {runId}-234", lalu klik Tab Asset Control
46. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter, catat jumlah baris Action `Generate Enrollment QR` (N3), lalu tutup modal
47. Klik [Generate Enrollment QR]
48. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Baru" tanpa dipilih manual dan QR Code tampil
49. Verifikasi tidak ada toast sukses
50. Klik [Download QR]
51. Verifikasi berkas `Station-Enrollment-QR.png` terunduh
52. Klik [Close]
53. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter
54. Verifikasi jumlah baris Action `Generate Enrollment QR` = N3 + 1
55. Verifikasi baris terbaru: Action `Generate Enrollment QR`, Object `Enrollment Token`, Field `Status`, Old Value `—`, New Value `Active`

### TC-AC-ACC-318: Token lama masih aktif: dialog warning D-13

56. Tutup modal Changelog, klik breadcrumb "Client", ketik Search "PT Uji Invalidasi QR {runId}-234", tekan Enter, klik Company Name "PT Uji Invalidasi QR {runId}-234", lalu klik Tab Asset Control
57. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter, catat jumlah baris Action `Generate Enrollment QR` (N4), lalu tutup modal
58. Klik [Generate Enrollment QR]
59. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Invalidasi" dan QR Code tampil, lalu klik [Close]
60. Klik [Generate Enrollment QR] lagi
61. Verifikasi dialog warning: Title "Active Enrollment QR", teks "A previous QR is still active and hasn't been used yet. Generating a new one will invalidate the previous QR. Are you sure you want to generate a new one?", tombol [Cancel] dan [Generate New QR]
62. Klik [Cancel]
63. Verifikasi dialog tertutup dan tidak ada dialog "Enrollment QR" baru
64. Klik [Generate Enrollment QR] lagi lalu klik [Generate New QR]
65. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Invalidasi" dan QR Code baru tampil, lalu klik [Close]
66. Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Generate Enrollment QR", tekan Enter
67. Verifikasi jumlah baris Action `Generate Enrollment QR` = N4 + 2
68. Verifikasi dua baris terbaru: Object `Enrollment Token`, Field `Status`, Old Value `—`, New Value `Active`
69. Tutup modal Changelog, lalu majukan jam server uji 15 menit hingga token Active menjadi Expired dan pulihkan jam server dan jam browser

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 16, 45, 56 (Search dan buka Detail Client, klik Tab Asset Control; hook suite hanya membuka List Client); klik breadcrumb "Client"; langkah 5, 19, 23 (membuka dan menutup dropdown agar opsi teramati); langkah 15, 24, 34, 44, 69 dan bagian akhir langkah 25, 31, 35, 41, 46, 53, 57, 66 (Search "Generate Enrollment QR" dan ukuran halaman 100 agar baris yang dihitung berada di halaman teramati, S-14; TC tidak menyebut Search ini). Langkah 15, 24, 34, 44, 69 memulihkan token Active menjadi Expired mengikuti Post Condition TC-AC-ACC-896/991/916/318 dan melayani precondition "tanpa token Enrollment QR Active" TC berikutnya; TC-AC-ACC-315 dan TC-AC-ACC-316 tidak menulis Post Condition itu (lihat Temuan).
- Baseline (S-12): TC-AC-ACC-916 tidak mencatat jumlah baris Changelog; langkah 35 dan 42 menambahkan baseline N2 agar "tepat 1 baris baru" teruji.
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas (Generate Enrollment QR dengan Active-Full pada Tab Asset Control) dan tiap blok berdiri sendiri (Client berbeda, atau token dipulihkan di antaranya); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC di spec berbeda dari urutan TC (315, 896, 991, 916, 316, 318) agar kembaran C-AST-8 dipakai berurutan dengan pemulihan token di antaranya; tidak ada TC yang bergantung pada hasil TC lain.
- Pembagian TC lintas spec: TTL token (batas 15:00) ada di spec 235; blokir Generate ada di spec 233; kegagalan Generate (500) di spec 240; hak Update-saja di spec 236.
- Temuan untuk QA:
  - TC-AC-ACC-315 dan TC-AC-ACC-316 menghasilkan token Active tetapi tidak menulis pemulihan token Active pada Post Condition (TC-AC-ACC-315 menyebut pemulihan jam server saja; TC-AC-ACC-316 memulihkan lewat seed ulang); langkah 15 memulihkan kembaran C-01 lewat jam server.
  - TC-AC-ACC-315 Expected b menyebut "belum ada token dibuat" sebelum SFR dipilih tanpa langkah observasi; tidak diasersi selain QR Code belum tampil.
  - TC-AC-ACC-315 memakai Client Pre-setup C-01 sebagai target Generate; spec memakai kembaran bersuffix `{runId}-234` agar C-01 bersama tidak berubah; Used/Available tidak berubah (token Active belum dihitung Used).
  - TC-AC-ACC-318 langkah 3 dan 7 menyebut "SFR otomatis terpilih" padahal C-AST-42 hanya punya satu SFR eligible; spec mengasersi sesuai TC.
