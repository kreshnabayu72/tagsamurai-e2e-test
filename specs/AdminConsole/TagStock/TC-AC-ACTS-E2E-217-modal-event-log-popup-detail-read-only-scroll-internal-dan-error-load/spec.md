---
id: TC-AC-ACTS-E2E-217-modal-event-log-popup-detail-read-only-scroll-internal-dan-error-load
title: "Modal Event Log: Popup Detail Read-Only dengan Scroll Internal dan Error Load Popup Detail"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-940
  - TC-AC-ACTS-941
coverage:
  web: automated
---

# Modal Event Log: Popup Detail Read-Only dengan Scroll Internal dan Error Load Popup Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed (kemampuan fixture BE): sesi Add Stock dengan 30 unit OK; sedikitnya satu sesi Add Stock lain untuk TC-AC-ACTS-941.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Intercept respons 5xx dan penahanan respons (delay) di atas backend nyata lewat `Spectra.intercept()`; intercept dilepas segera setelah dipakai dan hook `after` memastikan tidak ada intercept tersisa.
- State global: tidak ada yang diubah selain intercept respons yang dilepas segera setelah dipakai.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-940: Popup Detail read-only: tanpa sort, paginasi, Setup Column, dan Filter; scroll internal dengan header tetap

4. Klik (⋯) pada baris sesi Add Stock dengan 30 unit OK
5. Klik `Detail`
6. Verifikasi header kolom Popup Detail tanpa ikon sort dan tanpa Column Visibility
7. Verifikasi Popup Detail tidak memiliki Search, Filter, Download, maupun paginasi
8. Scroll isi Popup Detail ke bawah
9. Verifikasi isi Popup Detail di-scroll internal dengan header tabel tetap tampil
10. Verifikasi urutan awal TAG Code A–Z
11. Klik (X) pada Popup Detail
12. Verifikasi Popup Detail tertutup dan tampilan kembali ke modal Event Log

### TC-AC-ACTS-941: Error load Popup Detail Event Log: fetch gagal bukan empty state

13. Gagalkan request rincian sesi dengan intercept respons 5xx
14. Klik (⋯) pada satu baris sesi
15. Klik `Detail`
16. Verifikasi body popup menampilkan `Unable to load this data.` dan `[Try Again]`
17. Verifikasi header dan tombol close Popup Detail tetap tampil
18. Verifikasi tampilan bukan empty state `S-28`
19. Lepas intercept respons 5xx
20. Tutup Popup Detail dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-941 tidak menyatakan perilaku `[Try Again]` pada Popup Detail; spec tidak mengasersinya.
