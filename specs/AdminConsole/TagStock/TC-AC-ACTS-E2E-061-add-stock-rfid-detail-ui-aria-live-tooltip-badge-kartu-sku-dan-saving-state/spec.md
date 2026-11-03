---
id: TC-AC-ACTS-E2E-061-add-stock-rfid-detail-ui-aria-live-tooltip-badge-kartu-sku-dan-saving-state
title: "Add Stock RFID: Detail UI (Widget aria-live, Badge OK Tanpa Tooltip, Kartu SKU Terpotong, dan Saving State Submit)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-177
  - TC-AC-ACTS-179
  - TC-AC-ACTS-180
  - TC-AC-ACTS-857
coverage:
  web: automated
---

# Add Stock RFID: Detail UI (Widget aria-live, Badge OK Tanpa Tooltip, Kartu SKU Terpotong, dan Saving State Submit)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |

- SKU RFID uji untuk TC-AC-ACTS-857: Device Name `RFID Asset Tag`, Brand `Jakarta Selatan Distribution Center` (35 karakter), Model/Type `Handheld Reader Pro Model` (25 karakter); tidak ada di Tabel Data Uji Pre-setup, disediakan fixture BE (`Fixture.tagStock.skuBrandPanjang`).
- Kemampuan teknis tambahan: `Spectra.intercept()` untuk menahan respons request Submit (TC-AC-ACTS-177); tahanan dilepas pada langkah asersi dan di hook `after` bila spec gagal di tengah. Menahan respons hanya untuk mengamati state loading dan bukan fault injection. Atribut `aria-live` dibaca dari DOM (TC-AC-ACTS-179).
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-179: Floating widget aria-live

3. Klik `[Add by Scan]`
4. Verifikasi status widget memiliki `aria-live="polite"`
5. Verifikasi counter widget memiliki `aria-live="polite"`

### TC-AC-ACTS-180: Badge OK tanpa tooltip

6. Scan TAG A
7. Klik `[Stop]`
8. Hover badge OK
9. Verifikasi tidak ada tooltip pada badge OK

### TC-AC-ACTS-177: Saving state tombol Submit

10. Hover `[Submit]`
11. Verifikasi `[Submit]` menampilkan state hover
12. Tahan respons request Submit dengan intercept
13. Klik `[Submit]`
14. Verifikasi `[Submit]` berstatus loading dan disabled
15. Verifikasi `[Cancel]` ikut disabled
16. Lepas tahanan respons
17. Tunggu aksi selesai

### TC-AC-ACTS-857: Kartu SKU dengan Brand dan Model/Type panjang

18. Buka TAG > Stock lewat sidebar
19. Ketik Search SKU RFID uji Brand panjang (`Fixture.tagStock.skuBrandPanjang`), tekan Enter
20. Klik (⋯) baris SKU itu, klik `Add Stock`
21. Verifikasi badge `Brand:` menampilkan 12 huruf pertama + `..` + 12 huruf terakhir
22. Verifikasi badge `Model/Type:` menampilkan nama penuh tanpa `..`
23. Hover badge `Brand:`
24. Verifikasi hover badge `Brand:` menampilkan nama penuh `Jakarta Selatan Distribution Center`
25. Verifikasi label `TAG Type:` tampil persis seperti ditulis
26. Verifikasi label `Brand:` tampil persis seperti ditulis
27. Verifikasi label `Model/Type:` tampil persis seperti ditulis

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), `[Stop]`, dan melepas tahanan respons. Tahanan respons Submit hanya untuk mengamati state loading dan bukan fault injection; tahanan dilepas pada langkah asersi dan di hook `after` bila spec gagal di tengah.
- Setelah `[Submit]` TC-AC-ACTS-177 sukses, halaman berpindah ke Detail SKU; langkah berikutnya membuka SKU berbeda lewat sidebar sehingga tidak bergantung pada halaman Add Stock RFID-ASSET-CORE-R5.
- Temuan untuk QA:
  - TC-AC-ACTS-177 tidak menyebut hasil Submit (sukses setelah tahanan dilepas); spec hanya melepas tahanan dan menunggu aksi selesai.
  - TC-AC-ACTS-857 memakai SKU RFID dengan Brand 35 karakter dan Model 25 karakter yang tidak ada di Tabel Data Uji Pre-setup; disediakan fixture BE (`Fixture.tagStock.skuBrandPanjang`) milik spec. TC-AC-ACTS-857 tidak menyebut apakah `Add Stock` dibuka dari Stock List atau Detail.
  - TC-AC-ACTS-179 memeriksa atribut `aria-live` (kelas d teknologi bantu); atribut dibaca dari DOM.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
