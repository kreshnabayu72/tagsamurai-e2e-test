---
id: TC-GS-POS-E2E-045-absence-log-pada-edit-no-op
title: "Asersi Absence: Edit No-Op tidak menghasilkan entri baru pada Changelog, Activity Log, maupun System Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-246
  - TC-GS-POS-308
coverage:
  web: automated
---

# Asersi Absence: Edit No-Op tidak menghasilkan entri baru pada Changelog, Activity Log, maupun System Log

## Prerequisites

- Login sebagai Total Control
- Catat timestamp dan ID log terakhir pada Changelog, Activity Log, dan System Log aktor

## Test Steps

### Eksekusi Edit No-Op

1. Buka modal Edit pada salah satu record Position
2. Tanpa mengubah teks apa pun (atau hanya menambahkan spasi di depan/belakang nama), klik tombol "[Save]"
3. Verifikasi modal tertutup sukses

### Asersi Absence (Log Tidak Bertambah)

4. Buka Popup Changelog: Position
5. Verifikasi TIDAK ADA entri log baru yang ditambahkan dari aksi tersebut
6. Buka halaman Activity Log
7. Verifikasi TIDAK ADA baris activity log baru yang tercatat
8. Buka Detail User aktor > Tab System Log
9. Verifikasi TIDAK ADA entri system log baru yang tercatat

## Notes

- Menggabungkan asersi ketiadaan log (absence) untuk operasi no-op dari TC-GS-POS-246 dan 308.
