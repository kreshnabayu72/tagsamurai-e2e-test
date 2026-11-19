---
id: TC-FA-FASVC-E2E-027-create-nama-sama-serentak
title: "Dua Admin Create Nama Sama: Satu Sukses, yang Kedua Ditolak Name already exists"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [EC-FASVC-02, F-FASVC-02.k3, FASVC-LOGIC-11f, EB-CON-2]
smoke: []
dependsOn: []
trace:
  EC-FASVC-02: [12, 14]
  F-FASVC-02.k3: [17, 20, 21]
  FASVC-LOGIC-11f: 14
  EB-CON-2: [12, 14]
anchor: []
coverage:
  web: automated
---

# Dua Admin Create Nama Sama: Satu Sukses, yang Kedua Ditolak Name already exists

## Prerequisites
- Aktor: Total Control. Admin A (`Rina Wulandari {runId}`, role Total Control, cakupan seluruh Group) dan Admin B (`Budi Santoso {runId}`, role Total Control, cakupan seluruh Group) membuka form Create pada saat yang sama, masing-masing di konteksnya.
- Layar awal: Add-ons > Service Center.
- Data:
  - Belum ada Service Center ber-Name `Teknisi Lintas Cabang {runId}` di entitas aktor.
  - DU-027-1: Service Center baru `Teknisi Lintas Cabang {runId}`, Service type `Routine`, Available to `All groups` (bawaan Create untuk Total Control), Country `Indonesia` (negara company, bawaan Create), City `Bandung`, Company phone `+62 81234500327`; diisi dan dikirim oleh Admin A dan Admin B dengan nilai yang sama.

## Test Steps

### Dua admin mengisi form Create dengan Name yang sama, Create pertama sukses
1. Admin A klik `[+ Service Center]`
2. Admin A isi field Name `Teknisi Lintas Cabang {runId}`
3. Admin A centang Service type `Routine`
4. Admin A isi field City `Bandung`
5. Admin A isi Company phone dengan Dial Code `+62` dan nomor `81234500327`
6. Admin B klik `[+ Service Center]`
7. Admin B isi field Name `Teknisi Lintas Cabang {runId}`
8. Admin B centang Service type `Routine`
9. Admin B isi field City `Bandung`
10. Admin B isi Company phone dengan Dial Code `+62` dan nomor `81234500327`

11. Admin A klik `[Submit]`
12. Verifikasi toast `Success, Teknisi Lintas Cabang {runId} has been added.` tampil di layar Admin A

### Create kedua dengan Name yang sama ditolak
13. Admin B klik `[Submit]`
14. Verifikasi pesan `Name already exists` tampil di bawah field Name pada form Admin B
15. Admin B klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Hanya satu Service Center tersimpan dan hanya Create yang berhasil tercatat
16. Admin A ketik Search `Teknisi Lintas Cabang {runId}`, tekan Enter
17. Verifikasi tepat satu baris `Teknisi Lintas Cabang {runId}` tampil di tabel
18. Admin A klik `Changelog` pada toolbar
19. Ketik Search `Teknisi Lintas Cabang {runId}` pada modal `Changelog: Service Center`, tekan Enter
20. Verifikasi entri dengan Action `Created` untuk `Teknisi Lintas Cabang {runId}` tampil
21. Verifikasi seluruh entri hasil Search memiliki Modified By Admin A, dan tidak ada entri Modified By Admin B
22. Tutup modal `Changelog: Service Center` lewat icon close
