---
id: TC-FA-TAG-E2E-268-seleksi-popup-detail-select-all-selection-limit-checkbox-bagian-2
title: "Seleksi Popup Detail: Checkbox Header, Seleksi Terjaga Saat Pindah Halaman dan Saat Sort Diubah (Bagian 2)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1405
  - TC-FA-TAG-1406
  - TC-FA-TAG-1407
coverage:
  web: automated
---

# Seleksi Popup Detail: Checkbox Header, Seleksi Terjaga Saat Pindah Halaman dan Saat Sort Diubah (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab Paired (tanpa suffix `{runId}`; kunci `Fixture.fixedAssetTag.pairedGrup`): grup Excavator 20 Ton / Plant A (RFID, 20 aset), Excavator 20 Ton / Plant B (RFID, 20 aset; target Popup Detail, 10 baris per halaman sehingga 2 halaman; memuat aset AST-0011 dan AST-0021), Laptop Pro 14 / HQ (NFC dan QR, 25 aset), dan Forklift Manual / Plant A (Non TAG, 10 aset).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset tab Paired; tidak ada endpoint yang dikarang di spec ini.
- State global: tidak ada. Spec ini tidak mengubah Selection Limit dan tidak mengubah data bisnis; seleksi dan sort dikembalikan ke netral pada akhir kasus.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-1405: checkbox header mengikuti jumlah baris tercentang di halaman aktif

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Verifikasi checkbox header unchecked
3. Centang semua 10 baris halaman 1 satu per satu
4. Verifikasi checkbox header checked
5. Hilangkan centang semua baris halaman 1
6. Verifikasi checkbox header unchecked
7. Verifikasi Bulk Action Bar tertutup

### TC-FA-TAG-1406: seleksi terjaga saat pindah halaman

8. Centang dua baris pada halaman 1
9. Pindah ke halaman 2
10. Centang satu baris pada halaman 2
11. Verifikasi Bulk Action Bar menampilkan jumlah terpilih 3
12. Kembali ke halaman 1
13. Verifikasi dua baris yang dicentang sebelumnya tetap tercentang
14. Verifikasi jumlah terpilih tetap 3
15. Klik ikon `×` di sisi kanan Bulk Action Bar

### TC-FA-TAG-1407: seleksi terjaga saat sort diubah

16. Centang baris AST-0011 dan AST-0021
17. Klik header kolom Name untuk mengubah sort
18. Verifikasi baris AST-0011 dan AST-0021 tetap tercentang pada posisi barunya (seleksi dilacak per baris, bukan per posisi)
19. Verifikasi Bulk Action Bar tetap menampilkan jumlah terpilih 2
20. Klik header kolom Name dua kali lagi hingga indikator sort netral
21. Klik ikon `×` di sisi kanan Bulk Action Bar
22. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1405 s.d. 1407). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1400 s.d. 1404 ada di spec 267; TC-FA-TAG-1371 s.d. 1376 ada di spec 264; TC-FA-TAG-1408 s.d. 1413 ada di spec 265 dan 266.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 15, 21 (membatalkan seleksi lewat ikon `×` pada Bulk Action Bar); 20 (mengembalikan sort kolom Name ke netral); 22 (menutup Popup Detail).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1407 menyebut baris AST-0011 dan AST-0021 tanpa menyebut halaman tempat keduanya berada pada urutan awal; spec mengasersi keduanya tetap tercentang pada posisi barunya tanpa menyebut halaman.
  - TC-FA-TAG-1405 s.d. 1407 tidak menyebut cara membatalkan seleksi antar kasus; spec memakai ikon `×` pada Bulk Action Bar seperti pada TC-FA-TAG-1408.
  - TC-FA-TAG-1406 tidak menyebut baris mana yang dicentang; spec mencentang dua baris pada halaman 1 dan satu baris pada halaman 2 tanpa menyebut barisnya.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
