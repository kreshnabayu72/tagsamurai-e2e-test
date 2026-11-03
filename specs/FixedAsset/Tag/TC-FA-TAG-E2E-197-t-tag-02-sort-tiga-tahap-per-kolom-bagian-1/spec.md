---
id: TC-FA-TAG-E2E-197-t-tag-02-sort-tiga-tahap-per-kolom-bagian-1
title: "Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-780
  - TC-FA-TAG-781
  - TC-FA-TAG-782
  - TC-FA-TAG-783
coverage:
  web: automated
---

# Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-780: Name: Excavator 20 Ton - 11, Excavator 20 Ton - 20, Excavator 20 Ton - 21, Excavator 20 Ton - 43, Excavator 20 Ton - 44.
- Data TC-FA-TAG-781: Asset ID: AST-0011 = AST-0011; AST-0020 = AST-0020; AST-0021 = AST-0021; AST-0043 = AST-0043; AST-0044 = AST-0044.
- Data TC-FA-TAG-782: TAG Code: AST-0011 = RF-00101; AST-0020 = RF-00130; AST-0021 = RF-00140; AST-0043 = QR-00231; AST-0044 = QR-00232.
- Data TC-FA-TAG-783: Brand: AST-0011 = Caterpillar; AST-0020 = Komatsu; AST-0021 = Caterpillar; AST-0043 = Hitachi; AST-0044 = Komatsu.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-780: Sort tiga tahap kolom Name pada T-TAG-02 (increment numerik natural)

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Klik header kolom Name sekali
4. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: - 11, - 20, - 21, - 43, - 44 (increment numerik natural, bukan alfabet teks)
5. Klik header kolom Name sekali lagi
6. Verifikasi setelah klik 2 (menurun): - 44, - 43, - 21, - 20, - 11
7. Klik header kolom Name sekali lagi
8. Verifikasi setelah klik 3: indikator netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-781: Sort tiga tahap kolom Asset ID pada T-TAG-02

9. Klik header kolom Asset ID sekali
10. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0011, AST-0020, AST-0021, AST-0043, AST-0044; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
11. Klik header kolom Asset ID sekali lagi
12. Verifikasi setelah klik 2 (menurun): AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
13. Klik header kolom Asset ID sekali lagi
14. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-782: Sort tiga tahap kolom TAG Code pada T-TAG-02

15. Klik header kolom TAG Code sekali
16. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0043, AST-0044, AST-0011, AST-0020, AST-0021; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
17. Klik header kolom TAG Code sekali lagi
18. Verifikasi setelah klik 2 (menurun): AST-0021, AST-0020, AST-0011, AST-0044, AST-0043
19. Klik header kolom TAG Code sekali lagi
20. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-783: Sort tiga tahap kolom Brand pada T-TAG-02

21. Klik header kolom Brand sekali
22. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0021, AST-0011, AST-0043, AST-0044, AST-0020; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
23. Klik header kolom Brand sekali lagi
24. Verifikasi setelah klik 2 (menurun): AST-0044, AST-0020, AST-0043, AST-0021, AST-0011
25. Klik header kolom Brand sekali lagi
26. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru
27. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 27.
- Popup Detail dibuka sekali dan page size 25 diatur sekali pada TC pertama; keduanya tidak diulang pada TC berikutnya karena klik ketiga tiap TC mengembalikan sort ke netral (halaman yang sama dipakai berulang).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
