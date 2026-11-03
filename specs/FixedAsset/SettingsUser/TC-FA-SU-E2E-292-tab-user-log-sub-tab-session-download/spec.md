---
id: TC-FA-SU-E2E-292-tab-user-log-sub-tab-session-download
title: "Tab User Log sub-tab Session: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-889
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Session Budi Santoso (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-889: Cakupan baris dan kolom Download: Search, Filter, Sort, dan Column Visibility

1. Buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Session
2. Klik icon Download, pilih `Download as CSV`
3. Verifikasi berkas memuat seluruh baris (bukan hanya halaman aktif)
4. Verifikasi urutan baris pada berkas mengikuti sort aktif
5. Ketik Search `ended`, tekan Enter
6. Klik icon Filter, pilih rentang 12/07/26 sampai 13/07/26 pada Date
7. Klik `[Apply]`
8. Klik icon Download, pilih `Download as CSV`
9. Verifikasi berkas hanya memuat baris yang cocok dengan Search `ended` dan Filter Date 12/07/26 sampai 13/07/26 (irisan: S-6, S-8)
10. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon ← pada kotak Search
11. Klik icon Filter untuk menutup panel
12. Klik header kolom Column Visibility (⋯), hilangkan centang Note, tekan Esc
13. Klik icon Download, pilih `Download as CSV`
14. Verifikasi tidak ada toast peringatan
15. Verifikasi kolom Note tidak ikut berkas
16. Klik header kolom Column Visibility (⋯), centang kembali Note, tekan Esc
17. Klik icon Download, pilih `Download as CSV`
18. Verifikasi kolom Note ikut kembali pada berkas
19. Ketik Search `zzzz`, tekan Enter
20. Klik icon Download, pilih `Download as CSV`
21. Verifikasi tidak ada toast
22. Verifikasi berkas terunduh
23. Verifikasi berkas hanya memuat baris header kolom yang visible
24. Klik icon ← pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Panel Filter tetap terbuka sesudah `[Apply]` dan baru tertutup bila icon Filter diklik (keputusan produk); karena itu `[Clear Field]` + `[Apply]` dijalankan tanpa mengklik icon Filter lagi. Langkah 11 (`Klik icon Filter untuk menutup panel`) adalah langkah penghubung yang menutup panel sebelum blok berikutnya (S-03, S-09).
- Temuan untuk QA (S-15): (1) TC-FA-SU-889: Expected a menyebut seluruh baris tanpa jumlah; spec tidak menambah angka. Search `ended` dan Filter Date 12/07/26 sampai 13/07/26 dipilih spec karena TC tidak menyebut nilainya. Isi berkas adalah kemampuan baca berkas dari tim FE.
