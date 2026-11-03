---
id: TC-FA-TAG-E2E-005-search-tanpa-hasil-scroll-horizontal-dan-aksesibilitas-tab-paired
title: "Search Tanpa Hasil, Scroll Horizontal pada Layar Sempit, dan Aksesibilitas Tab Paired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-18
  - TC-FA-TAG-19
  - TC-FA-TAG-20
  - TC-FA-TAG-21
  - TC-FA-TAG-22
  - TC-FA-TAG-23
coverage:
  web: automated
---

# Search Tanpa Hasil, Scroll Horizontal pada Layar Sempit, dan Aksesibilitas Tab Paired

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

- Data TC-FA-TAG-23: grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan `AST-0011` (Excavator 20 Ton - 11), `AST-0020` (- 20), `AST-0021` (- 21), `AST-0043` (- 43), `AST-0044` (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011. `AST-0044` memuat Tag `QR-00232` (Non-standard) dan `RF-00132`.
- Kata kunci uji Search `zzzzqq` tidak cocok dengan data apa pun.
- Kemampuan teknis: pengaturan ukuran viewport browser (dipersempit pada langkah 9, dipulihkan pada langkah 15); pembacaan atribut label aksesibilitas (`aria-label`) ikon (TC-FA-TAG-22); navigasi fokus keyboard (Tab, Enter, Space).
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah selain ukuran viewport (dipulihkan pada langkah 15 dan di hook `after`).

## Test Steps

### TC-FA-TAG-18: Search tanpa hasil pada tab Paired menampilkan No results found

1. Ketik Search `zzzzqq`, tekan Enter
2. Verifikasi Illustration tampil dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
3. Verifikasi tabel grup tidak memuat baris

### TC-FA-TAG-19: Mengosongkan Search setelah No results found memulihkan baris grup

4. Klik `(←)` pada kotak Search
5. Ketik Search `zzzzqq`, tekan Enter
6. Verifikasi `No results found` tampil
7. Kosongkan isi kotak search, tekan Enter
8. Verifikasi empat baris grup tampil kembali

### TC-FA-TAG-20: Tabel grup dapat di-scroll horizontal pada layar sempit

9. Persempit viewport browser sehingga seluruh kolom tidak muat
10. Buka menu Fixed Asset > TAG lewat sidebar
11. Verifikasi tabel grup menampilkan scroll horizontal
12. Geser tabel grup secara horizontal sampai ujung kanan
13. Verifikasi kolom terakhir `Not Paired Yet` dapat dijangkau dengan scroll
14. Verifikasi isi kolom `Not Paired Yet` tidak terpotong
15. Pulihkan ukuran viewport browser

### TC-FA-TAG-21: Accessibility: baris grup dan tombol aksi dapat dijangkau keyboard

16. Tekan Tab berulang dari Table Tools hingga baris grup
17. Verifikasi fokus berpindah ke tombol Table Tools, Asset Name, dan kebab aksi grup secara berurutan
18. Pada Asset Name tekan Enter
19. Verifikasi Popup Detail terbuka
20. Tekan Tab berulang di dalam Popup Detail
21. Verifikasi Popup Detail memuat focus trap: Tab tidak keluar dari popup
22. Tutup popup dengan ikon close
23. Pada Asset Name lain tekan Space
24. Verifikasi Popup Detail terbuka
25. Tutup popup dengan ikon close

### TC-FA-TAG-22: Accessibility: ikon tipe Tag memiliki label aksesibilitas

26. Periksa atribut label aksesibilitas ikon TAG Type pada baris Excavator 20 Ton / Plant A
27. Verifikasi ikon RFID berlabel aksesibilitas `RFID`
28. Periksa ikon TAG Type pada baris Laptop Pro 14 / HQ
29. Verifikasi ikon NFC berlabel `NFC`
30. Verifikasi ikon QR berlabel `QR`

### TC-FA-TAG-23: Accessibility: ikon peringatan Non-standard punya tooltip yang dapat dibuka lewat fokus

31. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
32. Pindahkan fokus keyboard ke ikon peringatan di samping `QR-00232` pada AST-0044
33. Verifikasi tooltip `This TAG type is not required by the asset name.` tampil saat fokus keyboard
34. Tutup popup dengan ikon close

## Notes

- Langkah 4, 15, 22, 25, dan 34 adalah langkah penghubung (mengosongkan Search; memulihkan viewport; menutup popup), tanpa asersi (S-03). Langkah 4 mereset tabel dari state `No results found` TC-FA-TAG-18 sebelum TC-FA-TAG-19 (S-09).
- Langkah 10 membuka menu dari sidebar karena TC-FA-TAG-20 menguji tampilan tabel setelah halaman dibuka pada viewport sempit.
- Langkah 20 dan 21: TC-FA-TAG-21 Expected c ("focus trap: Tab tidak keluar dari popup") tidak punya langkah di TC; langkah 20 adalah aksi tambahan untuk mengamatinya (S-03).
- Langkah 33 mengasumsikan baris AST-0044 berada di halaman pertama Popup Detail (urutan Last Updated terbaru di atas; AST-0044 paling baru) (S-14).
- Temuan untuk QA:
  - TC-FA-TAG-20 Expected b berbunyi "Kolom terakhir Not Paired Yet dapat dijangkau dengan scroll tanpa memotong isi", sedangkan kolom terakhir tabel menurut TC-FA-TAG-1 adalah `Column Visibility (⋯)`; spec mengikuti teks TC.
  - TC-FA-TAG-21 Langkah 3 ("Asset Name lain") tidak menyebut baris yang dimaksud; spec memakai baris grup kedua.
  - TC-FA-TAG-22 tidak menyebut cara membaca atribut label aksesibilitas (mis. `aria-label`); spec menyerahkannya ke tahap script.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut asersi nama, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
