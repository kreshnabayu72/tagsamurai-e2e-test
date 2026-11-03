---
id: TC-FA-CAID-E2E-050-code-list-dataset-khusus-teks-literal-dan-nama-panjang
title: "Modal View Code List: Teks Literal, Nama 120 Karakter, dan Toolbar Tanpa Filter"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-127
  - TC-FA-CAID-162
  - TC-FA-CAID-163
coverage:
  web: automated
---

# Modal View Code List: Teks Literal, Nama 120 Karakter, dan Toolbar Tanpa Filter

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor pertama (TC-FA-CAID-162): Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Akun kedua (TC-FA-CAID-163 dan TC-FA-CAID-127): Total Control `Company Code List Khusus` (Pre-setup No 34, akun sendiri, bukan akun Pre-setup No 1); email disediakan tim FE/BE (Pre-setup No 34), kredensial `Spectra.env.FA_CODELIST_TC_PASSWORD` (nama usulan, didaftarkan di tahap script). Ganti akun ditulis sebagai langkah eksplisit (langkah 7 dan 8); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Environment variable: `FA_TC_PASSWORD` (akun default suite) dan `FA_CODELIST_TC_PASSWORD` (Total Control Company Code List Khusus). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen` untuk kedua akun UI; baseline konfigurasi dan aset Company Alpha (Pre-setup No 10 dan 11) tidak dipakai spec ini; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach` untuk akun yang login di hook `before`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup No 28 (Company Alpha, untuk TC-FA-CAID-162): master data ber-Code Company Alpha; hanya dibaca, dan asersi hanya membutuhkan sedikitnya satu baris Group.
- Data Pre-setup No 34 (`Company Code List Khusus`): dataset Pre-setup No 28 ditambah Group `<b>Bold</b> Site` (Code `BLD`) dan Group bernama 120 karakter berkode `LNG`. Disediakan tim FE/BE pada Company itu (dikembalikan ke keadaan awal sebelum tiap run); sesi API Company itu untuk seed adalah kemampuan yang disediakan tim FE/BE. Spec hanya membaca.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-162: Toolbar tanpa Filter dan Changelog, tabel tanpa checkbox seleksi

1. Klik tautan `[View Code List]`
2. Verifikasi Table Tools memuat icon Search dan icon Download
3. Verifikasi tabel `Group Codes` menampilkan sedikitnya satu baris
4. Verifikasi tidak ada icon Filter dan tidak ada icon Changelog pada Table Tools
5. Verifikasi tidak ada kolom checkbox seleksi dan tidak ada Bulk Action Bar

### TC-FA-CAID-163: Nama Group 120 karakter

6. Tutup Modal View Code List dengan `[✕]`
7. Ganti akun: Logout dari akun Total Control Company Alpha
8. Login sebagai Total Control `Company Code List Khusus`
9. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
10. Klik tautan `[View Code List]`
11. Ketik Search `LNG`, tekan Enter
12. Verifikasi baris Group berkode `LNG` tampil
13. Verifikasi nama tampil penuh 120 karakter dengan wrap natural tanpa penggalan `..`
14. Hover nama pada baris tersebut
15. Verifikasi tidak ada tooltip hover pada nama

### TC-FA-CAID-127: Teks literal pada Search dan nilai sel

16. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
17. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
18. Verifikasi tidak ada script yang dijalankan (tidak ada dialog alert)
19. Klik `(←)` pada kotak Search
20. Verifikasi nama Group tampil sebagai teks literal `<b>Bold</b> Site` tanpa dirender sebagai huruf tebal

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 20 langkah.
- Urutan TC di dalam spec: TC-FA-CAID-162, 163, lalu 127. TC-FA-CAID-162 memakai Company Alpha (akun hook `before`) sehingga berada di awal; TC-FA-CAID-163 dan 127 memakai `Company Code List Khusus` sesudah ganti akun. TC-FA-CAID-127 mengetik keyword skrip dan membersihkannya di akhir, sehingga TC lain tidak mewarisi Search aktif.
- Langkah penghubung (tanpa `Verifikasi`): langkah 6 (menutup modal sebelum ganti akun), langkah 7 dan 8 (ganti akun), langkah 9 (membuka halaman tujuan), langkah 11 (Search `LNG` untuk menemukan baris target TC-FA-CAID-163, bagian 8b butir 9), dan langkah 19 (klik `(←)` untuk mengosongkan Search sebelum membaca baris `<b>Bold</b> Site`).
- Pada TC-FA-CAID-127 `Verifikasi` empty state (langkah 17) ditulis sebelum `Verifikasi` tidak ada script karena empty state menjadi anchor positif bahwa Search sudah diproses (bagian 8b butir 2 dan 5); Expected TC menyebut keduanya dalam satu butir.
- Asersi absence (tidak ada Filter dan Changelog, tidak ada checkbox, tidak ada tooltip hover) didahului `Verifikasi` baris tabel tampil (langkah 3 dan 12).
- Pembagian TC lintas spec: Modal View Code List dikover spec 049 sampai 060, 064, dan 065; TC-FA-CAID-127, 162, dan 163 hanya ada di spec ini.
- Alasan topik Modal View Code List berada di beberapa spec (bagian 3 prinsip 1): tiap spec memakai dataset berbeda. Spec ini memakai `Company Code List Khusus` (Pre-setup No 34, dataset teks literal dan nama 120 karakter) dengan akun sendiri; dataset tetap Pre-setup No 28 ada di spec 049 dan `Company Volume` 120 master per tab (Pre-setup No 16) di spec 054 dan 055. Ukuran gabungan dataset-dataset itu juga melebihi sekitar 35 langkah.
- Temuan untuk QA:
  - Pre-setup No 34 mensyaratkan Company khusus dengan akun sendiri; email akun dan nama env var password tidak tertulis (email "disediakan tim FE/BE"), sehingga spec memakai usulan `FA_CODELIST_TC_PASSWORD`. TC-FA-CAID-162 tetap menyebut Company Alpha (Pre-setup No 1, dataset No 28), sehingga dijalankan sebelum ganti akun.
  - TC-FA-CAID-127 langkah 3 menyebut "Hapus keyword" tanpa menyebut aksinya; spec memakai `(←)` pada kotak Search (bagian 8b butir 9).
