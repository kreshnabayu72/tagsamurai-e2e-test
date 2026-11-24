---
id: TC-FA-FACO-BE-150-validasi-create
title: "Validasi server Create Account"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [C-07, FACO-LOGIC-01a, N-12, R-01, V-01, V-02, V-03, V-04, V-05, V-06, V-07, V-08, "§6#p1", "§[F-FACO-01] Create Account#b1", "§[F-FACO-01] Create Account#r1", "§[F-FACO-01] Create Account#r2", "§[F-FACO-01] Create Account#r3", "§[F-FACO-01] Create Account#r4", "§9.4.2#r1", "§9.4.2#r2", "§9.4.2#r3", "§9.4.2#r4", "§9.9#r1", "§9.9#r2", "§9.9#r3", EB-FRM-4@account-code, EB-FRM-4@account-name, EB-FRM-5@account-code, EB-FRM-6@form-add-account, EB-CON-2, FACO-LOGIC-07d]
smoke: []
dependsOn: []
trace:
  C-07: [10, 14, 28]
  FACO-LOGIC-01a: [40, 42, 44, 46, 47, 48, 49]
  N-12: [35, 38]
  R-01: [37]
  V-01: [20]
  V-02: [10]
  V-03: [16, 59, 61]
  V-04: [28, 30, 32, 34]
  V-05: [22]
  V-06: [14]
  V-07: [18]
  V-08: [24]
  "§6#p1": [2, 4, 8]
  "§[F-FACO-01] Create Account#b1": [2, 4]
  "§[F-FACO-01] Create Account#r1": [28, 30, 32]
  "§[F-FACO-01] Create Account#r2": [10, 16]
  "§[F-FACO-01] Create Account#r3": [14]
  "§[F-FACO-01] Create Account#r4": [20, 22, 24, 26]
  "§9.4.2#r1": [28, 30, 32]
  "§9.4.2#r2": [10, 16]
  "§9.4.2#r3": [14]
  "§9.4.2#r4": [20, 22, 24, 26]
  "§9.9#r1": [10, 16, 20, 28, 59, 61]
  "§9.9#r2": [14, 18, 22, 51, 57, 67]
  "§9.9#r3": [24, 40, 42, 44, 46, 47, 48, 49]
  EB-FRM-4@account-code: [6, 8, 10]
  EB-FRM-4@account-name: [12, 14]
  EB-FRM-5@account-code: [28]
  EB-FRM-6@form-add-account: [16, 18, 51, 53, 55, 57]
  EB-CON-2: [37, 38]
  FACO-LOGIC-07d: [63, 65]
---

# Validasi server Create Account

## Prerequisites
- Aktor: Admin A dan Admin B, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-150-1: Account Code `KAS-{runId}`, Account Name `Kas Operasional {runId}`, Account Function `Asset Cost`, ada di client aktor.
  - DU-150-5: Account Code `PTG-{runId}`, Account Name `Piutang Usaha Cabang {runId}`, Account Function `Asset Cost`, ada di client lain, bukan client aktor.
  - Account Code yang diharapkan tersimpan `TRM-{runId}`, dari Account Code DU-150-7 yang diberi satu spasi di awal dan satu di akhir.
  - Account Name yang diharapkan tersimpan `Beban Listrik Kantor {runId}`, dari Account Name DU-150-8 yang diberi dua spasi di awal dan dua di akhir.
  - Account Code yang diharapkan tersimpan `BE150-TRIMM-B15`, dari Account Code DU-150-10 yang diberi satu spasi di awal dan satu di akhir.
- Kondisi:
  - Batas jumlah akun client belum tercapai.

## Test Steps

### Account Code dan Account Name disimpan dalam bentuk ter-trim
1. Admin A mengirim Create dengan Account Code `" TRM-{runId} "`, Account Name `Kas Bank {runId}`, Account Function `Asset Cost`
2. Verifikasi akun tersimpan dengan Account Code `TRM-{runId}` tanpa spasi di awal dan akhir
3. Admin A mengirim Create dengan Account Code `LST-{runId}`, Account Name `"  Beban Listrik Kantor {runId}  "`, Account Function `Depreciation Expense`
4. Verifikasi akun tersimpan dengan Account Name `Beban Listrik Kantor {runId}` tanpa spasi di awal dan akhir, dan spasi di antara kata tetap utuh

### Batas panjang Account Code dan Account Name
5. Admin A mengirim Create dengan Account Code `BE150-LIMIT-A15` (15 karakter), Account Name `Batas Code Lima Belas {runId}`, Account Function `Asset Cost`
6. Verifikasi akun dengan Account Code `BE150-LIMIT-A15` diterima dan tersimpan
7. Admin A mengirim Create dengan Account Code `" BE150-TRIMM-B15 "` (satu spasi di awal dan satu di akhir; setelah trim panjangnya 15 karakter), Account Name `Batas Setelah Trim {runId}`, Account Function `Asset Cost`
8. Verifikasi akun diterima dan tersimpan dengan Account Code `BE150-TRIMM-B15`, karena batas dihitung dari panjang setelah trim
9. Admin A mengirim Create dengan Account Code `BE150-LIMIT-A16X` (16 karakter), Account Name `Batas Code Enam Belas {runId}`, Account Function `Asset Cost`
10. Verifikasi permintaan ditolak karena Account Code melebihi 15 karakter, dan tidak ada akun dengan Account Code `BE150-LIMIT-A16X`
11. Admin A mengirim Create dengan Account Code `NM120-{runId}`, Account Name `Akumulasi Penyusutan Peralatan Kantor Cabang Utama Wilayah Jakarta Selatan Periode Tahunan Dua Ribu Dua Puluh Enam Final` (120 karakter), Account Function `Accumulated Depreciation`
12. Verifikasi akun dengan Account Code `NM120-{runId}` diterima dan tersimpan dengan Account Name 120 karakter itu
13. Admin A mengirim Create dengan Account Code `NM121-{runId}`, Account Name `Akumulasi Penyusutan Peralatan Kantor Cabang Utama Wilayah Jakarta Selatan Periode Tahunan Dua Ribu Dua Puluh Enam Revisi` (121 karakter), Account Function `Accumulated Depreciation`
14. Verifikasi permintaan ditolak karena Account Name melebihi 120 karakter, dan tidak ada akun dengan Account Code `NM121-{runId}`

### Karakter yang tidak diizinkan ditolak walau form dilewati
15. Admin A mengirim Create dengan Account Code `AKUN#{runId}`, Account Name `Akun Karakter Khusus {runId}`, Account Function `Asset Cost`
16. Verifikasi permintaan ditolak karena Account Code memuat karakter di luar huruf Latin, angka, `-`, `_`, dan `.`, dan tidak ada akun dengan Account Name `Akun Karakter Khusus {runId}`
17. Admin A mengirim Create dengan Account Code `EMJ-{runId}`, Account Name `Kas 😊 {runId}`, Account Function `Asset Cost`
18. Verifikasi permintaan ditolak karena Account Name memuat emoji, dan tidak ada akun dengan Account Code `EMJ-{runId}`

### Field wajib kosong atau hanya berisi spasi ditolak
19. Admin A mengirim Create dengan Account Code kosong, Account Name `Akun Tanpa Code {runId}`, Account Function `Asset Cost`
20. Verifikasi permintaan ditolak karena Account Code kosong, dan tidak ada akun dengan Account Name `Akun Tanpa Code {runId}`
21. Admin A mengirim Create dengan Account Code `NMK-{runId}`, Account Name kosong, Account Function `Asset Cost`
22. Verifikasi permintaan ditolak karena Account Name kosong, dan tidak ada akun dengan Account Code `NMK-{runId}`
23. Admin A mengirim Create dengan Account Code `FNK-{runId}`, Account Name `Akun Tanpa Function {runId}`, Account Function kosong
24. Verifikasi permintaan ditolak karena Account Function kosong, dan tidak ada akun dengan Account Code `FNK-{runId}`
25. Admin A mengirim Create dengan Account Code `SPS-{runId}`, Account Name berisi tiga spasi saja, Account Function `Asset Cost`
26. Verifikasi permintaan ditolak karena Account Name yang hanya berisi spasi dianggap kosong, dan tidak ada akun dengan Account Code `SPS-{runId}`

### Account Code duplikat ditolak
27. Admin A mengirim Create dengan Account Code `KAS-{runId}`, Account Name `Kas Kecil {runId}`, Account Function `Asset Cost`
28. Verifikasi permintaan ditolak dengan alasan `Account code already exists`, dan akun DU-150-1 tetap bernama `Kas Operasional {runId}`
29. Admin A mengirim Create dengan Account Code `kas-{runId}`, Account Name `Kas Kecil Dua {runId}`, Account Function `Asset Cost`
30. Verifikasi permintaan ditolak dengan alasan `Account code already exists` karena perbedaan huruf besar-kecil tidak membuat kode berbeda
31. Admin A mengirim Create dengan Account Code `" KAS-{runId} "`, Account Name `Kas Kecil Tiga {runId}`, Account Function `Asset Cost`
32. Verifikasi permintaan ditolak dengan alasan `Account code already exists` karena kode dibandingkan setelah trim
33. Admin A mengirim Create dengan Account Code `PTG-{runId}`, Account Name `Piutang Usaha Pusat {runId}`, Account Function `Asset Cost`
34. Verifikasi akun dengan Account Code `PTG-{runId}` diterima dan tersimpan di client aktor, karena keunikan hanya berlaku di dalam satu client dan DU-150-5 ada di client lain
35. Verifikasi daftar akun client aktor dengan Account Code `KAS-{runId}` memuat tepat satu akun, tanpa membedakan huruf besar-kecil

### Dua admin membuat Account Code yang sama serentak
36. Admin A dan Admin B secara serentak mengirim Create dengan Account Code `SRN-{runId}`, Account Name `Kas Serentak {runId}`, Account Function `Asset Cost`
37. Verifikasi tepat satu dari kedua permintaan berhasil dan yang lain ditolak dengan alasan `Account code already exists`
38. Verifikasi daftar akun client aktor dengan Account Code `SRN-{runId}` memuat tepat satu akun

### Setiap akun tersimpan dengan tepat satu dari tujuh Account Function
39. Admin A mengirim Create dengan Account Code `FGD-{runId}`, Account Name `Keuntungan Pelepasan Aset {runId}`, Account Function `Gain on Disposal`
40. Verifikasi akun dengan Account Code `FGD-{runId}` tersimpan dengan tepat satu Account Function, yaitu `Gain on Disposal`
41. Admin A mengirim Create dengan Account Code `FLD-{runId}`, Account Name `Kerugian Pelepasan Aset {runId}`, Account Function `Loss on Disposal`
42. Verifikasi akun dengan Account Code `FLD-{runId}` tersimpan dengan tepat satu Account Function, yaitu `Loss on Disposal`
43. Admin A mengirim Create dengan Account Code `FCO-{runId}`, Account Name `Beban Perbaikan Dikapitalisasi {runId}`, Account Function `Capitalization Offset`
44. Verifikasi akun dengan Account Code `FCO-{runId}` tersimpan dengan tepat satu Account Function, yaitu `Capitalization Offset`
45. Admin A mengirim Create dengan Account Code `FDP-{runId}`, Account Name `Kliring Hasil Pelepasan {runId}`, Account Function `Disposal Proceeds`
46. Verifikasi akun dengan Account Code `FDP-{runId}` tersimpan dengan tepat satu Account Function, yaitu `Disposal Proceeds`
47. Verifikasi akun dengan Account Code `BE150-LIMIT-A15` tersimpan dengan tepat satu Account Function, yaitu `Asset Cost`
48. Verifikasi akun dengan Account Code `LST-{runId}` tersimpan dengan tepat satu Account Function, yaitu `Depreciation Expense`
49. Verifikasi akun dengan Account Code `NM120-{runId}` tersimpan dengan tepat satu Account Function, yaitu `Accumulated Depreciation`

### Payload dan markup pada Account Name tersimpan sebagai teks
50. Admin A mengirim Create dengan Account Code `XSS-{runId}`, Account Name `<script>alert(1)</script> {runId}`, Account Function `Asset Cost`
51. Verifikasi akun dengan Account Code `XSS-{runId}` tersimpan dengan Account Name persis `<script>alert(1)</script> {runId}` sebagai teks
52. Admin A mengirim Create dengan Account Code `SQL-{runId}`, Account Name `' OR '1'='1 {runId}`, Account Function `Asset Cost`
53. Verifikasi akun dengan Account Code `SQL-{runId}` tersimpan dengan Account Name persis `' OR '1'='1 {runId}`, dan akun DU-150-1 tetap bernama `Kas Operasional {runId}`
54. Admin A mengirim Create dengan Account Code `NSQ-{runId}`, Account Name `{"$ne": null} {runId}`, Account Function `Asset Cost`
55. Verifikasi akun dengan Account Code `NSQ-{runId}` tersimpan dengan Account Name persis `{"$ne": null} {runId}`
56. Admin A mengirim Create dengan Account Code `MRK-{runId}`, Account Name `<b>Kas Kecil</b> {runId}`, Account Function `Asset Cost`
57. Verifikasi akun dengan Account Code `MRK-{runId}` tersimpan dengan Account Name persis `<b>Kas Kecil</b> {runId}` sebagai teks
### Account Code berisi garis bawah dan titik diterima
58. Admin A mengirim Create dengan Account Code `BNK_{runId}`, Account Name `Rekening Bank Operasional {runId}`, Account Function `Asset Cost`
59. Verifikasi akun dengan Account Code `BNK_{runId}` diterima dan tersimpan, karena `_` termasuk karakter yang diizinkan
60. Admin A mengirim Create dengan Account Code `BNK.{runId}`, Account Name `Rekening Bank Cadangan {runId}`, Account Function `Asset Cost`
61. Verifikasi akun dengan Account Code `BNK.{runId}` diterima dan tersimpan, karena `.` termasuk karakter yang diizinkan

### Last Used in Journal tidak bisa diisi lewat Create langsung
62. Admin A mengirim Create dengan Account Code `LUJ-{runId}`, Account Name `Kas Periode Jurnal {runId}`, Account Function `Asset Cost`, dan Last Used in Journal `Oct 2026`
63. Verifikasi permintaan itu tidak menghasilkan akun ber-Last Used in Journal `Oct 2026`: akun dengan Account Code `LUJ-{runId}` tidak ada, atau ada dengan Last Used in Journal kosong
64. Admin A mengirim Create dengan Account Code `LUK-{runId}`, Account Name `Kas Tanpa Periode {runId}`, Account Function `Asset Cost`
65. Verifikasi akun dengan Account Code `LUK-{runId}` tersimpan dengan Last Used in Journal kosong

### Account Name dengan karakter non-ASCII disimpan apa adanya
66. Admin A mengirim Create dengan Account Code `NAS-{runId}`, Account Name `Café Ünïcode 北京 {runId}`, Account Function `Asset Cost`
67. Verifikasi akun dengan Account Code `NAS-{runId}` diterima dan tersimpan dengan Account Name persis `Café Ünïcode 北京 {runId}`, tanpa karakter non-ASCII yang diubah atau dibuang
