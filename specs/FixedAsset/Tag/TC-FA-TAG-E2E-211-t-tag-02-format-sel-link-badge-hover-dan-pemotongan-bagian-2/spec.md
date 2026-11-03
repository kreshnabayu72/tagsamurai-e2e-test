---
id: TC-FA-TAG-E2E-211-t-tag-02-format-sel-link-badge-hover-dan-pemotongan-bagian-2
title: "Tabel T-TAG-02: Format Sel Badge Brand, Model/Type, dan Group (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-837
  - TC-FA-TAG-838
  - TC-FA-TAG-839
  - TC-FA-TAG-840
  - TC-FA-TAG-841
  - TC-FA-TAG-842
coverage:
  web: automated
---

# Tabel T-TAG-02: Format Sel Badge Brand, Model/Type, dan Group (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-839: Model/Type: 320D.
- Aset acuan dengan Brand `Heavy Duty Hydraulic Excavator Series` (lebih dari 25 karakter), aset tanpa Brand, aset dengan Model/Type `Heavy Duty Hydraulic Excavator Series`, dan aset tanpa Model/Type disediakan fixture BE pada grup Excavator 20 Ton / Plant B; Group Plant B berada di bawah Head Office.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-837: Badge Brand lebih dari 25 karakter dipotong 12 huruf pertama titik dua 12 huruf terakhir

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Verifikasi Badge menampilkan `Heavy Duty H..vator Series`
4. Arahkan pointer ke badge Brand
5. Verifikasi Hover menampilkan nama penuh

### TC-FA-TAG-838: Kolom Brand kosong menampilkan strip

6. Verifikasi Sel menampilkan `—`

### TC-FA-TAG-839: Kolom Model/Type berupa badge Dark dengan hover nama penuh

7. Arahkan pointer ke badge Model/Type pada AST-0011
8. Verifikasi Badge Model/Type berseverity Dark
9. Verifikasi Hover menampilkan nama Model/Type penuh

### TC-FA-TAG-840: Badge Model/Type lebih dari 25 karakter dipotong 12 huruf pertama titik dua 12 huruf terakhir

10. Verifikasi Badge menampilkan `Heavy Duty H..vator Series`
11. Arahkan pointer ke badge Model/Type
12. Verifikasi Hover menampilkan nama penuh

### TC-FA-TAG-841: Kolom Model/Type kosong menampilkan strip

13. Verifikasi Sel menampilkan `—`

### TC-FA-TAG-842: Kolom Group pada T-TAG-02 berupa badge Primary dengan hover hierarki lengkap

14. Arahkan pointer ke badge Group
15. Verifikasi Badge berseverity primary
16. Verifikasi Hover `Head Office > Plant B`
17. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 17.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Data dasar TC menyebut 15 aset lain memakai Brand Volvo dan Model EC210, sehingga aset tanpa Brand atau tanpa Model/Type (TC-FA-TAG-838, 841) dan aset ber-Brand lebih dari 25 karakter (TC-FA-TAG-837, 840) harus disediakan terpisah; TC tidak menyebut Asset ID aset itu.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
