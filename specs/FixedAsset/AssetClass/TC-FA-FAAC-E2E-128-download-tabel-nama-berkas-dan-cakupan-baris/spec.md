---
id: TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris
title: "Download Tabel Asset Class: Menu, Nama Berkas, Cakupan Baris dan Kolom, serta Tanpa Toast Sukses"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-418
  - TC-FA-FAAC-419
  - TC-FA-FAAC-420
  - TC-FA-FAAC-421
  - TC-FA-FAAC-423
  - TC-FA-FAAC-424
  - TC-FA-FAAC-425
  - TC-FA-FAAC-430
sourceRules: ["§5#b8", "F-FAAC-14.k1", "R-15"]
smoke: []
dependsOn: []
trace:
  "§5#b8": [4, 6, 8, 11, 19, 20, 23]
  "F-FAAC-14.k1": [14, 15]
  "R-15": [25, 26]
anchor: [2]
coverage:
  web: automated
---

# Download Tabel Asset Class: Menu, Nama Berkas, Cakupan Baris dan Kolom, serta Tanpa Toast Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment), VEHICLES, IT-EQ (IT Equipment), MACHINERY, BLDG, STORAGE (Storage Equipment), OFFICE-NEW (Office Equipment (New)), LAND (Active) dan OFFICE-OLD (Office Equipment (Legacy), Inactive).
- Data Pre-setup tambahan (hanya dibaca): jumlah Asset Class total (N) lebih dari 25 (seed tambahan di luar sembilan kelas contoh); N diturunkan dari seeding dan tidak dibaca dari satu halaman tabel (8b butir 10). Seed disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: pembaca berkas unduhan CSV/XLSX (nama berkas, header, jumlah baris, baris data) disediakan tim FE; unduhan dicegat browser uji pada folder unduhan sementara.
- State yang diubah spec: konfigurasi kolom tabel (kolom Commercial dan Assets disembunyikan oleh langkah 17 lalu ditampilkan kembali oleh langkah 21). Pemulihan cadangan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-418: Menu Download pada tabel Asset Class

1. Arahkan kursor ke icon Download
2. Verifikasi tooltip icon berbunyi `Download`
3. Klik icon Download
4. Verifikasi menu menampilkan dua pilihan: `Download as CSV` dan `Download as XLSX`

### TC-FA-FAAC-419: Download as CSV memberi nama berkas Asset-Class.csv

5. Pilih `Download as CSV` pada menu yang terbuka
6. Verifikasi berkas terunduh dengan nama `Asset-Class.csv`

### TC-FA-FAAC-420: Download as XLSX memberi nama berkas Asset-Class.xlsx

7. Klik icon Download lalu pilih `Download as XLSX`
8. Verifikasi berkas terunduh dengan nama `Asset-Class.xlsx`

### TC-FA-FAAC-421: Download tanpa Search dan Filter memuat semua baris lintas halaman

9. Klik icon Download lalu pilih `Download as CSV`
10. Buka berkas dan hitung baris data
11. Verifikasi jumlah baris data sama dengan total Asset Class pada tabel (N lebih dari 10), bukan hanya 10 baris halaman pertama

### TC-FA-FAAC-430: Download saat hasil filter kosong hanya berisi header

12. Ketik Search `zzzzzz`, tekan Enter
13. Klik icon Download lalu pilih `Download as CSV`
14. Verifikasi berkas terunduh berisi baris header kolom
15. Verifikasi berkas tidak memuat baris data
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-FAAC-423: Download hanya memuat kolom yang sedang tampil

17. Sembunyikan kolom Commercial dan Assets lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Commercial dan Assets), klik `[Save]`
18. Klik icon Download lalu pilih `Download as CSV`
19. Verifikasi header berkas tidak memuat kolom Commercial dan Assets
20. Verifikasi kolom lain yang tampil ikut terunduh

### TC-FA-FAAC-424: Kolom yang ditampilkan kembali ikut terunduh

21. Tampilkan kembali kolom Commercial dan Assets lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Commercial dan Assets), klik `[Save]`
22. Klik icon Download lalu pilih `Download as CSV`
23. Verifikasi header berkas memuat kolom Commercial

### TC-FA-FAAC-425: Download berhasil tanpa toast sukses

24. Klik icon Download lalu pilih `Download as CSV`
25. Verifikasi tidak ada toast sukses yang tampil
26. Verifikasi berkas terunduh

## Notes

- Langkah 5 melanjutkan menu Download yang masih terbuka dari langkah 3 (state sama dengan membuka menu dari awal).
- Langkah penghubung (S-03): langkah 16 (menutup input Search dan mereset tabel, S-09; R-16), langkah 21 (menampilkan kembali kolom Commercial dan Assets; Assets ikut dipulihkan karena disembunyikan pada langkah 17). TC-FA-FAAC-424 langkah 1 dan 2 (sembunyikan lalu tampilkan Commercial) sudah terpenuhi oleh langkah 17 dan 21 karena Commercial telah disembunyikan oleh TC-FA-FAAC-423.
- Langkah 25 mendahului langkah 26 (8b butir 11): asersi absence toast diletakkan segera setelah pemicu dan sebelum asersi artefak; berkas terunduh pada langkah 26 menjadi anchor positif bahwa respons sudah diproses.
- TC-FA-FAAC-422 (keanggotaan baris berkas pada Search dan Filter aktif) tidak memuat klausa UI, hanya isi berkas, sehingga TC itu ada di spec 129 (kelas f); spec ini tidak mencampurnya lewat P-10. Nama berkas, header, dan jumlah baris tetap di spec ini (kelas f).
- Pembagian TC lintas spec: TC-FA-FAAC-422, 427 sampai 429, 432 sampai 434, dan 656 (isi berkas) ada di spec 129.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
