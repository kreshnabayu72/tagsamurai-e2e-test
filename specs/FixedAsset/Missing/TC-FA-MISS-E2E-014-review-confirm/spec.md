---
id: TC-FA-MISS-E2E-014-review-confirm
title: "Review > Confirm: record Waiting for Confirmation menjadi Missing, footer hilang, node Report confirmed by"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1a#r31", "§4.4#r4", "§4.4#r5", "§4.2.4#r19", "§8.1#r6", "§8.1#r9", "§7.3#r7", "§9.6#r2", "§9.2#r1", "§9.2#r2", "§1.2#r59", "§1.2#r58", "§2.1#r6", "§4.8#r6", "§9.2#b33", "§9.1#r6", "§3#p4", "§9.8#r3", "§9.8#p3", "§9.4.4#r19", "EB-FB-1@confirm"]
smoke: []
dependsOn: []
trace:
  "§4.1a#r31": [4, 6, 19]
  "§4.4#r4": [6, 7]
  "§4.4#r5": [9, 10, 11, 13, 14]
  "§4.2.4#r19": [10, 11, 12, 13, 14]
  "§8.1#r6": [7, 13]
  "§8.1#r9": 14
  "§7.3#r7": 9
  "§9.6#r2": [9, 12]
  "§9.2#r1": [2, 12]
  "§9.2#r2": [12, 16]
  "§1.2#r59": [12, 16]
  "§1.2#r58": [13, 18]
  "§2.1#r6": [4, 7]
  "§4.8#r6": [4, 7]
  "§9.2#b33": 12
  "§9.1#r6": [12, 14]
  "§3#p4": [12, 14]
  "§9.8#r3": [9, 12]
  "§9.8#p3": 12
  "§9.4.4#r19": [12, 14]
  "EB-FB-1@confirm": 9
anchor: []
coverage:
  web: automated
---

# Review > Confirm: record Waiting for Confirmation menjadi Missing, footer hilang, node Report confirmed by

## Prerequisites
- Aktor: Rina W, Total Control, tidak menjadi Last Holder record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-014-1: Record Waiting for Confirmation `Hydraulic Pallet Jack {runId}`, Asset ID `HPJ-014-0001`, Group `Warehouse`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Joko S`, Reported By `Rudi H (on behalf of Joko S)`, Reported Date `T0 − 2 hari, pukul 07:15`. Node: `Reported missing by Rudi H on behalf of Joko S` dengan What happened `Hydraulic pallet jack tidak kembali dari area bongkar muat`. Node yang diharapkan sesudah Confirm: `Report confirmed by Rina W`.
  - Pengguna pada data: Rina W, Total Control, seluruh client; Rudi H, PIC yang tercatat bagi Joko S; Joko S, karyawan pemegang tanpa akun.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`.

## Test Steps

### Review membuka dialog Missing Log dengan footer
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Hydraulic Pallet Jack {runId}` tampil dengan Status `Waiting for Confirmation`
3. Klik `⋯` pada baris `Hydraulic Pallet Jack {runId}`
4. Verifikasi menu baris memuat `Review` bagi Total Control yang bukan Last Holder
5. Klik `Review`
6. Verifikasi dialog `Missing Log` terbuka untuk record `Hydraulic Pallet Jack {runId}` dengan badge status record `Waiting for Confirmation`
7. Verifikasi footer `[Reject]` dan `[Confirm]` tampil

### Confirm langsung memperbarui dialog
8. Klik `[Confirm]`
9. Verifikasi toast `Success, report has been confirmed.` tampil
10. Verifikasi dialog `Missing Log` tetap terbuka
11. Verifikasi tidak ada dialog konfirmasi kedua yang tampil
12. Verifikasi badge status record `Missing` tampil
13. Verifikasi footer `[Reject]` dan `[Confirm]` tidak tampil lagi
14. Verifikasi node `Report confirmed by Rina W` tampil

### Record Missing di tab Active hanya dikoreksi lewat Mark as Found
15. Klik `✕` pada dialog Missing Log
16. Verifikasi Status baris `Hydraulic Pallet Jack {runId}` menampilkan `Missing` di sub-tab Active
17. Klik `⋯` pada baris `Hydraulic Pallet Jack {runId}`
18. Verifikasi menu baris memuat `Mark as Found`
19. Verifikasi `Review` tidak tampil pada menu baris karena status record bukan `Waiting for Confirmation`
