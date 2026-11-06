---
id: TC-FA-TAG-E2E-010-popup-detail-tombol-show-reported-non-standard-dan-not-paired-bagian-1
title: "Popup Detail: Tombol Show dan Close untuk Reported, Non-standard, dan Not Paired Yet"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-50
  - TC-FA-TAG-51
  - TC-FA-TAG-52
  - TC-FA-TAG-53
  - TC-FA-TAG-54
  - TC-FA-TAG-55
coverage:
  web: automated
---

# Popup Detail: Tombol Show dan Close untuk Reported, Non-standard, dan Not Paired Yet

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

- Data grup Excavator 20 Ton / Plant B (20 aset): lima aset acuan `AST-0011` (Excavator 20 Ton - 11), `AST-0020` (- 20), `AST-0021` (- 21), `AST-0043` (- 43), `AST-0044` (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011. Aset Reported: `AST-0020` dan `AST-0043`. Aset Non-standard: `AST-0043` sampai `AST-0047`.
- Data grup Excavator 20 Ton / Plant A: dua aset Not Paired Yet dengan TAG Code `—`, Status `Not Paired Yet`, dan row action `Pair TAG`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-50: Show Reported menyaring tabel T-TAG-02 ke aset yang dihitung

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik `Show` di samping angka `Reported`
3. Verifikasi tombol berubah label menjadi `Close`
4. Verifikasi tabel hanya memuat 2 aset: AST-0020 dan AST-0043
5. Verifikasi aset yang tampil memuat semua TAG Code-nya
6. Verifikasi angka pada blok info tidak berubah

### TC-FA-TAG-51: Close pada tombol Reported menampilkan semua aset kembali

7. Klik `Close` pada tombol yang sama
8. Verifikasi tabel kembali memuat 20 aset
9. Verifikasi label tombol kembali `Show`

### TC-FA-TAG-52: Show Non-standard menyaring tabel T-TAG-02 ke aset yang dihitung

10. Klik `Show` di samping angka `Non-standard`
11. Verifikasi tombol berubah label menjadi `Close`
12. Verifikasi tabel hanya memuat 5 aset: AST-0043, AST-0044, AST-0045, AST-0046, AST-0047
13. Verifikasi aset yang tampil memuat semua TAG Code-nya
14. Verifikasi angka pada blok info tidak berubah

### TC-FA-TAG-53: Close pada tombol Non-standard menampilkan semua aset kembali

15. Klik `Close` pada tombol yang sama
16. Verifikasi tabel kembali memuat 20 aset
17. Verifikasi label tombol kembali `Show`

### TC-FA-TAG-54: Hanya satu tombol Show aktif pada satu waktu

18. Klik `Show` di samping `Reported`
19. Klik `Show` di samping `Non-standard`
20. Verifikasi tombol di samping `Non-standard` berlabel `Close`
21. Verifikasi tombol `Reported` kembali berlabel `Show`
22. Verifikasi tabel memuat 5 aset Non-standard

### TC-FA-TAG-55: Show pada Not Paired Yet menyaring aset tanpa Tag Paired

23. Tutup popup dengan ikon close, lalu klik Asset Name `Excavator 20 Ton` pada baris Plant A
24. Klik `Show` di samping `Not Paired Yet`
25. Verifikasi tombol berlabel `Close`
26. Verifikasi tabel hanya memuat dua aset dengan TAG Code `—`, Status `Not Paired Yet`, dan row action `Pair TAG`
27. Verifikasi aset ber-Tag tidak tampil
28. Tutup popup dengan ikon close

## Notes

- Langkah 23 dan 28 adalah langkah penghubung (menutup popup), tanpa asersi (S-03, S-09).
- Langkah 2 TC-FA-TAG-51 dan TC-FA-TAG-53 (klik `Show`) sudah dijalankan oleh langkah 2 dan 10; tombol tetap aktif sampai langkah 7 dan 15 yang memuat klik `Close`. Urutan TC tidak diubah.
- Langkah 27 adalah asersi absence atas baris tabel; anchor positif adalah Verifikasi dua aset Not Paired Yet tampil (langkah 26) (bagian 8b butir 2).
- TC-FA-TAG-56 sampai 58 dan 1450 ada di spec 011.
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut asersi nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-51 dan TC-FA-TAG-53 Expected "Tabel kembali memuat 20 aset" tidak menyebut cara mengamati 20 baris sedangkan ukuran halaman default 10; spec mengasersi jumlah total aset (indikator total Pagination) dan menyerahkan cara pengamatannya ke tahap script. TC-FA-TAG-59 mengamati 20 baris dengan mengubah page size menjadi 25.
  - TC-FA-TAG-50 dan TC-FA-TAG-52 butir "memuat semua TAG Code-nya" tidak menyebut kode yang dimaksud; spec mengasersinya secara umum (semua Tag aset tampil di sel TAG Code).
