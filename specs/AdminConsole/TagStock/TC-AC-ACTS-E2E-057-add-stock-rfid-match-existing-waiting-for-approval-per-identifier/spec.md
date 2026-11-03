---
id: TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier
title: "Add Stock RFID: Scan Cocok Unit Existing Menjadi Waiting for Approval (EPC Saja, UID Saja, Keduanya, Dua Unit Berbeda)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-144
  - TC-AC-ACTS-145
  - TC-AC-ACTS-146
  - TC-AC-ACTS-147
  - TC-AC-ACTS-148
coverage:
  web: automated
---

# Add Stock RFID: Scan Cocok Unit Existing Menjadi Waiting for Approval (EPC Saja, UID Saja, Keduanya, Dua Unit Berbeda)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Akun aktor kedua (Ganti akun): Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
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

- Unit existing (status Available) di-seed fixture BE milik spec dan dipulihkan di hook `after`: unit 1 memegang EPC dan UID TAG A; unit 2 memegang EPC TAG B (UID TAG B baru); unit 3 memegang UID TAG C (EPC TAG C baru); unit X memegang EPC TAG D dan unit Y memegang UID TAG D (dua unit berbeda). Jalur approval normal (tanpa bypass E2a).
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
3. Klik `[Add by Scan]`
4. Scan TAG A
5. Scan TAG B
6. Scan TAG C
7. Scan TAG D
8. Klik `[Stop]`

### TC-AC-ACTS-144: Scan cocok unit existing menjadi Waiting for Approval

9. Verifikasi baris TAG A berstatus Waiting for Approval (severity warning) di Scanned TAG List
10. Hover badge Waiting TAG A
11. Verifikasi tooltip badge `TAG <EPC TAG A> matches an existing registered TAG. It will be sent for approval.`
12. Verifikasi baris TAG A belum memiliki TAG Code

### TC-AC-ACTS-145: Hanya EPC cocok unit existing

13. Verifikasi baris TAG B berstatus Waiting for Approval

### TC-AC-ACTS-146: Hanya UID cocok unit existing

14. Verifikasi baris TAG C berstatus Waiting for Approval

### TC-AC-ACTS-148: EPC dan UID cocok ke dua unit existing berbeda

15. Verifikasi baris TAG D berstatus Waiting for Approval

### TC-AC-ACTS-145 sampai TC-AC-ACTS-148: Submit lalu periksa Subject di Approvals

16. Klik `[Submit]`
17. Tunggu aksi selesai
18. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
19. Buka Approvals > TAG Stock > Tab Active
20. Ketik Search `<EPC TAG B>`, tekan Enter
21. Verifikasi Matched Identifier Subject TAG B menampilkan nilai EPC dengan badge `[EPC]`
22. Ganti isi kotak search dengan `<UID TAG C>`, tekan Enter
23. Verifikasi Matched Identifier Subject TAG C menampilkan nilai UID dengan badge `[UID]`
24. Ganti isi kotak search dengan `<UID TAG A>`, tekan Enter
25. Verifikasi satu Subject dibuat untuk TAG A (EPC dan UID cocok ke unit existing yang sama)
26. Verifikasi Matched Identifier Subject TAG A menampilkan nilai UID dengan badge `[UID]`
27. Ganti isi kotak search dengan `<EPC TAG D>`, tekan Enter
28. Verifikasi hanya satu Subject dibuat untuk TAG D
29. Verifikasi Existing Record Subject TAG D adalah unit Y (UID menang)
30. Verifikasi Matched Identifier Subject TAG D adalah UID dengan badge `[UID]`
31. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- TC-AC-ACTS-144 sampai TC-AC-ACTS-148 berbagi satu sesi scan dan satu Submit karena precondition-nya identik (akun Distributor Toggle ON, jalur approval normal, reader terhubung, unit existing seed). TC-AC-ACTS-147 memakai TAG A yang sama dengan TC-AC-ACTS-144 (EPC dan UID cocok unit yang sama). Urutan asersi mengikuti urutan keadaan: status di list lebih dulu (sebelum Submit), Subject di Approvals sesudah Submit.
- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), `[Stop]`, Search di Approvals untuk menemukan Subject target (R-16), dan reset Search di akhir. Hook `after` memulihkan sesi ke Total Control.
- Temuan untuk QA:
  - TC-AC-ACTS-145 dan TC-AC-ACTS-146 tidak memuat langkah `[Submit]` padahal Expected (b) membaca Subject di Approvals; spec menambahkan satu `[Submit]` bersama TC-AC-ACTS-147 dan TC-AC-ACTS-148.
  - TC-AC-ACTS-145 sampai TC-AC-ACTS-148 menulis identifier unit existing dalam bentuk singkatan (`E280...01`, `A1B2...F6`); spec memakai identifier fixture milik spec.
  - TC-AC-ACTS-144 Expected (c) "tidak mendapat TAG Code sampai di-review" diasersi pada baris Scanned TAG List saja.
  - Hasil Submit (toast dan navigasi) tidak ada di Expected TC-AC-ACTS-145 sampai TC-AC-ACTS-148 sehingga tidak diasersi.
- Langkah penghubung tambahan (S-03, 8b butir 8): "Tunggu aksi selesai" (langkah 17) sesudah `[Submit]` yang hasilnya tidak diasersi dan sebelum ganti akun.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
