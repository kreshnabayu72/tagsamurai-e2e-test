---
id: TC-FA-FAFM-E2E-020-delete-file-single
title: "Delete satu file ke Recycle Bin"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ACT-02f, ARS-01b, ARS-01c, ARS-01d, D-01, DIM-14a, DIM-14b, F-FAFM-02i, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, S-20, SYN-01a, SYN-01c, SYN-01d, SYN-01f, SYN-01b, SYN-01e, SYN-01h, T-01, "§4.4#b9", "EB-FB-1@delete-file"]
smoke: ["EB-FB-1@delete-file"]
dependsOn: []
trace:
  ACT-02e: 17
  ACT-02f: 13
  ARS-01b: 17
  ARS-01c: 14
  ARS-01d: 13
  D-01: [5, 6, 7]
  DIM-14a: [14, 17]
  DIM-14b: 14
  F-FAFM-02i: [14, 17, 21]
  FAFM-LOGIC-02c: [14, 17]
  FAFM-LOGIC-02e: 14
  FAFM-LOGIC-02f: 14
  S-20: 13
  SYN-01a: 17
  SYN-01c: 14
  SYN-01d: 17
  SYN-01f: [14, 17]
  SYN-01b: 14
  SYN-01e: 14
  SYN-01h: 21
  T-01: 13
  "§4.4#b9": [14, 17]
  "EB-FB-1@delete-file": 13
anchor: [2, 9]
coverage:
  web: automated
  android: automated
---

# Delete satu file ke Recycle Bin

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-020-1: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-020-2: File `laptop-front-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `300.0 KB`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Uploaded By `Budi S`, ada di tab `Asset Photo`.
  - Toast yang diharapkan `Success, laptop-front-{runId}.jpg has been deleted.`, dari Name file DU-020-2.

## Test Steps

### Delete dibatalkan lalu dikonfirmasi
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi file `laptop-front-{runId}.jpg` tampil di tab `Asset Photo`
3. Buka aksi baris `laptop-front-{runId}.jpg`
4. Klik `Delete`
5. Verifikasi dialog `Delete File` memuat bullet nama file `laptop-front-{runId}.jpg`
6. Verifikasi anotasi bullet memuat Source `Asset Photo`
7. Verifikasi anotasi bullet memuat nama aset `Laptop Dell Latitude 5420 {runId}`
8. Tutup dialog konfirmasi dengan Cancel
9. Verifikasi file `laptop-front-{runId}.jpg` masih tampil di tab `Asset Photo`
10. Buka aksi baris `laptop-front-{runId}.jpg`
11. Klik `Delete`
12. Klik `[Delete]` pada dialog `Delete File`
13. Verifikasi toast `Success, laptop-front-{runId}.jpg has been deleted.` tampil
14. Verifikasi file `laptop-front-{runId}.jpg` tidak tampil lagi di tab `Asset Photo`

### File masuk Recycle Bin
15. Klik `Recycle Bin` pada header kartu `Storage Usage`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi file `laptop-front-{runId}.jpg` tampil di Recycle Bin
18. Tutup modal `Recycle Bin`

### Delete tercatat di Changelog
19. Klik `Changelog` pada header kartu `Storage Usage`
20. Ketik Search `{runId}`, tekan Enter
21. Verifikasi entri Changelog dengan Action `Delete` untuk File Name `laptop-front-{runId}.jpg` tampil
22. Tutup modal `Changelog`
