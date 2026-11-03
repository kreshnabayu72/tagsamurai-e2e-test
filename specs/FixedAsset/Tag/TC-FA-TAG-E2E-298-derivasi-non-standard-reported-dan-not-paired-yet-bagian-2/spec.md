---
id: TC-FA-TAG-E2E-298-derivasi-non-standard-reported-dan-not-paired-yet-bagian-2
title: "Derivasi Non-standard, Reported, dan Not Paired Yet: Reported, Not Paired Yet, dan Pembentukan Baris Grup, Bagian 2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1324
  - TC-FA-TAG-1325
  - TC-FA-TAG-1326
  - TC-FA-TAG-1327
  - TC-FA-TAG-1328
  - TC-FA-TAG-1329
  - TC-FA-TAG-1330
  - TC-FA-TAG-1331
coverage:
  web: automated
---

# Derivasi Non-standard, Reported, dan Not Paired Yet: Reported, Not Paired Yet, dan Pembentukan Baris Grup, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data Pre-setup tab Paired (TC): Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC dan QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B memuat lima aset acuan: AST-0011 ('Excavator 20 Ton - 11'), AST-0020 ('- 20'), AST-0021 ('- 21'), AST-0043 ('- 43'), AST-0044 ('- 44').
- Data tambahan (TC, tanpa suffix): AST-0044 dengan dua Tag dan laporan terbuka pada keduanya (TC-FA-TAG-1324); AST-0020 dengan laporan berstatus Declined (TC-FA-TAG-1325); Asset Name Laptop Pro 14 (NFC dan QR) dengan aset AST-0500 yang hanya punya Tag NFC Paired (TC-FA-TAG-1327); Asset Name Drill Press di Plant C dengan 3 aset (1 ber-Tag dan 2 tidak) dan di Plant D hanya aset tanpa Tag yang bukan Not Paired Yet (TC-FA-TAG-1328); Asset Name Crane Hydraulic di Plant A dengan 4 aset tanpa Tag Paired (TC-FA-TAG-1329).
- Kemampuan teknis (disediakan tim FE/BE): membaca state backend (status Tag dan laporan) tanpa UI hanya untuk butir Expected TC yang menyebutnya (S-11).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: TAG Type Asset Name, data aset/Tag/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1324: Reported dihitung per aset dengan laporan Tag terbuka

1. Pulihkan data lewat fixture backend (AST-0044 dengan dua Tag dan laporan terbuka pada keduanya, tanpa laporan lain pada grup), lalu muat ulang halaman TAG tab Paired
2. Verifikasi Reported baris Excavator 20 Ton / Plant B = 1 (dihitung per aset)

### TC-FA-TAG-1325: aset tanpa laporan terbuka tidak terhitung Reported

3. Pulihkan data lewat fixture backend (AST-0020 dengan laporan berstatus Declined), lalu muat ulang halaman TAG tab Paired
4. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
5. Verifikasi status AST-0020 tidak memuat badge `Tag Reported`
6. Klik `Show` di samping `Reported`
7. Verifikasi tabel Show Reported memuat aset lain berstatus `Tag Reported`
8. Verifikasi AST-0020 tidak tampil pada `Show` Reported

### TC-FA-TAG-1326: aset tanpa Tag Paired sama sekali terhitung Not Paired Yet

9. Tutup Popup Detail
10. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
11. Klik `Show` di samping `Not Paired Yet`
12. Verifikasi dua aset tampil dengan Status `Not Paired Yet`

### TC-FA-TAG-1327: aset dengan sebagian tipe wajib terpasang bukan Not Paired Yet dan bukan Non-standard

13. Tutup Popup Detail, lalu pulihkan data lewat fixture backend (AST-0500 hanya punya Tag NFC Paired)
14. Klik Asset Name `Laptop Pro 14` pada baris HQ untuk membuka Popup Detail
15. Verifikasi AST-0500 tidak berstatus `Not Paired Yet` dan tidak bertanda Non-standard
16. Verifikasi tidak ada kondisi Tagging khusus pada AST-0500

### TC-FA-TAG-1328: baris grup terbentuk dari kombinasi Asset Name dan Group dengan minimal satu Tag Paired atau satu aset Not Paired Yet

17. Tutup Popup Detail, lalu pulihkan data lewat fixture backend (Drill Press di Plant C dan Plant D)
18. Ketik Search `Drill Press`, tekan Enter
19. Verifikasi baris Drill Press / Plant C tampil
20. Verifikasi tidak ada baris untuk kombinasi Drill Press / Plant D yang tidak memiliki Tag Paired maupun Not Paired Yet

### TC-FA-TAG-1329: grup hanya berisi aset Not Paired Yet tetap tampil

21. Klik `(←)` pada kotak Search, lalu pulihkan data lewat fixture backend (Crane Hydraulic di Plant A dengan 4 aset tanpa Tag Paired)
22. Ketik Search `Crane Hydraulic`, tekan Enter
23. Verifikasi baris Crane Hydraulic / Plant A tampil dengan Total Assets 4, Reported 0, Non-standard 0, Not Paired Yet 4

### TC-FA-TAG-1330: jumlah baris Show Non-standard sama dengan angka Non-standard pada blok info

24. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
25. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
26. Klik `Show` di samping `Non-standard`
27. Verifikasi tabel memuat 5 aset, sama dengan angka Non-standard 5 pada blok info

### TC-FA-TAG-1331: menu TAG tidak membuat jadwal, tugas, atau approval untuk Replace TAG

28. Tutup Popup Detail
29. Verifikasi tidak ada elemen penjadwalan, tugas, dokumen pengajuan, atau approval pada sidebar, Table Tools, dan aksi halaman TAG

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 3, 9, 13, 17, 21, 22, 24 dan 28 (memulihkan data lewat fixture antar TC, menutup popup, mereset Search, S-09; Search untuk menemukan baris target, R-16).
- Absence: TC-FA-TAG-1325 (AST-0020 tidak tampil pada `Show` Reported), TC-FA-TAG-1328 (tidak ada baris Plant D), dan TC-FA-TAG-1331 (tidak ada elemen penjadwalan) didahului `Verifikasi` data pembanding pada surface yang sama (aset lain berstatus `Tag Reported`, baris Drill Press / Plant C, dan halaman TAG yang termuat) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1324 dan 1329 tidak menyebut Asset Name dan Group baris yang diamati; spec memakai grup yang memuat aset itu dari fixture.
  - TC-FA-TAG-1325 Expected a ('AST-0020 tidak tampil pada Show Reported') dan b (badge `Tag Reported`) diasersi dengan urutan lihat daftar penuh dulu, lalu `Show` Reported.
  - TC-FA-TAG-1327 Expected b ('Tidak ada kondisi Tagging khusus') adalah kesimpulan; diasersi sebagai satu `Verifikasi`.
  - TC-FA-TAG-1331 menyebut 'sidebar, Table Tools, dan aksi'; spec mengasersi ketiganya dalam satu `Verifikasi` daftar elemen yang sama-sama tidak ada (S-01).
