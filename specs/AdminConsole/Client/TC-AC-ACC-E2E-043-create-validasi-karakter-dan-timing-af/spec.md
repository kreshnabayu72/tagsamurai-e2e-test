---
id: TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af
title: "Validasi Create: Filter Karakter, Newline, Emoji Fallback, dan Timing Pesan Error (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-78
  - TC-AC-ACC-85
  - TC-AC-ACC-493
  - TC-AC-ACC-494
  - TC-AC-ACC-495
  - TC-AC-ACC-496
  - TC-AC-ACC-497
  - TC-AC-ACC-503
  - TC-AC-ACC-504
  - TC-AC-ACC-505
  - TC-AC-ACC-506
coverage:
  web: automated
---

# Validasi Create: Filter Karakter, Newline, Emoji Fallback, dan Timing Pesan Error (Active-Full)

## Prerequisites

- Mode: FE+BE. Tidak ada Client yang berhasil dibuat; satu-satunya submit (TC-503) diblokir.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-043@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Company Name valid `PT Karakter {runId}-043`.
- Kemampuan teknis: menempel dari clipboard, menekan Tab, dan menginjeksi nilai langsung ke DOM lalu memicu event input.
- Cleanup: tidak ada data yang perlu dihapus.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`

### TC-78: Emoji pada Company Name diblok saat ketik dan tempel

2. Ketik `PT 😀 Uji` ke field Company Name
3. Verifikasi emoji tidak masuk ke field Company Name (diblok saat ketik)
4. Kosongkan Company Name
5. Tempel `PT 😀 Uji` dari clipboard ke field Company Name
6. Verifikasi emoji tidak masuk ke field Company Name (diblok saat tempel)
7. Verifikasi tidak ada pesan error di bawah Company Name
8. Verifikasi popup tetap terbuka
9. Verifikasi tidak ada toast
10. Kosongkan Company Name

### TC-495: Newline pada Company Name

11. Tempel `PT Nusa\nUji` (dengan baris baru) dari clipboard ke field Company Name
12. Verifikasi field Company Name tetap satu baris (baris baru tidak tersisip)
13. Verifikasi tidak ada pesan error di bawah Company Name
14. Verifikasi popup tetap terbuka
15. Verifikasi tidak ada toast
16. Kosongkan Company Name

### TC-496: Tab pada Company Name

17. Klik field Company Name lalu ketik `PT Kontrol`
18. Tekan tombol Tab
19. Verifikasi fokus berpindah ke field Client Code
20. Verifikasi Company Name tetap `PT Kontrol`
21. Verifikasi tidak ada pesan error di bawah Company Name
22. Kosongkan Company Name

### TC-85: Newline pada PIC Name

23. Tempel `Rina\nKartika` (dengan baris baru) dari clipboard ke field PIC Name
24. Verifikasi field PIC Name tetap satu baris (baris baru tidak tersisip)
25. Verifikasi tidak ada pesan error di bawah PIC Name
26. Verifikasi popup tetap terbuka
27. Verifikasi tidak ada toast
28. Kosongkan PIC Name

### TC-493: Emoji pada First Name

29. Ketik `Budi 😀` ke field First Name Default User
30. Verifikasi emoji tidak masuk ke field First Name (diblok saat ketik)
31. Kosongkan field First Name
32. Tempel `Budi 😀` dari clipboard ke field First Name
33. Verifikasi emoji tidak masuk ke field First Name (diblok saat tempel)
34. Verifikasi tidak ada pesan error di bawah First Name
35. Verifikasi popup tetap terbuka
36. Verifikasi tidak ada toast
37. Kosongkan field First Name

### TC-494: Newline pada Last Name

38. Tempel `Santoso\nPutra` (dengan baris baru) dari clipboard ke field Last Name Default User
39. Verifikasi field Last Name tetap satu baris (baris baru tidak tersisip)
40. Verifikasi tidak ada pesan error di bawah Last Name
41. Verifikasi popup tetap terbuka
42. Verifikasi tidak ada toast
43. Kosongkan field Last Name

### TC-497: Emoji yang lolos filter input ditolak dengan pesan fallback

44. Injeksi `PT 😀 Uji` langsung ke DOM field Company Name lalu picu event input
45. Verifikasi pesan error inline Company Name: "Company name contains invalid characters" muncul langsung
46. Injeksi `Rina 😀` langsung ke DOM field PIC Name lalu picu event input
47. Verifikasi pesan error inline PIC Name: "PIC name contains invalid characters" muncul langsung
48. Injeksi `Budi 😀` langsung ke DOM field First Name lalu picu event input
49. Verifikasi pesan error inline First Name: "First name contains invalid characters" muncul langsung
50. Injeksi `Santoso 😀` langsung ke DOM field Last Name lalu picu event input
51. Verifikasi pesan error inline Last Name: "Last name contains invalid characters" muncul langsung
52. Verifikasi popup tetap terbuka
53. Verifikasi tidak ada toast
54. Kosongkan Company Name, PIC Name, First Name, dan Last Name

### TC-504: Error format PIC Email muncul setelah fokus berpindah

55. Ketik `pic@` ke field PIC Email tanpa memindahkan fokus
56. Verifikasi tidak ada pesan error di bawah PIC Email
57. Klik field PIC Phone
58. Verifikasi pesan error inline di bawah PIC Email: "Enter a valid email address"
59. Kosongkan PIC Email

### TC-505: Error batas karakter PIC Name muncul langsung

60. Ketik 121×`A` ke field PIC Name tanpa memindahkan fokus dan tanpa klik `[Submit]`
61. Verifikasi pesan error inline di bawah PIC Name: "Max. 120 characters" muncul langsung saat karakter ke-121 diketik
62. Kosongkan PIC Name

### TC-506: Error batas minimum PIC Phone muncul langsung

63. Ketik `123` ke field PIC Phone tanpa memindahkan fokus dan tanpa klik `[Submit]`
64. Verifikasi pesan error inline di bawah PIC Phone: "Min. 4 characters" muncul langsung setelah digit ke-3 diketik
65. Kosongkan PIC Phone

### TC-503: Error wajib diisi Company Name hanya muncul setelah [Submit]

66. Klik field Company Name lalu klik field Client Code tanpa mengetik
67. Verifikasi tidak ada pesan error di bawah Company Name
68. Isi PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Company Name tetap kosong
69. Pilih Group "Area Jakarta" pada tree Select Group
70. Klik `[Submit]`
71. Verifikasi pesan error inline di bawah Company Name: "Company name must not be empty"
72. Verifikasi popup tetap terbuka
73. Verifikasi tidak ada toast sukses "Success, client has been created."

### Penutup

74. Klik `[✕]` di header popup
75. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
76. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 80 langkah): satu form Create, satu role, satu kelas (validasi input diblokir, tanpa data tercipta); tiap blok berdiri sendiri dan form tidak pernah di-submit kecuali TC-503. Satu pembukaan form dipakai berulang dengan field dikosongkan di antara kasus (prinsip 13, halaman yang sama dipakai berulang).
- Langkah penghubung (S-03): pengosongan field di akhir tiap blok, pengisian field valid dan pemilihan Group "Area Jakarta" sebelum TC-503; penutup `[✕]`, dialog `Unsaved Changes`, `[Leave]` (S-08).
- Temuan untuk QA:
  - TC-503: Company Name sengaja kosong sehingga "tidak ada Client dibuat" tidak dapat dibuktikan lewat Search; spec hanya memverifikasi popup tetap terbuka dan tidak ada toast sukses.
  - TC-78, TC-495, TC-85, TC-493, TC-494: Expected hanya menyebut "tidak ada toast" tanpa toast pembanding; spec mengasersi absence sesudah aksi ketik atau tempel pada form yang sudah dimuat (popup terbuka sebagai anchor).
