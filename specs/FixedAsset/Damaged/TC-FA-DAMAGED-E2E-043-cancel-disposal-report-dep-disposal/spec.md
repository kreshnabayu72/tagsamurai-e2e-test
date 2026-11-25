---
id: TC-FA-DAMAGED-E2E-043-cancel-disposal-report-dep-disposal
title: "Cancel Disposal Report atas record Reported Disposal lewat D-DMG-09 mengembalikan record ke Damaged dengan node Disposal report canceled by; pada status lain Hidden"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-09, D-DISP-15, TS-DISP-18, "§4.4#r12", TS-DMG-08, S-DMG-06, V-DMG-06, "§8.1#r15", "§Aturan Logika Modul#r21", "§9.2#b25", "§9.6#r8", "§9.4.4#r29", "§2.1#r9", "§4.8#r11", "§2.1#b6", "EB-FB-1@cancel-disposal-report", "§4.2.4#p6", "§4.2.4#r17", "§3#p7"]
smoke: []
dependsOn:
  - "Disposal: Cancel Report (D-DISP-15)"
trace:
  "§9.2#b25": [2, 4]
  T-DMG-01: [4, 13, 32, 33, 38, 39]
  "§2.1#r9": 4
  "§4.8#r11": 4
  "§2.1#b6": [4, 13, 33, 39]
  D-DISP-15: [4, 6, 9, 10, 13, 33, 39]
  D-DMG-09: [6, 10]
  "§4.4#r12": [6, 9, 10]
  TS-DISP-18: 9
  TS-DMG-08: 9
  "EB-FB-1@cancel-disposal-report": 9
  "§9.6#r8": [9, 10]
  "§Aturan Logika Modul#r21": [10, 12]
  S-DMG-06: [13, 30, 33, 36, 39]
  "§8.1#r15": [16, 17, 18]
  V-DMG-06: [21, 26, 28]
  "§9.4.4#r29": [26, 28]
  "§4.2.4#p6": [26, 28]
  "§4.2.4#r17": 26
  "§3#p7": [6, 10]
anchor: []
coverage:
  web: automated
---

# Cancel Disposal Report atas record Reported Disposal lewat D-DMG-09 mengembalikan record ke Damaged dengan node Disposal report canceled by; pada status lain Hidden

## Prerequisites
- Aktor: Total Control; `Admin B {runId}` (Total Control, seluruh client) hanya memicu perubahan state.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-043-1: Damage record `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-043-2: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-043-3: Damage record `Camera Canon EOS {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-043-4: Damage record `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, Status `In Disposal Process`, Source `Manual`.
  - DU-043-5: User `Admin B {runId}`, role Total Control, cakupan seluruh client.
  - DU-043-6: Input Cancel Disposal Report atas `Printer HP LaserJet M404 {runId}`: Reason `Aset masih dapat diperbaiki`.
  - DU-043-7: Input Decline Report `Admin B {runId}` atas `Monitor Dell P2422H {runId}`: Reason `Laporan ditolak karena aset masih dapat dipakai`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Full`.

## Test Steps

### Cancel Disposal Report atas record Reported Disposal mengembalikan record ke Damaged
1. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
2. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Reported Disposal`
3. Buka menu ⋯ pada baris `Printer HP LaserJet M404 {runId}`
4. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` memuat aksi `Cancel Disposal Report`
5. Klik `Cancel Disposal Report`
6. Verifikasi dialog `Cancel Disposal Report` terbuka
7. Isi Reason `Aset masih dapat diperbaiki`
8. Kirim dialog Cancel Disposal Report
9. Verifikasi toast sukses Cancel Disposal Report tampil
10. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Damaged`
11. Buka menu ⋯ pada baris `Printer HP LaserJet M404 {runId}`
12. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` memuat aksi `Mark as Repaired`
13. Verifikasi aksi `Cancel Disposal Report` Hidden pada menu baris `Printer HP LaserJet M404 {runId}`
14. Tutup menu ⋯

### Node Disposal report canceled by di Damage Log
15. Klik nama aset `Printer HP LaserJet M404 {runId}` di kolom Name
16. Verifikasi dialog Damage Log memuat node `Disposal report canceled by` dengan pelaku aktor yang menjalankan Cancel Disposal Report
17. Verifikasi baris detail node `Disposal report canceled by` memuat Reason `Aset masih dapat diperbaiki`
18. Verifikasi baris detail node `Disposal report canceled by` memuat `Back to Damaged`
19. Tutup dialog Damage Log

### Status record berubah sebelum Submit memunculkan dialog Already Changed
20. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
21. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Reported Disposal`
22. Buka menu ⋯ pada baris `Monitor Dell P2422H {runId}`
23. Klik `Cancel Disposal Report`
24. `Admin B {runId}` menjalankan Decline Report atas Disposal Report record `Monitor Dell P2422H {runId}` dengan Reason `Laporan ditolak karena aset masih dapat dipakai`
25. Kirim dialog Cancel Disposal Report
26. Verifikasi dialog `Already Changed` tampil dengan isi `This record was changed by [User Name]. Reload to see the latest status.` dengan `[User Name]` diisi `Admin B {runId}`
27. Klik `Reload`
28. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Damaged`

### Cancel Disposal Report Hidden pada status selain Reported Disposal
29. Ganti isi kotak search dengan `Camera Canon EOS {runId}`, tekan Enter
30. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Damaged`
31. Buka menu ⋯ pada baris `Camera Canon EOS {runId}`
32. Verifikasi menu baris `Camera Canon EOS {runId}` memuat aksi `Mark as Repaired`
33. Verifikasi aksi `Cancel Disposal Report` Hidden pada menu baris `Camera Canon EOS {runId}`
34. Tutup menu ⋯
35. Ganti isi kotak search dengan `Tablet Samsung Tab A8 {runId}`, tekan Enter
36. Verifikasi baris `Tablet Samsung Tab A8 {runId}` berstatus `In Disposal Process`
37. Buka menu ⋯ pada baris `Tablet Samsung Tab A8 {runId}`
38. Verifikasi menu baris `Tablet Samsung Tab A8 {runId}` memuat aksi `Damage Log`
39. Verifikasi aksi `Cancel Disposal Report` Hidden pada menu baris `Tablet Samsung Tab A8 {runId}`
40. Tutup menu ⋯
