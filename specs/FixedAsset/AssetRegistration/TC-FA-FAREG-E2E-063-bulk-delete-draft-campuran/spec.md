---
id: TC-FA-FAREG-E2E-063-bulk-delete-draft-campuran
title: "Bulk Delete draft: pilihan campuran dan tanpa batch yang dapat dihapus"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-10e, §4.8#r21, EB-BLK-3, T-REG-18, D-REG-28]
smoke: [T-REG-18, D-REG-28]
dependsOn: []
trace:
  FAREG-LOGIC-10e: [6, 10, 17, 18]
  §4.8#r21: [18, 20, 22]
  EB-BLK-3: [6, 20]
  T-REG-18: 20
  D-REG-28: [6, 7, 8, 9]
anchor: [12, 21]
coverage:
  web: automated
---

# Bulk Delete draft: pilihan campuran dan tanpa batch yang dapat dihapus

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Campur Bisa {runId}` dan seluruh Group `Gudang Campur Terkunci {n} {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-063-1: Satu batch Draft milik `Rina W`, Group `Gudang Campur Bisa {runId}`, berisi Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2` (Total Asset `2`), tidak dikunci user lain.
  - DU-063-2: Dua batch Draft milik `Rina W`, Group `Gudang Campur Terkunci {n} {runId}` dengan n `1` dan `2`, masing-masing berisi Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2` (Total Asset `2`).
- Kondisi:
  - Kunci sesi batch `Gudang Campur Terkunci 1 {runId}` dan `Gudang Campur Terkunci 2 {runId}` dipegang `Hadi K` (Manage asset & TAG, Group terkelola ketiga Group batch spec ini).

## Test Steps

### Tanpa batch yang dapat dihapus menampilkan dialog blok tanpa toast sukses
1. Ketik Search `{runId}`, tekan Enter
2. Centang baris `Gudang Campur Terkunci 1 {runId}`
3. Centang baris `Gudang Campur Terkunci 2 {runId}`
4. Klik `Bulk Action`
5. Pilih `Delete`
6. Verifikasi dialog blok `Cannot Delete Drafts` tampil
7. Verifikasi bullet identitas kedua batch terpilih: `Gudang Campur Terkunci 1 {runId} · 2 assets` dan `Gudang Campur Terkunci 2 {runId} · 2 assets`
8. Verifikasi teks dialog `None of the selected drafts can be deleted right now. They are being edited by another user, already deleted, or you don't have permission.`
9. Verifikasi tombol `[OK]` tampil pada dialog
10. Verifikasi toast `Success, draft has been deleted.` tidak tampil
11. Klik `[OK]`
12. Verifikasi baris `Gudang Campur Terkunci 1 {runId}` dan `Gudang Campur Terkunci 2 {runId}` masih tampil di sub tab Draft

### Pilihan campuran dibagi dua kelompok dan batch terkunci dilewati
13. Hapus centang baris `Gudang Campur Terkunci 2 {runId}`
14. Centang baris `Gudang Campur Bisa {runId}`
15. Klik `Bulk Action`
16. Pilih `Delete`
17. Verifikasi kelompok `The following will be deleted:` memuat bullet `Gudang Campur Bisa {runId} · 2 assets`
18. Verifikasi kelompok `The following can't be deleted and will be skipped:` memuat bullet `Gudang Campur Terkunci 1 {runId} · 2 assets`
19. Klik tombol konfirmasi pada dialog dua kali berturut-turut
20. Verifikasi toast `Success, draft has been deleted. Some items were skipped.` tampil satu kali
21. Verifikasi baris `Gudang Campur Terkunci 1 {runId}` masih tampil di sub tab Draft
22. Verifikasi baris `Gudang Campur Bisa {runId}` tidak ada lagi di tabel
