---
id: TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal
title: "Export Journal selesai saat form Edit atau dialog Delete terbuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [D-16, "§[F-FACO-02] Edit Account#r4", "§[F-FACO-02] Edit Account#r11", "§[F-FACO-02] Edit Account#r12", "§[F-FACO-02] Edit Account#r13", "§[F-FACO-02] Edit Account#r14", "§[F-FACO-05] Delete Account#r15", "§9.4.2#r8", "§9.4.2#r22"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  D-16: [8, 11]
  "§[F-FACO-02] Edit Account#r4": [8, 36]
  "§[F-FACO-02] Edit Account#r11": [8, 9]
  "§[F-FACO-02] Edit Account#r12": [11, 12, 14, 16, 17]
  "§[F-FACO-02] Edit Account#r13": [25, 27]
  "§[F-FACO-02] Edit Account#r14": [34, 35, 36, 37, 40]
  "§[F-FACO-05] Delete Account#r15": [48, 49, 50, 51]
  "§9.4.2#r8": [8, 36]
  "§9.4.2#r22": [48, 55]
anchor: [23, 45]
coverage:
  web: automated
---

# Export Journal selesai saat form Edit atau dialog Delete terbuka

## Prerequisites
- Aktor: Admin A dengan role Total Control, cakupan seluruh client. Pemicu perubahan: Admin B dengan role Total Control, cakupan seluruh client, yang menjalankan Export Journal.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-078-1: Account Code `LKB1-{runId}`, Account Name `Rental Equipment Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun DU-078-1 pada bullet dialog adalah `LKB1-{runId} – Rental Equipment Cost {runId}`, dari Account Code `LKB1-{runId}` dan Account Name `Rental Equipment Cost {runId}`.
  - DU-078-2: perubahan yang dikirim Admin A pada form Edit DU-078-1: Account Code `LKB1X-{runId}` dan Account Name `Rental Equipment Cost Revised {runId}`.
  - DU-078-3: Account Code `LKB2-{runId}`, Account Name `Warehouse Racking Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-078-4: Account Name baru untuk DU-078-3: `Warehouse Racking Cost Revised {runId}`.
  - DU-078-5: Account Code `LKB3-{runId}`, Account Name `Dock Leveler Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun DU-078-5 pada bullet dialog adalah `LKB3-{runId} – Dock Leveler Cost {runId}`, dari Account Code `LKB3-{runId}` dan Account Name `Dock Leveler Cost {runId}`.
- Kondisi:
  - Setiap Export Journal yang dijalankan Admin B di spec ini memakai periode jurnal `M0 − 2 bulan` dan memuat akun yang disebut pada langkahnya.

## Test Steps

### Save Edit yang mengubah field terkunci ditolak saat Export Journal selesai sesudah form dibuka
1. Ketik Search `LKB1-{runId}`, tekan Enter
2. Klik `⋯` pada baris `LKB1-{runId}`
3. Klik `Edit`
4. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB1-{runId}`, dan export selesai saat form Edit masih terbuka
5. Ganti isi Account Code dengan `LKB1X-{runId}`
6. Ganti isi Account Name dengan `Rental Equipment Cost Revised {runId}`
7. Klik `[Save]`
8. Verifikasi dialog `Cannot Save Account` tampil dengan bullet `LKB1-{runId} – Rental Equipment Cost {runId}`
9. Verifikasi tidak ada toast yang tampil bersama dialog `Cannot Save Account`
10. Klik `[OK]`
11. Verifikasi field Account Code Disabled dengan nilai tersimpan `LKB1-{runId}`
12. Verifikasi field Account Function Disabled dengan nilai tersimpan `Capitalization Offset`
13. Arahkan kursor ke field Account Code
14. Verifikasi alasan `Account Code can't be changed because this account was used in a journal in [Month Year]. Create a new account if needed.` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Code yang Disabled
15. Arahkan kursor ke field Account Function
16. Verifikasi alasan `Account Function can't be changed because this account was used in a journal in [Month Year].` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Function yang Disabled
17. Verifikasi field Account Name tetap berisi `Rental Equipment Cost Revised {runId}`
18. Klik `✕` pada form Edit, lalu klik `[Leave]` pada dialog Unsaved Changes
19. Muat ulang halaman
20. Ketik Search `LKB1-{runId}`, tekan Enter
21. Klik ikon `Changelog` di toolbar
22. Ketik Search `LKB1-{runId}`, tekan Enter
23. Verifikasi baris Changelog dengan Field `Last Used in Journal` untuk Account Code `LKB1-{runId}` tampil
24. Ganti isi kotak search dengan `LKB1X-{runId}`, tekan Enter
25. Verifikasi tidak ada baris Changelog dengan Account Code `LKB1X-{runId}`
26. Klik `✕` pada modal Changelog
27. Verifikasi baris `LKB1-{runId}` tampil dengan Account Name `Rental Equipment Cost {runId}`

### Save Edit yang hanya mengubah field tidak terkunci berhasil walau kunci berubah
28. Ganti isi kotak search dengan `LKB2-{runId}`, tekan Enter
29. Klik `⋯` pada baris `LKB2-{runId}`
30. Klik `Edit`
31. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB2-{runId}`, dan export selesai saat form Edit masih terbuka
32. Ganti isi Account Name dengan `Warehouse Racking Cost Revised {runId}`
33. Klik `[Save]`
34. Verifikasi toast `Success, account has been updated.` tampil
35. Verifikasi form Edit tertutup
36. Verifikasi baris `LKB2-{runId}` tampil dengan Account Name `Warehouse Racking Cost Revised {runId}`
37. Verifikasi Last Used in Journal baris `LKB2-{runId}` bernilai periode `M0 − 2 bulan` yang ditulis `MMM YYYY`, tanpa muat ulang halaman
38. Klik ikon `Changelog` di toolbar
39. Ganti isi kotak search dengan `LKB2-{runId}`, tekan Enter
40. Verifikasi baris Changelog dengan Action `Edit`, Field `Account Name`, Old Value `Warehouse Racking Cost {runId}`, dan New Value `Warehouse Racking Cost Revised {runId}` tampil
41. Klik `✕` pada modal Changelog

### Delete ditolak saat Export Journal selesai sesudah dialog dibuka
42. Ganti isi kotak search dengan `LKB3-{runId}`, tekan Enter
43. Klik `⋯` pada baris `LKB3-{runId}`
44. Klik `Delete`
45. Verifikasi dialog `Delete Account` tampil, yaitu akun belum diblokir saat dialog dibuka
46. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB3-{runId}`, dan export selesai saat dialog Delete masih terbuka
47. Klik `[Delete]`
48. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `LKB3-{runId} – Dock Leveler Cost {runId}`
49. Verifikasi kalimat `This account was last used in a journal in [Month Year]. Deleting it may break historical records.` tampil dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`
50. Verifikasi kalimat saran `Deactivate it instead.` tampil, karena akun masih Active dan Used By `0`
51. Verifikasi tidak ada toast yang tampil bersama dialog `Cannot Delete Account`
52. Klik `[OK]`
53. Muat ulang halaman
54. Ketik Search `LKB3-{runId}`, tekan Enter
55. Verifikasi baris `LKB3-{runId}` masih tampil di tabel
