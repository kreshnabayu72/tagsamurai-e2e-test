---
id: TC-FA-FAREG-BE-127-batas-karakter-field-teks
title: "Batas karakter field teks di server"
layer: be-e2e
priority: Medium
caseType: Edge
status: draft
sourceRules: [FAREG-LOGIC-01s, V-REG-18, "§9.9#r14", EB-FRM-4@alias-name, EB-FRM-4@damage-note, EB-FRM-4@reason, EB-FRM-4@skip-pairing-note]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-01s: [2, 5, 14]
  V-REG-18: [2, 9, 14, 21]
  "§9.9#r14": [9, 10, 12]
  EB-FRM-4@alias-name: [9, 10, 12]
  EB-FRM-4@damage-note: [2, 3, 5, 7]
  EB-FRM-4@reason: [19, 21, 22, 24]
  EB-FRM-4@skip-pairing-note: [14, 15, 17]
owner: BE
---
# Batas karakter field teks di server

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Banjarmasin {runId}` dan `Gudang Balikpapan {runId}`, pengaju); Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Balikpapan {runId}`, bukan pengaju, approver).
- Data:
  - DU-127-1: Group `Gudang Banjarmasin {runId}`, Assignable, di entitas aktor.
  - DU-127-2: Group `Gudang Balikpapan {runId}`, Assignable, di entitas aktor.
  - DU-127-3: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-127`, TAG Type `Non-TAG`.
  - DU-127-4: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`.
  - DU-127-5: batch Draft milik Rina, Group `Gudang Banjarmasin {runId}`, satu Item `Meja Kerja {runId}` Quantity `1`, Condition `Normal`, Tingkat 2 lengkap.
  - DU-127-6: batch Draft milik Rina, Group `Gudang Banjarmasin {runId}`, satu Item `Laptop {runId}` Quantity `1`, Tingkat 2 lengkap selain Tag, slot Tag RFID kosong.
  - DU-127-7: batch Draft milik Rina, Group `Gudang Balikpapan {runId}`, satu Item `Meja Kerja {runId}` Quantity `2`, Tingkat 2 lengkap.
- Kondisi:
  - Approval Workflow tidak aktif untuk `Gudang Banjarmasin {runId}`.
  - Approval Workflow aktif untuk `Gudang Balikpapan {runId}` dengan toggle `Require Approval for Registration` ON.
  - Kuota tenant dan kuota Group `Gudang Banjarmasin {runId}` dan `Gudang Balikpapan {runId}` mencukupi untuk seluruh aset yang diajukan spec ini.

## Test Steps

### Damage note dibatasi 120 karakter di server
1. Rina mengirim Save draft atas batch DU-127-5 dengan Condition `Damaged` dan Damage note `Casing belakang retak dan engsel kiri longgar sehingga unit tidak layak dipakai Referensi tiket 2026202620262026202620262` (121 karakter)
2. Verifikasi Save draft ditolak server dengan pesan `Max. 120 characters`
3. Verifikasi Condition aset batch DU-127-5 tetap `Normal` dan Damage note tetap kosong
4. Rina mengirim Submit atas batch DU-127-5 dengan Condition `Damaged` dan Damage note `Casing belakang retak dan engsel kiri longgar sehingga unit tidak layak dipakai Referensi tiket 2026202620262026202620262` (121 karakter)
5. Verifikasi Submit ditolak server dengan pesan `Max. 120 characters` dan aset tetap Draft
6. Rina mengirim Save draft atas batch DU-127-5 dengan Condition `Damaged` dan Damage note `Casing belakang retak dan engsel kiri longgar sehingga unit tidak layak dipakai Referensi tiket 202620262026202620262026` (120 karakter)
7. Verifikasi Save draft berhasil dan Damage note tersimpan utuh sebanyak 120 karakter

### Alias Name dibatasi 120 karakter di server
8. Rina mengirim Save draft atas batch DU-127-5 dengan Alias Name `Server Rak Utama Ruang Data Lantai Dua Gedung Barat Cabang Surabaya Kode 202620262026202620262026202620262026202620262026` (121 karakter)
9. Verifikasi Save draft ditolak server dengan pesan `Max. 120 characters`
10. Verifikasi aset batch DU-127-5 belum memiliki Alias Name
11. Rina mengirim Save draft atas batch DU-127-5 dengan Alias Name `Server Rak Utama Ruang Data Lantai Dua Gedung Barat Cabang Surabaya Kode 20262026202620262026202620262026202620262026202` (120 karakter)
12. Verifikasi Save draft berhasil dan Alias Name tersimpan utuh sebanyak 120 karakter

### Skip pairing Note dibatasi 120 karakter di server
13. Rina mengirim Submit atas batch DU-127-6 dengan Skip pairing dicentang, Reason `Other`, dan Note `Tag RFID untuk unit ini belum tiba dari pemasok dan jadwal pengiriman belum dikonfirmasi Referensi tiket 2026202620262026` (121 karakter)
14. Verifikasi Submit ditolak server dengan pesan `Max. 120 characters`
15. Verifikasi aset batch DU-127-6 tetap Draft
16. Rina mengirim Submit atas batch DU-127-6 dengan Skip pairing dicentang, Reason `Other`, dan Note `Tag RFID untuk unit ini belum tiba dari pemasok dan jadwal pengiriman belum dikonfirmasi Referensi tiket 202620262026202` (120 karakter)
17. Verifikasi Submit diterima dan aset batch DU-127-6 berstatus Active

### Reason keputusan approval dibatasi 360 karakter di server
18. Rina mengirim Submit atas batch DU-127-7
19. Verifikasi kedua aset batch DU-127-7 berstatus Waiting for Approval
20. Budi mengirim keputusan: aset pertama `Return to Draft` dengan Reason `Spesifikasi aset tidak cocok dengan dokumen pengajuan yang dilampirkan oleh pengaju. Merek dan model pada form berbeda dengan label fisik di unit. Mohon pengaju memeriksa kembali kondisi barang, mencocokkan nomor seri dengan faktur pembelian, lalu mengajukan ulang setelah data cocok. Nomor pengajuan 202620262026202620262026202620262026202620262026202620262026` (361 karakter); aset kedua `Reject` dengan Reason `Unit rusak saat pengiriman`
21. Verifikasi keputusan ditolak server dengan pesan `Max. 360 characters`
22. Verifikasi pengajuan batch DU-127-7 tetap Waiting for Approval tanpa keputusan tersimpan
23. Budi mengirim keputusan: aset pertama `Return to Draft` dengan Reason `Spesifikasi aset tidak cocok dengan dokumen pengajuan yang dilampirkan oleh pengaju. Merek dan model pada form berbeda dengan label fisik di unit. Mohon pengaju memeriksa kembali kondisi barang, mencocokkan nomor seri dengan faktur pembelian, lalu mengajukan ulang setelah data cocok. Nomor pengajuan 20262026202620262026202620262026202620262026202620262026202` (360 karakter); aset kedua `Reject` dengan Reason `Unit rusak saat pengiriman`
24. Verifikasi keputusan diterima dan Reason aset pertama tersimpan utuh sebanyak 360 karakter
