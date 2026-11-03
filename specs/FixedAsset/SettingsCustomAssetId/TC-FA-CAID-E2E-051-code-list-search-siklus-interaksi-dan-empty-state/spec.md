---
id: TC-FA-CAID-E2E-051-code-list-search-siklus-interaksi-dan-empty-state
title: "Modal View Code List: Siklus Interaksi Search dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-121
  - TC-FA-CAID-124
coverage:
  web: automated
---

# Modal View Code List: Siklus Interaksi Search dan Empty State

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-121: Siklus interaksi Search di Code List

1. Klik tautan `[View Code List]`
2. Hover icon Search
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search terbuka dengan placeholder `Search name or code...`
6. Verifikasi kursor fokus berada di input Search
7. Ketik `floor` tanpa menekan Enter
8. Verifikasi icon `(✕)` muncul di dalam input
9. Verifikasi tabel belum tersaring (enam Group masih tampil)
10. Tekan Enter
11. Verifikasi tabel menampilkan `Head Office > Floor 1` dan `Head Office > Floor 2`
12. Klik icon `(✕)` di dalam input
13. Verifikasi teks input kosong
14. Verifikasi input tetap terbuka
15. Verifikasi tabel masih menampilkan hasil `floor`
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan enam Group
18. Ganti isi kotak search dengan `floor`, tekan Enter
19. Klik icon `(←)` di kiri toolbar
20. Verifikasi kotak pencarian menutup
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung menampilkan enam Group

### TC-FA-CAID-124: Search tanpa hasil

23. Ketik Search `zzzzz`, tekan Enter
24. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 24 langkah.
- Langkah penghubung (tanpa `Verifikasi`): tidak ada; seluruh langkah aksi berasal dari langkah TC.
- Pada TC-FA-CAID-121 `Verifikasi` tooltip `Search` ditulis sebelum klik icon Search karena tooltip adalah state sementara (bagian 8b butir 5). Kursor fokus (langkah 6) ditulis segera setelah input terbuka.
- Modal tetap terbuka dari TC-FA-CAID-121 ke TC-FA-CAID-124; kotak Search sudah tertutup oleh klik `(←)` pada TC-FA-CAID-121, sehingga langkah Search pada TC-FA-CAID-124 membuka input kembali (atomik, bagian 8b butir 9).
- Pembagian TC lintas spec: TC-FA-CAID-122 dan 123 ada di spec 064; TC-FA-CAID-125, 126, dan 131 ada di spec 052.
- Temuan untuk QA:
  - TC-FA-CAID-121 Expected d menyatakan klik `(✕)` mengosongkan input tetapi tabel masih menampilkan hasil `floor`, sedangkan Expected f menyatakan klik `(←)` langsung mereset tabel; spec mengasersi keduanya sesuai TC.
