---
id: TC-AC-PP-E2E-053-sanitasi-elemen-dan-atribut-berbahaya
title: "Sanitasi Server: Penghapusan Script, Atribut Event, Style, dan Tautan Berskema Berbahaya"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-178
  - TC-AC-PP-179
  - TC-AC-PP-180
  - TC-AC-PP-181
  - TC-AC-PP-183
coverage:
  web: automated
---

# Sanitasi Server: Penghapusan Script, Atribut Event, Style, dan Tautan Berskema Berbahaya

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth): Publish dikirim langsung ke endpoint Publish lewat klien HTTP dengan token sesi, lalu hasilnya diperiksa di UI.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`, `Spectra.env.AC_TC_PASSWORD`). Login di hook `before`; token sesi akun ini dipakai klien HTTP. Hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1). Antar TC, dataset dikembalikan ke Riwayat A lewat Fixture BE karena riwayat append-only dan tiap TC mengasumsikan hasil Publish bernomor `Version 4`. Hook `after` mengembalikan dataset ke Riwayat A.
- Kemampuan teknis: klien HTTP (permintaan Publish langsung dengan token sesi); inspeksi DOM (atribut dan elemen konten Modal View); penanganan dialog `alert` browser (pendeteksi dialog); Fixture BE.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish `Version 4` berulang, sehingga suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung Settings > Privacy Policy | Seluruh TC |
| `kontenSanitasiScript` | `<h1>Safe heading</h1><script>alert('x')</script><p>After script</p>` | TC-AC-PP-178 |
| `kontenSanitasiEvent` | `<p onclick="alert(1)">Click me</p><a href="https://example.com" onmouseover="alert(2)">Hover link</a>` | TC-AC-PP-179 |
| `kontenSanitasiStyleClass` | `<p style="color:red" class="danger">Styled text</p>` | TC-AC-PP-180 |
| `kontenSanitasiTagStyle` | `<style>body{display:none}</style><p>Visible text</p>` | TC-AC-PP-181 |
| `kontenSanitasiSkemaTautan` | `<a href="javascript:alert(1)">JS link</a><a href="data:text/html,x">Data link</a><a href="ftp://example.com">FTP link</a>` | TC-AC-PP-183 |

## Test Steps

### TC-AC-PP-178: Tag script dihapus beserta isinya dan publish tetap sukses

1. Buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`)
2. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiScript`
3. Verifikasi respons permintaan sukses (bukan ditolak)
4. Muat ulang halaman Settings > Privacy Policy
5. Verifikasi tabel menampilkan `Version 4`
6. Klik teks tautan `Version 4`
7. Verifikasi Modal View `Version 4` menampilkan heading `Safe heading`
8. Verifikasi Modal View `Version 4` menampilkan paragraf `After script`
9. Verifikasi teks `alert('x')` tidak tampil
10. Verifikasi tidak ada elemen script di DOM konten
11. Verifikasi tidak ada dialog alert dari browser

### TC-AC-PP-179: Atribut event handler dihapus dari semua tag

12. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
13. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiEvent`
14. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
15. Verifikasi teks `Click me` tampil
16. Verifikasi teks `Hover link` tampil
17. Periksa atribut elemen di DOM konten
18. Verifikasi elemen paragraf tidak memiliki atribut `onclick`
19. Verifikasi elemen tautan tidak memiliki atribut `onmouseover`
20. Klik paragraf `Click me`
21. Verifikasi tidak ada dialog alert dari browser setelah klik paragraf
22. Hover tautan `Hover link`
23. Verifikasi tidak ada dialog alert dari browser setelah hover tautan

### TC-AC-PP-180: Atribut style dan class dihapus dari tag yang diizinkan

24. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
25. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiStyleClass`
26. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
27. Periksa atribut elemen di DOM konten
28. Verifikasi teks `Styled text` tampil sebagai paragraf biasa (bukan berwarna merah dari atribut)
29. Verifikasi elemen paragraf tidak memiliki atribut `style`
30. Verifikasi elemen paragraf tidak memiliki atribut `class`

### TC-AC-PP-181: Tag style dihapus beserta isinya

31. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
32. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiTagStyle`
33. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
34. Verifikasi teks `Visible text` tampil
35. Verifikasi halaman tidak disembunyikan
36. Verifikasi teks `body{display:none}` tidak tampil
37. Verifikasi tidak ada elemen style di konten

### TC-AC-PP-183: Tautan dengan skema yang tidak diizinkan kehilangan atribut href dan teks tetap tampil

38. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
39. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiSkemaTautan`
40. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
41. Periksa atribut tautan di DOM konten
42. Verifikasi teks `JS link` tampil
43. Verifikasi teks `Data link` tampil
44. Verifikasi teks `FTP link` tampil
45. Verifikasi ketiga elemen tautan tidak memiliki atribut `href`
46. Klik teks `JS link`
47. Verifikasi tidak ada dialog alert dari browser setelah klik `JS link`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Kelas harness a. Spec ini memakai klien HTTP dan dipisah dari spec sanitasi lain di `TC-AC-PP-E2E-054-sanitasi-whitelist-tautan-dan-paste` (whitelist, tautan aman, dan paste dari editor) karena kelompok TC-nya berbeda (penghapusan elemen/atribut berbahaya vs. pemeliharaan whitelist); keduanya tetap satu kelas (a) dan tidak digabung.
- Ukuran spec: 47 langkah (melewati sekitar 35) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Spec tidak dipecah lagi: kelima blok TC mandiri (dataset di-reseed di awal blok lewat Fixture BE), satu kelas harness (a), sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 12, 24, 31, dan 38 (tutup Modal View, kembalikan dataset ke Riwayat A lewat Fixture BE, muat ulang halaman). Fixture BE dipakai karena riwayat append-only dan setiap TC mengharapkan hasil Publish bernomor `Version 4`.
- Asersi tambahan atas TC: langkah 5 (`Version 4` tampil di tabel) adalah pengamatan atas Expected a "Version 4 terbentuk" dan dibutuhkan karena TC mengamati versi lewat tabel setelah muat ulang.
- Temuan untuk QA:
  - TC memakai "token sesi" tanpa menjelaskan cara klien HTTP memperolehnya dari sesi UI; spec mengasumsikan token sesi akun Total Control di hook `before`.
  - Post Condition TC ("Version 4 tersimpan dengan konten bersih") tidak punya langkah observasi sendiri dan tidak diasersi di luar Expected.
