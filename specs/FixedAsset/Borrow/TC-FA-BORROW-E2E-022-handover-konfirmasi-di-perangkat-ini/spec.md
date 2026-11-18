---
id: TC-FA-BORROW-E2E-022-handover-konfirmasi-di-perangkat-ini
title: "Request Confirmation dan Confirm on This Device menyelesaikan handover dengan Due date baris dan jendela konfirmasi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-75", "FI-BRW-76", "FI-BRW-77", "FI-BRW-78"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-75": 9
  "FI-BRW-76": [11, 12, 14, 17, 19]
  "FI-BRW-77": [21, 24, 27]
  "FI-BRW-78": 27
anchor: []
coverage:
  web: automated
---

# Request Confirmation dan Confirm on This Device menyelesaikan handover dengan Due date baris dan jendela konfirmasi

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-022-1: BRW `Waiting for Handover` Group `Head Office`, Borrower `Indra Gunawan {runId}` (punya akun tetapi tidak membawa HP saat serah terima), Requested By `Agus Pratama {runId}`, Photo at start OFF pada semua barisnya.
  - DU-022-2: aset `Laptop HP ProBook {runId}`, TAG `RFID`, Duration `3 / 7 days`, Purpose `Presentasi klien`, baris `Waiting for Handover`.
  - DU-022-3: aset `Tablet Lenovo {runId}`, TAG `QR`, Duration `2 / 7 days`, Purpose `Rapat divisi`, baris `Waiting for Handover`.
  - Due date aset DU-022-2 sesudah dikonfirmasi: T0 + 2 hari (tanggal handover T0 ditambah Duration 3 hari dikurangi 1 hari), berakhir pukul 23:59:59.

## Test Steps

### Request Confirmation membuka popup Waiting for Confirmation
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Indra Gunawan {runId}`, tekan Enter
4. Klik menu ⋯ pada baris BRW milik DU-022-1
5. Klik `Hand Over`
6. Scan TAG aset DU-022-2 lewat `[Verify Asset]`
7. Scan TAG aset DU-022-3 lewat `[Verify Asset]`
8. Klik `[Request Confirmation]`
9. Verifikasi popup `Waiting for Confirmation` tampil dengan tombol `[Cancel Request]` dan `[Confirm on This Device]` sebagai cara konfirmasi untuk Borrower yang tidak membawa HP

### Dialog Confirm Receipt mensyaratkan pernyataan dan minimal satu aset tercentang
10. Klik `[Confirm on This Device]`
11. Verifikasi dialog `Confirm Receipt` tampil dengan nama Borrower `Indra Gunawan {runId}`, teks `Uncheck any asset [Borrower] didn't receive.`, aset DU-022-2 dan DU-022-3 tercentang, dan checkbox pernyataan `I confirm that [Borrower] is here and has received the checked assets.`
12. Verifikasi tombol `[Confirm]` nonaktif karena checkbox pernyataan belum dicentang
13. Centang checkbox pernyataan
14. Verifikasi tombol `[Confirm]` aktif karena checkbox pernyataan dicentang dan dua aset tercentang
15. Hapus centang aset DU-022-2
16. Hapus centang aset DU-022-3
17. Verifikasi teks `Check at least one asset received.` tampil dan tombol `[Confirm]` nonaktif
18. Centang aset DU-022-2
19. Verifikasi tombol `[Confirm]` aktif karena checkbox pernyataan dicentang dan satu aset tercentang

### Konfirmasi dicatat atas nama Borrower dengan tanggung jawab pada Aktor
20. Klik `[Confirm]`
21. Verifikasi popup hasil menampilkan `[Borrower] confirmed 1 asset.` dengan [Borrower] berisi `Indra Gunawan {runId}`, `1 asset not received.`, aset DU-022-2 `Confirmed`, dan aset DU-022-3 `Not received`
22. Klik `[Done]`
23. Buka Borrow Detail BRW milik DU-022-1 dari tabel Transactions
24. Verifikasi baris aset DU-022-2 `Borrowed` dengan Due date T0 + 2 hari dan baris aset DU-022-3 `Waiting for Handover` dengan Due date `—`
25. Klik menu ⋯ pada baris aset DU-022-2
26. Klik `Borrow Log`
27. Verifikasi detail Confirmation pada node Handed over memuat `Confirmed by [Aktor Borrow] on behalf of [Borrower]` dengan [Aktor Borrow] berisi `Agus Pratama {runId}` dan [Borrower] berisi `Indra Gunawan {runId}`, sebagai pernyataan yang menjadi tanggung jawab `Agus Pratama {runId}`
