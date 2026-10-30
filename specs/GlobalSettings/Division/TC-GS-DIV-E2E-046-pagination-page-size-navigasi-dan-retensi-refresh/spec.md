---
id: TC-GS-DIV-E2E-046-pagination-page-size-navigasi-dan-retensi-refresh
title: "Pagination Tabel Division: Page Size, Navigasi, dan Retensi Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-166
  - TC-GS-DIV-167
  - TC-GS-DIV-168
  - TC-GS-DIV-170
coverage:
  web: automated
---

# Pagination Tabel Division: Page Size, Navigasi, dan Retensi Refresh

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS).
- Data Dinamis: Population D-02 (26 Division, Name (Code)): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada), sehingga tabel memuat 32 baris (4 halaman pada page size 10; halaman 4 berisi 2 baris). Nama literal tanpa suffix karena asersi jumlah baris, jumlah halaman, dan isi halaman 2 bergantung pada kumpulan nama ini (pengecualian S-12 untuk Population Division: seeding idempotent, cleanup milik spec, suite serial). Cleanup di hook `after` hanya menghapus Division Population yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Data uji TC-GS-DIV-170: keyword `a`, sort Name descending, halaman 2 pada page size 10. Hasil Search `a` berjumlah 25 baris: halaman 2 berurutan Name Z-A `Operations`, `Marketing`, `Legal`, `Internal Control`, `Information Technology`, `Human Resources`, `General Affairs`, `Finance`, `Facilities`, `Data Analytics`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: page size dikembalikan ke 10 (langkah 17), Search dikosongkan dan sort dikembalikan ke default Name A-Z (langkah 35 dan 36); hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): tabel harus memuat tepat 32 baris saat spec mulai.
- Kemampuan teknis: memuat ulang halaman (F5) pada konteks browser yang sama.

## Test Steps

1. Buka layar Global Settings > User > Division

### TC-GS-DIV-166: Pagination default 10 data per halaman dengan 4 halaman untuk 32 baris

2. Verifikasi halaman 1 menampilkan 10 baris
3. Verifikasi footer menampilkan 4 halaman
4. Verifikasi page size terpilih 10
5. Buka pilihan page size pada footer
6. Verifikasi pilihan page size 10, 25, 50, dan 100
7. Verifikasi tidak ada opsi All

### TC-GS-DIV-167: Ubah page size ke 25, 50, dan 100

8. Pilih page size 25
9. Verifikasi halaman 1 berisi 25 baris
10. Verifikasi total 2 halaman
11. Pilih page size 50
12. Verifikasi seluruh 32 baris tampil
13. Verifikasi total 1 halaman
14. Pilih page size 100
15. Verifikasi seluruh 32 baris tampil
16. Verifikasi total 1 halaman
17. Pilih page size 10

### TC-GS-DIV-168: Navigasi Next, Previous, dan input nomor halaman lewat Enter

18. Klik Next
19. Verifikasi tabel menampilkan halaman 2
20. Klik Previous
21. Verifikasi tabel kembali ke halaman 1
22. Ketik `4` pada input nomor halaman
23. Tekan Enter
24. Verifikasi halaman 4 langsung terbuka
25. Verifikasi halaman 4 berisi 2 baris

### TC-GS-DIV-170: Muat ulang halaman (F5) mempertahankan Search, Sort, Filter, dan halaman

26. Ketik Search `a`, tekan Enter
27. Klik header Name (ascending)
28. Klik header Name (descending)
29. Pindah ke halaman 2
30. Muat ulang halaman (F5)
31. Verifikasi tabel berada di halaman 2
32. Verifikasi baris halaman 2 berurutan Name Z-A: `Operations`, `Marketing`, `Legal`, `Internal Control`, `Information Technology`, `Human Resources`, `General Affairs`, `Finance`, `Facilities`, `Data Analytics`
33. Verifikasi indikator sort Name descending tetap aktif pada header Name
34. Verifikasi keyword `a` tetap aktif pada Search
35. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
36. Klik header Name (kembali ke sort default)

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Dependensi TC-GS-DIV-30 (Population) dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (166, 167, 168, 170) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (membuka pilihan page size untuk membaca daftar opsi TC-GS-DIV-166), langkah 17 (mengembalikan page size 10 sebelum TC-GS-DIV-168), langkah 35 dan 36 (mengosongkan Search dan mengembalikan sort default di akhir spec). Langkah 1 memenuhi "Buka Tab Division" TC-GS-DIV-166.
- Spec melewati sekitar 35 langkah (36 langkah) karena empat TC Pagination berbagi dataset 32 baris yang sama dan satu kelas harness (fungsional); tiap blok TC berdiri sendiri dan state dikembalikan lewat langkah penghubung, sehingga satu kegagalan tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-DIV-148 (Search dari halaman lebih dari 1) ada di spec 041; TC-GS-DIV-169 (Apply Filter dari halaman lebih dari 1) ada di spec 042; TC-GS-DIV-155 (kombinasi dengan page size) ada di spec 043.
- Temuan untuk QA:
  - TC-GS-DIV-170: nama TC dan Expected memuat "Filter", tetapi langkah dan Test Data tidak memakai Filter; spec mengikuti langkah TC (Search, Sort, halaman) dan tidak menambahkan Filter.
  - TC-GS-DIV-170: TC tidak menyatakan apakah Search bar tetap terbuka setelah F5; asersi keyword memeriksa nilai keyword aktif pada Search, dan langkah 35 mengasumsikan `(←)` tersedia setelah muat ulang.
  - TC-GS-DIV-170: isi halaman 2 diturunkan dari kumpulan nama Pre-setup + Population (25 baris cocok `a`); TC hanya menyebut halaman 2 tanpa isi.
