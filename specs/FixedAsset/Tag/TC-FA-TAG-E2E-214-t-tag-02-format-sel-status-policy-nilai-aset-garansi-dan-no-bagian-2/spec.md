---
id: TC-FA-TAG-E2E-214-t-tag-02-format-sel-status-policy-nilai-aset-garansi-dan-no-bagian-2
title: "Tabel T-TAG-02: Nilai Aset, Garansi, dan Sel No access per Role (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-855
  - TC-FA-TAG-859
  - TC-FA-TAG-856
  - TC-FA-TAG-858
  - TC-FA-TAG-857
coverage:
  web: automated
---

# Tabel T-TAG-02: Nilai Aset, Garansi, dan Sel No access per Role (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG (Read) (Read: Plant B tanpa akses View asset value) | MR_PB_NOVAL | `manageAssetTagReadReadPlantBTanpaAksesViewAssetValue_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PB_NOVAL_PASSWORD` |
| 3 | Manage asset & TAG (Read) (Read: Plant B; View asset value hanya pada sebagian aset) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-855: AST-0043 memiliki metode dan masa manfaat penyusutan.
- Data TC-FA-TAG-859: AST-0043 01 Sep 26 (lewat); AST-0021 31 Dec 26 (segera habis).
- Data TC-FA-TAG-858: AST-0043 Asset Value (Commercial) 800.00 tetapi `No access` bagi role ini.
- Data TC-FA-TAG-857: Sebagian aset berhak (nilai terisi) dan sebagian `No access`; aset berhak tanpa Purchase Cost (bila ada) menampilkan `Pending`.
- Role pada blok 3 (MR) memiliki Read Plant B dan View asset value hanya pada sebagian aset grup Excavator 20 Ton / Plant B; email akun Pre-setup bernama dasar sama (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 3, 6, 16, 28), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-855: Tooltip sel Asset Value menampilkan metode dan masa manfaat

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Tampilkan kolom `Asset Value (Commercial)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
4. Arahkan pointer ke sel AST-0043
5. Verifikasi Tooltip menampilkan metode dan masa manfaat sesuai catatan kolom

### TC-FA-TAG-859: Kolom Warranty Expiry: tanggal lewat dan segera habis memiliki tooltip masa garansi

6. Tampilkan kolom `Warranty Expiry` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
7. Arahkan pointer ke tanggal AST-0043 (sudah lewat)
8. Verifikasi Tanggal AST-0043 berwarna menurut masa garansi dengan tooltip `Warranty expired`
9. Arahkan pointer ke tanggal AST-0021 (segera habis)
10. Verifikasi Tanggal AST-0021 dengan tooltip `Warranty expires soon`
11. Tutup Popup Detail
12. Hapus preferensi kolom di browser
13. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG (Read) (Read: Plant B tanpa akses View asset value) [MR_PB_NOVAL], lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-856: Sel Asset Value di luar hak menampilkan No access dengan tooltip

14. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
15. Ubah page size menjadi 25
16. Tampilkan kolom `Asset Value (Commercial)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
17. Arahkan pointer ke sel `No access`
18. Verifikasi Seluruh sel menampilkan `No access`
19. Verifikasi Tooltip `Requires View asset value access in this group.`

### TC-FA-TAG-858: Search tidak mencocokkan sel Asset Value No access

20. Tutup Popup Detail
21. Ketik Search `800.00`, tekan Enter
22. Verifikasi `No results found`: sel `No access` tidak cocok
23. Klik `(←)` pada kotak Search
24. Hapus preferensi kolom di browser
25. Ganti akun: logout dari akun Manage asset & TAG (Read) (Read: Plant B tanpa akses View asset value) [MR_PB_NOVAL], login dengan akun Manage asset & TAG (Read) (Read: Plant B; View asset value hanya pada sebagian aset) [MR], lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-857: Sort Asset Value menempatkan sel No access selalu paling akhir

26. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
27. Ubah page size menjadi 25
28. Tampilkan kolom `Asset Value (Commercial)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
29. Klik header kolom Asset Value (Commercial) sekali
30. Verifikasi Menaik: sel `No access` di akhir; bila ada sel `Pending` (aset berhak tanpa Purchase Cost), sel itu tepat sebelum sel `No access`
31. Klik header kolom Asset Value (Commercial) sekali lagi
32. Verifikasi Menurun: sel `No access` tetap di akhir; sel `Pending` tetap tepat sebelumnya
33. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 11, 12, 13, 20, 23, 24, 25, 33.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Urutan TC diatur menurut akun agar ganti akun hanya dua kali: akun Total Control (TC-FA-TAG-855, 859), akun MR_PB_NOVAL (TC-FA-TAG-856, 858), lalu akun MR (TC-FA-TAG-857).
- Preferensi kolom dihapus di browser sebelum tiap ganti akun supaya langkah "Tampilkan kolom" akun berikutnya tidak menyembunyikan kolom yang tersimpan.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 3, 6, 16, 28), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - Role TC-FA-TAG-857 ("Read: Plant B; View asset value hanya pada sebagian aset") tidak punya baris Pre-setup sendiri; spec memakai akun Manage asset & TAG (Read) [MR] dan menandai pembagian View asset value per aset sebagai kebutuhan fixture BE.
  - TC-FA-TAG-857 tidak mengatur page size; spec memakai page size 25 agar seluruh 20 aset terlihat dan posisi "di akhir" dapat diamati.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
