---
id: TC-FA-FATR-BE-113-aturan-categories-dep-categories
title: "Setting dan override saat Category berubah"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§4.1#r21", "§4.1#r23", "§9.2#b35", "§9.2#b36", "§9.2#b121", "§9.2#b123", "§9.2#b146", "§9.2#b148", "§9.4.2#r34", "§9.4.2#r55", "§9.4.3#b11", "§9.4.3#b12", "EB-EDG-3", "§4.1#r19", "§4.1#r20", "§4.1#r24", "§9.2#b6"]
smoke: []
dependsOn:
  - "Settings Categories: hapus, nonaktifkan, dan tambah sub-Category"
trace:
  "§4.1#r21": [2, 7, 9, 11]
  "§9.2#b121": [3, 7, 11]
  "§9.2#b146": [3, 7, 11]
  "§9.4.2#r34": [3, 7, 9]
  "EB-EDG-3": [3, 11]
  "§9.2#b123": [5, 9]
  "§9.2#b148": 9
  "§9.4.3#b11": 9
  "§9.4.2#r55": [11, 12]
  "§9.4.3#b12": 12
  "§9.2#b36": [14, 17]
  "§9.2#b35": [15, 18]
  "§4.1#r23": [20, 21]
  "§4.1#r19": [11, 12]
  "§4.1#r20": 12
  "§4.1#r24": 12
  "§9.2#b6": [11, 12]
---

# Setting dan override saat Category berubah

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-113-1: Category `Perkakas Bengkel {runId} > Gerinda {runId}`, Max duration `7` sebagai nilai Category.
  - DU-113-2: Category `Perkakas Bengkel {runId} > Bor Meja {runId}`, aktif, Max duration `7` sebagai nilai Category.
  - DU-113-3: Category `Perkakas Bengkel {runId} > Obeng {runId}`, leaf, Max duration `7` sebagai nilai Category.
  - DU-113-4: Category `Perkakas Bengkel {runId} > Palu {runId}`, aktif, Max duration `9` sebagai nilai Category.
  - DU-113-5: Group `Divisi Bengkel {runId}`.
  - DU-113-6: aset `Bor Meja Unit 1 {runId}` di Category `Perkakas Bengkel {runId} > Bor Meja {runId}` dan Group `Divisi Bengkel {runId}`.
  - DU-113-7: override pada transaksi pinjam Category `Perkakas Bengkel {runId} > Gerinda {runId}`, target Group `Divisi Bengkel {runId}`, Max duration `5`.
  - DU-113-8: override pada transaksi pinjam Category `Perkakas Bengkel {runId} > Bor Meja {runId}`, target Group `Divisi Bengkel {runId}`, Max duration `5`.
  - DU-113-9: override pada transaksi pinjam Category `Perkakas Bengkel {runId} > Obeng {runId}`, target Group `Divisi Bengkel {runId}`, Max duration `5`.
  - DU-113-10: sub-Category `Perkakas Bengkel {runId} > Obeng {runId} > Obeng Presisi {runId}`.
  - DU-113-11: draft Max duration `8` untuk Category `Perkakas Bengkel {runId} > Obeng {runId}`.
  - DU-113-12: draft Max duration `6` untuk Category `Perkakas Bengkel {runId} > Bor Meja {runId}`.
  - DU-113-13: pengajuan pinjam aset `Bor Meja Unit 1 {runId}` selama `10` Days.
- Kondisi:
  - Max duration bernilai `14` di Company default untuk transaksi pinjam.

## Test Steps

### Category yang dihapus: setting dan override tetap tersimpan
1. Total Control menghapus Category `Perkakas Bengkel {runId} > Gerinda {runId}`
2. Verifikasi nilai Max duration `7` pada Category `Perkakas Bengkel {runId} > Gerinda {runId}` tetap tersimpan sebagai nilai setting Category yang tidak berlaku untuk evaluasi aset mana pun
3. Verifikasi override target Group `Divisi Bengkel {runId}` pada Category `Perkakas Bengkel {runId} > Gerinda {runId}` tetap tersimpan dan tampil di tabel Overrides sesudah Category dihapus

### Category yang dinonaktifkan: setting dan override tidak berlaku
4. Total Control mengajukan peminjaman aset `Bor Meja Unit 1 {runId}` selama `10` Days saat Category `Perkakas Bengkel {runId} > Bor Meja {runId}` masih aktif
5. Verifikasi pengajuan selama `10` Days ditolak karena override Max duration `5` pada Category `Perkakas Bengkel {runId} > Bor Meja {runId}` berlaku selama Category aktif
6. Total Control menonaktifkan Category `Perkakas Bengkel {runId} > Bor Meja {runId}`
7. Verifikasi nilai Max duration `7` dan override target Group `Divisi Bengkel {runId}` pada Category `Perkakas Bengkel {runId} > Bor Meja {runId}` tetap tersimpan, dan override tetap tampil di tabel Overrides
8. Total Control mengajukan peminjaman aset `Bor Meja Unit 1 {runId}` selama `10` Days sesudah Category `Perkakas Bengkel {runId} > Bor Meja {runId}` dinonaktifkan
9. Verifikasi pengajuan selama `10` Days diterima karena setting Category dan override pada Category yang dinonaktifkan tidak berlaku, dan Max duration efektif adalah `14` dari Company default

### Category yang menjadi induk: setting dan override tidak diwariskan
10. Total Control menambah sub-Category `Perkakas Bengkel {runId} > Obeng {runId} > Obeng Presisi {runId}` pada Category `Perkakas Bengkel {runId} > Obeng {runId}`
11. Verifikasi nilai Max duration `7` dan override target Group `Divisi Bengkel {runId}` tetap tersimpan di Category `Perkakas Bengkel {runId} > Obeng {runId}` yang kini menjadi induk
12. Verifikasi sub-Category `Perkakas Bengkel {runId} > Obeng {runId} > Obeng Presisi {runId}` mulai dengan Max duration Inherit tanpa override, dan aturan serta override Category `Perkakas Bengkel {runId} > Obeng {runId}` tidak diwariskan otomatis ke sub-Category itu

### Draft untuk Category yang bukan lagi leaf atau tidak aktif tetap disimpan
13. Total Control menyimpan draft Max duration bernilai `8` untuk Category `Perkakas Bengkel {runId} > Obeng {runId}` yang sudah menjadi induk
14. Verifikasi Save tidak ditolak karena draft pada Category yang bukan lagi leaf
15. Verifikasi nilai `8` tersimpan di Category `Perkakas Bengkel {runId} > Obeng {runId}` sebagai nilai tersimpan yang tidak berlaku
16. Total Control menyimpan draft Max duration bernilai `6` untuk Category `Perkakas Bengkel {runId} > Bor Meja {runId}` yang sudah tidak aktif
17. Verifikasi Save tidak ditolak karena draft pada Category yang tidak aktif
18. Verifikasi nilai `6` tersimpan di Category `Perkakas Bengkel {runId} > Bor Meja {runId}` sebagai nilai tersimpan yang tidak berlaku

### Nilai setting Category yang tidak berlaku tidak masuk sheet Rules
19. Total Control mengekspor rules untuk All categories
20. Verifikasi sheet Rules memuat baris Category `Perkakas Bengkel {runId} > Palu {runId}` dengan Max duration `9`
21. Verifikasi sheet Rules tidak memuat nilai setting Category `Perkakas Bengkel {runId} > Gerinda {runId}` yang dihapus, Category `Perkakas Bengkel {runId} > Bor Meja {runId}` yang dinonaktifkan, dan Category `Perkakas Bengkel {runId} > Obeng {runId}` yang menjadi induk
