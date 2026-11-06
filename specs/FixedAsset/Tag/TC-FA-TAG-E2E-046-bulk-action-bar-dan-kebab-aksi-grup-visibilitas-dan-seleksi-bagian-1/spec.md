---
id: TC-FA-TAG-E2E-046-bulk-action-bar-dan-kebab-aksi-grup-visibilitas-dan-seleksi-bagian-1
title: "Bulk Action Bar Popup Detail: Visibilitas Pair TAG dan Batch Replace TAG, serta Jumlah Terpilih"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-199
  - TC-FA-TAG-200
  - TC-FA-TAG-201
  - TC-FA-TAG-202
  - TC-FA-TAG-203
  - TC-FA-TAG-204
  - TC-FA-TAG-205
coverage:
  web: automated
---

# Bulk Action Bar Popup Detail: Visibilitas Pair TAG dan Batch Replace TAG, serta Jumlah Terpilih

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Aset acuan grup Excavator 20 Ton / Plant B: AST-0011 (Excavator 20 Ton - 11) dan AST-0021 (Excavator 20 Ton - 21), keduanya ber-Tag RFID tanpa laporan terbuka. Grup Excavator 20 Ton / Plant A memuat dua aset Not Paired Yet. Grup Laptop Pro 14 / HQ memuat 23 aset ber-Tag dan 2 aset Not Paired Yet; Popup Detail memuat aset ber-Tag dan aset Not Paired Yet pada halaman yang sama (precondition TC-FA-TAG-203 d).
- Kemampuan teknis (disediakan tim FE/BE): seed idempotent dan pemulihan aset dan Tag lewat fixture backend (lihat `suite.md`).
- Pemulihan di hook `after`: kembalikan data Pre-setup tab Paired ke keadaan awal bila seeding mengubahnya. Spec ini tidak mengubah data bisnis.
- State global: tidak ada. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-199 dan TC-FA-TAG-200: seleksi aset Not Paired Yet pada grup Plant A

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant A
2. Centang dua aset Not Paired Yet
3. Verifikasi Bulk Action Bar tampil dengan jumlah terpilih 2
4. Verifikasi aksi `Pair TAG` (ikon `Link`, dark) tampil
5. Verifikasi aksi `Batch Replace TAG` tidak tampil
6. Klik ikon `×` di sisi kanan Bulk Action Bar
7. Centang satu aset Not Paired Yet
8. Verifikasi aksi `Pair TAG` tampil pada Bulk Action Bar
9. Klik ikon `×` di sisi kanan Bulk Action Bar, lalu tutup Popup Detail

### TC-FA-TAG-204, TC-FA-TAG-201, TC-FA-TAG-202, dan TC-FA-TAG-205: grup Plant B

10. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
11. Verifikasi tabel Popup Detail memuat sedikitnya satu baris
12. Verifikasi Bulk Action Bar tidak tampil sebelum ada aset terpilih
13. Centang AST-0011 dan AST-0021
14. Verifikasi aksi `Batch Replace TAG` (ikon `ReplaceTag`, dark) tampil
15. Verifikasi aksi `Pair TAG` tidak tampil
16. Klik ikon `×` di sisi kanan Bulk Action Bar
17. Centang AST-0011
18. Verifikasi aksi `Batch Replace TAG` tampil pada Bulk Action Bar
19. Klik ikon `×` di sisi kanan Bulk Action Bar
20. Centang AST-0011 dan AST-0021
21. Verifikasi Bulk Action Bar menampilkan jumlah terpilih 2
22. Verifikasi Bulk Action Bar menampilkan ikon `×`
23. Klik ikon `×` di sisi kanan Bulk Action Bar
24. Verifikasi seleksi dibatalkan
25. Verifikasi Bulk Action Bar tertutup
26. Tutup Popup Detail

### TC-FA-TAG-203: seleksi campuran pada grup Laptop Pro 14 / HQ

27. Klik Asset Name `Laptop Pro 14` pada baris HQ
28. Centang satu aset ber-Tag dan satu aset Not Paired Yet
29. Verifikasi Bulk Action Bar tampil dengan jumlah terpilih 2
30. Verifikasi aksi `Pair TAG` tidak tampil karena tidak seluruh aset Not Paired Yet
31. Verifikasi aksi `Batch Replace TAG` tidak tampil karena aset Not Paired Yet tidak punya Tag eligible
32. Klik ikon `×` di sisi kanan Bulk Action Bar, lalu tutup Popup Detail

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6, 16, dan 19 (membersihkan seleksi lewat `×`, S-09), 9 dan 32 (membersihkan seleksi lewat `×` lalu menutup Popup Detail), 26 (menutup Popup Detail).
- Perubahan urutan (S-05): urutan TC sumber 199, 200, 201, 202, 203, 204, 205 menjadi 199, 200, 204, 201, 202, 205, 203. Alasan: TC-FA-TAG-199 dan TC-FA-TAG-200 memakai Popup Detail Plant A; TC-FA-TAG-204 (Bulk Action Bar belum tampil) harus lebih dulu sebelum ada aset yang dicentang di Popup Detail Plant B; TC-FA-TAG-203 memakai Popup Detail HQ sehingga ditaruh terakhir.
- Asersi tambahan di luar Expected TC (S-03): langkah 11 (tabel memuat baris sebagai anchor absence langkah 12, bagian 8b butir 2); langkah 29 (Bulk Action Bar tampil sebagai anchor absence langkah 30 dan 31). Absence langkah 5 didahului langkah 4 (anchor), dan absence langkah 15 didahului langkah 14.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-199 dan TC-FA-TAG-200 menyebut "aset Not Paired Yet" tanpa ID aset; spec memilih dua baris Not Paired Yet pada Popup Detail Plant A.
  - TC-FA-TAG-203 menyebut satu aset ber-Tag dan satu aset Not Paired Yet tanpa ID; spec memilih baris mana pun yang tampil bersama pada Popup Detail HQ.
  - TC-FA-TAG-205 Expected a menyebut jumlah terpilih 2 dan ikon `×` dalam satu butir; spec memisahnya menjadi dua langkah Verifikasi (21 dan 22).
