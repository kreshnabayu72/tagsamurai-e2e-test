---
id: TC-FA-FAREG-E2E-061-delete-draft
title: "Delete draft: satu batch terhapus"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: [F-FAREG-12, §9.7#r4, EB-TBL-7@tabel-draft, D-REG-01, T-REG-04]
smoke: [D-REG-01, T-REG-04]
dependsOn: []
trace:
  F-FAREG-12: 13
  §9.7#r4: 15
  EB-TBL-7@tabel-draft: 14
  D-REG-01: [8, 9, 10, 11]
  T-REG-04: 13
anchor: [4, 6]
coverage:
  web: automated
---

# Delete draft: satu batch terhapus

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola seluruh Group `Gudang Hapus {n} {runId}` dan `Gudang Hapus Sasaran {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-061-1: Sepuluh batch Draft milik `Rina W`, Group `Gudang Hapus {n} {runId}` dengan n `1` sampai `10`, masing-masing berisi Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2` (Total Asset `2`).
  - DU-061-2: Satu batch Draft milik `Rina W`, Group `Gudang Hapus Sasaran {runId}`, berisi Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2` (Total Asset `2`).
  - Seluruh batch Draft spec ini berjumlah `11` dan tidak dikunci user lain.

## Test Steps

### Delete batch terakhir di halaman terakhir menghapus batch dan memindahkan tabel ke halaman terakhir yang masih ada
1. Ketik Search `{runId}`, tekan Enter
2. Urutkan kolom `Group` secara A-Z
3. Ganti ukuran halaman menjadi `10`
4. Verifikasi halaman 1 memuat sepuluh baris dan tidak memuat baris `Gudang Hapus Sasaran {runId}`
5. Pindah ke halaman `2`
6. Verifikasi halaman 2 hanya memuat satu baris, yaitu Group `Gudang Hapus Sasaran {runId}`
7. Klik row action `Delete` pada baris `Gudang Hapus Sasaran {runId}`
8. Verifikasi judul dialog `Delete Draft`
9. Verifikasi bullet identitas batch `Gudang Hapus Sasaran {runId} · 2 assets`
10. Verifikasi pertanyaan konfirmasi `Are you sure you want to delete it? This action cannot be undone.`
11. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil pada dialog
12. Klik `[Delete]`
13. Verifikasi toast `Success, draft has been deleted.` tampil
14. Verifikasi tabel pindah ke halaman `1`, halaman terakhir yang masih ada, dan memuat sepuluh baris
15. Verifikasi baris `Gudang Hapus Sasaran {runId}` tidak ada lagi di tabel
