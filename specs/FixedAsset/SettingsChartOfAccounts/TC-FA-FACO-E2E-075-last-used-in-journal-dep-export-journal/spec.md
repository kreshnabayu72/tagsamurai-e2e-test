---
id: TC-FA-FACO-E2E-075-last-used-in-journal-dep-export-journal
title: "Export Journal memajukan Last Used in Journal dan tidak memundurkannya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [F-FACO-08, FACO-LOGIC-07a, FACO-LOGIC-07b, "§4.1.1#r6", "§4.1.1#b3", "§8.1#p2", "§[F-FACO-08] Update Last Used in Journal#p1", "§[F-FACO-08] Update Last Used in Journal#r1", "§[F-FACO-08] Update Last Used in Journal#r2", "§9.4.2#r23", "§9.4.2#r24", "§9.7#r29", L-10]
smoke: [L-10]
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  F-FACO-08: [2, 6, 17, 26]
  FACO-LOGIC-07a: 6
  FACO-LOGIC-07b: [26, 33]
  "§4.1.1#r6": [6, 8, 19, 20, 28, 35]
  "§4.1.1#b3": [6, 11]
  "§8.1#p2": 11
  "§[F-FACO-08] Update Last Used in Journal#p1": 6
  "§[F-FACO-08] Update Last Used in Journal#r1": [6, 17]
  "§[F-FACO-08] Update Last Used in Journal#r2": [26, 33]
  "§9.4.2#r23": 17
  "§9.4.2#r24": [26, 33]
  "§9.7#r29": 6
  L-10: 11
coverage:
  web: automated
---

# Export Journal memajukan Last Used in Journal dan tidak memundurkannya

## Prerequisites
- Aktor: Admin dengan role Total Control bernama lengkap `Sari Kusuma {runId}` (DU-075-2), yang juga menjalankan Export Journal.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-075-1: Account Code `LUJ1-{runId}`, Account Name `Equipment Cost Journal {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—`, ada di entitas aktor.
  - DU-075-2: User `Sari Kusuma {runId}`, Access Level `Total Control`, cakupan seluruh client, aktor spec ini dan pengekspor pada setiap Export Journal.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - Akun DU-075-1 ikut dalam berkas setiap Export Journal yang dijalankan di spec ini.
  - Periode jurnal yang diekspor berurutan: `Jun 2026`, `Aug 2026`, `Jul 2026`, lalu `Aug 2026`.

## Test Steps

### Export periode pertama mengisi Last Used in Journal dari kosong
1. Ketik Search `LUJ1-{runId}`, tekan Enter
2. Verifikasi Last Used in Journal baris `LUJ1-{runId}` bernilai `—`
3. Export Journal untuk periode `Jun 2026` selesai dan memuat akun `LUJ1-{runId}`
4. Muat ulang halaman
5. Ketik Search `LUJ1-{runId}`, tekan Enter
6. Verifikasi Last Used in Journal baris `LUJ1-{runId}` bernilai `Jun 2026`, yaitu periode jurnal yang diekspor dan bukan tanggal export
7. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
8. Verifikasi hover memuat `Last exported [Date Time] by [User Name]`, dengan [Date Time] menurut Date Format `dd/MM/yy` dan Time Format `24h`, dan [User Name] berupa nama lengkap aktor pengekspor `Sari Kusuma {runId}`

### Changelog mencatat periode pertama
9. Klik ikon `Changelog` di toolbar
10. Ketik Search `LUJ1-{runId}`, tekan Enter
11. Verifikasi baris Changelog dengan Action `Edit`, Account Code `LUJ1-{runId}`, Field `Last Used in Journal`, Old Value `—`, dan New Value `Jun 2026` tampil
12. Klik `✕` pada modal Changelog

### Export periode yang lebih baru memajukan nilai
13. Waktu berlalu sampai menit berganti
14. Export Journal untuk periode `Aug 2026` selesai dan memuat akun `LUJ1-{runId}`
15. Muat ulang halaman
16. Ketik Search `LUJ1-{runId}`, tekan Enter
17. Verifikasi Last Used in Journal baris `LUJ1-{runId}` bernilai `Aug 2026`
18. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
19. Verifikasi teks hover berbeda dari teks hover pada langkah 8
20. Verifikasi [Date Time] pada hover adalah waktu Export Journal periode `Aug 2026`, yaitu menit yang lebih akhir daripada [Date Time] pada langkah 8, dengan [User Name] tetap `Sari Kusuma {runId}`

### Export ulang periode yang lebih lama tidak memundurkan nilai
21. Catat teks hover sel Last Used in Journal baris `LUJ1-{runId}`
22. Waktu berlalu sampai menit berganti
23. Export Journal untuk periode `Jul 2026` selesai dan memuat akun `LUJ1-{runId}`
24. Muat ulang halaman
25. Ketik Search `LUJ1-{runId}`, tekan Enter
26. Verifikasi Last Used in Journal baris `LUJ1-{runId}` tetap bernilai `Aug 2026`
27. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
28. Verifikasi teks hover sama dengan teks yang dicatat pada langkah 21

### Export ulang periode yang sama tidak mengubah nilai
29. Waktu berlalu sampai menit berganti
30. Export Journal untuk periode `Aug 2026` selesai dan memuat akun `LUJ1-{runId}`
31. Muat ulang halaman
32. Ketik Search `LUJ1-{runId}`, tekan Enter
33. Verifikasi Last Used in Journal baris `LUJ1-{runId}` tetap bernilai `Aug 2026`
34. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
35. Verifikasi teks hover sama dengan teks yang dicatat pada langkah 21
