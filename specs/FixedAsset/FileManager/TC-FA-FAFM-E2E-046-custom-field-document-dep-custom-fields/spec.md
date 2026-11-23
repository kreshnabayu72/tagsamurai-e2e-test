---
id: TC-FA-FAFM-E2E-046-custom-field-document-dep-custom-fields
title: "Custom Field Document pada aset dan definisi field"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, FAFM-LOGIC-07h, SRC-04, SYN-01b, SYN-01e, SYN-01h]
smoke: []
dependsOn: ["Custom Fields: field Custom Field Document pada aset"]
trace:
  ACT-02e: [10, 13]
  ARS-01c: 13
  DIM-14a: 13
  DIM-14b: 14
  FAFM-LOGIC-02c: [10, 13]
  FAFM-LOGIC-02e: 13
  FAFM-LOGIC-02f: 14
  FAFM-LOGIC-07h: [22, 25, 29, 30, 36, 40, 41]
  SRC-04: [3, 4, 5]
  SYN-01b: 13
  SYN-01e: 13
  SYN-01h: 16
anchor: [24]
coverage:
  web: automated
---

# Custom Field Document pada aset dan definisi field

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-046-1: Aset `Scanner Epson DS-530 {runId}`, Status `Active`, Group `Branch Bandung`, ada di entitas aktor.
  - DU-046-2: Field custom bertipe Document `Warranty Card {runId}` pada aset DU-046-1, bernilai file `warranty-card-{runId}.pdf`.
  - DU-046-3: Field custom bertipe Document `Service Manual {runId}` pada aset DU-046-1, bernilai file `service-manual-{runId}.pdf`.
  - DU-046-4: Field custom bertipe Document `Insurance Certificate {runId}` pada aset DU-046-1, bernilai file `insurance-certificate-{runId}.pdf`.

## Test Steps

### File Custom Field Document terdaftar di tab Asset Documents
1. Klik tab `Asset Documents`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `warranty-card-{runId}.pdf` tampil dengan Source `Custom Field Document`
4. Verifikasi baris file `warranty-card-{runId}.pdf` menampilkan Reference `Warranty Card {runId}`
5. Verifikasi baris file `service-manual-{runId}.pdf` menampilkan Reference `Service Manual {runId}`

### Delete file Custom Field Document mengosongkan nilai field di aset tanpa mengubah statusnya
6. Klik aksi Delete pada baris file `warranty-card-{runId}.pdf`
7. Klik `[Delete]` pada dialog Delete File
8. Klik tombol Recycle Bin pada header kartu Storage Usage
9. Ketik Search `warranty-card-{runId}.pdf`, tekan Enter
10. Verifikasi baris file `warranty-card-{runId}.pdf` tampil di Recycle Bin
11. Tutup modal Recycle Bin
12. Buka halaman detail aset `Scanner Epson DS-530 {runId}`
13. Verifikasi field `Warranty Card {runId}` pada detail aset menampilkan `—`
14. Verifikasi Status aset `Scanner Epson DS-530 {runId}` tetap `Active`
15. Buka Changelog aset `Scanner Epson DS-530 {runId}`
16. Verifikasi entri dengan Action `Edit`, Field `Warranty Card {runId}`, Old Value `warranty-card-{runId}.pdf`, dan New Value `—` tampil
17. Tutup Changelog aset

### Penghapusan definisi field men-soft-delete file tanpa pertanyaan
18. Buka Settings > Custom Fields
19. Ketik Search `Service Manual {runId}`, tekan Enter
20. Hapus field custom `Service Manual {runId}`
21. Konfirmasi penghapusan field custom
22. Verifikasi tidak ada dialog yang menanyakan apakah file dokumen field itu juga dihapus dari File Manager
23. Buka halaman detail aset `Scanner Epson DS-530 {runId}`
24. Verifikasi field `Warranty Card {runId}` tampil pada detail aset
25. Verifikasi field `Service Manual {runId}` tidak tampil pada detail aset (Hidden)
26. Buka Settings > File Manager
27. Klik tombol Recycle Bin pada header kartu Storage Usage
28. Ketik Search `service-manual-{runId}.pdf`, tekan Enter
29. Verifikasi baris file `service-manual-{runId}.pdf` tampil di Recycle Bin
30. Verifikasi baris file `service-manual-{runId}.pdf` menampilkan Deleted By nama aktor yang menghapus field custom
31. Tutup modal Recycle Bin

### Penggantian tipe definisi field men-soft-delete file tanpa pertanyaan
32. Buka Settings > Custom Fields
33. Ketik Search `Insurance Certificate {runId}`, tekan Enter
34. Ubah tipe field custom `Insurance Certificate {runId}` menjadi tipe yang bukan tipe file
35. Konfirmasi perubahan tipe field custom
36. Verifikasi tidak ada dialog yang menanyakan apakah file dokumen field itu juga dihapus dari File Manager
37. Buka Settings > File Manager
38. Klik tombol Recycle Bin pada header kartu Storage Usage
39. Ketik Search `insurance-certificate-{runId}.pdf`, tekan Enter
40. Verifikasi baris file `insurance-certificate-{runId}.pdf` tampil di Recycle Bin
41. Verifikasi baris file `insurance-certificate-{runId}.pdf` menampilkan Deleted By nama aktor yang mengubah tipe field custom
42. Tutup modal Recycle Bin
