---
id: TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter
title: "Auto-Generate Code: Inisial Token, Numerik, Alfanumerik Campuran, dan Delimiter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-50
  - TC-GS-DIV-51
  - TC-GS-DIV-52
  - TC-GS-DIV-53
  - TC-GS-DIV-54
coverage:
  web: automated
---

# Auto-Generate Code: Inisial Token, Numerik, Alfanumerik Campuran, dan Delimiter

## Prerequisites

- Mode: FE+BE (backend nyata; Code di-generate server dan keunikannya dicek ke backend).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury) sebagai latar tabel; tidak diubah spec ini.
- Data dinamis (D-04, dibuat lewat UI oleh spec ini; Name literal tanpa suffix `{runId}` karena Code hasil auto-generate yang diasersi bergantung pada token Name, bagian 5 konvensi dan S-12; penghapusan sisa berdasar Name literal, bukan berdasar Code saja; suite berjalan serial), Code dikosongkan:
  - `Customer Care` menghasilkan `CC` (TC-GS-DIV-50)
  - `Region 5` menghasilkan `R5` (TC-GS-DIV-51)
  - `Branch 123` menghasilkan `B123` (TC-GS-DIV-52)
  - `A1 Logistics` menghasilkan `AL` (TC-GS-DIV-53)
  - `Customer-Care/Support_24` menghasilkan `CCS24` (TC-GS-DIV-54; Code `CC` sudah dipakai `Customer Care` dari TC-GS-DIV-50 di spec yang sama)
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: hapus lewat API sisa Division run sebelumnya bernama `Customer Care`, `Region 5`, `Branch 123`, `A1 Logistics`, dan `Customer-Care/Support_24`, sehingga Code `CC`, `R5`, `B123`, `AL`, dan `CCS24` belum dipakai Division lain (precondition TC-GS-DIV-50).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API kelima Division di atas bila masih ada.
- Kemampuan teknis: Search pada tabel; pembacaan teks sel tabel.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah.

## Test Steps

### Persiapan sesi form

1. Klik `[+ Division]`
2. Centang checkbox `Stay on this form after submitting` agar form tetap terbuka untuk Create berikutnya

### TC-GS-DIV-50: Auto-generate Code: dua token alfabetik menjadi inisial

3. Isi Division Name `Customer Care` dengan Code dibiarkan kosong
4. Klik `[Submit]`
5. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-51: Auto-generate Code: token numerik murni diteruskan utuh

6. Isi Division Name `Region 5` dengan Code dibiarkan kosong
7. Klik `[Submit]`
8. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-52: Auto-generate Code: token numerik beberapa digit diteruskan utuh

9. Isi Division Name `Branch 123` dengan Code dibiarkan kosong
10. Klik `[Submit]`
11. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-53: Auto-generate Code: token alfanumerik campuran hanya karakter pertama

12. Isi Division Name `A1 Logistics` dengan Code dibiarkan kosong
13. Klik `[Submit]`
14. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-54: Auto-generate Code: pemisah hyphen, garis miring, dan underscore memecah token

15. Isi Division Name `Customer-Care/Support_24` dengan Code dibiarkan kosong
16. Klik `[Submit]`
17. Verifikasi toast sukses: `Success, division has been created.`

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-DIV-50, 51, 52, 53, 54)

18. Klik `✕` untuk menutup form yang sudah kosong
19. Ketik Search `Customer Care`, tekan Enter
20. Verifikasi tabel menampilkan Code `CC` pada baris `Customer Care` (TC-GS-DIV-50)
21. Ganti isi kotak search dengan `Region 5`, tekan Enter
22. Verifikasi tabel menampilkan Code `R5` pada baris `Region 5` (TC-GS-DIV-51)
23. Ganti isi kotak search dengan `Branch 123`, tekan Enter
24. Verifikasi tabel menampilkan Code `B123` pada baris `Branch 123` (TC-GS-DIV-52)
25. Ganti isi kotak search dengan `A1 Logistics`, tekan Enter
26. Verifikasi tabel menampilkan Code `AL` pada baris `A1 Logistics` (TC-GS-DIV-53)
27. Ganti isi kotak search dengan `Customer-Care/Support_24`, tekan Enter
28. Verifikasi tabel menampilkan Code `CCS24` pada baris `Customer-Care/Support_24` (TC-GS-DIV-54)
29. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec sama dengan urutan TC sumber (50, 51, 52, 53, 54); TC-GS-DIV-54 sesudah TC-GS-DIV-50 sesuai kolom Dependensi TC sumber. Kelima Create berbagi satu sesi modal dengan Stay tercentang (prinsip 8 konvensi), sehingga hanya satu kali `[+ Division]` dibuka dan satu kejadian menutup form.
- Asersi "tabel menampilkan Code ..." milik kelima TC ditaruh sesudah form ditutup (langkah 19 sampai 28) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung sesudah tiap Submit. Search dipakai per Division karena Name literal tidak berbagi token pencarian.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mengatur mode sesi modal, bukan asersi TC), langkah 18 (menutup form kosong sesudah Submit terakhir, sehingga tidak ada dialog `Unsaved Changes`), langkah 19, 21, 23, 25, dan 27 (Search agar baris target tampil di halaman aktif), dan langkah 29 (mengosongkan Search).
- Langkah "Biarkan Code kosong" pada tiap TC sumber ditulis dalam langkah pengisian Division Name (Code dibiarkan kosong); sesudah Submit dengan Stay tercentang, field Code sudah kosong.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA: precondition TC-GS-DIV-50 ("Code `CC` belum dipakai Division lain") dan Code `R5`, `B123`, `AL`, `CCS24` bergantung pada tidak adanya Division lain dengan Code yang sama di environment; TC tidak memberi cara memastikannya, sehingga spec membersihkan Division bernama sama lewat API di hook `before` dan mengandalkan suite serial bagi Division spec lain.
