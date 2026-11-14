---
id: TC-FA-FACO-E2E-026-bulk-deactivate
title: "Bulk Deactivate akun Active yang seluruhnya lolos guard"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-02", "F-FACO-04", "§4.1.1#p4", "§[F-FACO-04] Deactivate Account#b3", "§8.4#r3", "T-05"]
smoke: ["§8.4#r3", "T-05"]
dependsOn: []
trace:
  "D-02": [9, 22, 42]
  "F-FACO-04": [12, 26, 45]
  "§4.1.1#p4": [23, 25, 26, 31]
  "§[F-FACO-04] Deactivate Account#b3": [12, 26, 29, 30, 45]
  "§8.4#r3": [29, 30]
  "T-05": [11, 25]
anchor: [5, 17, 37, 44]
coverage:
  web: automated
---

# Bulk Deactivate akun Active yang seluruhnya lolos guard

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-026-1: akun Active dengan Account Code `GD-{runId}`, Account Name `Gain on Disposal Kantor Pusat {runId}`, Account Function `Gain on Disposal`, Used By `0`, Last Used in Journal `—`; Account Label `GD-{runId} – Gain on Disposal Kantor Pusat {runId}`.
  - DU-026-2: akun Active dengan Account Code `LD1-{runId}`, Account Name `Loss on Disposal Equipment {runId}`, Account Function `Loss on Disposal`, Used By `0`, Last Used in Journal `—`; Account Label `LD1-{runId} – Loss on Disposal Equipment {runId}`.
  - DU-026-3: akun Active dengan Account Code `LD2-{runId}`, Account Name `Loss on Disposal Vehicles {runId}`, Account Function `Loss on Disposal`, Used By `0`, Last Used in Journal `—`; Account Label `LD2-{runId} – Loss on Disposal Vehicles {runId}`.
  - DU-026-4: akun Active dengan Account Code `LD3-{runId}`, Account Name `Loss on Disposal Buildings {runId}`, Account Function `Loss on Disposal`, Used By `0`, Last Used in Journal `—`; Account Label `LD3-{runId} – Loss on Disposal Buildings {runId}`.
  - DU-026-5: akun Inactive dengan Account Code `LD4-{runId}`, Account Name `Loss on Disposal Furniture {runId}`, Account Function `Loss on Disposal`, Used By `0`, Last Used in Journal `—`; Account Label `LD4-{runId} – Loss on Disposal Furniture {runId}`.
  - DU-026-6: 12 akun Active dengan Account Code `DP{n}-{runId}`, Account Name `Disposal Proceeds Clearing Cabang Pusat Distribusi Nasional Wilayah Jawa Barat Unit {n} {runId}`, `{n}` dari 1 sampai 12, Account Function `Disposal Proceeds`, Used By `0`, Last Used in Journal `—`.

## Test Steps

### Bulk Deactivate satu akun
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon Filter pada toolbar
3. Pilih Function `Gain on Disposal` pada Filter Panel
4. Klik `[Apply]`
5. Verifikasi baris `GD-{runId}` tampil dengan Switch Status berstatus Active
6. Centang baris `GD-{runId}`
7. Klik `Bulk Action`
8. Klik `Deactivate`
9. Verifikasi dialog memuat bullet `GD-{runId} – Gain on Disposal Kantor Pusat {runId}`
10. Klik `[Deactivate]`
11. Verifikasi toast `Success, account has been deactivated.` tampil
12. Verifikasi Switch Status pada baris `GD-{runId}` berstatus Inactive

### Bulk Deactivate beberapa akun pada seleksi yang memuat akun Inactive
13. Klik ikon Filter pada toolbar
14. Klik `[Clear Field]`
15. Pilih Function `Loss on Disposal` pada Filter Panel
16. Klik `[Apply]`
17. Verifikasi baris `LD1-{runId}`, `LD2-{runId}`, `LD3-{runId}`, dan `LD4-{runId}` tampil
18. Centang baris `LD1-{runId}`
19. Klik `Select All (4 records)`
20. Klik `Bulk Action`
21. Klik `Deactivate`
22. Verifikasi dialog memuat bullet `LD1-{runId} – Loss on Disposal Equipment {runId}`, `LD2-{runId} – Loss on Disposal Vehicles {runId}`, dan `LD3-{runId} – Loss on Disposal Buildings {runId}`
23. Verifikasi dialog tidak memuat bullet `LD4-{runId} – Loss on Disposal Furniture {runId}`
24. Klik `[Deactivate]`
25. Verifikasi toast `Success, account has been deactivated.` tampil
26. Verifikasi Switch Status pada baris `LD1-{runId}`, `LD2-{runId}`, dan `LD3-{runId}` berstatus Inactive

### Satu entri Changelog per akun yang berhasil dinonaktifkan
27. Klik ikon Changelog pada toolbar
28. Ketik Search `{runId}`, tekan Enter
29. Verifikasi setiap akun `LD1-{runId}`, `LD2-{runId}`, dan `LD3-{runId}` memiliki tepat satu baris Changelog dengan Action `Edit` dan Field `Status`
30. Verifikasi baris-baris Field `Status` itu memuat Old Value `Active` dan New Value `Inactive`
31. Verifikasi tidak ada baris Changelog dengan Account Code `LD4-{runId}` dan Field `Status`
32. Klik `✕` pada modal Changelog

### Daftar dialog yang melebihi tampilan tetap memuat seluruh akun
33. Klik ikon Filter pada toolbar
34. Klik `[Clear Field]`
35. Pilih Function `Disposal Proceeds` pada Filter Panel
36. Klik `[Apply]`
37. Verifikasi baris `DP1-{runId}` tampil dengan Switch Status berstatus Active
38. Centang baris `DP1-{runId}`
39. Klik `Select All (12 records)`
40. Klik `Bulk Action`
41. Klik `Deactivate`
42. Verifikasi dialog Deactivate memuat 12 bullet dan seluruhnya dapat dijangkau pada daftar yang bergulir
43. Klik `[Deactivate]`
44. Verifikasi Switch Status pada baris `DP1-{runId}` berstatus Inactive
45. Verifikasi setiap baris dari 12 baris hasil Search dan Filter Panel berstatus Inactive
