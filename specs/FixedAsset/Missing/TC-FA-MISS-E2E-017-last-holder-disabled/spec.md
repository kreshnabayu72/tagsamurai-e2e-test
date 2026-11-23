---
id: TC-FA-MISS-E2E-017-last-holder-disabled
title: "Pemisahan tugas: Review, Mark as Found, dan Report Disposal Disabled bagi Last holder, aktif bagi admin lain"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r118", "§1.2#r119", "§1.2#r120", "§1.2#r121", "§1.2#r74", "§6#r1", "§4.3#r4", "§9.4.2#r17", "§9.2#b28", "§2.1#b9", "§2.1#p12", "§2.1#p17", "§2.1#p18", "§2.1#p19", "§2.1#p20", "§9.4.3#b6", "§9.4.4#r14", "§8.1#r6", "§4.8#r6", "EB-TBL-5@aksi-last-holder", "§4.5#p1"]
smoke: []
dependsOn: []
trace:
  "§1.2#r118": [2, 8, 11, 42, 57]
  "§1.2#r119": [3, 8]
  "§1.2#r120": [14, 18, 40]
  "§1.2#r121": [15, 21, 24, 25, 40]
  "§1.2#r74": [15, 18, 24, 39]
  "§6#r1": [9, 12, 19, 22, 24, 25, 30]
  "§4.3#r4": [8, 9, 11, 18, 24, 28]
  "§9.4.2#r17": [8, 9]
  "§9.2#b28": [8, 11, 18, 24, 28]
  "§2.1#b9": [8, 35]
  "§2.1#p12": [2]
  "§2.1#p17": [2, 4]
  "§2.1#p18": [6, 9, 12]
  "§2.1#p19": [35, 36]
  "§2.1#p20": [3, 8]
  "§9.4.3#b6": [8, 11, 18, 21, 24]
  "§9.4.4#r14": [8, 9]
  "§8.1#r6": [28, 30]
  "§4.8#r6": [8, 18, 21, 24, 28, 35, 39, 45, 48, 52, 60, 64]
  "EB-TBL-5@aksi-last-holder": [9, 12, 19, 24, 25, 46, 49, 61]
  "§4.5#p1": [9, 19, 25, 30]
anchor: []
coverage:
  web: automated
---

# Pemisahan tugas: Review, Mark as Found, dan Report Disposal Disabled bagi Last holder, aktif bagi admin lain

## Prerequisites
- Aktor: Andi P, Group Manager pada Group Head Office, tercatat sebagai Last Holder semua record di bawah; lalu Rina W, Total Control, yang bukan Last Holder DU-017-1 dan DU-017-2 tetapi Last Holder DU-017-3; lalu `Bimo Tirta {runId}`, Manage asset & TAG (Update) pada Group Head Office, Last Holder DU-017-4.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-017-1: Record Missing `Laptop Dell Latitude 7440 {runId}`, Asset ID `LPT-017-0001`, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `Andi P`, Reported By `Andi P`, Reported Date `T0 − 3 hari, pukul 10:00`; Andi P melapor sendiri sebagai Pelapor admin sehingga record langsung `Missing`.
  - DU-017-2: Record Waiting for Confirmation `Pallet Stacker Electric {runId}`, Asset ID `PST-017-0002`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Joko S`, Reported By `Andi P (on behalf of Joko S)`, Reported Date `T0 − 1 hari, pukul 09:20`; Joko S adalah karyawan pemegang tanpa akun dan PIC yang tercatat saat dilaporkan adalah Andi P; saat laporan itu dibuat Andi P belum memegang hak Aktor Missing pada Group aset, dan hak itu (Group Manager pada Group Head Office) baru ia terima sesudah laporan dibuat.
  - DU-017-3: Record Waiting for Confirmation `Mesin Label Printer {runId}`, Asset ID `MLP-017-0003`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Rina W`, Reported By `Rina W`, Reported Date `T0 − 2 hari, pukul 13:40`; Rina W memegang aset ini dan melapor saat belum memegang hak Aktor Missing, dan hak Total Control baru ia terima sesudah laporan dibuat.
  - DU-017-4: Record Waiting for Confirmation `Scanner Barcode Zebra {runId}`, Asset ID `SBZ-017-0004`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Bimo T`, Reported By `Bimo T`, Reported Date `T0 − 2 hari, pukul 08:15`; Bimo T memegang aset ini dan melapor saat belum memegang hak Aktor Missing, dan hak Manage asset & TAG (Update) pada Group Head Office baru ia terima sesudah laporan dibuat.
  - DU-017-5: Pengguna `Bimo Tirta {runId}`, role Manage asset & TAG (Update) pada Group `Head Office`; tampil sebagai `Bimo T`, dari `Bimo Tirta {runId}`.
  - Pengguna pada data: Andi P, Group Manager pada Group Head Office beserta sub-group; Rina W, Total Control, seluruh client; Joko S, karyawan pemegang tanpa akun.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`.
- Kondisi:
  - Level Feature Suite Disposal pada entitas aktor adalah Full

## Test Steps

### Last Holder yang melapor sendiri tidak dapat Mark as Found dan Report Disposal
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi Last Holder baris `Laptop Dell Latitude 7440 {runId}` menampilkan `Andi P`
3. Verifikasi Reported By baris `Laptop Dell Latitude 7440 {runId}` menampilkan `Andi P`
4. Verifikasi Status baris `Laptop Dell Latitude 7440 {runId}` menampilkan `Missing`
5. Klik `⋯` pada baris `Laptop Dell Latitude 7440 {runId}`
6. Verifikasi menu baris memuat `Add Update` yang aktif
7. Arahkan kursor ke `Mark as Found` pada menu baris
8. Verifikasi `Mark as Found` Disabled
9. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Mark as Found` yang Disabled[^drift-1]
10. Arahkan kursor ke `Report Disposal` pada menu baris
11. Verifikasi `Report Disposal` Disabled
12. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Report Disposal` yang Disabled[^drift-1]
13. Tekan Esc untuk menutup menu baris
### PIC yang tercatat adalah Last Holder bagi pemegang tanpa akun
14. Verifikasi Last Holder baris `Pallet Stacker Electric {runId}` menampilkan `Joko S`
15. Verifikasi Reported By baris `Pallet Stacker Electric {runId}` menampilkan `Andi P (on behalf of Joko S)`
16. Klik `⋯` pada baris `Pallet Stacker Electric {runId}`
17. Arahkan kursor ke `Review` pada menu baris
18. Verifikasi `Review` Disabled
19. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Review` yang Disabled[^drift-1]
20. Arahkan kursor ke `Mark as Found` pada menu baris
21. Verifikasi `Mark as Found` Disabled bagi PIC yang tercatat
22. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Mark as Found` yang Disabled bagi PIC[^drift-1]
23. Arahkan kursor ke `Report Disposal` pada menu baris
24. Verifikasi `Report Disposal` Disabled bagi PIC yang tercatat
25. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Report Disposal` yang Disabled bagi PIC[^drift-1]
26. Tekan Esc untuk menutup menu baris
27. Klik nama `Pallet Stacker Electric {runId}` pada kolom Name
28. Verifikasi footer `[Reject]` dan `[Confirm]` tampil dan Disabled
29. Arahkan kursor ke `[Confirm]` pada footer dialog Missing Log
30. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada footer `[Confirm]` yang Disabled[^drift-1]
31. Klik `✕` pada dialog Missing Log
### Admin lain yang bukan Last Holder tidak terhalang
32. Masuk sebagai Rina W
33. Ketik Search `{runId}`, tekan Enter
34. Klik `⋯` pada baris `Laptop Dell Latitude 7440 {runId}`
35. Verifikasi `Mark as Found` aktif
36. Verifikasi `Report Disposal` aktif
37. Tekan Esc untuk menutup menu baris
38. Klik `⋯` pada baris `Pallet Stacker Electric {runId}`
39. Verifikasi `Review` aktif
40. Verifikasi `Mark as Found` aktif pada baris ini
### Total Control yang menjadi Last Holder tidak dapat Review dan Mark as Found
41. Ketik Search `{runId}`, tekan Enter
42. Verifikasi Last Holder baris `Mesin Label Printer {runId}` menampilkan `Rina W`
43. Klik `⋯` pada baris `Mesin Label Printer {runId}`
44. Arahkan kursor ke `Review` pada menu baris
45. Verifikasi `Review` Disabled bagi Total Control yang menjadi Last Holder
46. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Review` yang Disabled bagi Total Control[^drift-1]
47. Arahkan kursor ke `Mark as Found` pada menu baris
48. Verifikasi `Mark as Found` Disabled bagi Total Control yang menjadi Last Holder
49. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Mark as Found` yang Disabled bagi Total Control[^drift-1]
50. Tekan Esc untuk menutup menu baris
51. Klik nama `Mesin Label Printer {runId}` pada kolom Name
52. Verifikasi footer `[Reject]` dan `[Confirm]` tampil dan Disabled bagi Total Control yang menjadi Last Holder
53. Klik `✕` pada dialog Missing Log
### Manage asset & TAG (Update) yang menjadi Last Holder tidak dapat Review dan Confirm
54. Keluar dari akun
55. Masuk sebagai `Bimo Tirta {runId}`
56. Ketik Search `{runId}`, tekan Enter
57. Verifikasi Last Holder baris `Scanner Barcode Zebra {runId}` menampilkan `Bimo T`
58. Klik `⋯` pada baris `Scanner Barcode Zebra {runId}`
59. Arahkan kursor ke `Review` pada menu baris
60. Verifikasi `Review` Disabled bagi Manage asset & TAG (Update) yang menjadi Last Holder
61. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Review` yang Disabled bagi Manage asset & TAG (Update)[^drift-1]
62. Tekan Esc untuk menutup menu baris
63. Klik nama `Scanner Barcode Zebra {runId}` pada kolom Name
64. Verifikasi footer `[Reject]` dan `[Confirm]` tampil dan Disabled bagi Manage asset & TAG (Update) yang menjadi Last Holder
65. Klik `✕` pada dialog Missing Log

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.5: «Tooltip Disabled 🔖 dapat diakses lewat fokus.»; kontrak `Tooltip#38`: «A disabled control cannot be focused, so its tooltip opens on hover only.», `Button#2`: «A disabled button (`disabled`) is a native disabled button with `aria-disabled="true"`: it cannot take focus» dan `Menu#6`: item menu yang disabled dilewati Tab dan tombol panah. Diasersi: kontrak, sehingga alasan pada item menu dan tombol yang Disabled dibuka lewat hover, bukan fokus keyboard (SB-7).
