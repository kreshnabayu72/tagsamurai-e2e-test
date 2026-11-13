---
id: TC-FA-FAREG-E2E-062-bulk-delete-draft
title: "Bulk Delete draft: beberapa batch terhapus"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.8#r21, D-REG-01, T-REG-04]
smoke: [D-REG-01, T-REG-04]
dependsOn: []
trace:
  §4.8#r21: [7, 12, 14]
  D-REG-01: [7, 8, 9, 10]
  T-REG-04: 12
anchor: [13]
coverage:
  web: automated
---

# Bulk Delete draft: beberapa batch terhapus

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola seluruh Group `Gudang Massal {n} {runId}` dan `Gudang Massal Pembanding {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-062-1: Tiga batch Draft milik `Rina W`, Group `Gudang Massal {n} {runId}` dengan n `1` sampai `3`, masing-masing berisi Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2` (Total Asset `2`), tidak dikunci user lain.
  - DU-062-2: Satu batch Draft milik `Rina W`, Group `Gudang Massal Pembanding {runId}`, berisi Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `1`; tidak ikut dipilih.

## Test Steps

### Bulk Delete menghapus semua batch terpilih
1. Ketik Search `{runId}`, tekan Enter
2. Centang baris `Gudang Massal 1 {runId}`
3. Centang baris `Gudang Massal 2 {runId}`
4. Centang baris `Gudang Massal 3 {runId}`
5. Klik `Bulk Action`
6. Pilih `Delete`
7. Verifikasi judul dialog `Delete Drafts`
8. Verifikasi bullet identitas ketiga batch tampil lengkap: `Gudang Massal 1 {runId} · 2 assets`, `Gudang Massal 2 {runId} · 2 assets`, dan `Gudang Massal 3 {runId} · 2 assets`
9. Verifikasi pertanyaan konfirmasi bentuk jamak `...delete them?` beserta kalimat `This action cannot be undone.`
10. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil pada dialog
11. Klik `[Delete]`
12. Verifikasi toast `Success, draft has been deleted.` tampil
13. Verifikasi baris `Gudang Massal Pembanding {runId}` masih tampil di sub tab Draft
14. Verifikasi ketiga baris `Gudang Massal 1 {runId}`, `Gudang Massal 2 {runId}`, dan `Gudang Massal 3 {runId}` tidak ada lagi di tabel
