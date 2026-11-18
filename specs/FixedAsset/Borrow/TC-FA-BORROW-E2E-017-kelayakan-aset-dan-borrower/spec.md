---
id: TC-FA-BORROW-E2E-017-kelayakan-aset-dan-borrower
title: "Kelayakan aset dan Borrower ditampilkan sebagai alasan tidak layak di form, Draft, dan Select Borrower"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-29", "FI-BRW-30", "FI-BRW-31", "FI-BRW-32", "V-BRW-01", "V-BRW-02", "V-BRW-03", "V-BRW-04", "V-BRW-05", "V-BRW-06", "V-BRW-08", "V-BRW-09", "V-BRW-10", "V-BRW-11", "V-BRW-12", "V-BRW-13", "V-BRW-14", "V-BRW-40", "V-BRW-41", "V-BRW-42", "V-BRW-43", "V-BRW-44", "V-BRW-45", "V-BRW-46", "§4.8#p2", "§6#p1", "EB-CON-4"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-29": 30
  "FI-BRW-30": 31
  "FI-BRW-31": 33
  "FI-BRW-32": 37
  "V-BRW-01": 7
  "V-BRW-02": 8
  "V-BRW-03": 14
  "V-BRW-04": [5, 20, 22, 24]
  "V-BRW-05": 8
  "V-BRW-06": 65
  "V-BRW-08": 30
  "V-BRW-09": [10, 11]
  "V-BRW-10": 9
  "V-BRW-11": [12, 19]
  "V-BRW-12": 71
  "V-BRW-13": 49
  "V-BRW-14": [37, 42]
  "V-BRW-40": 6
  "V-BRW-41": 7
  "V-BRW-42": 8
  "V-BRW-43": 9
  "V-BRW-44": 10
  "V-BRW-45": 11
  "V-BRW-46": 12
  "§4.8#p2": 10
  "§6#p1": 13
  "EB-CON-4": [71, 75]
anchor: [4]
coverage:
  web: automated
---

# Kelayakan aset dan Borrower ditampilkan sebagai alasan tidak layak di form, Draft, dan Select Borrower

## Prerequisites
- Aktor: Asset Admin `Asset Admin Kelayakan {runId}` (Aktor Borrow) dengan Group penugasan `Head Office` dan `Branch Surabaya`.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-017-1: Aktor `Asset Admin Kelayakan {runId}`, role Asset Admin, Group penugasan `Head Office` dan `Branch Surabaya`.
  - DU-017-2: Borrower `Pratiwi Borrower {runId}`, Email `pratiwi.borrower{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-017-3: Borrower `Surya Surabaya {runId}`, Email `surya.surabaya{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Branch Surabaya`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-017-4: Borrower `Edo Terlambat {runId}`, Email `edo.terlambat{runId}@example.com`, Position `Operator {runId}`, Division `Warehouse {runId}`, Home Group `Head Office`, akun ber-login aktif, Active Borrows `1 asset` berstatus Overdue (Due date T0 − 3 hari); alasan Blocked `Edo Terlambat {runId} has an overdue borrow: [Asset Code], due [Date]. Return it first.`.
  - DU-017-5: Borrower `Lukman Resign {runId}`, Email `lukman.resign{runId}@example.com`, Home Group `Head Office`, karyawan sudah dinonaktifkan sesudah Draft disimpan; pesan di field Borrower `Lukman Resign {runId} is no longer active. Pick another borrower.`.
  - DU-017-6: karyawan tanpa akun login `Wawan Tanpa PIC {runId}`, Email `wawan.tanpapic{runId}@example.com`, Home Group `Head Office`, PIC sudah dikosongkan sesudah Draft disimpan; pesan di field Borrower `Wawan Tanpa PIC {runId} has no login account and no PIC. Set a PIC in Users first.`; alasan Blocked di Select Borrower `No login account and no PIC. Set a PIC in Users first.`.
  - DU-017-7: Borrower `Citra Batas {runId}`, Email `citra.batas{runId}@example.com`, Home Group `Head Office`, akun ber-login aktif, Active Borrows `9 assets`; pesan batas `Citra Batas {runId} can borrow up to 10 assets at a time.`.
  - DU-017-8: pemegang hak Manage asset & TAG `Rizal Manager {runId}`, kontak pada alasan Deny pada override.
  - DU-017-9: aset `Laptop Lenovo Yoga {runId}` sudah dihapus (Deleted); tooltip `This asset has been deleted.`.
  - DU-017-10: aset `Tablet Samsung Tab {runId}` berstatus Condition `Damaged`; tooltip `This asset is Damaged and can't be borrowed.`.
  - DU-017-11: aset `Genset Honda {runId}` sedang ada di BRW lain; tooltip `This asset is already in another transaction.`.
  - DU-017-12: aset `Scanner Zebra {runId}` dengan TAG yang perlu diganti; tooltip `This asset can't be borrowed until its TAG is replaced.`.
  - DU-017-13: aset `Drone DJI Air {runId}` dengan Deny pada override aset; tooltip `Can't be borrowed: this asset is not available for borrowing. Contact Rizal Manager {runId} (Manage asset & TAG).`.
  - DU-017-14: aset `Forklift Toyota {runId}` dengan Category `Heavy Machine {runId}` yang Allow Borrow efektifnya Deny; tooltip `Borrowing isn't allowed for Heavy Machine {runId}.`.
  - DU-017-15: aset `Bus Hino {runId}` di Group `Branch Surabaya` dengan Allowed borrower `Same Group only`; tooltip bagi Borrower `Pratiwi Borrower {runId}` `Pratiwi Borrower {runId} can't borrow assets from Branch Surabaya.`.
  - DU-017-16: aset `Kamera Fujifilm {runId}` dengan TAG yang perlu diganti dan Deny pada override sekaligus; tooltip yang tampil `This asset can't be borrowed until its TAG is replaced.`.
  - DU-017-17: aset `Printer Brother {runId}` layak: Custody `Available`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`.
  - DU-017-18: aset `Printer Canon {runId}` di Group `Branch Medan` (di luar Group penugasan Aktor), Custody `Available`.
  - DU-017-19: Draft untuk Borrower `Pratiwi Borrower {runId}` berisi sepuluh aset (`Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, `Forklift Toyota {runId}`, `Bus Hino {runId}`, `Kamera Fujifilm {runId}`, `Printer Brother {runId}`, `Printer Canon {runId}`), Total Asset `10`, Modified By `Asset Admin Kelayakan {runId}`.
  - DU-017-20: Draft untuk Borrower `Edo Terlambat {runId}` berisi aset `Radio Motorola {runId}` dengan Duration `1` dan Purpose `Training`.
  - DU-017-21: Draft untuk Borrower `Lukman Resign {runId}` berisi aset `Headset Jabra {runId}` dengan Duration `1` dan Purpose `Training`.
  - DU-017-22: Draft untuk Borrower `Wawan Tanpa PIC {runId}` berisi aset `Tripod Manfrotto {runId}` dengan Duration `1` dan Purpose `Training`.
  - DU-017-23: aset layak `Speaker Bose {runId}`, Group `Head Office`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-017-25: aset layak `Mikrofon Rode {runId}`, Group `Head Office`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-017-24: isian form Borrow Request untuk Borrower `Citra Batas {runId}`: Duration `2` dan Purpose `Training` untuk `Speaker Bose {runId}` dan untuk `Mikrofon Rode {runId}`.
- Kondisi:
  - Max assets per borrower bernilai `10`.
  - Block new borrow when overdue bernilai ON.

## Test Steps

### Draft dibuka: baris tidak layak ditandai dengan satu alasan menurut prioritas
1. Buka tab Drafts
2. Ketik Search `Pratiwi Borrower {runId}`, tekan Enter
3. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `10`
4. Verifikasi baris `Printer Brother {runId}` tidak ditandai tidak layak dan tidak punya caption error
5. Verifikasi baris `Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, `Forklift Toyota {runId}`, `Bus Hino {runId}`, dan `Kamera Fujifilm {runId}` masing-masing ditandai ⚠ dengan caption `This asset can no longer be borrowed.` di bawah nama aset
6. Verifikasi alasan `This asset has been deleted.` tersampaikan pada ⚠ baris `Laptop Lenovo Yoga {runId}`
7. Verifikasi alasan `This asset is Damaged and can't be borrowed.` tersampaikan pada ⚠ baris `Tablet Samsung Tab {runId}`
8. Verifikasi alasan `This asset is already in another transaction.` tersampaikan pada ⚠ baris `Genset Honda {runId}`
9. Verifikasi alasan `This asset can't be borrowed until its TAG is replaced.` tersampaikan pada ⚠ baris `Scanner Zebra {runId}`
10. Verifikasi alasan `Can't be borrowed: this asset is not available for borrowing. Contact Rizal Manager {runId} (Manage asset & TAG).` tersampaikan pada ⚠ baris `Drone DJI Air {runId}` dan menyebut siapa yang dapat dihubungi
11. Verifikasi alasan `Borrowing isn't allowed for Heavy Machine {runId}.` tersampaikan pada ⚠ baris `Forklift Toyota {runId}`
12. Verifikasi alasan `Pratiwi Borrower {runId} can't borrow assets from Branch Surabaya.` tersampaikan pada ⚠ baris `Bus Hino {runId}`
13. Verifikasi ⚠ baris `Kamera Fujifilm {runId}` hanya memuat satu alasan `This asset can't be borrowed until its TAG is replaced.` walau aset juga gagal karena Deny pada override
14. Verifikasi baris `Printer Canon {runId}` tampil read-only dengan keterangan `Outside your groups` dan tanpa isian yang dapat diubah

### Mengganti Borrower menilai ulang kelayakan Allowed borrower
15. Klik `[Select Borrower]`
16. Ketik Search `Surya Surabaya {runId}`, tekan Enter
17. Pilih baris `Surya Surabaya {runId}`
18. Klik `[Select]`
19. Verifikasi baris `Bus Hino {runId}` tidak lagi ditandai tidak layak karena Borrower `Surya Surabaya {runId}` memenuhi Allowed borrower `Same Group only`
20. Verifikasi baris `Laptop Lenovo Yoga {runId}` tetap ditandai ⚠ dengan caption `This asset can no longer be borrowed.`

### Submit diblokir sampai aset tidak layak dikeluarkan
21. Klik `[Submit]`
22. Verifikasi caption error `Remove the unavailable assets to continue.` tampil di atas deretan tombol dan tidak ada BRW yang dibuat
23. Klik `[Remove Unavailable]`
24. Verifikasi baris `Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, dan `Forklift Toyota {runId}` tidak lagi ada di form sedangkan baris `Printer Brother {runId}` tetap ada
25. Klik `[Cancel]` pada form
26. Klik `[Leave]` pada dialog Unsaved Changes

### Borrower tidak aktif ditolak saat Submit dan Draft tetap tersimpan
27. Ketik Search `Lukman Resign {runId}`, tekan Enter
28. Klik ikon pensil `Edit` pada baris Draft untuk Borrower itu
29. Klik `[Submit]`
30. Verifikasi caption `Lukman Resign {runId} is no longer active. Pick another borrower.` tampil di field Borrower
31. Verifikasi baris `Headset Jabra {runId}` tetap ada dengan Duration `1` dan Purpose `Training`
32. Klik `[Cancel]` pada form yang belum diubah
33. Verifikasi tabel Drafts tetap memuat baris Draft untuk Borrower `Lukman Resign {runId}`

### Borrower tanpa akun login dan tanpa PIC ditolak
34. Ketik Search `Wawan Tanpa PIC {runId}`, tekan Enter
35. Klik ikon pensil `Edit` pada baris Draft untuk Borrower itu
36. Klik `[Save Draft]`
37. Verifikasi caption `Wawan Tanpa PIC {runId} has no login account and no PIC. Set a PIC in Users first.` tampil di field Borrower
38. Klik `[Cancel]` pada form yang belum diubah
39. Klik `[+ Borrow]`
40. Klik `[Select Borrower]`
41. Ketik Search `Wawan Tanpa PIC {runId}`, tekan Enter
42. Verifikasi baris `Wawan Tanpa PIC {runId}` berstatus Eligibility `Blocked` dengan alasan `No login account and no PIC. Set a PIC in Users first.` tersampaikan
43. Klik `[Cancel]` pada dialog Select Borrower
44. Klik `[Cancel]` pada form yang belum diubah

### Block new borrow when overdue menolak Submit
45. Buka tab Drafts
46. Ketik Search `Edo Terlambat {runId}`, tekan Enter
47. Klik ikon pensil `Edit` pada baris Draft untuk Borrower itu
48. Klik `[Submit]`
49. Verifikasi caption error `Edo Terlambat {runId} has an overdue borrow: [Asset Code], due [Date]. Return it first.` tampil di atas deretan tombol, dengan Asset Code dan Date dari baris Overdue Borrower itu
50. Klik `[Cancel]` pada form yang belum diubah

### Batas Max assets per borrower: pengajuan ke-N berhasil dan ke-N+1 ditolak
51. Klik `[+ Borrow]`
52. Klik `[Select Borrower]`
53. Ketik Search `Citra Batas {runId}`, tekan Enter
54. Pilih baris `Citra Batas {runId}`
55. Klik `[Select]`
56. Klik `[+ Asset]`
57. Ketik Search `{runId}`, tekan Enter
58. Centang baris `Speaker Bose {runId}`
59. Centang baris `Mikrofon Rode {runId}`
60. Klik `[Select]`
61. Klik `[+ Asset]`
62. Ketik Search `{runId}`, tekan Enter
63. Centang baris `Speaker Bose {runId}` yang sudah ada di form
64. Klik `[Select]`
65. Verifikasi toast netral `This asset is already in this borrow.` tampil dan baris aset tidak digandakan
66. Isi Duration baris `Speaker Bose {runId}` dengan `2`
67. Isi Purpose baris `Speaker Bose {runId}` dengan `Training`
68. Isi Duration baris `Mikrofon Rode {runId}` dengan `2`
69. Isi Purpose baris `Mikrofon Rode {runId}` dengan `Training`
70. Klik `[Submit]`
71. Verifikasi caption error `Citra Batas {runId} can borrow up to 10 assets at a time.` tampil di atas deretan tombol untuk pengajuan ke-11
72. Pilih aksi baris `Remove from List` pada baris `Mikrofon Rode {runId}`
73. Klik `[Submit]`
74. Klik `[Submit]` pada dialog `Submit Borrow`
75. Verifikasi toast `Success, borrow has been submitted for approval.` tampil untuk pengajuan ke-10
