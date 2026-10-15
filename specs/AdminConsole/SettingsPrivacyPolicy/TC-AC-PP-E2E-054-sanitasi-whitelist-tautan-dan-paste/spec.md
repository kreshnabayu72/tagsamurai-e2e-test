---
id: TC-AC-PP-E2E-054-sanitasi-whitelist-tautan-dan-paste
title: "Sanitasi Server: Unwrap Tag, Tautan Aman, Whitelist Utuh, dan Paste Berbahaya dari Editor"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-182
  - TC-AC-PP-184
  - TC-AC-PP-185
  - TC-AC-PP-186
coverage:
  web: automated
---

# Sanitasi Server: Unwrap Tag, Tautan Aman, Whitelist Utuh, dan Paste Berbahaya dari Editor

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth): TC-AC-PP-182, 184, dan 185 mengirim Publish langsung lewat klien HTTP dengan token sesi; TC-AC-PP-186 memakai editor UI dengan paste dari clipboard.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`, `Spectra.env.AC_TC_PASSWORD`). Login di hook `before`; token sesi akun ini dipakai klien HTTP. Hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1). Antar TC, dataset dikembalikan ke Riwayat A lewat Fixture BE karena riwayat append-only dan tiap TC mengasumsikan hasil Publish bernomor `Version 4`. Hook `after` mengembalikan dataset ke Riwayat A.
- Kemampuan teknis: klien HTTP; inspeksi DOM (elemen dan atribut konten Modal View); penanganan dialog `alert` browser; kemampuan menaruh HTML ke clipboard browser untuk paste ber-format (TC-AC-PP-186); Fixture BE.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish `Version 4` berulang, sehingga suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung Settings > Privacy Policy | Seluruh TC |
| `kontenSanitasiUnwrap` | `<div><span>Wrapped text</span></div><table><tr><td>Cell text</td></tr></table><h4>Heading four</h4><img src="x.png" alt="Image alt">` | TC-AC-PP-182 |
| `kontenSanitasiTautanAman` | `<a href="http://example.com" target="_self" rel="author">HTTP link</a><a href="https://example.com">HTTPS link</a><a href="mailto:privacy@example.com">Mail link</a>` | TC-AC-PP-184 |
| `kontenSanitasiWhitelist` | `<h1>H1 text</h1><h2>H2 text</h2><h3>H3 text</h3><p>Para<br>second line</p><b>Bold b</b><strong>Strong s</strong><i>Italic i</i><em>Em e</em><u>Under u</u><ul><li>List item</li></ul><ol><li>Number item</li></ol>` | TC-AC-PP-185 |
| `clipboardPasteBerbahaya` | `<img src=x onerror=alert(1)>Pasted <b>text</b>` | TC-AC-PP-186 |

## Test Steps

### TC-AC-PP-182: Tag di luar whitelist di-unwrap, tag dibuang dan teksnya dipertahankan

1. Buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`)
2. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiUnwrap`
3. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
4. Periksa elemen di DOM konten
5. Verifikasi teks `Wrapped text` tampil sebagai teks biasa
6. Verifikasi teks `Cell text` tampil sebagai teks biasa
7. Verifikasi teks `Heading four` tampil sebagai teks biasa
8. Verifikasi tidak ada elemen `div`, `span`, `table`, `h4`, atau `img` di konten
9. Verifikasi tidak ada gambar yang dirender

### TC-AC-PP-184: Tautan dengan skema http, https, mailto dipertahankan dan target serta rel dipaksa aman

10. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
11. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiTautanAman`
12. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
13. Periksa atribut tautan di DOM konten
14. Verifikasi atribut `href` tautan `HTTP link` sama dengan `http://example.com`
15. Verifikasi atribut `href` tautan `HTTPS link` sama dengan `https://example.com`
16. Verifikasi atribut `href` tautan `Mail link` sama dengan `mailto:privacy@example.com`
17. Verifikasi ketiga tautan memiliki `target="_blank"` (nilai `_self` dari pengirim ditimpa)
18. Verifikasi ketiga tautan memiliki `rel="noopener noreferrer"` (nilai `author` dari pengirim ditimpa)

### TC-AC-PP-185: Seluruh tag dalam whitelist dipertahankan setelah sanitasi

19. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
20. Kirim permintaan Publish langsung lewat klien HTTP dengan token sesi dan konten `kontenSanitasiWhitelist`
21. Muat ulang halaman Settings > Privacy Policy dan klik teks tautan `Version 4`
22. Periksa elemen di DOM konten
23. Verifikasi teks `H1 text` tampil sebagai heading level 1
24. Verifikasi teks `H2 text` tampil sebagai heading level 2
25. Verifikasi teks `H3 text` tampil sebagai heading level 3
26. Verifikasi paragraf `Para` dan `second line` tampil dengan pemisah baris
27. Verifikasi teks `Bold b` tampil tebal dalam elemen `b`
28. Verifikasi teks `Strong s` tampil tebal dalam elemen `strong`
29. Verifikasi teks `Italic i` tampil miring dalam elemen `i`
30. Verifikasi teks `Em e` tampil miring dalam elemen `em`
31. Verifikasi teks `Under u` tampil bergaris bawah dalam elemen `u`
32. Verifikasi teks `List item` tampil sebagai daftar bertanda butir dalam elemen `ul`
33. Verifikasi teks `Number item` tampil sebagai daftar bernomor dalam elemen `ol`
34. Verifikasi tidak ada elemen yang hilang dari konten yang dikirim
35. Verifikasi tidak ada elemen yang berubah menjadi teks biasa

### TC-AC-PP-186: Publish dengan konten berbahaya dari editor lewat paste menghasilkan versi bersih tanpa eksekusi script

36. Tutup Modal View dengan `[✕]`, lalu kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman Settings > Privacy Policy
37. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat, lalu klik `[Clear Field]`
38. Tempel (paste) konten HTML dari clipboard `clipboardPasteBerbahaya` ke editor
39. Klik `[Publish New Version]`
40. Klik `[Publish]` pada Dialog Publish Confirm
41. Verifikasi muncul toast sukses "Success, Privacy Policy has been published."
42. Verifikasi tabel menampilkan `Version 4`
43. Klik teks tautan `Version 4`
44. Verifikasi Modal View `Version 4` menampilkan teks `Pasted text`
45. Verifikasi kata `text` pada `Pasted text` tampil tebal
46. Verifikasi tidak ada elemen gambar di konten
47. Verifikasi tidak ada atribut `onerror` di konten
48. Verifikasi tidak ada dialog alert dari browser

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Kelas harness a. Spec ini adalah pasangan dari `TC-AC-PP-E2E-053-sanitasi-elemen-dan-atribut-berbahaya`; pembagian dua spec karena kelompok TC-nya berbeda (whitelist, tautan aman, dan paste dari editor), bukan karena perbedaan kelas; keduanya tidak digabung menjadi satu spec.
- Ukuran spec: 48 langkah (melewati sekitar 35) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Spec tidak dipecah lagi: keempat blok TC mandiri (dataset di-reseed di awal blok lewat Fixture BE), satu kelas harness (a), sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 10, 19, dan 36 (tutup Modal View, kembalikan dataset ke Riwayat A lewat Fixture BE, muat ulang halaman). Fixture BE dipakai karena riwayat append-only dan tiap TC mengharapkan hasil Publish bernomor `Version 4`.
- Urutan TC mengikuti TC sumber (182, 184, 185, 186); TC-AC-PP-186 satu-satunya yang memakai editor UI (paste), tiga TC lain memakai klien HTTP.
- Asersi tambahan atas TC: langkah 42 (`Version 4` tampil di tabel) adalah pengamatan atas Expected a TC-AC-PP-186 ("`Version 4` terbentuk").
- TC-AC-PP-186 beririsan dengan TC-AC-PP-59 dan TC-AC-PP-60 (paste ber-format dan di luar whitelist) yang berada di spec editor; spec ini hanya memakai paste sebagai pemicu sanitasi server.
- Temuan untuk QA:
  - TC memakai "token sesi" untuk klien HTTP tanpa menjelaskan cara memperolehnya dari sesi UI (login API akun Total Control); spec mengasumsikan token sesi akun Total Control disediakan di hook `before`.
  - TC-AC-PP-182 dan TC-AC-PP-185 tidak menyebut bagaimana "pemisah baris" pada `<br>` diamati (visual atau elemen `br`); spec memverifikasi tampilan paragraf dengan pemisah baris.
  - Pada TC-AC-PP-185 elemen `b` dan `strong` (serta `i` dan `em`) dikirim bersamaan sebagai elemen terpisah; TC tidak menyebut apakah sanitasi menyatukan keduanya menjadi satu tag setara (lihat NC-13 normalisasi no-op), sehingga spec mengasersi tampilan tebal/miring dan keberadaan elemen sesuai pengirim.
  - Post Condition TC ("Version 4 tersimpan dengan konten utuh/bersih") tidak punya langkah observasi sendiri dan tidak diasersi di luar Expected.
