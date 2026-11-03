---
id: TC-AC-ACTS-E2E-069-add-stock-ble-screening-sesi-scan-baris-ok-dan-mode-terkunci
title: "Add Stock BLE: Screening Idle, Sesi Scan Mengunci Halaman, Scan Baru Menjadi OK, dan Mode Scan Terkunci"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-211
  - TC-AC-ACTS-212
  - TC-AC-ACTS-213
  - TC-AC-ACTS-219
coverage:
  web: automated
---

# Add Stock BLE: Screening Idle, Sesi Scan Mengunci Halaman, Scan Baru Menjadi OK, dan Mode Scan Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #14 `BLE-BEACON-ALPHA-B1` (Device Name `BLE Beacon Alpha`, Brand `Alpha`, Model `B1`, TAG Type BLE).
- Kemampuan teknis: simulator pemindai BLE (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji BLE (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
2. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-211: Screening halaman Add Stock BLE saat Idle

3. Verifikasi Breadcrumb `TAG > Stock > Detail > Add Stock`
4. Verifikasi judul `Add Stock` tanpa kode SKU
5. Verifikasi SKU info card baris 1 `BLE Beacon Alpha (BLE-BEACON-ALPHA-B1)` setelah foto
6. Verifikasi `TAG Type:` dengan icon BLE
7. Verifikasi `Brand:` dengan badge `Alpha`
8. Verifikasi `Model/Type:` dengan badge `B1`
9. Verifikasi tombol `[Add by Scan]` tampil
10. Verifikasi tombol `[Remove by Scan]` tampil dalam keadaan disabled
11. Verifikasi Scanned TAG List dengan kolom `Checkbox | # | MAC Address | Status`
12. Verifikasi pesan `Ready to scan. Point the reader at TAGs.`
13. Verifikasi `[Cancel]` (text, contrast) tampil
14. Verifikasi `[Submit]` (Success) tampil dan enabled

### TC-AC-ACTS-212 dan TC-AC-ACTS-213: Sesi scan mengunci halaman dan scan baru menjadi baris OK

15. Klik `[Add by Scan]`
16. Scan TAG A
17. Verifikasi seluruh halaman blur ringan dan non-interaktif
18. Verifikasi Floating Status Widget di kanan bawah menampilkan `Adding TAGs...`
19. Verifikasi live counter widget `1 TAG scanned`
20. Verifikasi tombol `[Stop]` satu-satunya yang bisa diklik
21. Verifikasi baris baru tetap samar terlihat di Scanned TAG List
22. Klik `[Stop]`
23. Verifikasi satu baris di Scanned TAG List dengan Status OK (severity success)
24. Hover badge OK
25. Verifikasi tidak ada tooltip pada badge OK
26. Verifikasi baris belum memiliki TAG Code

### TC-AC-ACTS-219: Mode scan terkunci selama sesi aktif

27. Klik `[Add by Scan]`
28. Coba klik `[Remove by Scan]` selama sesi aktif
29. Verifikasi tidak ada switch mode (selain `[Stop]` tidak ada kontrol yang bisa diklik)
30. Klik `[Stop]`, lalu klik `[Remove by Scan]`
31. Verifikasi sesi baru dimulai dari Idle dengan widget `Removing TAGs...`
32. Klik `[Stop]`
33. Klik `[Cancel]`
34. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
35. Klik `[Leave]`

## Notes

- TC-AC-ACTS-212 dan TC-AC-ACTS-213 berbagi satu sesi scan dengan satu TAG (212 diamati saat sesi aktif, 213 sesudah `[Stop]`); preconditionnya identik.
- Langkah penghubung (S-03): langkah 1 dan 2 (mencari SKU dan membuka halaman Add Stock dari Stock List, precondition TC) dan penutupan halaman dirty di akhir (S-08, S-09).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
