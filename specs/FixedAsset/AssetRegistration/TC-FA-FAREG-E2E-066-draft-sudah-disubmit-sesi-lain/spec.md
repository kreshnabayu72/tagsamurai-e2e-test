---
id: TC-FA-FAREG-E2E-066-draft-sudah-disubmit-sesi-lain
title: "Edit draft: batch sudah di-Submit sesi lain"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [FAREG-LOGIC-19g, FAREG-LOGIC-20i, §9.4.2#r27, D-REG-16]
smoke: [D-REG-16]
dependsOn: []
trace:
  FAREG-LOGIC-19g: [8, 11]
  FAREG-LOGIC-20i: [13, 16]
  §9.4.2#r27: [8, 11]
  D-REG-16: [8, 9]
anchor: []
coverage:
  web: automated
---

# Edit draft: batch sudah di-Submit sesi lain

## Prerequisites
- Aktor:
  - `Rina W` (Manage asset & TAG, Group terkelola `Gudang Submit {runId}`), pemegang form Edit yang ditolak.
  - `Hadi K` (Manage asset & TAG, Group terkelola `Gudang Submit {runId}`), pemicu Submit dari sesi lain.
- Layar awal: Rina W di Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-066-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Submit {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`; kedua aset memenuhi Tingkat 2 dan berstatus `✓ Ready`; aset 1 ber-Alias Name `Laptop Gudang Submit`.
- Kondisi:
  - Kuota tenant dan Group `Gudang Submit {runId}` mencukupi untuk dua aset, sehingga Submit oleh `Hadi K` berhasil.

## Test Steps

### Save draft dari sesi lama ditolak dengan dialog Draft Already Submitted
1. Rina W mengetik Search `Gudang Submit {runId}`, tekan Enter
2. Rina W mengklik Group `Gudang Submit {runId}` pada baris untuk membuka form Edit
3. Rina W mengklik tab `Asset`
4. Rina W mengklik row option `Detail` pada aset 1
5. Rina W mengisi Alias Name `Laptop Rina Revisi` pada aset 1 tanpa menyimpan
6. Hadi K men-Submit batch `Gudang Submit {runId}` dari sesi lain
7. Rina W mengklik `[Save draft]`
8. Verifikasi dialog `Draft Already Submitted` tampil bagi Rina W
9. Verifikasi isi dialog `This draft was submitted by Hadi K. Your changes cannot be saved.`
10. Waktu berlalu sampai 40 detik sejak dialog tampil
11. Verifikasi hanya satu dialog `Draft Already Submitted` yang tampil, tanpa dialog kedua dari autosave

### OK menutup dialog, membuang perubahan, dan membuka Detail pengajuan
12. Rina W mengklik `[OK]`
13. Verifikasi halaman Detail pengajuan batch `Gudang Submit {runId}` terbuka
14. Rina W mengklik tab `Asset`
15. Rina W mengklik Name aset 1 untuk membuka panel aset
16. Verifikasi Alias Name aset 1 pada Detail tetap `Laptop Gudang Submit`, perubahan `Laptop Rina Revisi` yang belum tersimpan dibuang
