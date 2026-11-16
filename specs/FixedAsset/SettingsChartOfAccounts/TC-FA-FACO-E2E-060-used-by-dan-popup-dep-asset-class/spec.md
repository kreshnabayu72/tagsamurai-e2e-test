---
id: TC-FA-FACO-E2E-060-used-by-dan-popup-dep-asset-class
title: "Kolom Used By dan popup Used By menghitung Asset Class pemakai akun"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FACO-LOGIC-02a, FACO-LOGIC-02f, FACO-LOGIC-02g, FACO-LOGIC-02h, "§4.1.1#r5", "§4.1.4#p1", "§4.1.4#p2", "§4.1.4#p3", "§4.4#r4", "§4.6#b3", "§4.8#r4"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)", "Asset Class: Assign dan Unassign Asset Name pada Asset Class"]
trace:
  FACO-LOGIC-02a: [2, 4, 5, 55, 56]
  FACO-LOGIC-02f: [3, 18]
  FACO-LOGIC-02g: [2, 6]
  FACO-LOGIC-02h: 2
  "§4.1.1#r5": [2, 3, 4, 5, 6, 24, 25, 26, 29, 30, 34, 35, 39, 40, 41, 52, 53, 55, 56]
  "§4.1.4#p1": [9, 17]
  "§4.1.4#p2": [10, 11]
  "§4.1.4#p3": [12, 13, 14, 47, 48]
  "§4.4#r4": 8
  "§4.6#b3": 8
  "§4.8#r4": [8, 50]
anchor: []
coverage:
  web: automated
  android: automated
---

# Kolom Used By dan popup Used By menghitung Asset Class pemakai akun

## Prerequisites
- Aktor: pengguna Total Control di entitas khusus spec ini.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-060-10: entitas khusus `Entitas Uji Used By {runId}`, hanya dipakai spec ini, dan tidak berisi akun selain DU-060-1 sampai DU-060-6, DU-060-11, dan DU-060-12. Akun di entitas ini tanpa pengenal run, dan Account Code, Account Name, serta Account Function-nya tidak memuat digit `3`, sehingga digit `3` hanya muncul pada nilai Used By `3` milik DU-060-1.
  - DU-060-1: Account Code `UBC`, Account Name `Equipment Cost`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 3 Asset Class (DU-060-7, DU-060-8, DU-060-9).
  - DU-060-2: Account Code `UBG`, Account Name `Gain and Loss on Disposal`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-060-7) pada field Gain on Disposal dan field Loss on Disposal.
  - DU-060-3: Account Code `UBA`, Account Name `Accumulated Depreciation Equipment`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-060-7, DU-060-8).
  - DU-060-4: Account Code `UBE`, Account Name `Depreciation Expense Equipment`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-060-7).
  - DU-060-5: Account Code `UBN`, Account Name `Unused Account`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-060-6: Account Code `UBI`, Account Name `Legacy Unused Account`, Account Function `Asset Cost`, Status Inactive, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-060-11: Account Code `UBL`, Account Name `Vehicle Loss on Disposal`, Account Function `Loss on Disposal`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-060-8) hanya pada field Loss on Disposal.
  - DU-060-12: Account Code `UBP`, Account Name `Equipment Gain on Disposal`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-060-9) hanya pada field Gain on Disposal.
  - DU-060-7: Asset Class `Delivery Vehicles {runId}` dengan 3 Asset Name; Asset Cost `UBC`, Accumulated Depreciation `UBA`, Depreciation Expense `UBE`, Gain on Disposal `UBG`, Loss on Disposal `UBG`.
  - DU-060-8: Asset Class `Heavy Equipment {runId}` dengan 12 Asset Name; Asset Cost `UBC`, Accumulated Depreciation `UBA`, Loss on Disposal `UBL`.
  - DU-060-9: Asset Class `Office Equipment {runId}` berstatus Inactive dengan 1 Asset Name; Asset Cost `UBC`, Gain on Disposal `UBP`.
  - Identitas akun pada popup untuk DU-060-1: Account Code `UBC`, Account Name `Equipment Cost`, dan jumlah Asset Class pemakai `3`, dari 3 Asset Class DU-060-7, DU-060-8, dan DU-060-9.
  - Daftar pemakai popup untuk DU-060-1 memuat nama Asset Class `Delivery Vehicles {runId}` dengan teks jumlah `3 Asset Names`, `Heavy Equipment {runId}` dengan `12 Asset Names`, dan `Office Equipment {runId}` dengan `1 Asset Name`, dari jumlah Asset Name masing-masing.
  - Identitas akun pada popup untuk DU-060-2: Account Code `UBG`, Account Name `Gain and Loss on Disposal`, dan jumlah Asset Class pemakai `1`, dari 1 Asset Class DU-060-7.
  - Urutan pembuatan Asset Class: DU-060-9 dibuat lebih dulu, lalu DU-060-8, lalu DU-060-7, sehingga urutan pembuatan berlawanan dengan urutan A-Z menurut nama.
  - Teks jumlah untuk `Heavy Equipment {runId}` pada daftar pemakai DU-060-1 sesudah satu Asset Name di-Unassign dari DU-060-8 adalah `11 Asset Names`, dari jumlah Asset Name 12 dikurangi 1.

## Test Steps

### Used By menghitung Asset Class berbeda pada setiap field akun
1. Ketik Search `UB`, tekan Enter
2. Verifikasi Used By baris `UBC` bernilai `3`
3. Verifikasi Used By baris `UBG` bernilai `1`
4. Verifikasi Used By baris `UBA` bernilai `2`
5. Verifikasi Used By baris `UBE` bernilai `1`
6. Verifikasi Used By baris `UBI` yang berstatus Inactive bernilai `0`

### Popup Used By memuat Asset Class pemakai akun
7. Klik angka Used By `3` pada baris `UBC`
8. Verifikasi popup `Used By` untuk akun `UBC` tampil
9. Verifikasi identitas akun pada popup memuat Account Code `UBC`, Account Name `Equipment Cost`, dan jumlah Asset Class `3`, sama dengan nilai Used By
10. Verifikasi bullet pemakai berurutan A-Z: `Delivery Vehicles {runId}`, `Heavy Equipment {runId}`, `Office Equipment {runId}`
11. Verifikasi jumlah bullet pada popup `3`, sama dengan nilai Used By
12. Verifikasi `Delivery Vehicles {runId}` tampil pada daftar pemakai bersama teks jumlah `3 Asset Names`
13. Verifikasi `Heavy Equipment {runId}` tampil pada daftar pemakai bersama teks jumlah `12 Asset Names`
14. Verifikasi `Office Equipment {runId}` tampil pada daftar pemakai bersama teks jumlah `1 Asset Name`
15. Klik `✕` pada popup Used By

### Asset Class yang merujuk akun lebih dari sekali dihitung satu kali
16. Klik angka Used By `1` pada baris `UBG`
17. Verifikasi identitas akun pada popup memuat Account Code `UBG`, Account Name `Gain and Loss on Disposal`, dan jumlah Asset Class `1`, sama dengan nilai Used By
18. Verifikasi jumlah bullet pada popup `1`
19. Klik `✕` pada popup Used By

### Filter Used By dengan Min dan Max
20. Buka Filter Panel
21. Isi Used By Min `1`
22. Isi Used By Max `3`
23. Klik `[Apply]`
24. Verifikasi baris `UBG` tampil, Used By `1` tepat di Min
25. Verifikasi baris `UBC` tampil, Used By `3` tepat di Max
26. Verifikasi baris `UBN` tidak tampil, Used By `0` satu di bawah Min
27. Ganti isi Used By Max menjadi `2`
28. Klik `[Apply]`
29. Verifikasi baris `UBA` tampil, Used By `2` di dalam rentang
30. Verifikasi baris `UBC` tidak tampil, Used By `3` satu di atas Max
31. Klik `[Clear Field]`
32. Isi Used By Min `2`
33. Klik `[Apply]`
34. Verifikasi baris `UBC` tampil, Used By `3` di atas Min tanpa batas Max
35. Verifikasi baris `UBG` tidak tampil, Used By `1` di bawah Min
36. Klik `[Clear Field]`
37. Isi Used By Max `1`
38. Klik `[Apply]`
39. Verifikasi baris `UBG` tampil, Used By `1` tepat di Max tanpa batas Min
40. Verifikasi baris `UBN` tampil, Used By `0` di bawah Max
41. Verifikasi baris `UBC` tidak tampil, Used By `3` di atas Max
42. Klik `[Clear Field]`
43. Klik `[Apply]`

### Jumlah Asset Name dibaca saat popup dibuka
44. Ketik Search `UB`, tekan Enter
45. Total Control meng-Unassign satu Asset Name dari Asset Class `Heavy Equipment {runId}` di modul Asset Class, sehingga jumlah Asset Name menjadi 11
46. Klik angka Used By `3` pada baris `UBC`
47. Verifikasi `Heavy Equipment {runId}` tampil pada daftar pemakai bersama teks jumlah `11 Asset Names`
48. Verifikasi jumlah bullet pada popup `3`, tidak berubah karena jumlah Asset Name tidak memengaruhi nilai Used By
49. Klik `✕` pada popup Used By

### Link Used By tampil bagi Total Control
50. Verifikasi angka Used By `3` pada baris `UBC` dapat diklik

### Search atas kolom Used By
51. Ganti isi kotak search dengan `3`, tekan Enter
52. Verifikasi baris `UBC` tampil, Used By `3` cocok dengan Search `3`
53. Verifikasi baris `UBG`, `UBA`, `UBE`, `UBN`, dan `UBI` tidak tampil, Used By `1`, `2`, `1`, `0`, dan `0` tidak cocok dengan Search `3`
54. Klik `(←)` pada kotak Search

### Used By menghitung akun yang hanya dirujuk pada satu field disposal
55. Verifikasi Used By baris `UBL` yang hanya dirujuk pada field Loss on Disposal bernilai `1`
56. Verifikasi Used By baris `UBP` yang hanya dirujuk pada field Gain on Disposal bernilai `1`
