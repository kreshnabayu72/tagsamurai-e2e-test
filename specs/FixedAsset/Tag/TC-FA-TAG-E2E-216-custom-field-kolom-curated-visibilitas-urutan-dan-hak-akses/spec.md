---
id: TC-FA-TAG-E2E-216-custom-field-kolom-curated-visibilitas-urutan-dan-hak-akses
title: "Custom Field pada Tabel T-TAG-02: Kolom Curated, Visibilitas, Urutan, dan Hak Akses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-865
  - TC-FA-TAG-866
  - TC-FA-TAG-867
  - TC-FA-TAG-868
  - TC-FA-TAG-869
  - TC-FA-TAG-871
  - TC-FA-TAG-870
coverage:
  web: automated
---

# Custom Field pada Tabel T-TAG-02: Kolom Curated, Visibilitas, Urutan, dan Hak Akses

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG (Read) (Read: Plant B tanpa akses Manage purchase) | MR_PB_NOPUR | `manageAssetTagReadReadPlantBTanpaAksesManagePurchase_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PB_NOPUR_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-865: Custom Field Active: CF Text, CF Dropdown, CF Numeric, CF Date.
- Data TC-FA-TAG-866: Custom Field `CF Retired` berstatus Inactive.
- Data TC-FA-TAG-867: Custom Field baru `CF New` dibuat Active.
- Data TC-FA-TAG-868: Field General: CF Zeta, CF Alpha; Purchasing: CF Vendor; Accounting: CF Ledger.
- Data TC-FA-TAG-869: Custom Field `CF Laptop Only` hanya berlaku untuk Asset Name Laptop Pro 14.
- Data TC-FA-TAG-870: Custom Field Purchasing `CF Vendor`.
- Custom Field Active per tipe di-seed lewat fixture BE: CF Text, CF Dropdown, CF Numeric, CF Date; Custom Field Inactive `CF Retired`; Custom Field General `CF Zeta` dan `CF Alpha`, Purchasing `CF Vendor`, Accounting `CF Ledger`; `CF Laptop Only` hanya berlaku untuk Asset Name Laptop Pro 14; `CF New` dibuat Active di tengah spec. Seluruh Custom Field seeding dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 19, 22, 28), serta melakukan aksi lewat sesi API (langkah 11).

## Test Steps

### TC-FA-TAG-865: Kolom Custom Field Active tersedia sebagai kolom curated yang Hidden secara default

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik header `⋯` pada tabel T-TAG-02
3. Verifikasi Setiap Custom Field Active muncul sebagai kolom curated dengan checkbox tidak tercentang
4. Verifikasi Kolom tidak tampil di tabel sampai dicentang
5. Tutup overlay Column Visibility

### TC-FA-TAG-866: Custom Field Inactive tidak menjadi kolom

6. Klik header `⋯` pada tabel T-TAG-02
7. Verifikasi daftar kolom memuat Custom Field Active `CF Text`
8. Verifikasi Kolom `CF Retired` tidak ada pada daftar kolom
9. Tutup overlay Column Visibility

### TC-FA-TAG-867: Custom Field baru tampil sebagai kolom Hidden

10. Tutup Popup Detail
11. Buat Custom Field `CF New` berstatus Active lewat API hingga tersimpan
12. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
13. Klik header `⋯` pada tabel T-TAG-02
14. Verifikasi Kolom `CF New` ada pada daftar dengan checkbox tidak tercentang
15. Tutup overlay Column Visibility

### TC-FA-TAG-868: Urutan kolom Custom Field: grup General, Purchasing, Accounting, lalu nama A-Z

16. Klik header `⋯` lalu `Setup Column...`
17. Verifikasi Urutan: CF Alpha, CF Zeta (General A-Z), CF Vendor (Purchasing), CF Ledger (Accounting)
18. Tutup dialog Setup Column tanpa menyimpan

### TC-FA-TAG-869: Kolom Custom Field di luar Scope Asset Name berisi strip pada seluruh baris

19. Tampilkan kolom `CF Laptop Only` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
20. Verifikasi sedikitnya satu baris Excavator 20 Ton tampil pada tabel
21. Verifikasi Seluruh baris Excavator 20 Ton menampilkan `—` pada kolom `CF Laptop Only`

### TC-FA-TAG-871: Custom Field yang belum diisi menampilkan strip

22. Tampilkan kolom `CF Text` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
23. Verifikasi Sel CF Text AST-0020 menampilkan `—`
24. Tutup Popup Detail
25. Hapus preferensi kolom di browser
26. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG (Read) (Read: Plant B tanpa akses Manage purchase) [MR_PB_NOPUR], lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-870: Custom Field Purchasing di luar hak menampilkan No access dengan tooltip

27. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
28. Tampilkan kolom `CF Vendor` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
29. Arahkan pointer ke sel `No access`
30. Verifikasi Sel menampilkan `No access`
31. Verifikasi Tooltip `Requires Manage purchase access in this group.`
32. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 5, 9, 10, 11, 15, 18, 24, 25, 26, 32.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Urutan TC diatur menurut akun: Total Control lebih dulu (TC-FA-TAG-865 sampai 869 dan 871), lalu Manage asset & TAG (Read) (Read: Plant B tanpa akses Manage purchase) untuk TC-FA-TAG-870.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 19, 22, 28), serta melakukan aksi lewat sesi API (langkah 11).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-867 tidak menyebut kapan `CF New` dibuat; spec membuatnya lewat API sebagai langkah penghubung sebelum popup dibuka agar kolom baru ikut dimuat.
  - TC-FA-TAG-869 memakai Expected universal ("seluruh baris") sehingga spec menambah `Verifikasi` pembanding berupa sedikitnya satu baris tampil.
  - Seeding nilai Custom Field pada aset acuan dapat mengubah Last Updated aset itu dan menggeser urutan bawaan Last Updated terbaru yang dipakai TC lain; pemulihan lewat fixture BE di hook `after` perlu mengembalikan Last Updated.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
