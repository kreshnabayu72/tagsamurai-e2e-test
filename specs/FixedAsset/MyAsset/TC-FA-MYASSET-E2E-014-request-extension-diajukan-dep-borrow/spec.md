---
id: TC-FA-MYASSET-E2E-014-request-extension-diajukan-dep-borrow
title: "Request Extension dari tab Borrowed: pengajuan menunggu review dan baris berstatus Extension Request"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["§1.2#r58", "§1.2#r63", "§1.2#r64", "§1.2#r65", "§1.2#r66", "§1.2#r67", "§2.1#r5", "§3#p11", "§4.1b#r35", "§4.1b#r39", "§4.2.1#b6", "§4.2.3#p1", "§4.3#r7", "§4.4#r2", "§4.4#r4", "§4.8#r7", "§7.3#r5", "§9.2#b7", "§9.4.2#r41", "§9.4.2#r43", "§9.6#r3", "§9.7#r4"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r58": [17, 18]
  "§1.2#r63": 9
  "§1.2#r64": 17
  "§1.2#r65": [13, 14]
  "§1.2#r66": 19
  "§1.2#r67": 22
  "§2.1#r5": 17
  "§3#p11": [10, 13, 14, 17, 31, 33, 35, 36]
  "§4.1b#r35": [4, 7]
  "§4.1b#r39": [9, 17]
  "§4.2.1#b6": [13, 26]
  "§4.2.3#p1": [9, 10, 11, 31, 33]
  "§4.3#r7": [21, 22]
  "§4.4#r2": [15, 16, 50, 51, 52, 53, 54, 58, 59, 60, 61, 62]
  "§4.4#r4": [9, 13, 14]
  "§4.8#r7": 7
  "§7.3#r5": 13
  "§9.2#b7": [10, 31, 33]
  "§9.4.2#r41": 22
  "§9.4.2#r43": 21
  "§9.6#r3": [13, 14]
  "§9.7#r4": 17
anchor: []
coverage:
  web: automated
---

# Request Extension dari tab Borrowed: pengajuan menunggu review dan baris berstatus Extension Request

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-014-1: Pinjaman milik Borrower berstatus `Borrowed`, Source `Admin`, satu aset: Name `Laptop Lenovo ThinkPad E14 {runId}`, Asset ID `LPT-E14-{runId}`, Brand `Lenovo`, Model/Type `ThinkPad E14`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-014-2: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Proyektor Epson EB-X49 {runId}`, Asset ID `PRJ-X49-{runId}`, Brand `Epson`, Model/Type `EB-X49`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-014-3: Pinjaman milik Borrower yang sama dari BRW lain, berbeda dari BRW DU-014-2, berstatus `Borrowed`, Source `Admin`, satu aset: Name `Kamera Canon EOS 90D {runId}`, Asset ID `CAM-90D-{runId}`, Brand `Canon`, Model/Type `EOS 90D`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-014-4: `11` pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, masing-masing satu aset: Name `Monitor Philips 24 inci {n} {runId}`, Asset ID `MON-PH-{n}-{runId}`, Brand `Philips`, Model/Type `243V7`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - Dengan Search `{runId}` dan Filter Brand `Philips`, tabel Borrowed memuat `11` baris, sehingga pada rows per page `10` halaman `1` memuat `10` baris dan halaman `2` memuat satu baris.

## Test Steps

### Request Extension satu baris: halaman Extension Request, toast, status, dan state list sesudah kembali
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Pilih rows per page `25`
4. Verifikasi baris `Laptop Lenovo ThinkPad E14 {runId}` berstatus `Borrowed`
5. Catat Due Date baris `Laptop Lenovo ThinkPad E14 {runId}`
6. Klik `⋯` pada baris `Laptop Lenovo ThinkPad E14 {runId}`
7. Verifikasi opsi `Request Extension` tersedia pada menu baris
8. Klik `Request Extension`
9. Verifikasi breadcrumb `My Asset > Borrowed > Extension Request` tampil
10. Verifikasi tabel halaman Extension Request memuat aset `Laptop Lenovo ThinkPad E14 {runId}`
11. Verifikasi tabel halaman Extension Request tidak memuat kolom `Extensions` dan `Max Duration`
12. Klik `[Submit Request]`
13. Verifikasi toast `Success, extension request has been sent to the Asset Admin for review.` tampil
14. Verifikasi tab `Borrowed` aktif sesudah halaman kembali ke My Asset
15. Verifikasi kotak Search tetap berisi `{runId}`
16. Verifikasi rows per page tetap `25`
17. Verifikasi baris `Laptop Lenovo ThinkPad E14 {runId}` berstatus `Extension Request`
18. Verifikasi kolom Remaining baris `Laptop Lenovo ThinkPad E14 {runId}` tidak memuat `Extension`
19. Verifikasi Due Date baris `Laptop Lenovo ThinkPad E14 {runId}` sama dengan Due Date yang dicatat
20. Klik `⋯` pada baris `Laptop Lenovo ThinkPad E14 {runId}`
21. Verifikasi opsi `Cancel Extension Request` tersedia pada menu baris
22. Verifikasi opsi `Request Extension` tidak tersedia pada menu baris
23. Klik tab `Task`
24. Klik tab `Borrowed`
25. Muat ulang halaman
26. Verifikasi toast `Success, extension request has been sent to the Asset Admin for review.` tidak tampil lagi

### Aset pinjaman lain milik Borrower ditambahkan lewat [+ Asset] pada halaman Extension Request
27. Ganti isi kotak search dengan `{runId}`, tekan Enter
28. Klik `⋯` pada baris `Proyektor Epson EB-X49 {runId}`
29. Klik `Request Extension`
30. Klik `[+ Asset]`
31. Verifikasi daftar kandidat memuat aset `Kamera Canon EOS 90D {runId}` dari BRW lain milik Borrower yang sama
32. Tambahkan aset `Kamera Canon EOS 90D {runId}` dari daftar kandidat ke tabel Extension Request
33. Verifikasi tabel halaman Extension Request memuat aset `Proyektor Epson EB-X49 {runId}` dan `Kamera Canon EOS 90D {runId}`
34. Klik `[Submit Request]`
35. Verifikasi baris `Proyektor Epson EB-X49 {runId}` berstatus `Extension Request`
36. Verifikasi baris `Kamera Canon EOS 90D {runId}` berstatus `Extension Request`

### State list tab Borrowed dipertahankan saat kembali dari halaman Extension Request lewat Cancel dan breadcrumb
37. Ganti isi kotak search dengan `{runId}`, tekan Enter
38. Pilih rows per page `10`
39. Urutkan kolom `Name` dari A ke Z
40. Klik ikon `Filter` pada toolbar
41. Klik field `Brand`
42. Centang opsi `Philips`
43. Tekan `Esc` untuk menutup daftar opsi
44. Klik `[Apply]`
45. Pindah ke halaman `2` pada Pagination
46. Catat Name baris yang tampil di halaman `2`
47. Klik `⋯` pada baris yang dicatat
48. Klik `Request Extension`
49. Klik `[Cancel]` pada halaman Extension Request
50. Verifikasi kotak Search tetap berisi `{runId}`
51. Verifikasi kolom `Name` tetap terurut dari A ke Z
52. Verifikasi Filter Brand `Philips` tetap ter-Apply
53. Verifikasi halaman aktif tetap `2` dan memuat baris yang dicatat
54. Verifikasi rows per page tetap `10`
55. Klik `⋯` pada baris yang dicatat
56. Klik `Request Extension`
57. Klik breadcrumb `Borrowed`
58. Verifikasi kotak Search tetap berisi `{runId}`
59. Verifikasi kolom `Name` tetap terurut dari A ke Z
60. Verifikasi Filter Brand `Philips` tetap ter-Apply
61. Verifikasi halaman aktif tetap `2` dan memuat baris yang dicatat
62. Verifikasi rows per page tetap `10`
