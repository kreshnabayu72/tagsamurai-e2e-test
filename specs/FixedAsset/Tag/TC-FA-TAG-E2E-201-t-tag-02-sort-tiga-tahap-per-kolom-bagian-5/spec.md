---
id: TC-FA-TAG-E2E-201-t-tag-02-sort-tiga-tahap-per-kolom-bagian-5
title: "Tabel T-TAG-02: Sort Kolom dengan Nilai Sama dan Pindah Target Sort (Bagian 5)"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-794
  - TC-FA-TAG-795
  - TC-FA-TAG-796
coverage:
  web: automated
---

# Tabel T-TAG-02: Sort Kolom dengan Nilai Sama dan Pindah Target Sort (Bagian 5)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-794: Category seluruh aset = Heavy Equipment > Earthmoving.
- Data TC-FA-TAG-795: Transactional Policy seluruh aset = Borrow dan Transfer On.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 3, 9), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-794: Sort kolom Category pada T-TAG-02 dengan nilai sama di seluruh baris

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Tampilkan kolom `Category` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
4. Klik header kolom Category sekali
5. Verifikasi setelah klik 1: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
6. Klik header kolom Category sekali lagi
7. Verifikasi setelah klik 2: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
8. Klik header kolom Category sekali lagi hingga indikator sort netral

### TC-FA-TAG-795: Sort kolom Transactional Policy pada T-TAG-02 dengan nilai sama di seluruh baris

9. Tampilkan kolom `Transactional Policy` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
10. Klik header kolom Transactional Policy sekali
11. Verifikasi setelah klik 1: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
12. Klik header kolom Transactional Policy sekali lagi
13. Verifikasi setelah klik 2: urutan relatif lima aset acuan tetap mengikuti default sort karena nilai sama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
14. Klik header kolom Transactional Policy sekali lagi hingga indikator sort netral

### TC-FA-TAG-796: Pindah target sort pada T-TAG-02 mereset kolom sebelumnya

15. Klik header Brand sekali
16. Verifikasi Indikator Brand netral
17. Klik header Asset ID sekali
18. Verifikasi Asset ID menaik: AST-0011, AST-0020, AST-0021, AST-0043, AST-0044
19. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 8, 14, 19.
- Popup Detail dibuka sekali dan page size 25 diatur sekali pada TC pertama.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 3, 9), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
