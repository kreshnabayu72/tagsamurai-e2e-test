---
id: TC-FA-FACO-E2E-095-format-tanggal-dep-general-settings
title: "Perubahan Date Format dan Time Format tercermin di Last Updated dan Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [EB-XM-1]
smoke: []
dependsOn: ["Global Settings > General Settings: Date Format dan Time Format"]
trace:
  EB-XM-1: [9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 75, 77]
coverage:
  web: automated
---
# Perubahan Date Format dan Time Format tercermin di Last Updated dan Changelog

## Prerequisites
- Aktor: Admin dengan role Total Control pada entitas khusus DU-095-1, yang hanya dipakai spec ini dan tidak dipakai spec lain.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-095-1: entitas khusus `Entitas Format Tanggal {runId}` dengan Date Format `dd/MM/yy`, Time Format `24h`, dan Time Zone bawaan General Settings; seluruh data dan setting di dalamnya hanya dipakai spec ini.
  - DU-095-2: Account Code `FMT1-{runId}`, Account Name `Format Probe Cost {runId}`, Account Function `Asset Cost`, dibuat oleh spec ini lewat `[+ Account]` di entitas DU-095-1.
  - DU-095-3: Date Format `M/d/yy`.
  - DU-095-4: Date Format `dd MMM yy`.
  - DU-095-5: Date Format `DDD, MMM dd, yy`.
  - DU-095-6: Date Format `DDD, MMM dd, yyyy`.
  - DU-095-7: Time Format `12h`.
  - DU-095-8: Time Zone `Asia/Tokyo`.

## Test Steps

### Nilai default Date Format dan Time Format tampil di Last Updated dan Changelog
1. Klik `[+ Account]`
2. Isi Account Code `FMT1-{runId}`
3. Isi Account Name `Format Probe Cost {runId}`
4. Pilih `Asset Cost` pada field Account Function
5. Klik `[Submit]`
6. Ketik Search `FMT1-{runId}`, tekan Enter
7. Klik header kolom Actions (`⋯`) pada tabel
8. Centang `Last Updated` pada panel Column Visibility
9. Verifikasi Last Updated baris `FMT1-{runId}` ditulis dengan pola tanggal `dd/MM/yy` diikuti waktu 24 jam, misalnya `17/06/26, 09:42` (contoh, bukan nilai tetap)
10. Klik ikon `Changelog` di toolbar
11. Verifikasi Date baris Create akun `FMT1-{runId}` di modal Changelog ditulis dengan pola tanggal `dd/MM/yy` diikuti waktu 24 jam, misalnya `17/06/26, 09:42` (contoh, bukan nilai tetap)
12. Klik `✕` pada modal Changelog

### Date Format diubah menjadi `M/d/yy` dan tercermin di Last Updated dan Changelog
13. Buka Global Settings > General Settings
14. Pilih Date Format `M/d/yy`
15. Klik tombol simpan pada General Settings
16. Buka Settings > Accounting > Chart of Accounts
17. Muat ulang halaman
18. Ketik Search `FMT1-{runId}`, tekan Enter
19. Verifikasi Last Updated baris `FMT1-{runId}` ditulis dengan pola tanggal `M/d/yy` diikuti waktu 24 jam
20. Klik ikon `Changelog` di toolbar
21. Verifikasi Date baris Create akun `FMT1-{runId}` di modal Changelog ditulis dengan pola tanggal `M/d/yy` diikuti waktu 24 jam
22. Klik `✕` pada modal Changelog

### Date Format diubah menjadi `dd MMM yy` dan tercermin di Last Updated dan Changelog
23. Buka Global Settings > General Settings
24. Pilih Date Format `dd MMM yy`
25. Klik tombol simpan pada General Settings
26. Buka Settings > Accounting > Chart of Accounts
27. Muat ulang halaman
28. Ketik Search `FMT1-{runId}`, tekan Enter
29. Verifikasi Last Updated baris `FMT1-{runId}` ditulis dengan pola tanggal `dd MMM yy` diikuti waktu 24 jam
30. Klik ikon `Changelog` di toolbar
31. Verifikasi Date baris Create akun `FMT1-{runId}` di modal Changelog ditulis dengan pola tanggal `dd MMM yy` diikuti waktu 24 jam
32. Klik `✕` pada modal Changelog

### Date Format diubah menjadi `DDD, MMM dd, yy` dan tercermin di Last Updated dan Changelog
33. Buka Global Settings > General Settings
34. Pilih Date Format `DDD, MMM dd, yy`
35. Klik tombol simpan pada General Settings
36. Buka Settings > Accounting > Chart of Accounts
37. Muat ulang halaman
38. Ketik Search `FMT1-{runId}`, tekan Enter
39. Verifikasi Last Updated baris `FMT1-{runId}` ditulis dengan pola tanggal `DDD, MMM dd, yy` diikuti waktu 24 jam
40. Klik ikon `Changelog` di toolbar
41. Verifikasi Date baris Create akun `FMT1-{runId}` di modal Changelog ditulis dengan pola tanggal `DDD, MMM dd, yy` diikuti waktu 24 jam
42. Klik `✕` pada modal Changelog

### Date Format diubah menjadi `DDD, MMM dd, yyyy` dan tercermin di Last Updated dan Changelog
43. Buka Global Settings > General Settings
44. Pilih Date Format `DDD, MMM dd, yyyy`
45. Klik tombol simpan pada General Settings
46. Buka Settings > Accounting > Chart of Accounts
47. Muat ulang halaman
48. Ketik Search `FMT1-{runId}`, tekan Enter
49. Verifikasi Last Updated baris `FMT1-{runId}` ditulis dengan pola tanggal `DDD, MMM dd, yyyy` diikuti waktu 24 jam
50. Klik ikon `Changelog` di toolbar
51. Verifikasi Date baris Create akun `FMT1-{runId}` di modal Changelog ditulis dengan pola tanggal `DDD, MMM dd, yyyy` diikuti waktu 24 jam
52. Klik `✕` pada modal Changelog

### Time Format 12h tercermin di Last Updated dan Changelog
53. Buka Global Settings > General Settings
54. Pilih Time Format `12h`
55. Klik tombol simpan pada General Settings
56. Buka Settings > Accounting > Chart of Accounts
57. Muat ulang halaman
58. Ketik Search `FMT1-{runId}`, tekan Enter
59. Verifikasi Last Updated baris `FMT1-{runId}` ditulis dengan pola tanggal `DDD, MMM dd, yyyy` diikuti waktu 12 jam dengan penanda AM atau PM
60. Klik ikon `Changelog` di toolbar
61. Verifikasi Date baris Create akun `FMT1-{runId}` di modal Changelog ditulis dengan pola tanggal `DDD, MMM dd, yyyy` diikuti waktu 12 jam dengan penanda AM atau PM
62. Klik `✕` pada modal Changelog

### Time Zone non-default menggeser waktu di Last Updated dan Changelog
63. Buka Settings > Accounting > Chart of Accounts
64. Ketik Search `FMT1-{runId}`, tekan Enter
65. Catat jam dan menit pada Last Updated baris `FMT1-{runId}`
66. Klik ikon `Changelog` di toolbar
67. Catat jam dan menit pada Date baris Create akun `FMT1-{runId}` di modal Changelog
68. Klik `✕` pada modal Changelog
69. Buka Global Settings > General Settings
70. Pilih Time Zone `Asia/Tokyo`
71. Klik tombol simpan pada General Settings
72. Buka Settings > Accounting > Chart of Accounts
73. Muat ulang halaman
74. Ketik Search `FMT1-{runId}`, tekan Enter
75. Verifikasi jam pada Last Updated baris `FMT1-{runId}` bergeser sebesar selisih UTC offset antara Time Zone `Asia/Tokyo` dan Time Zone sebelumnya, dengan menit yang sama seperti yang dicatat
76. Klik ikon `Changelog` di toolbar
77. Verifikasi jam pada Date baris Create akun `FMT1-{runId}` di modal Changelog bergeser sebesar selisih UTC offset yang sama, dengan menit yang sama seperti yang dicatat
78. Klik `✕` pada modal Changelog
