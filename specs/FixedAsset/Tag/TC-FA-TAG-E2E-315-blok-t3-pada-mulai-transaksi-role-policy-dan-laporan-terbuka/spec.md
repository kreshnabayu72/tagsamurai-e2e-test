---
id: TC-FA-TAG-E2E-315-blok-t3-pada-mulai-transaksi-role-policy-dan-laporan-terbuka
title: "Blok T3 pada Mulai Transaksi: Role, Policy, dan Laporan Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1205
  - TC-FA-TAG-1206
  - TC-FA-TAG-1207
  - TC-FA-TAG-1208
  - TC-FA-TAG-1209
  - TC-FA-TAG-1210
coverage:
  web: automated
---

# Blok T3 pada Mulai Transaksi: Role, Policy, dan Laporan Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Manage asset & TAG dengan Update di group Plant B, `manageAssetTagDenganUpdateDiGroupPlantB_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_UP_PB_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 7): Asset Admin tanpa Manage asset & TAG, `assetAdminTanpaManageAssetTag_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_NOTAG_PASSWORD`.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 14): Asset Admin, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_PASSWORD`.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0020` ('Excavator 20 Ton - 20', Group Plant B) dengan Tag RFID `RF-00130` berstatus Paired. Keadaan awal di hook `before`: aset Available, Tag `RF-00130` tidak dapat dipindai dan tanpa laporan terbuka (T3). Langkah 19, 24, dan 28 menyiapkan ulang keadaan aset untuk TC berikutnya.
- Nama dan kode literal TC (aset `AST-0020` dan Tag `RF-00130`) tidak diberi suffix `{runId}` karena precondition dan asersi TC bergantung pada kode persis. Lampiran A belum memuat butir modul ini; seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE dicatat sebagai kebutuhan, dan suite berjalan serial.
- Transaction Policy Borrow memakai nilai bawaan (Allow manual identification to start OFF) dan tidak diubah. Pemegang Update di group Plant B, Asset Admin tanpa Manage asset & TAG, dan Asset Admin adalah baris Tabel Data Uji Pre-setup TC.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0020` (status Available, Tag `RF-00130`, laporan Tag) ke keadaan awal dan kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1205: Blok T3 pada Mulai: pemegang Update melihat tombol Replace TAG langsung

1. Buka layar Check-out Borrow untuk aset `AST-0020`
2. Jalankan langkah "Check-out"
3. Verifikasi pesan blok "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B." tampil
4. Verifikasi tombol `[Replace TAG]` tampil langsung bagi pemegang Update
5. Verifikasi tombol `[Report TAG]` tampil karena Tag belum dilaporkan

### TC-FA-TAG-1206: Blok T3 pada Mulai: pengguna tanpa Update tidak melihat tombol Replace TAG

6. Ganti akun: Logout dari akun yang sedang aktif
7. Login sebagai Asset Admin tanpa Manage asset & TAG dengan `assetAdminTanpaManageAssetTag_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_AA_NOTAG_PASSWORD`
8. Buka layar Check-out Borrow untuk aset `AST-0020`
9. Jalankan langkah "Check-out"
10. Verifikasi pesan blok "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B." tampil
11. Verifikasi tombol `[Replace TAG]` tidak tampil
12. Verifikasi tombol `[Report TAG]` tampil

### TC-FA-TAG-1210: Policy Allow manual identification to start bernilai bawaan OFF tidak membuka identifikasi manual pada Mulai

13. Ganti akun: Logout dari akun yang sedang aktif
14. Login sebagai Asset Admin dengan `assetAdmin_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_AA_PASSWORD`
15. Buka layar Check-out Borrow untuk aset `AST-0020`
16. Jalankan langkah "Check-out"
17. Verifikasi langkah "Check-out" diblokir
18. Verifikasi opsi `[I can't scan the TAG]` tidak tersedia untuk memulai transaksi (Policy "Allow manual identification to start" memakai nilai bawaan OFF)

### TC-FA-TAG-1207: Blok T3 pada Mulai: tombol Report TAG tidak tampil bila Tag sudah dilaporkan

19. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` Available di Group Plant B, Tag `RF-00130` tidak terbaca dan punya laporan terbuka Unreadable
20. Buka layar Check-out Borrow untuk aset `AST-0020`
21. Jalankan langkah "Check-out"
22. Verifikasi pesan blok "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B." tampil
23. Verifikasi tombol `[Report TAG]` tidak tampil

### TC-FA-TAG-1208: Aset T3 karena laporan Missing terbuka diblokir pada Mulai

24. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` Available di Group Plant B, Tag `RF-00130` punya laporan terbuka Missing
25. Buka layar Check-out Borrow untuk aset `AST-0020`
26. Jalankan langkah "Check-out"
27. Verifikasi langkah "Check-out" diblokir dengan pesan "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B."

### TC-FA-TAG-1209: Peringatan S-25 pada T2 tidak menutup transaksi dan dapat dilanjutkan

28. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` Available, Tag `RF-00130` dapat dipindai dan punya laporan Damaged terbuka (T2)
29. Buka layar Assign untuk aset `AST-0020`
30. Jalankan langkah "Assign / serah ke pemegang baru"
31. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tampil
32. Lanjutkan langkah "Assign / serah ke pemegang baru" sampai selesai
33. Verifikasi langkah Assign selesai dan aset berstatus Assigned

## Notes

- Mode: FE+BE.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6, 7, 13, 14, 19, 24, 28 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Urutan TC di spec ini mengikuti kesamaan keadaan aset (TC-FA-TAG-1205, 1206, dan 1210 memakai keadaan awal yang sama) dan akun, bukan urutan nomor TC; langkah ganti akun 6 sampai 7 dan 13 sampai 14 memakai akun yang dituntut precondition TC masing-masing.
- Verifikasi tidak tampil atau tidak tersedia (langkah 11, 18, 23) masing-masing didahului `Verifikasi` pesan blok atau blok langkah yang tampil pada TC yang sama sebagai anchor positif.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC-FA-TAG-1209 Post Condition ("Aset AST-0020 berstatus Assigned dan tetap memiliki status Tag Reported") tidak punya langkah observasi di TC; tidak diasersi.
  - TC-FA-TAG-1205 sampai 1210 memakai aset AST-0020 yang sama dengan keadaan berbeda (laporan Unreadable, Missing, atau Damaged terbuka) tanpa menyebut cara menyiapkan ulangnya; spec menyiapkannya lewat fixture BE (langkah 19, 24, dan 28).
