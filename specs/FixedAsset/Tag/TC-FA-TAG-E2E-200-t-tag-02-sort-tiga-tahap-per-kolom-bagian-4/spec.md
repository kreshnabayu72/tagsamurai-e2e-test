---
id: TC-FA-TAG-E2E-200-t-tag-02-sort-tiga-tahap-per-kolom-bagian-4
title: "Tabel T-TAG-02: Sort Tiga Tahap per Kolom dan Nilai Sama (Bagian 4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-790
  - TC-FA-TAG-791
  - TC-FA-TAG-792
  - TC-FA-TAG-793
coverage:
  web: automated
---

# Tabel T-TAG-02: Sort Tiga Tahap per Kolom dan Nilai Sama (Bagian 4)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-790: Warranty Expiry: AST-0011 = 01 Mar 27; AST-0020 = —; AST-0021 = 31 Dec 26; AST-0043 = 01 Sep 26; AST-0044 = —.
- Data TC-FA-TAG-791: Last Updated: AST-0011 = 01 Oct 26; AST-0020 = 05 Oct 26; AST-0021 = 10 Oct 26; AST-0043 = 15 Oct 26; AST-0044 = 20 Oct 26.
- Data TC-FA-TAG-792: Group seluruh aset = Plant B.
- Data TC-FA-TAG-793: Measurement seluruh aset = pcs.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-790: Sort tiga tahap kolom Warranty Expiry pada T-TAG-02

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Tampilkan kolom `Warranty Expiry` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
4. Klik header kolom Warranty Expiry sekali
5. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0043, AST-0021, AST-0011, AST-0044, AST-0020; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
6. Klik header kolom Warranty Expiry sekali lagi
7. Verifikasi setelah klik 2 (menurun): AST-0044, AST-0020, AST-0011, AST-0021, AST-0043
8. Klik header kolom Warranty Expiry sekali lagi
9. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-791: Sort tiga tahap kolom Last Updated pada T-TAG-02

10. Klik header kolom Last Updated sekali
11. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0011, AST-0020, AST-0021, AST-0043, AST-0044; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
12. Klik header kolom Last Updated sekali lagi
13. Verifikasi setelah klik 2 (menurun): AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
14. Klik header kolom Last Updated sekali lagi
15. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-792: Sort kolom Group pada T-TAG-02 dengan nilai sama di seluruh baris

16. Klik header kolom Group sekali
17. Verifikasi setelah klik 1: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
18. Klik header kolom Group sekali lagi
19. Verifikasi setelah klik 2: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
20. Klik header kolom Group sekali lagi hingga indikator sort netral

### TC-FA-TAG-793: Sort kolom Measurement pada T-TAG-02 dengan nilai sama di seluruh baris

21. Tampilkan kolom `Measurement` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
22. Klik header kolom Measurement sekali
23. Verifikasi setelah klik 1: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
24. Klik header kolom Measurement sekali lagi
25. Verifikasi setelah klik 2: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
26. Klik header kolom Measurement sekali lagi hingga indikator sort netral
27. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 20, 26, 27.
- Popup Detail dibuka sekali dan page size 25 diatur sekali pada TC pertama.
- TC-FA-TAG-792 dan 793 hanya menekan header dua kali; langkah penghubung mengembalikan sort ke netral sebelum TC berikutnya.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-792 dan 793 tidak menyebut klik ketiga; Expected hanya membahas klik 1 dan klik 2, sehingga tiap klik diasersi sesuai Expected "Setelah klik 1 dan klik 2".
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
