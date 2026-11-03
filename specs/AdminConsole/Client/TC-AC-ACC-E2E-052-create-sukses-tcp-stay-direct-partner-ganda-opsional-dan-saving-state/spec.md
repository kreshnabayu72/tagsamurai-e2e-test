---
id: TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state
title: "Create Client oleh Total Control: Stay on this Form, Direct, Dua Partner, Field Opsional, dan Saving State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-71
  - TC-AC-ACC-67
  - TC-AC-ACC-70
  - TC-AC-ACC-490
  - TC-AC-ACC-491
  - TC-AC-ACC-749
coverage:
  web: automated
---

# Create Client oleh Total Control: Stay on this Form, Direct, Dua Partner, Field Opsional, dan Saving State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-052@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis (nama bersuffix): `PT Stay Satu {runId}-052`, `PT Mandiri Sentosa {runId}-052` (Position `IT Manager`), `PT Dua Partner {runId}-052` (Partner dipilih berurutan CV Mitra Lestari lalu CV Mitra Sejati), `PT Tanpa Opsional {runId}-052`, `PT Lengkap Uji {runId}-052` (Client Code literal `OPT-017`, Company Email `info@ptlengkapuji.qwertysystem.net`, Industry `Technology`, Website `www.ptlengkapuji.co.id`, Fax `021-5550199`, PIC Phone `081234567890`), `PT Uji Penyimpanan {runId}-052` (Group `Regional Timur`). Hook `before` menghapus lewat API sisa Client berkode `OPT-017`.
- Kemampuan teknis: menahan response request Create (throttle jaringan) pada TC-749; menyimpan dan menghapus preferensi Column Visibility (pemulihan: hapus preferensi kolom di browser pada hook `after`).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`
2. Centang checkbox "Stay on this form after submitting"

### TC-71: Stay on this form

3. Isi Company Name `PT Stay Satu {runId}-052`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Area Jakarta"
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, client has been created."
6. Verifikasi popup tetap terbuka dengan form kosong
7. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang

### TC-67: Create Direct oleh Principal dengan Position

8. Isi Company Name `PT Mandiri Sentosa {runId}-052`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Partner dikosongkan, Position `IT Manager`
9. Verifikasi field Select Group tampil (wajib)
10. Pilih Group "Cabang Menteng" pada tree Select Group
11. Verifikasi Group "Cabang Menteng" terpilih
12. Klik `[Submit]`
13. Verifikasi toast sukses "Success, client has been created."

### TC-70: Dua Partner, Anchor

14. Isi Company Name `PT Dua Partner {runId}-052`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group tidak diisi
15. Pilih Partner "CV Mitra Lestari" lalu "CV Mitra Sejati"
16. Klik `[Submit]`
17. Verifikasi toast sukses "Success, client has been created."

### TC-490: Create tanpa field opsional

18. Isi Company Name `PT Tanpa Opsional {runId}-052`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Client Code, Company Email, Industry, Website, Fax, PIC Phone, Partner, dan Position dikosongkan; Group "Cabang Menteng"
19. Klik `[Submit]`
20. Verifikasi toast sukses "Success, client has been created."

### TC-491: Create dengan field opsional terisi

21. Isi Company Name `PT Lengkap Uji {runId}-052`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Client Code `OPT-017`, Company Email `info@ptlengkapuji.qwertysystem.net`, Industry `Technology`, Website `www.ptlengkapuji.co.id`, Fax `021-5550199`, PIC Phone `081234567890`, Group "Cabang Menteng"
22. Klik `[Submit]`
23. Verifikasi toast sukses "Success, client has been created."

### TC-749: Saving state tombol Submit

24. Hapus centang checkbox "Stay on this form after submitting"
25. Isi Company Name `PT Uji Penyimpanan {runId}-052`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Regional Timur"
26. Tahan response request Create (throttle jaringan)
27. Klik `[Submit]` lalu lihat popup sebelum response diterima
28. Verifikasi tombol `[Submit]` menampilkan indikator loading dan berstatus disabled
29. Verifikasi tombol `[Clear Field]`, ikon close `[✕]`, serta input Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division disabled
30. Lepas throttle dan tunggu response
31. Verifikasi popup tertutup
32. Verifikasi toast sukses "Success, client has been created."

### Verifikasi hasil di List

33. Ketik Search `PT Mandiri Sentosa {runId}-052`, tekan Enter
34. Verifikasi baris "PT Mandiri Sentosa {runId}-052": Managed By "Direct"
35. Verifikasi baris "PT Mandiri Sentosa {runId}-052": Group "Cabang Menteng"
36. Ketik Search `PT Dua Partner {runId}-052`, tekan Enter
37. Verifikasi baris "PT Dua Partner {runId}-052": Managed By "CV Mitra Lestari" +1 more (Anchor = Partner yang dipilih pertama)
38. Verifikasi baris "PT Dua Partner {runId}-052": Group mengikuti Group Distributor induk Anchor ("Area Jakarta")
39. Ketik Search `PT Tanpa Opsional {runId}-052`, tekan Enter
40. Klik header kolom Actions (`⋯`) lalu centang Company Email, PIC Phone, dan Industry pada dropdown Column Visibility
41. Verifikasi baris "PT Tanpa Opsional {runId}-052": Company Email "—", PIC Phone "—", Industry "—"
42. Klik Company Name `PT Tanpa Opsional {runId}-052` untuk membuka Detail
43. Verifikasi Detail, section Default User: Division "Finance"
44. Verifikasi Detail, section Default User: Position "—"
45. Klik breadcrumb "Client" untuk kembali ke List
46. Klik header kolom Actions (`⋯`) lalu hilangkan centang Company Email, PIC Phone, dan Industry pada dropdown Column Visibility
47. Ketik Search `PT Lengkap Uji {runId}-052`, tekan Enter
48. Verifikasi baris "PT Lengkap Uji {runId}-052" menampilkan Client Code "OPT-017"
49. Klik Company Name `PT Lengkap Uji {runId}-052` untuk membuka Detail
50. Verifikasi Detail menampilkan Client Code "OPT-017", Company Email "info@ptlengkapuji.qwertysystem.net", Industry "Technology", Website "www.ptlengkapuji.co.id", Fax "021-5550199", dan PIC Phone "081234567890"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 65 langkah): satu popup memakai "Stay on this form after submitting" (prinsip 8) untuk lima pembuatan beruntun, lalu satu pembuatan terakhir tanpa Stay (TC-749) menutup popup; satu role, satu kelas (Create sukses). Verifikasi baris List dilakukan sesudah popup tertutup karena List tertutup popup selama Stay aktif.
- Langkah penghubung (S-03): Search nama unik; membuka dan menutup Column Visibility; Client Code literal `OPT-017` mengikuti nilai TC (hook `before` membersihkan sisanya).
- Temuan untuk QA:
  - TC-67 dan TC-70 tidak memakai Stay; spec memakainya untuk efisiensi tanpa mengubah Expected.
  - TC-70 Expected butir b ("Group mengikuti Group Distributor induk Anchor") tidak menyebut nama Group; spec menurunkan "Area Jakarta" dari hierarki Tabel A1 (Group Distributor PT Distribusi Nusantara).
