---
id: TC-AC-ACTS-E2E-265-isi-sel-detail-sku-tab-available-tab-in-use-dan-approvals-tab-history-berkas-xlsx
title: "Detail SKU Tab Available dan Tab In Use serta Approvals Tab History: Isi Sel Berkas XLSX per Tipe Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-424
  - TC-AC-ACTS-470
  - TC-AC-ACTS-653
coverage:
  web: automated
---

# Detail SKU Tab Available dan Tab In Use serta Approvals Tab History: Isi Sel Berkas XLSX per Tipe Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12); `skuNfc` = `NFC-CARD-BETA-N2` (SKU NFC, Pre-setup #13).
- Data TC-AC-ACTS-424: SKU `Fixture.tagStock.skuNfc` memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing, termasuk unit non-RFID (Identifier (UID, RFID) kosong), dan satu unit Waiting for Approval W1 (disediakan fixture BE).
- Data TC-AC-ACTS-470: SKU `Fixture.tagStock.skuRfid` memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing; ada unit In Use dengan Status belum sinkron (`—`) dan unit BYO atau Jalur B (Registered By `—`).
- Data TC-AC-ACTS-653: Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) termasuk sel Approver dan TAG Code kosong (disediakan fixture BE).
- Kemampuan teknis (kelas f, binary buffer): pembaca isi berkas XLSX hasil unduhan dan pembanding dengan tabel di layar, disediakan tim FE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec), pembacaan state BE yang tidak terlihat di UI, dan sesi API aktor, disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data.

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.tagStock.skuNfc`; pastikan Tab `Available` aktif

### TC-AC-ACTS-424: Download Detail SKU Tab Available: isi sel per tipe kolom

2. Klik icon Download, pilih `Download as XLSX`
3. Buka file dan bandingkan dengan tabel di layar
4. Verifikasi Status ditulis sebagai label teks (`Available`, `Damaged/Missing`)
5. Verifikasi file tidak memuat baris unit Waiting for Approval
6. Verifikasi Identifier (UID, RFID) non-RFID ditulis `-`
7. Verifikasi Registered At mengikuti General Settings
8. Verifikasi Registered By ditulis `[first name] [inisial]`

### TC-AC-ACTS-470: Download Detail SKU Tab In Use: isi sel per tipe kolom

9. Klik Breadcrumb `Stock`
10. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`, klik Tab `In Use`
11. Klik icon Download, pilih `Download as XLSX`
12. Buka file dan bandingkan dengan tabel di layar
13. Verifikasi Status ditulis sebagai label teks (`Available` atau `Damaged/Missing`)
14. Verifikasi Status yang belum sinkron ditulis `-`
15. Verifikasi Client ditulis nama perusahaan
16. Verifikasi Registered At dan Activated At mengikuti General Settings
17. Verifikasi Registered By ditulis `[first name] [inisial]`
18. Verifikasi Registered By unit BYO ditulis `-`

### TC-AC-ACTS-653: Download Approvals > TAG Stock > Tab History: isi sel per tipe kolom

19. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
20. Klik icon Download, pilih `Download as XLSX`
21. Buka file dan bandingkan dengan tabel di layar
22. Verifikasi Approval ditulis label teks (`Approved`, `Rejected`, `Canceled`) tanpa warna
23. Verifikasi Approver dan TAG Code kosong ditulis `-`
24. Verifikasi Requested At dan Resolved At mengikuti General Settings

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat asersi isi berkas (kelas f) saja; nama berkas dan ekstensi diasersi di spec 180 (TC-AC-ACTS-422 dan 423), 195 (TC-AC-ACTS-468 dan 469), dan 211 (TC-AC-ACTS-651 dan 652). Isi sel Stock List, Event Log, dan Approvals Tab Active ada di spec 037 dan 260.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU `Fixture.tagStock.skuNfc`), langkah 9 dan 10 (kembali ke Stock List dan membuka Tab `In Use` SKU RFID), dan langkah 19 (membuka Approvals > TAG Stock Tab `History`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-424 memakai SKU `NFC-CARD-BETA-N2` dengan satu unit Waiting for Approval W1; unit non-RFID dan unit W1 disediakan fixture BE karena TC tidak menyebut identitasnya.
  - TC-AC-ACTS-470 Expected a menyatakan "`-` bila belum sinkron" dan Expected d "`-` untuk BYO" tanpa menyebut unit seed; disediakan fixture BE.
  - Pembaca isi berkas dan format tanggal General Settings tidak disebut TC; disediakan tim FE.
