---
id: TC-FA-FACO-BE-156-bulk-dan-selection-limit
title: "Aksi bulk: catatan log per akun, tanpa entri, dan Selection Limit"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: [N-08, "§8.4#r3", "§8.4#r4", "§9.4.2#r35"]
smoke: []
dependsOn: []
trace:
  N-08: [4, 8]
  "§8.4#r3": [3, 4, 5]
  "§8.4#r4": [11, 12]
  "§9.4.2#r35": [14, 15, 17, 18]
---

# Aksi bulk: catatan log per akun, tanpa entri, dan Selection Limit

## Prerequisites
- Aktor: Admin A, Total Control dengan cakupan seluruh client.
- Data:
  - DU-156-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-156-2: Account Code `BKA-{runId}`, Account Name `Kas Bulk Nonaktif Satu {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-156-3: Account Code `BKB-{runId}`, Account Name `Kas Bulk Nonaktif Dua {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-156-4: Account Code `BKC-{runId}`, Account Name `Kas Bulk Sudah Nonaktif {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-156-5: Account Code `BKD-{runId}`, Account Name `Kas Bulk Tidak Dipilih {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-156-6: Account Code `NOP-{runId}`, Account Name `Kas Tanpa Perubahan {runId}`, Account Function `Asset Cost`.
  - DU-156-7: Account Code `DUP-{runId}`, Account Name `Kas Pemilik Kode {runId}`, Account Function `Asset Cost`.
  - DU-156-8: 1001 akun volume dengan Account Code `V{n}-{runId}` dan Account Name `Kas Volume {n} {runId}` (n dari 1 sampai 1001), Account Function `Asset Cost`, Status `Active`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga Deactivate tidak diblokir.
  - Selection Limit client bernilai `1000`.
  - Batas jumlah akun client mencukupi untuk 1001 akun volume tambahan.

## Test Steps

### Bulk Deactivate: satu entri per akun yang berubah, akun yang sudah Inactive dan akun yang tidak dipilih tanpa entri
1. Admin A mencatat jumlah entri log akun `BKA-{runId}`, `BKB-{runId}`, `BKC-{runId}`, dan `BKD-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A mengirim Deactivate bulk atas akun `BKA-{runId}`, `BKB-{runId}`, dan `BKC-{runId}`
3. Verifikasi akun `BKA-{runId}` dan `BKB-{runId}` berstatus `Inactive`, dan jumlah entri log masing-masing akun bertambah satu pada setiap surface
4. Verifikasi akun `BKC-{runId}` tetap `Inactive` dan jumlah entri log akun itu tidak bertambah pada ketiga surface, karena sudah berstatus target dan dilewati
5. Verifikasi akun `BKD-{runId}` yang tidak dipilih tetap `Active` dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Edit tanpa perubahan nilai tidak menulis entri
6. Admin A mencatat jumlah entri log akun `NOP-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
7. Admin A mengirim Edit akun `NOP-{runId}` dengan Account Name `Kas Tanpa Perubahan {runId}` dan Account Function `Asset Cost`, nilai yang sama persis dengan data akun saat ini
8. Verifikasi akun `NOP-{runId}` tidak berubah dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Create yang ditolak tidak menulis entri pada ketiga surface
9. Admin A mencatat jumlah entri log akun dengan Account Code `DUP-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
10. Admin A mengirim Create dengan Account Code `DUP-{runId}`, kode yang sudah dipakai akun lain, Account Name `Kas Duplikat Ditolak {runId}`, dan Account Function `Asset Cost`
11. Verifikasi Create ditolak dengan pesan `Account code already exists`, dan akun yang sudah ada tetap memakai Account Name `Kas Pemilik Kode {runId}`
12. Verifikasi jumlah entri log akun dengan Account Code `DUP-{runId}` tidak bertambah pada ketiga surface, karena penolakan atomik tidak meninggalkan data maupun log

### Selection Limit 1000 pada aksi bulk
13. Admin A mengirim Deactivate bulk atas seluruh 1001 akun volume, yaitu 1001 akun melebihi Selection Limit `1000`
14. Verifikasi permintaan ditolak sebelum diproses karena jumlah akun yang dipilih melebihi `1000`
15. Verifikasi akun volume pertama dan akun volume ke-1001 yang dijadikan sampel tetap berstatus `Active`, dan tidak ada entri log baru untuk keduanya pada ketiga surface
16. Admin A mengirim Deactivate bulk atas 1000 akun volume pertama
17. Verifikasi permintaan diterima: akun volume pertama dan akun volume ke-1000 berstatus `Inactive`, masing-masing dengan satu entri log baru pada ketiga surface
18. Verifikasi akun volume ke-1001 tetap berstatus `Active` tanpa entri log baru
