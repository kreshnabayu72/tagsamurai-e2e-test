---
id: TC-FA-FASVC-E2E-011-inactivate-activate-status
title: "Inactivate lalu Activate: Status, Badge, dan Status Tujuan yang Sudah Tercapai"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FASVC-03.k1", "F-FASVC-03.k4", "ST-FASVC-02", "RS-FASVC-03", "EB-FB-1@inactivate-service-center", "EB-FB-1@activate-service-center"]
smoke: []
dependsOn: []
trace:
  "F-FASVC-03.k1": [2, 7, 10, 19]
  "F-FASVC-03.k4": [16, 19]
  "ST-FASVC-02": 7
  "RS-FASVC-03": [22, 27, 29, 32, 38, 40, 43]
  "EB-FB-1@inactivate-service-center": 6
  "EB-FB-1@activate-service-center": 15
anchor: []
coverage:
  web: automated
---

# Inactivate lalu Activate: Status, Badge, dan Status Tujuan yang Sudah Tercapai

## Prerequisites
- Aktor: Total Control. Aktor lain: Total Control B (DU-011-3), yang mengubah status di sesi lain.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-011-1: Service Center `Vendor Siklus {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Seremban {runId}`, Company phone `+60 6555010101`.
  - DU-011-2: Service Center `Vendor Serentak {runId}`, Status `Active`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Miri {runId}`, Company phone `+60 8555020202`.
  - DU-011-3: User `Admin Kedua {runId}`, Role `Total Control`, cakupan Group `All groups`.
  - DU-011-4: Service Center `Vendor Terpakai {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Ipoh {runId}`, Company phone `+60 5555030303`, Usage `1 Schedule`.
  - DU-011-5: Service Center `Vendor Tanpa Group {runId}`, Status `Inactive`, Service type `Repair`, Available to `(kosong)`, Country `Malaysia`, City `Kota Bharu {runId}`, Company phone `+60 9555040404`.

## Test Steps

### Inactivate mengubah status dan badge
1. Ketik Search `Vendor Siklus {runId}`, tekan Enter
2. Verifikasi baris `Vendor Siklus {runId}` tampil dengan Status `Active`
3. Klik `⋯` pada baris `Vendor Siklus {runId}`
4. Klik `Inactivate`
5. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
6. Verifikasi toast `Success, Vendor Siklus {runId} has been inactivated.` tampil
7. Verifikasi baris `Vendor Siklus {runId}` tetap tampil di tabel dengan Status `Inactive`
8. Klik `[Changelog]`
9. Ketik Search `Vendor Siklus {runId}`, tekan Enter
10. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Inactivated`, Field `Status`, Old Value `Active`, dan New Value `Inactive`
11. Klik ikon close pada modal `Changelog: Service Center`

### Activate mengembalikan status dan badge
12. Klik `⋯` pada baris `Vendor Siklus {runId}`
13. Klik `Activate`
14. Klik `[Activate]` pada dialog `Activate Service Center`
15. Verifikasi toast `Success, Vendor Siklus {runId} has been activated.` tampil
16. Verifikasi baris `Vendor Siklus {runId}` tampil dengan Status `Active`
17. Klik `[Changelog]`
18. Ketik Search `Vendor Siklus {runId}`, tekan Enter
19. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Activated`, Field `Status`, Old Value `Inactive`, dan New Value `Active`
20. Klik ikon close pada modal `Changelog: Service Center`

### Inactivate saat Service Center sudah dinonaktifkan sesi lain
21. Ganti isi kotak search dengan `Vendor Serentak {runId}`, tekan Enter
22. Verifikasi baris `Vendor Serentak {runId}` tampil dengan Status `Active`
23. Klik `⋯` pada baris `Vendor Serentak {runId}`
24. Klik `Inactivate`
25. Total Control B menginaktifkan Service Center `Vendor Serentak {runId}`
26. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
27. Verifikasi toast `Success, Vendor Serentak {runId} has been inactivated.` tidak tampil
28. Muat ulang halaman
29. Verifikasi baris `Vendor Serentak {runId}` tampil dengan Status `Inactive`
30. Klik `[Changelog]`
31. Ketik Search `Vendor Serentak {runId}`, tekan Enter
32. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Inactivated` dan Field `Status`
33. Klik ikon close pada modal `Changelog: Service Center`

### Activate saat Service Center sudah diaktifkan sesi lain
34. Klik `⋯` pada baris `Vendor Serentak {runId}`
35. Klik `Activate`
36. Total Control B mengaktifkan Service Center `Vendor Serentak {runId}`
37. Klik `[Activate]` pada dialog `Activate Service Center`
38. Verifikasi toast `Success, Vendor Serentak {runId} has been activated.` tidak tampil
39. Muat ulang halaman
40. Verifikasi baris `Vendor Serentak {runId}` tampil dengan Status `Active`
41. Klik `[Changelog]`
42. Ketik Search `Vendor Serentak {runId}`, tekan Enter
43. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Activated` dan Field `Status`
44. Klik ikon close pada modal `Changelog: Service Center`
