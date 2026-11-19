---
id: TC-FA-FASVC-E2E-012-delete-service-center-usage-nol
title: "Delete Service Center dengan Usage 0: Terhapus dan Hilang dari Daftar"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FASVC-04.k1", "FASVC-LOGIC-06c", "§9.7#r11", "EB-FB-1@delete-service-center", "EB-EDG-3"]
smoke: []
dependsOn: []
trace:
  "F-FASVC-04.k1": [7, 14, 17]
  "FASVC-LOGIC-06c": [18, 22]
  "§9.7#r11": [18, 19, 22]
  "EB-FB-1@delete-service-center": 11
  "EB-EDG-3": 19
anchor: [3, 13]
coverage:
  web: automated
---

# Delete Service Center dengan Usage 0: Terhapus dan Hilang dari Daftar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-012-1: Service Center `Hapus Uji {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Muar {runId}`, Company phone `+60 6555050505`, Attachments satu berkas PDF di bawah 1 MB (nama berkas dibentuk server), Usage `0`.
  - DU-012-2: Service Center `Hapus Sisa {runId}`, Status `Active`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Alor Setar {runId}`, Company phone `+60 4555060606`, Usage `0`.

## Test Steps

### Lampiran Service Center dapat dibuka sebelum Delete
1. Ketik Search `Hapus Uji {runId}`, tekan Enter
2. Klik Name `Hapus Uji {runId}`
3. Verifikasi lampiran pada Overview Attachments dapat dibuka
4. Catat alamat lampiran pada Overview Attachments
5. Klik breadcrumb `Service Center`

### Delete Service Center yang Usage-nya 0
6. Ketik Search `Hapus Uji {runId}`, tekan Enter
7. Verifikasi baris `Hapus Uji {runId}` tampil dengan kolom Usage `0`
8. Klik `⋯` pada baris `Hapus Uji {runId}`
9. Klik `Delete`
10. Klik `[Delete]` pada dialog `Delete Service Center`
11. Verifikasi toast `Success, Hapus Uji {runId} has been deleted.` tampil
12. Ganti isi kotak search dengan `{runId}`, tekan Enter
13. Verifikasi tabel memuat baris `Hapus Sisa {runId}`
14. Verifikasi baris `Hapus Uji {runId}` tidak tampil di tabel

### Changelog mencatat Delete dan entri lama tetap
15. Klik `[Changelog]`
16. Ketik Search `Hapus Uji {runId}`, tekan Enter
17. Verifikasi tabel Changelog memuat baris dengan Action `Deleted`, Field `Name`, Old Value `Hapus Uji {runId}`, dan New Value `—`
18. Verifikasi tabel Changelog memuat baris dengan Action `Deleted`, Field `Attachments`, Old Value nama berkas lampiran milik DU-012-1, dan New Value `—`
19. Verifikasi tabel Changelog tetap memuat baris dengan Action `Created`, Field `Name`, dan New Value `Hapus Uji {runId}`
20. Klik ikon close pada modal `Changelog: Service Center`

### Lampiran tidak lagi dapat dibuka setelah Delete
21. Buka alamat lampiran yang dicatat pada langkah 4
22. Verifikasi lampiran tidak dapat dibuka
