---
id: TC-FA-MISS-UI-058-dialog-missing-log-klien
title: "Dialog Missing Log: judul, tanpa record id, parties, badge status dan penanda, footer Review per kondisi, Confirm memperbarui dialog, Reject membuka D-MIS-04"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§8.1#p1, §8.1#r1, §8.1#r2, §8.1#r3, §8.1#r4, §8.1#r5, §8.1#r6, §4.2.4#r19, §4.2.4#r20, §4.4#r4, §4.4#r5, §4.4#r6, §4.1#r4, §4.1a#r31, §7.2#r15, §7.3#r7, §9.6#r2, §4.3#r4, §6#r1, §4.5#p1, EB-TBL-5@aksi-last-holder, EB-FB-1@confirm, EB-ERR-1@confirm, EB-FB-2@tutup-missing-log, §1.2#r113]
smoke: []
dependsOn: []
trace:
  §8.1#p1: [8, 11, 17]
  §8.1#r1: 2
  §8.1#r2: 4
  §8.1#r3: 3
  §8.1#r4: 5
  §8.1#r5: [6, 10, 12, 14, 15]
  §8.1#r6: [8, 17, 19, 21, 33]
  §4.2.4#r19: [27, 28, 29, 30]
  §4.2.4#r20: [33, 37, 38]
  §4.4#r4: 8
  §4.4#r5: [26, 27, 28, 29, 30]
  §4.4#r6: [33, 36, 37, 38]
  §4.1#r4: 7
  §4.1a#r31: 8
  §7.2#r15: [33, 36, 37]
  §7.3#r7: [26, 36, 41]
  §9.6#r2: [26, 41, 42, 43]
  §4.3#r4: [17, 19, 21]
  §6#r1: [17, 19, 21]
  §4.5#p1: [6, 10, 15, 23, 57, 59, 61, 63, 64]
  EB-TBL-5@aksi-last-holder: [19, 21, 23]
  EB-FB-1@confirm: [26, 41]
  EB-ERR-1@confirm: [41, 42, 44, 46, 49, 50, 51]
  EB-FB-2@tutup-missing-log: [53, 55, 56]
  §1.2#r113: [66, 68, 69]
anchor: []
coverage:
  web: automated
---
# Dialog Missing Log: judul, tanpa record id, parties, badge status dan penanda, footer Review per kondisi, Confirm memperbarui dialog, Reject membuka D-MIS-04

## Prerequisites
- Aktor: Aktor Missing pada Group aset yang bukan Last holder; Sari D sebagai Aktor Missing sekaligus Last holder untuk K2.
- Layar awal: halaman Missing, tab Active.
- Komponen: Dialog Missing Log
- Data:
  - DU-058-1: Record `Monitor LG 27UL500 - 11`, Asset ID `MON-2026-0011`, Group `Head Office`, status record `Waiting for Confirmation`, Last Holder `Sari D`, Reported By `Sari D`.
  - DU-058-2: Record `Laptop Dell Latitude 5420 - 22`, Asset ID `LPT-2026-0022`, Group `Finance Room`, status record `Missing`, Last Holder `Andi P`, Reported By `Andi P`.
  - DU-058-3: Record `Laptop Lenovo ThinkPad T14 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, status record `Missing`, penanda `Long missing`, Last Holder `Dewi A`, Reported By `Rina W`.
  - DU-058-5: Record `Printer HP LaserJet M404 - 5`, Asset ID `PRN-2026-0005`, Group `Head Office`, status record `Waiting for Confirmation`, Last Holder `Andi P`, Reported By `Andi P`, sudah punya node `Detected by scan` pada tanggal `08/11/26`.
- Kondisi:
  - K1: dialog dibuka untuk record DU-058-1 oleh Aktor Missing yang bukan Last holder; Confirm dan Reject berhasil.
  - K2: dialog dibuka untuk record DU-058-1 oleh Sari D sebagai Last holder.
  - K3: dialog dibuka untuk record DU-058-2.
  - K4: dialog dibuka untuk record DU-058-3.
  - K5: dialog dibuka untuk record DU-058-1 oleh Aktor Missing yang bukan Last holder; Confirm pertama gagal karena error server, Confirm berikutnya berhasil.
  - K6: dialog dibuka untuk record DU-058-1 oleh Aktor Missing yang bukan Last holder; Confirm gagal karena timeout.
  - K7: dialog dibuka untuk record DU-058-5 oleh Aktor Missing yang bukan Last holder; Date Format bernilai `DD/MM/YY`.

## Test Steps

### Tampilan awal record Waiting for Confirmation bagi Aktor Missing
1. Tampilkan Dialog Missing Log dengan kondisi K1
2. Verifikasi judul dialog `Missing Log`
3. Verifikasi dialog memuat record `Monitor LG 27UL500 - 11` yang dibuka dari baris tabel Active
4. Verifikasi dialog tidak menampilkan nomor transaksi record
5. Verifikasi label `Last Holder` dan `Reported By` tampil
6. Verifikasi badge status record `Waiting for Confirmation` tampil
7. Verifikasi dialog memuat daftar peristiwa record
8. Verifikasi footer dialog memuat tombol `[Reject]` dan `[Confirm]` yang aktif

### Record Missing tanpa penanda Long missing
9. Tampilkan Dialog Missing Log dengan kondisi K3
10. Verifikasi badge status record `Missing` tampil
11. Verifikasi footer dialog tidak memuat tombol `[Reject]` dan `[Confirm]`
12. Verifikasi penanda `Long missing` tidak tampil

### Record Missing dengan penanda Long missing
13. Tampilkan Dialog Missing Log dengan kondisi K4
14. Verifikasi badge status record `Missing` tampil
15. Verifikasi penanda `Long missing` tampil

### Last holder: Confirm dan Reject Disabled dengan alasan
16. Tampilkan Dialog Missing Log dengan kondisi K2
17. Verifikasi tombol `[Reject]` dan `[Confirm]` disabled
18. Arahkan kursor ke tombol `[Confirm]`
19. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada tombol `[Confirm]` yang disabled
20. Arahkan kursor ke tombol `[Reject]`
21. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada tombol `[Reject]` yang disabled
22. Tekan Tab hingga fokus melewati footer dialog
23. Verifikasi tombol `[Confirm]` dan `[Reject]` yang disabled tidak menerima fokus keyboard[^drift-1]

### Confirm langsung memperbarui dialog
24. Tampilkan Dialog Missing Log dengan kondisi K1
25. Klik `[Confirm]`
26. Verifikasi toast `Success, report has been confirmed.` tampil
27. Verifikasi tidak ada dialog kedua yang tampil
28. Verifikasi dialog Missing Log tetap terbuka
29. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak tampil lagi di footer
30. Verifikasi badge status record `Missing` tampil

### Reject membuka Reject Report dan menutup kedua dialog
31. Tampilkan Dialog Missing Log dengan kondisi K1
32. Klik `[Reject]`
33. Verifikasi dialog `Reject Report` tampil
34. Isi Reason `Aset masih tercatat dipegang oleh pelapor`
35. Klik `[Reject]` pada dialog Reject Report
36. Verifikasi toast `Success, report has been rejected.` tampil
37. Verifikasi dialog Reject Report tertutup
38. Verifikasi dialog Missing Log tertutup

### Confirm gagal karena error server: dialog dipertahankan dan submit ulang berhasil
39. Tampilkan Dialog Missing Log dengan kondisi K5
40. Klik `[Confirm]`
41. Verifikasi toast `Error, failed to confirm report.` tampil
42. Verifikasi dialog Missing Log tetap terbuka
43. Verifikasi badge status record tetap `Waiting for Confirmation`
44. Verifikasi `[Confirm]` aktif lagi
45. Klik `[Confirm]`
46. Verifikasi toast `Success, report has been confirmed.` tampil

### Confirm gagal karena timeout
47. Tampilkan Dialog Missing Log dengan kondisi K6
48. Klik `[Confirm]`
49. Verifikasi toast `Connection problem. Please try again.` tampil setelah Confirm pada dialog Missing Log
50. Verifikasi dialog Missing Log tetap terbuka
51. Verifikasi `[Confirm]` aktif lagi

### Dialog ditutup dengan tombol silang tanpa toast
52. Tampilkan Dialog Missing Log dengan kondisi K1
53. Verifikasi tombol `✕` tampil pada dialog Missing Log
54. Klik `✕` pada dialog
55. Verifikasi dialog Missing Log tertutup
56. Verifikasi tidak ada toast yang tampil
57. Verifikasi fokus kembali ke elemen pemicu dialog Missing Log

### Dialog dapat dioperasikan dengan keyboard
58. Tampilkan Dialog Missing Log dengan kondisi K1
59. Verifikasi fokus berada di dalam dialog Missing Log
60. Tekan Tab sepuluh kali berturut-turut
61. Verifikasi fokus tetap berada di dalam dialog Missing Log
62. Tekan Esc
63. Verifikasi dialog Missing Log tertutup
64. Verifikasi fokus kembali ke elemen pemicu dialog Missing Log

### Confirm Disabled pada record yang sudah dideteksi scan
65. Tampilkan Dialog Missing Log dengan kondisi K7
66. Verifikasi tombol `[Confirm]` disabled
67. Arahkan kursor ke tombol `[Confirm]`
68. Verifikasi alasan `This asset was scanned on 08/11/26. Reject the report or mark it as found.` tersampaikan pada tombol `[Confirm]` yang disabled
69. Verifikasi tombol `[Reject]` aktif

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.5: «Tooltip Disabled 🔖 dapat diakses lewat fokus.»; kontrak `Tooltip#38`: «A disabled control cannot be focused, so its tooltip opens on hover only.» (juga `Button#2`: tombol disabled tidak bisa menerima fokus). Diasersi: kontrak, sehingga alasan pada tombol disabled dibuka lewat hover dan tombol disabled tidak menerima fokus keyboard (SB-7).
