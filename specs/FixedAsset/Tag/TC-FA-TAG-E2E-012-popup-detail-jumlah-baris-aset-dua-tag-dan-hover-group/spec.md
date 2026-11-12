---
id: TC-FA-TAG-E2E-012-popup-detail-jumlah-baris-aset-dua-tag-dan-hover-group
title: "Popup Detail: Jumlah Baris Sama dengan Total Assets, Aset dengan Dua Tag, dan Hover Badge Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-59
  - TC-FA-TAG-60
  - TC-FA-TAG-61
coverage:
  web: automated
---

# Popup Detail: Jumlah Baris Sama dengan Total Assets, Aset dengan Dua Tag, dan Hover Badge Group

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

- Data grup Excavator 20 Ton / Plant B (20 aset): lima aset acuan `AST-0011` (Excavator 20 Ton - 11), `AST-0020` (- 20), `AST-0021` (- 21), `AST-0043` (- 43), `AST-0044` (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011. `AST-0044` memuat dua Tag: `QR-00232` (Non-standard) dan `RF-00132`.
- Group Plant B berada di bawah hierarki `Head Office > Plant B`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-59: Jumlah baris tabel T-TAG-02 tanpa penyaringan sama dengan Total Assets

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Hitung jumlah baris pada tabel
4. Verifikasi tabel memuat 20 baris, sama dengan nilai Total Assets 20 pada blok info
5. Verifikasi satu baris per aset meskipun aset ber-Tag lebih dari satu

### TC-FA-TAG-60: Aset dengan dua Tag tampil sebagai satu baris dengan TAG Code bertumpuk

6. Cari baris AST-0044 pada tabel
7. Verifikasi AST-0044 tampil sebagai satu baris
8. Verifikasi sel TAG Code memuat dua baris sel bertumpuk vertikal berurutan A-Z menurut TAG Code: `[QR] QR-00232` dengan ikon peringatan, lalu `[RFID] RF-00132`
9. Verifikasi tidak ada `+N more` pada sel TAG Code

### TC-FA-TAG-61: Hover badge Group pada Popup Detail menampilkan hierarki penuh

10. Arahkan pointer ke badge Group pada baris pertama
11. Verifikasi tooltip menampilkan hierarki penuh `Head Office > Plant B`
12. Tutup popup dengan ikon close

## Notes

- Langkah 3, 6, dan 12 adalah langkah penghubung atau pengamatan tanpa asersi (S-03). Langkah 2 mengubah page size menjadi 25 agar seluruh 20 baris tampil sebelum dihitung (S-14); pengaturan itu tidak dipulihkan karena popup ditutup pada langkah 12.
- Langkah 6 mencari AST-0044 pada baris yang tampil tanpa Search: AST-0044 adalah aset dengan Last Updated terbaru sehingga berada di baris teratas tabel yang diurutkan Last Updated terbaru di atas.
- Langkah 9 adalah asersi absence atas teks `+N more`; anchor positif adalah Verifikasi dua baris sel TAG Code pada AST-0044 (langkah 8) (bagian 8b butir 2).
- Langkah 10 mengarahkan pointer ke badge Group pada baris pertama, yaitu baris AST-0044 yang berada di Group Plant B.
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut asersi nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-61 Expected menyebut "hierarki penuh `Head Office > Plant B`" tanpa menyebut apakah baris pertama memang ber-Group Plant B (semua aset grup ini ber-Group Plant B); spec mengikuti TC.
  - TC-FA-TAG-59 tidak menyebut cara menghitung jumlah baris selain mengubah page size; spec menyerahkan cara penghitungan ke tahap script.
