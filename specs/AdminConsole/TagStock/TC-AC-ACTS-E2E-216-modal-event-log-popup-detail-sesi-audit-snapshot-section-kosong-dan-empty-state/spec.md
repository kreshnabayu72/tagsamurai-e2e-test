---
id: TC-AC-ACTS-E2E-216-modal-event-log-popup-detail-sesi-audit-snapshot-section-kosong-dan-empty-state
title: "Modal Event Log: Popup Detail Sesi Audit, Snapshot Unit Terhapus, Section Tanpa Baris Disembunyikan, dan Empty State S-28"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-936
  - TC-AC-ACTS-937
  - TC-AC-ACTS-938
  - TC-AC-ACTS-939
coverage:
  web: automated
---

# Modal Event Log: Popup Detail Sesi Audit, Snapshot Unit Terhapus, Section Tanpa Baris Disembunyikan, dan Empty State S-28

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12); `unitU1` = `TAG-4F7K2XQ9` (unit Available U1, Data Uji Dinamis #5).
- Data seed (kemampuan fixture BE): sesi Audit dengan Found `5` dan Not Found `3` (Mark as Damaged/Missing dicentang) tanpa unit dilewati; sesi Delete Stock yang menghapus unit U1 (`Fixture.tagStock.unitU1`) lewat Bulk Delete; sesi Add Stock tanpa unit Waiting for Approval; sesi Audit tanpa Not Found; sesi Audit yang seluruh barisnya dilewati `T-08`. Dipakai sebagai precondition TC.
- Identifier tetap unit U1 (Data Uji Dinamis #5) tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE (S-12).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-936: Popup Detail sesi Audit: section `TAGs Found` dan `TAGs Not Found` dengan Status After

4. Klik tab `Audit TAG`
5. Klik (⋯) pada baris sesi Audit dengan Found `5` dan Not Found `3` (Mark as Damaged/Missing dicentang)
6. Klik `Detail`
7. Verifikasi section `TAGs Found` (5 unit) tampil lalu section `TAGs Not Found` (3 unit)
8. Verifikasi tiap section memuat kolom `TAG Code`, `Identifier`, `Status After`
9. Verifikasi `Status After` unit Not Found adalah `Damaged/Missing`
10. Verifikasi `Status After` unit Found yang pulih adalah `Available`
11. Tutup Popup Detail dengan klik (X)

### TC-AC-ACTS-937: Popup Detail adalah snapshot: unit yang sudah dihapus tetap tampil di section `Deleted`

12. Klik tab `Add Stock`
13. Klik (⋯) pada baris sesi Delete Stock yang menghapus unit U1 lewat Bulk Delete
14. Klik `Detail`
15. Verifikasi unit U1 tampil di section `Deleted` dengan TAG Code, Identifier, dan Status Sebelum Dihapus saat dihapus
16. Tutup Popup Detail dengan klik (X)
17. Tutup modal Event Log dengan klik (X)
18. Verifikasi sedikitnya satu baris unit lain tampil pada Tab Available
19. Ketik Search `Fixture.tagStock.unitU1`, tekan Enter
20. Verifikasi unit U1 tidak ada di Tab Available (empty state `No results found`)
21. Klik `(←)` pada kotak Search
22. Klik icon `[Event Log]` di toolbar Tab Available
23. Klik (⋯) pada baris sesi Delete Stock yang menghapus unit U1
24. Klik `Detail`
25. Verifikasi unit U1 tetap tampil di section `Deleted` dengan TAG Code, Identifier, dan Status Sebelum Dihapus saat dihapus
26. Verifikasi isi popup tidak berubah dibanding pembukaan pertama (langkah 15) dan tidak mengikuti data unit saat ini
27. Tutup Popup Detail dengan klik (X)

### TC-AC-ACTS-938: Popup Detail menyembunyikan section tanpa baris beserta judulnya

28. Klik tab `Add Stock`
29. Klik (⋯) pada baris sesi Add Stock tanpa unit Waiting for Approval
30. Klik `Detail`
31. Verifikasi Popup Detail menampilkan section `Added`
32. Verifikasi judul section `Waiting for Approval` tidak tampil
33. Tutup Popup Detail dengan klik (X)
34. Klik tab `Audit TAG`
35. Klik (⋯) pada baris sesi Audit tanpa Not Found
36. Klik `Detail`
37. Verifikasi Popup Detail menampilkan section `TAGs Found`
38. Verifikasi judul section `TAGs Not Found` tidak tampil
39. Tutup Popup Detail dengan klik (X)

### TC-AC-ACTS-939: Popup Detail tanpa section berisi menampilkan empty state `S-28`

40. Klik (⋯) pada baris sesi Audit yang seluruh barisnya dilewati `T-08`
41. Klik `Detail`
42. Verifikasi Popup Detail menampilkan ilustrasi dengan judul `No details to show` dan deskripsi `There are no TAGs recorded for this session.`
43. Verifikasi tidak ada section atau tabel di Popup Detail
44. Tutup Popup Detail dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 44 langkah dihitung dengan ekspansi; semua blok membaca Popup Detail dari sesi seed pada modal Event Log yang sama dan berdiri sendiri; jumlah langkah berasal dari `Verifikasi` per klausa Expected (S-01), dan TC-AC-ACTS-937 membutuhkan urutan buka, hapus pantau, dan buka lagi (S-04).
- TC-AC-ACTS-937: langkah mencari U1 di Tab Available memakai Search sebagai langkah penghubung (R-16).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-939 menyebut sesi Audit yang seluruh barisnya dilewati `T-08` hanya sebagai contoh ("mis."); spec memakai sesi itu sebagai data seed.
  - Identifier tetap Data Uji Dinamis #5 dipakai ulang lintas TC dan tidak dapat bersuffix per run; hitungan valid hanya bila tidak ada spec lain yang mengubah dataset.
