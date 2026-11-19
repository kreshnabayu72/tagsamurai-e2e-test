---
id: TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af
title: "Validasi Create: Field Wajib, Format, dan Batas Karakter Diblokir (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-76
  - TC-AC-ACC-77
  - TC-AC-ACC-79
  - TC-AC-ACC-80
  - TC-AC-ACC-81
  - TC-AC-ACC-82
  - TC-AC-ACC-83
  - TC-AC-ACC-84
  - TC-AC-ACC-86
  - TC-AC-ACC-87
  - TC-AC-ACC-88
  - TC-AC-ACC-89
  - TC-AC-ACC-90
  - TC-AC-ACC-91
  - TC-AC-ACC-92
  - TC-AC-ACC-93
  - TC-AC-ACC-97
  - TC-AC-ACC-98
  - TC-AC-ACC-99
  - TC-AC-ACC-101
  - TC-AC-ACC-102
  - TC-AC-ACC-103
  - TC-AC-ACC-104
  - TC-AC-ACC-105
  - TC-AC-ACC-106
  - TC-AC-ACC-107
  - TC-AC-ACC-108
  - TC-AC-ACC-109
  - TC-AC-ACC-110
  - TC-AC-ACC-94
  - TC-AC-ACC-95
  - TC-AC-ACC-96
  - TC-AC-ACC-100
  - TC-AC-ACC-479
  - TC-AC-ACC-480
  - TC-AC-ACC-1044
  - TC-AC-ACC-1046
coverage:
  web: automated
---

# Validasi Create: Field Wajib, Format, dan Batas Karakter Diblokir (Active-Full)

## Prerequisites

- Mode: FE+BE. Tidak ada Client yang berhasil dibuat; semua submit diblokir.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-042@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Company Name valid `PT Validasi {runId}-042`. Default User Email unik per run.
- Tabel Validasi Teks (TC | Field | Nilai uji | Pesan error di bawah field):
  - TC-76 | Company Name | (kosong) | Company name must not be empty
  - TC-77 | Company Name | A×121 | Max. 120 characters
  - TC-79 | Client Code | AB@#12 | Client code contains invalid characters
  - TC-80 | Client Code | ABCDEFGHIJKLMNOP (16 karakter) | Max. 15 characters
  - TC-81 | Company Email | bukan-email | Enter a valid email address
  - TC-82 | Company Email | email 121 karakter (60×`c` + `@` + 43×`x` + `.qwertysystem.net`) | Max. 120 characters
  - TC-83 | PIC Name | (kosong) | PIC name must not be empty
  - TC-84 | PIC Name | A×121 | Max. 120 characters
  - TC-86 | PIC Email | (kosong) | PIC email must not be empty
  - TC-87 | PIC Email | pic@ | Enter a valid email address
  - TC-88 | PIC Email | email 121 karakter (60×`c` + `@` + 43×`x` + `.qwertysystem.net`) | Max. 120 characters
  - TC-89 | PIC Phone | 123 | Min. 4 characters
  - TC-90 | PIC Phone | 1234567890123456 | Max. 15 characters
  - TC-91 | PIC Phone | 08ab1234 | PIC phone contains invalid characters
  - TC-92 | Address | (kosong) | Address must not be empty
  - TC-93 | Address | A×361 | Max. 360 characters
  - TC-97 | Postal Code | (kosong) | Postal code must not be empty
  - TC-98 | Postal Code | 1234567890123456 | Max. 15 characters
  - TC-99 | Postal Code | 12AB5 | Postal code contains invalid characters
  - TC-101 | Default User - First Name | (kosong) | First name must not be empty
  - TC-102 | Default User - First Name | A×121 | Max. 120 characters
  - TC-103 | Default User - Last Name | (kosong) | Last name must not be empty
  - TC-104 | Default User - Last Name | A×121 | Max. 120 characters
  - TC-105 | Default User - Email | (kosong) | Email must not be empty
  - TC-106 | Default User - Email | user@ | Enter a valid email address
  - TC-107 | Default User - Email | email 121 karakter (60×`d` + `@` + 43×`x` + `.qwertysystem.net`) | Max. 120 characters
  - TC-108 | Default User - Division | (kosong) | Division must not be empty
  - TC-109 | Default User - Division | A×121 | Max. 120 characters
  - TC-110 | Default User - Position | A×121 | Max. 120 characters
- Kasus Select (Country, State, City, Select Group) dijalankan berurutan karena State dan City bergantung pada Country; Partner dikosongkan agar Select Group tampil.
- Cleanup: tidak ada data yang perlu dihapus.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`
2. Isi Company Name `PT Validasi {runId}-042`, PIC Name, PIC Email, Address, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; biarkan Partner, Country, State, City, dan Select Group kosong

### TC-94, TC-95, TC-96, TC-100: Field Select

3. Klik `[Submit]`
4. Verifikasi pesan error inline di bawah Country: "Country must not be empty"
5. Verifikasi popup tetap terbuka
6. Verifikasi tidak ada toast sukses "Success, client has been created."
7. Pilih Country "Indonesia" lalu klik `[Submit]`
8. Verifikasi pesan error inline di bawah State: "State must not be empty"
9. Verifikasi popup tetap terbuka
10. Verifikasi tidak ada toast sukses "Success, client has been created."
11. Pilih State "DKI Jakarta" lalu klik `[Submit]`
12. Verifikasi pesan error inline di bawah City: "City must not be empty"
13. Verifikasi popup tetap terbuka
14. Verifikasi tidak ada toast sukses "Success, client has been created."
15. Pilih City "Jakarta Selatan" lalu klik `[Submit]`
16. Verifikasi pesan error inline di bawah Select Group: "Group must not be empty"
17. Verifikasi popup tetap terbuka
18. Verifikasi tidak ada toast sukses "Success, client has been created."
19. Pilih Group "Area Jakarta" pada tree Select Group

### Field teks: tabel Validasi Teks

20. Untuk setiap baris tabel Validasi Teks di Prerequisites, lakukan langkah 21 sampai 26
21. Ganti isi field baris tabel dengan nilai uji (nilai "(kosong)" berarti field dikosongkan)
22. Klik `[Submit]`
23. Verifikasi pesan error inline di bawah field sama dengan kolom Pesan error baris tabel
24. Verifikasi popup tetap terbuka
25. Verifikasi tidak ada toast sukses "Success, client has been created."
26. Kembalikan field ke nilai valid

### TC-479: Website 121 karakter

27. Ketik `https://` + 109×`a` + `.com` (121 karakter) ke field Website tanpa memindahkan fokus
28. Verifikasi pesan error inline di bawah Website: "Max. 120 characters" sebelum `[Submit]`
29. Klik `[Submit]`
30. Verifikasi popup tetap terbuka
31. Verifikasi tidak ada toast sukses "Success, client has been created."
32. Ganti isi Website dengan kosong

### TC-1044: Website bukan format URL

33. Ketik `qwertysystem` ke field Website tanpa memindahkan fokus
34. Verifikasi belum ada pesan error di bawah Website
35. Klik field Fax (fokus keluar dari Website)
36. Verifikasi pesan error inline di bawah Website: "Invalid website URL format"
37. Klik `[Submit]`
38. Verifikasi pesan error Website tetap tampil dan popup tetap terbuka
39. Verifikasi tidak ada toast sukses "Success, client has been created."
40. Ganti isi Website dengan kosong

### TC-480: Fax 31 karakter

41. Ketik 31×`1` ke field Fax tanpa memindahkan fokus
42. Verifikasi pesan error inline di bawah Fax: "Max. 30 characters" sebelum `[Submit]`
43. Klik `[Submit]`
44. Verifikasi popup tetap terbuka
45. Verifikasi tidak ada toast sukses "Success, client has been created."
46. Ganti isi Fax dengan kosong

### TC-1046: Karakter Fax yang tidak diizinkan dibuang

47. Ketik `+62 (21) 555-0100 ext.9` ke field Fax
48. Verifikasi field Fax berisi `+62 (21) 555-0100 9`
49. Ganti isi Fax dengan kosong, lalu paste `021abc5550100😀` ke field Fax
50. Verifikasi field Fax berisi `0215550100`
51. Klik field Website (fokus keluar dari Fax)
52. Verifikasi tidak ada pesan error di bawah Fax
53. Ganti isi Fax dengan kosong

### Penutup

54. Klik `[✕]` di header popup
55. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
56. Klik `[Leave]`
57. Ketik Search `PT Validasi {runId}-042`, tekan Enter
58. Verifikasi tidak ada Client "PT Validasi {runId}-042" yang dibuat (empty state "No results found")

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (setara sekitar 200 langkah setelah ekspansi tabel): satu form Create, satu role, satu dataset, kasus sejenis (validasi diblokir) yang diulang per field dengan parameter di tabel Prerequisites (butir 8b-7); langkah yang diulang adalah langkah 21 sampai 26 dengan 29 baris; tiap baris berdiri sendiri.
- Langkah penghubung (S-03): pengembalian field ke nilai valid (langkah 26), pengosongan Website dan Fax sesudah tiap blok TC-479, TC-1044, TC-480, dan TC-1046, pemilihan Group "Area Jakarta"; penutup form dirty memakai `[✕]`, dialog `Unsaved Changes`, `[Leave]` (S-08).
- "Tidak ada Client dibuat" tiap baris dibuktikan satu kali di akhir lewat Search `PT Validasi {runId}-042` (empty state "No results found" sebagai anchor); tiap baris memverifikasi popup tetap terbuka dan tidak ada toast sukses.
- Kasus Select memakai urutan kumulatif (Country, lalu State, City, Select Group) karena State dan City disabled sampai Country dipilih; pesan error tiap field diasersi saat field itu menjadi satu-satunya field Select yang belum terisi.
- Temuan untuk QA:
  - Langkah TC-76 sampai TC-110 berbunyi "Klik [Submit] atau keluar dari field sesuai timing" tanpa menyebut mana yang berlaku per field; spec memakai `[Submit]` untuk semua baris. Timing per field diuji di spec validasi karakter dan timing (TC-503 sampai TC-506).
  - TC-479 dan TC-480 meminta error muncul sebelum `[Submit]` (langsung saat mengetik); baris TC lain tidak membedakan timing, sehingga asersi timing hanya ditulis untuk kasus yang menyebutnya.
