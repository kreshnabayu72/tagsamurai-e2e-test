---
id: TC-FA-BORROW-E2E-011-transaction-rules-dialog
title: "Dialog Transaction Rules menampilkan batas efektif baris dan progres approval per putaran"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EC-BRW-107", "EC-BRW-108", "§4.2.8#p1", "§4.2.8#p2", "§4.2.8#b1", "§4.2.8#b2", "§4.2.8#b3", "§4.2.8#b4", "§4.2.8#b5", "§4.2.8#b6", "§4.2.8#b7", "§4.2.8#b8", "§4.2.8#b9", "§4.2.8#b10", "§4.2.8#b11", "§4.2.8#b12", "§4.2.8#b13", "§4.2.8#b14", "§4.4#r14"]
smoke: []
dependsOn: []
trace:
  "EC-BRW-107": [35, 36]
  "EC-BRW-108": [48, 52, 70]
  "§4.2.8#p1": [6, 7]
  "§4.2.8#p2": [5, 6, 8, 57]
  "§4.2.8#b1": [9, 13]
  "§4.2.8#b2": [9, 13, 14]
  "§4.2.8#b3": [19, 23]
  "§4.2.8#b4": [27, 31]
  "§4.2.8#b5": [8, 57]
  "§4.2.8#b6": [48, 52, 59, 61, 63]
  "§4.2.8#b7": [31, 61]
  "§4.2.8#b8": [58]
  "§4.2.8#b9": [15]
  "§4.2.8#b10": [35, 36]
  "§4.2.8#b11": [40]
  "§4.2.8#b12": [44]
  "§4.2.8#b13": [70, 71]
  "§4.2.8#b14": [56]
  "§4.4#r14": [5]
anchor: []
coverage:
  web: automated
---

# Dialog Transaction Rules menampilkan batas efektif baris dan progres approval per putaran

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-011-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-011-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - Pengaju: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`.
  - DU-011-4: user `Bayu Anggoro`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-5: user `Dwi Rahayu`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-6: user `Eko Santoso`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-7: user `Farah Nabila`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-8: user `Galih Prakoso`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-9: user `Hendra Saputra`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-10: user `Maria Ulfa`, pemegang Role Transaksi Approver di Group `Head Office`.
  - DU-011-11: user `Siti Rahmawati`, Group Manager Group `Head Office`.
  - DU-011-2: BRW Borrower `Wawan Kurniawan` (tampil `Wawan K`), Group `Head Office`, pengaju `Agus P`, memuat 12 aset ber-Category `Peralatan Kantor` dengan aturan efektif Max duration `7 days`, Max extensions `3`, dan Photo requirement. Aset dan keadaan approval-nya:
    - `Aset Rules 01 Menunggu Any One {runId}`: Waiting for Approval, Approval type `Any one approver`, approver `Bayu Anggoro`, `Hendra Saputra`, dan `Maria Ulfa` seluruhnya belum memutuskan.
    - `Aset Rules 02 Disetujui Any One {runId}`: Waiting for Handover, Approval type `Any one approver`, approver yang sama; `Hendra Saputra` menyetujui dengan Approval Note `Disetujui untuk keperluan kantor` dan Approve Duration `5 days`.
    - `Aset Rules 03 All Parsial {runId}`: Waiting for Approval, Approval type `All approvers`, approver `Bayu Anggoro` (sudah menyetujui), `Hendra Saputra`, dan `Maria Ulfa` (belum memutuskan).
    - `Aset Rules 04 All Ditolak {runId}`: Rejected, Approval type `All approvers`, `Bayu Anggoro` menyetujui, `Hendra Saputra` menolak, `Maria Ulfa` belum bertindak.
    - `Aset Rules 05 Dibatalkan {runId}`: Canceled oleh `Agus Pratama` lewat Cancel Borrow, Approval type `All approvers`, `Bayu Anggoro` sudah menyetujui, `Hendra Saputra` dan `Maria Ulfa` belum bertindak.
    - `Aset Rules 06 Timeout {runId}`: Canceled oleh System dengan Reason `Timed out (Waiting for Approval)`, Approval type `Any one approver`, approver `Bayu Anggoro` dan `Maria Ulfa` belum bertindak.
    - `Aset Rules 07 Override {runId}`: Waiting for Handover, Approval type `Any one approver`, approver snapshot `Bayu Anggoro` dan `Maria Ulfa`; keputusan Approved diambil `Siti Rahmawati` lewat override Group Manager.
    - `Aset Rules 08 Dirutekan {runId}`: Waiting for Approval, daftar approver snapshot kosong sejak Submit sehingga dirutekan ke Group Manager `Siti Rahmawati`.
    - `Aset Rules 09 Banyak Approver {runId}`: Waiting for Approval, Approval type `All approvers`, tujuh approver `Bayu Anggoro`, `Dwi Rahayu`, `Eko Santoso`, `Farah Nabila`, `Galih Prakoso`, `Hendra Saputra`, dan `Maria Ulfa`, seluruhnya belum memutuskan.
    - `Aset Rules 10 Tanpa Approval {runId}`: Waiting for Handover, Require approval OFF sehingga Approval `Not required`.
    - `Aset Rules 11 Auto Approved {runId}`: Waiting for Handover, memenuhi Auto-approve sehingga Approval `Auto-approved`.
    - `Aset Rules 12 Extension {runId}`: Borrowed dengan tiga putaran: Borrow (disetujui `Bayu Anggoro`, Approval type `Any one approver`), Extension 1 (Extend by `2 days`, Approval type `All approvers`, `Hendra Saputra` menolak dan `Maria Ulfa` belum bertindak), dan Extension 2 (Extend by `3 days`, Approval type `Any one approver`, `Bayu Anggoro` dan `Maria Ulfa` belum memutuskan).
  - DU-011-3: Draft Borrower `Pandu Nugraha` (tampil `Pandu N`), Group `Head Office`, aset `Aset Rules 13 Draft {runId}`.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal dan waktu.

## Test Steps

### Dialog Transaction Rules dibuka dari baris aset
1. Ketik Search `{runId}`, tekan Enter
2. Klik Transaction ID baris Borrower `Wawan K`
3. Klik `⋯` pada baris aset `Aset Rules 01 Menunggu Any One {runId}`
4. Klik `Transaction Rules`
5. Verifikasi dialog `Transaction Rules` terbuka dengan Asset `Aset Rules 01 Menunggu Any One {runId}`
6. Verifikasi dialog memuat `Max duration` `7 days`, `Max extensions` `3`, dan `Photo requirement`
7. Verifikasi dialog tidak menampilkan versi setting dan tidak memiliki tombol `Close`, dan dapat ditutup lewat ikon silang
8. Verifikasi Approval menampilkan `Needs approval`, Approval type `Any one approver`, dan bagian `Approval Progress` memuat blok `Borrow`
9. Verifikasi approver `Bayu Anggoro`, `Hendra Saputra`, dan `Maria Ulfa` tampil berurutan A–Z dengan status `Waiting for Approval`
10. Tutup dialog `Transaction Rules` lewat ikon silang

### Any one approver: satu memutuskan, lainnya Not Involved
11. Klik `⋯` pada baris aset `Aset Rules 02 Disetujui Any One {runId}`
12. Klik `Transaction Rules`
13. Verifikasi approver `Hendra Saputra` berstatus `Approved` disertai waktu keputusan
14. Verifikasi approver `Bayu Anggoro` dan `Maria Ulfa` berstatus `Not Involved`
15. Verifikasi dialog tidak menampilkan Approval Note `Disetujui untuk keperluan kantor` maupun Approve Duration `5 days`
16. Tutup dialog `Transaction Rules` lewat ikon silang

### All approvers: status per approver, penolakan, dan pembatalan
17. Klik `⋯` pada baris aset `Aset Rules 03 All Parsial {runId}`
18. Klik `Transaction Rules`
19. Verifikasi Approval type `All approvers`, `Bayu Anggoro` berstatus `Approved`, serta `Hendra Saputra` dan `Maria Ulfa` berstatus `Waiting for Approval`
20. Tutup dialog `Transaction Rules` lewat ikon silang
21. Klik `⋯` pada baris aset `Aset Rules 04 All Ditolak {runId}`
22. Klik `Transaction Rules`
23. Verifikasi `Hendra Saputra` berstatus `Rejected` dan `Maria Ulfa` yang belum bertindak berstatus `Not Involved`
24. Tutup dialog `Transaction Rules` lewat ikon silang
25. Klik `⋯` pada baris aset `Aset Rules 05 Dibatalkan {runId}`
26. Klik `Transaction Rules`
27. Verifikasi `Bayu Anggoro` tetap `Approved` dengan waktunya, `Hendra Saputra` dan `Maria Ulfa` berstatus `Not Involved`, dan keterangan `Canceled by Agus Pratama` tampil dengan waktunya
28. Tutup dialog `Transaction Rules` lewat ikon silang
29. Klik `⋯` pada baris aset `Aset Rules 06 Timeout {runId}`
30. Klik `Transaction Rules`
31. Verifikasi `Bayu Anggoro` dan `Maria Ulfa` berstatus `Not Involved` dan keterangan `Canceled by system (Timed out (Waiting for Approval))` tampil dengan waktunya
32. Tutup dialog `Transaction Rules` lewat ikon silang

### Override Group Manager dan approval yang dirutekan ulang
33. Klik `⋯` pada baris aset `Aset Rules 07 Override {runId}`
34. Klik `Transaction Rules`
35. Verifikasi `Siti Rahmawati` tampil sebagai baris tambahan berstatus `Approved` dengan keterangan `Group Manager override`
36. Verifikasi `Bayu Anggoro` dan `Maria Ulfa` berstatus `Not Involved`
37. Tutup dialog `Transaction Rules` lewat ikon silang
38. Klik `⋯` pada baris aset `Aset Rules 08 Dirutekan {runId}`
39. Klik `Transaction Rules`
40. Verifikasi `Siti Rahmawati` tampil sebagai penerima dengan keterangan `Routed to Group Manager`
41. Tutup dialog `Transaction Rules` lewat ikon silang

### Banyak approver tampil semua tanpa dipotong
42. Klik `⋯` pada baris aset `Aset Rules 09 Banyak Approver {runId}`
43. Klik `Transaction Rules`
44. Verifikasi ketujuh nama `Bayu Anggoro`, `Dwi Rahayu`, `Eko Santoso`, `Farah Nabila`, `Galih Prakoso`, `Hendra Saputra`, dan `Maria Ulfa` tampil lengkap dalam daftar yang dapat di-scroll
45. Tutup dialog `Transaction Rules` lewat ikon silang

### Aset tanpa approval dan yang lolos Auto-approve
46. Klik `⋯` pada baris aset `Aset Rules 10 Tanpa Approval {runId}`
47. Klik `Transaction Rules`
48. Verifikasi Approval menampilkan `Not required` tanpa Approval type dan tanpa daftar approver
49. Tutup dialog `Transaction Rules` lewat ikon silang
50. Klik `⋯` pada baris aset `Aset Rules 11 Auto Approved {runId}`
51. Klik `Transaction Rules`
52. Verifikasi Approval menampilkan `Auto-approved` tanpa Approval type dan tanpa daftar approver
53. Tutup dialog `Transaction Rules` lewat ikon silang

### Aset dengan putaran Extension
54. Klik `⋯` pada baris aset `Aset Rules 12 Extension {runId}`
55. Klik `Transaction Rules`
56. Verifikasi Approval di atas bagian `Approval Progress` mengikuti putaran terakhir: `Needs approval` dengan Approval type `Any one approver`
57. Verifikasi bagian `Approval Progress` memuat blok `Extension 2`, `Extension 1`, dan `Borrow` dengan blok terbaru di atas
58. Verifikasi blok `Extension 2` terbuka dan blok `Extension 1` serta `Borrow` terlipat
59. Verifikasi blok `Extension 2` memuat `Extend by 3 days`, Approval type `Any one approver`, serta approver `Bayu Anggoro` dan `Maria Ulfa` berstatus `Waiting for Approval`
60. Klik blok `Extension 1`
61. Verifikasi blok `Extension 1` memuat `Extend by 2 days`, Approval type `All approvers`, `Hendra Saputra` berstatus `Rejected`, dan `Maria Ulfa` berstatus `Not Involved`
62. Klik blok `Borrow`
63. Verifikasi blok `Borrow` memuat Approval type `Any one approver` dan `Bayu Anggoro` berstatus `Approved`
64. Tutup dialog `Transaction Rules` lewat ikon silang

### Varian Draft dari form Borrow Request
65. Klik tab `Drafts`
66. Ketik Search `{runId}`, tekan Enter
67. Klik Borrower `Pandu N`
68. Klik `⋯` pada baris aset `Aset Rules 13 Draft {runId}`
69. Klik `Transaction Rules`
70. Verifikasi dialog `Transaction Rules` menampilkan nilai efektif aset dan keterangan `Final rules are fixed when you submit`
71. Verifikasi dialog tidak memuat bagian `Approval Progress`
72. Tutup dialog `Transaction Rules` lewat ikon silang
73. Klik `[Cancel]` pada form yang belum diubah
