---
id: TC-FA-FASVC-E2E-026-hapus-sudah-dihapus-pihak-lain
title: "Aksi pada Service Center yang Sudah Dihapus: Toast Netral dan Daftar Dimuat Ulang"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FASVC-LOGIC-11e, TS-FASVC-08]
smoke: []
dependsOn: []
trace:
  FASVC-LOGIC-11e: [9, 10, 21]
  TS-FASVC-08: [9, 11, 12, 21, 22]
anchor: [2, 5, 14, 16]
coverage:
  web: automated
---

# Aksi pada Service Center yang Sudah Dihapus: Toast Netral dan Daftar Dimuat Ulang

## Prerequisites
- Aktor: Total Control. Admin A (`Rina Wulandari {runId}`, role Total Control, cakupan seluruh Group) menguji layarnya. Admin B (`Budi Santoso {runId}`, role Total Control, cakupan seluruh Group) memicu penghapusan dari konteks lain.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-026-1: Service Center `Sentra Kalibrasi Edit {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company phone `+62 81234500230`, Status `Active`, Usage `0`, ada di entitas aktor.
  - DU-026-2: Service Center `Sentra Kalibrasi Detail {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company phone `+62 81234500231`, Status `Active`, Usage `0`, ada di entitas aktor.
  - DU-026-3: City yang dicoba disimpan Admin A `Malang`.

## Test Steps

### Save pada dialog Edit yang Service Center-nya sudah dihapus
1. Ketik Search `Sentra Kalibrasi Edit {runId}`, tekan Enter
2. Verifikasi baris `Sentra Kalibrasi Edit {runId}` tampil di tabel
3. Klik `⋯` pada baris `Sentra Kalibrasi Edit {runId}`
4. Klik `Edit`
5. Verifikasi dialog `Edit Service Center` terbuka dengan field City berisi `Surabaya`
6. Admin B menghapus `Sentra Kalibrasi Edit {runId}` lewat `Delete` dan mengonfirmasi dengan `[Delete]` pada dialog `Delete Service Center`
7. Ganti isi field City dengan `Malang`
8. Klik `[Save]`
9. Verifikasi toast `This service center is no longer available.` tampil
10. Verifikasi toast tersebut bersifat Info (netral), bukan toast sukses maupun error
11. Verifikasi dialog `Edit Service Center` tertutup
12. Verifikasi tidak ada baris `Sentra Kalibrasi Edit {runId}`: tabel kosong dengan pesan `No results found` pada daftar yang dimuat ulang

### Aksi pada halaman Detail yang Service Center-nya sudah dihapus
13. Ganti isi kotak Search dengan `Sentra Kalibrasi Detail {runId}`, tekan Enter
14. Verifikasi baris `Sentra Kalibrasi Detail {runId}` tampil di tabel
15. Klik nama `Sentra Kalibrasi Detail {runId}` pada baris tabel
16. Verifikasi halaman Detail `Sentra Kalibrasi Detail {runId}` terbuka dengan breadcrumb `Add-ons > Service Center > Detail`
17. Admin B menghapus `Sentra Kalibrasi Detail {runId}` lewat `Delete` dan mengonfirmasi dengan `[Delete]` pada dialog `Delete Service Center`
18. Klik `⋯` pada header Detail
19. Klik `Inactivate`
20. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
21. Verifikasi toast `This service center is no longer available.` tampil
22. Verifikasi tidak ada halaman Detail yang tampil: pengguna kembali ke halaman daftar dengan breadcrumb `Add-ons > Service Center`
