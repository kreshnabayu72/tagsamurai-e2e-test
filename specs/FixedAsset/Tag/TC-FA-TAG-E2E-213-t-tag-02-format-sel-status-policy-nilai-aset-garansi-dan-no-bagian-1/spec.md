---
id: TC-FA-TAG-E2E-213-t-tag-02-format-sel-status-policy-nilai-aset-garansi-dan-no-bagian-1
title: "Tabel T-TAG-02: Format Sel Status, Transactional Policy, Last Scanned, dan Asset Value (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-849
  - TC-FA-TAG-850
  - TC-FA-TAG-851
  - TC-FA-TAG-852
  - TC-FA-TAG-853
  - TC-FA-TAG-854
coverage:
  web: automated
---

# Tabel T-TAG-02: Format Sel Status, Transactional Policy, Last Scanned, dan Asset Value (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-849: Aset 'Excavator 20 Ton - 90' (AST-0090, Group Plant A) berlifecycle Waiting for Approval dan aset 'Excavator 20 Ton - 91' (AST-0091, Group Plant A) berlifecycle Draft, keduanya tanpa Tag Paired.
- Data TC-FA-TAG-850: Policy On: Borrow dan Transfer.
- Data TC-FA-TAG-851: Asset Name dengan seluruh policy Off.
- Aset AST-0090 (Excavator 20 Ton - 90, lifecycle Waiting for Approval) dan AST-0091 (Excavator 20 Ton - 91, lifecycle Draft) di Group Plant A tanpa Tag Paired, plus Asset Name milik spec `Policy Off {runId}-213` dengan seluruh policy transaksi Off, disediakan fixture BE; Asset Name milik spec dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 8, 20, 23, 26), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-849: Aset berlifecycle Draft atau Waiting for Approval tidak muncul di menu TAG dan tidak terhitung

1. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Verifikasi Blok info menampilkan Total Assets 20 dan Not Paired Yet 2; angka tidak bertambah oleh AST-0090 dan AST-0091
4. Verifikasi Tabel hanya memuat dua aset Not Paired Yet dari Pre-setup; AST-0090 dan AST-0091 tidak tampil
5. Verifikasi Tidak ada badge Status `Draft` atau `Waiting for Approval` pada tabel
6. Tutup Popup Detail

### TC-FA-TAG-850: Kolom Transactional Policy menampilkan ikon transaksi On dengan urutan tetap dan hover nama transaksi

7. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
8. Tampilkan kolom `Transactional Policy` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
9. Arahkan pointer ke ikon pertama
10. Verifikasi Ikon tampil berurutan Borrow lalu Transfer (urutan tetap Borrow, Self Service Borrow, Assign, Transfer)
11. Verifikasi Hover menampilkan nama transaksi pada ikon

### TC-FA-TAG-851: Kolom Transactional Policy dengan seluruh policy Off menampilkan strip

12. Tutup Popup Detail
13. Ketik Search `Policy Off {runId}-213`, tekan Enter
14. Buka Popup Detail Asset Name milik spec yang seluruh policy transaksinya Off
15. Verifikasi Sel menampilkan `—`
16. Tutup Popup Detail
17. Klik `(←)` pada kotak Search

### TC-FA-TAG-852: Kolom Last Scanned mengikuti format General Settings dan strip bila belum pernah dipindai

18. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
19. Ubah page size menjadi 25
20. Tampilkan kolom `Last Scanned` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
21. Verifikasi AST-0011 menampilkan tanggal sesuai format General Settings
22. Verifikasi AST-0020 menampilkan `—`

### TC-FA-TAG-853: Kolom Asset Value menampilkan currency dua desimal rata kanan dan Pending bila Purchase Cost belum ada

23. Tampilkan kolom `Asset Value (Commercial)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
24. Verifikasi AST-0043: currency dua desimal rata kanan (800.00)
25. Verifikasi AST-0020 (berhak, Purchase Cost belum ada): `Pending` (bukan `—`)
26. Arahkan pointer ke sel `Pending` AST-0020
27. Verifikasi Tooltip `Purchase cost has not been set.`

### TC-FA-TAG-854: Asset Value berupa dua kolom tetap Commercial lalu Fiscal

28. Tampilkan kolom `Asset Value (Fiscal)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
29. Verifikasi Dua kolom `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` tampil berurutan pada posisi kolom ini
30. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 6, 12, 13, 16, 17, 30.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Langkah Search `Policy Off {runId}-213` menemukan baris grup target (langkah penghubung); Search ditutup sesudahnya.
- TC-FA-TAG-854 menampilkan kedua kolom Asset Value; kolom Asset Value (Commercial) sudah tampil dari TC-FA-TAG-853 dalam spec ini, sehingga langkah Setup Column hanya mencentang Asset Value (Fiscal).
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 8, 20, 23, 26), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-851 tidak menyebut nama Asset Name yang seluruh policy transaksinya Off; spec memakai Asset Name milik spec bersuffix.
  - Kolom Transactional Policy pada TC-FA-TAG-851 sudah tampil dari TC-FA-TAG-850 dalam spec ini; langkah "Tampilkan kolom Transactional Policy" TC tidak diulang karena akan menyembunyikannya kembali.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
