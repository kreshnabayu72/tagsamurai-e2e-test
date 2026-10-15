---
id: TC-AC-PP-E2E-058-defense-search-payload-script-dan-karakter-literal
title: "Defense-in-Depth Search: Karakter Pola dan Payload Script Diperlakukan sebagai Teks Literal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-103
coverage:
  web: automated
---

# Defense-in-Depth Search: Karakter Pola dan Payload Script Diperlakukan sebagai Teks Literal

## Prerequisites

- Mode: FE+BE (kelas a, defense-in-depth: injeksi karakter pola dan payload script pada input Search).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe` 10 Aug 2026, Version 2 `John Doe` 02 Jul 2026, Version 1 `Jane Smith` 15 Jan 2026 akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- Kemampuan teknis:
  - Fixture BE untuk membuat ulang dataset Riwayat A.
  - Pemantau dialog alert browser (untuk mengamati bahwa payload script tidak memunculkan dialog `alert`) dan pengamat eksekusi script pada halaman.
- State UI yang diubah spec dan dipulihkan: search bar ditutup dan keyword dikosongkan di akhir spec.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-103: Karakter khusus dan payload script pada Search diperlakukan sebagai teks literal

1. Buka Settings > Privacy Policy
2. Klik icon Search
3. Ketik "%"
4. Tekan Enter
5. Verifikasi tabel menampilkan empty state "No results found"
6. Verifikasi tabel tidak menampilkan seluruh baris (karakter pola pencarian tidak menjadi wildcard)
7. Ganti keyword dengan "_"
8. Tekan Enter
9. Verifikasi tabel menampilkan empty state "No results found"
10. Verifikasi tabel tidak menampilkan seluruh baris (karakter pola pencarian tidak menjadi wildcard)
11. Ganti keyword dengan ".*"
12. Tekan Enter
13. Verifikasi tabel menampilkan empty state "No results found"
14. Verifikasi tabel tidak menampilkan seluruh baris (karakter pola pencarian tidak menjadi regex)
15. Ganti keyword dengan `<script>alert(1)</script>`
16. Tekan Enter
17. Verifikasi tabel menampilkan empty state "No results found"
18. Verifikasi tabel tidak menampilkan seluruh baris
19. Verifikasi tidak ada dialog alert dari browser
20. Verifikasi tidak ada script yang dieksekusi
21. Verifikasi isi input pencarian tampil sebagai teks apa adanya (`<script>alert(1)</script>`)
22. Klik icon `(←)` untuk menutup search bar dan mereset keyword

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness: a (defense-in-depth: injeksi pada input Search), dipisah dari spec fungsional Search `TC-AC-PP-E2E-033` sesuai prinsip 13a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AC-PP-103 dipindah dari spec `TC-AC-PP-E2E-033` ke spec ini sesuai prinsip 13a; spec `033` tidak lagi memuat TC tersebut.
- Langkah penghubung (tanpa awalan Verifikasi): langkah membuka halaman di awal dan langkah menutup search bar serta mengosongkan keyword di akhir.
- Temuan untuk QA:
  - TC-AC-PP-103 Expected a menggabungkan tiga klausa untuk setiap keyword (empty state, karakter pola bukan wildcard atau regex, tidak mencocokkan semua baris); spec mengasersi empty state dan ketiadaan seluruh baris sebagai dua `Verifikasi` terpisah per keyword, dan tidak menambah asersi baru di luar Expected.
  - TC-AC-PP-103 tidak menyebut cara mengamati "tidak ada script yang dieksekusi" selain ketiadaan dialog alert; spec memakai pemantau dialog alert dan pengamat eksekusi script sebagai kebutuhan tim FE di Prerequisites.
