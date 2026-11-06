---
id: TC-FA-TAG-E2E-210-t-tag-02-format-sel-link-badge-hover-dan-pemotongan-bagian-1
title: "Tabel T-TAG-02: Format Sel Name, TAG Code, dan Aset Not Paired Yet (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-830
  - TC-FA-TAG-831
  - TC-FA-TAG-832
  - TC-FA-TAG-833
  - TC-FA-TAG-834
  - TC-FA-TAG-835
  - TC-FA-TAG-836
coverage:
  web: automated
---

# Tabel T-TAG-02: Format Sel Name, TAG Code, dan Aset Not Paired Yet (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-833: Aset A (satu Tag QR-00231) dan aset B (QR-00231 dan RF-00500).
- Data TC-FA-TAG-835: Excavator 20 Ton / Plant A: dua aset Not Paired Yet.
- Data TC-FA-TAG-836: Brand: Caterpillar.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-830: Format Name pada T-TAG-02 berupa Asset Name - Increment

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Verifikasi Kolom Name menampilkan `Excavator 20 Ton - 11`, `Excavator 20 Ton - 43`, `Excavator 20 Ton - 44` (format `[Asset Name] - [Increment]`)

### TC-FA-TAG-831: Kolom TAG Code menumpuk Tag per baris sel dengan ikon tipe dan ikon peringatan Non-standard

4. Verifikasi AST-0011: `[RFID] RF-00101` tanpa ikon peringatan
5. Verifikasi AST-0044: dua baris sel `[QR] QR-00232` dengan ikon peringatan kecil (severity warning) lalu `[RFID] RF-00132`, urut A-Z menurut TAG Code, tanpa `+N more`

### TC-FA-TAG-832: Tooltip ikon tipe dan ikon peringatan pada kolom TAG Code

6. Arahkan pointer ke ikon QR pada AST-0044
7. Verifikasi Tooltip `QR` pada ikon tipe
8. Arahkan pointer ke ikon peringatan di samping QR-00232
9. Verifikasi Tooltip `This TAG type is not required by the asset name.`

### TC-FA-TAG-833: Sort TAG Code memakai TAG Code pertama pada sel dengan awalan lebih pendek lebih dulu

10. Klik header kolom TAG Code sekali
11. Verifikasi Menaik: aset A (urutan Tag lebih pendek, awalan) tampil sebelum aset B
12. Klik header kolom TAG Code dua kali lagi hingga indikator sort netral

### TC-FA-TAG-834: Klik TAG Code pada T-TAG-02 membuka Popup TAG Log

13. Klik `RF-00101` pada AST-0011
14. Verifikasi Popup TAG Log terbuka untuk RF-00101
15. Tutup Popup TAG Log

### TC-FA-TAG-835: Aset Not Paired Yet tampil dengan TAG Code strip dan Status Not Paired Yet

16. Tutup Popup Detail
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant A
18. Verifikasi Sel TAG Code `—`
19. Verifikasi Badge Status `Not Paired Yet`
20. Verifikasi Row action `Pair TAG`

### TC-FA-TAG-836: Kolom Brand berupa badge Dark dengan hover nama penuh

21. Tutup Popup Detail
22. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
23. Ubah page size menjadi 25
24. Arahkan pointer ke badge Brand pada AST-0011
25. Verifikasi Badge Brand berseverity Dark
26. Verifikasi Hover menampilkan nama Brand penuh

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 12, 15, 16, 21.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- TC-FA-TAG-835 memakai popup grup Plant A; popup Plant B ditutup dan dibuka kembali untuk TC-FA-TAG-836 (langkah penghubung).
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-833 menyebut aset A dengan Tag QR-00231 dan aset B dengan QR-00231 serta RF-00500, tetapi kode QR-00231 sudah menjadi Tag AST-0043 dan satu kode Tag hanya dapat dipegang satu aset; TC juga tidak menyebut Asset ID aset A dan B. Spec mengikuti TC dan menandai data aset A dan B sebagai disediakan fixture BE.
  - TC-FA-TAG-833 tidak menyebut apakah aset A dan B berada pada grup Excavator 20 Ton / Plant B; spec mengasumsikan keduanya di popup Plant B.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
