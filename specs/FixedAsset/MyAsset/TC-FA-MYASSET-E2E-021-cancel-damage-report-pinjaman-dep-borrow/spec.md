---
id: TC-FA-MYASSET-E2E-021-cancel-damage-report-pinjaman-dep-borrow
title: "Cancel Damage Report pada pinjaman: badge hilang dan aksi kembali"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r9", "§4.1b#r60", "§4.1b#r61", "§4.1b#r62", "§4.1b#r64", "§4.1b#r65", "§4.1b#r66", "§4.8#r12", "§7.3#r9", "§9.6#r9", "EB-FB-1@cancel-damage-report"]
smoke: ["EB-FB-1@cancel-damage-report"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§2.1#r9": [4, 8]
  "§4.1b#r60": [2, 4]
  "§4.1b#r61": [6]
  "§4.1b#r62": [12, 14]
  "§4.1b#r64": [12]
  "§4.1b#r65": [14]
  "§4.1b#r66": [8]
  "§4.8#r12": [4]
  "§7.3#r9": [8]
  "§9.6#r9": [8, 12]
  "EB-FB-1@cancel-damage-report": [8]
anchor: [11]
coverage:
  web: automated
---

# Cancel Damage Report pada pinjaman: badge hilang dan aksi kembali

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login, pemilik pinjaman dan pelapor Damage Report di Data.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-021-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, dengan Damage Report berstatus `Waiting for Confirmation` yang dilaporkan aktor sendiri.

## Test Steps

### Cancel Damage Report oleh pelapor berhasil
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Reported Damaged` di kolom Status sebelum Cancel Damage Report
3. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Verifikasi aksi `Cancel Damage Report` tampil di menu baris
5. Klik `Cancel Damage Report`
6. Verifikasi dialog `Cancel Report` tampil untuk Damage Report
7. Konfirmasi pembatalan pada dialog `Cancel Report`
8. Verifikasi toast `Success, report has been canceled.` tampil

### Badge hilang dan aksi tampil lagi sesudah pembatalan
9. Muat ulang halaman
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dengan status `Borrowed` sesudah pembatalan Damage Report
12. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Laptop Dell Latitude 5420 {runId}`
13. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi aksi `Request Extension` dan `Report Damaged` tampil lagi di menu baris
15. Tekan `Esc` untuk menutup menu baris
