---
id: TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by
title: "Search: Brand, Model/Type, Default Addon, Default Label, Total Asset, Modified By, Tanpa Hasil, dan Kolom Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-346
  - TC-FA-FAAM-347
  - TC-FA-FAAM-348
  - TC-FA-FAAM-349
  - TC-FA-FAAM-350
coverage:
  web: automated
---

# Search: Brand, Model/Type, Default Addon, Default Label, Total Asset, Modified By, Tanpa Hasil, dan Kolom Tanggal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Modified By `Sarah Johnson`, Total Asset 42), `MacBook Pro` (Pre-setup #12), `Service Vehicle` (Pre-setup #14).
- Date Format dan Time Format General Settings dibaca dari pengaturan client sebelum langkah; nilainya dipakai apa adanya oleh teks Last Updated yang diketik.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-346: Search kelas kolom Brand, Model/Type, Default Addon, Default Label
1. Ketik Search `isuzu`, tekan Enter
2. Verifikasi keyword `isuzu` pada kolom Brand menampilkan baris `Service Vehicle`
3. Ganti isi kotak search dengan `7420`, tekan Enter
4. Verifikasi keyword `7420` pada kolom Model/Type menampilkan baris `Dell Latitude` (model ketiga di balik `+1 more`)
5. Ganti isi kotak search dengan `maps`, tekan Enter
6. Verifikasi keyword `maps` pada kolom Default Addon menampilkan baris `Service Vehicle` (addon di balik `+1 more`)
7. Ganti isi kotak search dengan `executive`, tekan Enter
8. Verifikasi keyword `executive` pada kolom Default Label menampilkan baris `MacBook Pro`
### TC-FA-FAAM-347: Search kelas kolom Total Asset
9. Ganti isi kotak search dengan `42`, tekan Enter
10. Verifikasi keyword `42` pada kolom Total Asset menampilkan baris `Dell Latitude` (Total Asset 42)
### TC-FA-FAAM-348: Search kelas kolom Modified By
11. Ganti isi kotak search dengan `johnson`, tekan Enter
12. Verifikasi keyword `johnson` menampilkan baris yang dimodifikasi `Sarah Johnson` (kolom Modified By tampil `Sarah J`), karena Search mencocokkan nama lengkap
13. Ganti isi kotak search dengan `sarah j`, tekan Enter
14. Verifikasi keyword `sarah j` menampilkan baris yang dimodifikasi `Sarah Johnson` (kolom Modified By tampil `Sarah J`)
### TC-FA-FAAM-349: Search tanpa kecocokan menampilkan empty state pencarian
15. Ganti isi kotak search dengan `zzzz-none`, tekan Enter
16. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
### TC-FA-FAAM-350: Kolom tanggal Last Updated tidak dapat dicari lewat Search
17. Klik `(←)` pada kotak Search
18. Verifikasi baris `Dell Latitude` tampil di tabel
19. Catat teks Last Updated baris `Dell Latitude` sesuai Date Format General Settings
20. Ketik Search teks Last Updated yang dicatat, tekan Enter
21. Verifikasi tabel kosong dengan `No results found`
22. Klik icon Filter
23. Verifikasi field `Last Updated` dengan placeholder `Select date` tersedia di Filter Panel
24. Klik icon Filter untuk menutup Filter Panel
25. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): klik `(←)` pada kotak Search sebelum TC-FA-FAAM-350 (mengembalikan tabel agar teks Last Updated dapat dicatat), pencatatan teks Last Updated, klik icon Filter untuk menutup panel, dan klik `(←)` terakhir.
- Expected b TC-FA-FAAM-350 ("penyaringan tanggal hanya lewat Filter Panel") berupa pernyataan; spec mengamatinya lewat keberadaan field `Last Updated` di Filter Panel (S-03; alasan: Expected b tidak memberi langkah observasi lain).
- Modified By diasersi berformat `[First Name] [Last Initial]` (`Sarah J`) pada kolom, sedangkan Search mencocokkan nama lengkap (R-14).
- Temuan untuk QA: Pre-setup #10 sampai #14 menyebut lima Asset Name bernama; Asset Name keenam (Total Asset 3, urutan sort pada TC-FA-FAAM-394) tidak diberi nama di Pre-setup.
