---
id: TC-AC-ACTS-E2E-060-add-stock-rfid-bypass-e2a-total-control-pada-batch-campuran
title: "Add Stock RFID: Bypass E2a oleh Total Control, Tidak Menampilkan Waiting, dan Unit Bypass Tidak Masuk Quantity dan Success Event Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-181
  - TC-AC-ACTS-778
coverage:
  web: automated
---

# Add Stock RFID: Bypass E2a oleh Total Control, Tidak Menampilkan Waiting, dan Unit Bypass Tidak Masuk Quantity dan Success Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |
| TAG C | `Fixture.tagStock.rfidC.epc` | `Fixture.tagStock.rfidC.uid` |
| TAG D | `Fixture.tagStock.rfidD.epc` | `Fixture.tagStock.rfidD.uid` |

- Unit existing Available U1 memegang identifier TAG A dan TAG D (sama), di-seed fixture BE milik spec; jalur bypass E2a (Total Control).
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: jumlah entri `Add Stock` dan `Duplicate Approved` di Activity Log, jumlah baris Event Log Tab Add Stock SKU `RFID-ASSET-CORE-R5`, dan saldo Stock Ledger entitas registrant (lewat kemampuan baca BE)
2. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
3. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-181: Total Control tidak menampilkan Waiting (bypass E2a)

4. Klik `[Add by Scan]`
5. Scan TAG A yang cocok unit existing U1
6. Klik `[Stop]`
7. Verifikasi baris TAG A berbadge OK tanpa tooltip match
8. Klik `[Submit]`
9. Verifikasi tidak ada dialog `Partial Register`
10. Verifikasi tidak ada toast T-04
11. Verifikasi toast `Success, TAG has been registered.`
12. Verifikasi TAG A terdaftar dengan TAG Code baru
13. Klik Breadcrumb `Stock`
14. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
15. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-778: Bypass E2a pada batch campuran

16. Catat ulang baseline sesudah Submit TC-AC-ACTS-181: jumlah entri `Add Stock` dan `Duplicate Approved` di Activity Log, jumlah baris Event Log Tab Add Stock SKU `RFID-ASSET-CORE-R5`, dan saldo Stock Ledger entitas registrant (lewat kemampuan baca BE)
17. Klik `[Add by Scan]`
18. Scan TAG B dan TAG C (baru) lalu scan TAG D yang cocok unit existing U1
19. Klik `[Stop]`
20. Klik `[Submit]`
21. Verifikasi ketiga baris berbadge OK
22. Verifikasi tidak ada dialog `Partial Register`
23. Verifikasi toast `Success, TAG has been registered.`
24. Verifikasi tiga unit baru Available dengan TAG Code baru di Tab Available
25. Buka Activity Log
26. Verifikasi satu entri `Add Stock` baru dari baseline langkah 16 dengan New Value `2 TAGs` (unit bypass tidak dihitung)
27. Verifikasi satu entri `Duplicate Approved` baru dari baseline langkah 16 (Field `Status`, Old `—`, New `Available`, Modified By requester)
28. Buka modal Event Log SKU (Tab Add Stock)
29. Verifikasi satu baris baru dari baseline langkah 16, Activity `Add Stock` dengan Success `2` (unit bypass tidak dihitung)
30. Verifikasi tidak ada baris `Duplicate Approved` baru di Event Log dibanding baseline langkah 16
31. Tutup modal Event Log
32. Buka Device Allocation > Stock Balance Summary Panel
33. Verifikasi saldo Stock Ledger entitas registrant bertambah 3 dari baseline langkah 16

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), `[Stop]`, penutupan modal Event Log, dan pencatatan baseline.
- Asersi "tidak ada baris `Duplicate Approved` di Event Log" TC-AC-ACTS-778 (d) ditulis sebagai selisih nol terhadap baseline dengan anchor baris `Add Stock` baru pada surface yang sama; bukan kelas g (bagian 3, asersi jumlah).
- TC-AC-ACTS-779 dan TC-AC-ACTS-946 (batch seluruhnya bypass tanpa entri `Add Stock` atau baris Event Log) ada di spec 077.
- Temuan untuk QA: TC-AC-ACTS-181 tidak menyebut SKU dan reader; spec memakai SKU `RFID-ASSET-CORE-R5` dan reader RFID terhubung seperti TC lain halaman Add Stock RFID. Unit existing U1 dan identifier-nya diseed fixture BE milik spec.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
