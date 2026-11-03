---
id: TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger
title: "Delete Unit: Dialog Delete Unit, Cancel, Unit Waiting Tanpa Delete, Guard Combined (D-07) dan Existing Record (D-08), Urutan Evaluasi Guard, dan Saldo Ledger Negatif (T-16)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-360
  - TC-AC-ACTS-363
  - TC-AC-ACTS-364
  - TC-AC-ACTS-366
  - TC-AC-ACTS-367
  - TC-AC-ACTS-368
  - TC-AC-ACTS-369
coverage:
  web: automated
---

# Delete Unit: Dialog Delete Unit, Cancel, Unit Waiting Tanpa Delete, Guard Combined (D-07) dan Existing Record (D-08), Urutan Evaluasi Guard, dan Saldo Ledger Negatif (T-16)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data tambahan milik spec: unit CP yang sekaligus Combined set aktif dan Existing Record Subject pending (TC-AC-ACTS-368). Saldo Stock Ledger entitas registrant diset 0 oleh fixture BE sebelum TC-AC-ACTS-369 (semua dialokasikan lewat Device Allocation) dan dipulihkan di hook `after`.
- Kemampuan teknis: Sesi API aktor untuk meng-approve Subject pending (TC-AC-ACTS-367, pelaku kedua yang hanya memicu perubahan state), disediakan tim BE/FE (lihat `suite.md`).
- Pembacaan Activity Log (Search TAG Code) untuk TC-AC-ACTS-369 memakai baseline sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-360: Klik Delete membuka dialog Delete Unit

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik (⋯) pada unit Available U1 (`TAG-4F7K2XQ9`)
3. Klik `Delete`
4. Verifikasi dialog `Delete Unit` memuat `• TAG-4F7K2XQ9`, `For more accurate results, use Delete by Scan.`, dan `This action cannot be undone. Are you sure you want to delete it?` dengan tombol `[Cancel]` dan `[Delete]`

### TC-AC-ACTS-363: `[Cancel]` pada dialog Delete Unit tidak menghapus

5. Klik `[Cancel]` pada dialog yang terbuka
6. Klik (⋯) pada unit U1, lalu klik `Delete`
7. Klik `[Cancel]`
8. Verifikasi dialog tertutup
9. Verifikasi unit U1 tetap ada di Tab Available

### TC-AC-ACTS-364: Unit Waiting for Approval tidak muncul di Tab Available; Tab In Use tanpa row action Delete

10. Verifikasi Tab Available memuat baris unit Available dan Damaged/Missing (pembanding)
11. Verifikasi unit Waiting for Approval W1 tidak ada di Tab Available sehingga tidak ada row action `Delete` untuk unit itu
12. Buka Tab In Use
13. Klik (⋯) pada satu baris
14. Verifikasi row action Tab In Use hanya `TAG Log`, tanpa `Delete`
15. Tutup menu aksi dan kembali ke Tab Available

### TC-AC-ACTS-366: Delete unit komponen Combined set memunculkan dialog blok D-07

16. Klik (⋯) pada unit Combined C1, lalu klik `Delete`
17. Verifikasi dialog blok `Cannot Delete Unit` dengan bullet `• [TAG Code]` dan `This unit is part of a Combined TAG. Separate it first before deleting.` serta tombol `[OK]`
18. Verifikasi dialog konfirmasi `D-05` tidak tampil
19. Klik `[OK]`
20. Verifikasi dialog tertutup dan unit C1 tetap ada

### TC-AC-ACTS-368: Urutan evaluasi bila beberapa guard terpenuhi (T-17, D-07, D-08)

21. Klik (⋯) pada unit CP (berstatus Available, Combined, dan sekaligus Existing Record Subject pending), lalu klik `Delete`
22. Verifikasi dialog blok `D-07` tampil: `This unit is part of a Combined TAG. Separate it first before deleting.`
23. Verifikasi dialog `D-08` tidak tampil
24. Verifikasi dialog konfirmasi `D-05` tidak tampil
25. Verifikasi tidak ada toast `T-17` (`This unit is no longer available.`) karena unit berstatus Available
26. Klik `[OK]`

### TC-AC-ACTS-369: Delete ditolak bila saldo Stock Ledger akan negatif (T-16)

27. Atur saldo Stock Ledger entitas registrant menjadi 0 lewat fixture BE
28. Catat baseline jumlah entri Activity Log `TAG Stock` untuk unit U2 (Search TAG Code)
29. Klik (⋯) pada unit Available U2, lalu klik `Delete`
30. Klik `[Delete]`
31. Verifikasi Delete ditolak dengan toast error `Error, failed to delete unit.`
32. Verifikasi unit U2 tetap ada di Tab Available
33. Buka Activity Log (filter Object `TAG Stock`)
34. Verifikasi jumlah entri Activity Log untuk unit U2 sama dengan baseline langkah 28
35. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
36. Pulihkan saldo Stock Ledger entitas registrant ke nilai sebelum langkah 27 lewat fixture BE

### TC-AC-ACTS-367: Delete unit Existing Record Subject pending memunculkan dialog blok D-08

37. Klik (⋯) pada unit P1 (Existing Record Subject Register Duplicate pending), lalu klik `Delete`
38. Verifikasi dialog blok `Cannot Delete Unit` dengan bullet `• [TAG Code]` dan `This unit is referenced by a pending approval and cannot be deleted.` serta tombol `[OK]`
39. Verifikasi dialog konfirmasi `D-05` tidak tampil
40. Klik `[OK]`
41. Sesi API meng-approve Subject yang merujuk P1 hingga status resolved tersimpan
42. Muat ulang halaman
43. Klik (⋯) pada unit P1, lalu klik `Delete`
44. Verifikasi dialog konfirmasi `Delete Unit` tampil (bukan dialog blok)
45. Klik `[Delete]`
46. Verifikasi unit P1 tidak ada di Tab Available

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Cancel]` dan `[OK]` dialog, pembukaan dan penutupan menu aksi, "Atur saldo Stock Ledger" dan pemulihannya lewat fixture BE, navigasi ke Activity Log, dan "Muat ulang halaman" sesudah Subject di-approve. Urutan TC: 360, 363, 364, 366, 368, 369, 367; TC-AC-ACTS-367 diletakkan terakhir karena menghapus unit P1 pada bagiannya (aksi menghapus data di akhir).
- P-1: bagian "tidak ada log baru" TC-AC-ACTS-369 diasersi sebagai jumlah entri Activity Log sama dengan baseline di spec ini karena bergantung pada state saldo Stock Ledger 0 yang dibangun fixture BE sebelum aksi TC yang sama; tidak ada spec absence untuk TC itu.
- Temuan untuk QA:
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - Langkah Uji TC-AC-ACTS-363 nomor 1 menyebut "Klik (⋯) > Delete" tanpa menyebut unit; spec memakai unit U1.
  - TC-AC-ACTS-368 menyebut "Klik `[Delete]` pada unit itu" tanpa langkah membuka menu aksi; spec membuka (⋯) > `Delete`. Pre-setup dan Dinamis TC tidak mendaftar unit Combined sekaligus Existing Record (CP); unit itu dari seeding. Precondition TC-AC-ACTS-368 menyebut unit target berstatus Available, sehingga toast `T-17` tidak boleh tampil.
  - TC-AC-ACTS-367 butir c ("Setelah Subject resolved unit dapat dihapus") tidak punya langkah observasi; spec men-approve Subject lewat sesi API dan menghapus unit P1 untuk mengasersinya. Kode pesan D-05, D-07, D-08 pada Expected dibandingkan dengan teks dialog yang ditulis TC.
  - TC-AC-ACTS-369 mengharapkan toast `Error, failed to delete unit.` (T-16) untuk kondisi saldo negatif, sama dengan toast kegagalan 5xx pada TC-AC-ACTS-370; perbedaan sebab tidak teramati di UI.
