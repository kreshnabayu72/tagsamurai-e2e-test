---
id: TC-FA-FACO-UI-126-tabel-switch-status
title: "Tab Chart of Accounts: Switch Status per state"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["R-04", "ST-01", "ST-02", "ST-03", "§4.1.1#r1", "§4.5#b1", "§4.5#b3", "§4.5#b5", "§4.8#b2", "§7.2#p2", "EB-TBL-5@switch-status"]
smoke: []
dependsOn: []
trace:
  "R-04": [46, 47, 51, 52]
  "ST-01": [3, 4, 42]
  "ST-02": [38, 39, 41]
  "ST-03": [13, 14, 16, 18, 20, 21, 23, 24, 26]
  "§4.1.1#r1": [2, 5, 6, 13, 14, 23, 24, 28, 29]
  "§4.5#b1": [32, 34]
  "§4.5#b3": [8, 9, 10, 11]
  "§4.5#b5": [16, 18, 62, 63, 66, 68, 70, 72]
  "§4.8#b2": [16, 18, 26]
  "§7.2#p2": [46, 47, 51, 52, 56, 57]
  "EB-TBL-5@switch-status": [16, 18, 26]
anchor: [60]
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
16. Verifikasi `You don't have permission to edit.` tersampaikan pada switch baris `1-1001`
17. Arahkan kursor ke switch baris `1-2001`
18. Verifikasi `You don't have permission to edit.` tersampaikan pada switch baris `1-2001`
19. Klik switch baris `1-2001`
20. Verifikasi dialog `Activate Account` tidak tampil
21. Verifikasi switch baris `1-2001` berstatus Off

### Switch Disabled bagi aktor yang hanya memegang huruf Delete
22. Tampilkan Tab Chart of Accounts dengan kondisi K4
23. Verifikasi switch baris `1-1001` disabled
24. Verifikasi switch baris `1-2001` disabled
25. Arahkan kursor ke switch baris `1-1001`
26. Verifikasi `You don't have permission to edit.` tersampaikan pada switch baris `1-1001`

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

### Switch Loading saat request dikirim
35. Tampilkan Tab Chart of Accounts dengan kondisi K8
36. Klik switch baris `1-2001`
37. Klik `[Activate]` pada dialog `Activate Account`
38. Verifikasi switch baris `1-2001` menampilkan spinner
39. Verifikasi switch baris `1-2001` non-interaktif
40. Lepaskan respons server atas Activate
41. Verifikasi switch baris `1-2001` tidak menampilkan spinner
42. Verifikasi switch baris `1-2001` berstatus On

### Activate gagal karena error server
43. Tampilkan Tab Chart of Accounts dengan kondisi K5
44. Klik switch baris `1-2001`
45. Klik `[Activate]` pada dialog `Activate Account`
46. Verifikasi toast `Error, failed to activate account.` tampil
47. Verifikasi switch baris `1-2001` kembali berstatus Off

### Activate gagal karena timeout
48. Tampilkan Tab Chart of Accounts dengan kondisi K6
49. Klik switch baris `1-2001`
50. Klik `[Activate]` pada dialog `Activate Account`
51. Verifikasi toast `Connection problem. Please try again.` tampil
52. Verifikasi switch baris `1-2001` kembali berstatus Off

### Deactivate gagal karena error server
53. Tampilkan Tab Chart of Accounts dengan kondisi K7
54. Klik switch baris `1-1001`
55. Klik `[Deactivate]` pada dialog `Deactivate Account`
56. Verifikasi toast `Error, failed to deactivate account.` tampil
57. Verifikasi switch baris `1-1001` kembali berstatus On

### Switch Disabled tidak dapat difokus keyboard
58. Tampilkan Tab Chart of Accounts dengan kondisi K2
59. Tekan Tab sampai fokus berada pada ikon Filter
60. Verifikasi ikon Filter menerima fokus
61. Tekan Tab berulang kali sampai fokus melewati baris `1-2001`
62. Verifikasi switch baris `1-1001` yang Disabled tidak menerima fokus selama Tab berjalan sehingga alasannya hanya tersampaikan lewat hover
63. Verifikasi switch baris `1-2001` yang Disabled tidak menerima fokus selama Tab berjalan sehingga alasannya hanya tersampaikan lewat hover

### Tooltip pada elemen yang dapat difokus terbuka lewat fokus keyboard
64. Tampilkan Tab Chart of Accounts dengan kondisi K1
65. Tekan Tab sampai fokus berada pada ikon Search
66. Verifikasi `Search` tersampaikan pada ikon Search
67. Tekan Tab sampai fokus berada pada ikon Filter
68. Verifikasi `Filter` tersampaikan pada ikon Filter
69. Tekan Tab sampai fokus berada pada ikon Download
70. Verifikasi `Download` tersampaikan pada ikon Download
71. Tekan Tab sampai fokus berada pada ikon Changelog
72. Verifikasi `Changelog` tersampaikan pada ikon Changelog
