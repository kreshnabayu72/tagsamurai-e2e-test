---
id: TC-FA-FACO-UI-126-tabel-switch-status
title: "Tab Chart of Accounts: Switch Status per state"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["R-04", "ST-01", "ST-02", "ST-03", "§4.1.1#r1", "§4.5#b1", "§4.5#b3", "§4.5#b5", "§4.8#b2", "§7.2#p2", "EB-TBL-5@switch-status"]
smoke: []
dependsOn: []
trace:
  "R-04": [50, 51, 55, 56]
  "ST-01": [3, 4, 46]
  "ST-02": [42, 43, 45]
  "ST-03": [13, 14, 16, 18, 20, 21, 23, 24, 26]
  "§4.1.1#r1": [2, 5, 6, 13, 14, 23, 24, 28, 29]
  "§4.5#b1": [32, 34, 38]
  "§4.5#b3": [8, 9, 10, 11]
  "§4.5#b5": [16, 18]
  "§4.8#b2": [16, 18, 26]
  "§7.2#p2": [50, 51, 55, 56, 60, 61]
  "EB-TBL-5@switch-status": [16, 18, 26]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: Switch Status per state

## Prerequisites
- Aktor: Total Control; aktor Read Only, Update, dan Delete hanya pada Kondisi K2, K3, dan K4.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-126-1: Account `1-1001`, Name `Fixed Assets – Equipment`, Function `Asset Cost`, status Active, Used By `0`.
  - DU-126-2: Account `1-2001`, Name `Accumulated Depreciation – Equipment`, Function `Asset Cost`, status Inactive, Used By `0`.
- Kondisi:
  - K1: tabel berisi DU-126-1 dan DU-126-2; aktor Total Control.
  - K2: seperti K1; aktor Read Only.
  - K3: seperti K1; aktor memegang Manage accounting huruf Read dan Update.
  - K4: seperti K1; aktor memegang Manage accounting huruf Read dan Delete.
  - K5: seperti K1; server menolak Activate dengan error 5xx.
  - K6: seperti K1; server tidak menjawab Activate sampai batas waktu.
  - K7: seperti K1; server menolak Deactivate dengan error 5xx.
  - K8: seperti K1; respons server atas Activate ditahan sampai pengujian melepasnya.

## Test Steps

### Switch per status akun
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Verifikasi kolom `Active` menampilkan switch pada baris `1-1001` dan baris `1-2001`
3. Verifikasi switch baris `1-1001` berstatus On
4. Verifikasi switch baris `1-2001` berstatus Off
5. Verifikasi switch baris `1-1001` enabled
6. Verifikasi switch baris `1-2001` enabled

### Label aksesibilitas dan state checked
7. Tampilkan Tab Chart of Accounts dengan kondisi K1
8. Verifikasi nama aksesibel switch baris `1-1001` berpola `Status for account [Account Code]` dengan Account Code `1-1001`
9. Verifikasi nama aksesibel switch baris `1-2001` berpola `Status for account [Account Code]` dengan Account Code `1-2001`
10. Verifikasi switch baris `1-1001` berstatus checked
11. Verifikasi switch baris `1-2001` tidak berstatus checked

### Switch Disabled bagi aktor Read Only
12. Tampilkan Tab Chart of Accounts dengan kondisi K2
13. Verifikasi switch baris `1-1001` disabled
14. Verifikasi switch baris `1-2001` disabled
15. Arahkan kursor ke switch baris `1-1001`
16. Verifikasi `You don't have permission to edit.` tersampaikan pada switch baris `1-1001`[^drift-1]
17. Arahkan kursor ke switch baris `1-2001`
18. Verifikasi `You don't have permission to edit.` tersampaikan pada switch baris `1-2001`[^drift-1]
19. Klik switch baris `1-2001`
20. Verifikasi dialog `Activate Account` tidak tampil
21. Verifikasi switch baris `1-2001` berstatus Off

### Switch Disabled bagi aktor yang hanya memegang huruf Delete
22. Tampilkan Tab Chart of Accounts dengan kondisi K4
23. Verifikasi switch baris `1-1001` disabled
24. Verifikasi switch baris `1-2001` disabled
25. Arahkan kursor ke switch baris `1-1001`
26. Verifikasi `You don't have permission to edit.` tersampaikan pada switch baris `1-1001`[^drift-1]

### Switch enabled bagi aktor yang memegang huruf Update
27. Tampilkan Tab Chart of Accounts dengan kondisi K3
28. Verifikasi switch baris `1-1001` enabled
29. Verifikasi switch baris `1-2001` enabled

### Navigasi keyboard pada switch
30. Tampilkan Tab Chart of Accounts dengan kondisi K1
31. Tekan Tab sampai fokus berada pada switch baris `1-2001`
32. Verifikasi switch baris `1-2001` menerima fokus
33. Tekan Space
34. Verifikasi dialog `Activate Account` tampil
35. Klik `[Cancel]`
36. Tekan Tab sampai fokus berada pada switch baris `1-2001`
37. Tekan Enter
38. Verifikasi dialog `Activate Account` tampil

### Switch Loading saat request dikirim
39. Tampilkan Tab Chart of Accounts dengan kondisi K8
40. Klik switch baris `1-2001`
41. Klik `[Activate]` pada dialog `Activate Account`
42. Verifikasi switch baris `1-2001` menampilkan spinner
43. Verifikasi switch baris `1-2001` non-interaktif
44. Lepaskan respons server atas Activate
45. Verifikasi switch baris `1-2001` tidak menampilkan spinner
46. Verifikasi switch baris `1-2001` berstatus On

### Activate gagal karena error server
47. Tampilkan Tab Chart of Accounts dengan kondisi K5
48. Klik switch baris `1-2001`
49. Klik `[Activate]` pada dialog `Activate Account`
50. Verifikasi toast `Error, failed to activate account.` tampil
51. Verifikasi switch baris `1-2001` kembali berstatus Off

### Activate gagal karena timeout
52. Tampilkan Tab Chart of Accounts dengan kondisi K6
53. Klik switch baris `1-2001`
54. Klik `[Activate]` pada dialog `Activate Account`
55. Verifikasi toast `Connection problem. Please try again.` tampil
56. Verifikasi switch baris `1-2001` kembali berstatus Off

### Deactivate gagal karena error server
57. Tampilkan Tab Chart of Accounts dengan kondisi K7
58. Klik switch baris `1-1001`
59. Klik `[Deactivate]` pada dialog `Deactivate Account`
60. Verifikasi toast `Error, failed to deactivate account.` tampil
61. Verifikasi switch baris `1-1001` kembali berstatus On

[^drift-1]: Drift PRD vs kontrak komponen. PRD `§4.5#b5`: «Tooltip 🔖 dapat diakses lewat keyboard focus.» Kontrak `Tooltip#38`: «A disabled control cannot be focused, so its tooltip opens on hover only.» dan `Switch#37`: «A disabled or loading switch is skipped by Tab (the native input is disabled).» Diasersi: kontrak (tooltip switch Disabled hanya lewat hover), karena fokus pada kontrol disabled adalah mekanik komponen (SB-7); akses keyboard untuk tooltip kontrol yang dapat difokus dimiliki spec lain.
