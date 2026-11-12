---
id: TC-FA-TAG-E2E-230-pagination-popup-detail-state-sort-dan-halaman
title: "Pagination Popup Detail Assets: Pilihan Page Size, Navigasi, Input Tidak Valid, dan State Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-922
  - TC-FA-TAG-923
  - TC-FA-TAG-924
  - TC-FA-TAG-1451
  - TC-FA-TAG-1452
coverage:
  web: automated
---

# Pagination Popup Detail Assets: Pilihan Page Size, Navigasi, Input Tidak Valid, dan State Sort

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk dataset tab Paired di bawah; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup tab Paired (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup acuan | Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupAcuan` |
| Aset acuan grup Excavator 20 Ton / Plant B | Grup memuat 20 aset sehingga Popup Detail punya 2 halaman pada page size 10; lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; AST-0020 laporan terbuka; AST-0043 Non-standard dan laporan terbuka; AST-0044 Tag QR Non-standard | `asetPlantB` |

- State yang diubah: hanya state tampilan tabel grup dan Popup Detail (sort, halaman, tombol `Show`); tidak ada perubahan data bisnis. Sort tabel grup dikembalikan netral oleh langkah 32.
- Nilai literal Pre-setup (nama aset, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### Pagination Popup Detail (TC-FA-TAG-922)

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Verifikasi popup menampilkan 10 baris pada halaman 1 dari 2 halaman
3. Buka selector page size pada popup
4. Verifikasi opsi page size 10 / 25 / 50 / 100
5. Tutup selector page size dengan Esc

### Navigasi halaman (TC-FA-TAG-1451)

6. Klik halaman berikut
7. Verifikasi halaman 2 memuat baris ke-11 sampai ke-20
8. Klik halaman sebelumnya
9. Verifikasi halaman 1 memuat baris ke-1 sampai ke-10

### Input nomor halaman tidak valid (TC-FA-TAG-1452)

10. Ketik `0` pada input nomor halaman lalu tekan Enter
11. Verifikasi input `0` diabaikan
12. Ganti isi input nomor halaman dengan `3`, tekan Enter
13. Verifikasi input `3` diabaikan
14. Ganti isi input nomor halaman dengan `a`, tekan Enter
15. Verifikasi input `a` diabaikan
16. Verifikasi Popup Detail tetap di halaman 1

### Menutup dan membuka kembali mereset state (TC-FA-TAG-923)

17. Klik header Brand sekali
18. Pindah ke halaman 2
19. Klik `Show` di samping `Reported`
20. Tutup popup dengan ikon close
21. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
22. Verifikasi popup terbuka dengan urutan bawaan Last Updated terbaru: lima aset acuan tampil berurutan AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
23. Verifikasi popup berada di halaman 1
24. Verifikasi tombol `Show` berlabel `Show`
25. Tutup popup dengan ikon close

### Sort dan halaman independen dari tabel grup (TC-FA-TAG-924)

26. Klik header Total Assets pada tabel grup sekali
27. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
28. Klik header Asset ID pada popup sekali
29. Verifikasi tabel grup tetap terurut Total Assets menaik
30. Verifikasi popup terurut Asset ID menaik
31. Tutup popup dengan ikon close
32. Klik header Total Assets pada tabel grup dua kali lagi hingga sort netral

## Notes

- Langkah penghubung (S-03): langkah 5 (menutup selector page size), 18 (TC-FA-TAG-923 langkah 3: pindah ke halaman 2), 20 dan 25 (menutup popup dengan ikon close; TC-FA-TAG-923 langkah 5 memakai "tutup popup"), serta 31 dan 32 (menutup popup dan mengembalikan sort tabel grup ke netral sebelum spec berakhir).
- Pembagian TC: TC-FA-TAG-1451 dan TC-FA-TAG-1452 diurutkan sesudah TC-FA-TAG-922 karena memakai popup yang sudah terbuka dan halaman 1; TC-FA-TAG-923 dan TC-FA-TAG-924 diurutkan sesudahnya karena mengubah sort dan menutup popup (S-10).
- A-15: nilai literal Pre-setup (nama aset, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-923 Expected "urutan bawaan Last Updated terbaru" tidak menyebut baris yang tampil; spec hanya mengasersi urutan relatif lima aset acuan dari Data Uji (S-14).
  - TC-FA-TAG-923 langkah 4 `Show` di samping `Reported` tidak menyebut bahwa `Show` berubah label menjadi `Hide` atau lainnya; spec hanya mengasersi label `Show` pada Expected langkah akhir.
  - TC-FA-TAG-1452 mengasersi popup "tetap di halaman 1" tanpa menyebut isi baris; spec hanya mengasersi nomor halaman.
  - Post Condition semua TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
