---
id: TC-AC-ACTS-E2E-260-modal-event-log-dan-approvals-tab-active-isi-sel-berkas-xlsx
title: "Modal Event Log (Tab Add Stock dan Tab Audit TAG) serta Approvals Tab Active: Isi Sel Berkas XLSX per Tipe Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-516
  - TC-AC-ACTS-609
  - TC-AC-ACTS-926
coverage:
  web: automated
---

# Modal Event Log (Tab Add Stock dan Tab Audit TAG) serta Approvals Tab Active: Isi Sel Berkas XLSX per Tipe Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed: tabel yang diunduh mengandung seluruh jenis nilai kolom termasuk sel kosong `—`: Event Log Tab Add Stock dan Tab Audit TAG SKU `Fixture.tagStock.skuRfid` (sesi dengan dan tanpa reader), serta Approvals > Tab Active (termasuk satu Subject Activation Collision dari Client BYO tanpa SKU). Di-seed fixture BE di hook `before`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembaca isi berkas XLSX hasil unduhan (kelas f, binary buffer), disediakan tim FE.
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-516: Download modal Event Log (Tab Add Stock): isi sel per tipe kolom

4. Klik icon Download, pilih `Download as XLSX`
5. Buka berkas XLSX hasil unduhan dan bandingkan dengan tabel di layar
6. Verifikasi kolom Date pada berkas mengikuti format tanggal General Settings
7. Verifikasi kolom Activity pada berkas ditulis teks apa adanya (`Add Stock` atau `Delete Stock`)
8. Verifikasi kolom Success, Waiting for Approval, dan Failed pada berkas ditulis sebagai sel angka
9. Verifikasi sel `—` pada kolom Success, Waiting for Approval, dan Failed ditulis `-`
10. Verifikasi kolom Hardware pada berkas ditulis teks nama reader
11. Verifikasi sel `—` pada kolom Hardware ditulis `-`
12. Verifikasi kolom Modified By pada berkas ditulis `[first name] [inisial]`
13. Verifikasi kolom Actions tidak ikut di berkas
14. Klik tab `Audit TAG`

### TC-AC-ACTS-926: Download modal Event Log (Tab Audit TAG): isi sel per tipe kolom

15. Klik icon Download, pilih `Download as XLSX`
16. Buka berkas XLSX hasil unduhan dan bandingkan dengan tabel di layar
17. Verifikasi kolom Date pada berkas mengikuti format tanggal General Settings
18. Verifikasi kolom Found dan Not Found pada berkas ditulis sebagai sel angka
19. Verifikasi kolom Not Found Action pada berkas ditulis teks apa adanya
20. Verifikasi sel `—` pada kolom Not Found Action ditulis `-`
21. Verifikasi kolom Hardware pada berkas ditulis teks nama reader
22. Verifikasi sel `—` pada kolom Hardware ditulis `-`
23. Verifikasi kolom Modified By pada berkas ditulis `[first name] [inisial]`
24. Verifikasi kolom Actions tidak ikut di berkas
25. Tutup modal Event Log dengan klik (X)
26. Buka Approvals > TAG Stock lewat sidebar
27. Klik Tab `Active`

### TC-AC-ACTS-609: Download Approvals > TAG Stock > Tab Active: isi sel per tipe kolom

28. Klik icon Download, pilih `Download as XLSX`
29. Buka berkas XLSX hasil unduhan dan bandingkan dengan tabel di layar
30. Verifikasi kolom Type pada berkas ditulis label teks tanpa warna
31. Verifikasi kolom Device Name (SKU) pada berkas ditulis `[Device Name] ([SKU])`
32. Verifikasi baris Client BYO tanpa SKU pada berkas ditulis `[Device Name] (-)`
33. Verifikasi kolom Matched Identifier pada berkas ditulis nilai identifier
34. Verifikasi kolom Requested At pada berkas mengikuti format tanggal General Settings

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Spec ini memuat asersi isi berkas (kelas f) saja; nama berkas dan ekstensi diasersi di spec 236 (TC-AC-ACTS-514 dan 515), 244 (TC-AC-ACTS-924 dan 925), dan 258 (TC-AC-ACTS-607 dan 608).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-516, 926, dan 609 tidak menyebut format tanggal General Settings yang dipakai; spec mengasersi bahwa kolom tanggal mengikuti General Settings tanpa nilai literal.
  - TC-AC-ACTS-609 Expected b menyebut baris Client BYO tanpa SKU ditulis `[Device Name] (-)`, sedangkan TC-AC-ACTS-568 menampilkannya sebagai `(—)` di UI; spec mengikuti rumusan masing-masing TC.
