---
id: TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist
title: "Create Division Sukses: Trim Name, Batas 120/15 Karakter, Code Uppercase, dan Whitelist"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-36
  - TC-GS-DIV-37
  - TC-GS-DIV-43
  - TC-GS-DIV-44
  - TC-GS-DIV-47
coverage:
  web: automated
---

# Create Division Sukses: Trim Name, Batas 120/15 Karakter, Code Uppercase, dan Whitelist

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury) sebagai latar tabel; tidak diubah spec ini.
- Data dinamis (dibuat lewat UI oleh spec ini; Name memakai suffix per run `{runId}-013`, Code memakai nilai literal TC):
  - D-05: input Name `  Internal Affairs {runId}-013  ` (2 spasi di awal dan akhir), Code `IAF`; tersimpan sebagai `Internal Affairs {runId}-013`.
  - D-03: Name 120 karakter huruf yang diakhiri ` {runId}-013` (panjang total termasuk suffix tepat 120, dibangkitkan skrip dari awalan `Divisions of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs`), Code `LONG120`.
  - D-06: Name `Legal Affairs {runId}-013`, input Code ` la-01 ` (spasi di awal dan akhir); tersimpan `LA-01`.
  - D-07: Name `Network Operations {runId}-013`, Code 15 karakter `CODE-15-CHARS-A`.
  - D-08: Name `Plant Maintenance {runId}-013`, input Code `pm-1_a.b`; tersimpan `PM-1_A.B`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: hapus lewat API sisa Division run sebelumnya yang bernama memuat `-013`, supaya Code literal (`IAF`, `LONG120`, `LA-01`, `CODE-15-CHARS-A`, `PM-1_A.B`) tidak bentrok sebagai duplikat.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua Division D-03, D-05, D-06, D-07, dan D-08 yang bernama memuat `{runId}-013` bila masih ada.
- Kemampuan teknis: pengetikan karakter demi karakter dan paste via clipboard (spasi tepi dipertahankan); pembacaan nilai field Code saat mengetik; pembacaan teks sel tabel termasuk spasi; Search pada tabel.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah.

## Test Steps

### Persiapan sesi form

1. Klik `[+ Division]`
2. Centang checkbox `Stay on this form after submitting` agar form tetap terbuka untuk Create berikutnya

### TC-GS-DIV-36: Division Name dengan spasi depan dan belakang disimpan ter-trim

3. Isi Division Name `  Internal Affairs {runId}-013  ` dan Code `IAF` (D-05)
4. Klik `[Submit]`
5. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-37: Division Name tepat 120 karakter berhasil disimpan

6. Isi Division Name 120 karakter (D-03, total termasuk suffix ` {runId}-013`) dan Code `LONG120`
7. Verifikasi tidak ada pesan error pada field Division Name
8. Klik `[Submit]`
9. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-43: Create dengan Code manual huruf kecil disimpan uppercase dan ter-trim

10. Isi Division Name `Legal Affairs {runId}-013` dan ketik Code ` la-01 ` (D-06)
11. Verifikasi Code berubah menjadi huruf besar otomatis saat mengetik
12. Klik `[Submit]`
13. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-44: Code tepat 15 karakter berhasil disimpan

14. Isi Division Name `Network Operations {runId}-013` dan Code `CODE-15-CHARS-A` (D-07)
15. Verifikasi tidak ada pesan error pada field Code
16. Klik `[Submit]`
17. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-47: Code dengan huruf, angka, hyphen, underscore, dan titik diterima

18. Isi Division Name `Plant Maintenance {runId}-013` dan Code `pm-1_a.b` (D-08)
19. Verifikasi tidak ada error pada field Code
20. Klik `[Submit]`
21. Verifikasi toast sukses: `Success, division has been created.`

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-DIV-36, 37, 43, 44, 47)

22. Klik `✕` untuk menutup form yang sudah kosong
23. Ketik Search `{runId}-013`, tekan Enter
24. Verifikasi tabel menampilkan Name `Internal Affairs {runId}-013` tanpa spasi di awal dan akhir (TC-GS-DIV-36)
25. Verifikasi baris D-03 tampil dengan Name utuh 120 karakter (TC-GS-DIV-37)
26. Verifikasi baris `Legal Affairs {runId}-013` menampilkan Code `LA-01` tanpa spasi (TC-GS-DIV-43)
27. Verifikasi baris `Network Operations {runId}-013` menampilkan Code `CODE-15-CHARS-A` (TC-GS-DIV-44)
28. Verifikasi baris `Plant Maintenance {runId}-013` menampilkan Code `PM-1_A.B` (TC-GS-DIV-47)
29. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec sama dengan urutan TC sumber (36, 37, 43, 44, 47). Kelima Create berbagi satu sesi modal dengan Stay tercentang (prinsip 8 konvensi); hanya satu kali `[+ Division]` dibuka dan satu kejadian menutup form.
- Asersi "tabel menampilkan ..." milik kelima TC ditaruh sesudah form ditutup (langkah 24 sampai 28) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung sesudah tiap Submit. Satu Search `{runId}-013` menampilkan kelima baris (kurang dari 10 baris, satu halaman).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mengatur mode sesi modal, bukan asersi TC), langkah 22 (menutup form yang kosong sesudah Submit terakhir, sehingga tidak ada dialog `Unsaved Changes`), langkah 23 (Search agar baris target tampil di halaman aktif), dan langkah 29 (mengosongkan Search).
- Spec berada di batas sekitar 35 langkah (29 langkah) karena lima TC Create sukses berkelas harness sama (aksi sukses) dan berbagi satu sesi modal Stay; tiap blok memakai Name bersuffix sendiri, sehingga kegagalan satu Create tidak membuat blok lain kehilangan makna. Pemecahan hanya menambah login, hook, dan pembukaan form.
- Panjang 120 karakter pada TC-GS-DIV-37 sudah termasuk suffix ` {runId}-013`; suffix tidak mengubah batas yang diuji. Name memakai suffix `{runId}-013` supaya tidak bentrok dengan spec lain yang memakai nama dasar yang sama (D-03, D-05, D-06, D-07, D-08 dibuat TC yang sama pada spec lain). Code tetap literal sesuai TC karena nilainya adalah objek uji.
- Temuan untuk QA:
  - TC-GS-DIV-43 Expected a ("Saat mengetik Code berubah menjadi huruf besar otomatis") tidak menyatakan apakah spasi tepi ikut tampil di field; spec hanya mengasersi huruf besar (langkah 11) dan Code tersimpan `LA-01` tanpa spasi (langkah 26).
