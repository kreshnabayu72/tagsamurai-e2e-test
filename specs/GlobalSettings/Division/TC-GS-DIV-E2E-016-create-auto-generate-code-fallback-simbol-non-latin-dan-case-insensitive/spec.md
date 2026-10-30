---
id: TC-GS-DIV-E2E-016-create-auto-generate-code-fallback-simbol-non-latin-dan-case-insensitive
title: "Auto-Generate Code: Fallback 6 Karakter, DIV pada Simbol dan Non-Latin, dan Unik Case-Insensitive"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-55
  - TC-GS-DIV-56
  - TC-GS-DIV-57
  - TC-GS-DIV-62
coverage:
  web: automated
---

# Auto-Generate Code: Fallback 6 Karakter, DIV pada Simbol dan Non-Latin, dan Unik Case-Insensitive

## Prerequisites

- Mode: FE+BE (backend nyata; Code di-generate server dan keunikannya dicek ke backend).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tidak diubah spec): Division `Legal` dengan Code `LGL` (kandidat Code TC-GS-DIV-62 bentrok dengannya); 5 Division Pre-setup lain sebagai latar tabel.
- Data dinamis (D-04, dibuat lewat UI oleh spec ini; Name literal tanpa suffix `{runId}` karena Code hasil auto-generate yang diasersi bergantung pada token Name, bagian 5 konvensi dan S-12; penghapusan sisa berdasar Name literal, bukan berdasar Code saja; suite berjalan serial), Code dikosongkan:
  - `Research` menghasilkan `RESEAR` (TC-GS-DIV-55)
  - `!!! ###` menghasilkan `DIV` (TC-GS-DIV-56)
  - `日本支店` menghasilkan `DIV2` (TC-GS-DIV-57; Code `DIV` sudah dipakai `!!! ###` dari TC-GS-DIV-56 di spec yang sama)
  - `Local Government Liaison` menghasilkan `LGL2` (TC-GS-DIV-62)
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: hapus lewat API sisa Division run sebelumnya bernama `Research`, `!!! ###`, `日本支店`, dan `Local Government Liaison`, sehingga Code `RESEAR`, `DIV`, `DIV2`, dan `LGL2` belum dipakai Division lain.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API keempat Division di atas bila masih ada.
- Kemampuan teknis: mengetik karakter non-Latin (`日本支店`) dan simbol; Search pada tabel; pembacaan teks sel tabel.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah.

## Test Steps

### Persiapan sesi form

1. Klik `[+ Division]`
2. Centang checkbox `Stay on this form after submitting` agar form tetap terbuka untuk Create berikutnya

### TC-GS-DIV-55: Auto-generate Code: kandidat kurang dari 2 karakter memakai 6 karakter alfanumerik pertama

3. Isi Division Name `Research` dengan Code dibiarkan kosong
4. Klik `[Submit]`
5. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-56: Auto-generate Code: Name tanpa huruf atau angka ASCII memakai DIV

6. Isi Division Name `!!! ###` dengan Code dibiarkan kosong
7. Klik `[Submit]`
8. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-57: Auto-generate Code: Name non-Latin memakai DIV lalu dedup suffix

9. Isi Division Name `日本支店` dengan Code dibiarkan kosong
10. Klik `[Submit]`
11. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-62: Auto-generate Code dihitung unik tanpa membedakan huruf besar kecil

12. Isi Division Name `Local Government Liaison` dengan Code dibiarkan kosong
13. Klik `[Submit]`
14. Tunggu aksi selesai (field Division Name kembali kosong dan `[Submit]` aktif)

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-DIV-55, 56, 57, 62)

15. Klik `✕` untuk menutup form yang sudah kosong
16. Ketik Search `Research`, tekan Enter
17. Verifikasi tabel menampilkan Code `RESEAR` pada baris `Research` (TC-GS-DIV-55)
18. Ganti isi kotak search dengan `!!! ###`, tekan Enter
19. Verifikasi tabel menampilkan Code `DIV` pada baris `!!! ###` (TC-GS-DIV-56)
20. Ganti isi kotak search dengan `日本支店`, tekan Enter
21. Verifikasi tabel menampilkan Code `DIV2` pada baris `日本支店` (TC-GS-DIV-57)
22. Ganti isi kotak search dengan `Local Government Liaison`, tekan Enter
23. Verifikasi Code hasil auto-generate `Local Government Liaison` adalah `LGL2` karena kandidat `LGL` bentrok dengan Code `LGL` yang sudah ada (TC-GS-DIV-62)
24. Verifikasi tabel menampilkan Code `LGL2` pada baris `Local Government Liaison` (TC-GS-DIV-62)
25. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec sama dengan urutan TC sumber (55, 56, 57, 62); TC-GS-DIV-57 sesudah TC-GS-DIV-56 sesuai kolom Dependensi TC sumber. Keempat Create berbagi satu sesi modal dengan Stay tercentang (prinsip 8 konvensi), sehingga hanya satu kali `[+ Division]` dibuka dan satu kejadian menutup form.
- Asersi "tabel menampilkan Code ..." milik keempat TC ditaruh sesudah form ditutup (langkah 16 sampai 24) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung sesudah Submit (kecuali TC-GS-DIV-62, yang tidak memuat toast pada Expected Result).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mengatur mode sesi modal, bukan asersi TC), langkah 14 (menunggu Create TC-GS-DIV-62 selesai, karena TC itu tanpa Expected penyelesaian dan icon `[✕]` ikut disabled selama Saving), langkah 15 (menutup form kosong sesudah Submit terakhir, sehingga tidak ada dialog `Unsaved Changes`), langkah 16, 18, 20, dan 22 (Search agar baris target tampil di halaman aktif), dan langkah 25 (mengosongkan Search).
- Langkah "Biarkan Code kosong" pada tiap TC sumber ditulis dalam langkah pengisian Division Name (Code dibiarkan kosong); sesudah Submit dengan Stay tercentang, field Code sudah kosong.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-62 Expected a menyatakan bahwa kandidat `LGL` bentrok sehingga Code menjadi `LGL2`, yang merupakan penjelasan mekanisme dan bukan keadaan UI tersendiri; langkah 23 mengasersi hasilnya (`LGL2`) dan langkah 24 mengasersi tampilan tabel sesuai Expected b.
  - TC-GS-DIV-62 tidak mencantumkan toast sukses pada Expected Result; spec tidak mengasersi toast untuk TC itu.
  - Nama `日本支店` (TC-GS-DIV-57) hanya dapat ditemukan lewat Search bila Search mendukung karakter non-Latin; TC tidak menyatakannya, spec mengikuti TC.
