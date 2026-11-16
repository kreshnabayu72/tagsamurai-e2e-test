---
id: TC-FA-FACO-E2E-075-last-used-in-journal-dep-export-journal
title: "Export Journal memajukan Last Used in Journal dan tidak memundurkannya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [F-FACO-08, FACO-LOGIC-07a, FACO-LOGIC-07b, "§4.1.1#r6", "§4.1.1#b2", "§8.1#p2", "§[F-FACO-08] Update Last Used in Journal#p1", "§[F-FACO-08] Update Last Used in Journal#r1", "§[F-FACO-08] Update Last Used in Journal#r2", "§9.4.2#r23", "§9.4.2#r24", "§9.7#r29", L-10]
smoke: [L-10]
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  F-FACO-08: [2, 6, 17, 26]
  FACO-LOGIC-07a: 6
  FACO-LOGIC-07b: [26, 33]
  "§4.1.1#r6": [6, 8, 19, 20, 28, 35, 38]
  "§4.1.1#b2": [6, 11]
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
- Aktor: Admin dengan role Total Control bernama lengkap `Sari Kusuma {runId}` (DU-075-2), yang membuka tabel Chart of Accounts; Admin lain dengan role Total Control bernama lengkap `Budi Santoso {runId}` (DU-075-5), yang menjalankan Export Journal yang memajukan nilai; `Sari Kusuma {runId}` juga menjalankan Export Journal yang tidak memajukan nilai; pada entitas khusus DU-075-4 yang tidak dipakai spec lain.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-075-1: Account Code `LUJ1-{runId}`, Account Name `Equipment Cost Journal {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `1`, Last Used in Journal `—`, dipakai DU-075-3, ada di entitas khusus DU-075-4.
  - DU-075-2: User `Sari Kusuma {runId}`, Access Level `Total Control`, cakupan seluruh client entitas khusus DU-075-4, aktor yang membuka tabel spec ini, dan pengekspor Export Journal yang tidak memajukan nilai.
  - DU-075-5: User `Budi Santoso {runId}`, Access Level `Total Control`, cakupan seluruh client entitas khusus DU-075-4, pengekspor Export Journal yang memajukan nilai.
  - DU-075-3: Asset Class `Kelas Ekspor Jurnal {runId}`, Status `Active`; Asset Cost `LUJ1-{runId}`.
  - DU-075-4: entitas khusus `Entitas Hover Journal {runId}` dengan Date Format `dd MMM yy` dan Time Format `12h`; seluruh data dan setting di dalamnya hanya dipakai spec ini.
- Kondisi:
  - Entitas khusus DU-075-4 memakai Date Format `dd MMM yy` dan Time Format `12h`, format non-bawaan, dan nilai itu tidak berubah selama spec ini.
  - Akun DU-075-1 ikut dalam berkas setiap Export Journal yang dijalankan di spec ini, karena Asset Class DU-075-3 memakainya pada Asset Cost dan pemetaan itu tidak berubah selama spec ini.
  - Periode jurnal yang diekspor berurutan: `Jun 2026` oleh `Budi Santoso {runId}`, `Aug 2026` oleh `Budi Santoso {runId}`, `Jul 2026` oleh `Sari Kusuma {runId}`, lalu `Aug 2026` oleh `Sari Kusuma {runId}`.
  - Entri log L-10 (Changelog dan sumber hover Last Used in Journal) ditulis sesudah commit secara best-effort; nilai Last Used in Journal itu sendiri tersimpan saat commit.

## Test Steps

### Export periode pertama mengisi Last Used in Journal dari kosong
1. Ketik Search `LUJ1-{runId}`, tekan Enter
2. Verifikasi Last Used in Journal baris `LUJ1-{runId}` bernilai `—`
3. `Budi Santoso {runId}` menjalankan Export Journal untuk periode `Jun 2026` hingga selesai dan memuat akun `LUJ1-{runId}`
4. Muat ulang halaman
5. Ketik Search `LUJ1-{runId}`, tekan Enter
6. Verifikasi Last Used in Journal baris `LUJ1-{runId}` bernilai `Jun 2026`, yaitu periode jurnal yang diekspor dan bukan tanggal export
7. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
8. Verifikasi hover memuat `Last exported [Date Time] by [User Name]`, dengan [Date Time] menurut Date Format `dd MMM yy` dan Time Format `12h`, dan [User Name] berupa nama lengkap pengekspor `Budi Santoso {runId}`

### Changelog mencatat periode pertama
9. Klik ikon `Changelog` di toolbar
10. Ketik Search `LUJ1-{runId}`, tekan Enter
11. Verifikasi baris Changelog dengan Action `Edit`, Account Code `LUJ1-{runId}`, Field `Last Used in Journal`, Old Value `—`, dan New Value `Jun 2026` tampil
12. Klik `✕` pada modal Changelog

### Export periode yang lebih baru memajukan nilai
13. Waktu berlalu sampai menit berganti
14. `Budi Santoso {runId}` menjalankan Export Journal untuk periode `Aug 2026` hingga selesai dan memuat akun `LUJ1-{runId}`
15. Muat ulang halaman
16. Ketik Search `LUJ1-{runId}`, tekan Enter
17. Verifikasi Last Used in Journal baris `LUJ1-{runId}` bernilai `Aug 2026`
18. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
19. Verifikasi teks hover berbeda dari teks hover pada langkah 8
20. Verifikasi [Date Time] pada hover adalah waktu Export Journal periode `Aug 2026`, yaitu menit yang lebih akhir daripada [Date Time] pada langkah 8, dengan [User Name] berupa nama lengkap pengekspor `Budi Santoso {runId}`

### Export ulang periode yang lebih lama tidak memundurkan nilai
21. Catat teks hover sel Last Used in Journal baris `LUJ1-{runId}`
22. Waktu berlalu sampai menit berganti
23. `Sari Kusuma {runId}` menjalankan Export Journal untuk periode `Jul 2026` hingga selesai dan memuat akun `LUJ1-{runId}`
24. Muat ulang halaman
25. Ketik Search `LUJ1-{runId}`, tekan Enter
26. Verifikasi Last Used in Journal baris `LUJ1-{runId}` tetap bernilai `Aug 2026`
27. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
28. Verifikasi teks hover sama dengan teks yang dicatat pada langkah 21, termasuk [User Name] `Budi Santoso {runId}` sebagai pengekspor yang memajukan nilai walau Export Journal terakhir dijalankan `Sari Kusuma {runId}`

### Export ulang periode yang sama tidak mengubah nilai
29. Waktu berlalu sampai menit berganti
30. `Sari Kusuma {runId}` menjalankan Export Journal untuk periode `Aug 2026` hingga selesai dan memuat akun `LUJ1-{runId}`
31. Muat ulang halaman
32. Ketik Search `LUJ1-{runId}`, tekan Enter
33. Verifikasi Last Used in Journal baris `LUJ1-{runId}` tetap bernilai `Aug 2026`
34. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
35. Verifikasi teks hover sama dengan teks yang dicatat pada langkah 21, termasuk [User Name] `Budi Santoso {runId}` sebagai pengekspor yang memajukan nilai walau Export Journal terakhir dijalankan `Sari Kusuma {runId}`

### Hover Last Used in Journal mengikuti Date Format dan Time Format non-bawaan entitas
36. Ketik Search `LUJ1-{runId}`, tekan Enter
37. Arahkan kursor ke sel Last Used in Journal baris `LUJ1-{runId}`
38. Verifikasi [Date Time] pada hover `Last exported [Date Time] by [User Name]` ditulis dengan pola tanggal `dd MMM yy` diikuti waktu 12 jam
