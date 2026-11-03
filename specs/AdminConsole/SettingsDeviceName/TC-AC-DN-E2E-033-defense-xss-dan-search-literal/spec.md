---
id: TC-AC-DN-E2E-033-defense-xss-dan-search-literal
title: "Defense-in-Depth: Nama berisi Tag Script Dirender sebagai Teks dan Search Karakter Khusus Literal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-561
  - TC-AC-DN-562
  - TC-AC-DN-563
  - TC-AC-DN-564
coverage:
  web: automated
---

# Defense-in-Depth: Nama berisi Tag Script Dirender sebagai Teks dan Search Karakter Khusus Literal

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-561, 562, 563, 564 |

- Env var password: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Measurement `Unit` (#13) dan Pohon Uji Kategori dengan leaf `Antenna` (#14) dibaca saja; Device Name inti dan seed (#16, #17) dibaca saja untuk TC-AC-DN-564 (tidak ada nama yang memuat karakter uji).
- Data Dinamis (S-12): Device Name `<script>alert(1)</script> {runId}-033` (Category `Antenna`, Measurement `Unit`) dibuat langkah Create TC-AC-DN-561 lewat UI; hook `after` menghapusnya lewat fixture backend (disediakan tim FE/BE). Kemampuan teknis: pembaca dialog browser untuk asersi tidak ada dialog alert.

## Test Steps

### TC-AC-DN-561: Nama Device Name berisi tag script dirender sebagai teks pada List

1. Klik `+ Device Name`
2. Ketik `<script>alert(1)</script> {runId}-033` pada field Device Name
3. Pilih Measurement "Unit"
4. Pilih Category "Antenna"
5. Klik `[Submit]`
6. Ketik Search `{runId}-033`, tekan Enter
7. Verifikasi kolom Device Name menampilkan teks literal `<script>alert(1)</script> {runId}-033`
8. Verifikasi tidak ada dialog alert browser yang tampil
9. Verifikasi tidak ada elemen script yang ditambahkan pada tabel

### TC-AC-DN-562: Nama Device Name berisi tag script dirender sebagai teks pada dialog Detail

10. Klik nama Device Name `<script>alert(1)</script> {runId}-033` pada baris
11. Verifikasi grid dialog "Device Name Detail" menampilkan Device Name sebagai teks literal `<script>alert(1)</script> {runId}-033`
12. Verifikasi tidak ada dialog alert browser yang tampil
13. Tutup dialog Detail

### TC-AC-DN-563: Nama Device Name berisi tag script dirender sebagai teks pada modal Changelog

14. Klik ikon Changelog
15. Klik header kolom Date dua kali
16. Verifikasi kolom Device Name pada entri terbaru menampilkan teks literal `<script>alert(1)</script> {runId}-033`
17. Verifikasi tidak ada dialog alert browser yang tampil
18. Tutup modal "Changelog: Device Name"
19. Klik `(←)` pada kotak Search

### TC-AC-DN-564: Kata kunci Search berisi karakter khusus dicocokkan sebagai teks literal

20. Klik ikon Search, ketik Search `%`, tekan Enter
21. Verifikasi kata kunci "%" menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
22. Ganti isi kotak search dengan `'`, tekan Enter
23. Verifikasi kata kunci "'" menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
24. Ganti isi kotak search dengan `"`, tekan Enter
25. Verifikasi kata kunci """ menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
26. Ganti isi kotak search dengan `' OR '1'='1`, tekan Enter
27. Verifikasi kata kunci "' OR '1'='1" menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
28. Klik `(←)` pada kotak Search

## Notes

- Spec defense-in-depth (kelas a, injeksi XSS pada render dan karakter khusus Search). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan nilai (S-12): nama uji bersuffix `{runId}-033` setelah teks `<script>alert(1)</script>`; kata kunci Search TC-AC-DN-561 dan 562 ("script") diganti `{runId}-033` agar baris milik spec yang ditemukan (R-16). Asersi teks literal memakai nilai bersuffix yang sama (R-06).
- Ketergantungan dalam spec: TC-AC-DN-562 dan 563 memakai Device Name yang dibuat langkah Create TC-AC-DN-561 (precondition TC "sudah dibuat"); Search yang aktif dari TC-AC-DN-561 dipakai ulang oleh TC-AC-DN-562 (halaman yang sama dipakai berulang tanpa alasan state).
- Langkah penghubung (S-03): menutup dialog Detail, menutup modal Changelog, dan mengosongkan Search lewat `(←)`.
- Temuan untuk QA:
  - TC-AC-DN-564 langkah 4 menulis kata kunci `""""` (empat tanda kutip) sedangkan Expected c menulis `"""`; spec memakai satu tanda kutip ganda `"` sebagai kata kunci.
  - TC-AC-DN-563 mengurutkan Date dua kali menjadi Newest First tanpa menyebut urutan awal modal.
