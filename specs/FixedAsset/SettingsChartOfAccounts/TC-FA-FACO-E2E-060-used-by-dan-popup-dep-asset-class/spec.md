---
id: TC-FA-FACO-E2E-060-used-by-dan-popup-dep-asset-class
title: "Kolom Used By dan popup Used By menghitung Asset Class pemakai akun"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FACO-LOGIC-02a, FACO-LOGIC-02f, FACO-LOGIC-02g, FACO-LOGIC-02h, "§4.1.1#r5", "§4.1.4#p1", "§4.1.4#p2", "§4.1.4#p3", "§4.4#r4", "§4.6#b3"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  FACO-LOGIC-02a: [2, 4, 5]
  FACO-LOGIC-02f: [3, 18]
  FACO-LOGIC-02g: [2, 6]
  FACO-LOGIC-02h: 2
  "§4.1.1#r5": [2, 3, 4, 5, 6, 24, 25, 26, 29, 30, 34, 35, 39, 40, 41, 45]
  "§4.1.4#p1": [9, 17]
  "§4.1.4#p2": [10, 11]
  "§4.1.4#p3": [12, 13, 14, 50, 51]
  "§4.4#r4": 8
  "§4.6#b3": 8
anchor: []
coverage:
  web: automated
  android: automated
---

# Kolom Used By dan popup Used By menghitung Asset Class pemakai akun

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-060-1: Account Code `UBC-{runId}`, Account Name `Equipment Cost {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 3 Asset Class (DU-060-7, DU-060-8, DU-060-9).
  - DU-060-2: Account Code `UBG-{runId}`, Account Name `Gain and Loss on Disposal {runId}`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-060-7) pada field Gain on Disposal dan field Loss on Disposal.
  - DU-060-3: Account Code `UBA-{runId}`, Account Name `Accumulated Depreciation Equipment {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-060-7, DU-060-8).
  - DU-060-4: Account Code `UBE-{runId}`, Account Name `Depreciation Expense Equipment {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-060-7).
  - DU-060-5: Account Code `UBN-{runId}`, Account Name `Unused Account {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-060-6: Account Code `UBI-{runId}`, Account Name `Legacy Unused Account {runId}`, Account Function `Asset Cost`, Status Inactive, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-060-7: Asset Class `Delivery Vehicles {runId}` dengan 3 Asset Name; Asset Cost `UBC-{runId}`, Accumulated Depreciation `UBA-{runId}`, Depreciation Expense `UBE-{runId}`, Gain on Disposal `UBG-{runId}`, Loss on Disposal `UBG-{runId}`.
  - DU-060-8: Asset Class `Heavy Equipment {runId}` dengan 12 Asset Name; Asset Cost `UBC-{runId}`, Accumulated Depreciation `UBA-{runId}`.
  - DU-060-9: Asset Class `Office Equipment {runId}` berstatus Inactive dengan 1 Asset Name; Asset Cost `UBC-{runId}`.
  - Baris identitas popup yang diharapkan untuk DU-060-1 adalah `UBC-{runId} – Equipment Cost {runId} (3)`, dari Account Code, Account Name, dan jumlah Asset Class pemakai 3.
  - Bullet popup yang diharapkan untuk DU-060-1 adalah `Delivery Vehicles {runId} — 3 Asset Names`, `Heavy Equipment {runId} — 12 Asset Names`, dan `Office Equipment {runId} — 1 Asset Name`, dari nama Asset Class dan jumlah Asset Name-nya.
  - Baris identitas popup yang diharapkan untuk DU-060-2 adalah `UBG-{runId} – Gain and Loss on Disposal {runId} (1)`, dari Account Code, Account Name, dan jumlah Asset Class pemakai 1.
  - Urutan pembuatan Asset Class: DU-060-9 dibuat lebih dulu, lalu DU-060-8, lalu DU-060-7, sehingga urutan pembuatan berlawanan dengan urutan A-Z menurut nama.
  - Bullet popup yang diharapkan untuk DU-060-1 sesudah satu Asset Name di-Unassign dari DU-060-8 adalah `Heavy Equipment {runId} — 11 Asset Names`, dari jumlah Asset Name 12 dikurangi 1.

## Test Steps

### Used By menghitung Asset Class berbeda pada setiap field akun
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi Used By baris `UBC-{runId}` bernilai `3`
3. Verifikasi Used By baris `UBG-{runId}` bernilai `1`
4. Verifikasi Used By baris `UBA-{runId}` bernilai `2`
5. Verifikasi Used By baris `UBE-{runId}` bernilai `1`
6. Verifikasi Used By baris `UBI-{runId}` yang berstatus Inactive bernilai `0`

### Popup Used By memuat Asset Class pemakai akun
7. Klik angka Used By `3` pada baris `UBC-{runId}`
8. Verifikasi popup `Used By` untuk akun `UBC-{runId}` tampil
9. Verifikasi baris identitas `UBC-{runId} – Equipment Cost {runId} (3)` tampil pada popup
10. Verifikasi bullet pemakai berurutan A-Z: `Delivery Vehicles {runId}`, `Heavy Equipment {runId}`, `Office Equipment {runId}`
11. Verifikasi jumlah bullet pada popup `3`, sama dengan nilai Used By
12. Verifikasi bullet `Delivery Vehicles {runId} — 3 Asset Names` tampil
13. Verifikasi bullet `Heavy Equipment {runId} — 12 Asset Names` tampil
14. Verifikasi bullet `Office Equipment {runId} — 1 Asset Name` tampil
15. Klik `✕` pada popup Used By

### Asset Class yang merujuk akun lebih dari sekali dihitung satu kali
16. Klik angka Used By `1` pada baris `UBG-{runId}`
17. Verifikasi baris identitas `UBG-{runId} – Gain and Loss on Disposal {runId} (1)` tampil pada popup
18. Verifikasi jumlah bullet pada popup `1`
19. Klik `✕` pada popup Used By

### Filter Used By dengan Min dan Max
20. Buka Filter Panel
21. Isi Used By Min `1`
22. Isi Used By Max `3`
23. Klik `[Apply]`
24. Verifikasi baris `UBG-{runId}` tampil, Used By `1` tepat di Min
25. Verifikasi baris `UBC-{runId}` tampil, Used By `3` tepat di Max
26. Verifikasi baris `UBN-{runId}` tidak tampil, Used By `0` satu di bawah Min
27. Ganti isi Used By Max menjadi `2`
28. Klik `[Apply]`
29. Verifikasi baris `UBA-{runId}` tampil, Used By `2` di dalam rentang
30. Verifikasi baris `UBC-{runId}` tidak tampil, Used By `3` satu di atas Max
31. Klik `[Clear Field]`
32. Isi Used By Min `2`
33. Klik `[Apply]`
34. Verifikasi baris `UBC-{runId}` tampil, Used By `3` di atas Min tanpa batas Max
35. Verifikasi baris `UBG-{runId}` tidak tampil, Used By `1` di bawah Min
36. Klik `[Clear Field]`
37. Isi Used By Max `1`
38. Klik `[Apply]`
39. Verifikasi baris `UBG-{runId}` tampil, Used By `1` tepat di Max tanpa batas Min
40. Verifikasi baris `UBN-{runId}` tampil, Used By `0` di bawah Max
41. Verifikasi baris `UBC-{runId}` tidak tampil, Used By `3` di atas Max
42. Klik `[Clear Field]`
43. Klik `[Apply]`

### Search mencakup nilai Used By
44. Ketik Search `3`, tekan Enter
45. Verifikasi baris `UBC-{runId}` tampil, Used By `3` ikut dicari oleh kata kunci
46. Klik `(←)` pada kotak Search

### Jumlah Asset Name dibaca saat popup dibuka
47. Ketik Search `{runId}`, tekan Enter
48. Total Control meng-Unassign satu Asset Name dari Asset Class `Heavy Equipment {runId}` di modul Asset Class, sehingga jumlah Asset Name menjadi 11
49. Klik angka Used By `3` pada baris `UBC-{runId}`
50. Verifikasi bullet `Heavy Equipment {runId} — 11 Asset Names` tampil
51. Verifikasi jumlah bullet pada popup `3`, tidak berubah karena jumlah Asset Name tidak memengaruhi nilai Used By
52. Klik `✕` pada popup Used By
