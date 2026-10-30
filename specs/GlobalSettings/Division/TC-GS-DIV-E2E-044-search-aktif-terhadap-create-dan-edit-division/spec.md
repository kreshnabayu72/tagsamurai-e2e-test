---
id: TC-GS-DIV-E2E-044-search-aktif-terhadap-create-dan-edit-division
title: "Search Aktif terhadap Create dan Edit Division"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-161
  - TC-GS-DIV-162
coverage:
  web: automated
---

# Search Aktif terhadap Create dan Edit Division

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Dinamis milik spec (dibuat lewat kemampuan seeding Division lewat API di hook `before`, Code auto-generate dan tidak diasersi; seeding minimal, hanya Division yang dipakai langkah `Verifikasi`):
  - `Accounting {runId}-044` (baris pembanding yang cocok dengan keyword `Accounting`, tampil sebelum asersi baris `Tax Compliance` tidak tampil; TC-GS-DIV-161).
  - `Customer Service {runId}-044` (target Edit TC-GS-DIV-162, setara baris `Customer Service`; Division Population `Customer Service` tidak diubah, sesuai S-06).
  - `Customer Care {runId}-044` (setara Division `Customer Care` D-04 yang harus tetap tampil).
- Data Dinamis dibuat lewat UI: `Tax Compliance {runId}-044` dengan Code `TAX` literal (D-13, TC-GS-DIV-161). Code `TAX` literal mengikuti TC dan harus unik; hook `before` menghapus lewat API sisa Division `Tax Compliance` bersuffix `-044` dari run lama yang berkode `TAX` (penghapusan dibatasi ke nama bersuffix spec ini, bukan berdasarkan kode saja), dan hook `after` menghapus `Tax Compliance {runId}-044`, `Client Care {runId}-044`, `Customer Service {runId}-044`, `Customer Care {runId}-044`, dan `Accounting {runId}-044` lewat API tanpa berasumsi setup berhasil penuh.
- Hasil rename TC-GS-DIV-162: `Client Care {runId}-044`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: Search dikosongkan dan page size dikembalikan ke 10 di akhir spec; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): Code `TAX` literal harus bebas dari Division lain saat spec mulai.
- Kemampuan teknis: membuka row action `⋯` baris tertentu hasil Search; memilih page size 50.

## Test Steps

### TC-GS-DIV-161: Division baru yang tidak cocok dengan Search aktif tidak muncul

1. Ketik Search `Accounting`, tekan Enter
2. Klik `[+ Division]`
3. Isi `Division Name` dengan `Tax Compliance {runId}-044`
4. Isi `Code` dengan `TAX`
5. Klik `[Submit]`
6. Verifikasi toast sukses `Success, division has been created.`
7. Verifikasi baris `Accounting {runId}-044` tampil di tabel (pembanding, cocok dengan keyword `Accounting`)
8. Verifikasi baris `Tax Compliance {runId}-044` tidak tampil karena tidak cocok dengan keyword `Accounting`
9. Klik icon `(✕)` pada input Search
10. Tekan Enter pada input kosong
11. Ubah page size ke 50
12. Verifikasi baris `Tax Compliance {runId}-044` tampil setelah Search dikosongkan

### TC-GS-DIV-162: Edit Name yang membuat Division tidak lagi cocok dengan Search aktif menghilangkannya dari tabel

13. Ketik Search `Customer`, tekan Enter
14. Klik row action `⋯` pada baris `Customer Service {runId}-044` lalu pilih `Edit`
15. Ubah `Division Name` menjadi `Client Care {runId}-044`
16. Klik `[Save]`
17. Verifikasi toast sukses `Success, division has been updated.`
18. Verifikasi baris `Customer Care {runId}-044` tetap tampil
19. Verifikasi baris `Client Care {runId}-044` hilang dari tabel karena tidak lagi cocok dengan keyword `Customer`
20. Klik icon `(✕)` pada input Search
21. Tekan Enter pada input kosong
22. Ubah page size ke 10

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Precondition "Tabel Division terisi 32 baris" (TC-GS-DIV-30) tidak diasersi langkah mana pun sehingga tidak di-seed; spec hanya men-seed Division yang dipakai langkah `Verifikasi` (S-11) di hook `before`, termasuk dependensi TC-GS-DIV-50 (`Customer Care`), tanpa menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (161, 162) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (page size 50 supaya seluruh baris, termasuk `Tax Compliance {runId}-044`, tampil pada satu halaman sebelum langkah 12; posisi baris itu pada halaman 10 baris tidak diasumsikan), langkah 20 sampai 22 (mengosongkan Search dan mengembalikan page size 10 di akhir spec). Search bar tetap terbuka sejak langkah 1, sehingga "Klik icon Search" TC-GS-DIV-162 tidak diulang dan langkah 13 memakai langkah atomik "Ketik Search"; langkah 9 dan 10 (mengosongkan Search) merupakan Expected c TC-GS-DIV-161 sekaligus pembersihan state sebelum TC-GS-DIV-162.
- Asersi tambahan: langkah 7 (baris `Accounting {runId}-044` tampil) adalah baris pembanding sebelum asersi baris tidak tampil (bagian 8b butir 2). Pada TC-GS-DIV-162, `Customer Care` tetap tampil (butir c, langkah 18) diasersi sebelum `Client Care` hilang (butir b, langkah 19) karena menjadi baris pembanding.
- Nama Division uji memakai suffix per run (S-12) walau TC menyebut `Tax Compliance`, `Customer Service`, `Customer Care`, dan `Client Care`: asersi hanya bergantung pada kecocokan keyword (`Accounting`, `Customer`) dan bukan pada nama literal; Code `TAX` dipertahankan literal karena disebut TC (D-13).
- Pembagian TC lintas spec: TC-GS-DIV-141 sampai 148 (Search toolbar) ada di spec 041; TC-GS-DIV-153 sampai 159 (kombinasi) ada di spec 043.
- Temuan untuk QA:
  - TC-GS-DIV-161: Post Condition ("Division Tax Compliance (TAX) tersimpan") tanpa langkah observasi tersendiri; disimpulkan dari Expected c (baris tampil setelah Search dikosongkan), tidak ada asersi tambahan.
  - TC-GS-DIV-162: TC mengedit baris `Customer Service` (Population) dan mengandalkan `Customer Care` dari TC-GS-DIV-50 (Code `CC`); spec memakai Division milik sendiri bersuffix dengan Code auto-generate supaya Population bersama tidak berubah, sehingga Code `CC` tidak dipakai.
  - TC-GS-DIV-161: TC tidak menyebut posisi baris `Tax Compliance` pada tabel; spec memakai page size 50 untuk menampilkan seluruh baris pada satu halaman.
