---
id: TC-FA-TAG-E2E-044-row-action-per-kondisi-aset-urutan-dan-penghitungan-ulang-bagian-1
title: "Row Action per Kondisi Aset di Popup Detail: Replace TAG, Decline Report, dan Pair TAG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-189
  - TC-FA-TAG-190
  - TC-FA-TAG-191
  - TC-FA-TAG-192
  - TC-FA-TAG-193
  - TC-FA-TAG-194
  - TC-FA-TAG-195
  - TC-FA-TAG-196
coverage:
  web: automated
---

# Row Action per Kondisi Aset di Popup Detail: Replace TAG, Decline Report, dan Pair TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Aset acuan grup Excavator 20 Ton / Plant B: AST-0011 (Excavator 20 Ton - 11, Tag RF-00101, tanpa laporan terbuka), AST-0020 (- 20, laporan terbuka pada RF-00130), AST-0021 (- 21, tanpa laporan terbuka), AST-0043 (- 43, Tag QR-00231 Non-standard dan laporan terbuka), AST-0044 (- 44, dua Tag: RF-00132 Normal dan QR-00232 Non-standard, tanpa laporan terbuka). Grup Excavator 20 Ton / Plant A memuat dua aset Not Paired Yet.
- Data precondition TC-FA-TAG-194 (dipakai sebagai precondition TC, hanya dasar langkah 30): AST-0044 punya dua Tag (RF-00132 dan QR-00232) tanpa laporan terbuka pada Data Pre-setup; fixture TC ini membuat laporan terbuka Damaged hanya pada RF-00132 lewat fixture BE pada langkah 30 dan dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seed idempotent dan pemulihan aset, Tag, dan laporan Tag lewat fixture backend (lihat `suite.md`).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus laporan terbuka RF-00132 pada AST-0044 dan kembalikan data Pre-setup tab Paired ke keadaan awal.
- State global: tidak ada. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 30) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-189, TC-FA-TAG-190, TC-FA-TAG-191, TC-FA-TAG-192, TC-FA-TAG-195, TC-FA-TAG-196: aset di grup Plant B

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik kebab baris AST-0011 (Tag RF-00101 sesuai TAG Type RFID, tanpa laporan terbuka)
3. Verifikasi kebab memuat satu aksi `Replace TAG` (ikon `ReplaceTag`, dark)
4. Verifikasi kebab tidak memuat `Decline Report` dan `Pair TAG`
5. Tutup kebab
6. Klik kebab baris AST-0044 (dua Tag: RF-00132 Normal dan QR-00232 Non-standard, tanpa laporan terbuka)
7. Verifikasi kebab memuat satu aksi `Replace TAG`
8. Verifikasi kebab tidak memuat `Decline Report`
9. Tutup kebab
10. Klik kebab baris AST-0020 (laporan terbuka pada RF-00130)
11. Verifikasi kebab memuat `Replace TAG` (dark) lalu `Decline Report` (ikon `CloseCircleLine`, severity danger)
12. Verifikasi aksi dark tampil sebelum aksi danger
13. Tutup kebab
14. Klik kebab baris AST-0043 (QR-00231 Non-standard dan laporan terbuka)
15. Verifikasi kebab memuat `Replace TAG` lalu `Decline Report`
16. Tutup kebab
17. Klik kebab baris AST-0021 (tanpa laporan terbuka)
18. Verifikasi kebab memuat `Replace TAG`
19. Verifikasi kebab tidak memuat `Decline Report`
20. Tutup kebab
21. Klik kebab baris AST-0011
22. Verifikasi kebab memuat `Replace TAG`
23. Verifikasi kebab tidak memuat aksi `TAG Log`
24. Tutup kebab, lalu tutup Popup Detail

### TC-FA-TAG-193: aset Not Paired Yet di grup Plant A

25. Klik Asset Name `Excavator 20 Ton` pada baris Plant A
26. Klik kebab baris aset Not Paired Yet
27. Verifikasi kebab memuat satu aksi `Pair TAG` (ikon `Link`, dark)
28. Verifikasi kebab tidak memuat `Replace TAG` dan `Decline Report`
29. Tutup kebab, lalu tutup Popup Detail

### TC-FA-TAG-194: aset dua Tag dengan laporan terbuka pada salah satu Tag

30. Buka laporan terbuka pada Tag RF-00132 milik AST-0044 lewat fixture BE hingga laporan tersimpan
31. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
32. Klik kebab baris AST-0044
33. Verifikasi kebab memuat `Replace TAG` dan `Decline Report` karena minimal satu Tag punya laporan terbuka
34. Tutup kebab
35. Tutup Popup Detail

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5, 9, 13, 16, 20, 24, 29, 34, dan 35 (menutup kebab dan Popup Detail), 30 (membuat laporan precondition TC-FA-TAG-194).
- Perubahan urutan (S-05): urutan TC sumber 189, 190, 191, 192, 193, 194, 195, 196 menjadi 189, 190, 191, 192, 195, 196, 193, 194. Alasan: TC-FA-TAG-189 sampai 192, 195, dan 196 memakai satu pembukaan Popup Detail Plant B; TC-FA-TAG-193 memakai Popup Detail Plant A; TC-FA-TAG-194 ditaruh paling akhir karena precondition-nya (laporan terbuka pada RF-00132 milik AST-0044) bertentangan dengan keadaan AST-0044 pada TC-FA-TAG-190 dan harus dibuat sesudah TC-FA-TAG-190 selesai.
- Baris target dipilih langsung dari lima aset acuan yang tampil di halaman pertama Popup Detail menurut urutan Last Updated terbaru ke terlama (AST-0044, AST-0043, AST-0021, AST-0020, AST-0011); Search tidak dipakai.
- Asersi tambahan di luar Expected TC (S-03): langkah 18 dan 22 (aksi `Replace TAG` tampil sebagai anchor positif untuk absence langkah 19 dan 23, bagian 8b butir 2). Pada langkah 4, 8, 19, 23, dan 28, absence didahului Verifikasi aksi lain pada kebab yang sama (langkah 3, 7, 18, 22, dan 27).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 30) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-190 (langkah 2) dan TC-FA-TAG-194 (precondition d) sama-sama menyatakan AST-0044 punya dua Tag (RF-00132 dan QR-00232); laporan terbuka pada RF-00132 hanya diadakan fixture TC-FA-TAG-194. Data Uji kedua TC menyebut AST-0044 Tag QR Non-standard dan Reported grup Plant B bernilai 2. Spec membuat laporan RF-00132 sesudah TC-FA-TAG-190 (langkah 30) supaya keadaan kedua TC terpenuhi.
  - TC-FA-TAG-193 menyebut "baris aset Not Paired Yet" tanpa menyebut ID aset di grup Plant A; spec memilih baris Not Paired Yet mana pun di Popup Detail Plant A.
  - TC-FA-TAG-196 Expected b ("Popup TAG Log hanya dibuka lewat klik TAG Code") tidak punya langkah observasi di TC itu; spec mengasersi hanya ketiadaan aksi `TAG Log` pada kebab (langkah 23). Pembukaan Popup TAG Log lewat klik TAG Code diuji TC-FA-TAG-212 di spec 048.
