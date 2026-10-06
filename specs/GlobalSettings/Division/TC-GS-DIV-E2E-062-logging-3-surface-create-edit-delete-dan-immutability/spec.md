---
id: TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability
title: "Sinkronisasi Pencatatan Mutasi 3 Surface (Changelog, System Log, Activity Log) dan Immutability Snapshot"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-131
  - TC-GS-DIV-132
  - TC-GS-DIV-133
  - TC-GS-DIV-134
  - TC-GS-DIV-135
  - TC-GS-DIV-204
  - TC-GS-DIV-277
coverage:
  web: automated
---

# Sinkronisasi Pencatatan Mutasi 3 Surface (Changelog, System Log, Activity Log) dan Immutability Snapshot

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

1. Buat divisi baru bernama 'Audit Log Test' dengan Code manual 'ALT'
2. Buka Modal Changelog dan verifikasi tercatat TEPAT 1 entri Create dengan Field = 'Division Name', Old = '—', New = 'Audit Log Test' (Field Code TIDAK dicatat saat Create)
3. Buka menu Global Settings > Activity Log dan verifikasi mutasi tercatat pada Tab User Action
4. Buka tab User > detail salah satu user > Tab System Log dan verifikasi event mutasi tercatat
5. Lakukan Edit pada divisi 'Audit Log Test' mengubah namanya menjadi 'Audit Test Updated' dan Code menjadi 'ATU'
6. Verifikasi Changelog mencatat 2 entri Edit terpisah: 1 baris Field = 'Division Name' dan 1 baris Field = 'Code'
7. Lakukan Edit kedua mengubah nama kembali menjadi 'Audit Test Final'
8. Verifikasi entri log terdahulu TETAP menampilkan snapshot nilai lama tanpa berubah retroaktif (Snapshot Immutability)
9. Lakukan Delete pada divisi tersebut dan verifikasi tercatat entri Delete dengan Old = 'Audit Test Final' dan New = '—'
10. Verifikasi pada seluruh entri log tidak pernah ada kondisi di mana Old Value dan New Value keduanya bernilai '—' secara bersamaan

## Notes

- Memvalidasi integritas audit trail atomik pada ketiga surface sesuai division.md §8 dan DIV-LOGIC-03.
