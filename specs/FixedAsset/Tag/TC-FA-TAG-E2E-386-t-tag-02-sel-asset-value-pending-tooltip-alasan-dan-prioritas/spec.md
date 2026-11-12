---
id: TC-FA-TAG-E2E-386-t-tag-02-sel-asset-value-pending-tooltip-alasan-dan-prioritas
title: "Tabel T-TAG-02: Sel Asset Value Pending, Tooltip Alasan, dan Prioritas Alasan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1502
coverage:
  web: automated
---

# Tabel T-TAG-02: Sel Asset Value Pending, Tooltip Alasan, dan Prioritas Alasan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-1502: AST-0020 (Excavator 20 Ton - 20, Plant B) belum ada Purchase Cost; Pre-setup tambahan: Asset Name `Tanpa Class Item` tanpa Asset Class di Plant B dengan satu aset AST-0301 (Purchase Cost 100000, tag RFID Paired). Pre-setup tambahan disediakan fixture BE (kunci fixture usulan `tanpaClassItem`) dan dikembalikan ke keadaan awal di hook `after`.

## Test Steps

### TC-FA-TAG-1502: Sel Asset Value Pending pada tabel T-TAG-02: tooltip alasan Purchase cost belum diisi atau Asset class belum diisi, dan prioritas alasan

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Tampilkan kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kedua kolom, `[Save]`)
4. Arahkan pointer ke sel `Pending` AST-0020 pada kolom `Asset Value (Commercial)`
5. Verifikasi AST-0020 menampilkan teks `Pending` pada kedua kolom (bukan `—`, bukan currency nol, bukan `No access`)
6. Verifikasi Tooltip AST-0020 pada kolom `Asset Value (Commercial)`: `Purchase cost has not been set.`
7. Arahkan pointer ke sel `Pending` AST-0020 pada kolom `Asset Value (Fiscal)`
8. Verifikasi Tooltip AST-0020 pada kolom `Asset Value (Fiscal)`: `Purchase cost has not been set.`
9. Tutup Popup Detail
10. Klik Asset Name `Tanpa Class Item` pada baris Plant B
11. Tampilkan kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kedua kolom, `[Save]`)
12. Arahkan pointer ke sel `Pending` AST-0301 pada kolom `Asset Value (Commercial)`
13. Verifikasi AST-0301 menampilkan teks `Pending` pada kedua kolom (Purchase Cost sudah ada)
14. Verifikasi Tooltip AST-0301 pada kolom `Asset Value (Commercial)`: `Asset class has not been set.`
15. Arahkan pointer ke sel `Pending` AST-0301 pada kolom `Asset Value (Fiscal)`
16. Verifikasi Tooltip AST-0301 pada kolom `Asset Value (Fiscal)`: `Asset class has not been set.`
17. Verifikasi Tooltip sel `Pending` (AST-0020 dan AST-0301) pada kedua kolom tidak memuat metode atau masa manfaat
18. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 9, 18.
- Langkah TC 4 dan 7 (hover `Pending` "pada masing-masing kolom") dipecah per kolom: langkah 4, 7 dan 12, 15 agar tooltip tiap kolom diverifikasi.
- Langkah 11 mengikuti langkah TC 6 apa adanya ("Tampilkan kolom ... lewat Setup Column"); bila preferensi kolom dari langkah 3 masih tersimpan, kedua kolom sudah tercentang dan langkah ini cukup memastikan keduanya tampil (jangan mencentang ulang sehingga menyembunyikannya).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Fixture Asset Name `Tanpa Class Item` (tanpa Asset Class) dengan AST-0301 baru muncul pada TC-FA-TAG-1502; kunci fixture belum ada dan disediakan tim FE/BE.
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
