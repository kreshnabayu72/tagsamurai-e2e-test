---
id: TC-FA-DAMAGED-E2E-003-tabel-active-sort
title: "Sort per kolom sub-tab Active mengikuti tipe data, Status diurutkan per label tanpa penanda, dan klik ketiga kembali ke urutan default"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§5#r4", EB-SRT-1, EB-SRT-2, EB-SRT-3@tabel-active]
smoke: [EB-SRT-1, EB-SRT-2, EB-SRT-3@tabel-active]
dependsOn: []
trace:
  T-DMG-01: [5, 7, 10, 12, 17, 19, 22, 23, 25, 28, 31, 32, 34, 37, 39, 48, 49, 51, 52, 54, 56, 57, 60, 62]
  "§5#r4": [3]
  EB-SRT-1: [5, 7, 10, 12, 17, 19, 22, 25, 28, 48, 51, 54, 56, 60, 62]
  EB-SRT-2: [23, 31, 32, 34, 37, 39, 49, 52, 57]
  EB-SRT-3@tabel-active: [15]
anchor: []
coverage:
  web: automated
---

# Sort per kolom sub-tab Active mengikuti tipe data, Status diurutkan per label tanpa penanda, dan klik ketiga kembali ke urutan default

## Prerequisites
- Aktor: Total Control, user `Admin T`.
- Layar awal: halaman Assets.
- Data:
  - DU-003-1: Name `anggur {runId} - 1`, Status `Damaged`, Last Holder `—`, Reported Date `T0 − 4 hari, pukul 10:00`, Days Damaged `4 days`, TAG `RFID`, Asset Value (Commercial) `800000`.
  - DU-003-2: Name `Apel {runId} - 1`, Status `Damaged`, Last Holder `Sari D` (nama lengkap `Sari Dewanti`), Reported Date `T0 − 6 hari, pukul 10:00`, Days Damaged `6 days`, TAG `QR`, Asset Value (Commercial) `2500000`.
  - DU-003-3: Name `Crate {runId} - 1`, Status `Waiting for Confirmation`, Last Holder `—`, Reported Date `T0 − 9 hari, pukul 10:00`, Days Damaged `9 days`, TAG `NFC`, Asset Value (Commercial) `12000000`.
  - DU-003-4: Name `Crate {runId} - 2`, Status `Reported Disposal`, Last Holder `Dewi A` (nama lengkap `Dewi Anggraini`), Reported Date `T0 − 12 hari, pukul 10:00`, Days Damaged `12 days`.
  - DU-003-5: Name `Crate {runId} - 10`, Status `In Disposal Process`, Last Holder `—`, Reported Date `T0 − 15 hari, pukul 10:00`, Days Damaged `15 days`.
  - DU-003-6: Name `Elan {runId} - 1`, Status `Damaged`, Last Holder `Budi S` (nama lengkap `Budi Santoso`), Reported Date `T0 − 5 hari, pukul 10:00`, Days Damaged `5 days`, Labels `Aset Kritis {runId}`.
  - DU-003-7: Name `Élan {runId} - 1`, Status `Damaged`, Last Holder `—`, Reported Date `T0 − 7 hari, pukul 10:00`, Days Damaged `7 days`.
  - DU-003-8: Name `Ezra {runId} - 1`, Status `Damaged`, Last Holder `Sari D` (nama lengkap `Sari Dewanti`), Reported Date `T0 − 8 hari, pukul 10:00`, Days Damaged `8 days`, Labels `Operasional {runId}`.
  - DU-003-9: Name `3D Printer {runId} - 1`, Status `Damaged`, Last Holder `—`, Reported Date `T0 − 10 hari, pukul 10:00`, Days Damaged `10 days`.
  - DU-003-10: Name `#Gudang {runId} - 1`, Status `Damaged`, Last Holder `Dewi A` (nama lengkap `Dewi Anggraini`), Reported Date `T0 − 11 hari, pukul 10:00`, Days Damaged `11 days`.
  - DU-003-11: Name `Zulu {runId} - 1`, Status `Damaged`, Last Holder `Budi H` (nama lengkap `Budi Hartono`), Reported Date `T0 − 13 hari, pukul 09:00`, Days Damaged `13 days`, Last Updated sama dengan Reported Date, Labels `Aset Kritis {runId}` dan `Gudang {runId}`.
  - DU-003-12: Name `Zulu {runId} - 2`, Status `Damaged`, Last Holder `Sari D` (nama lengkap `Sari Dewanti`), Reported Date `T0 − 13 hari, pukul 09:30`, Days Damaged `13 days`, Last Updated sama dengan Reported Date, Labels `Aset Kritis {runId}`, `Gudang {runId}`, dan `Operasional {runId}`.
  - Seluruh record di atas memakai Group `Head Office {runId}`, Source `Manual`, Reported By `Agus P`, dan Asset ID `SRT-0001-{runId}` sampai `SRT-0012-{runId}` menurut nomor entri; dibuat dalam urutan DU-003-1 sampai DU-003-12.
  - Ke-`12` record berjalan itu menempati dua halaman dengan 10 baris per halaman; user `Agus P` adalah user ber-runId, Pelapor admin.
  - Record yang tidak disebut membawa TAG, Labels, atau Asset Value (Commercial) tidak memilikinya, sehingga sel kolom itu tampil `—`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Urutan default sebelum sort aktif
1. Buka tab `Damaged` pada halaman Assets
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi sepuluh baris pada halaman pertama tampil dengan baris pertama `Crate {runId} - 1` yang berstatus `Waiting for Confirmation` dan baris kedua `Crate {runId} - 10`

### Sort Name menaik, menurun, lalu kembali ke default pada klik ketiga
4. Klik ikon sort pada header kolom `Name`
5. Verifikasi baris pada halaman pertama berurutan menaik: `#Gudang {runId} - 1`, `3D Printer {runId} - 1`, `anggur {runId} - 1`, `Apel {runId} - 1`, `Crate {runId} - 1`, `Crate {runId} - 2`, `Crate {runId} - 10`, `Elan {runId} - 1`, `Élan {runId} - 1`, `Ezra {runId} - 1`
6. Pindah ke halaman `2`
7. Verifikasi halaman `2` memuat `Zulu {runId} - 1` lalu `Zulu {runId} - 2`
8. Pindah ke halaman `1`
9. Klik ikon sort pada header kolom `Name`
10. Verifikasi baris pada halaman pertama berurutan menurun: `Zulu {runId} - 2`, `Zulu {runId} - 1`, `Ezra {runId} - 1`, `Élan {runId} - 1`, `Elan {runId} - 1`, `Crate {runId} - 10`, `Crate {runId} - 2`, `Crate {runId} - 1`, `Apel {runId} - 1`, `anggur {runId} - 1`
11. Pindah ke halaman `2`
12. Verifikasi halaman `2` memuat `3D Printer {runId} - 1` lalu `#Gudang {runId} - 1`
13. Pindah ke halaman `1`
14. Klik ikon sort pada header kolom `Name`
15. Verifikasi urutan kembali ke default: baris pertama `Crate {runId} - 1` dan baris kedua `Crate {runId} - 10`

### Sort Reported Date mengikuti waktu laporan
16. Klik ikon sort pada header kolom `Reported Date`
17. Verifikasi baris pada halaman pertama berurutan dari laporan terlama: `Crate {runId} - 10`, `Zulu {runId} - 1`, `Zulu {runId} - 2`, `Crate {runId} - 2`, `#Gudang {runId} - 1`, `3D Printer {runId} - 1`, `Crate {runId} - 1`, `Ezra {runId} - 1`, `Élan {runId} - 1`, `Apel {runId} - 1`
18. Klik ikon sort pada header kolom `Reported Date`
19. Verifikasi baris pertama `anggur {runId} - 1` dan baris kedua `Elan {runId} - 1` untuk laporan terbaru lebih dulu
20. Klik ikon sort pada header kolom `Reported Date`

### Sort Status mengikuti label badge dan memakai urutan default untuk status sama
21. Klik ikon sort pada header kolom `Status`
22. Verifikasi sembilan baris pertama berstatus `Damaged` dan baris kesepuluh berstatus `In Disposal Process`
23. Verifikasi baris ketiga sampai kesembilan, yaitu baris `Damaged` yang laporannya lebih baru dari `Zulu {runId} - 1` dan `Zulu {runId} - 2`, berurutan menurut default: `#Gudang {runId} - 1`, `3D Printer {runId} - 1`, `Ezra {runId} - 1`, `Élan {runId} - 1`, `Apel {runId} - 1`, `Elan {runId} - 1`, `anggur {runId} - 1`
24. Pindah ke halaman `2`
25. Verifikasi halaman `2` memuat `Crate {runId} - 2` berstatus `Reported Disposal` lalu `Crate {runId} - 1` berstatus `Waiting for Confirmation`
26. Pindah ke halaman `1`
27. Klik ikon sort pada header kolom `Status`
28. Verifikasi tiga baris pertama berstatus `Waiting for Confirmation`, `Reported Disposal`, lalu `In Disposal Process`
29. Klik ikon sort pada header kolom `Status`

### Sort Last Holder menaruh nilai kosong di akhir saat menaik dan di awal saat menurun
30. Klik ikon sort pada header kolom `Last Holder`
31. Verifikasi tujuh baris pertama berurutan menurut nama lengkap pemegang: `Zulu {runId} - 1`, `Elan {runId} - 1`, `Crate {runId} - 2`, `#Gudang {runId} - 1`, `Zulu {runId} - 2`, `Ezra {runId} - 1`, `Apel {runId} - 1`
32. Verifikasi tiga baris berikutnya memuat Last Holder `—`
33. Klik ikon sort pada header kolom `Last Holder`
34. Verifikasi lima baris pertama memuat Last Holder `—` dan baris keenam memuat Last Holder `Sari D`
35. Klik ikon sort pada header kolom `Last Holder`

### Sort kolom bernilai sama di seluruh baris tetap deterministik lintas halaman
36. Klik ikon sort pada header kolom `Source`
37. Verifikasi halaman `1` memuat sepuluh baris dan baris pertama `Crate {runId} - 1`
38. Pindah ke halaman `2`
39. Verifikasi halaman `2` memuat dua baris yang tidak tampil di halaman `1`, sehingga kedua belas baris milik spec ini tampil tepat satu kali

### Sort kolom TAG, Labels, Days Damaged, Asset Value (Commercial), dan Last Updated
40. Pindah ke halaman `1`
41. Klik header kolom Actions `⋯`
42. Centang `TAG`
43. Klik header kolom Actions `⋯`
44. Centang `Labels`
45. Klik header kolom Actions `⋯`
46. Centang `Asset Value (Commercial)`
47. Klik ikon sort pada header kolom `TAG`
48. Verifikasi tiga baris pertama berurutan menurut label ikon TAG: `Crate {runId} - 1` dengan TAG `NFC`, `Apel {runId} - 1` dengan TAG `QR`, lalu `anggur {runId} - 1` dengan TAG `RFID`
49. Verifikasi tujuh baris berikutnya pada halaman pertama memuat TAG `—` di akhir urutan menaik
50. Klik ikon sort pada header kolom `Labels`
51. Verifikasi empat baris pertama berurutan menurut jumlah label terkecil dulu: `Elan {runId} - 1` dan `Ezra {runId} - 1` (satu label, label pertama `Aset Kritis {runId}` lebih dulu daripada `Operasional {runId}`), `Zulu {runId} - 1` (dua label), lalu `Zulu {runId} - 2` (tiga label)
52. Verifikasi enam baris berikutnya pada halaman pertama memuat Labels `—` di akhir urutan menaik
53. Klik ikon sort pada header kolom `Days Damaged`
54. Verifikasi lima baris pertama berurutan menurut Days Damaged terkecil dulu: `anggur {runId} - 1` (`4 days`), `Elan {runId} - 1` (`5 days`), `Apel {runId} - 1` (`6 days`), `Élan {runId} - 1` (`7 days`), lalu `Ezra {runId} - 1` (`8 days`)
55. Klik ikon sort pada header kolom `Asset Value (Commercial)`
56. Verifikasi tiga baris pertama berurutan menurut nilai angka terkecil dulu: `anggur {runId} - 1` (`800000`), `Apel {runId} - 1` (`2500000`), lalu `Crate {runId} - 1` (`12000000`)
57. Verifikasi tujuh baris berikutnya pada halaman pertama memuat Asset Value (Commercial) `—` di akhir urutan menaik
58. Ganti isi kotak search dengan `Zulu {runId}`, tekan Enter
59. Klik ikon sort pada header kolom `Last Updated`
60. Verifikasi baris pertama `Zulu {runId} - 1` dan baris kedua `Zulu {runId} - 2` untuk Last Updated terlama lebih dulu
61. Klik ikon sort pada header kolom `Last Updated`
62. Verifikasi baris pertama `Zulu {runId} - 2` dan baris kedua `Zulu {runId} - 1` untuk Last Updated terbaru lebih dulu
63. Klik ikon sort pada header kolom `Last Updated`
64. Ganti isi kotak search dengan `{runId}`, tekan Enter
