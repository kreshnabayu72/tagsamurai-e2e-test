---
id: TC-FA-MYASSET-E2E-023-cancel-missing-report-pinjaman-dep-borrow
title: "Cancel Missing Report pada pinjaman: badge hilang dan aksi baris kembali"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r9", "§4.1b#r68", "§4.1b#r69", "§4.1b#r70", "§4.1b#r72", "§4.1b#r73", "§4.1b#r74", "§4.8#r12", "§7.3#r9", "§9.6#r9", "EB-FB-1@cancel-missing-report"]
smoke: ["EB-FB-1@cancel-missing-report"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§2.1#r9": [4, 8]
  "§4.1b#r68": [2, 4]
  "§4.1b#r69": [6]
  "§4.1b#r70": [12, 14]
  "§4.1b#r72": [12]
  "§4.1b#r73": [14]
  "§4.1b#r74": [8]
  "§4.8#r12": [4]
  "§7.3#r9": [8]
  "§9.6#r9": [8, 12]
  "EB-FB-1@cancel-missing-report": [8]
anchor: [11]
coverage:
  web: automated
---

# Cancel Missing Report pada pinjaman: badge hilang dan aksi baris kembali

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login yang tidak memegang hak Aktor Missing pada Group aset, pemilik pinjaman dan pelapor laporan Missing di Data.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-023-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, dengan laporan Missing berstatus `Waiting for Confirmation` yang dilaporkan aktor sendiri.

## Test Steps

### Cancel Missing Report oleh pelapor berhasil
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Reported Missing` di kolom Status sebelum Cancel Missing Report
3. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Verifikasi aksi `Cancel Missing Report` tampil di menu baris
5. Klik `Cancel Missing Report`
6. Verifikasi dialog `Cancel Report` tampil untuk laporan kehilangan
7. Konfirmasi pembatalan pada dialog `Cancel Report`
8. Verifikasi toast `Success, report has been canceled.` tampil

### Badge hilang dan aksi baris kembali sesudah pembatalan
9. Muat ulang halaman
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dengan status `Borrowed` sesudah pembatalan laporan kehilangan
12. Verifikasi badge `Reported Missing` tidak tampil pada baris `Laptop Dell Latitude 5420 {runId}`
13. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi aksi `Request Extension`, `Report Damaged`, dan `Report Missing` tampil lagi di menu baris
15. Tekan `Esc` untuk menutup menu baris
