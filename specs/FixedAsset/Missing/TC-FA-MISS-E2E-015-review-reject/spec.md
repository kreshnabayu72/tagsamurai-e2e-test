---
id: TC-FA-MISS-E2E-015-review-reject
title: "Review > Reject: D-MIS-04 dengan Reason, record pindah ke History sebagai Rejected"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.4#r6", "§4.2.4#r20", "§7.2#r15", "§7.2#r7", "§4.2.4#p11", "§8.1#r9", "§9.6#r3", "§9.2#r7", "§1.2#r18", "§1.2#r60", "§9.4.2#r7", "§9.9#r7", "EB-FB-1@reject", "§8.1#r3", "EB-FRM-4@reject-report"]
smoke: ["EB-FRM-4@reject-report"]
dependsOn: []
trace:
  "§4.4#r6": [7, 11, 12, 14, 17, 24, 25]
  "§4.2.4#r20": [4, 7, 12, 14, 17]
  "§7.2#r15": [7, 11]
  "§7.2#r7": [7, 8]
  "§4.2.4#p11": 8
  "§8.1#r9": 19
  "§9.6#r3": 11
  "§9.2#r7": 17
  "§1.2#r18": 17
  "§1.2#r60": [17, 19]
  "§9.4.2#r7": 17
  "§9.9#r7": 19
  "EB-FB-1@reject": 11
  "§8.1#r3": [5, 24, 25]
  "EB-FRM-4@reject-report": 19
anchor: [13]
coverage:
  web: automated
---

# Review > Reject: D-MIS-04 dengan Reason, record pindah ke History sebagai Rejected

## Prerequisites
- Aktor: Rina W, Total Control, tidak menjadi Last Holder record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-015-1: Record Waiting for Confirmation `Barcode Scanner Honeywell {runId}`, Asset ID `BCS-015-0001`, Group `Warehouse`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Budi S`, Reported By `Budi S`, Reported Date `T0 − 1 hari, pukul 08:30`. Node: `Reported missing by Budi S` dengan What happened `Barcode scanner tidak ada di meja kasir gudang`.
  - DU-015-2: Record Missing `Fire Extinguisher Amerex {runId}`, Asset ID `FEX-015-0002`, Group `Warehouse`, Status `Missing`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 4 hari, pukul 09:00`, tidak diubah spec ini.
  - Pengguna pada data: Rina W, Total Control, seluruh client; Budi S, pemegang yang memakai akun sendiri.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`.

## Test Steps

### Footer Reject membuka dialog Reject Report
1. Ketik Search `{runId}`, tekan Enter
2. Klik `⋯` pada baris `Barcode Scanner Honeywell {runId}`
3. Klik `Review`
4. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog `Missing Log` record `Barcode Scanner Honeywell {runId}`
5. Verifikasi `Next` aktif karena tabel sub-tab Active masih memuat record `Fire Extinguisher Amerex {runId}`
6. Klik `[Reject]` pada footer dialog `Missing Log`
7. Verifikasi dialog `Reject Report` terbuka
8. Verifikasi dialog `Reject Report` memuat nama aset `Barcode Scanner Honeywell {runId}`

### Reject dengan Reason sepanjang batas menutup kedua dialog
9. Isi Reason `Aset terlihat kembali di ruang gudang lantai 2 saat pengecekan rutin sehingga laporan kehilangan dari pemegang tidak perlu dilanjutkan sebagai kehilangan resmi dan catatan ini ditulis lengkap supaya admin berikutnya memahami alasan penolakan laporan Aset terlihat kembali di ruang gudang lantai 2 saat pengecekan rutin sehingga laporan kehilangan dari pemegan.` (360 karakter)
10. Klik `[Reject]` pada dialog `Reject Report`
11. Verifikasi toast `Success, report has been rejected.` tampil
12. Verifikasi dialog `Reject Report` dan dialog `Missing Log` tertutup
13. Verifikasi baris `Fire Extinguisher Amerex {runId}` tetap tampil di sub-tab Active
14. Verifikasi baris `Barcode Scanner Honeywell {runId}` tidak tampil lagi di sub-tab Active

### Record pindah ke History sebagai Rejected
15. Klik sub-tab `History`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris `Barcode Scanner Honeywell {runId}` tampil di sub-tab History dengan Status `Rejected`
18. Klik nama `Barcode Scanner Honeywell {runId}` pada kolom Name
19. Verifikasi node `Report rejected by Rina W` memuat Reason `Aset terlihat kembali di ruang gudang lantai 2 saat pengecekan rutin sehingga laporan kehilangan dari pemegang tidak perlu dilanjutkan sebagai kehilangan resmi dan catatan ini ditulis lengkap supaya admin berikutnya memahami alasan penolakan laporan Aset terlihat kembali di ruang gudang lantai 2 saat pengecekan rutin sehingga laporan kehilangan dari pemegan.` (360 karakter)

### Siblings dihitung ulang dari baris Active yang tersisa
20. Klik `✕` pada dialog Missing Log
21. Klik sub-tab `Active`
22. Ketik Search `{runId}`, tekan Enter
23. Klik nama `Fire Extinguisher Amerex {runId}` pada kolom Name
24. Verifikasi `Prev` Disabled karena record `Fire Extinguisher Amerex {runId}` menjadi baris pertama tabel sub-tab Active
25. Verifikasi `Next` Disabled karena tidak ada record lain di tabel sub-tab Active
