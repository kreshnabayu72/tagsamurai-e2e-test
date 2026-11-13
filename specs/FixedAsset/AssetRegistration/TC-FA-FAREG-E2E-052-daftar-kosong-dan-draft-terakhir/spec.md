---
id: TC-FA-FAREG-E2E-052-daftar-kosong-dan-draft-terakhir
title: "Daftar tanpa data: empty state tiap tabel dan draft pertama serta terakhir"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-EDG-2", "S-REG-01", "S-REG-02", "S-REG-03", "S-REG-04", "S-REG-05"]
smoke: ["S-REG-01", "S-REG-02", "S-REG-03", "S-REG-04", "S-REG-05"]
dependsOn: []
trace:
  "S-REG-01": [1, 27]
  "EB-EDG-2": [1, 3, 5, 8, 10, 19, 21, 22, 24, 26, 27]
  "S-REG-02": [3]
  "S-REG-03": [5]
  "S-REG-04": [8]
  "S-REG-05": [10]
coverage:
  web: automated
---

# Daftar tanpa data: empty state tiap tabel dan draft pertama serta terakhir

## Prerequisites
- Aktor: Total Control `Maya L`, bekerja di entitas khusus `Entitas Kosong {runId}` yang tidak dipakai spec lain.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-052-1: Entitas khusus `Entitas Kosong {runId}` tanpa batch Draft dan tanpa pengajuan, sehingga sub tab Draft, Waiting for Approval, dan History serta antrean Approvals tab Active dan History kosong (PRD tidak menetapkan record bawaan pada entitas).
  - DU-052-2: Group `Gudang Kosong {runId}`, node Assignable dan bukan Excess, belum memiliki batch Draft.
  - DU-052-3: Master Asset Name `Laptop`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`.
  - DU-052-4: Draft pertama Group `Gudang Kosong {runId}` dengan satu Item `Laptop`, `Dell`, `Latitude 5440`, Quantity `1` (Total Asset `1`), dibuat dan dihapus oleh spec ini.
  - Maya L adalah pengguna aktif dengan role Total Control pada entitas khusus.

## Test Steps

### Empty state alami sub tab Draft, Waiting for Approval, dan History
1. Verifikasi sub tab Draft menampilkan ilustrasi dengan teks `No drafts yet` dan `Get started by creating your first draft.`
2. Klik sub tab `Waiting for Approval`
3. Verifikasi sub tab Waiting for Approval menampilkan ilustrasi dengan teks `No requests waiting for approval` dan `Submitted registrations that need a decision will appear here.`
4. Klik sub tab `History`
5. Verifikasi sub tab History menampilkan ilustrasi dengan teks `No history yet` dan `Decided or canceled registrations will appear here.`

### Empty state alami antrean Approvals
6. Klik induk menu `Approvals` pada sidebar
7. Klik anak menu `Registration`
8. Verifikasi antrean Approvals tab Active menampilkan ilustrasi dengan teks `No pending approvals` dan `You have no pending approval requests at this moment.`
9. Klik tab `History`
10. Verifikasi antrean Approvals tab History menampilkan ilustrasi dengan teks `No history yet` dan `Decided or canceled registrations will appear here.`

### Draft pertama mengubah daftar dari nol menjadi satu
11. Klik menu `Registration` pada sidebar Assets
12. Klik `[+ Register Asset]`
13. Pilih Group `Gudang Kosong {runId}`
14. Pilih Asset Name `Laptop` pada Item 1
15. Pilih Brand `Dell` pada Item 1
16. Pilih Model `Latitude 5440` pada Item 1
17. Isi Quantity Item 1 dengan `1`
18. Klik `[Save draft]`
19. Verifikasi toast `Success, draft has been saved.` tampil sesudah draft pertama disimpan
20. Klik `[Cancel]` pada form
21. Verifikasi tabel sub tab Draft memuat satu baris, yaitu Group `Gudang Kosong {runId}` dengan Total Asset `1`
22. Verifikasi empty state `No drafts yet` tidak tampil lagi di sub tab Draft

### Draft terakhir dihapus mengembalikan empty state
23. Klik row action `Delete` pada baris `Gudang Kosong {runId}`
24. Verifikasi judul dialog `Delete Draft` untuk batch `Gudang Kosong {runId}`
25. Klik `[Delete]`
26. Verifikasi toast `Success, draft has been deleted.` tampil sesudah draft terakhir dihapus
27. Verifikasi sub tab Draft menampilkan kembali ilustrasi dengan teks `No drafts yet` dan `Get started by creating your first draft.`
