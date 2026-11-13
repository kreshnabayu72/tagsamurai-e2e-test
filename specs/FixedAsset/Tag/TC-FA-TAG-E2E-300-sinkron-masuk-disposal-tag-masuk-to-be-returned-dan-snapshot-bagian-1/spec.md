---
id: TC-FA-TAG-E2E-300-sinkron-masuk-disposal-tag-masuk-to-be-returned-dan-snapshot-bagian-1
title: "Sinkron Masuk Disposal: Tag Masuk ke Tab To Be Returned dan Snapshot, Bagian 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1233
  - TC-FA-TAG-1234
  - TC-FA-TAG-1235
  - TC-FA-TAG-1236
  - TC-FA-TAG-1237
  - TC-FA-TAG-1238
coverage:
  web: automated
---

# Sinkron Masuk Disposal: Tag Masuk ke Tab To Be Returned dan Snapshot, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Pengamat tab To Be Returned (sesi UI).
- Akun aktor: Asset Admin (pelaku disposal) [AA_DSPO] `assetAdminPelakuDisposal_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_AA_DSPO_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Pelaku disposal; dipakai sebagai pelaku kedua lewat sesi API.
- Akun aktor: Asset Admin (pelaku disposal Dedi K.) [AA_DSPK] `assetAdminPelakuDisposalDediK_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_AA_DSPK_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Pelaku disposal Dedi K.; dipakai sebagai pelaku kedua lewat sesi API pada TC-FA-TAG-1238.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui); Tag RFID `RF-00071`, NFC `NF-00092`, QR `QR-00433` dipasangkan ke aset itu sesuai TC; pemegang terakhir aset Rina T. (TC-FA-TAG-1238).
- Kemampuan teknis (disediakan tim FE/BE): menjalankan Execute disposal lewat sesi API; baseline jumlah baris dan badge tab To Be Returned dibaca di hook `before` (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri TAG Log Global dari Execute Disposal (Tag masuk To Be Returned) (langkah 1, 7, 12, 18, 25, 30).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset AST-0900, Tag, dan daftar To Be Returned ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status aset AST-0900, status Tag, dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1233: Execute Disposal memasukkan Tag RFID dengan snapshot lengkap

1. Pelaku kedua (Asset Admin pelaku Execute) lewat sesi API menjalankan Execute pada layar Disposal Execute aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui) dengan Tag RFID RF-00071 Paired sampai baris Executed
2. Buka tab To Be Returned
3. Verifikasi baris baru RF-00071 tampil di tab To Be Returned dengan Last Asset "Excavator 20 Ton - 2", Reason "Disposal", dan Return Group "Plant B"
4. Verifikasi kolom Since menampilkan tanggal hari Execute diikuti "(0 days)"
5. Verifikasi badge tab "To Be Returned" bertambah satu terhadap baseline

### TC-FA-TAG-1234: Execute Disposal memasukkan Tag NFC

6. Siapkan lewat fixture backend aset AST-0900 dengan Tag NFC NF-00092 Paired dan pulihkan daftar To Be Returned
7. Pelaku kedua (Asset Admin pelaku Execute) lewat sesi API menjalankan Execute pada layar Disposal Execute aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui) dengan Tag NFC NF-00092 Paired sampai baris Executed
8. Muat ulang halaman TAG tab Paired (F5)
9. Buka tab To Be Returned
10. Verifikasi baris NF-00092 tampil di tab To Be Returned dengan ikon tipe NFC, Reason "Disposal", dan Return Group "Plant B"

### TC-FA-TAG-1235: aset dengan Tag RFID dan NFC menghasilkan dua baris

11. Siapkan lewat fixture backend aset AST-0900 dengan Tag RFID RF-00071 dan Tag NFC NF-00092 Paired dan pulihkan daftar To Be Returned
12. Pelaku kedua (Asset Admin pelaku Execute) lewat sesi API menjalankan Execute pada layar Disposal Execute aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui) dengan Tag RFID RF-00071 dan NFC NF-00092 Paired sampai baris Executed
13. Muat ulang halaman TAG tab Paired (F5)
14. Buka tab To Be Returned
15. Verifikasi dua baris baru tampil: RF-00071 dan NF-00092, masing-masing Last Asset "Excavator 20 Ton - 2" dan Return Group "Plant B"
16. Verifikasi badge tab "To Be Returned" bertambah dua terhadap baseline

### TC-FA-TAG-1236: aset dengan Tag RFID dan QR hanya memasukkan Tag RFID

17. Siapkan lewat fixture backend aset AST-0900 dengan Tag RFID RF-00071 dan Tag QR QR-00433 Paired dan pulihkan daftar To Be Returned
18. Pelaku kedua (Asset Admin pelaku Execute) lewat sesi API menjalankan Execute pada layar Disposal Execute aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui) dengan Tag RFID RF-00071 dan QR QR-00433 Paired sampai baris Executed
19. Muat ulang halaman TAG tab Paired (F5)
20. Buka tab To Be Returned
21. Verifikasi baris RF-00071 tampil di tab To Be Returned
22. Ketik Search `QR-00433`, tekan Enter
23. Verifikasi Illustration `No results found`: pencarian "QR-00433" tidak menemukan Tag QR di To Be Returned

### TC-FA-TAG-1237: Return Group snapshot adalah Group asal aset (Group DSP), tanpa Disposal Group

24. Klik `(←)` pada kotak Search, lalu siapkan lewat fixture backend aset AST-0900 (group asal Plant B) dengan Tag RFID RF-00071 Paired dan pulihkan daftar To Be Returned
25. Pelaku kedua (Asset Admin pelaku Execute) lewat sesi API menjalankan Execute pada layar Disposal Execute aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui) dengan Tag RFID RF-00071 Paired sampai baris Executed
26. Muat ulang halaman TAG tab Paired (F5)
27. Buka tab To Be Returned
28. Verifikasi kolom Return Group baris RF-00071 menampilkan "Plant B" (Group asal aset)

### TC-FA-TAG-1238: Current Holder snapshot adalah pemegang terakhir aset

29. Siapkan lewat fixture backend aset AST-0900 (pemegang terakhir Rina T.) dengan Tag RFID RF-00071 Paired dan pulihkan daftar To Be Returned
30. Pelaku kedua (Asset Admin pelaku Execute Dedi K.) lewat sesi API menjalankan Execute pada layar Disposal Execute aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui) dengan Tag RFID RF-00071 Paired sampai baris Executed
31. Muat ulang halaman TAG tab Paired (F5)
32. Buka tab To Be Returned
33. Verifikasi kolom Current Holder baris RF-00071 menampilkan "Rina T." (pemegang terakhir aset), bukan "Dedi K." (pelaku Execute)

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 6, 11, 17, 24 dan 29 (menyiapkan data dan memulihkan daftar To Be Returned lewat fixture antar TC, S-09; mereset Search).
- Disposal dijalankan pelaku kedua lewat sesi API karena hanya memicu masuknya Tag ke To Be Returned dan tidak diasersi di sesinya (R-20); sesi UI akun Total Control mengamati tab To Be Returned.
- Absence TC-FA-TAG-1236 (Tag QR tidak ada di To Be Returned): memakai empty state `No results found` hasil Search sebagai anchor positif; baris RF-00071 yang tampil sebelumnya menjadi anchor tambahan (bagian 8b butir 2).
- TC-FA-TAG-1239 sampai 1243 dan 1381 ada di spec 301; TC-FA-TAG-1244 sampai 1247 di spec 302.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri TAG Log Global dari Execute Disposal (Tag masuk To Be Returned) (langkah 1, 7, 12, 18, 25, 30).
- Temuan untuk QA:
  - TC-FA-TAG-1233 sampai 1238 langkah TC ke-1 ('Login sbg Asset Admin lalu buka layar Disposal Execute') dan langkah TC ke-3 ('Login sbg Total Control') berupa dua akun; spec memakai Asset Admin sebagai pelaku kedua lewat sesi API dan Total Control sebagai pengamat UI.
  - TC-FA-TAG-1233 Post Condition (Tag RF-00071 berstatus To be Returned di registri Global; modul terdampak transactions-disposal dan all-tags) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-FA-TAG-1233 sampai 1238 memakai aset AST-0900 yang sama dengan kombinasi Tag berbeda; fixture memulihkan aset di antara TC.
