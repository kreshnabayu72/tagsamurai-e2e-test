---
id: TC-FA-TAG-E2E-215-t-tag-02-format-sel-status-policy-nilai-aset-garansi-dan-no-bagian-3
title: "Tabel T-TAG-02: Warranty Expiry, Last Updated, Name Panjang, dan Scroll Horizontal (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-860
  - TC-FA-TAG-861
  - TC-FA-TAG-862
  - TC-FA-TAG-863
  - TC-FA-TAG-864
coverage:
  web: automated
---

# Tabel T-TAG-02: Warranty Expiry, Last Updated, Name Panjang, dan Scroll Horizontal (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read) (Read: Plant B tanpa akses Manage purchase) | MR_PB_NOPUR | `manageAssetTagReadReadPlantBTanpaAksesManagePurchase_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PB_NOPUR_PASSWORD` |
| 2 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-863: Asset Name: Excavator Hydraulic Heavy Duty 20 Ton Crawler Type Komatsu PC200 Long Boom Series (81 karakter); Increment: 1; Asset ID: AST-0200.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 3, 12, 22), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-860: Warranty Expiry di luar hak menampilkan No access dengan tooltip

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Tampilkan kolom `Warranty Expiry` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
4. Arahkan pointer ke sel `No access`
5. Verifikasi Sel menampilkan `No access`
6. Verifikasi Tooltip `Requires Manage purchase access in this group.`
7. Tutup Popup Detail
8. Hapus preferensi kolom di browser
9. Ganti akun: logout dari akun Manage asset & TAG (Read) (Read: Plant B tanpa akses Manage purchase) [MR_PB_NOPUR], login dengan akun Total Control [TC], lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-861: Warranty Expiry berhak tetapi belum diisi menampilkan strip

10. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
11. Ubah page size menjadi 25
12. Tampilkan kolom `Warranty Expiry` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
13. Verifikasi Sel Warranty Expiry AST-0020 menampilkan `—`

### TC-FA-TAG-862: Kolom Last Updated mengikuti format General Settings

14. Verifikasi Tanggal dan waktu tampil sesuai format General Settings, tidak pernah kosong

### TC-FA-TAG-863: Name dan Asset ID tidak pernah dipotong walau panjang

15. Tutup Popup Detail
16. Klik Asset Name 'Excavator Hydraulic Heavy Duty 20 Ton Crawler Type Komatsu PC200 Long Boom Series' pada baris grup Plant B untuk membuka Popup Detail
17. Verifikasi teks pada sel Name baris 'Excavator Hydraulic Heavy Duty 20 Ton Crawler Type Komatsu PC200 Long Boom Series - 1' (AST-0200) tampil utuh tanpa `..`
18. Verifikasi kolom melebar mengikuti konten

### TC-FA-TAG-864: Popup Detail dapat di-scroll horizontal bila kolom banyak

19. Tutup Popup Detail
20. Hapus preferensi kolom di browser
21. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
22. Tampilkan seluruh kolom curated lewat Setup Column (header `⋯`, `Setup Column...`, centang semua kolom curated, `[Save]`)
23. Geser tabel secara horizontal
24. Verifikasi Tabel T-TAG-02 menampilkan scroll horizontal dan kolom Name dan kolom terakhir yang tercentang dapat dijangkau
25. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 7, 8, 9, 15, 19, 20, 22, 25.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Urutan TC diatur menurut akun: akun Manage asset & TAG (Read) (Read: Plant B tanpa akses Manage purchase) lebih dulu, lalu Total Control.
- Preferensi kolom dihapus di browser sebelum ganti akun dan sebelum TC-FA-TAG-864 supaya langkah menampilkan kolom bersifat deterministik.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 3, 12, 22), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-864 mensyaratkan seluruh kolom curated ditampilkan tetapi Langkah Uji tidak memuat langkahnya; spec menambah langkah penghubung Setup Column.
  - TC-FA-TAG-863 menyebut Asset Name 81 karakter dengan increment 1 pada baris Plant B; Asset Name itu tidak termasuk dataset dasar TC dan disediakan fixture BE.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
