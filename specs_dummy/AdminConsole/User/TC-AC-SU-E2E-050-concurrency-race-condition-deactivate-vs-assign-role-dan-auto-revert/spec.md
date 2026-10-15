---
id: TC-AC-SU-E2E-050-concurrency-race-condition-deactivate-vs-assign-role-dan-auto-revert
title: "Resiliensi Concurrency Race Condition 2 Aktor: Deactivate vs Assign Group Role dan Auto-Revert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-215
  - TC-AC-SU-216
coverage:
  web: automated
---

# Resiliensi Concurrency Race Condition 2 Aktor: Deactivate vs Assign Group Role dan Auto-Revert

## Prerequisites

- Sesi Context A: Login sebagai Admin A
- Sesi Context B: Login sebagai Admin B
- Kedua sesi membuka target pengguna yang sama secara simultan

## Test Steps

### Race Condition 1: Deactivate vs Assign Group Role
1. Di Context A, Admin A bersiap melakukan deactive user
2. Di Context B, Admin B bersiap menyimpan penugasan Assign Group Role baru
3. Jalankan kedua request mutasi secara simultan pada milidetik yang sama
4. Verifikasi backend memproses kedua transaksi secara komutatif tanpa error 500
5. Verifikasi hasil akhir: penugasan grup tersimpan di database dan status pengguna tercatat sebagai `Inactive`
6. Verifikasi pada Context B yang melakukan submit role menerima pembaruan status terkini tanpa inkonsistensi UI

### Race Condition 2: Deactivate vs Auto-Revert Tier
7. Admin A melakukan deactive user sementara Admin B mengubah izin yang memicu terjadinya Auto-Revert tier Total Control
8. Jalankan kedua aksi secara simultan
9. Verifikasi integritas status akhir: tier pengguna ter-revert menjadi Custom Role dan status akun adalah Inactive tanpa adanya rekaman yatim (orphaned records) di database

## Notes

Memastikan stabilitas database dan integritas state sistem saat terjadi tabrakan eksekusi konkuren.
