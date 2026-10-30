---
id: TC-GS-DIV-E2E-017-create-auto-generate-code-dedup-suffix-dan-truncation
title: "Auto-Generate Code: Dedup Suffix Angka dan Pemotongan 15 Karakter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-58
  - TC-GS-DIV-59
  - TC-GS-DIV-60
  - TC-GS-DIV-61
coverage:
  web: automated
---

# Auto-Generate Code: Dedup Suffix Angka dan Pemotongan 15 Karakter

## Prerequisites

- Mode: FE+BE (backend nyata; Code di-generate server dan keunikannya dicek ke backend).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tidak diubah spec): Division `Human Resources` dengan Code `HR` (in-use Login User aktif) sebagai Code yang sudah dipakai untuk TC-GS-DIV-58; 5 Division Pre-setup lain sebagai latar tabel.
- Data dinamis (D-04, dibuat lewat UI oleh spec ini; Name literal tanpa suffix `{runId}` karena Code hasil auto-generate yang diasersi bergantung pada token Name, bagian 5 konvensi dan S-12; penghapusan sisa berdasar Name literal, bukan berdasar Code saja; suite berjalan serial), Code dikosongkan:
  - `Hotel Reservation` menghasilkan `HR2` (TC-GS-DIV-58)
  - `Hospital Records` menghasilkan `HR3` (TC-GS-DIV-59; Code `HR` dan `HR2` sudah dipakai, `HR2` dari TC-GS-DIV-58 di spec yang sama)
  - `A B C D E F G H I J K L M N O P` menghasilkan `ABCDEFGHIJKLMNO` (TC-GS-DIV-60)
  - `A B C D E F G H I J K L M N O Q` menghasilkan `ABCDEFGHIJKLMN2` (TC-GS-DIV-61; Code `ABCDEFGHIJKLMNO` sudah dipakai dari TC-GS-DIV-60 di spec yang sama)
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: hapus lewat API sisa Division run sebelumnya bernama `Hotel Reservation`, `Hospital Records`, `A B C D E F G H I J K L M N O P`, dan `A B C D E F G H I J K L M N O Q`, sehingga Code `HR2`, `HR3`, `ABCDEFGHIJKLMNO`, dan `ABCDEFGHIJKLMN2` belum dipakai Division lain.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API keempat Division di atas bila masih ada.
- Kemampuan teknis: Search pada tabel; pembacaan teks sel tabel.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah.

## Test Steps

### Persiapan sesi form

1. Klik `[+ Division]`
2. Centang checkbox `Stay on this form after submitting` agar form tetap terbuka untuk Create berikutnya

### TC-GS-DIV-58: Auto-generate Code: kandidat bentrok ditambah suffix angka 2

3. Isi Division Name `Hotel Reservation` dengan Code dibiarkan kosong
4. Klik `[Submit]`
5. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-59: Auto-generate Code: suffix angka berlanjut ke 3 saat HR dan HR2 dipakai

6. Isi Division Name `Hospital Records` dengan Code dibiarkan kosong
7. Klik `[Submit]`
8. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-60: Auto-generate Code: kandidat dipotong maksimum 15 karakter

9. Isi Division Name `A B C D E F G H I J K L M N O P` dengan Code dibiarkan kosong
10. Klik `[Submit]`
11. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-61: Auto-generate Code: kandidat 15 karakter bentrok, basis dipotong agar total 15 karakter dengan suffix

12. Isi Division Name `A B C D E F G H I J K L M N O Q` dengan Code dibiarkan kosong
13. Klik `[Submit]`
14. Verifikasi toast sukses: `Success, division has been created.`

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-DIV-58, 59, 60, 61)

15. Klik `✕` untuk menutup form yang sudah kosong
16. Ketik Search `Hotel Reservation`, tekan Enter
17. Verifikasi tabel menampilkan Code `HR2` pada baris `Hotel Reservation` (TC-GS-DIV-58)
18. Ganti isi kotak search dengan `Hospital Records`, tekan Enter
19. Verifikasi tabel menampilkan Code `HR3` pada baris `Hospital Records` (TC-GS-DIV-59)
20. Ganti isi kotak search dengan `A B C D E F G H I J K L M N O P`, tekan Enter
21. Verifikasi tabel menampilkan Code `ABCDEFGHIJKLMNO` pada baris `A B C D E F G H I J K L M N O P` (TC-GS-DIV-60)
22. Ganti isi kotak search dengan `A B C D E F G H I J K L M N O Q`, tekan Enter
23. Verifikasi tabel menampilkan Code `ABCDEFGHIJKLMN2` pada baris `A B C D E F G H I J K L M N O Q` (TC-GS-DIV-61)
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec sama dengan urutan TC sumber (58, 59, 60, 61); TC-GS-DIV-59 sesudah TC-GS-DIV-58 dan TC-GS-DIV-61 sesudah TC-GS-DIV-60 sesuai kolom Dependensi TC sumber. Keempat Create berbagi satu sesi modal dengan Stay tercentang (prinsip 8 konvensi), sehingga hanya satu kali `[+ Division]` dibuka dan satu kejadian menutup form.
- Asersi "tabel menampilkan Code ..." milik keempat TC ditaruh sesudah form ditutup (langkah 16 sampai 23) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung sesudah tiap Submit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mengatur mode sesi modal, bukan asersi TC), langkah 15 (menutup form kosong sesudah Submit terakhir, sehingga tidak ada dialog `Unsaved Changes`), langkah 16, 18, 20, dan 22 (Search agar baris target tampil di halaman aktif), dan langkah 24 (mengosongkan Search).
- Langkah "Biarkan Code kosong" pada tiap TC sumber ditulis dalam langkah pengisian Division Name (Code dibiarkan kosong); sesudah Submit dengan Stay tercentang, field Code sudah kosong.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA: precondition TC-GS-DIV-59 ("Code `HR` dan `HR2` sudah dipakai (TC-GS-DIV-58)") dan TC-GS-DIV-61 bergantung pada tidak adanya Division lain dengan Code `HR2`, `HR3`, `ABCDEFGHIJKLMNO`, atau `ABCDEFGHIJKLMN2` di environment; TC tidak memberi cara memastikannya, sehingga spec membersihkan Division bernama sama lewat API di hook `before` dan mengandalkan suite serial bagi Division spec lain.
