---
id: TC-FA-BORROW-E2E-013-form-submit-borrow-satu-brw
title: "Submit form Borrow Request ditolak seluruhnya bila ada aset tidak layak, lalu membuat satu BRW dan membuka Borrow Detail sesudah aset itu dikeluarkan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-BORROW-02", "FI-BRW-42", "§4.4#r5", "§4.4#r6", "EB-ERR-4"]
smoke: ["EB-ERR-4"]
dependsOn: []
trace:
  "F-BORROW-02": [34, 36]
  "FI-BRW-42": [24, 27, 31, 36, 37]
  "§4.4#r5": [24, 25, 26, 58, 59, 61, 63]
  "§4.4#r6": [34, 35]
  "EB-ERR-4": [28, 29, 40, 41]
anchor: []
coverage:
  web: automated
---

# Submit form Borrow Request ditolak seluruhnya bila ada aset tidak layak, lalu membuat satu BRW dan membuka Borrow Detail sesudah aset itu dikeluarkan

## Prerequisites
- Aktor: Asset Admin `Asset Admin Pemohon {runId}` (Aktor Borrow) dengan Group penugasan `Head Office`; Asset Admin lain `Admin Lain {runId}` dengan Group penugasan `Head Office` memicu perubahan state (LK-8).
- Layar awal: Transactions > Borrow.
- Data:
  - DU-013-1: Borrower `Rina Peminjam {runId}`, Email `rina.peminjam{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-013-2: Borrower `Gita Lain {runId}`, Email `gita.lain{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-013-3: Aktor `Asset Admin Pemohon {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - DU-013-4: Asset Admin `Admin Lain {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - DU-013-5: Approver `Citra Approver {runId}`, role Approver, Group penugasan `Head Office` (approver eligible bagi aset yang butuh approval).
  - DU-013-6: aset `Notebook Lenovo ThinkPad {runId}`, Brand `Lenovo {runId}`, Model/Type `ThinkPad T14 {runId}`, Group `Head Office`, Category `Laptop {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Auto (≤ 3 days)`.
  - DU-013-7: aset `Proyektor BenQ {runId}`, Brand `BenQ {runId}`, Model/Type `MX560 {runId}`, Group `Head Office`, Category `Projector {runId}`, Custody `Available`, Max Duration `5 days`, Approval `Needs approval`.
  - DU-013-8: aset `Kamera Canon EOS {runId}`, Brand `Canon {runId}`, Model/Type `EOS R6 {runId}`, Group `Head Office`, Category `Camera {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Needs approval`.
  - DU-013-9: isian form Borrow Request: Duration `2` dan Purpose `Training` untuk `Kamera Canon EOS {runId}`; Duration `3` dan Purpose `Training` untuk `Notebook Lenovo ThinkPad {runId}`; Duration `3` dan Purpose `Training` untuk `Proyektor BenQ {runId}`; Duration `2` dan Purpose `Training` untuk `Tripod Manfrotto {runId}`. Baris aset di form berurutan menurut urutan dicentang: `Kamera Canon EOS {runId}`, `Notebook Lenovo ThinkPad {runId}`, `Proyektor BenQ {runId}`, `Tripod Manfrotto {runId}`.
  - DU-013-10: aset `Tripod Manfrotto {runId}`, Brand `Manfrotto {runId}`, Model/Type `MT190 {runId}`, Group `Head Office`, Category `Camera Accessory {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Needs approval`; diambil `Admin Lain {runId}` bersama `Kamera Canon EOS {runId}` sebelum Submit.
  - DU-013-11: aset `Mikrofon Rode {runId}`, Brand `Rode {runId}`, Model/Type `NT-USB {runId}`, Group `Head Office`, Category `Audio {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Needs approval`; diambil `Admin Lain {runId}` untuk Borrower `Gita Lain {runId}` sementara form Borrow Request kedua terbuka.
  - DU-013-12: aset `Speaker JBL {runId}`, Brand `JBL {runId}`, Model/Type `Flip 6 {runId}`, Group `Head Office`, Category `Audio {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Needs approval`; tidak diambil siapa pun.
  - DU-013-13: isian form Borrow Request kedua: Duration `2` dan Purpose `Training` untuk `Mikrofon Rode {runId}`; Duration `2` dan Purpose `Training` untuk `Speaker JBL {runId}`.

## Test Steps

### Submit ditolak seluruhnya bila satu aset tidak lagi layak
1. Klik `[+ Borrow]`
2. Klik `[Select Borrower]`
3. Ketik Search `Rina Peminjam {runId}`, tekan Enter
4. Pilih baris `Rina Peminjam {runId}`
5. Klik `[Select]`
6. Klik `[+ Asset]`
7. Ketik Search `{runId}`, tekan Enter
8. Centang baris `Kamera Canon EOS {runId}`
9. Centang baris `Notebook Lenovo ThinkPad {runId}`
10. Centang baris `Proyektor BenQ {runId}`
11. Centang baris `Tripod Manfrotto {runId}`
12. Klik `[Select]`
13. Isi Duration baris `Kamera Canon EOS {runId}` dengan `2`
14. Isi Purpose baris `Kamera Canon EOS {runId}` dengan `Training`
15. Isi Duration baris `Notebook Lenovo ThinkPad {runId}` dengan `3`
16. Isi Purpose baris `Notebook Lenovo ThinkPad {runId}` dengan `Training`
17. Isi Duration baris `Proyektor BenQ {runId}` dengan `3`
18. Isi Purpose baris `Proyektor BenQ {runId}` dengan `Training`
19. Isi Duration baris `Tripod Manfrotto {runId}` dengan `2`
20. Isi Purpose baris `Tripod Manfrotto {runId}` dengan `Training`
21. Asset Admin `Admin Lain {runId}` men-Submit BRW untuk Borrower `Gita Lain {runId}` berisi aset `Kamera Canon EOS {runId}` dan `Tripod Manfrotto {runId}`
22. Gulir halaman form ke deretan tombol di bagian bawah
23. Klik `[Submit]`
24. Verifikasi baris `Kamera Canon EOS {runId}` ditandai dengan caption `This asset can no longer be borrowed.`
25. Verifikasi baris `Tripod Manfrotto {runId}`, baris bermasalah kedua, ditandai dengan caption `This asset can no longer be borrowed.`
26. Verifikasi baris `Kamera Canon EOS {runId}`, baris bermasalah pertama di form, terlihat di layar karena halaman menggulir ke atas ke baris itu dari deretan tombol
27. Verifikasi caption error `Remove the unavailable assets to continue.` tampil di atas deretan tombol
28. Verifikasi baris `Notebook Lenovo ThinkPad {runId}` tidak ditandai dan tetap berisi Duration `3` dan Purpose `Training`
29. Verifikasi field Borrower tetap menampilkan `Rina Peminjam {runId}` dan form Borrow Request tetap terbuka tanpa dialog atau toast sukses

### Submit lolos membuat satu BRW dan membuka Borrow Detail
30. Klik `[Remove Unavailable]`
31. Verifikasi baris `Kamera Canon EOS {runId}` dan `Tripod Manfrotto {runId}` tidak lagi ada di tabel aset form sedangkan baris `Notebook Lenovo ThinkPad {runId}` dan `Proyektor BenQ {runId}` tetap ada
32. Klik `[Submit]`
33. Klik `[Submit]` pada dialog `Submit Borrow`
34. Verifikasi halaman pindah ke Borrow Detail BRW yang baru dengan judul berformat `BRW-YYYY-NNNN`
35. Verifikasi toast `Success, 1 of 2 assets have been approved. 1 submitted for approval.` tampil
36. Verifikasi di tabel Assets Borrow Detail baris `Notebook Lenovo ThinkPad {runId}` berstatus `Waiting for Handover` dan baris `Proyektor BenQ {runId}` berstatus `Waiting for Approval`
37. Verifikasi di Borrow Detail Borrower menampilkan `Rina Peminjam {runId}` dan Group `Head Office`

### Submit yang ditolak tidak meninggalkan BRW
38. Klik breadcrumb `Transactions`
39. Ketik Search `Rina Peminjam {runId}`, tekan Enter
40. Verifikasi tabel Transactions memuat tepat satu baris BRW untuk Borrower `Rina Peminjam {runId}`
41. Verifikasi BRW itu hanya memuat aset `Notebook Lenovo ThinkPad {runId}` dan `Proyektor BenQ {runId}` serta tidak memuat `Kamera Canon EOS {runId}`

### Kelayakan dicek ulang saat tab form aktif kembali
42. Klik `[+ Borrow]`
43. Klik `[Select Borrower]`
44. Ketik Search `Rina Peminjam {runId}`, tekan Enter
45. Pilih baris `Rina Peminjam {runId}`
46. Klik `[Select]`
47. Klik `[+ Asset]`
48. Ketik Search `{runId}`, tekan Enter
49. Centang baris `Mikrofon Rode {runId}`
50. Centang baris `Speaker JBL {runId}`
51. Klik `[Select]`
52. Isi Duration baris `Mikrofon Rode {runId}` dengan `2`
53. Isi Purpose baris `Mikrofon Rode {runId}` dengan `Training`
54. Isi Duration baris `Speaker JBL {runId}` dengan `2`
55. Isi Purpose baris `Speaker JBL {runId}` dengan `Training`
56. Asset Admin `Admin Lain {runId}` men-Submit BRW untuk Borrower `Gita Lain {runId}` berisi aset `Mikrofon Rode {runId}`
57. Pindah ke tab browser lain, lalu kembali ke tab form Borrow Request
58. Verifikasi baris `Mikrofon Rode {runId}` ditandai dengan caption `This asset can no longer be borrowed.` tanpa menekan `[Submit]`
59. Verifikasi baris `Speaker JBL {runId}` tidak ditandai dan tetap berisi Duration `2` dan Purpose `Training`
60. Klik `[Submit]`
61. Verifikasi caption error `Remove the unavailable assets to continue.` tampil dan form Borrow Request tetap terbuka tanpa dialog `Submit Borrow` (Submit diblokir)
62. Klik `[Remove Unavailable]`
63. Verifikasi baris `Mikrofon Rode {runId}` tidak lagi ada di tabel aset form sedangkan baris `Speaker JBL {runId}` tetap ada
